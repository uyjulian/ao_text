from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c031b.bin",                # FileName
        "c031b",                    # MapName
        "c031b",                    # Location
        0x002B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c031b",                  # 0
        "Helmer",               # 1
        "Joanna",             # 2
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
    ))

    DeclNpc(0,       4059,    7760,    180,  257,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(4294921947, 59,      3900,    360,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)

    ChipFrameInfo(236, 0)                                        # 0

    ScpFunction((
        "Function_0_EC",           # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1C7",          # 02, 2
        "Function_3_1C8",          # 03, 3
        "Function_4_1C9",          # 04, 4
        "Function_5_36B",          # 05, 5
    ))


    def Function_0_EC(): pass

    label("Function_0_EC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_124"),
        (1, "loc_130"),
        (2, "loc_13C"),
        (3, "loc_148"),
        (4, "loc_154"),
        (5, "loc_160"),
        (6, "loc_16C"),
        (SWITCH_DEFAULT, "loc_178"),
    )


    label("loc_124")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_130")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_13C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_148")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_154")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_160")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_16C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_178")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_184")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_19B")

    Return()

    # Function_0_EC end

    def Function_1_19C(): pass

    label("Function_1_19C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C6")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_19C")

    label("loc_1C6")

    Return()

    # Function_1_19C end

    def Function_2_1C7(): pass

    label("Function_2_1C7")

    Return()

    # Function_2_1C7 end

    def Function_3_1C8(): pass

    label("Function_3_1C8")

    Return()

    # Function_3_1C8 end

    def Function_4_1C9(): pass

    label("Function_4_1C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0")

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
    Jump("loc_367")

    label("loc_2D0")


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
            "英気を養ってI'd like to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367")

    TalkEnd(0xFE)
    Return()

    # Function_4_1C9 end

    def Function_5_36B(): pass

    label("Function_5_36B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")

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
            "#00012F(Well, I suppose …\x01",
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
    Jump("loc_526")

    label("loc_48C")


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
        "#00106FDo not touch it … ….?\x02",
    )

    CloseMessageWindow()

    label("loc_526")

    TalkEnd(0xFE)
    Return()

    # Function_5_36B end

    SaveToFile()

Try(main)
