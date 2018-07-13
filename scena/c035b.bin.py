from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c035b.bin",                # FileName
        "c035b",                    # MapName
        "c035b",                    # Location
        0x002D,                     # MapIndex
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
        "c035b",                  # 0
        "Yuri",                   # 1
        "Sykes",                  # 2
        "Reggie",                 # 3
    ))

    AddCharChip((
        "chr/ch44100.itc",                   # 00
        "chr/ch47500.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch44102.itc",                   # 03
    ))

    DeclNpc(7989,    200,     1600,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5699,    0,       469,     45,   261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7780,    0,       4294966486, 0,    261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    ChipFrameInfo(280, 0)                                        # 0

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_231",          # 03, 3
        "Function_4_232",          # 04, 4
        "Function_5_494",          # 05, 5
        "Function_6_49E",          # 06, 6
        "Function_7_6BB",          # 07, 7
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_150"),
        (1, "loc_15C"),
        (2, "loc_168"),
        (3, "loc_174"),
        (4, "loc_180"),
        (5, "loc_18C"),
        (6, "loc_198"),
        (SWITCH_DEFAULT, "loc_1A4"),
    )


    label("loc_150")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_15C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_168")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_174")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_180")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_18C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_198")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1C7")

    Return()

    # Function_0_118 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0x334, 0x2904, 0xFFFFF31C, 0x3804, 0x3E8)
    Sleep(300)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 3700, 270)
    SetChrPos(0xA, -500, 0, 3700, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_2_1F3 end

    def Function_3_231(): pass

    label("Function_3_231")

    Return()

    # Function_3_231 end

    def Function_4_232(): pass

    label("Function_4_232")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC")

    ChrTalk(
        0xFE,
        "...What do you want in the dead of night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't tell you that I forgot...\x01",
            "What you did to us during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00605F(Did...\x01",
            "Anything happen with them?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, you see, it's like we\x01",
            "couldn't avoid it happening...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F(Honestly...causing stupid trouble\x01",
            "in this delicate time...)\x02\x03",
            "#00600F(Don't absolutely let your guard down\x01",
            "until tomorrow's conference is over.\x01",
            "...Understood?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(R-Roger.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_490")

    label("loc_3FC")


    ChrTalk(
        0xFE,
        (
            "I won't tell you that I forgot...\x01",
            "What you did to us during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll make you regret it one day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(So damn persistent...)\x02",
    )

    CloseMessageWindow()

    label("loc_490")

    TalkEnd(0xFE)
    Return()

    # Function_4_232 end

    def Function_5_494(): pass

    label("Function_5_494")

    TalkBegin(0xFE)
    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_5_494 end

    def Function_6_49E(): pass

    label("Function_6_49E")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647")

    ChrTalk(
        0x9,
        (
            "That Yuri is in a\x01",
            "really bad mood...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if we went to the Entertainment District\x01",
            "for a change of pace, it seems there're plenty\x01",
            "of officers due to VIPs security or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, then...\x01",
            "What about we go for a drive\x01",
            "at night on the mountain path?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There will be few passersby at\x01",
            "this hour and we could go all\x01",
            "out at our heart's' content...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ooh, that could be a nice idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6B2")

    label("loc_647")


    ChrTalk(
        0x9,
        (
            "Alright, being this the case,\x01",
            "let's go propose it to Yuri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Reggie, prepare the car.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Got it.\x02",
    )

    CloseMessageWindow()

    label("loc_6B2")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_49E end

    def Function_7_6BB(): pass

    label("Function_7_6BB")

    TalkBegin(0xFE)
    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_7_6BB end

    SaveToFile()

Try(main)
