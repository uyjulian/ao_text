from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Helmer",                 # 1
        "Joanna",                 # 2
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
        "Function_7_1A38",         # 07, 7
        "Function_8_1C90",         # 08, 8
        "Function_9_32A2",         # 09, 9
        "Function_10_3F93",        # 0A, 10
        "Function_11_45CD",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556")

    ChrTalk(
        0xFE,
        (
            "It seems the master will\x01",
            "have command of Orchis\x01",
            "Tower from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the President has been\x01",
            "arrested, the master is the only\x01",
            "one who can lead Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a heavy burden, but...\x01",
            "I know he we do his best for\x01",
            "all of us, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_60B")

    label("loc_556")


    ChrTalk(
        0xFE,
        (
            "Now that the President has been\x01",
            "arrested, the master is the only\x01",
            "one who can lead Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a heavy burden, but...\x01",
            "I know he we do his best for\x01",
            "all of us, somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B")

    Jump("loc_1A34")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B")
    Call(0, 7)
    Jump("loc_6C9")

    label("loc_62B")


    ChrTalk(
        0xFE,
        (
            "Ever since the master and milady\x01",
            "were detained at Michelam, I feel\x01",
            "I haven't been myself, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a relief to be\x01",
            "able to see milady like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9")

    Jump("loc_1A34")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "...Milady... Have you\x01",
            "been in contact with the\x01",
            "master?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FNo, I haven't heard\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Anyway... If I\x01",
            "learn anything, I shall\x01",
            "contact you right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please devote\x01",
            "yourselves to what you\x01",
            "must do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FOf course we will,\x01",
            "Helmer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 2)
    Jump("loc_8A1")

    label("loc_818")


    ChrTalk(
        0xFE,
        (
            "If you learn anything\x01",
            "about the master, please\x01",
            "contact me immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please devote\x01",
            "yourselves to what you\x01",
            "must do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A1")

    Jump("loc_1A34")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B8")

    ChrTalk(
        0xFE,
        (
            "...The attack earlier\x01",
            "was a truly tragic\x01",
            "event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it seems the end\x01",
            "of reconstruction\x01",
            "activities is in sight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even now, I feel no\x01",
            "small degree of fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would like the master\x01",
            "or the mayor to develop\x01",
            "preventive measures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A34")

    label("loc_9B8")


    ChrTalk(
        0xFE,
        (
            "Yesterday's attack was a\x01",
            "truly tragic event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would like the master\x01",
            "or the mayor to develop\x01",
            "preventive measures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A34")

    Jump("loc_1A34")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B41")

    ChrTalk(
        0xFE,
        (
            "Both the master and the mayor\x01",
            "are dealing with the military\x01",
            "occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is just a rumor, but they\x01",
            "say even the CGF cannot do a\x01",
            "thing about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm getting worried.\x01",
            "I pray the incident is\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BDB")

    label("loc_B41")


    ChrTalk(
        0xFE,
        (
            "They say the CGF cannot do\x01",
            "anything against the strength\x01",
            "of the armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm getting worried.\x01",
            "I pray the incident is\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDB")

    Jump("loc_1A34")

    label("loc_BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment\x01",
            "was surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People are making a fuss over\x01",
            "whether it was caused by falling\x01",
            "rocks or a giant monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, I wonder\x01",
            "what the cause really\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D34")

    label("loc_CBA")


    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment\x01",
            "was surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Various rumors are flying\x01",
            "about... but I wonder\x01",
            "what the real cause was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D34")

    Jump("loc_1A34")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(
        0xFE,
        (
            "I heard sirens in the\x01",
            "direction of West\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'm just hearing\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A34")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E88")

    ChrTalk(
        0xFE,
        (
            "The state independence proposal has\x01",
            "affected a lot of things. It seems the\x01",
            "master is busy dealing with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is meeting with Mayor Dieter at\x01",
            "Orchis Tower today... I do wish\x01",
            "he'd watch out for his health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A34")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9B")

    ChrTalk(
        0xFE,
        (
            "The referendum on the\x01",
            "question of independence\x01",
            "is nearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The master is carefully\x01",
            "considering his position\x01",
            "on the matter, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, what will the people of\x01",
            "Crossbell choose? It seems he has\x01",
            "personal interest in the answer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1047")

    label("loc_F9B")


    ChrTalk(
        0xFE,
        (
            "The referendum on the\x01",
            "question of independence\x01",
            "is nearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, what will the people of\x01",
            "Crossbell choose? It seems he has\x01",
            "personal interest in the answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")

    Jump("loc_1A34")

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10D4")

    ChrTalk(
        0xFE,
        (
            "The master headed for\x01",
            "Orchis Tower early this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's main session...\x01",
            "I hope it ends without\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A34")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_129D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206")

    ChrTalk(
        0xFE,
        (
            "Lately, the master is busy and\x01",
            "often rests at city hall without\x01",
            "coming back to the mansion, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He called earlier and it seems he\x01",
            "will be able to come home this\x01",
            "evening after a long time away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to absolutely\x01",
            "build up his energy for\x01",
            "tomorrow's conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1298")

    label("loc_1206")


    ChrTalk(
        0xFE,
        (
            "Tonight, I am going to\x01",
            "prepare a nutrient-rich\x01",
            "menu for the master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to absolutely\x01",
            "build up his energy for\x01",
            "tomorrow's conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1298")

    Jump("loc_1A34")

    label("loc_129D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A4")

    ChrTalk(
        0xFE,
        (
            "In Chairman Hartmann's congress, the\x01",
            "master did his best to restrain the\x01",
            "Imperial and Republican factions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, due to his cooperation\x01",
            "with the new mayor, they've\x01",
            "finally become equal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that is a good\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_144E")

    label("loc_13A4")


    ChrTalk(
        0xFE,
        (
            "I think Mr. Crois\x01",
            "becoming mayor is a good\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the conference's main\x01",
            "session... I want the master and the\x01",
            "mayor to display their full abilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144E")

    Jump("loc_1A34")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(
        0xFE,
        (
            "Starting tomorrow, the master and\x01",
            "Mayor Dieter will prepare carefully\x01",
            "for the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hardly returns to the\x01",
            "mansion anymore... Oh,\x01",
            "how I worry about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A34")

    label("loc_1512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_16E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(
        0xFE,
        (
            "The people who moved in\x01",
            "next door recently...\x01",
            "they're a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They drive their car in the city, play loud\x01",
            "music in the dead of night... Their intolerable\x01",
            "actions really make them stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I complain, they\x01",
            "won't listen... What to\x01",
            "do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E0")

    label("loc_163D")


    ChrTalk(
        0xFE,
        (
            "The intolerable actions of the\x01",
            "people who moved in next door\x01",
            "recently really make them stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I complain, they\x01",
            "won't listen... What to\x01",
            "do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E0")

    Jump("loc_1A34")

    label("loc_16E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1996")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "Well, well, if it isn't\x01",
            "Lady Elie. Welcome home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI'm back, Helmer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see, so this is your\x01",
            "home, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FWhat a big mansion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... Well, it is\x01",
            "Chairman MacDowell's\x01",
            "residence after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha. Please don't make\x01",
            "too much of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. All of you are Lady\x01",
            "Elie's co-workers, so please,\x01",
            "make yourselves at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support Section has\x01",
            "restarted activities, so it is likely\x01",
            "you'll all be very busy from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care of Lady\x01",
            "Elie, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, of course. Leave it\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, thank you Helmer.\x01",
            "I'll do my best to\x01",
            "support them, too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x134, 1)
    Jump("loc_1A34")

    label("loc_1996")


    ChrTalk(
        0xFE,
        (
            "The Special Support Section has\x01",
            "restarted activities, so it is likely\x01",
            "you'll all be very busy from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care of Lady\x01",
            "Elie, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A34")

    TalkEnd(0xFE)
    Return()

    # Function_6_43B end

    def Function_7_1A38(): pass

    label("Function_7_1A38")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        "Oh, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "M-Milady... It's you,\x01",
            "Lady Elie!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FJoanna and Helmer. I'm\x01",
            "back. ...Sorry for\x01",
            "worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...(*shiver*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since the master's invalidity\x01",
            "declaration, I wondered if you were safe,\x01",
            "Lady Elie. I couldn't think of anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is a relief to be\x01",
            "able to see milady like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you very much.\x02\x03",
            "#00103F...But right now,\x01",
            "there's somewhere I\x01",
            "absolutely must go.\x02\x03",
            "#00101FCan both of you watch\x01",
            "the house a while\x01",
            "longer?\x02",
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
            "Lady Elie, everyone...\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    SetScenarioFlags(0x1CC, 7)
    Return()

    # Function_7_1A38 end

    def Function_8_1C90(): pass

    label("Function_8_1C90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    ChrTalk(
        0xFE,
        (
            "So you are going to that\x01",
            "strange, giant tree,\x01",
            "Lady Elie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FDon't worry, Joanna. I'm\x01",
            "sure everyone will\x01",
            "protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yes. Just as they\x01",
            "have protected Milady up\x01",
            "until now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that you'll\x01",
            "return safely. ...Please,\x01",
            "take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E20")

    label("loc_1DD0")


    ChrTalk(
        0xFE,
        (
            "I believe everyone will\x01",
            "return safely. ...Please,\x01",
            "take care of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E20")

    Jump("loc_329E")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E40")
    Call(0, 7)
    Jump("loc_1E98")

    label("loc_1E40")


    ChrTalk(
        0xFE,
        (
            "It's extremely dangerous\x01",
            "outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady Elie, everyone...\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E98")

    Jump("loc_329E")

    label("loc_1E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201C")

    ChrTalk(
        0xFE,
        (
            "The master... I wonder\x01",
            "where he's gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just so worried\x01",
            "about him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI didn't see him at the\x01",
            "address earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FI wonder where\x01",
            "grandfather went...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "...Ah, sorry! I made\x01",
            "milady even more\x01",
            "worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...No, I'm all right.\x02\x03",
            "#00100FAlthough I think you\x01",
            "worry too much, Joanna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "U-Understood...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 3)
    Jump("loc_2070")

    label("loc_201C")


    ChrTalk(
        0xFE,
        (
            "...I made milady even\x01",
            "more worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The master... I'm sure\x01",
            "he's safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2070")

    Jump("loc_329E")

    label("loc_2075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A7")
    Call(0, 10)
    Return()

    label("loc_20A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_END)), "loc_2138")

    ChrTalk(
        0xFE,
        (
            "...I knew it...\x01",
            "Participating in the pageant\x01",
            "was the right choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Please call me when\x01",
            "needed. I'll be right\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_2138")


    ChrTalk(
        0xFE,
        (
            "I heard a charity event is\x01",
            "being held in Governmental\x01",
            "District today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder if I can\x01",
            "help with that in some\x01",
            "way...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BB")

    Jump("loc_329E")

    label("loc_21C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2241")

    ChrTalk(
        0xFE,
        (
            "To think the mining\x01",
            "town's occupied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm scared... I feel\x01",
            "like something else is\x01",
            "going to happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329E")

    label("loc_2241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_22A2")

    ChrTalk(
        0xFE,
        (
            "It sure has rained a lot\x01",
            "lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't dry the\x01",
            "laundry. *sigh*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329E")

    label("loc_22A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_22B0")
    Jump("loc_329E")

    label("loc_22B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245F")

    ChrTalk(
        0xFE,
        (
            "I want to prepare a meal that\x01",
            "will give the master energy, as\x01",
            "he's been working hard lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But just what should\x01",
            "I make, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's right... How about\x01",
            "lamb?\x02\x03",
            "#00104FIt's high in protein, low in\x01",
            "calories and tastes good.\x01",
            "I'm sure he will love it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "...That's a good idea..\x01",
            "You're so smart, milady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FA-Ahaha. To be praised\x01",
            "even for something like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24DA")

    label("loc_245F")


    ChrTalk(
        0xFE,
        (
            "I'm on a diet and not\x01",
            "eating much, but meat\x01",
            "might be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just need to go\x01",
            "shopping at the\x01",
            "department store...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DA")

    Jump("loc_329E")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_269A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266A")

    ChrTalk(
        0xFE,
        (
            "I heard there was a terrorist attack targeting\x01",
            "the trade conference the other day... I\x01",
            "thought I was going to have a heart attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since then, I can't\x01",
            "stop worrying about Lady\x01",
            "Elie and the master...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FJoanna... You worry too\x01",
            "much.\x02\x03",
            "#00100FThe Support Section is\x01",
            "here for me... I'm sure\x01",
            "I'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes... It is as you say,\x01",
            "milady.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2695")

    label("loc_266A")


    ChrTalk(
        0xFE,
        (
            "Everyone, please take\x01",
            "care of milady.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2695")

    Jump("loc_329E")

    label("loc_269A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2706")

    ChrTalk(
        0xFE,
        (
            "Lady Elie... It seems\x01",
            "the city is on high\x01",
            "alert today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_329E")

    label("loc_2706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2845")

    ChrTalk(
        0xFE,
        (
            "For tonight's dinner we\x01",
            "have the master's favorite\x01",
            "acerbic tomato dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Acerbic tomato salad, acerbic\x01",
            "tomato sauce spaghetti, 100%\x01",
            "acerbic tomato juice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(W-Whoa... What a\x01",
            "painstaking menu.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Grandfather, to think\x01",
            "you liked acerbic\x01",
            "tomatoes that much...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2900")

    label("loc_2845")


    ChrTalk(
        0xFE,
        (
            "Today, we have Master's\x01",
            "favorite acerbic tomato\x01",
            "dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say they're good for\x01",
            "your health, so I will\x01",
            "endure and eat them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FD-Don't overdo it, all\x01",
            "right...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2900")

    Jump("loc_329E")

    label("loc_2905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D1")

    ChrTalk(
        0xFE,
        (
            "This morning, I ran into\x01",
            "our next door neighbors\x01",
            "by the entrance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They suddenly asked me\x01",
            "if I wanted to go on a\x01",
            "drive with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I politely refused, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A46")

    label("loc_29D1")


    ChrTalk(
        0xFE,
        (
            "This morning, our neighbors\x01",
            "suddenly invited me to go\x01",
            "on a drive with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I politely refused, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A46")

    Jump("loc_329E")

    label("loc_2A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AF7")

    ChrTalk(
        0xFE,
        (
            "The new City Hall\x01",
            "building will be unveiled\x01",
            "tomorrow, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty amazing already\x01",
            "with that curtain hanging over\x01",
            "it. I'm positively giddy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329E")

    label("loc_2AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C03")

    ChrTalk(
        0xFE,
        "(*squeek, squeek*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm, Joanna? Are you\x01",
            "drawing something on the\x01",
            "windows?\x02",
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
            "...T-The windows were\x01",
            "foggy, so without\x01",
            "thinking, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "E-Excuse me. I'll get\x01",
            "back to cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2C60")

    label("loc_2C03")


    ChrTalk(
        0xFE,
        (
            "The sound of rain is\x01",
            "oddly distracting\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I don't like\x01",
            "rainy days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C60")

    Jump("loc_329E")

    label("loc_2C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_329E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EF")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Welcome home, Lady Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI'm back, Joanna.\x01",
            "Anything out of the\x01",
            "ordinary today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No... Thankfully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that milady is back\x01",
            "from her trip abroad, I\x01",
            "can finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, Joanna... There's\x01",
            "no need to worry about\x01",
            "me so much, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's not true. For you see,\x01",
            "milady, and the master as\x01",
            "well, are everything to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha. A maid who thinks\x01",
            "only of her master.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Um, Lady Elie? Yesterday, we\x01",
            "received letters from the young\x01",
            "master and his wife, but...\x02",
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
        "#00005FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Yes, they're from my parents in the\x01",
            "Republic and Empire.\x02\x03",
            "#00100FUntil now I've gotten them every so\x01",
            "often, but I've been getting them more\x01",
            "often ever since that cult incident.\x02\x03",
            "#00104FThey're mostly worried about my\x01",
            "grandfather and me, but lately they've\x01",
            "been encouraging me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(...Family, huh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FJoanna, I'll read them\x01",
            "later, so please hold on\x01",
            "to them for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes... As you say,\x01",
            "milady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, I heard the Special Support\x01",
            "Section restarted... Please,\x01",
            "take care of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The master, the young master and his\x01",
            "wife... and myself as well, of course.\x01",
            "All of us are worried about you, milady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I understand.\x01",
            "Thank you, Joanna.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 2)
    Jump("loc_329E")

    label("loc_31EF")

    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "Lady Elie, please take\x01",
            "care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The master, the young master and his\x01",
            "wife... and myself as well, of course.\x01",
            "All of us are worried about you, milady.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1C90 end

    def Function_9_32A2(): pass

    label("Function_9_32A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_3344")
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
            "#1KRead the Quincy Company\x01",
            "pamphlet?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Read\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3333")
    Call(0, 11)
    TalkEnd(0xFF)
    Jump("loc_333F")

    label("loc_3333")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_333F")

    Jump("loc_3F92")

    label("loc_3344")

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
        (
            "#00105FLet's see... Ah, here it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(400)
    OP_93(0x102, 0x10E, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00100FThis is the Quincy\x01",
            "Company pamphlet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWow... It's even bound.\x02\x03",
            "#00300FIt looks very well made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThey're a large company\x01",
            "so they're able to put\x01",
            "that much more into it.\x02\x03",
            "I think we can trust\x01",
            "whatever's written\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I'm glad to hear\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FAlright... For now,\x01",
            "let's read through it,\x01",
            "shall we?\x02",
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
            "#10303FHmm. I just skimmed it, but\x01",
            "it doesn't seem like there's\x01",
            "anything important here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FDid you find a\x01",
            "contradiction between this\x01",
            "and Minneth's statements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FH-Hmm... I thought this\x01",
            "might not be too useful\x01",
            "for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWait... I found\x01",
            "something.\x02",
        )
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

    def lambda_37AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37AB)
    Sleep(50)

    def lambda_37BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37BB)
    Sleep(50)

    def lambda_37CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_37CB)
    Sleep(50)

    def lambda_37DB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37DB)

    ChrTalk(
        0x103,
        "#00205FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, we can always\x01",
            "count on you, can't we.\x02\x03",
            "#00300FSo, what is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThinking about what Minneth told us\x01",
            "yesterday at the hotel, his answers\x01",
            "weren't all that complicated.\x02\x03",
            "#00000FIt was just a few words, but what\x01",
            "he said... it contradicts what's\x01",
            "written here.\x02\x03",
            "And, it's enough to prove Minneth\x01",
            "isn't an employee of the Quincy\x01",
            "Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FY-You got that much from\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, you see─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F─Wait, keep quiet about\x01",
            "that for now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39DC():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39DC)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh... What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, it's shocking that\x01",
            "only you would have the\x01",
            "answer.\x02\x03",
            "#10309FIn that case, why not\x01",
            "save it for when we\x01",
            "thrust it at Minneth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FH-Hey. I'm not messing\x01",
            "around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FNo, it's as Wazy said.\x02",
    )

    CloseMessageWindow()

    def lambda_3B07():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B07)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00203FIt's possible your answer is\x01",
            "wrong, Lloyd. So it's dangerous\x01",
            "to pool our thoughts here.\x02\x03",
            "#00211FIt's also shocking that you\x01",
            "always, always manage to steal\x01",
            "the show, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAE")
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
            "◆IBC? (Test use)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",             # 0
            "[Investigated]\x01",          # 1
            "[Not Investigated]\x01",      # 2
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
        (0, "loc_3C99"),
        (1, "loc_3C9E"),
        (2, "loc_3CA6"),
        (SWITCH_DEFAULT, "loc_3CAE"),
    )


    label("loc_3C99")

    Jump("loc_3CAE")

    label("loc_3C9E")

    SetScenarioFlags(0x177, 4)
    Jump("loc_3CAE")

    label("loc_3CA6")

    ClearScenarioFlags(0x177, 4)
    Jump("loc_3CAE")

    label("loc_3CAE")

    OP_29(0x87, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_END)), "loc_3E2F")

    ChrTalk(
        0x101,
        (
            "#00006F(That last one seems like\x01",
            "how she really feels...)\x02\x03",
            "#00001FAlright. For now, everyone\x01",
            "think about what we've\x01",
            "learned...\x02\x03",
            "I'll write down the main\x01",
            "points of this material in\x01",
            "my detective notebook.\x02\x03",
            "#00003FAt present, we've gathered\x01",
            "enough material to secure\x01",
            "Minneth's guilt.\x02\x03",
            "#00000FFor now, let's return to\x01",
            "Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's.\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_3F59")

    label("loc_3E2F")


    ChrTalk(
        0x101,
        (
            "#00006F(That last one seems like\x01",
            "how she really feels...)\x02\x03",
            "#00001FAlright. For now,\x01",
            "everyone think about what\x01",
            "we've learned...\x02\x03",
            "I'll write down the main\x01",
            "points of this material\x01",
            "in my detective notebook.\x02\x03",
            "#00003FAll that's left is IBC.\x01",
            "Let's head there and\x01",
            "investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, roger.\x02",
    )

    CloseMessageWindow()

    label("loc_3F59")

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

    label("loc_3F92")

    Return()

    # Function_9_32A2 end

    def Function_10_3F93(): pass

    label("Function_10_3F93")

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
            "Ah... Miss Elie and\x01",
            "everyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(How about her as the\x01",
            "maid for the pageant?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Right... She'd be\x01",
            "perfect.)\x02\x03",
            "#00000F(Elie, will you ask her\x01",
            "for us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Understood. I think\x01",
            "this'll be difficult,\x01",
            "though...)\x02\x03",
            "#00100FI have a request for\x01",
            "you, Joanna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes... If it is a\x01",
            "request from Lady Elie,\x01",
            "I will do anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Joanna to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "...Aaaa... p-pageant...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#4S...Whaaaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F...An impressive\x01",
            "reaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I-I can't... For me to\x01",
            "appear in a pageant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI'm telling you, it'll\x01",
            "be fine. I personally\x01",
            "guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWhat are you\x01",
            "guaranteeing now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FU-Umm, Joanna? Don't\x01",
            "worry about it.\x02\x03",
            "#00103FIf we ask around, I think\x01",
            "we'll find another maid\x01",
            "who'll participate...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Umm... I think... I'd\x01",
            "like to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell that was fast.\x01",
            "You're helping us out,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am milady's maid,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha, thank you, Joanna.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Please call me when\x01",
            "needed. I'll be right\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks. We're counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4593")

    ChrTalk(
        0x101,
        (
            "#00003F─Alright. With this\x01",
            "we've finally filled our\x01",
            "quota.\x02\x03",
            "#00000FLet's head to City\x01",
            "Meeting Hall and report\x01",
            "to Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_4593")

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

    # Function_10_3F93 end

    def Function_11_45CD(): pass

    label("Function_11_45CD")

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
            "#3S...Our company stands alone in the confectionery\x01",
            "business, working day and night, searching for our\x01",
            "next product. Through this pamphlet, we would like\x01",
            "to introduce you to a small part of our company.\x07\x00\x02",
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
            "#3SRegarding confectioneries, the most important thing is\x01",
            "whether it's tasty. Our company is run on this single\x01",
            "point. For this reason, we make no compromises on quality.\x07\x00\x02",
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
            "#3SOur factories are outfitted with the latest equipment.\x01",
            "Though hygiene is of course our primary concern, we\x01",
            "have an obsession with quality ingredients and the\x01",
            "places they come from. Furthermore, we have strict\x01",
            "standards for product development.\x07\x00\x02",
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
            "#3SOur employees themselves sample developmental products,\x01",
            "and impartially judge whether they are worthy of sale. It\x01",
            "is only after many planning meetings that products finally\x01",
            "enter our manufacturing lines. In order to bring you only\x01",
            "confectioneries you'll surely love, this tradition has\x01",
            "been passed down since our company's founding.\x07\x00\x02",
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
            "#3SThe present Quincy Company exists\x01",
            "to continually bring you the best\x01",
            "in quality confectioneries...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_45CD end

    SaveToFile()

Try(main)
