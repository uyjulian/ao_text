from ScenarioHelper import *

def main():
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
        "tourist",                 # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "boy",                 # 5
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
        "Function_4_313",          # 04, 4
        "Function_5_3B3",          # 05, 5
        "Function_6_46A",          # 06, 6
        "Function_7_4D1",          # 07, 7
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2F8")

    ChrTalk(
        0xFE,
        (
            "We, on a honeymoon\x01",
            "I am in Mishram.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today so much\x01",
            "It was a wonderful day.\x01",
            "I must thank her and the goddess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_306")
    Jump("loc_30F")

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_30F")

    label("loc_30F")

    TalkEnd(0xFE)
    Return()

    # Function_3_270 end

    def Function_4_313(): pass

    label("Function_4_313")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_398")

    ChrTalk(
        0xFE,
        (
            "This fun and beautiful place is\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He also moved to the crossbell\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3A6")
    Jump("loc_3AF")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3AF")

    label("loc_3AF")

    TalkEnd(0xFE)
    Return()

    # Function_4_313 end

    def Function_5_3B3(): pass

    label("Function_5_3B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_44F")

    ChrTalk(
        0xFE,
        (
            "From now on the theme park night part\x01",
            "I'm going to see the night parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally already\x01",
            "I would like to take a break in the room ……\x01",
            "Haha, it is hard to say father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_466")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_45D")
    Jump("loc_466")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_466")

    label("loc_466")

    TalkEnd(0xFE)
    Return()

    # Function_5_3B3 end

    def Function_6_46A(): pass

    label("Function_6_46A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B6")

    ChrTalk(
        0xFE,
        (
            "Huhu, that girl is also waiting\x01",
            "I have to get ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_4CD")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4CD")

    label("loc_4CD")

    TalkEnd(0xFE)
    Return()

    # Function_6_46A end

    def Function_7_4D1(): pass

    label("Function_7_4D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_52B")

    ChrTalk(
        0xFE,
        "Dad, mommy, not yet! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not do it quickly\x01",
            "The parade is over!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_539")
    Jump("loc_542")

    label("loc_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_542")

    label("loc_542")

    TalkEnd(0xFE)
    Return()

    # Function_7_4D1 end

    SaveToFile()

Try(main)
