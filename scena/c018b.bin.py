from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c018b.bin",                # FileName
        "c018b",                    # MapName
        "c018b",                    # Location
        0x0005,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c018b",                  # 0
        "tourist",                 # 1
        "tourist",                 # 2
        "Citizen",                   # 3
        "Citizen",                   # 4
    ))

    AddCharChip((
        "chr/ch33100.itc",                   # 00
        "chr/ch33200.itc",                   # 01
        "chr/ch24500.itc",                   # 02
        "chr/ch22100.itc",                   # 03
    ))

    DeclNpc(4294960416, 4294967096, 4840,    0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294961327, 4294967096, 5070,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294953097, 4294967096, 6070,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294954196, 4294967096, 5980,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)

    ChipFrameInfo(304, 0)                                        # 0

    ScpFunction((
        "Function_0_130",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_209",          # 02, 2
        "Function_3_20A",          # 03, 3
        "Function_4_24E",          # 04, 4
        "Function_5_277",          # 05, 5
        "Function_6_2EC",          # 06, 6
    ))


    def Function_0_130(): pass

    label("Function_0_130")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_130 end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_1_1E0 end

    def Function_2_209(): pass

    label("Function_2_209")

    Return()

    # Function_2_209 end

    def Function_3_20A(): pass

    label("Function_3_20A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Is this the Orkis Tower at night …?\x01",
            "I will lose my words.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_20A end

    def Function_4_24E(): pass

    label("Function_4_24E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Uhufu, it is a truly spectacular night view.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_24E end

    def Function_5_277(): pass

    label("Function_5_277")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Certainly the night view is too much\x01",
            "It's beautiful, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all this kind of thing,\x01",
            "I want to see it with people I like.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_277 end

    def Function_6_2EC(): pass

    label("Function_6_2EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9")

    ChrTalk(
        0xFE,
        (
            "Yeah, I want a boyfriend ….\x01",
            "- Not!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    TurnDirection(0xB, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Do your best at this place.\x01",
            "Because I try not to think.\x01",
            "Do not say anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_93(0xB, 0x0, 0x1F4)
    SetScenarioFlags(0x0, 0)
    Jump("loc_441")

    label("loc_3A9")


    ChrTalk(
        0xFE,
        (
            "Orkis Tower Clean,\x01",
            "Orkis Tower Clean …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_441")

    TalkEnd(0xFE)
    Return()

    # Function_6_2EC end

    SaveToFile()

Try(main)
