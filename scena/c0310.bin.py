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
        "Function_7_1ABA",         # 07, 7
        "Function_8_1D34",         # 08, 8
        "Function_9_33A1",         # 09, 9
        "Function_10_40CE",        # 0A, 10
        "Function_11_476A",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(
        0xFE,
        (
            "It seems the Master will have\x01",
            "command of Orchis Tower from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the President has been\x01",
            "arrested, the Master is the only\x01",
            "one who can lead Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a heavy burden, but... I know he\x01",
            "will do his best for all of us, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_60F")

    label("loc_558")


    ChrTalk(
        0xFE,
        (
            "Now that the President has been\x01",
            "arrested, the Master is the only\x01",
            "one who can lead Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a heavy burden, but... I know he\x01",
            "will do his best for all of us, somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F")

    Jump("loc_1AB6")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    Call(0, 7)
    Jump("loc_6CD")

    label("loc_62F")


    ChrTalk(
        0xFE,
        (
            "Ever since the Master and Milady\x01",
            "were detained at Michelam, I feel\x01",
            "I haven't been myself, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a relief to be able\x01",
            "to see Milady like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD")

    Jump("loc_1AB6")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_833")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "...Milady... Have\x01",
            "you been in contact\x01",
            "with the Master?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FNo, I haven't heard anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Anyway... If I too\x01",
            "learn anything, I shall\x01",
            "contact you right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Milady and everyone, \x01",
            "please devote yourselves\x01",
            "to what you must do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FOf course we will, \x01",
            "Mr. Helmer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 2)
    Jump("loc_8C8")

    label("loc_833")


    ChrTalk(
        0xFE,
        (
            "If I learn anything about\x01",
            "the Master, I shall contact\x01",
            "you immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Milady and everyone, \x01",
            "please devote yourselves\x01",
            "to what you must do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8")

    Jump("loc_1AB6")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(
        0xFE,
        (
            "...The attack earlier was\x01",
            "a truly tragic event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it seems the end of\x01",
            "reconstruction activities is in sight...\x02",
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
            "I would like the Master\x01",
            "and the Mayor to develop\x01",
            "preventive measures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A5D")

    label("loc_9E0")


    ChrTalk(
        0xFE,
        (
            "Yesterday's attack was\x01",
            "a truly tragic event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would like the Master\x01",
            "and the Mayor to develop\x01",
            "preventive measures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5D")

    Jump("loc_1AB6")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6C")

    ChrTalk(
        0xFE,
        (
            "Both the Master and the Mayor\x01",
            "are dealing with the military\x01",
            "occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is just a rumor, but they\x01",
            "say even the CGF cannot \x01",
            "do a thing about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I am getting worried. I pray\x01",
            "the incident is resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C07")

    label("loc_B6C")


    ChrTalk(
        0xFE,
        (
            "They say the CGF cannot do anything\x01",
            "against the strength of the armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I am getting worried. I pray\x01",
            "the incident is resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C07")

    Jump("loc_1AB6")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE4")

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment\x01",
            "was shocking.\x02",
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
            "In the end, I wonder what\x01",
            "the cause really was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D5B")

    label("loc_CE4")


    ChrTalk(
        0xFE,
        "Yesterday's derailment was shocking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Various rumors are flying\x01",
            "about...but I wonder\x01",
            "what the real cause was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5B")

    Jump("loc_1AB6")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DD6")

    ChrTalk(
        0xFE,
        (
            "I think I heard sirens in the\x01",
            "direction of the West Street...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I am just hearing things?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EBE")

    ChrTalk(
        0xFE,
        (
            "The state independence proposal has\x01",
            "affected a lot of things. It seems\x01",
            "Master is busy dealing with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is meeting with Mayor Dieter at\x01",
            "Orchis Tower today... I do wish\x01",
            "he would watch out for his health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_108A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD5")

    ChrTalk(
        0xFE,
        (
            "The referendum on the question\x01",
            "of independence is nearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Master is carefully\x01",
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
            "personal interest in the answer too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1085")

    label("loc_FD5")


    ChrTalk(
        0xFE,
        (
            "The referendum on the question\x01",
            "of independence is nearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, what will the people of\x01",
            "Crossbell choose? It seems he has\x01",
            "personal interest in the answer too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1085")

    Jump("loc_1AB6")

    label("loc_108A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1111")

    ChrTalk(
        0xFE,
        (
            "The Master headed\x01",
            "for Orchis Tower\x01",
            "early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's conference... \x01",
            "I hope it ends without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_12DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1242")

    ChrTalk(
        0xFE,
        (
            "Lately, the Master is busy and\x01",
            "often rests at City Hall without\x01",
            "coming back to the mansion, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He called  just before and\x01",
            "it seems that today he will be able \x01",
            "to come home after a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to absolutely build up\x01",
            "his energy for tomorrow's\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D7")

    label("loc_1242")


    ChrTalk(
        0xFE,
        (
            "Tonight, we are going to \x01",
            "prepare a nutrient-rich\x01",
            "menu for the Master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to absolutely build up his\x01",
            "energy for tomorrow's conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D7")

    Jump("loc_1AB6")

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F9")

    ChrTalk(
        0xFE,
        (
            "When Chairman Hartmann's  was in the \x01",
            "congress, Master did his best to restrain\x01",
            "the Imperial and Republican Factions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, due to his cooperation\x01",
            "with the new Mayor, there were\x01",
            "finally no mean foe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too think that is\x01",
            "a very good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14A8")

    label("loc_13F9")


    ChrTalk(
        0xFE,
        (
            "I think Mr. Crois becoming\x01",
            "Mayor is a very good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the conference's main\x01",
            "session... I wish the Master and the\x01",
            "mayor to display their full abilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A8")

    Jump("loc_1AB6")

    label("loc_14AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(
        0xFE,
        (
            "Master and Mayor Dieter are\x01",
            "carefully preparing for the Trade \x01",
            "Conference beginning tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hardly returns to the\x01",
            "mansion anymore... \x01",
            "Oh, how I worry about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_174C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(
        0xFE,
        (
            "The people who moved in\x01",
            "next door recently...\x01",
            "...They are a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They run around in their car in the city, play \x01",
            "loud music in the dead of night... Their \x01",
            "intolerable actions really make them stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I complain,\x01",
            "they won't listen...\x01",
            "What to do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1747")

    label("loc_16A4")


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
            "Even if I complain,\x01",
            "they won't listen...\x01",
            "What to do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1747")

    Jump("loc_1AB6")

    label("loc_174C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A16")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "Well, well, if it isn't Milady Elie. \x01",
            "Welcome home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI'm back, Mr. Helmer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see, so this is\x01",
            "your home, Elie.\x02",
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
            "#00004FYeah... Well, it's\x01",
            "Chairman MacDowell's\x01",
            "residence after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, please don't make too much of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. All of you are Milady's\x01",
            "co-workers, so please,\x01",
            "make yourselves at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support Section has\x01",
            "restarted activities, so it is likely\x01",
            "you will all be very busy from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care of\x01",
            "Lady Elie, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course. Please leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, thank you Mr. Helmer. \x01",
            "I'll do my best to support them, too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x134, 1)
    Jump("loc_1AB6")

    label("loc_1A16")


    ChrTalk(
        0xFE,
        (
            "The Special Support Section has\x01",
            "restarted activities, so it is likely\x01",
            "you will all be very busy from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care of\x01",
            "Lady Elie, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB6")

    TalkEnd(0xFE)
    Return()

    # Function_6_43B end

    def Function_7_1ABA(): pass

    label("Function_7_1ABA")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        "Oh, everyone...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "M-Milady... \x01",
            "...It's you, Milady Elie...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMr. Helmer, Joanna. I'm back.\x01",
            "...Sorry for worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "......(*shiver*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since the Master's declaration of\x01",
            "invalidity, I wondered if you were safe,\x01",
            "Lady Elie. I couldn't think of anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is a relief to be able\x01",
            "to see Milady like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, thank you very much.\x02\x03",
            "#00103F...But right now, there's\x01",
            "somewhere I absolutely must go.\x02\x03",
            "#00101FCan both of you watch the\x01",
            "house for awhile longer?\x02",
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
            "Milady Elie, everyone...\x01",
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

    # Function_7_1ABA end

    def Function_8_1D34(): pass

    label("Function_8_1D34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1ECE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E79")

    ChrTalk(
        0xFE,
        (
            "So you are going to\x01",
            "that strange, giant\x01",
            "tree, Milady Elie...\x02",
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
            "#00104FDon't worry, Joanna. I am sure\x01",
            "everyone will protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yes. Just as they\x01",
            "have protected Milady\x01",
            "up until now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that you will return safely.\x01",
            "...Please, take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EC9")

    label("loc_1E79")


    ChrTalk(
        0xFE,
        (
            "I believe everyone will\x01",
            "return safely. ...Please,\x01",
            "take care of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC9")

    Jump("loc_339D")

    label("loc_1ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE9")
    Call(0, 7)
    Jump("loc_1F48")

    label("loc_1EE9")


    ChrTalk(
        0xFE,
        "It seems it is very dangerous outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Milady Elie, everyone...\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F48")

    Jump("loc_339D")

    label("loc_1F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_212B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CE")

    ChrTalk(
        0xFE,
        (
            "Master...\x01",
            "I wonder where\x01",
            "he has gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am just so worried about him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI didn't see him at\x01",
            "the address earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI wonder where grandfather is...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "...Ah, sorry!\x01",
            "I have made Milady\x01",
            "even more worried...\x02",
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
    Jump("loc_2126")

    label("loc_20CE")


    ChrTalk(
        0xFE,
        (
            "...I have made\x01",
            "Milady even\x01",
            "more worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Master... \x01",
            "I am sure he is safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2126")

    Jump("loc_339D")

    label("loc_212B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2265")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215D")
    Call(0, 10)
    Return()

    label("loc_215D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_END)), "loc_21DD")

    ChrTalk(
        0xFE,
        (
            "...I think I...\x01",
            "Will take part \x01",
            "in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Please call me when needed.\x01",
            "I will be right there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_21DD")


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
            "...I wonder if I can help\x01",
            "with that in some way...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2260")

    Jump("loc_339D")

    label("loc_2265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22E7")

    ChrTalk(
        0xFE,
        "To think the mining town's occupied...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I am scared... I feel\x01",
            "like something else is\x01",
            "going to happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339D")

    label("loc_22E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2348")

    ChrTalk(
        0xFE,
        "It sure has rained a lot lately...\x02",
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
    Jump("loc_339D")

    label("loc_2348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2356")
    Jump("loc_339D")

    label("loc_2356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2502")

    ChrTalk(
        0xFE,
        (
            "I must prepare a meal that will give Master\x01",
            "energy, as he is been working hard lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...But just what should I make, I wonder.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's right...\x01",
            "How about lamb?\x02\x03",
            "#00104FIt's high in protein, low in calories and\x01",
            "tastes good. I'm sure he will love it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "...That is a good idea...\x01",
            "You are so smart, Milady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FA-Ahaha. To be praised even\x01",
            "for something like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257E")

    label("loc_2502")


    ChrTalk(
        0xFE,
        (
            "I am on a diet and\x01",
            "not eating much, but\x01",
            "meat might be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just need to go shopping\x01",
            "at the department store...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257E")

    Jump("loc_339D")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_274A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2717")

    ChrTalk(
        0xFE,
        (
            "I heard there was a terrorist attack targeting\x01",
            "the Trade Conference the other day... \x01",
            "I thought I was going to have a heart attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since then, I can't stop worry\x01",
            "about Lady Elie and the Master...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FJoanna... \x01",
            "You worry too much.\x02\x03",
            "#00100FThere's also all the Support Section with me...\x01",
            "I'm sure I'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes... It is as you say, Milady.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2745")

    label("loc_2717")


    ChrTalk(
        0xFE,
        (
            "Everyone, please\x01",
            "take care of Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2745")

    Jump("loc_339D")

    label("loc_274A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27B6")

    ChrTalk(
        0xFE,
        (
            "Lady Elie... It seems the city\x01",
            "is on high alert today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_339D")

    label("loc_27B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_29B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F0")

    ChrTalk(
        0xFE,
        (
            "For tonight's dinner we\x01",
            "have Master's favorite\x01",
            "acerbic tomato dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Acerbic tomato salad,\x01",
            "acerbic tomato sauce spaghetti,\x01",
            "100% acerbic tomato juice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(W-Whoa...\x01",
            "What a painstaking menu.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Grandfather, to think you liked \x01",
            "acerbic tomatoes so much...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AC")

    label("loc_28F0")


    ChrTalk(
        0xFE,
        (
            "Today, we have Master's favorite\x01",
            "acerbic tomato dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say they are good\x01",
            "for your health, so I will\x01",
            "endure and eat them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FD-Don't overdo it, all right...?\x02",
    )

    CloseMessageWindow()

    label("loc_29AC")

    Jump("loc_339D")

    label("loc_29B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9F")

    ChrTalk(
        0xFE,
        (
            "This morning, I ran into our next\x01",
            "door neighbors by the entrance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They suddenly asked me if I wanted\x01",
            "to go on a drive with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I politely refused, of course.\x01",
            "Somehow they are over-familiar...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B36")

    label("loc_2A9F")


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
            "I politely refused, of course.\x01",
            "Somehow they are over-familiar...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B36")

    Jump("loc_339D")

    label("loc_2B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BE9")

    ChrTalk(
        0xFE,
        (
            "The new City Hall building will\x01",
            "be unveiled tomorrow, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty amazing already\x01",
            "with that curtain hanging over it. \x01",
            "I am positively giddy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339D")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF3")

    ChrTalk(
        0xFE,
        "(*draw draw*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm, Joanna? Are you drawing\x01",
            "something on the windows?\x02",
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
            "...T-The windows were foggy,\x01",
            "so without thinking, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "E-Excuse me. \x01",
            "I will get back to cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2D50")

    label("loc_2CF3")


    ChrTalk(
        0xFE,
        (
            "The sound of rain is oddly\x01",
            "distracting somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*. I don't like rainy days.\x02",
    )

    CloseMessageWindow()

    label("loc_2D50")

    Jump("loc_339D")

    label("loc_2D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_339D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EF")
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
            "#00100FI'm back, Joanna. Anything\x01",
            "out of the ordinary today?\x02",
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
            "Now that Milady is back from her\x01",
            "trip abroad, I can finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*gigge*, Joanna... There's no need to\x01",
            "worry about me so much, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is not true. For you see, Milady, and\x01",
            "the Master as well, are everything to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHu hu. A maid who thinks only of her masters.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Um, Lady Elie? Yesterday,\x01",
            "we received letters from the\x01",
            "young master and his wife...\x02",
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
        "#00005FCould it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Yes, it's from my parents\x01",
            "in the Republic and Empire.\x02\x03",
            "#00100FUntil now I've been getting them every so\x01",
            "often, but I've been getting them more\x01",
            "often ever since that Cult incident.\x02\x03",
            "#00104FMostly they're worried about my\x01",
            "grandfather and me, but lately\x01",
            "they've been encouraging me.\x02",
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
            "#00100FJoanna, I'll read them later, so\x01",
            "please hold on to them for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes... As you say, Milady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, I heard the Special \x01",
            "Support Section restarted... \x01",
            "Please, take care of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Master, the young master and his\x01",
            "wife...and myself as well, of course.\x01",
            "All of us are worried about you, Milady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, I understand.\x01",
            "Thank you, Joanna.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 2)
    Jump("loc_339D")

    label("loc_32EF")

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
            "The Master, the young master and his\x01",
            "wife...and myself as well, of course.\x01",
            "All of us are worried about you, Milady.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339D")

    TalkEnd(0xFE)
    Return()

    # Function_8_1D34 end

    def Function_9_33A1(): pass

    label("Function_9_33A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_3443")
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
            "#1KRead the Quincy Company pamphlet?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Read\x01",        # 0
            "Do Not\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3432")
    Call(0, 11)
    TalkEnd(0xFF)
    Jump("loc_343E")

    label("loc_3432")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_343E")

    Jump("loc_40CD")

    label("loc_3443")

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
        "#00105FLet's see... Ah, here it is.\x02",
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
            "#00305FWow... \x01",
            "It's even bound.\x02\x03",
            "#00300FIt looks very\x01",
            "well made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThey are a large company so they are\x01",
            "able to put that much more into it.\x02\x03",
            "I think we can trust\x01",
            "whatever's written inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, I'm glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FAlright... For now, let's\x01",
            "read through it, shall we?\x02",
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
            "#10303FHmm. We just skimmed it, but it doesn't\x01",
            "seem like there's anything important here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FDid you find a contradiction between\x01",
            "this and Minneth's statements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FH-Hmm...maybe\x01",
            "this might not be\x01",
            "too useful for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNo... I found something.\x02",
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

    def lambda_38AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38AB)
    Sleep(50)

    def lambda_38BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38BB)
    Sleep(50)

    def lambda_38CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_38CB)
    Sleep(50)

    def lambda_38DB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_38DB)

    ChrTalk(
        0x103,
        "#00205F...Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, we can always\x01",
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
            "#00000FIt was just a few words, but what he\x01",
            "said...it contradicts what's written here.\x02\x03",
            "And, it's enough to prove\x01",
            "Minneth isn't an employee\x01",
            "of the Quincy Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FY-You got that\x01",
            "much from this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, you see──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F──Wait, keep quiet\x01",
            "about that for now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AE3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AE3)
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
            "#10300FHu hu, it's shocking that only\x01",
            "you would have the answer.\x02\x03",
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
        (
            "#00203FNo, it is also as\x01",
            "Mr. Wazy said.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C19():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C19)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00203FIt is possible your answer is wrong,\x01",
            "Mr. Lloyd. So it is dangerous\x01",
            "to pool our thoughts here.\x02\x03",
            "#00211FIt is also shocking that\x01",
            "you always, always manage\x01",
            "to steal the show, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC8")
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
            "◆IBC? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",             # 0
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
        (0, "loc_3DB3"),
        (1, "loc_3DB8"),
        (2, "loc_3DC0"),
        (SWITCH_DEFAULT, "loc_3DC8"),
    )


    label("loc_3DB3")

    Jump("loc_3DC8")

    label("loc_3DB8")

    SetScenarioFlags(0x177, 4)
    Jump("loc_3DC8")

    label("loc_3DC0")

    ClearScenarioFlags(0x177, 4)
    Jump("loc_3DC8")

    label("loc_3DC8")

    OP_29(0x87, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_END)), "loc_3F62")

    ChrTalk(
        0x101,
        (
            "#00006F(I guess the latter remark was her real feelings...)\x02\x03",
            "#00001FA-Alright. For now,\x01",
            "everyone think about\x01",
            "what we've learned...\x02\x03",
            "I'll write down the main points of this\x01",
            "material in the Detective Notebook.\x02\x03",
            "#00003F...At present, we've gathered\x01",
            "enough material to secure\x01",
            "Minneth's guilt.\x02\x03",
            "#00000FFor now, let's return\x01",
            "to Mr. Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's return there.\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_4094")

    label("loc_3F62")


    ChrTalk(
        0x101,
        (
            "#00006F(I guess the latter remark was her real feelings...)\x02\x03",
            "#00001FA-Alright. For now,\x01",
            "everyone think about\x01",
            "what we've learned...\x02\x03",
            "I'll write down the main points of this\x01",
            "material in the Detective Notebook.\x02\x03",
            "#00003F...All that's left is IBC. Let's\x01",
            "head there and investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, roger.\x02",
    )

    CloseMessageWindow()

    label("loc_4094")

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

    label("loc_40CD")

    Return()

    # Function_9_33A1 end

    def Function_10_40CE(): pass

    label("Function_10_40CE")

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
            "Ah... Milady Elie\x01",
            "and everyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(How about her as the\x01",
            ""maid" for the pageant?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Right... \x01",
            "She would be perfect.)\x02\x03",
            "#00000F(Elie, will you\x01",
            "ask her for us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Understood. I think this'll\x01",
            "be difficult, though...)\x02\x03",
            "#00100FI have a request\x01",
            "for you, Joanna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes...\x01",
            "If it is a request from Lady Elie,\x01",
            "I will do anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "...*gasp*...\x01",
            "A p-pageant...\x02",
        )
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
        "#00205F...An impressive reaction.\x02",
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
            "#00302FI'm tellin' you, you'll be fine.\x01",
            "I personally guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWhat're you guaranteeing now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FU-Umm, Joanna? \x01",
            "Don't worry about it.\x02\x03",
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
            "...Umm... I think... \x01",
            "I would like to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FW-Well that was fast. \x01",
            "You're helping us out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am Milady's maid,\x01",
            "after all, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, thank you, Joanna.\x01",
            "But don't overdo it, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Please call me when needed.\x01",
            "I will be right there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThanks. We're counting on you.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4730")

    ChrTalk(
        0x101,
        (
            "#00003F──Well then, with this we finally have\x01",
            "a sufficient number of participants.\x02\x03",
            "#00000FLet's go to the City Meeting Hall\x01",
            "and report to Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_4730")

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

    # Function_10_40CE end

    def Function_11_476A(): pass

    label("Function_11_476A")

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
            "#3SRegarding confectioneries, the\x01",
            "most important thing is whether\x01",
            "it is tasty. Our company is run\x01",
            "on this single point. For this\x01",
            "reason,  we make no compromises\x01",
            "on quality.\x07\x00\x02",
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
            "#3SOur factories are outfitted with the\x01",
            "latest equipment. Though hygiene is of\x01",
            "course our primary concern, we have an\x01",
            "obsession with quality ingredients and\x01",
            "the places they come from.\x01",
            "Furthermore, we have strict standards\x01",
            "for product development.\x07\x00\x02",
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
            "#3SOur employees themselves sample developmental\x01",
            "products, and judge whether they are worthy of\x01",
            "sale. It is only after many planning meetings\x01",
            "that products finally enter our manufacturing\x01",
            "lines. In order to bring you only confectioneries\x01",
            "you will surely love, this tradition has been\x01",
            "passed down since our company's founding.\x07\x00\x02",
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

    # Function_11_476A end

    SaveToFile()

Try(main)
