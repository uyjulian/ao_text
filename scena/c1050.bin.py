from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "Old Man Mors",           # 1
        "Mrs. Perla",             # 2
        "Roy",                    # 3
        "Meiling",                # 4
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21502.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch21500.itc",                   # 06
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(889,     100,     6969,    270,  389,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(4294965146, 100,     7010,    90,   389,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_200",          # 01, 1
        "Function_2_22B",          # 02, 2
        "Function_3_3B3",          # 03, 3
        "Function_4_43C",          # 04, 4
        "Function_5_1BBC",         # 05, 5
        "Function_6_2E19",         # 06, 6
        "Function_7_2FD2",         # 07, 7
        "Function_8_3068",         # 08, 8
        "Function_9_36A0",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_188"),
        (1, "loc_194"),
        (2, "loc_1A0"),
        (3, "loc_1AC"),
        (4, "loc_1B8"),
        (5, "loc_1C4"),
        (6, "loc_1D0"),
        (SWITCH_DEFAULT, "loc_1DC"),
    )


    label("loc_188")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_194")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1FF")

    Return()

    # Function_0_148 end

    def Function_1_200(): pass

    label("Function_1_200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22A")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_200")

    label("loc_22A")

    Return()

    # Function_1_200 end

    def Function_2_22B(): pass

    label("Function_2_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_239")
    Jump("loc_3B2")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C8")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 1020, 0, 3500, 270)
    SetChrPos(0x8, -800, 0, 3500, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288")
    SetChrFlags(0xA, 0x10)

    label("loc_288")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 1040, 4019, 7540, 0)
    SetChrPos(0x9, 1040, 4019, 8540, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3B2")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D6")
    Jump("loc_3B2")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_3B2")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3B2")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_318")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_3B2")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_3B2")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_3B2")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_3B2")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A4")
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)

    label("loc_3A4")

    Jump("loc_3B2")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B2")

    label("loc_3B2")

    Return()

    # Function_2_22B end

    def Function_3_3B3(): pass

    label("Function_3_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_43B")

    Return()

    # Function_3_3B3 end

    def Function_4_43C(): pass

    label("Function_4_43C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584")

    ChrTalk(
        0xFE,
        (
            "While everyday life may have\x01",
            "returned to Crossbell, there's still\x01",
            "a huge mound of other problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because diplomatic relations\x01",
            "have been severed, merchants\x01",
            "everywhere will be out of stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll need to think of a way to\x01",
            "deal with this while keeping in\x01",
            "touch with Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_64E")

    label("loc_584")


    ChrTalk(
        0xFE,
        (
            "While everyday life may have\x01",
            "returned to Crossbell, there's still\x01",
            "a huge mound of other problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll need to think of a way to\x01",
            "deal with this while keeping in\x01",
            "touch with Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E")

    Jump("loc_1BB8")

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm worried for the\x01",
            "safety of the street vendors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they wanted to continue \x01",
            "operating despite martial law no matter \x01",
            "what, and I gave them permission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything were to happen to them,\x01",
            "it will be my responsibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_813")

    label("loc_766")


    ChrTalk(
        0xFE,
        (
            "Hmm, I'm worried for the\x01",
            "safety of the street vendors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything happens to them, I, who\x01",
            "gave them permission to operate under\x01",
            "martial law, will be responsible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_813")

    Jump("loc_1BB8")

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FC")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter's address just now...\x01",
            "I'm concerned about it because I\x01",
            "didn't see Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Elie, do you\x01",
            "know anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...No. Actually, I'm a little\x01",
            "concerned about it myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I see... \x01",
            "That is indeed concerning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any event, now that we've done\x01",
            "the deed, conflict with the two\x01",
            "major powers can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I need to call a meeting of the Merchants\x01",
            "Association to prepare for this emergency...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ABA")

    label("loc_9FC")


    ChrTalk(
        0xFE,
        (
            "Now that we've done the deed, conflict\x01",
            "with the two major powers can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I need to call a meeting of the Merchants\x01",
            "Association to prepare for this emergency...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABA")

    Jump("loc_1BB8")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ACD")
    Jump("loc_1BB8")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBF")

    ChrTalk(
        0xFE,
        (
            "Hmm, for an incident like\x01",
            "this to occur with the\x01",
            "referendum approaching...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we're not careful, it will\x01",
            "make a lot of material for\x01",
            "the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the problem's\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C56")

    label("loc_BBF")


    ChrTalk(
        0xFE,
        (
            "In addition, we're betraying our\x01",
            "weaknesses in terms of public order\x01",
            "to the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the problem's\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C56")

    Jump("loc_1BB8")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(
        0xFE,
        (
            "Yesterday's train accident\x01",
            "was caused by some\x01",
            "unknown monster, they say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I wonder if it's the same\x01",
            "as those strange monsters that\x01",
            "have been spotted recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been more incidents than normal\x01",
            "lately. You all should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E2C")

    label("loc_D75")


    ChrTalk(
        0xFE,
        (
            "I don't know if the monster that\x01",
            "caused the train accident is the\x01",
            "same as those in recent rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been more incidents than normal\x01",
            "lately. You all should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2C")

    Jump("loc_1BB8")

    label("loc_E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E3F")
    Jump("loc_1BB8")

    label("loc_E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E4D")
    Jump("loc_1BB8")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_112D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103F")

    ChrTalk(
        0xFE,
        (
            "The autonomous state of Crossbell independence...\x01",
            "Mayor Dieter has certainly\x01",
            "proposed something drastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, now that influential voices have\x01",
            "risen inside and outside of Crossbell,\x01",
            "it might be a good opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Throughout its long history, Crossbell has \x01",
            "remained under the control of the two major\x01",
            "powers. Crossbell has been losing its pride...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is some resistance to it,\x01",
            "but I'd like us to do everything\x01",
            "possible to regain our independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1128")

    label("loc_103F")


    ChrTalk(
        0xFE,
        (
            "...Oh yes, in a sense to support\x01",
            "the mayor's recent efforts,\x01",
            "a certain plan is proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of a planned cooperation with CNS\x01",
            "the citizens will liven up too. Ladies and\x01",
            "gentlemen, please look forward to the results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1128")

    Jump("loc_1BB8")

    label("loc_112D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206")

    ChrTalk(
        0xFE,
        "The Trade Conference has finally started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We citizens are waiting for\x01",
            "the results to be published\x01",
            "in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I wonder what kind\x01",
            "of conference it will be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1284")

    label("loc_1206")


    ChrTalk(
        0xFE,
        (
            "Normally, I would have liked\x01",
            "to see the conference myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I wonder what kind\x01",
            "of conference it will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1284")

    Jump("loc_1BB8")

    label("loc_1289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(
        0xFE,
        (
            "My grandson Roy has started\x01",
            "to take an interest in the\x01",
            "street vendors' job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I was one back in my day.\x01",
            "Hmm, perhaps it's in the blood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB8")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135E")
    Call(0, 9)
    Jump("loc_13F7")

    label("loc_135E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_13F7")

    ChrTalk(
        0x8,
        (
            "Hmm. Who would have thought\x01",
            "the grandson of a Heiyue\x01",
            "elder would come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, I'd be happy if\x01",
            "he took an interest\x01",
            "in this city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F7")

    Jump("loc_14A7")

    label("loc_13FC")


    ChrTalk(
        0xFE,
        (
            "At the Trade Conference, the\x01",
            "representatives will discuss\x01",
            "mainly economic agreements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of the the Merchants Association\x01",
            "will take notice of their actions too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7")

    Jump("loc_1BB8")

    label("loc_14AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_18BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1716")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C8")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't Lloyd. \x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm...\x01",
            "Is Meiling\x01",
            "at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I thought she returned\x01",
            "just now, but... Maybe she\x01",
            "went off somewhere again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but why not\x01",
            "try asking my wife?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1637")

    label("loc_15C8")


    ChrTalk(
        0xFE,
        (
            "It's for work, right?\x01",
            "I didn't realize my\x01",
            "granddaughter went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe my wife has\x01",
            "heard something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1637")

    Jump("loc_1678")

    label("loc_163C")


    ChrTalk(
        0xFE,
        (
            "Now then, to continue my\x01",
            "Merchants Association work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1678")

    Jump("loc_1712")

    label("loc_167D")


    ChrTalk(
        0xFE,
        (
            "I thought of giving\x01",
            "that Roy a stern\x01",
            "lecture, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing it in the presence\x01",
            "of Meiling would've been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll overlook it for today.\x02",
    )

    CloseMessageWindow()

    label("loc_1712")

    TalkEnd(0xFE)
    Return()

    label("loc_1716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1829")

    ChrTalk(
        0xFE,
        (
            "The budget agreed upon\x01",
            "just before the Cult\x01",
            "incident has been revised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new mayor and new chairman\x01",
            "played a central role in redoing\x01",
            "the budget without conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. They say the city\x01",
            "government is finally heading\x01",
            "in a positive direction.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BA")

    label("loc_1829")


    ChrTalk(
        0xFE,
        (
            "It seems the city government is finally\x01",
            "heading in a positive direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have the new mayor and chairman\x01",
            "to thank for that as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BA")

    Jump("loc_1BB8")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B26")

    ChrTalk(
        0xFE,
        (
            "Oh... If it isn't Lloyd and\x01",
            "Chairman MacDowell's granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been awhile. I'm\x01",
            "glad you're both well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHello, President Mors.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIt has been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYou're the president of the Merchants Association\x01",
            "that unifies the East Street merchants, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh, this person is... (When my\x01",
            "mom was a street vendor, he\x01",
            "helped her a lot, I think.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I see some new faces.\x01",
            "You could say the Support Section\x01",
            "has finally restarted its activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We citizens are expecting\x01",
            "great things from all of you.\x01",
            "Please, do your best for us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 1)
    Jump("loc_1BB8")

    label("loc_1B26")


    ChrTalk(
        0xFE,
        (
            "We're expecting great things from the\x01",
            "Special Support Section from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's anything I can do\x01",
            "for you, please ask me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB8")

    TalkEnd(0xFE)
    Return()

    # Function_4_43C end

    def Function_5_1BBC(): pass

    label("Function_5_1BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE5")
    Call(0, 8)
    Return()

    label("loc_1BE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0D")

    ChrTalk(
        0xFE,
        (
            "We've overcome the President's arrest, \x01",
            "but what will we do from now on...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that's the most important thing\x01",
            "for all of us living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we discuss the problems with everyone, I'm sure\x01",
            "we'll find a good direction in which to proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DDF")

    label("loc_1D0D")


    ChrTalk(
        0xFE,
        (
            "What will we do from now on...?\x01",
            "That's the most important thing \x01",
            "for all of us living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we discuss the problems with everyone, I'm sure\x01",
            "we'll find a good direction in which to proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDF")

    Jump("loc_2E15")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E7A")

    ChrTalk(
        0xFE,
        (
            "There is nothing to be scared of,\x01",
            "because Roy and your grandpa\x01",
            "will protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why there's no\x01",
            "need to worry, Meiling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_1E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_200B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F73")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter's declaration of independence...\x01",
            "I wonder if it was premature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm prepared to accept\x01",
            "that everything in this\x01",
            "world will change, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No... I suppose you\x01",
            "could already say\x01",
            "that about Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2006")

    label("loc_1F73")


    ChrTalk(
        0xFE,
        (
            "All of these sudden\x01",
            "changes are scary to\x01",
            "us elderly folks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell is already at a\x01",
            "point where it's no longer\x01",
            "possible to turn back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2006")

    Jump("loc_2E15")

    label("loc_200B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xFE,
        (
            "If you're looking for my husband, he went to City\x01",
            "Meeting Hall on Merchants Association business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Roy too is helping with\x01",
            "the Charity Event, but...\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2165")

    ChrTalk(
        0xFE,
        (
            "For now anyway, all I can\x01",
            "do is pray to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That no more blood will be\x01",
            "needlessly spilled in Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(
        0xFE,
        (
            "I don't know what has really\x01",
            "been going on lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have got to tell Roy and\x01",
            "Meiling to be careful\x01",
            "when they go out walking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_229B")

    ChrTalk(
        0xFE,
        (
            "Now then... I wonder if\x01",
            "my husband and Meiling\x01",
            "will be back soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I will get tea and sweets\x01",
            "ready while I'm waiting for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_229B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_234A")

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband\x01",
            "is playing with Meiling \x01",
            "around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it has been awhile since he\x01",
            "played with his granddaughter.\x01",
            "I'm very happy for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_234A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23E9")

    ChrTalk(
        0xFE,
        (
            "It seems the Merchants Association\x01",
            "is helping with the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will happen... \x01",
            "I personally have no idea whatsoever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_23E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2496")

    ChrTalk(
        0xFE,
        (
            "My husband has a lot of things to think about\x01",
            "as the Merchants Association President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he is old, \x01",
            "I'd like him not to push\x01",
            "himself too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2638")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259A")

    ChrTalk(
        0xFE,
        (
            "Before, my husband too\x01",
            "was apathetic like Roy and \x01",
            "didn't know what to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roy is trying hard and maybe someday\x01",
            "he will join the Merchants Association...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be pleasant if it\x01",
            "really does turn out that way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2633")

    label("loc_259A")


    ChrTalk(
        0xFE,
        (
            "Roy is trying hard and maybe someday\x01",
            "he will join the Merchants Association...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband will be pleased if it\x01",
            "really does turn out that way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2633")

    Jump("loc_2E15")

    label("loc_2638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2867")

    ChrTalk(
        0x9,
        (
            "My, my, everyone.\x01",
            "You have another cute\x01",
            "kid with you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hm, madam.\x01",
            "I am sorry to intrude.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Uh uh, you're welcome. \x01",
            "You have good manners, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Would you like some tea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Ah, no. I don't\x01",
            "want to overstay\x01",
            "my welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(*giggle*, what perfect social skills.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(I don't know what to say...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_27F9")

    ChrTalk(
        0x104,
        "#00300F(Yeah, no mistakes at all.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_285F")

    label("loc_27F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_282E")

    ChrTalk(
        0x109,
        "#10100F(Yes, no mistakes at all.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_285F")

    label("loc_282E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(
        0x105,
        "#10300F(Yeah, no mistakes at all.)\x02",
    )

    CloseMessageWindow()

    label("loc_285F")

    SetScenarioFlags(0x1DC, 2)
    Jump("loc_28BF")

    label("loc_2867")


    ChrTalk(
        0x9,
        (
            "Uh uh, you really do\x01",
            "have good manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wish Roy would follow your example.\x02",
    )

    CloseMessageWindow()

    label("loc_28BF")

    Jump("loc_2A36")

    label("loc_28C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BF")

    ChrTalk(
        0xFE,
        (
            "My husband's is annoying whenever he\x01",
            "talks about politics. And, it seems he\x01",
            "holds Mayor Dieter in high esteem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, he does run\x01",
            "the world-famous IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he will play an active\x01",
            "role at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A36")

    label("loc_29BF")


    ChrTalk(
        0xFE,
        (
            "My husband holds the new\x01",
            "mayor in high esteem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he will play an active\x01",
            "role at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A36")

    Jump("loc_2E15")

    label("loc_2A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CD4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_END)), "loc_2BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4E")

    ChrTalk(
        0xFE,
        (
            "Roy and Meiling went out\x01",
            "walking in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think they would have\x01",
            "gone that far. Please try\x01",
            "searching the nearby districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Keep an eye for Roy's\x01",
            "green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BF6")

    label("loc_2B4E")


    ChrTalk(
        0xFE,
        (
            "I don't think Roy or Meiling would\x01",
            "have gone that far. Please try\x01",
            "searching the nearby districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Keep an eye for Roy's\x01",
            "green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF6")

    Jump("loc_2C51")

    label("loc_2BFB")


    ChrTalk(
        0xFE,
        (
            "My grandchildren\x01",
            "have returned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll give them\x01",
            "some hot lemonade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C51")

    TalkEnd(0xFE)
    Return()

    label("loc_2C55")


    ChrTalk(
        0xFE,
        (
            "Hmm. The rain isn't too bad,\x01",
            "but it's not letting up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where Roy and\x01",
            "Meiling have gone shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBD")

    ChrTalk(
        0xFE,
        "My my, you all are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FMrs. Perla, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, same here. \x01",
            "I'm glad you're all well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have you met my\x01",
            "husband yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's upstairs, so\x01",
            "please say hello,\x01",
            "if you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 2)
    Jump("loc_2E15")

    label("loc_2DBD")


    ChrTalk(
        0xFE,
        (
            "Have you met my\x01",
            "husband yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's upstairs, so\x01",
            "please say hello,\x01",
            "if you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E15")

    TalkEnd(0xFE)
    Return()

    # Function_5_1BBC end

    def Function_6_2E19(): pass

    label("Function_6_2E19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDD")

    ChrTalk(
        0xFE,
        (
            "Don't worry, grandpa.\x01",
            "I'm sure Mr. Cronk and\x01",
            "the others are all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't go to the City\x01",
            "Meeting Hall right now, so\x01",
            "let's just stay put at home.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F68")

    label("loc_2EDD")


    ChrTalk(
        0xFE,
        (
            "I'm sure Mr. Cronk and\x01",
            "the others are all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't go to the City\x01",
            "Meeting Hall right now, so\x01",
            "let's just stay put at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F68")

    Jump("loc_2FCE")

    label("loc_2F6D")


    ChrTalk(
        0xFE,
        (
            "Yo, thanks for returning\x01",
            "that umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too have got to be more\x01",
            "careful next time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCE")

    TalkEnd(0xFE)
    Return()

    # Function_6_2E19 end

    def Function_7_2FD2(): pass

    label("Function_7_2FD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3028")

    ChrTalk(
        0xFE,
        (
            "Big bro and grandpa\x01",
            "told me to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so scared...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3064")

    label("loc_3028")


    ChrTalk(
        0xFE,
        "*chew, chew*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Big bro, this bread is delicious!\x02",
    )

    CloseMessageWindow()

    label("loc_3064")

    TalkEnd(0xFE)
    Return()

    # Function_7_2FD2 end

    def Function_8_3068(): pass

    label("Function_8_3068")

    EventBegin(0x0)
    Fade(500)
    OP_68(-610, 1000, 9780, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -1400, 20, 9580, 90)
    SetChrPos(0x102, -2470, 0, 10160, 90)
    SetChrPos(0x109, -2700, 30, 8760, 90)
    SetChrPos(0x105, -3840, 30, 9080, 90)
    OP_4B(0x9, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00000FUhm, good morning.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "Oh, good morning. It's rare to\x01",
            "have visitors on a rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes, we had something\x01",
            "to ask you.\x02\x03",
            "#00000FDo you recognize this at all?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Meiling's\x01",
            "umbrella to the madam.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh, that's... \x01",
            "Meiling's umbrella, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You brought it all the way here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Oh, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That child had an umbrella\x01",
            "when she came home from\x01",
            "the bakery, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FUhm, actually....\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that\x01",
            "they are looking for\x01",
            "Momo's umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh my, so that's\x01",
            "what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Poor Momo, what\x01",
            "an unpleasant thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FMadam, do you know where\x01",
            "she might be now?\x02\x03",
            "#10300FLooks like she's\x01",
            "not here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, Meiling went for a\x01",
            "walk with Roy with the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I'm terribly sorry. \x01",
            "Come to think of it, I forgot to\x01",
            "ask where they were going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FHmm, it seems we\x01",
            "passed by each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThey couldn't have gone\x01",
            "far in this rain anyway.\x02\x03",
            "#00104FThey're probably near East Street...\x01",
            "Central Square, Waterfront Area or\x01",
            "Downtown...somewhere around there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, I think you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Keep an eye for Roy's\x01",
            "green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FA green or pink umbrella...\x01",
            "They should be easy to spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRight. Let's begin the search.\x02\x03",
            "#00004FThank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It was nothing.\x01",
            "Please, come visit anytime.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3270, 20, 8130, 225)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x132, 4)
    OP_29(0x6B, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_3068 end

    def Function_9_36A0(): pass

    label("Function_9_36A0")

    EventBegin(0x0)
    Fade(500)
    OP_68(630, 5020, 6780, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x8, 390, 4019, 5600, 0)
    SetChrPos(0x1A2, -600, 4000, 8580, 180)
    SetChrPos(0x101, 390, 4019, 6840, 180)
    SetChrPos(0x102, 390, 4019, 8320, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3738")
    SetChrPos(0x104, 1590, 4019, 8580, 180)
    Jump("loc_3771")

    label("loc_3738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3757")
    SetChrPos(0x109, 1590, 4019, 8580, 180)
    Jump("loc_3771")

    label("loc_3757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3771")
    SetChrPos(0x105, 1590, 4019, 8580, 180)

    label("loc_3771")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        "#12PHmm, if it isn't Lloyd and his colleagues.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_37C4():

        label("loc_37C4")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_37C4")

    QueueWorkItem2(0x8, 1, lambda_37C4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12PAnd that child with you... \x01",
            "He has an Eastern appearance. \x01",
            "I wager he's not from around here.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x1A2, 0x0, 0x7D0, 0x7D0, 0x0)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)
    EndChrThread(0x8, 0x1)

    ChrTalk(
        0x1A2,
        (
            "#6PI see, so you're the Crossbell\x01",
            "Merchants Association President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PMy name is Shing. A man burdened\x01",
            "with the future of "Heiyue".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, "Heiyue" is that Eastern\x01",
            "District company that recently\x01",
            "expanded into Crossbell too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PBurdened with the future, you said.\x01",
            "Could you be related to the Elders Council?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYes. My grandfather is\x01",
            "actually one of the elders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PMr. Mors, do you \x01",
            "know the elders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAh, no. As a trader, I did\x01",
            "some light deals with them,\x01",
            "but never actually met them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, but that was\x01",
            "smart of an elder to\x01",
            "send his grandson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PBut, why are you with\x01",
            "Lloyd and the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FOh, well, there's\x01",
            "various circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PHu hu. These people said they\x01",
            "wanted to show me around the\x01",
            "city no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PIt couldn't be helped,\x01",
            "so I went along with it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3C48")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3BFD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BFD)
    Sleep(50)

    def lambda_3C0D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C0D)
    Sleep(50)

    def lambda_3C1D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C1D)
    Sleep(300)

    ChrTalk(
        0x104,
        "#11P#00306FHey now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3CE9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3CA1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA1)
    Sleep(50)

    def lambda_3CB1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CB1)
    Sleep(50)

    def lambda_3CC1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CC1)
    Sleep(300)

    ChrTalk(
        0x109,
        "#11P#10106FUhhm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3D8D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3D42():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D42)
    Sleep(50)

    def lambda_3D52():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D52)
    Sleep(50)

    def lambda_3D62():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3D62)
    Sleep(300)

    ChrTalk(
        0x105,
        "#11P#10306F*sigh*, oh boy.\x02",
    )

    CloseMessageWindow()

    label("loc_3D8D")


    ChrTalk(
        0x8,
        (
            "#12PHa ha. I don't really get it, but you seem to\x01",
            "be getting along and that's enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PShing, you said? I'd be\x01",
            "happy if you took an\x01",
            "interest in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYes, it's a nice place.\x01",
            "I'll take my leave, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 390, 4019, 8320, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1CA, 0)
    OP_29(0x73, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_9_36A0 end

    SaveToFile()

Try(main)
