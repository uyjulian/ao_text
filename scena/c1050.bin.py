from ScenarioHelper import *

def main():
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
        "Mols old man",             # 1
        "Mrs. Parla",             # 2
        "Roy",                   # 3
        "Meyrin",               # 4
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
        "Function_5_176B",         # 05, 5
        "Function_6_2839",         # 06, 6
        "Function_7_29DC",         # 07, 7
        "Function_8_2A74",         # 08, 8
        "Function_9_3098",         # 09, 9
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C")

    ChrTalk(
        0xFE,
        (
            "Crossbell daily\x01",
            "Although it is getting back,\x01",
            "There are still a lot of problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the influence refusing diplomacy\x01",
            "Any store has enough products\x01",
            "I have not arranged it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Mr. MacDarl\x01",
            "While keeping in touch,\x01",
            "I have to think about measures somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5B8")

    label("loc_52C")


    ChrTalk(
        0xFE,
        (
            "Crossbell daily\x01",
            "Although it is getting back,\x01",
            "There are still a lot of problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Mr. MacDarl\x01",
            "While keeping in touch,\x01",
            "I have to think about measures somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B8")

    Jump("loc_1767")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_70E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")

    ChrTalk(
        0xFE,
        (
            "Umu, street vendors\x01",
            "Safety is anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even under martial law, absolutely\x01",
            "Because I would like to continue my business\x01",
            "I have allowed it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they have something\x01",
            "It is my responsibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_709")

    label("loc_68C")


    ChrTalk(
        0xFE,
        (
            "Umu, street vendors\x01",
            "Safety is anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they have something\x01",
            "Permitted business under martial law\x01",
            "It is my responsibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709")

    Jump("loc_1767")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_90B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890")

    ChrTalk(
        0xFE,
        (
            "Dictator's speech ……\x01",
            "McDaely's appearance\x01",
            "I am worried that I did not show it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ellie,\x01",
            "You do not know anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F……House.\x01",
            "Actually, I was a little worried … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I see.\x01",
            "Let's be worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway\x01",
            "As it is this way,\x01",
            "Conflict with two major powers is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To prepare for emergency\x01",
            "I have to call out from the Chamber of Commerce ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_906")

    label("loc_890")


    ChrTalk(
        0xFE,
        (
            "As it is this way,\x01",
            "Conflict with two major powers is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To prepare for emergency\x01",
            "I have to call out from the Chamber of Commerce ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_906")

    Jump("loc_1767")

    label("loc_90B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_919")
    Jump("loc_1767")

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0B")

    ChrTalk(
        0xFE,
        (
            "Hmm, there is also a referendum\x01",
            "At this closing time,\x01",
            "It is said that such a case will happen …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Poorly, to the Empire and the Republic\x01",
            "To the suitable material to be attached\x01",
            "It may become it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, urgent solution\x01",
            "It is a desired place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A88")

    label("loc_A0B")


    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "To the empire and republic in terms of security\x01",
            "It is the current situation showing weakness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, urgent solution\x01",
            "It is a desired place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A88")

    Jump("loc_1767")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")

    ChrTalk(
        0xFE,
        (
            "Yesterday's train accident\x01",
            "A monster who might be an acquaintance\x01",
            "It was a work or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I have been witnessed lately\x01",
            "With a mysterious monster\x01",
            "Is it the same thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even recently there are many incidents.\x01",
            "You too are careful enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C08")

    label("loc_B6F")


    ChrTalk(
        0xFE,
        (
            "The monster that caused the train accident\x01",
            "Recently rumored to be a mysterious monster\x01",
            "I do not know whether it is the same … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even recently there are many incidents.\x01",
            "You too are careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C08")

    Jump("loc_1767")

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1B")
    Jump("loc_1767")

    label("loc_C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C29")
    Jump("loc_1767")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9D")

    ChrTalk(
        0xFE,
        (
            "Crossbell autonomous state independence ……\x01",
            "Mayor Dieter also dared to\x01",
            "I declared it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the ability to say inside and outside\x01",
            "It is growing more than ever\x01",
            "There is no doubt that now is the opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continued to be dominated by the two major powers in a long history,\x01",
            "Pride of crossbell being lost … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There will be various conflicts,\x01",
            "With the result of realization of independence\x01",
            "I want you to recover anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E65")

    label("loc_D9D")


    ChrTalk(
        0xFE,
        (
            "… Oh yeah, such a mayor's\x01",
            "Even in terms of supporting the recent momentum,\x01",
            "I am promoting some projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In collaboration with Crossbell Communication Company,\x01",
            "Citizens will notice it.\x01",
            "Everyone, please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E65")

    Jump("loc_1767")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0C")

    ChrTalk(
        0xFE,
        "At last the trade meeting will start.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Watari citizen\x01",
            "At the Crossbell Times\x01",
            "Just wait for the results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now……\x01",
            "What kind of meeting will it be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F6E")

    label("loc_F0C")


    ChrTalk(
        0xFE,
        (
            "Originally, by all means\x01",
            "I wanted to see the state of the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now……\x01",
            "What kind of meeting will it be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6E")

    Jump("loc_1767")

    label("loc_F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(
        0xFE,
        (
            "Apparently my grandson Roy,\x01",
            "Interest in stalls work\x01",
            "I heard you started to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Was also originally a street vendor.\x01",
            "Hmm, this is also bloodline.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_114E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1030")
    Call(0, 9)
    Jump("loc_10BF")

    label("loc_1030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(
        0x8,
        (
            "Hmm, it's nothing black\x01",
            "Elders' grandchildren\x01",
            "I will not come to my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway,\x01",
            "If you like this town\x01",
            "I am also happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BF")

    Jump("loc_1149")

    label("loc_10C4")


    ChrTalk(
        0xFE,
        (
            "At the Trade Council, delegates from each country\x01",
            "Mainly on economic relationship arrangements\x01",
            "Talks will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wheelchair Chamber of Commerce also trends\x01",
            "You are paying attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1149")

    Jump("loc_1767")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1509")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")

    ChrTalk(
        0xFE,
        (
            "Oh, is not it Lloyd?\x01",
            "What on earth happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEr …\x01",
            "Meilin is\x01",
            "Are you at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought that I came home earlier\x01",
            "I thought that … ….\x01",
            "Did you go somewhere again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry but my grandmother\x01",
            "Can you hear me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12DC")

    label("loc_1275")


    ChrTalk(
        0xFE,
        (
            "You are working.\x01",
            "My grandchild went out.\x01",
            "It is noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About grandchildren to an old lady\x01",
            "Can you hear me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DC")

    Jump("loc_130E")

    label("loc_12E1")


    ChrTalk(
        0xFE,
        (
            "Well, for the work of the Chamber of Commerce\x01",
            "Continue if you do … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130E")

    Jump("loc_13A6")

    label("loc_1313")


    ChrTalk(
        0xFE,
        (
            "To Roy's bastard\x01",
            "Even one of the sermons\x01",
            "I thought I'd rather do it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where there is Meyrin\x01",
            "I do not want to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Will you miss today.\x02",
    )

    CloseMessageWindow()

    label("loc_13A6")

    TalkEnd(0xFE)
    Return()

    label("loc_13AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A4")

    ChrTalk(
        0xFE,
        (
            "It was held just before the cult incident\x01",
            "Crossbell Budget Parliament,\x01",
            "It has become a partition again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "New mayor, new chairperson is the center\x01",
            "To a plan that does not involve interests\x01",
            "The budget was reorganized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the city government finally\x01",
            "I began to move in a good direction\x01",
            "I mean that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1504")

    label("loc_14A4")


    ChrTalk(
        0xFE,
        (
            "Municipal administration finally got better\x01",
            "You seem to be getting started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is also the new mayor and the new chairman\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1504")

    Jump("loc_1767")

    label("loc_1509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(
        0xFE,
        (
            "Oh … … To Lloyd,\x01",
            "Mr. MacDaely Chairman Miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a long time ago.\x01",
            "Looks fine and more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHello, Mr. President Morse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Flong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FCertainly, put together the merchants of east street\x01",
            "It was the president of the Chamber of Commerce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOh, this one is … …\x01",
            "(Mother also in the street vendor's age\x01",
            "I was indebted to you. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there seems to be a new face\x01",
            "The Special Affairs Support Division is finally here\x01",
            "Where did it say restart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To you guys\x01",
            "We 're expecting citizens as well.\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 1)
    Jump("loc_1767")

    label("loc_16FB")


    ChrTalk(
        0xFE,
        (
            "You guys at the Special Affairs Support Division\x01",
            "I am expecting it from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I have something to help with\x01",
            "You should come at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_4_43C end

    def Function_5_176B(): pass

    label("Function_5_176B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1794")
    Call(0, 8)
    Return()

    label("loc_1794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1871")

    ChrTalk(
        0xFE,
        (
            "Overcoming President's detention,\x01",
            "What to do now … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those who live in Crossbell\x01",
            "I think it's more important than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Talking with everyone, surely in a good direction\x01",
            "I hope things will progress.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1910")

    label("loc_1871")


    ChrTalk(
        0xFE,
        (
            "What to do now … ….\x01",
            "For those living in Crossbell\x01",
            "I think that is more important than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Talking with everyone, surely in a good direction\x01",
            "I hope things will progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1910")

    Jump("loc_2835")

    label("loc_1915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19A2")

    ChrTalk(
        0xFE,
        (
            "Roy and his grandfather\x01",
            "Because I keep on watching him,\x01",
            "I am not afraid of coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So Meilin,\x01",
            "You do not have to worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_19A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA8")

    ChrTalk(
        0xFE,
        (
            "Dieter's Declaration of Independence ……\x01",
            "I wonder if it was premature ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything in this world\x01",
            "What is changing things\x01",
            "I intended to understand, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No … … Crossbell already\x01",
            "In a situation I can not say so\x01",
            "Perhaps it has become … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B32")

    label("loc_1AA8")


    ChrTalk(
        0xFE,
        (
            "The sudden change of things,\x01",
            "For us old people\x01",
            "There is a scary thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell already\x01",
            "Until I can not return\x01",
            "You had it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B32")

    Jump("loc_2835")

    label("loc_1B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(
        0xFE,
        (
            "If you are a grandfather, at a business of the Chamber of Commerce\x01",
            "I'm going to the city hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This charity event\x01",
            "Roy says he is helping, though ….\x01",
            "I wonder what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C5A")

    ChrTalk(
        0xFE,
        (
            "Anyway, now to the goddess\x01",
            "I can only pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this crossbell no more\x01",
            "I wish useless blood will not flow ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1CE7")

    ChrTalk(
        0xFE,
        (
            "Recently what really happens\x01",
            "I do not know …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roy and Meilin, too,\x01",
            "When going out enough\x01",
            "I have to tell him to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D6C")

    ChrTalk(
        0xFE,
        (
            "Well ……\x01",
            "My grandfather and meirin\x01",
            "I wonder if it is time to go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Prepare black tea and sweets\x01",
            "Let's say we are waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E1A")

    ChrTalk(
        0xFE,
        (
            "If you are a grandfather,\x01",
            "As shown in the table with meylin\x01",
            "I wonder if you are playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, grandpa\x01",
            "I can play with my grandchild on a holiday for the first time in a while,\x01",
            "I was very happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E9E")

    ChrTalk(
        0xFE,
        (
            "Regarding referendums,\x01",
            "It seems that even the Chamber of Commerce will go to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will happen ….\x01",
            "I do not understand at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F35")

    ChrTalk(
        0xFE,
        (
            "Grandfather, as chief of the Chamber of Commerce\x01",
            "It seems there are places to think differently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is already an age,\x01",
            "Do not overdo it\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_206F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFC")

    ChrTalk(
        0xFE,
        (
            "Old grandfather also\x01",
            "For Roy's spirit\x01",
            "It seems he was burning his hands ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's do our best next time,\x01",
            "Eventually to the Chamber of Commerce ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it supposed to be,\x01",
            "I'm sure you will be pleased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_206A")

    label("loc_1FFC")


    ChrTalk(
        0xFE,
        (
            "Let's do our best next time,\x01",
            "Eventually to the Chamber of Commerce ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it supposed to be,\x01",
            "My grandfather will surely be pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206A")

    Jump("loc_2835")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")

    ChrTalk(
        0x9,
        (
            "Oh no, you guys.\x01",
            "Today I will have a cute child again\x01",
            "You are taking them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hm, your wife.\x01",
            "I'm getting in the way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Hehe, you are welcome.\x01",
            "You behaved very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Would you like to drink tea if you do not mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Oh,\x01",
            "I am not going to stay long\x01",
            "Unnamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(Hehe, you are a brilliant social gift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(What I should say … …)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2230")

    ChrTalk(
        0x104,
        "#00300F(Oh, you do not have any snow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2267")

    ChrTalk(
        0x109,
        "#10100F(Yes, there is not schnitz.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_2267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2295")

    ChrTalk(
        0x105,
        "#10300F(Oh, I do not have any sorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_2295")

    SetScenarioFlags(0x1DC, 2)
    Jump("loc_22E4")

    label("loc_229D")


    ChrTalk(
        0x9,
        (
            "Huhu, really\x01",
            "Be polite and a good child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I would like Roy to practice it.\x02",
    )

    CloseMessageWindow()

    label("loc_22E4")

    Jump("loc_243D")

    label("loc_22E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")

    ChrTalk(
        0xFE,
        (
            "A noisy grandfather also talks about politics,\x01",
            "Mayor Dieter\x01",
            "It seems to be very appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I am going to take IBC\x01",
            "It is a person who has handled it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely at the trade meeting\x01",
            "It will be useful for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_243D")

    label("loc_23C9")


    ChrTalk(
        0xFE,
        (
            "My grandfather also has a new mayor\x01",
            "It seems to be very appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely at the trade meeting\x01",
            "It will be useful for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243D")

    Jump("loc_2835")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_END)), "loc_260A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255E")

    ChrTalk(
        0xFE,
        (
            "Roy and Meirin,\x01",
            "I went for a walk in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To far there\x01",
            "Because I think that I have not gone,\x01",
            "Please find a neighboring block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Roy 's green umbrella,\x01",
            "Meilin's pink umbrella\x01",
            "You may try looking for either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_260A")

    label("loc_255E")


    ChrTalk(
        0xFE,
        (
            "Roy and Meilin\x01",
            "I think that I have not gone so far,\x01",
            "Please find a neighboring block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Roy 's green umbrella,\x01",
            "Meilin's pink umbrella\x01",
            "You may try looking for either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_266B")

    label("loc_260F")


    ChrTalk(
        0xFE,
        (
            "Both grandchildren\x01",
            "It's just that I came back … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even at hot lemonade\x01",
            "Shall I give you a cup of it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266B")

    TalkEnd(0xFE)
    Return()

    label("loc_266F")


    ChrTalk(
        0xFE,
        (
            "Well, rain foot is weak, but\x01",
            "I do not quite stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roy, how far\x01",
            "I wonder if I went shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_26DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D2")

    ChrTalk(
        0xFE,
        "Fairly, you guys ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOka, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, this is it.\x01",
            "It seems to be healthy and anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the grandfather\x01",
            "I have already met him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is on the top,\x01",
            "If you do not mind please greet\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 2)
    Jump("loc_2835")

    label("loc_27D2")


    ChrTalk(
        0xFE,
        (
            "To the grandfather\x01",
            "I have already met him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is on the top,\x01",
            "If you do not mind please greet\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2835")

    TalkEnd(0xFE)
    Return()

    # Function_5_176B end

    def Function_6_2839(): pass

    label("Function_6_2839")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F2")

    ChrTalk(
        0xFE,
        (
            "Do not worry, Grandpa.\x01",
            "Mr. Crooks\x01",
            "Surely it's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also make inquiries to the city hall\x01",
            "I can not do it,\x01",
            "Let's keep still at home now.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_296B")

    label("loc_28F2")


    ChrTalk(
        0xFE,
        (
            "Mr. Crooks\x01",
            "Surely it's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also make inquiries to the city hall\x01",
            "I can not do it,\x01",
            "Let's keep still at home now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296B")

    Jump("loc_29D8")

    label("loc_2970")


    ChrTalk(
        0xFE,
        (
            "Oh, the umbrella is safe\x01",
            "It seems they delivered it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on I got a bit more\x01",
            "I wish it was solid …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D8")

    TalkEnd(0xFE)
    Return()

    # Function_6_2839 end

    def Function_7_29DC(): pass

    label("Function_7_29DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(
        0xFE,
        (
            "To my older brother and grandpa,\x01",
            "I was told to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am very scared …\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A70")

    label("loc_2A40")


    ChrTalk(
        0xFE,
        "Munching\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My older brother, bread is delicious!\x02",
    )

    CloseMessageWindow()

    label("loc_2A70")

    TalkEnd(0xFE)
    Return()

    # Function_7_29DC end

    def Function_8_2A74(): pass

    label("Function_8_2A74")

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
        "#6P#00000FUh, good day\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "Oh, hello there.\x01",
            "It is unusual in such rain, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, hey\x01",
            "There was something I wanted to ask.\x02\x03",
            "#00000FDo you recognize this at all>\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's umbrella of Maylin\x01",
            "I showed to my wife.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh, this is ….\x01",
            "It is not Meirin 's umbrella.\x02",
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
        "Oh but\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That girl from a bakery\x01",
            "When I return home,\x01",
            "I thought I had it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FUh, actually\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is\x01",
            "I am looking for umbrella of peach\x01",
            "I explained the circumstances.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh no, like that\x01",
            "That was it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That peach is a child\x01",
            "You did a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FWell, your lady.\x01",
            "Where are your grandchildren now?\x02\x03",
            "#10300FAs you can see here\x01",
            "It does not seem to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, together with Roy\x01",
            "I guess I went for a walk by putting an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……I'm sorry,\x01",
            "That reminds me of listening to the destination\x01",
            "I have forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FWell, apparently mistaken.\x01",
            "You seem to have become it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's raining, and far there\x01",
            "I wonder if it is not going.\x02\x03",
            "#00104FNext to east street,\x01",
            "Central square or port area, old city … ….\x01",
            "I think that's about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Right, I think that's true\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Roy 's green umbrella,\x01",
            "Meilin's pink umbrella\x01",
            "You may try looking for either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FGreen or pink umbrella …\x01",
            "Surely it seems to be a landmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRight. Ok we'll go check\x02\x03",
            "#00004FThanks for your help\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No problem.\x01",
            "You can come any time again.\x02",
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

    # Function_8_2A74 end

    def Function_9_3098(): pass

    label("Function_9_3098")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3130")
    SetChrPos(0x104, 1590, 4019, 8580, 180)
    Jump("loc_3169")

    label("loc_3130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_314F")
    SetChrPos(0x109, 1590, 4019, 8580, 180)
    Jump("loc_3169")

    label("loc_314F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3169")
    SetChrPos(0x105, 1590, 4019, 8580, 180)

    label("loc_3169")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        "#12PHmm, you are Lloyd guys.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_31B0():

        label("loc_31B0")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_31B0")

    QueueWorkItem2(0x8, 1, lambda_31B0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12PYour child is … …\x01",
            "I am wearing an easterly style\x01",
            "It is a face you do not see around here.\x02",
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
            "#6PIndeed, you\x01",
            "It is the president of the Cross Bell Chamber of Commerce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PMy name is Shin.\x01",
            "It is a man who carries the future of \"black moon\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, when we say \"black moon\"\x01",
            "Recently Cross Bell\x01",
            "Toho People's Street Entering ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PI told you to carry the future now,\x01",
            "Maybe it is an official of the Presbyterian Association?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYeah, that's it\x01",
            "My grandfather is an elder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PPerhaps,\x01",
            "Does Mrs. are acquainted with the elders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12POh no, through business\x01",
            "Just lightly interacted directly\x01",
            "I have never met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, but\x01",
            "Only with the elder grandchildren\x01",
            "It is quite intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PBut, why\x01",
            "With Lloyd the guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell,\x01",
            "There were various circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PHuhu, these guys\x01",
            "Do not miss the city\x01",
            "It is what you would like to announce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI have no choice but to go out with you\x01",
            "It is a tokoro.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_35EE")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_35A1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A1)
    Sleep(50)

    def lambda_35B1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35B1)
    Sleep(50)

    def lambda_35C1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35C1)
    Sleep(300)

    ChrTalk(
        0x104,
        "#11P#00306FCome on … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3692")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3647():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3647)
    Sleep(50)

    def lambda_3657():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3657)
    Sleep(50)

    def lambda_3667():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3667)
    Sleep(300)

    ChrTalk(
        0x109,
        "#11P#10106FEr …\x02",
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_3692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_373B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_36EB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36EB)
    Sleep(50)

    def lambda_36FB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36FB)
    Sleep(50)

    def lambda_370B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_370B)
    Sleep(300)

    ChrTalk(
        0x105,
        "#11P#10306FWell, I'm pleased.\x02",
    )

    CloseMessageWindow()

    label("loc_373B")


    ChrTalk(
        0x8,
        (
            "#12PHaha, I do not quite understand it\x01",
            "It seems like good relations, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHave you said Shin?\x01",
            "Please cross-town of Crossbell\x01",
            "I am glad if you like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYes, I think so.\x01",
            "Well, you have it.\x02",
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

    # Function_9_3098 end

    SaveToFile()

Try(main)
