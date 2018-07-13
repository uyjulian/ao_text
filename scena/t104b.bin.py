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
        "Function_6_75B",          # 06, 6
        "Function_7_97D",          # 07, 7
        "Function_8_A37",          # 08, 8
        "Function_9_AF1",          # 09, 9
        "Function_10_B92",         # 0A, 10
        "Function_11_C29",         # 0B, 11
        "Function_12_C58",         # 0C, 12
        "Function_13_EAF",         # 0D, 13
        "Function_14_EDE",         # 0E, 14
        "Function_15_EE2",         # 0F, 15
        "Function_16_1144",        # 10, 16
        "Function_17_11F5",        # 11, 17
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_517")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_752")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54B")
    Jump("loc_752")

    label("loc_54B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_73B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_691")

    ChrTalk(
        0x8,
        (
            "Birthdays parties, welcome parties, seeing off \x01",
            "parties and on top of that, proposals to your \x01",
            "significant others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this establishment, we are ready to help\x01",
            "you as much as possible with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please consult us, if you like,\x01",
            "to have an excellent night...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_736")

    label("loc_691")


    ChrTalk(
        0x8,
        (
            "At this establishment, we are ready to help as\x01",
            "much as possible the customer with his ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please consult us, if you like,\x01",
            "to have an excellent night...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_736")

    Jump("loc_752")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_749")
    Jump("loc_752")

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_752")

    label("loc_752")

    Jump("loc_4C7")

    label("loc_757")

    TalkEnd(0x8)
    Return()

    # Function_5_4BA end

    def Function_6_75B(): pass

    label("Function_6_75B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_899")

    ChrTalk(
        0xFE,
        (
            "It seems that today is the birthday\x01",
            "of the customer at the central table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Prepared for that, the man sang the\x01",
            "celebration song and I clapped my\x01",
            "hands with all the people in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our Master gets quite easily\x01",
            "taken into that mood and things\x01",
            "like that sometimes happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_95D")

    label("loc_899")


    ChrTalk(
        0xFE,
        (
            "Well then, tonight there're many persons for\x01",
            "dinner reservation and it's a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am very sorry, but customers without a reservation\x01",
            "should please seat at the counter in the back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95D")

    Jump("loc_979")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_970")
    Jump("loc_979")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_979")

    label("loc_979")

    TalkEnd(0xFE)
    Return()

    # Function_6_75B end

    def Function_7_97D(): pass

    label("Function_7_97D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A1C")

    ChrTalk(
        0xFE,
        (
            "The young man at the central\x01",
            "table did a quite refined thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to make some kind of surprise\x01",
            "at my grandson's birthday too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A33")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A2A")
    Jump("loc_A33")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A33")

    label("loc_A33")

    TalkEnd(0xFE)
    Return()

    # Function_7_97D end

    def Function_8_A37(): pass

    label("Function_8_A37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AD6")

    ChrTalk(
        0xFE,
        (
            "Well, being suddenly spoken to by the shopkeeper\x01",
            "made me think what could I help him with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "These kind of ideas aren't bad at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AE4")
    Jump("loc_AED")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AED")

    label("loc_AED")

    TalkEnd(0xFE)
    Return()

    # Function_8_A37 end

    def Function_9_AF1(): pass

    label("Function_9_AF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B77")

    ChrTalk(
        0xFE,
        (
            "Actually, when you go\x01",
            "through things like that,\x01",
            "it's embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, although\x01",
            "looking at them is fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8E")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B85")
    Jump("loc_B8E")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B8E")

    label("loc_B8E")

    TalkEnd(0xFE)
    Return()

    # Function_9_AF1 end

    def Function_10_B92(): pass

    label("Function_10_B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C0E")

    ChrTalk(
        0xFE,
        (
            "That miss...\x01",
            "They say that today it's her birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How enviable having\x01",
            "everyone celebrating it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C25")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C1C")
    Jump("loc_C25")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C25")

    label("loc_C25")

    TalkEnd(0xFE)
    Return()

    # Function_10_B92 end

    def Function_11_C29(): pass

    label("Function_11_C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C3D")
    Call(0, 12)
    Jump("loc_C54")

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C4B")
    Jump("loc_C54")

    label("loc_C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C54")

    label("loc_C54")

    TalkEnd(0xFE)
    Return()

    # Function_11_C29 end

    def Function_12_C58(): pass

    label("Function_12_C58")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(
        0xF,
        (
            "*haah*, that gave\x01",
            "me a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't believe that the employees and all the\x01",
            "customers would've celebrated my birthday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I asked the store people for their collaboration.\x01",
            "It's just a little surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Uh uh, it made me really happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But why, Mr. Southwark,\x01",
            "did you do all this for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hu hu, looking at you who were depressed,\x01",
            "I couldn't ignore you no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "What, that means...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_EA6")

    label("loc_E16")


    ChrTalk(
        0xE,
        (
            "...J-Just kidding.\x01",
            "Ha ha, I guess it was a little cheesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...*cough*.\x01",
            "The night is long, let's \x01",
            "enjoy it to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Y-Yes㈱\x02",
    )

    CloseMessageWindow()

    label("loc_EA6")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_12_C58 end

    def Function_13_EAF(): pass

    label("Function_13_EAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EC3")
    Call(0, 12)
    Jump("loc_EDA")

    label("loc_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ED1")
    Jump("loc_EDA")

    label("loc_ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EDA")

    label("loc_EDA")

    TalkEnd(0xFE)
    Return()

    # Function_13_EAF end

    def Function_14_EDE(): pass

    label("Function_14_EDE")

    Call(0, 15)
    Return()

    # Function_14_EDE end

    def Function_15_EE2(): pass

    label("Function_15_EE2")

    TalkBegin(0x10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1140")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_113B")

    label("loc_F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F73")
    Jump("loc_113B")

    label("loc_F73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1116")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107A")

    ChrTalk(
        0x10,
        (
            "Mister customer, are you going\x01",
            "out to a party tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At this store, we deal in a great\x01",
            "number of formal wears too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We can adjust their size to fit you in no time,\x01",
            "so please, have a look around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1111")

    label("loc_107A")


    ChrTalk(
        0x10,
        (
            "At this store, we deal in a great\x01",
            "number of formal wears too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We can adjust their size to fit you in no time,\x01",
            "so please, have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1111")

    Jump("loc_113B")

    label("loc_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1124")
    Jump("loc_113B")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1132")
    Jump("loc_113B")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_113B")

    label("loc_113B")

    Jump("loc_EEF")

    label("loc_1140")

    TalkEnd(0x10)
    Return()

    # Function_15_EE2 end

    def Function_16_1144(): pass

    label("Function_16_1144")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11CC")

    ChrTalk(
        0xFE,
        "Uhuhu, it suits you well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, this dress has\x01",
            "a sober design too, so it can\x01",
            "be used every day too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F1")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11DA")
    Jump("loc_11F1")

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11E8")
    Jump("loc_11F1")

    label("loc_11E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11F1")

    label("loc_11F1")

    TalkEnd(0xFE)
    Return()

    # Function_16_1144 end

    def Function_17_11F5(): pass

    label("Function_17_11F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12B0")

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
            "Under these circumstances, I believe\x01",
            "I'll buy some accessories too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C7")

    label("loc_12B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12BE")
    Jump("loc_12C7")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12C7")

    label("loc_12C7")

    TalkEnd(0xFE)
    Return()

    # Function_17_11F5 end

    SaveToFile()

Try(main)
