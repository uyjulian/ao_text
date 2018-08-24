from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1403.bin",                # FileName
        "t1403",                    # MapName
        "t1403",                    # Location
        0x00BB,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1403",                  # 0
        "Tourist",                # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch34200.itc",                   # 01
        "chr/ch20400.itc",                   # 02
        "chr/ch20500.itc",                   # 03
        "chr/ch32200.itc",                   # 04
        "chr/ch33200.itc",                   # 05
    ))

    DeclNpc(94029,   8000,    4294959057, 135,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(93470,   8000,    4294960066, 180,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(91110,   20000,   4294963497, 270,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(89930,   20000,   4294963437, 90,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(95379,   32000,   1120,    315,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(94440,   32000,   140,     315,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)

    ChipFrameInfo(376, 0)                                        # 0

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_2DC",          # 02, 2
        "Function_3_34D",          # 03, 3
        "Function_4_39B",          # 04, 4
        "Function_5_3E5",          # 05, 5
        "Function_6_41D",          # 06, 6
        "Function_7_46C",          # 07, 7
        "Function_8_49C",          # 08, 8
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_178 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_23E")
    Jump("loc_2DB")

    label("loc_23E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_24C")
    Jump("loc_2DB")

    label("loc_24C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_25A")
    Jump("loc_2DB")

    label("loc_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_29A")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2DB")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2A8")
    Jump("loc_2DB")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2B6")
    Jump("loc_2DB")

    label("loc_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2C4")
    Jump("loc_2DB")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2D2")
    Jump("loc_2DB")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2DB")

    label("loc_2DB")

    Return()

    # Function_1_230 end

    def Function_2_2DC(): pass

    label("Function_2_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32C")
    Sound(135, 1, 100, 0)
    Jump("loc_32F")

    label("loc_32C")

    OP_24(0x87)

    label("loc_32F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_347")
    SetMapFlags(0x2000)
    Jump("loc_34C")

    label("loc_347")

    ClearMapFlags(0x2000)

    label("loc_34C")

    Return()

    # Function_2_2DC end

    def Function_3_34D(): pass

    label("Function_3_34D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hoh hoh ho, don't worry.\x01",
            "I won't lose to the\x01",
            "young ones just yet.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_34D end

    def Function_4_39B(): pass

    label("Function_4_39B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grampa, the staircase is\x01",
            "pretty long. Will you be\x01",
            "all right~?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_39B end

    def Function_5_3E5(): pass

    label("Function_5_3E5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*pant pant*... That's\x01",
            "enough, I'm pooped...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_3E5 end

    def Function_6_41D(): pass

    label("Function_6_41D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "C'mon, hang in there.\x01",
            "It's just a little\x01",
            "further to the top floor.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_41D end

    def Function_7_46C(): pass

    label("Function_7_46C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*... What an\x01",
            "amazing height...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_46C end

    def Function_8_49C(): pass

    label("Function_8_49C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Really... I'm getting a\x01",
            "little dizzy...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_49C end

    SaveToFile()

Try(main)
