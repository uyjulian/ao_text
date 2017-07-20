from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "Helmer",               # 1
        "Joanna",             # 2
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
    ))

    DeclNpc(0,       4059,    7760,    180,  257,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(4294921947, 59,      3900,    360,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(4294926476, 0,       40910,   1500,    4294926476, 1500,    40910,   0x007C, 0,  9,  0x0000)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_236",          # 03, 3
        "Function_4_261",          # 04, 4
        "Function_5_392",          # 05, 5
        "Function_6_43B",          # 06, 6
        "Function_7_1911",         # 07, 7
        "Function_8_1B75",         # 08, 8
        "Function_9_30BB",         # 09, 9
        "Function_10_3D83",        # 0A, 10
        "Function_11_43FA",        # 0B, 11
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_168"),
        (1, "loc_174"),
        (2, "loc_180"),
        (3, "loc_18C"),
        (4, "loc_198"),
        (5, "loc_1A4"),
        (6, "loc_1B0"),
        (SWITCH_DEFAULT, "loc_1BC"),
    )


    label("loc_168")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_174")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_180")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_18C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_198")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1DF")

    Return()

    # Function_0_128 end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20A")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_1E0")

    label("loc_20A")

    Return()

    # Function_1_1E0 end

    def Function_2_20B(): pass

    label("Function_2_20B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_235")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_20B")

    label("loc_235")

    Return()

    # Function_2_20B end

    def Function_3_236(): pass

    label("Function_3_236")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_260")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_236")

    label("loc_260")

    Return()

    # Function_3_236 end

    def Function_4_261(): pass

    label("Function_4_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_391")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrPos(0x8, 810, 0, 500, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -810, 0, 500, 90)
    Jump("loc_391")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_391")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CD")
    SetChrFlags(0x9, 0x80)

    label("loc_2CD")

    Jump("loc_391")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E0")
    Jump("loc_391")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EE")
    Jump("loc_391")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_301")
    SetChrFlags(0x9, 0x80)
    Jump("loc_391")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30F")
    Jump("loc_391")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D")
    Jump("loc_391")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32B")
    Jump("loc_391")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_391")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_391")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_391")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x9, -42190, 0, 48970, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_391")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0x8, 0x10)

    label("loc_391")

    Return()

    # Function_4_261 end

    def Function_5_392(): pass

    label("Function_5_392")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BA")
    OP_66(0x0, 0x1)

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FF")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_43A")

    Return()

    # Function_5_392 end

    def Function_6_43B(): pass

    label("Function_6_43B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D")

    ChrTalk(
        0xFE,
        (
            "Husband is Orkis Tower\x01",
            "It seems that you are taking command of the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the president was detained,\x01",
            "I can lead the crossbells\x01",
            "There is only one person, my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There will be a burden … …\x01",
            "I'd like you to do some best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5DE")

    label("loc_53D")


    ChrTalk(
        0xFE,
        (
            "Now that the president was detained,\x01",
            "I can lead the crossbells\x01",
            "There is only one person, my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There will be a burden … …\x01",
            "I'd like you to do some best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE")

    Jump("loc_190D")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    Call(0, 7)
    Jump("loc_68D")

    label("loc_5FE")


    ChrTalk(
        0xFE,
        (
            "My husband and my girlfriend\x01",
            "Since being detained by Michelam,\x01",
            "I was not mind, but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way I can see the figure\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D")

    Jump("loc_190D")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "……Lady……\x01",
            "From my husband, something contact me\x01",
            "Is it there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FNo, nothing to me either ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, anyway …\x01",
            "As soon as I know something,\x01",
            "We will contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady's garments,\x01",
            "To your own work\x01",
            "Please devote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, thank you\x01",
            "Heller.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 2)
    Jump("loc_86D")

    label("loc_7EB")


    ChrTalk(
        0xFE,
        (
            "N / A about your husband\x01",
            "As soon as I understand it,\x01",
            "We will contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady's garments,\x01",
            "To your own work\x01",
            "Please devote.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D")

    Jump("loc_190D")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(
        0xFE,
        (
            "…… Previous raid incident,\x01",
            "It was a really painful event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For restoration activities, finally\x01",
            "It seems that it is a promising … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even those who are still fearing\x01",
            "Not many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To prevent recurrence,\x01",
            "To my husband and mayor\x01",
            "I would like you to keep up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9ED")

    label("loc_972")


    ChrTalk(
        0xFE,
        (
            "The other day 's raid incident,\x01",
            "It was a really painful event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To prevent recurrence,\x01",
            "To my husband and mayor\x01",
            "I would like you to keep up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ED")

    Jump("loc_190D")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8")

    ChrTalk(
        0xFE,
        (
            "Mr. Husband as well as mayor\x01",
            "In dealing with occupation cases\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In rumors, the armed group\x01",
            "Even the guard does not have any hands or legs\x01",
            "The situation seems to be continuing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I am worried.\x01",
            "I just pray for an immediate solution.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B68")

    label("loc_AE8")


    ChrTalk(
        0xFE,
        (
            "Even the guards are the strength of the armed group\x01",
            "I do not have hands or feet ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I am worried.\x01",
            "I just pray for an immediate solution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B68")

    Jump("loc_190D")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment accident ……\x01",
            "No, I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cause is falling rock, or\x01",
            "With the work of huge chemicals etc\x01",
            "It seems to be being troubled, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the real cause is\x01",
            "What was it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA0")

    label("loc_C34")


    ChrTalk(
        0xFE,
        "I was surprised at the derailment accident yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Various rumors are flowing … …\x01",
            "The real cause is\x01",
            "What was it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0")

    Jump("loc_190D")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(
        0xFE,
        (
            "Somewhat in the direction of Nishi-dori\x01",
            "Like a siren could hear …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay, is this the sky?\x02",
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(
        0xFE,
        (
            "With the advice of national independence\x01",
            "The influence comes out in each direction, and the husband also\x01",
            "It seems that it is being chased by that correspondence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today with Mayor Dieter\x01",
            "I heard that it is a meeting at the Orkis Tower ……\x01",
            "I want you to be careful about your body.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDE")

    ChrTalk(
        0xFE,
        (
            "A referendum on referendum on independence\x01",
            "It is approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this regard,\x01",
            "You should take a cautious stance\x01",
            "It seems to be thinking … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cross Bell residents are\x01",
            "What choices are you making ……\x01",
            "I am also interested personally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F73")

    label("loc_EDE")


    ChrTalk(
        0xFE,
        (
            "A referendum on referendum on independence\x01",
            "It is approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cross Bell residents are\x01",
            "What choices are you making ……\x01",
            "I am also interested personally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F73")

    Jump("loc_190D")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FFD")

    ChrTalk(
        0xFE,
        (
            "Husband, too early this morning\x01",
            "To the Orkis Tower\x01",
            "I was headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's plenary session ……\x01",
            "I hope it ends without delay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_11A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(
        0xFE,
        (
            "Husband is busy recently,\x01",
            "At the city office without returning to the mansion\x01",
            "Although there were many things to be absent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have contacted you earlier,\x01",
            "Today is the first time in a while\x01",
            "It seems to come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For tomorrow's plenary session,\x01",
            "By all means nourish your spirit\x01",
            "I'd like to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11A1")

    label("loc_110A")


    ChrTalk(
        0xFE,
        (
            "Tonight for my husband,\x01",
            "Menu with nutritious value\x01",
            "We are preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Towards tomorrow's plenary session, by all means\x01",
            "I'd like you to develop spirit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A1")

    Jump("loc_190D")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B6")

    ChrTalk(
        0xFE,
        (
            "At parliament around the time Hartmann 's chairman,\x01",
            "Husband sent empire and republican\x01",
            "It was all I could do with keeping it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, recently in collaboration with the new Mayor\x01",
            "Finally to be able to cross each other\x01",
            "Things that it became ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are also very pleased that\x01",
            "I am thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1361")

    label("loc_12B6")


    ChrTalk(
        0xFE,
        (
            "When Dieter became mayor,\x01",
            "We are very pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The main conference from tomorrow … …\x01",
            "No matter what happens to your husband and mayor\x01",
            "I would like you to demonstrate that skill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")

    Jump("loc_190D")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1422")

    ChrTalk(
        0xFE,
        (
            "For the commerce meeting from tomorrow,\x01",
            "Husband and Mayor of Dieter\x01",
            "It seems that we are preparing careful preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently mostly on the mansion\x01",
            "I will not return either … ….\x01",
            "I am worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_15DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(
        0xFE,
        (
            "These days, next to me\x01",
            "People who moved in … …\x01",
            "There was a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Running around the city with a driving car,\x01",
            "Shed loud music at midnight ……\x01",
            "There seems to be noticeable actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I make a complaint hear me ears\x01",
            "You can not have me ……\x01",
            "What shall I do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D7")

    label("loc_1537")


    ChrTalk(
        0xFE,
        (
            "These days, next to me\x01",
            "People who moved in … …\x01",
            "It seems that notable acts are prominent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I make a complaint hear me ears\x01",
            "You can not have me ……\x01",
            "What shall I do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D7")

    Jump("loc_190D")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_190D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "This is Elie Lady.\x01",
            "Welcome back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI'm home, Mr. Helmer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see,\x01",
            "This is Eri's parents house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FReally, it is a big house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAh……\x01",
            "Anyway, McDowell's chairman\x01",
            "It is also a mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehuu, please do not hold back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, everyone is a lady's colleague\x01",
            "I will be able to show you, by all means\x01",
            "Amenity#2RRelax#I hope you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mission support department is finally here\x01",
            "By being restarted,\x01",
            "I will be busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Eli again.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, thank you Helmer.\x01",
            "I will keep trying hard.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x134, 1)
    Jump("loc_190D")

    label("loc_1888")


    ChrTalk(
        0xFE,
        (
            "The mission support department is finally here\x01",
            "By being restarted,\x01",
            "I will be busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Eli again.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")

    TalkEnd(0xFE)
    Return()

    # Function_6_43B end

    def Function_7_1911(): pass

    label("Function_7_1911")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        "Oh, everyone …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oyou lady …………\x01",
            "…… Elie Lady … …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHeller, Mr. Joanna.\x01",
            "… … I worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "………… (Bun Bun)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since my husband's invalid declaration,\x01",
            "Whether Ellie is safe or not,\x01",
            "It was just a concern, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this way I can see the figure\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHehe, thank you.\x02\x03",
            "#00103F…… But I have to go now\x01",
            "There is a place not to be done.\x02\x03",
            "#00101FFor a while\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Eli lady, everyone … …\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    SetScenarioFlags(0x1CC, 7)
    Return()

    # Function_7_1911 end

    def Function_8_1B75(): pass

    label("Function_8_1B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")

    ChrTalk(
        0xFE,
        (
            "Eli lady,\x01",
            "To that eerie big tree\x01",
            "It is going to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FDo not worry, Joanna.\x01",
            "I'm sure they will come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……Yes.\x01",
            "Lady's ever\x01",
            "He came back … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that you will be able to return safely.\x01",
            "… … Please please take care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D1A")

    label("loc_1CC0")


    ChrTalk(
        0xFE,
        (
            "Ely, our friends\x01",
            "I believe that I will be back.\x01",
            "… … Please please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1A")

    Jump("loc_30B7")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3A")
    Call(0, 7)
    Jump("loc_1D97")

    label("loc_1D3A")


    ChrTalk(
        0xFE,
        "Outside seems to be very dangerous ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eli lady, everyone … …\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D97")

    Jump("loc_30B7")

    label("loc_1D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(
        0xFE,
        (
            "Husband ……\x01",
            "Where the hell are you going to?\x01",
            "Did they get dropped ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am worried about you ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlso in the place of the speech just before\x01",
            "I did not show up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FGrandfather, where are you really ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "…… Oh, I'm sorry!\x01",
            "Mischief's fears unnecessarily\x01",
            "Something to be fueled ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F…… No, I am okay.\x02\x03",
            "#00100FJoanna is the better side,\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, I understand …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 3)
    Jump("loc_1FB1")

    label("loc_1F42")


    ChrTalk(
        0xFE,
        (
            "…… What I did with you,\x01",
            "Mischief's fears unnecessarily\x01",
            "Something to be fueled ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Husband ……\x01",
            "Surely it is safe, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB1")

    Jump("loc_30B7")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2105")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FE8")
    Call(0, 10)
    Return()

    label("loc_1FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(
        0xFE,
        (
            "After all …………\x01",
            "Let me out to Miscon\x01",
            "I think that I will do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Please call me when you need it.\x01",
            "I will be heading soon …………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2100")

    label("loc_207F")


    ChrTalk(
        0xFE,
        (
            "Today is the administrative district\x01",
            "Charity event\x01",
            "I heard you are doing it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I also, in some form\x01",
            "Can not you help?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2100")

    Jump("loc_30B7")

    label("loc_2105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_217F")

    ChrTalk(
        0xFE,
        "The mining town is occupied … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I am scared … …\x01",
            "From now on again, something\x01",
            "I feel like it will happen ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21D2")

    ChrTalk(
        0xFE,
        "Recently, there are a lot of rain ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The laundry does not dry up.\x01",
            "Ha\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_21E0")
    Jump("loc_30B7")

    label("loc_21E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2358")

    ChrTalk(
        0xFE,
        (
            "Recently, especially for busy husband,\x01",
            "If you do not prepare meals that are refined ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… What kind of dish is good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FGeez …\x01",
            "I wonder what kind of lamb meat is.\x02\x03",
            "#00104FIt is high protein and low in calories,\x01",
            "I think that it will suit the mouth of your grandfather.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "… … It might be good …\x01",
            "It is truly Ellie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FOh, haha.\x01",
            "Even if praised at this much …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23CF")

    label("loc_2358")


    ChrTalk(
        0xFE,
        (
            "Because I am a small meal\x01",
            "I do not eat much,\x01",
            "Meat may be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later in the department store\x01",
            "If you do not go shopping ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CF")

    Jump("loc_30B7")

    label("loc_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_254C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2510")

    ChrTalk(
        0xFE,
        (
            "At the trade meeting this time\x01",
            "Listening to the attacks of terrorists ……\x01",
            "My heart was about to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since then, Eli and Husband\x01",
            "I will not stop getting worried for a long time ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FJoanna ……\x01",
            "Do not worry too much.\x02\x03",
            "#00100FEveryone in the support department … …\x01",
            "Surely it will be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, That's right……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2547")

    label("loc_2510")


    ChrTalk(
        0xFE,
        (
            "Everyone, Eli-sama … …\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2547")

    Jump("loc_30B7")

    label("loc_254C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25A7")

    ChrTalk(
        0xFE,
        (
            "Eli, …\x01",
            "Town of the city seems to be in heavy caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful …\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_276D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")

    ChrTalk(
        0xFE,
        (
            "Today's supper,\x01",
            "My husband's favorite\x01",
            "It is a tomato dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomato salad,\x01",
            "Spaghetti with tomato sauce,\x01",
            "Tomato 100 juice … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Well, I suppose …\x01",
            "It's a thorough menu. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Grandfather,\x01",
            "I liked that much … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2768")

    label("loc_26CE")


    ChrTalk(
        0xFE,
        (
            "Today is my husband's favorite,\x01",
            "It is a tomato dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be good for your health,\x01",
            "I am also gaming.\x01",
            "I think I will eat … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FDo not touch it … ….?\x02",
    )

    CloseMessageWindow()

    label("loc_2768")

    Jump("loc_30B7")

    label("loc_276D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284F")

    ChrTalk(
        0xFE,
        (
            "This morning, people who live next door\x01",
            "I came across the front door … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Suddenly, \"Let's go for a drive together\"\x01",
            "I was invited and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course we refused politely,\x01",
            "It is kind of familiar people …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F6")

    label("loc_284F")


    ChrTalk(
        0xFE,
        (
            "To people living next door this morning\x01",
            "Suddenly, \"Let's go for a drive together\"\x01",
            "I was invited and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course we refused politely,\x01",
            "It is kind of familiar people …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F6")

    Jump("loc_30B7")

    label("loc_28FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2982")

    ChrTalk(
        0xFE,
        (
            "It will be announced tomorrow\x01",
            "New city hall building ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even with a banning curtain\x01",
            "Feeling enough powerfully,\x01",
            "I will sprain it …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6F")

    ChrTalk(
        0xFE,
        "(Kyuukyukyuu)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEr, Joanna.\x01",
            "Do you draw something in the window?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x102, 1000)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "…. Well, the window is\x01",
            "I thought it was cloudy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And then I was rude.\x01",
            "I will return to cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2AC2")

    label("loc_2A6F")


    ChrTalk(
        0xFE,
        (
            "If you are listening to rain sounds\x01",
            "I got distracted … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, I am not good on rainy days.\x02",
    )

    CloseMessageWindow()

    label("loc_2AC2")

    Jump("loc_30B7")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3013")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Ah……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Welcome back, Ellie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI am Joanna.\x01",
            "I wonder if today will change?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes … thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The lady came back from the excursion,\x01",
            "I could finally be relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, Joanna … …\x01",
            "There is nothing to worry about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, for me it's a lady\x01",
            "Husband is everything ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHuh, it's a maid of your husband.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, Ellie.\x01",
            "The other day, from my younger sister and my younger wife\x01",
            "I received your letter, but … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005Fthat's……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F…… Yes, I am in the Republic and the Empire\x01",
            "It's about my parents.\x02\x03",
            "#00100FAlthough I have received it from time to time,\x01",
            "Since that group incident has ended\x01",
            "It got to reach better than before.\x02\x03",
            "#00104FI'm worried about me and the grandfather\x01",
            "Most of the content,\x01",
            "It is one of recent encouragement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(…… Family, or ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FJoanna, I will read it later\x01",
            "I wonder if it keeps it safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes … I will do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that mission support section was resumed\x01",
            "I heard that … …. on your body\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Husband, husband, young wife ……\x01",
            "Of course this me too, about the lady\x01",
            "Because we are always thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, I know.\x01",
            "Thank you Joanna.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 2)
    Jump("loc_30B7")

    label("loc_3013")

    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "Eli-sama, lucky you in the body\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Husband, husband, young wife ……\x01",
            "Of course this me too, about the lady\x01",
            "Because we are always thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B7")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B75 end

    def Function_9_30BB(): pass

    label("Function_9_30BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_3166")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KDo you read Quincy's brochure?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Read\x01",          # 0
            "I do not read\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3155")
    Call(0, 11)
    TalkEnd(0xFF)
    Jump("loc_3161")

    label("loc_3155")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_3161")

    Jump("loc_3D82")

    label("loc_3166")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-41830, 1500, 40450, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, -43440, 60, 40740, 90)
    SetChrPos(0x102, -41310, 0, 40520, 90)
    SetChrPos(0x103, -42890, 0, 39580, 45)
    SetChrPos(0x104, -42860, 60, 41860, 135)
    SetChrPos(0x109, -42020, 0, 38900, 0)
    SetChrPos(0x105, -41650, 0, 42460, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FUh …… Hurry up.\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(400)
    OP_93(0x102, 0x10E, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00100FThis is Quincy's\x01",
            "Pamphlets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh\x01",
            "It is a solid binding.\x02\x03",
            "#00300FIn a very simple article\x01",
            "I can not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt can be done because it is a large company\x01",
            "It is how to put power.\x02\x03",
            "Information on the contents of the document is also\x01",
            "It seems that reliability is high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, that was nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FAlright ……\x01",
            "Anyway, let's quickly read it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x105,
        (
            "#10303FHmm, I looked through it roughly … …\x01",
            "I did not write much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FContent contradicting Minnes' remarks,\x01",
            "Did you find it……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FNo……\x01",
            "After all from such materials\x01",
            "I wonder whether there was impossible ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNo … … I found a contradiction.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_359C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_359C)
    Sleep(50)

    def lambda_35AC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35AC)
    Sleep(50)

    def lambda_35BC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35BC)
    Sleep(50)

    def lambda_35CC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35CC)

    ChrTalk(
        0x103,
        "#00205F……really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FAs usual\x01",
            "I'm counting on you Oy.\x02\x03",
            "#00300FSo what kind of contradiction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FConversation at the hotel yesterday\x01",
            "As long as you remember it well,\x01",
            "That's not that difficult answer.\x02\x03",
            "#00000FA word, Minnes spilled words ……\x01",
            "There are certainly contradictions with that.\x02\x03",
            "That is what Minnes\x01",
            "It is not \"the officer of Quincy\"\x01",
            "It is the proof that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FThat tips for that\x01",
            "In this article … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, that is ──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F── We waited,\x01",
            "Try to keep it silent once.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37D1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTo … Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, you just know that you are\x01",
            "It is somewhat shaku.\x02\x03",
            "#10309FSo, actually\x01",
            "Until it sticks to Minnes\x01",
            "Have you done your homework?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, that one.\x01",
            "I'm not playing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FNo, Waji says something\x01",
            "It is reasonable.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_390F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_390F)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00203FLloyd's answer is\x01",
            "There is also the possibility of being wrong,\x01",
            "It is dangerous to unify the idea here.\x02\x03",
            "#00211FAlso, always as usual\x01",
            "Have a nice place for Mr. Lloyd\x01",
            "It is shaku that can be done.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆ IBC (for testing)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                  # 0
            "【We will investigate】\x01",            # 1
            "[Let's not investigate]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AB5"),
        (1, "loc_3ABA"),
        (2, "loc_3AC2"),
        (SWITCH_DEFAULT, "loc_3ACA"),
    )


    label("loc_3AB5")

    Jump("loc_3ACA")

    label("loc_3ABA")

    SetScenarioFlags(0x177, 4)
    Jump("loc_3ACA")

    label("loc_3AC2")

    ClearScenarioFlags(0x177, 4)
    Jump("loc_3ACA")

    label("loc_3ACA")

    OP_29(0x87, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_END)), "loc_3C39")

    ChrTalk(
        0x101,
        (
            "#00006F(Rather, the latter is really like …).\x02\x03",
            "#00001FWow, I understood.\x01",
            "Well then once for everyone,\x01",
            "As I thought … ….\x02\x03",
            "For this material,\x01",
            "Let's make a note in the notebook.\x02\x03",
            "#00003F…… For now,\x01",
            "Pursue allegations of Minnes\x01",
            "Materials should have gathered.\x02\x03",
            "#00000FOnce at Harold's house\x01",
            "Let's go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's do that.\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_3D49")

    label("loc_3C39")


    ChrTalk(
        0x101,
        (
            "#00006F(Rather, the latter is really like …).\x02\x03",
            "#00001FWow, I understood.\x01",
            "Well then once for everyone,\x01",
            "As I thought … ….\x02\x03",
            "For this material,\x01",
            "Let's make a note in the notebook.\x02\x03",
            "#00003F… … The remainder is only the investigation of IBC.\x01",
            "Let's go looking up quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYeah, OK.\x02",
    )

    CloseMessageWindow()

    label("loc_3D49")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 5)
    SetChrPos(0x0, -43000, 60, 40720, 90)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_3D82")

    Return()

    # Function_9_30BB end

    def Function_10_3D83(): pass

    label("Function_10_3D83")

    EventBegin(0x0)
    Fade(500)
    OP_68(-45700, 1560, 2610, 0)
    MoveCamera(38, 32, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -44780, 60, 2500, 0)
    SetChrPos(0x102, -45960, 0, 2500, 0)
    SetChrPos(0x103, -46730, 0, 1660, 0)
    SetChrPos(0x104, -44030, 0, 1620, 0)
    SetChrPos(0x105, -45860, 0, 980, 0)
    SetChrPos(0x109, -44820, 0, 940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "Ah……\x01",
            "Eli lady, everyone … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Miscon's \"Maid\" frame … …\x01",
            "How about her? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(That's right ……\x01",
            "It might be nice. )\x02\x03",
            "#00000F(Erie,\x01",
            "Can you please ask me? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(I understood.\x01",
            "I think it is difficult, but …).\x02\x03",
            "#00100FHey Joanna,\x01",
            "I have a favor to you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes……\x01",
            "If you ask Ellie\x01",
            "With what.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "… ….\x01",
            "Mistake, Ko ………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#4SWHAAAAAA!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FThat was quite the reaction\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mumu, impossible ……\x01",
            "I do not care like mistaken … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FNo, no, it's okay.\x01",
            "My older brother guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHow are you going to do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEr, Joanna?\x01",
            "You do not have to worry.\x02\x03",
            "#00103FIf I search for it,\x01",
            "Even for the other maids\x01",
            "I think that you can participate … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … Um … after all …………\x01",
            "I'd like to let you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell, that is also sudden.\x01",
            "I am saved, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The maid of the lady … …\x01",
            "…… I, that's why …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHehe, thank you Joanna.\x01",
            "But do not push yourself, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … Please call me when you need it.\x01",
            "I will be heading soon …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we're counting on you\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43C0")

    ChrTalk(
        0x101,
        (
            "#00003F─ ─ Now, at last\x01",
            "Participants' frame was filled.\x02\x03",
            "#00000FGo to the city hall\x01",
            "Let 's report to Roy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_43C0")

    SetScenarioFlags(0x199, 6)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -45350, 60, 2400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_3D83 end

    def Function_11_43FA(): pass

    label("Function_11_43FA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S…… Our company as the forerunner of confectionery industry\x01",
            "For the future of confectionery, we are piling the day and night.\x01",
            "In this brochure, I did it\x01",
            "I would like to introduce one part of our company.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3SThe most important thing for sweets is,\x01",
            "Whether you think that it is \"delicious\"\x01",
            "Our company believes that it will exhaust into that one point.\x01",
            "For that reason,\x01",
            "\"Increase the quality of sweets\"\x01",
            "I will not make any compromise in that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3SThe confectionery factory is equipped with the latest equipment,\x01",
            "Maximum consideration for sanitation\x01",
            "Of course it is done,\x01",
            "Quality of materials used for sweets and\x01",
            "I also have a strong insistence on the place of origin.\x01",
            "Also about product development\x01",
            "Strict standards are stipulated.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3SOfficers taste products under development themselves,\x01",
            "It was judged whether it was a product that could withstand sales,\x01",
            "After several planning meetings\x01",
            "Finally get on the production line.\x01",
            "This will definitely make customers happy\x01",
            "For delivering the best sweets,\x01",
            "It is a tradition since the establishment of the company.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3SSo always have high quality sweets\x01",
            "Because it keeps providing it,\x01",
            "There is the present figure of Quincy Company ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_43FA end

    SaveToFile()

Try(main)
