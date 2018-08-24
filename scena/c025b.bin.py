from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c025b.bin",                # FileName
        "c025b",                    # MapName
        "c025b",                    # Location
        0x000E,                     # MapIndex
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
        "c025b",                  # 0
        "Leyte",                  # 1
        "Pinset",                 # 2
        "Kｷken",                 # 3
    ))

    AddCharChip((
        "chr/ch10300.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch22302.itc",                   # 02
        "chr/ch32700.itc",                   # 03
        "chr/ch32702.itc",                   # 04
        "apl/ch50148.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21002.itc",                   # 07
    ))

    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294912986, 0,       52840,   90,   261,  0x0, 0,   1,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(4294915377, 0,       108370,  90,   261,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)

    ChipFrameInfo(292, 0)                                        # 0

    ScpFunction((
        "Function_0_124",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_1FF",          # 02, 2
        "Function_3_226",          # 03, 3
        "Function_4_227",          # 04, 4
        "Function_5_2AA",          # 05, 5
        "Function_6_3E9",          # 06, 6
    ))


    def Function_0_124(): pass

    label("Function_0_124")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_15C"),
        (1, "loc_168"),
        (2, "loc_174"),
        (3, "loc_180"),
        (4, "loc_18C"),
        (5, "loc_198"),
        (6, "loc_1A4"),
        (SWITCH_DEFAULT, "loc_1B0"),
    )


    label("loc_15C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_168")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_174")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_180")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_18C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_198")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1D3")

    Return()

    # Function_0_124 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_1_1D4")

    label("loc_1FE")

    Return()

    # Function_1_1D4 end

    def Function_2_1FF(): pass

    label("Function_2_1FF")

    SetChrPos(0x9, -58130, 0, 58620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    SetChrFlags(0x9, 0x10)

    label("loc_21F")

    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_2_1FF end

    def Function_3_226(): pass

    label("Function_3_226")

    Return()

    # Function_3_226 end

    def Function_4_227(): pass

    label("Function_4_227")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, before I knew it,\x01",
            "the sky has become all\x01",
            "dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband is coming\x01",
            "home, so I must hurry\x01",
            "and prepare dinner.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_227 end

    def Function_5_2AA(): pass

    label("Function_5_2AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")

    ChrTalk(
        0xFE,
        (
            "...Ah! There's a railway\x01",
            "book mixed in on the shelf\x01",
            "of my fashion magazines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is my father's doing for\x01",
            "sure. I wonder how many times\x01",
            "he'll use the same tactics.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_3E5")

    label("loc_375")


    ChrTalk(
        0xFE,
        (
            "My father does things like\x01",
            "this sometimes to try to\x01",
            "make me like the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, how impudent.\x02",
    )

    CloseMessageWindow()

    label("loc_3E5")

    TalkEnd(0xFE)
    Return()

    # Function_5_2AA end

    def Function_6_3E9(): pass

    label("Function_6_3E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493")

    ChrTalk(
        0xFE,
        (
            "One day I'd like to have\x01",
            "Ryｹ inherit the wholesale\x01",
            "store job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to that\x01",
            "boy, he thinks of nothing\x01",
            "but play. Boy oh boy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FE")

    label("loc_493")


    ChrTalk(
        0xFE,
        (
            "Ryｹ's Sunday School\x01",
            "grades are no good\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He shouldn't just play,\x01",
            "but study a little\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE")

    TalkEnd(0xFE)
    Return()

    # Function_6_3E9 end

    SaveToFile()

Try(main)
