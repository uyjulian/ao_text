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
        "Function_5_1B46",         # 05, 5
        "Function_6_2D3C",         # 06, 6
        "Function_7_2EEE",         # 07, 7
        "Function_8_2F8B",         # 08, 8
        "Function_9_358F",         # 09, 9
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E")

    ChrTalk(
        0xFE,
        (
            "While everyday life may have\x01",
            "returned to Crossbell, there's\x01",
            "still a heap of other problems.\x02",
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
    Jump("loc_642")

    label("loc_57E")


    ChrTalk(
        0xFE,
        (
            "While everyday life may have\x01",
            "returned to Crossbell, there's\x01",
            "still a heap of other problems.\x02",
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

    label("loc_642")

    Jump("loc_1B42")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_80D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_756")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm worried for the\x01",
            "safety of the street\x01",
            "vendors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said wanted to continue operating\x01",
            "despite martial law no matter what,\x01",
            "and I gave them permission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything were to\x01",
            "happen to them, I shall\x01",
            "bear the responsibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_808")

    label("loc_756")


    ChrTalk(
        0xFE,
        (
            "Hmm, I'm worried for the\x01",
            "safety of the street\x01",
            "vendors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything happens to them, I, who\x01",
            "gave them permission to operate under\x01",
            "martial law, will bear responsibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808")

    Jump("loc_1B42")

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA")

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
            "Elie, do you know\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...No. Actually, I'm a\x01",
            "little concerned about\x01",
            "it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I see... That is\x01",
            "indeed concerning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any event, now that we've\x01",
            "done the deed, conflict with the\x01",
            "major powers can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I need to call a meeting\x01",
            "of the Merchants Association to\x01",
            "prepare for this emergency...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA4")

    label("loc_9EA")


    ChrTalk(
        0xFE,
        (
            "Now that we've done the deed,\x01",
            "conflict with the major\x01",
            "powers can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I need to call a meeting\x01",
            "of the Merchants Association to\x01",
            "prepare for this emergency...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4")

    Jump("loc_1B42")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AB7")
    Jump("loc_1B42")

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA7")

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
            "If we're not careful, it'll\x01",
            "make a lot of material for\x01",
            "the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the\x01",
            "problem's resolved\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2D")

    label("loc_BA7")


    ChrTalk(
        0xFE,
        (
            "Even at the best of times,\x01",
            "public order is weakened by\x01",
            "the Republic and Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the\x01",
            "problem's resolved\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2D")

    Jump("loc_1B42")

    label("loc_C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(
        0xFE,
        (
            "Yesterday's train\x01",
            "accident was caused by\x01",
            "some unknown monster...\x02",
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
            "There's been more incidents\x01",
            "than normal lately. You all\x01",
            "should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DF9")

    label("loc_D42")


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
            "There's been more incidents\x01",
            "than normal lately. You all\x01",
            "should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF9")

    Jump("loc_1B42")

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E0C")
    Jump("loc_1B42")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E1A")
    Jump("loc_1B42")

    label("loc_E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF5")

    ChrTalk(
        0xFE,
        (
            "Crossbell State independence...\x01",
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
            "Throughout its long history, Crossbell has\x01",
            "remained under the control of the major\x01",
            "powers. Crossbell has been losing its pride...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is some resistance to it, but\x01",
            "I'd like us to do everything\x01",
            "possible to regain our independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E9")

    label("loc_FF5")


    ChrTalk(
        0xFE,
        (
            "...Oh yes, because of the\x01",
            "mayor's recent support, it means\x01",
            "a certain plan is proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of a planned cooperation with Crossbell\x01",
            "News, the citizens have become active. Ladies and\x01",
            "gentlemen, please look forward to the results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E9")

    Jump("loc_1B42")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_124A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C7")

    ChrTalk(
        0xFE,
        (
            "The trade conference has\x01",
            "finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us citizens are waiting for\x01",
            "the results to be published\x01",
            "in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I wonder\x01",
            "what kind of conference\x01",
            "it will be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1245")

    label("loc_11C7")


    ChrTalk(
        0xFE,
        (
            "Normally, I would have\x01",
            "liked to see the\x01",
            "conference myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I wonder\x01",
            "what kind of conference\x01",
            "it will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1245")

    Jump("loc_1B42")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12E6")

    ChrTalk(
        0xFE,
        (
            "My grandson Roy has started\x01",
            "to take an interest in the\x01",
            "street vendors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I was one back in my\x01",
            "day. Hmm, perhaps it's\x01",
            "in the blood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_12E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_145C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131A")
    Call(0, 9)
    Jump("loc_13B0")

    label("loc_131A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_13B0")

    ChrTalk(
        0x8,
        (
            "Hmm. Who would have\x01",
            "thought the grandson of a\x01",
            "Heiyue elder would come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, I'm happy that\x01",
            "he's taken an interest\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B0")

    Jump("loc_1457")

    label("loc_13B5")


    ChrTalk(
        0xFE,
        (
            "At the trade conference, the\x01",
            "representatives will discuss\x01",
            "mainly economic agreements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The members of the\x01",
            "Merchants Association\x01",
            "have taken notice of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1457")

    Jump("loc_1B42")

    label("loc_145C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1856")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156E")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't Lloyd.\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUmm... Is Meiling here?\x02",
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
            "Sorry, but why not try\x01",
            "asking my wife?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15DD")

    label("loc_156E")


    ChrTalk(
        0xFE,
        (
            "It's for work, right? I\x01",
            "didn't realize my\x01",
            "granddaughter went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe my wife has heard\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DD")

    Jump("loc_1619")

    label("loc_15E2")


    ChrTalk(
        0xFE,
        (
            "Now then, to continue my\x01",
            "trade conference work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1619")

    Jump("loc_16AA")

    label("loc_161E")


    ChrTalk(
        0xFE,
        (
            "I thought of giving that\x01",
            "Roy a stern lecture,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was doing that where\x01",
            "Meiling was, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll overlook it for\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AA")

    TalkEnd(0xFE)
    Return()

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C0")

    ChrTalk(
        0xFE,
        (
            "The budget agreed upon\x01",
            "just before the cult\x01",
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
            "Hmm. The say the city\x01",
            "government is finally heading\x01",
            "in a positive direction.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1851")

    label("loc_17C0")


    ChrTalk(
        0xFE,
        (
            "It seems the city government\x01",
            "is finally heading in a\x01",
            "positive direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have the new mayor\x01",
            "and chairman to thank\x01",
            "for that as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1851")

    Jump("loc_1B42")

    label("loc_1856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(
        0xFE,
        (
            "Oh... If it isn't Lloyd\x01",
            "and Chairman MacDowell's\x01",
            "granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while. I'm\x01",
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
        "#00100FIt's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYou're the president of the\x01",
            "Merchants Association that unifies\x01",
            "the East Street merchants, right?\x02",
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
            "Hmm, I see some new faces. You\x01",
            "could say the Support Section\x01",
            "has finally restarted.\x02",
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
    Jump("loc_1B42")

    label("loc_1AAE")


    ChrTalk(
        0xFE,
        (
            "We're expecting great things\x01",
            "from the Special Support\x01",
            "Section going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's anything I\x01",
            "can do for you, please\x01",
            "ask me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B42")

    TalkEnd(0xFE)
    Return()

    # Function_4_43C end

    def Function_5_1B46(): pass

    label("Function_5_1B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B6F")
    Call(0, 8)
    Return()

    label("loc_1B6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8B")

    ChrTalk(
        0xFE,
        (
            "We managed to arrest our\x01",
            "President, but what will\x01",
            "happen now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that's the most\x01",
            "important question for all\x01",
            "of us living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we discuss the problem with\x01",
            "everyone, I'm sure we'll find a\x01",
            "good direction in which to proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D51")

    label("loc_1C8B")


    ChrTalk(
        0xFE,
        (
            "What will happen now? That's\x01",
            "the most important thing for\x01",
            "all of us living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we discuss the problem with\x01",
            "everyone, I'm sure we'll find a\x01",
            "good direction in which to proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D51")

    Jump("loc_2D38")

    label("loc_1D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1DF0")

    ChrTalk(
        0xFE,
        (
            "There's nothing to be scared\x01",
            "of, because Roy and your\x01",
            "grandpa will protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why there's no\x01",
            "need to worry about\x01",
            "Meiling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_1DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE5")

    ChrTalk(
        0xFE,
        (
            "Dieter's declaration of\x01",
            "independence... I wonder\x01",
            "if it was premature.\x02",
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
            "could already say that\x01",
            "about Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F7D")

    label("loc_1EE5")


    ChrTalk(
        0xFE,
        (
            "All of these sudden\x01",
            "changes are scary to us\x01",
            "elderly folks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell is already at a\x01",
            "place where it's no longer\x01",
            "possible to turn back, huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7D")

    Jump("loc_2D38")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2050")

    ChrTalk(
        0xFE,
        (
            "If you're looking for my husband,\x01",
            "he went to the City Meeting Hall\x01",
            "on Merchants Association business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Roy's helping with\x01",
            "the Charity Event, but...\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(
        0xFE,
        (
            "For now anyway, all I\x01",
            "can do is pray to the\x01",
            "goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That no more blood will\x01",
            "be needlessly spilled in\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2172")

    ChrTalk(
        0xFE,
        (
            "I really don't\x01",
            "understand what's been\x01",
            "going lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to tell Roy and\x01",
            "Meiling to be careful\x01",
            "when they go out walking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_220E")

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
            "I think I'll get tea and\x01",
            "sweets ready while I'm\x01",
            "waiting for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_220E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22BA")

    ChrTalk(
        0xFE,
        (
            "I wonder if my husband\x01",
            "is playing with Meiling\x01",
            "around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it's been a while since he\x01",
            "played with his granddaughter.\x01",
            "I'm very happy for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_22BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2358")

    ChrTalk(
        0xFE,
        (
            "It seems the Merchants\x01",
            "Association is helping\x01",
            "with the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will\x01",
            "happen... I personally\x01",
            "have no idea whatsoever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2404")

    ChrTalk(
        0xFE,
        (
            "My husband has a lot of things\x01",
            "to think about as the Merchants\x01",
            "Association president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he is old, I'd\x01",
            "like him not to push\x01",
            "himself too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FF")

    ChrTalk(
        0xFE,
        (
            "Before, my husband and Roy\x01",
            "were apathetic and didn't\x01",
            "know what to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roy will try hard and\x01",
            "maybe someday join the\x01",
            "Merchants Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband will be\x01",
            "pleased if it really\x01",
            "does turn out that way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_258D")

    label("loc_24FF")


    ChrTalk(
        0xFE,
        (
            "Roy will try hard and\x01",
            "maybe someday join the\x01",
            "Merchants Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband will be\x01",
            "pleased if it really\x01",
            "does turn out that way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258D")

    Jump("loc_2D38")

    label("loc_2592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A4")

    ChrTalk(
        0x9,
        (
            "My, my, everyone. You've\x01",
            "got another cute kid\x01",
            "with you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Miss. Sorry to\x01",
            "interrupt.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Haha, you're welcome.\x01",
            "You have good manners,\x01",
            "don't you.\x02",
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
            "Ah, no. I don't want to\x01",
            "overstay my welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(Haha, well done.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I don't know what to\x01",
            "say...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2736")

    ChrTalk(
        0x104,
        (
            "#00300F(Yeah, no mistakes at\x01",
            "all.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_2736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_276B")

    ChrTalk(
        0x109,
        (
            "#10100F(Yes, no mistakes at\x01",
            "all.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_276B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(
        0x105,
        (
            "#10300F(Yeah, no mistakes at\x01",
            "all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    SetScenarioFlags(0x1DC, 2)
    Jump("loc_27FB")

    label("loc_27A4")


    ChrTalk(
        0x9,
        (
            "Haha, you really do have\x01",
            "good manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wish Roy would follow\x01",
            "your example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    Jump("loc_296C")

    label("loc_2800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F7")

    ChrTalk(
        0xFE,
        (
            "My husband is annoying whenever he\x01",
            "talks about politics. And, it seems\x01",
            "he holds Mayor Dieter in high esteem.\x02",
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
            "I'm sure he'll play an\x01",
            "active role at the trade\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_296C")

    label("loc_28F7")


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
            "I'm sure he'll play an\x01",
            "active role at the trade\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296C")

    Jump("loc_2D38")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_END)), "loc_2B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A79")

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
            "They shouldn't have gone\x01",
            "far. Please try searching\x01",
            "the nearby districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Keep an eye out for\x01",
            "Roy's green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B25")

    label("loc_2A79")


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
            "Keep an eye out for\x01",
            "Roy's green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B25")

    Jump("loc_2B77")

    label("loc_2B2A")


    ChrTalk(
        0xFE,
        "They've both returned...\x02",
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

    label("loc_2B77")

    TalkEnd(0xFE)
    Return()

    label("loc_2B7B")


    ChrTalk(
        0xFE,
        (
            "Hmm. The rain isn't too\x01",
            "bad, but it's not\x01",
            "letting up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where Roy and\x01",
            "Meiling are going\x01",
            "shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE0")

    ChrTalk(
        0xFE,
        "Ah, you all are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FMrs. Perla, it's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, same here. I'm glad\x01",
            "you're all well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have you met my husband\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's upstairs, so please\x01",
            "say hello, if you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 2)
    Jump("loc_2D38")

    label("loc_2CE0")


    ChrTalk(
        0xFE,
        (
            "Have you met my husband\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's upstairs, so please\x01",
            "say hello, if you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D38")

    TalkEnd(0xFE)
    Return()

    # Function_5_1B46 end

    def Function_6_2D3C(): pass

    label("Function_6_2D3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFC")

    ChrTalk(
        0xFE,
        (
            "Don't worry, grandpa.\x01",
            "I'm sure Cronk and the\x01",
            "others are all right.\x02",
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
    Jump("loc_2E83")

    label("loc_2DFC")


    ChrTalk(
        0xFE,
        (
            "I'm sure Cronk and the\x01",
            "others are all right.\x02",
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

    label("loc_2E83")

    Jump("loc_2EEA")

    label("loc_2E88")


    ChrTalk(
        0xFE,
        (
            "Yo, thanks for returning\x01",
            "that umbrella for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to be more\x01",
            "careful next time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEA")

    TalkEnd(0xFE)
    Return()

    # Function_6_2D3C end

    def Function_7_2EEE(): pass

    label("Function_7_2EEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F47")

    ChrTalk(
        0xFE,
        (
            "Big brother and grandpa\x01",
            "told me to say here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's so scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F87")

    label("loc_2F47")


    ChrTalk(
        0xFE,
        "*chew, chew*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Big brother, this bread\x01",
            "is delicious!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F87")

    TalkEnd(0xFE)
    Return()

    # Function_7_2EEE end

    def Function_8_2F8B(): pass

    label("Function_8_2F8B")

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
        "#6P#00000FUm, good afternoon.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "Oh, good afternoon. It's\x01",
            "rare to have visitors on\x01",
            "a rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes, we had something to\x01",
            "ask you.\x02\x03",
            "#00000FDo you recognize this at\x01",
            "all?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Meiling's umbrella.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh, that's Meiling's\x01",
            "umbrella right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You brought it all the\x01",
            "way here?\x02",
        )
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
            "That girl had an\x01",
            "umbrella when she came\x01",
            "home.\x02",
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
            "Lloyd explained about\x01",
            "the umbrella swap.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh I see, so that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Poor Momo, what a\x01",
            "terrible thing she's\x01",
            "done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FDo you know where she\x01",
            "might be now?\x02\x03",
            "#10300FLooks like she's not\x01",
            "here right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, Meiling went\x01",
            "for a walk with Roy and\x01",
            "the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I'm terribly sorry. Come\x01",
            "to think of it, I forgot to\x01",
            "ask where they were going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FHmm, it seems we passed\x01",
            "each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FShe couldn't have gone far in this\x01",
            "rain anyway.\x02\x03",
            "#00104FShe's probably near East Street...\x01",
            "Central Square, Waterfront Area or\x01",
            "Downtown... somewhere around there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, she's probably\x01",
            "somewhere around there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Keep an eye out for\x01",
            "Roy's green umbrella or\x01",
            "Meiling's pink one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FA green or pink\x01",
            "umbrella... They should\x01",
            "be easy to spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRight. Let's begin the\x01",
            "search.\x02\x03",
            "#00004FThanks for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No problem. Come visit\x01",
            "anytime.\x02",
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

    # Function_8_2F8B end

    def Function_9_358F(): pass

    label("Function_9_358F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3627")
    SetChrPos(0x104, 1590, 4019, 8580, 180)
    Jump("loc_3660")

    label("loc_3627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3646")
    SetChrPos(0x109, 1590, 4019, 8580, 180)
    Jump("loc_3660")

    label("loc_3646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3660")
    SetChrPos(0x105, 1590, 4019, 8580, 180)

    label("loc_3660")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#12PHmm, if it isn't Lloyd\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_36AF():

        label("loc_36AF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_36AF")

    QueueWorkItem2(0x8, 1, lambda_36AF)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12PAnd that kid's with you... He has\x01",
            "an Eastern appearance. I reckon\x01",
            "he's not from around here.\x02",
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
            "#6PI see, so you're the\x01",
            "Crossbell Merchants\x01",
            "Association President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI'm Shing, the man\x01",
            "burdened with Heiyue's\x01",
            "future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYes, Heiyue is that Eastern\x01",
            "Quarter company that recently\x01",
            "expanded into Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PBurdened with its future,\x01",
            "you say. Could you be\x01",
            "staff of an elder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYes, I'm actually an\x01",
            "elder's grandson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PMr. Mors, do you know\x01",
            "the elders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAh, no. As a merchant, I did\x01",
            "some light deals with them,\x01",
            "but never actually met them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, but that was smart\x01",
            "of the elder to send his\x01",
            "grandson.\x02",
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
            "#00009FAh, well, there's\x01",
            "various circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PHaha. These people said\x01",
            "they absolutely had to\x01",
            "show me around the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI didn't really have a\x01",
            "choice, so I went along\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3B08")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3ABD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ABD)
    Sleep(50)

    def lambda_3ACD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ACD)
    Sleep(50)

    def lambda_3ADD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3ADD)
    Sleep(300)

    ChrTalk(
        0x104,
        "#11P#00306FHey now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_3B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3BA9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3B61():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B61)
    Sleep(50)

    def lambda_3B71():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B71)
    Sleep(50)

    def lambda_3B81():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B81)
    Sleep(300)

    ChrTalk(
        0x109,
        "#11P#10106FUhmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_3BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3C4D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3C02():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C02)
    Sleep(50)

    def lambda_3C12():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C12)
    Sleep(50)

    def lambda_3C22():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C22)
    Sleep(300)

    ChrTalk(
        0x105,
        "#11P#10306F*sigh*. Oh man.\x02",
    )

    CloseMessageWindow()

    label("loc_3C4D")


    ChrTalk(
        0x8,
        (
            "#12PHaha. I don't really get it,\x01",
            "but you seem to be getting\x01",
            "along and that's enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PShing, you said? I'm\x01",
            "happy you've taken an\x01",
            "interest in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYes, it's a nice place.\x01",
            "I'll take my leave,\x01",
            "then.\x02",
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

    # Function_9_358F end

    SaveToFile()

Try(main)
