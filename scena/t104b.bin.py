from ScenarioHelper import *

def main():
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
        "lute",               # 1
        "Mesh",               # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Southwark",               # 7
        "Janetta",             # 8
        "Winona",               # 9
        "Dorona",               # 10
        "tourist",                 # 11
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
        "Function_6_727",          # 06, 6
        "Function_7_8BC",          # 07, 7
        "Function_8_966",          # 08, 8
        "Function_9_9FF",          # 09, 9
        "Function_10_A9A",         # 0A, 10
        "Function_11_B2C",         # 0B, 11
        "Function_12_B5B",         # 0C, 12
        "Function_13_D84",         # 0D, 13
        "Function_14_DB3",         # 0E, 14
        "Function_15_DB7",         # 0F, 15
        "Function_16_1006",        # 10, 16
        "Function_17_10BC",        # 11, 17
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_723")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_525")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_525")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71E")

    label("loc_545")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_559")
    Jump("loc_71E")

    label("loc_559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")

    ChrTalk(
        0x8,
        (
            "Birthday celebration, welcome party, pick-up party,\x01",
            "Proposal to an important person ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In our shop they are as far as possible\x01",
            "We are preparing to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not mind, please contact us once.\x01",
            "The guests should have the supreme night ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_702")

    label("loc_66A")


    ChrTalk(
        0x8,
        (
            "In our shop, our customer's preferences\x01",
            "I will help you as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not mind, please contact us once.\x01",
            "The guests should have the supreme night ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702")

    Jump("loc_71E")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_715")
    Jump("loc_71E")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_71E")

    label("loc_71E")

    Jump("loc_4C7")

    label("loc_723")

    TalkEnd(0x8)
    Return()

    # Function_5_4BA end

    def Function_6_727(): pass

    label("Function_6_727")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_810")

    ChrTalk(
        0xFE,
        (
            "Today the customer at the central table\x01",
            "It seems like a birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the preparation of a man,\x01",
            "Clapping with all the people in the store\x01",
            "I sang a celebration song.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Master of our family,\x01",
            "Because it is quite nice for that\x01",
            "Sometimes there are such things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_89C")

    label("loc_810")


    ChrTalk(
        0xFE,
        (
            "Well, tonight for dinner reservations\x01",
            "There are a lot of trouble entering it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sorry, but customers without reservations\x01",
            "I'd like to ask you at the back counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C")

    Jump("loc_8B8")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8AF")
    Jump("loc_8B8")

    label("loc_8AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8B8")

    label("loc_8B8")

    TalkEnd(0xFE)
    Return()

    # Function_6_727 end

    def Function_7_8BC(): pass

    label("Function_7_8BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94B")

    ChrTalk(
        0xFE,
        (
            "Young people in that middle table also\x01",
            "I will do something pretty strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also on the next grandchild's birthday\x01",
            "I wanted to do some surprise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_962")

    label("loc_94B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_959")
    Jump("loc_962")

    label("loc_959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_962")

    label("loc_962")

    TalkEnd(0xFE)
    Return()

    # Function_7_8BC end

    def Function_8_966(): pass

    label("Function_8_966")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(
        0xFE,
        (
            "No, suddenly heard from the shopkeeper\x01",
            "I thought what would be helped … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This kind of taste is not bad either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FB")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9F2")
    Jump("loc_9FB")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9FB")

    label("loc_9FB")

    TalkEnd(0xFE)
    Return()

    # Function_8_966 end

    def Function_9_9FF(): pass

    label("Function_9_9FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A7F")

    ChrTalk(
        0xFE,
        (
            "In fact, this is what\x01",
            "If you are the side to be done\x01",
            "It's embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, in looking for\x01",
            "I hope that's interesting, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A96")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A8D")
    Jump("loc_A96")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A96")

    label("loc_A96")

    TalkEnd(0xFE)
    Return()

    # Function_9_9FF end

    def Function_10_A9A(): pass

    label("Function_10_A9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B11")

    ChrTalk(
        0xFE,
        (
            "That old sister,\x01",
            "Today is your birthday ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Congratulations to everyone\x01",
            "I'm so jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B28")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B1F")
    Jump("loc_B28")

    label("loc_B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B28")

    label("loc_B28")

    TalkEnd(0xFE)
    Return()

    # Function_10_A9A end

    def Function_11_B2C(): pass

    label("Function_11_B2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B40")
    Call(0, 12)
    Jump("loc_B57")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B4E")
    Jump("loc_B57")

    label("loc_B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B57")

    label("loc_B57")

    TalkEnd(0xFE)
    Return()

    # Function_11_B2C end

    def Function_12_B5B(): pass

    label("Function_12_B5B")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE")

    ChrTalk(
        0xF,
        (
            "Ha, the little while ago\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No way, the clerk and all the customers\x01",
            "I celebrated my birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hahaha, please ask the store person for cooperation.\x01",
            "It's a little surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hehe, I was very happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "でもでも、なんでSouthwarkさんは\x01",
            "Are you going to do this far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, look at you falling down,\x01",
            "You can not leave it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Well, that's ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_D7B")

    label("loc_CEE")


    ChrTalk(
        0xE,
        (
            "…… Nothing.\x01",
            "Haha, I guess it was a little shabby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Kohon.\x01",
            "The night is long.\x01",
            "Let's have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Is an injection\x02",
    )

    CloseMessageWindow()

    label("loc_D7B")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_12_B5B end

    def Function_13_D84(): pass

    label("Function_13_D84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D98")
    Call(0, 12)
    Jump("loc_DAF")

    label("loc_D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DA6")
    Jump("loc_DAF")

    label("loc_DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DAF")

    label("loc_DAF")

    TalkEnd(0xFE)
    Return()

    # Function_13_D84 end

    def Function_14_DB3(): pass

    label("Function_14_DB3")

    Call(0, 15)
    Return()

    # Function_14_DB3 end

    def Function_15_DB7(): pass

    label("Function_15_DB7")

    TalkBegin(0x10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1002")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E22")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E42")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FFD")

    label("loc_E42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E56")
    Jump("loc_FFD")

    label("loc_E56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4B")

    ChrTalk(
        0x10,
        (
            "Customers, even tonight at the party\x01",
            "Are you going out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In our shop we also have formal attire\x01",
            "We handle a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Since size adjustment etc can be done immediately,\x01",
            "Please have a look, if very well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FD3")

    label("loc_F4B")


    ChrTalk(
        0x10,
        (
            "In our shop we also have formal attire\x01",
            "We handle a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Since size adjustment etc can be done immediately,\x01",
            "Please have a look, if very well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD3")

    Jump("loc_FFD")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FE6")
    Jump("loc_FFD")

    label("loc_FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_FF4")
    Jump("loc_FFD")

    label("loc_FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_FFD")

    label("loc_FFD")

    Jump("loc_DC4")

    label("loc_1002")

    TalkEnd(0x10)
    Return()

    # Function_15_DB7 end

    def Function_16_1006(): pass

    label("Function_16_1006")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1093")

    ChrTalk(
        0xFE,
        "Uhufu, it fits well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Plus, this dress is\x01",
            "Design is calm, too,\x01",
            "Whether you can use it even in daily life ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B8")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_10A1")
    Jump("loc_10B8")

    label("loc_10A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10AF")
    Jump("loc_10B8")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_10B8")

    label("loc_10B8")

    TalkEnd(0xFE)
    Return()

    # Function_16_1006 end

    def Function_17_10BC(): pass

    label("Function_17_10BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1158")

    ChrTalk(
        0xFE,
        (
            "Indeed, to the next party\x01",
            "I thought that … ….\x01",
            "That is also ants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is this case so many things\x01",
            "Would you like to buy small items as well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116F")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1166")
    Jump("loc_116F")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_116F")

    label("loc_116F")

    TalkEnd(0xFE)
    Return()

    # Function_17_10BC end

    SaveToFile()

Try(main)
