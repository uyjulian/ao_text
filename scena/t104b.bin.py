from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t104b.bin",                # FileName
        "t104b",                    # MapName
        "t104b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t104b",                  # 0
        "Ryｹto",                 # 1
        "Marcy",                  # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Southwark",              # 7
        "Jeanetta",               # 8
        "Winona",                 # 9
        "Drona",                  # 10
        "Tourist",                # 11
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch24002.itc",                   # 02
        "chr/ch21802.itc",                   # 03
        "chr/ch21902.itc",                   # 04
        "chr/ch34402.itc",                   # 05
        "chr/ch27900.itc",                   # 06
        "chr/ch26600.itc",                   # 07
        "chr/ch32400.itc",                   # 08
        "chr/ch22002.itc",                   # 09
        "chr/ch26602.itc",                   # 0A
    ))

    DeclNpc(4294863227, 0,       2980,    90,   389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294866197, 0,       5880,    90,   385,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(4294869337, 119,     19090,   45,   453,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4294862496, 119,     8930,    45,   453,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294864296, 119,     10930,   225,  453,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294871176, 119,     20889,   225,  453,  0x0, 0,   5,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294873286, 119,     11039,   225,  453,  0x0, 0,   9,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4294871477, 119,     9050,    45,   453,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(4294965436, 0,       10640,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(3930,    0,       3420,    225,  389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3930,    0,       2299,    315,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)

    DeclActor(4294965526, 0,       8810,    1000,    4294965436, 1500,    10640,   0x007E, 0,  14, 0x0000)
    DeclActor(4294865646, 0,       2470,    1000,    4294863226, 1500,    2980,    0x007E, 0,  4,  0x0000)

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_3C5",          # 02, 2
        "Function_3_48E",          # 03, 3
        "Function_4_4B6",          # 04, 4
        "Function_5_4BA",          # 05, 5
        "Function_6_761",          # 06, 6
        "Function_7_968",          # 07, 7
        "Function_8_A22",          # 08, 8
        "Function_9_ADA",          # 09, 9
        "Function_10_B82",         # 0A, 10
        "Function_11_C12",         # 0B, 11
        "Function_12_C41",         # 0C, 12
        "Function_13_E94",         # 0D, 13
        "Function_14_EC3",         # 0E, 14
        "Function_15_EC7",         # 0F, 15
        "Function_16_1121",        # 10, 16
        "Function_17_11E1",        # 11, 17
    ))


    def Function_0_284(): pass

    label("Function_0_284")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C4"),
        (1, "loc_2D0"),
        (2, "loc_2DC"),
        (3, "loc_2E8"),
        (4, "loc_2F4"),
        (5, "loc_300"),
        (6, "loc_30C"),
        (SWITCH_DEFAULT, "loc_318"),
    )


    label("loc_2C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_300")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_33B")

    Return()

    # Function_0_284 end

    def Function_1_33C(): pass

    label("Function_1_33C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C4")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_33C")

    label("loc_3C4")

    Return()

    # Function_1_33C end

    def Function_2_3C5(): pass

    label("Function_2_3C5")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_439")
    Jump("loc_48D")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_48D")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)

    label("loc_48D")

    Return()

    # Function_2_3C5 end

    def Function_3_48E(): pass

    label("Function_3_48E")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_4B5")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B5")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_4B5")

    Return()

    # Function_3_48E end

    def Function_4_4B6(): pass

    label("Function_4_4B6")

    Call(0, 5)
    Return()

    # Function_4_4B6 end

    def Function_5_4BA(): pass

    label("Function_5_4BA")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_519")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_519")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_539")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_758")

    label("loc_539")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")
    Jump("loc_758")

    label("loc_54D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C")

    ChrTalk(
        0x8,
        (
            "Birthday parties, welcome parties,\x01",
            "farewell parties and on top of that,\x01",
            "proposals to your significant other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this establishment, we\x01",
            "are ready to help you as\x01",
            "much as possible with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please consult us, if you\x01",
            "like. We will treat you to\x01",
            "an excellent evening...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_73C")

    label("loc_69C")


    ChrTalk(
        0x8,
        (
            "At this establishment, we\x01",
            "are ready to help customers\x01",
            "with any of those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please consult us, if you\x01",
            "like. We will treat you to\x01",
            "an excellent evening...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C")

    Jump("loc_758")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_74F")
    Jump("loc_758")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_758")

    label("loc_758")

    Jump("loc_4C7")

    label("loc_75D")

    TalkEnd(0x8)
    Return()

    # Function_5_4BA end

    def Function_6_761(): pass

    label("Function_6_761")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(
        0xFE,
        (
            "It seems that it's the\x01",
            "birthday of the customer at\x01",
            "the central table today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were prepared. Everyone\x01",
            "in the store applauded and\x01",
            "sang the birthday song.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our master gets quite easily\x01",
            "taken into that mood and things\x01",
            "like that sometimes happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_948")

    label("loc_883")


    ChrTalk(
        0xFE,
        (
            "Now then, there's many parties\x01",
            "with dinner reservations\x01",
            "tonight and it'll be tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am terribly sorry, but customers\x01",
            "without a reservation should please\x01",
            "sit at the counter in the back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_948")

    Jump("loc_964")

    label("loc_94D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_95B")
    Jump("loc_964")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_964")

    label("loc_964")

    TalkEnd(0xFE)
    Return()

    # Function_6_761 end

    def Function_7_968(): pass

    label("Function_7_968")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A07")

    ChrTalk(
        0xFE,
        (
            "The young man at the\x01",
            "central table did a\x01",
            "quite refined thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to make some\x01",
            "kind of surprise at my\x01",
            "grandson's birthday too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1E")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A15")
    Jump("loc_A1E")

    label("loc_A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A1E")

    label("loc_A1E")

    TalkEnd(0xFE)
    Return()

    # Function_7_968 end

    def Function_8_A22(): pass

    label("Function_8_A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ABF")

    ChrTalk(
        0xFE,
        (
            "Well, the shopkeeper suddenly\x01",
            "spoke to me and I wondered what\x01",
            "he needed help with, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These kinds of ideas\x01",
            "aren't bad at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD6")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ACD")
    Jump("loc_AD6")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AD6")

    label("loc_AD6")

    TalkEnd(0xFE)
    Return()

    # Function_8_A22 end

    def Function_9_ADA(): pass

    label("Function_9_ADA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(
        0xFE,
        (
            "Actually, it's embarrassing\x01",
            "when you have these kinds\x01",
            "of things done to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Although watching\x01",
            "them is fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E")

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B75")
    Jump("loc_B7E")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B7E")

    label("loc_B7E")

    TalkEnd(0xFE)
    Return()

    # Function_9_ADA end

    def Function_10_B82(): pass

    label("Function_10_B82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(
        0xFE,
        (
            "That lady... They say\x01",
            "it's her birthday today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How enviable having\x01",
            "everyone celebrate it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0E")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C05")
    Jump("loc_C0E")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C0E")

    label("loc_C0E")

    TalkEnd(0xFE)
    Return()

    # Function_10_B82 end

    def Function_11_C12(): pass

    label("Function_11_C12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C26")
    Call(0, 12)
    Jump("loc_C3D")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C34")
    Jump("loc_C3D")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C3D")

    label("loc_C3D")

    TalkEnd(0xFE)
    Return()

    # Function_11_C12 end

    def Function_12_C41(): pass

    label("Function_12_C41")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD")

    ChrTalk(
        0xF,
        (
            "*sigh*, that gave me a\x01",
            "shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't believe that all the\x01",
            "employees and all the customers\x01",
            "would celebrate my birthday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I asked the store people for\x01",
            "their collaboration. It's\x01",
            "just a little surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha, it made me really\x01",
            "happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But why, Southwark?\x01",
            "Why'd you do all this\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. Seeing you depressed\x01",
            "like that, I couldn't\x01",
            "ignore you no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "What, then that means...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_E8B")

    label("loc_DFD")


    ChrTalk(
        0xE,
        (
            "...J-Just kidding. Haha,\x01",
            "I guess it was a little\x01",
            "cheesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...*cough*. The night is\x01",
            "long, let's enjoy it to\x01",
            "the fullest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Y-Yes㈱\x02",
    )

    CloseMessageWindow()

    label("loc_E8B")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_12_C41 end

    def Function_13_E94(): pass

    label("Function_13_E94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EA8")
    Call(0, 12)
    Jump("loc_EBF")

    label("loc_EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EB6")
    Jump("loc_EBF")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EBF")

    label("loc_EBF")

    TalkEnd(0xFE)
    Return()

    # Function_13_E94 end

    def Function_14_EC3(): pass

    label("Function_14_EC3")

    Call(0, 15)
    Return()

    # Function_14_EC3 end

    def Function_15_EC7(): pass

    label("Function_15_EC7")

    TalkBegin(0x10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F26")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F46")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1118")

    label("loc_F46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F5A")
    Jump("loc_1118")

    label("loc_F5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1118")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1054")

    ChrTalk(
        0x10,
        (
            "Sir, are you going to a\x01",
            "party tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At this store, we have a\x01",
            "great selection of\x01",
            "formal wear as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We can adjust their size to\x01",
            "fit you in no time, so\x01",
            "please, have a look around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10EE")

    label("loc_1054")


    ChrTalk(
        0x10,
        (
            "At this store, we have a\x01",
            "great selection of\x01",
            "formal wear as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We can adjust their size to\x01",
            "fit you in no time, so\x01",
            "please, have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EE")

    Jump("loc_1118")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1101")
    Jump("loc_1118")

    label("loc_1101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_110F")
    Jump("loc_1118")

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1118")

    label("loc_1118")

    Jump("loc_ED4")

    label("loc_111D")

    TalkEnd(0x10)
    Return()

    # Function_15_EC7 end

    def Function_16_1121(): pass

    label("Function_16_1121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11B8")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, it suits you\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, this dress has a\x01",
            "subdued design, so it can be used\x01",
            "in everyday situations as well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11C6")
    Jump("loc_11DD")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11D4")
    Jump("loc_11DD")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11DD")

    label("loc_11DD")

    TalkEnd(0xFE)
    Return()

    # Function_16_1121 end

    def Function_17_11E1(): pass

    label("Function_17_11E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_129C")

    ChrTalk(
        0xFE,
        (
            "I see, I was thinking about it\x01",
            "for the next party, however...\x01",
            "It can be used like that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under these circumstances,\x01",
            "I believe I'll buy some\x01",
            "accessories too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B3")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12AA")
    Jump("loc_12B3")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12B3")

    label("loc_12B3")

    TalkEnd(0xFE)
    Return()

    # Function_17_11E1 end

    SaveToFile()

Try(main)
