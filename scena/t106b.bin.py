from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t106b.bin",                # FileName
        "t106b",                    # MapName
        "t106b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 1, 0, 2],
    )

    BuildStringList((
        "t106b",                  # 0
        "Tourist",                # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Boy",                    # 5
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch33300.itc",                   # 01
        "chr/ch23402.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch23800.itc",                   # 04
    ))

    DeclNpc(4294866256, 0,       1070,    180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294871447, 0,       3210,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(101919,  400,     4294964447, 0,    453,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(101940,  0,       4294965576, 180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(99339,   0,       4294967087, 135,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)

    ChipFrameInfo(340, 0)                                        # 0

    ScpFunction((
        "Function_0_154",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_270",          # 03, 3
        "Function_4_304",          # 04, 4
        "Function_5_39B",          # 05, 5
        "Function_6_456",          # 06, 6
        "Function_7_4CE",          # 07, 7
    ))


    def Function_0_154(): pass

    label("Function_0_154")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_194"),
        (1, "loc_1A0"),
        (2, "loc_1AC"),
        (3, "loc_1B8"),
        (4, "loc_1C4"),
        (5, "loc_1D0"),
        (6, "loc_1DC"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_194")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_20B")

    Return()

    # Function_0_154 end

    def Function_1_20C(): pass

    label("Function_1_20C")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_22B")
    Jump("loc_26E")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_257")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_26E")

    label("loc_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_265")
    Jump("loc_26E")

    label("loc_265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_26E")

    label("loc_26E")

    Return()

    # Function_1_20C end

    def Function_2_26F(): pass

    label("Function_2_26F")

    Return()

    # Function_2_26F end

    def Function_3_270(): pass

    label("Function_3_270")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2E9")

    ChrTalk(
        0xFE,
        (
            "We came at Michelam\x01",
            "on our honeymoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today was a very great day.\x01",
            "We must thank the Goddess.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_300")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_300")

    label("loc_300")

    TalkEnd(0xFE)
    Return()

    # Function_3_270 end

    def Function_4_304(): pass

    label("Function_4_304")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_380")

    ChrTalk(
        0xFE,
        (
            "It's such a funny and pretty\x01",
            "place like no other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, even moving to Crossbell\x01",
            "could be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397")

    label("loc_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_397")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_397")

    label("loc_397")

    TalkEnd(0xFE)
    Return()

    # Function_4_304 end

    def Function_5_39B(): pass

    label("Function_5_39B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_43B")

    ChrTalk(
        0xFE,
        (
            "We're going to see the night\x01",
            "parade at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I'd like to\x01",
            "rest in our room, but...\x01",
            "Ha ha, being a dad is tough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_449")
    Jump("loc_452")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_452")

    label("loc_452")

    TalkEnd(0xFE)
    Return()

    # Function_5_39B end

    def Function_6_456(): pass

    label("Function_6_456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(
        0xFE,
        (
            "Uh uh, that child is waiting too,\x01",
            "I have to finish to prepare quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_4CA")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4CA")

    label("loc_4CA")

    TalkEnd(0xFE)
    Return()

    # Function_6_456 end

    def Function_7_4CE(): pass

    label("Function_7_4CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_53A")

    ChrTalk(
        0xFE,
        "Papa, mama, are you not ready yet!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we don't hurry up,\x01",
            "the parade will start!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_551")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_548")
    Jump("loc_551")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_551")

    label("loc_551")

    TalkEnd(0xFE)
    Return()

    # Function_7_4CE end

    SaveToFile()

Try(main)
