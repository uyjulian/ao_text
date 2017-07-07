from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1070.bin",                # FileName
        "t1070",                    # MapName
        "t1070",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1070",                  # 0
        "Mariah",               # 1
        "Tyler",               # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Waji",                   # 7
        "Randy",               # 8
        "Noel",                 # 9
        "Franc",                 # 10
    ))

    AddCharChip((
        "chr/ch32400.itc",                   # 00
        "chr/ch25900.itc",                   # 01
        "chr/ch33000.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch03000.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(4294960796, 0,       5000,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294960996, 0,       9500,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6119,    0,       2240,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(5550,    0,       10000,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       9000,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294966796, 0,       9000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   3,   255,  0)

    DeclActor(4294962596, 0,       5000,    1000,    4294960796, 1500,    5000,    0x007E, 0,  8,  0x0000)

    ChipFrameInfo(636, 0)                                        # 0

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_4FB",          # 02, 2
        "Function_3_532",          # 03, 3
        "Function_4_73D",          # 04, 4
        "Function_5_AAA",          # 05, 5
        "Function_6_C0E",          # 06, 6
        "Function_7_1113",         # 07, 7
        "Function_8_11F0",         # 08, 8
        "Function_9_11F4",         # 09, 9
        "Function_10_1835",        # 0A, 10
        "Function_11_1B92",        # 0B, 11
        "Function_12_1D13",        # 0C, 12
        "Function_13_1D9B",        # 0D, 13
        "Function_14_1F15",        # 0E, 14
        "Function_15_2098",        # 0F, 15
        "Function_16_2AB5",        # 10, 16
        "Function_17_2B0E",        # 11, 17
        "Function_18_2B67",        # 12, 18
        "Function_19_2BC0",        # 13, 19
        "Function_20_2C0B",        # 14, 20
        "Function_21_2C5D",        # 15, 21
        "Function_22_3E58",        # 16, 22
        "Function_23_3EAA",        # 17, 23
        "Function_24_3F2E",        # 18, 24
        "Function_25_3F87",        # 19, 25
        "Function_26_3FD9",        # 1A, 26
        "Function_27_4024",        # 1B, 27
        "Function_28_4050",        # 1C, 28
        "Function_29_409B",        # 1D, 29
        "Function_30_50F5",        # 1E, 30
        "Function_31_5E76",        # 1F, 31
        "Function_32_6DB2",        # 20, 32
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_342")
    Jump("loc_47C")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_350")
    Jump("loc_47C")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100, 0, 5000, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1200, 0, 5000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_3AB")

    label("loc_3A1")

    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3AB")

    Jump("loc_47C")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_3BE")
    Jump("loc_47C")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_421")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_3FC")
    TurnDirection(0x10, 0x11, 0)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x11, 0x10, 0)
    ClearChrFlags(0x11, 0x10)

    label("loc_3FC")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -5340, 0, 1100, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_47C")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_43E")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47C")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_47C")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_473")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_47C")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    Event(0, 15)
    Jump("loc_4FA")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_4BB")
    Event(0, 21)
    Jump("loc_4FA")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_4CC")
    Event(0, 29)
    Jump("loc_4FA")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_4DD")
    Event(0, 30)
    Jump("loc_4FA")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_4EE")
    Event(0, 31)
    Jump("loc_4FA")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 32)

    label("loc_4FA")

    Return()

    # Function_1_334 end

    def Function_2_4FB(): pass

    label("Function_2_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_51A")

    label("loc_514")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531")

    Return()

    # Function_2_4FB end

    def Function_3_532(): pass

    label("Function_3_532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_543")
    Jump("loc_739")

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_551")
    Jump("loc_739")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_55F")
    Jump("loc_739")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_67B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")

    ChrTalk(
        0x11,
        (
            "#06406FOnee, from a little while ago\x01",
            "The state is strange, is not it ~!\x02\x03",
            "#06402FDid something happen on the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo~……\x01",
            "That's a bit, from me\x01",
            "Is it hard to explain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#06405FIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_676")

    label("loc_63A")


    ChrTalk(
        0x11,
        (
            "#06406FOnee, from a little while ago\x01",
            "The state is strange, is not it ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676")

    Jump("loc_739")

    label("loc_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")
    Call(0, 5)
    Jump("loc_70F")

    label("loc_696")


    ChrTalk(
        0x11,
        (
            "#06409FMr. Lloyd, this necklace\x01",
            "Please give me a present ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNo, no, no way out of hand.\x02",
    )

    CloseMessageWindow()

    label("loc_70F")

    Jump("loc_739")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_722")
    Jump("loc_739")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_730")
    Jump("loc_739")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_739")

    label("loc_739")

    TalkEnd(0xFE)
    Return()

    # Function_3_532 end

    def Function_4_73D(): pass

    label("Function_4_73D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_AA6")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_AA6")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_AA6")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_9E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_937")

    ChrTalk(
        0x10,
        (
            "#10106FHa … … Although there was a danger,\x01",
            "No way to really swim suit … …\x02\x03",
            "#10101FTo not prevent that degree of attack,\x01",
            "I do not have enough training yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F…… Go, sorry.\x01",
            "I too, as soon as I notice it a little more\x01",
            "I may have managed to do something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10114FOh, no!\x01",
            "Fortunately I did not get hurt!\x02\x03",
            "#10103FI am embarrassed, but … …\x01",
            "I would like to devote this to a spring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Wha, what will you go through … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_9DE")

    label("loc_937")


    ChrTalk(
        0x10,
        (
            "#10106FHaa …… That demon's beast\x01",
            "I can not prevent attacks,\x01",
            "I do not have enough training yet.\x02\x03",
            "#10101FThanks and I feel embarrassed … …\x01",
            "With this as a spring, I have to devote!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DE")

    Jump("loc_AA6")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE")
    Call(0, 5)
    Jump("loc_A6E")

    label("loc_9FE")


    ChrTalk(
        0x10,
        (
            "#10106FHere, this amazing necklace,\x01",
            "Who can buy it?\x02\x03",
            "#10101FIf you do not do it, it's national treasure level\x01",
            "It's a price … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6E")

    Jump("loc_AA6")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A81")
    Jump("loc_AA6")

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A8F")
    Jump("loc_AA6")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A9D")
    Jump("loc_AA6")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AA6")

    label("loc_AA6")

    TalkEnd(0xFE)
    Return()

    # Function_4_73D end

    def Function_5_AAA(): pass

    label("Function_5_AAA")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x10,
        "#10109FHaa ~, a very beautiful necklace ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06402FIt looks like an eye-catching item of this store ~.\x02\x03",
            "#06405FWell, the price you care about is ……\x01",
            "…… Zero, Hii, Fuu, Mi ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    OP_64(0x11)

    ChrTalk(
        0x10,
        (
            "#10106F…… Here, with this one necklace\x01",
            "I can buy many power guide cars ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#06406FWell, the world is different indeed!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_5_AAA end

    def Function_6_C0E(): pass

    label("Function_6_C0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C1F")
    Jump("loc_110F")

    label("loc_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C2D")
    Jump("loc_110F")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C3B")
    Jump("loc_110F")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xF,
        (
            "#00300FYo, Lloyd.\x01",
            "I heard that the keeper was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FWell, sorry to hurry around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00303F…… Alright, forgive!\x01",
            "There is no reason not to forgive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x02\x03",
            "#00005F……あれ、そういえばRandy、\x01",
            "Did you buy something here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00302FOh, to Mireille's guy\x01",
            "I thought that it was a little souvenir.\x02\x03",
            "#00304FIt seems that Promotion is also close,\x01",
            "I feel that celebration is also included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell ~, I see. ….\x02\x03",
            "#00012Fあのさ、もしかしてRandyって\x01",
            "About Mireille warrante … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00304FHey, what made you sleepy\x01",
            "I'm telling you.\x02\x03",
            "#00300FIt was taken care of during the guard days,\x01",
            "Is this place courtesy?\x02\x03",
            "#00309FBesides, my strike is\x01",
            "Cecil-san! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt is a remark that is not to be heard … …\x01",
            "Oh well, that kind of thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 1)
    Jump("loc_FAD")

    label("loc_F27")


    ChrTalk(
        0xF,
        (
            "#00300FOnce I got well,\x01",
            "Noelたちと集合場所に向かうぜ。\x02\x03",
            "#00304FUntil then to window shopping\x01",
            "I guess you are working.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAD")

    Jump("loc_110F")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")

    ChrTalk(
        0xF,
        (
            "#00301FWell, is it a necklace …?\x02\x03",
            "#00306FBecause it's about Hitsuji,\x01",
            "This is exercise jama\x01",
            "I heard he said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Somehow I have chosen seriously\x01",
            "Looks like … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_10E5")

    label("loc_1075")


    ChrTalk(
        0xF,
        (
            "#00303FIf it comes to jamas very much\x01",
            "Accessories may be better.\x02\x03",
            "#00300FDo you like a brooch over there\x01",
            "I can not see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_110F")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_10F8")
    Jump("loc_110F")

    label("loc_10F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1106")
    Jump("loc_110F")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_110F")

    label("loc_110F")

    TalkEnd(0xFE)
    Return()

    # Function_6_C0E end

    def Function_7_1113(): pass

    label("Function_7_1113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1124")
    Jump("loc_11EC")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1132")
    Jump("loc_11EC")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1140")
    Jump("loc_11EC")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11B9")

    ChrTalk(
        0xE,
        (
            "#10305F…… Oh, this jewel is between us\x01",
            "Do not look like things that women gave.\x02\x03",
            "#10302FHuh, you bought it here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EC")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11C7")
    Jump("loc_11EC")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_11EC")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11E3")
    Jump("loc_11EC")

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11EC")

    label("loc_11EC")

    TalkEnd(0xFE)
    Return()

    # Function_7_1113 end

    def Function_8_11F0(): pass

    label("Function_8_11F0")

    Call(0, 9)
    Return()

    # Function_8_11F0 end

    def Function_9_11F4(): pass

    label("Function_9_11F4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 7)), scpexpr(EXPR_END)), "loc_1327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C3")

    ChrTalk(
        0x8,
        (
            "Ho ho ho …\x01",
            "Thank you for purchasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jewelry is exactly what\x01",
            "I can express my feelings\x01",
            "The gift of life …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something to be cherished\x01",
            "I pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1322")

    label("loc_12C3")


    ChrTalk(
        0x8,
        "宝飾品とはまさにThe gift of life …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something to be cherished\x01",
            "I pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1322")

    Jump("loc_14A6")

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FE")

    ChrTalk(
        0x8,
        (
            "Jewelry is exactly what\x01",
            "I can express my feelings\x01",
            "The gift of life …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You may be able to grasp the opportunity to give\x01",
            "Also, it depends on that person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho …\x01",
            "When coming next time I will warm your bosom\x01",
            "You have been warming up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14A6")

    label("loc_13FE")


    ChrTalk(
        0x8,
        (
            "Jewelry is just a gift for life ……\x01",
            "You may be able to grasp the opportunity to give\x01",
            "Also, it depends on that person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho …\x01",
            "When coming next time I will warm your bosom\x01",
            "You have been warming up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A6")

    Jump("loc_1831")

    label("loc_14AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_16AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DB")

    ChrTalk(
        0x8,
        (
            "As for our membership system,\x01",
            "Towards trustworthy customers\x01",
            "It is to provide the best service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If customers increase, inevitably\x01",
            "Because the quality of service will decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just being able to attract unlimited attendance\x01",
            "It is not a way of business.\x01",
            "Hoho Ho, did you study?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A7")

    label("loc_15DB")


    ChrTalk(
        0x8,
        (
            "As for our membership system,\x01",
            "Towards trustworthy customers\x01",
            "It is to provide the best service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just being able to attract unlimited attendance\x01",
            "It is not a way of business.\x01",
            "Hoho Ho, did you study?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A7")

    Jump("loc_1831")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1793")

    ChrTalk(
        0x8,
        (
            "Ho ho ho …\x01",
            "To Ataxi's \"Diamante\"\x01",
            "Well, I heard that you came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here, only the finest jewelry items\x01",
            "We have it stocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Qualification to get this eternal glow,\x01",
            "I wonder if you have it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1831")

    label("loc_1793")


    ChrTalk(
        0x8,
        (
            "In this \"Diamante\"\x01",
            "Only the finest jewelry items\x01",
            "We have it stocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho …\x01",
            "Qualification to get this eternal glow,\x01",
            "I wonder if you have it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1831")

    TalkEnd(0x8)
    Return()

    # Function_9_11F4 end

    def Function_10_1835(): pass

    label("Function_10_1835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(
        0x9,
        (
            "… …. Also visit us again\x01",
            "I am waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")

    ChrTalk(
        0x9,
        (
            "In that show window\x01",
            "Exhibited is \"tears of the saint\"\x01",
            "It is called a necklace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It was unearthed from ruins of medieval times\x01",
            "Crossbell ownership of those days,\x01",
            "I am exhibiting it specially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is pricing for convenience,\x01",
            "It can not be sold.\x01",
            "Just in case, please do not hesitate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A66")

    label("loc_19AE")


    ChrTalk(
        0x9,
        (
            "In that show window\x01",
            "Exhibited is \"tears of the saint\"\x01",
            "It is called a necklace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is pricing for convenience,\x01",
            "It can not be sold.\x01",
            "Just in case, please do not hesitate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A66")

    Jump("loc_1B8E")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1C")

    ChrTalk(
        0x9,
        "I was very sorry to have made it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As a special member in the future\x01",
            "We will respectfully hospitate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is something please do not hesitate\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B8E")

    label("loc_1B1C")


    ChrTalk(
        0x9,
        (
            "As a special member in the future\x01",
            "We will respectfully hospitate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is something please do not hesitate\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1835 end

    def Function_11_1B92(): pass

    label("Function_11_1B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1BA3")
    Jump("loc_1D0F")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1BB1")
    Jump("loc_1D0F")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C91")

    ChrTalk(
        0xA,
        (
            "Many seven giant stones are excavated,\x01",
            "Crossbell with Mainz mine ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A certain jewelry item at this shop …\x01",
            "Especially in the seven-ray stone work\x01",
            "It seems that high quality items are lining up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hmm, I just said that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D0F")

    label("loc_1C91")


    ChrTalk(
        0xA,
        (
            "This shop's Sekayaishi workmanship\x01",
            "It seems that high quality items are lining up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Truly has a Mainz mine\x01",
            "I told you that you are crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B92 end

    def Function_12_1D13(): pass

    label("Function_12_1D13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1D24")
    Jump("loc_1D97")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1D32")
    Jump("loc_1D97")

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D97")

    ChrTalk(
        0xB,
        "Huh, I guess it can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it's for you\x01",
            "One or two of the necklace,\x01",
            "There is no feature.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D97")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D13 end

    def Function_13_1D9B(): pass

    label("Function_13_1D9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E10")

    ChrTalk(
        0xC,
        "Huhu, I'm sorry a little while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We, even this\x01",
            "Because I have a loving darling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E95")

    label("loc_1E10")


    ChrTalk(
        0xC,
        (
            "Yes, recently in the direction of the empire\x01",
            "I often look out for you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A better quality jewelry as much as this store\x01",
            "The stores that have many stocks\x01",
            "It is not quite right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E95")

    Jump("loc_1F11")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1EA8")
    Jump("loc_1F11")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1F11")

    ChrTalk(
        0xC,
        (
            "This necklace,\x01",
            "It's pretty cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hey darling,\x01",
            "Will you give me a present?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D9B end

    def Function_14_1F15(): pass

    label("Function_14_1F15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F90")

    ChrTalk(
        0xD,
        "Some fire fascination is attractive, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After all, chastity and lady as a lady\x01",
            "I think it's important.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F90")


    ChrTalk(
        0xD,
        (
            "Huhu, indeed\x01",
            "I can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After all, Crossbell produced seven-ray stone work,\x01",
            "I will not be able to withdraw to other countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2000")

    Jump("loc_2094")

    label("loc_2005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_208B")

    ChrTalk(
        0xD,
        (
            "Jewelry suitable for me,\x01",
            "I can not find it easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, meeting encounter with jewels for once in a while ……\x01",
            "Let's try to find it embarrassed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2094")

    label("loc_208B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2094")

    label("loc_2094")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F15 end

    def Function_15_2098(): pass

    label("Function_15_2098")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x105, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(2140, 400, 4920, 0)
    MoveCamera(312, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25520, 0)
    FadeToBright(1000, 0)
    OP_68(-380, 400, 2640, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005Fhere……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt is a member-owned jewelry store.\x02\x03",
            "#10304FI am with the club's guests\x01",
            "I wonder if it has entered several times.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(
        0x104,
        (
            "#6P#00306FSurely, when we came in front\x01",
            "I was repelled in front of the shop.\x02\x03",
            "#00301FThe attitude of that store clerk\x01",
            "Subtle topography is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, by the way it is this time\x01",
            "I could not stop it … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2340")

    label("loc_22B7")


    ChrTalk(
        0x104,
        (
            "#6P#00306FIs not it okay with refusing a look … …\x01",
            "I feel something bad story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FThat we are saying that we are\x01",
            "Do not you enter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2340")

    OP_68(-3330, 400, 5840, 2500)
    OP_6F(0x1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    NpcTalk(
        0x9,
        "Clerk",
        "Customer.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 19)
    Sleep(50)
    OP_68(-2610, 600, 2290, 3000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(2000)

    def lambda_23E4():

        label("loc_23E4")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_23E4")

    QueueWorkItem2(0x101, 2, lambda_23E4)

    def lambda_23F6():

        label("loc_23F6")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_23F6")

    QueueWorkItem2(0x104, 2, lambda_23F6)

    def lambda_2408():

        label("loc_2408")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2408")

    QueueWorkItem2(0x105, 2, lambda_2408)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x105, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_2462")

    ChrTalk(
        0x105,
        "#12P#10300FHuh, what a hell do you do with rumors.\x02",
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_2462")


    ChrTalk(
        0x101,
        "#12P#00011FWow …\x02",
    )

    CloseMessageWindow()

    label("loc_247F")


    ChrTalk(
        0x9,
        (
            "#5PTo the jewelry store \"Diamante\"\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P…… Excuse me, but a customer.\x01",
            "The letter of introduction from someone\x01",
            "Do you have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FUnfortunately, there is no letter of introduction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PPlease refrain from entering the store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POur store is limited to customers selected\x01",
            "Because it is a membership system.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306FChisa, hey …\x01",
            "Let's get out and get out, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FThat's right, at the beach\x01",
            "I also have to wait ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PMr. Lloyd … ….?\x02",
    )

    CloseMessageWindow()

    def lambda_2680():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2680)
    Sleep(50)

    def lambda_2690():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2690)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x9,
        (
            "#5P……Customer.\x01",
            "If you are a member of \"Special Affairs Support Division\"\x01",
            "Do you Come?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FWell, yes, but … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#5P#4SRude, I'm sorry!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PKo, Kohon ……\x01",
            "As I mentioned earlier,\x01",
            "There was a message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PToday is special, everyone's entrance\x01",
            "It is to allow it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PPlease forgive me some rudeness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, that means …\x01",
            "Does that mean we can use it, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P左様、As a special member in the future\x01",
            "We will respectfully hospitate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThen, if there is something\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 3)
    OP_4C(0x9, 0xFF)

    def lambda_2955():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2955)

    def lambda_2962():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2962)

    def lambda_296F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296F)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_93(0x105, 0x13B, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, apparently that girlfriend\x01",
            "You seem to have made a difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FThat's it.\x01",
            "変わり身の早えClerkだなあ。\x02\x03",
            "#00300FWell, if you decide so\x01",
            "Would you let me use the cancer gun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012FHaha, because they all seem to be expensive\x01",
            "I do not think I can get a hand.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15B, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 800, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2098 end

    def Function_16_2AB5(): pass

    label("Function_16_2AB5")


    def lambda_2ABA():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ABA)

    def lambda_2AD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AD4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2AED():
        OP_95(0xFE, 0, 0, 800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AED)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2AB5 end

    def Function_17_2B0E(): pass

    label("Function_17_2B0E")


    def lambda_2B13():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B13)

    def lambda_2B2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B2D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B46():
        OP_95(0xFE, -790, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B46)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_2B0E end

    def Function_18_2B67(): pass

    label("Function_18_2B67")


    def lambda_2B6C():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B6C)

    def lambda_2B86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B86)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B9F():
        OP_95(0xFE, 870, 0, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_2B67 end

    def Function_19_2BC0(): pass

    label("Function_19_2BC0")


    def lambda_2BC5():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BC5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x0)

    def lambda_2BEA():
        OP_95(0xFE, -3560, 0, 2870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BEA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_2BC0 end

    def Function_20_2C0B(): pass

    label("Function_20_2C0B")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2C17():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C17)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x0)

    def lambda_2C3C():
        OP_95(0xFE, -6300, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C3C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_20_2C0B end

    def Function_21_2C5D(): pass

    label("Function_21_2C5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x102, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x102, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)

    ChrTalk(
        0x102,
        (
            "#00105FThis is \"Diamante\" … …\x02\x03",
            "#00104FIndeed a beautiful jewelry item\x01",
            "You seem to handle a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, Ellie is in the daytime\x01",
            "I went to the boutique.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FWell, that's … …\x01",
            "Ellie is not a member here.\x02\x03",
            "#00000FIt is Maria Bell's childhood friend,\x01",
            "I thought I was treated as VIP clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, when I came to Bell before\x01",
            "You did not enter the jewelry shop, did you?\x02\x03",
            "#00100FYou are watching clothes at a boutique\x01",
            "I feel that it fits sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, I see.\x02\x03",
            "#00000FWell then,\x01",
            "Shall we watch various things together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FWell, let's do that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4810, 1400, 4230, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 4100, 0, 4500, 270)
    SetChrPos(0x102, 4000, 0, 5500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000FBrooch on a ring on a necklace ……\x02\x03",
            "#00003FThere are various things even to say jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FHehe, that's right.\x01",
            "Everything is quite handy\x01",
            "It's an expensive item ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00102FLook, Lloyd.\x01",
            "Do not you think that this ring is nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005Flet's see……\x02\x03",
            "#00000FYes, certainly …\x01",
            "I feel like it will suit Erie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00109FHuhu, flattering\x01",
            "You do not have to tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo no, it is true.\x02\x03",
            "#00003F(The price is my salary\x01",
            "About three months or so ……\x01",
            "As I thought, I will do it. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011F(Well, this corner …!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 24)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x9,
        "Are you looking for customers, engagement rings?\x02",
    )

    CloseMessageWindow()

    def lambda_3230():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3230)
    Sleep(50)

    def lambda_3240():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3240)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x9,
        (
            "If you do not mind,\x01",
            "I'll mend you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x102,
        "#6P#00105F#4SOh.#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FHaha, no, well … um …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, you two\x01",
            "Would you be married …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry, the engagement ring\x01",
            "Because I looked over a corner, it is just me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#6P#00112FEr, Oh!\x02\x03",
            "#00112FWell, that's … that is not the case!\x01",
            "We are not yet that kind of …!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00112FB, Lloyd, because it is different! Is it?\x02\x03",
            "#00113FSeparately like that appeal\x01",
            "I tried not to try it … !.!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FWell, because I knew,\x01",
            "Even if you do not panic so much ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Hmm, then\x01",
            "From that,\x01",
            "You said that it was.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#6P#00112FSo, that's why …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012F(Hey, over there\x01",
            "When desperately stated,\x01",
            "That's a shame with that … but …)\x02\x03",
            "#00004F(… … but that's right.\x01",
            "Ellie has been helped a lot. )\x02\x03",
            "#00000F(Even if it is not a wedding ring,\x01",
            "The gift may be enough ant. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00000FThis brooch of Yuya stone ……\x01",
            "It looks good on Ellie. )\x02\x03",
            "#00003F(The price is … 10000 Mira.\x01",
            "I do quite well … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C9E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Purchase brooches\x01",      # 0
            "To give up\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B19")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FSorry, this brooch\x01",
            "I would like you to wrap it up ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Gee\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#11P#00112FB, Lloyd …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHello, to Erie\x01",
            "I'm getting help from my daily life.\x02\x03",
            "#00000FIt's not a special meaning,\x01",
            "Will you give me a present if you do not mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00113F(Sure enough.\x01",
            "There seems to be a special meaning\x01",
            "I feel it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FOr, is it no chance?\x01",
            "I gotta get something ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#11P#00112FWell, no, it is wrong ……\x02\x03",
            "#00104F…… Kohon.\x01",
            "Thank you, I'm happy Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00100FWell then, in return …\x01",
            "I will also look good on you from me\x01",
            "Would you please let me do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FHuhu, that's okay.\x02\x03",
            "#00109FWell then, I will search for good things\x01",
            "Please wait a while.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Eli each\x01",
            "買った宝飾品をClerkに包んでもらい、\x01",
            "They gave presents to each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '翠耀石挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('翠耀石挂饰', 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_3C99")

    label("loc_3B19")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(… …. It might be slightly heavy indeed.\x01",
            "Would you like to stop this time … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F… …. So, we are still\x01",
            "Even my lovers are not even together … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00113FWait a minute, Lloyd!\x01",
            "You must explain!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#00012FOh, oh … I got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Eli were\x01",
            "While feeling somewhat awkward\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3C99")

    Jump("loc_3E48")

    label("loc_3C9E")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(……, there is not enough Mira in the first place.\x01",
            "I regret that I have to give up … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F… …. So, we are still\x01",
            "Even my lovers are not even together … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00113FWait a minute, Lloyd!\x01",
            "You must explain!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#00012FOh, oh … I got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Eli were\x01",
            "While feeling somewhat awkward\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3E48")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2C5D end

    def Function_22_3E58(): pass

    label("Function_22_3E58")


    def lambda_3E5D():
        OP_95(0xFE, 800, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E5D)

    def lambda_3E77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E77)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3E90():
        OP_95(0xFE, 800, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E90)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_3E58 end

    def Function_23_3EAA(): pass

    label("Function_23_3EAA")


    def lambda_3EAF():
        OP_95(0xFE, -200, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EAF)

    def lambda_3EC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EC9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)

    def lambda_3F14():
        OP_95(0xFE, -200, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F14)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3EAA end

    def Function_24_3F2E(): pass

    label("Function_24_3F2E")


    def lambda_3F33():
        OP_95(0xFE, 4120, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F33)

    def lambda_3F4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F4D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3F6D():
        OP_95(0xFE, 4120, 0, 7340, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F6D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3F2E end

    def Function_25_3F87(): pass

    label("Function_25_3F87")


    def lambda_3F8C():
        OP_95(0xFE, -500, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F8C)

    def lambda_3FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FA6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3FBF():
        OP_95(0xFE, -500, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FBF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_3F87 end

    def Function_26_3FD9(): pass

    label("Function_26_3FD9")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_3FE5():
        OP_95(0xFE, 650, 0, 8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FE5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_400A():
        OP_95(0xFE, 650, 0, 6000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_400A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_3FD9 end

    def Function_27_4024(): pass

    label("Function_27_4024")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_404F")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jump("Function_27_4024")

    label("loc_404F")

    Return()

    # Function_27_4024 end

    def Function_28_4050(): pass

    label("Function_28_4050")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_405C():
        OP_95(0xFE, -3800, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_405C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_4081():
        OP_95(0xFE, -3800, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4081)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_4050 end

    def Function_29_409B(): pass

    label("Function_29_409B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x103, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x103,
        (
            "#00205FThis is a jewelry store ……\x02\x03",
            "#00202FMr. Lloyd,\x01",
            "May I look around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, I still have time\x01",
            "I think it's okay.\x02\x03",
            "#00012FEven so ……\x01",
            "You wanted to come so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, yeah …\x01",
            "Clean accessories etc\x01",
            "Because I heard that there are lots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, that's right.\x02\x03",
            "#00000FWell then let's see various things together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209F……Yes.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(70, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 500, 0, 8900, 0)
    SetChrPos(0x103, -500, 0, 9000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00005FAlso,\x01",
            "It is a wonderful necklace.\x02\x03",
            "#00004FIs it a jewelry of medieval times …?\x01",
            "I feel history somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F…… Er, Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F…. Ah, no.\x02\x03",
            "#00204FBecause it was too beautiful,\x01",
            "I lost my words ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F……what is it?\x01",
            "My eyes seem to be dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo……\x01",
            "I thought it was surprising.\x02\x03",
            "#00003FI thought about a while ago,\x01",
            "Tio is such a vulgar one\x01",
            "To show interest …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FI, I like this kind of thing\x01",
            "There are things that I think obediently beautiful.\x02\x03",
            "#00204F… Well, that was\x01",
            "In a way thanks to Lloyd's guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FAh……\x02\x03",
            "#00004F(Okay … …. Think about it.\x01",
            "Tio is also a girl of age. )\x02\x03",
            "(When we first met with you\x01",
            "It was an impressive adulthood … but …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F…… Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, nothing.\x02\x03",
            "#00004F(That's right, I'm in a mood\x01",
            "I do not mean … …)\x02\x03",
            "(There's also something to give to Tio\x01",
            "It might be nice. )\x02\x03",
            "#00000F(… with what you are willing to … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00000F(This pale yellow stone hair ornament ……\x01",
            "It seems to be perfect for Tio. )\x02\x03",
            "#00003F(The price is … 10000 Mira.\x01",
            "I do quite well … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4F6B")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Purchase hair ornaments\x01",      # 0
            "To give up\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E19")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FTio, there is a hair ornament\x01",
            "Will you give me a present?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        "#00205Feh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha, as expected\x01",
            "There is a necklace that is there\x01",
            "I can not buy it … ….\x02\x03",
            "#00000FTio also seems to be a girl\x01",
            "I want you to be fashionable.\x02\x03",
            "Of course, that's a special meaning.\x01",
            "It is not a translation, but what about …?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204F……I'm happy.\x02\x03",
            "#00200FBut only one point\x01",
            "Even if you say that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F\"Of course, it's not a special meaning …\"\x02\x03",
            "#00211FEven though I say that,\x01",
            "Is it rude in a sense to women?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FWell, that kind of thing?\x02\x03",
            "#00002FAs much as gifts among brothers and sisters\x01",
            "I am supposed to accept it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F… ….\x02\x03",
            "#00211FWell, now that is around\x01",
            "Is it a dropping place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00003FWell, hmm … ….\x01",
            "Why is not it so convinced?\x02\x03",
            "#00012FAfter all it is not hair ornament\x01",
            "You said good Miti goods … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00206F(This person really is already ……)\x02\x03",
            "#00202F… But, that's right.\x01",
            "If you do not mind, from me too\x01",
            "Please let me present to Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYeah, it's been a big problem.\x02\x03",
            "#00204FSo, I will search for good things,\x01",
            "Please wait a bit.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio then\x01",
            "買った宝飾品をClerkに包んでもらい、\x01",
            "They gave presents to each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '苍耀石挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('苍耀石挂饰', 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_4F66")

    label("loc_4E19")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(… … as I thought I should stop it.\x01",
            "It may be annoying … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F…… Mr. Lloyd,\x01",
            "Why do not you visit there too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FOh, I see.\x01",
            "I will get involved until I'm done.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and Tio are alone\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F66")

    Jump("loc_50E5")

    label("loc_4F6B")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(……, there is not enough Mira in the first place.\x01",
            "I regret that I have to give up … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F…… Mr. Lloyd,\x01",
            "Why do not you visit there too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FOh, I see.\x01",
            "I will get involved until I'm done.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and Tio are alone\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_50E5")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_409B end

    def Function_30_50F5(): pass

    label("Function_30_50F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x104, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x104, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#12P#00000FI got to the jewelry store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright, soon\x01",
            "To search for gifts for Lloyd\x01",
            "I will associate with you.\x02\x03",
            "#00309FWho is the aim?\x01",
            "Try to teach your older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, no.\x01",
            "So I said not that.\x02\x03",
            "#00000FAnyway, I have a little time\x01",
            "Let's see the inside of the dustball store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FOh, ok.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5520, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24620, 0)
    SetChrPos(0x101, 5350, 0, 9700, 270)
    SetChrPos(0x104, 4150, 0, 9700, 90)
    SetChrPos(0x9, -900, 0, 9680, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00001FSomehow ……\x02\x03",
            "#00006FThe more you look\x01",
            "In a store like two men in the middle of the night\x01",
            "I have no idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, if you say something\x01",
            "I entered by myself at midday\x01",
            "What is my position?\x02\x03",
            "#00300FWell, however, I agree with that opinion.\x01",
            "Anyway go to the theme park\x01",
            "It is one of Nanpa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FThat's why I do not have time like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTake a water bus from the beginning\x01",
            "I guess that was such a story.\x02\x03",
            "#00301FYou guys are a herbivorous one … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00302FOkay, because you are wrong, so you\x01",
            "Accessories that the guy looks likely to rise\x01",
            "Let's give it a gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FEr … Is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, a while ago\x01",
            "In the other show window\x01",
            "You see that it looks good on you.\x02\x03",
            "#00309FHaha, I guess it looks like playing\x01",
            "That's why I feel depressed.\x02\x03",
            "#00304FOf course there is a special meaning\x01",
            "Even if there is a certain thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo no …\x01",
            "Even so there is no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, this is a joke.\x02\x03",
            "#00304FThen, a little\x01",
            "Clerkに包んでもらってくるとすっかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4210, 1400, 7590, 2000)
    OP_6F(0x79)
    TurnDirection(0x104, 0xC, 500)

    ChrTalk(
        0x104,
        (
            "#11P#00309FI am just over there\x01",
            "To the celebrities older sisters,\x01",
            "Just install the promise of tonight!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 2, 0, 27)
    BeginChrThread(0x104, 3, 0, 26)

    def lambda_57DE():

        label("loc_57DE")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_57DE")

    QueueWorkItem2(0x101, 2, lambda_57DE)
    WaitChrThread(0x104, 3)
    EndChrThread(0x104, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    def lambda_5800():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5800)
    TurnDirection(0xD, 0x104, 500)
    EndChrThread(0x101, 0xFF)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha … well …\x02\x03",
            "#00004F(But, to that good deed\x01",
            "All of us are helped. )\x02\x03",
            "(As a leader of the support department,\x01",
            "I want to express my gratitude … …)\x02\x03",
            "#00000F(I came to the jewelry shop so much,\x01",
            "Will I also try to find out something? )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00000F(This bracelet with red gemstone … …\x01",
            "  Randyに似合うかもな。）\x02\x03",
            "#00003F(The price is … 10000 Mira.\x01",
            "I do quite well … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CE6")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Purchase a bracelet\x01",      # 0
            "To give up\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA6")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FExcuse me.\x01",
            "I want this bracelet ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4B(0x9, 0xFF)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "#5PI'm home.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd then failed to Nampa\x01",
            "肩をすくめているRandyを冗談交じりに慰め……\x02\x03",
            "買った宝飾品をClerkに包んでもらい、\x01",
            "They gave presents to each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_5CE1")

    label("loc_5BA6")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(… It's kind of embarrassingly embarrassing\x01",
            "Let's stop it. )\x02\x03",
            "#00000F（Randyへの感謝の気持ちは\x01",
            "I have to show it again in another form at a later date. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd then failed to Nampa\x01",
            "肩をすくめているRandyを冗談交じりに慰め……\x02\x03",
            "Randyから宝飾品を贈られてから、\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5CE1")

    Jump("loc_5E2B")

    label("loc_5CE6")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(… .., there is not enough Mira in the first place.\x02\x03",
            "#00008F(I'm sorry but I give you this from\x01",
            "It seems better to give up … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd then failed to Nampa\x01",
            "肩をすくめているRandyを冗談交じりに慰め……\x02\x03",
            "Randyから宝飾品を贈られてから、\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5E2B")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '红耀石挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('红耀石挂饰', 1)
    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_50F5 end

    def Function_31_5E76(): pass

    label("Function_31_5E76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x109, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x109, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x109,
        (
            "#10108Fうーん、昼間Francと一緒に\x01",
            "I went around looking all along … ….\x02\x03",
            "#10106FHa, after all\x01",
            "I feel like I'm out of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FFirst of all, Mr. Marybele\x01",
            "Without mouthfeel,\x01",
            "It is a store not to enter.\x02\x03",
            "#00000FWell, it's okay.\x01",
            "Will not you go round with me this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYeah, I will associate!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8500, 90)
    SetChrPos(0x109, 6000, 0, 7200, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#5P#10103FYup……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00005Fどうした、Noel？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10101FNo, thanks a little while ago\x01",
            "I thought I saw it … ….\x02\x03",
            "#10106FSomehow Jewelry\x01",
            "Do you have a lot of waste?\x02\x03",
            "#10108FTurning on and turning on\x01",
            "It seems to be difficult to move,\x01",
            "There is a problem with work ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#6P#10111FOh, I'm sorry!\x01",
            "Even though I was looking happily fun … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha … … no, somehow\x01",
            "Noelらしい意見だな。\x02\x03",
            "#00000FそういえばNoelの私服って\x01",
            "It seems to be easy to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha ……\x01",
            "Focus a lot on that point\x01",
            "I feel like I am picking it.\x02\x03",
            "#10106FThanks for choosing by yourself\x01",
            "It tends to be manish\x01",
            "I am in trouble, though.\x02\x03",
            "#10100FだからいつもはFrancに頼んで、\x01",
            "Have them coordinate …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I see.\x02\x03",
            "#00000FWell then, this store\x01",
            "Is there anything you like like it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FThat's true.\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#5P#10102FOh, of this Amoya\x01",
            "Addicted choker ……\x02\x03",
            "#10109F昼間、Francと一緒に見てから\x01",
            "A bit better\x01",
            "I thought that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002Fはは、確かにNoelに似合いそうだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(Yeah, I came along with it all the time,\x01",
            "It might be good to give a present. )\x02\x03",
            "#00003F(The price is … 10000 Mira.\x01",
            "I do quite well … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6BFF")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Purchase a choker\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A70")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FNoel、このチョーカー……\x01",
            "君にWill you give me a present?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FHuh…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10111FEeeeeee! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, maybe it was annoying?\x02\x03",
            "#00004FYou are trying hard on the outsourcing of the support department,\x01",
            "Because that labor is included in it\x01",
            "It's not a special meaning … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10111FEr, um … or no! It is!\x01",
            "I'm glad that I am happy … ___ ___ 0 It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs there something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F……No! It is!\x01",
            "That's why …!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#6P#10101F…… So, then!\x01",
            "It is a great offer,\x01",
            "We will be happy to accept!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FEven if you do not cheat so much ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FNo……\x01",
            "After all I am sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10103FThat's right. In that case …\x02\x03",
            "#10100FFrom Mr. Lloyd also from me\x01",
            "Could you give me something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes.\x02\x03",
            "#10100FBecause I will search for good things,\x01",
            "Please wait for a moment.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとNoelはそれぞれ\x01",
            "買った宝飾品をClerkに包んでもらい、\x01",
            "They gave presents to each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '琥耀石挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('琥耀石挂饰', 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_6BFA")

    label("loc_6A70")


    ChrTalk(
        0x101,
        (
            "#00006F(… Well, after all it stops.\x01",
            "  Francとかにも誤解を生みそうだし……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FMr. Lloyd, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh no, nothing.\x02\x03",
            "#00000FIs there anything else you like like\x01",
            "Let's see it variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYeah, you are right!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはNoelとひとしきり\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6BFA")

    Jump("loc_6DA2")

    label("loc_6BFF")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(……, there is not enough Mira in the first place.\x01",
            "I regret that I have to give up … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FMr. Lloyd, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh no, nothing.\x02\x03",
            "#00000FIs there anything else you like like\x01",
            "Let's see it variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYeah, you are right!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはNoelとひとしきり\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6DA2")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5E76 end

    def Function_32_6DB2(): pass

    label("Function_32_6DB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x105, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x105, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#12P#00000FWell, I came to a jewelry store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI have time to dinner,\x01",
            "Would you like to see it together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FOh, it's okay\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, it's a rule.\x01",
            "Well then let's walk around.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8100, 90)
    SetChrPos(0x105, 6000, 0, 6900, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FWell, as long as it is a membership system\x01",
            "After all I have something expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, it's pity,\x01",
            "Later on to ring the key\x01",
            "You may want to give it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00006FHey Hey,\x01",
            "It will not give children.\x02\x03",
            "#00005F……そういえばWajiって、\x01",
            "Before entering the support department\x01",
            "I'd like to wear a lot of wings.\x02\x03",
            "#00003FTactical auctions as well\x01",
            "It seems I had it since I saw him … …\x02\x03",
            "#00000FAlthough it is inferior care,\x01",
            "After all the host club\x01",
            "Are they profitable?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FDisagreeable? I am byte bye,\x01",
            "I will occasionally help\x01",
            "The actual salary is not a big deal.\x02\x03",
            "#10304FIn clubs, rather,\x01",
            "Temporary income separate from salary#8R噵 噵 噵 噵#I wonder if there will be more.\x02\x03",
            "#10302FFrom celebrity madam\x01",
            "Gems passed on behalf of pocket money,\x01",
            "Sometimes it happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Well, I see.\x01",
            "I can not admire it much,\x01",
            "That is the source of funding … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, no no.\x01",
            "Things that customers received\x01",
            "I will not do cashing?\x02\x03",
            "#10304FEven the enigma I had before,\x01",
            "From Ashley's shop\x01",
            "I purchased it at my mirror.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005F…… Well then, after all, Mira\x01",
            "Where are you out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10309FHuh, that is a company secret.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, well like that\x01",
            "Let's leave something that does not matter …\x02\x03",
            "#10302FLloyd, if you do not mind\x01",
            "Can you accept it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '金耀石挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('金耀石挂饰', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005Fis this……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FJust before\x01",
            "In the showcase over there\x01",
            "With the accessory I found.\x02\x03",
            "#10304FBecause I thought it would suit you\x01",
            "It's a big deal and I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FUntil when … …\x02\x03",
            "#00005FBut, I think that this kind of expensive thing\x01",
            "Can I really get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, it's just a whim\x01",
            "You do not have to think hard to think so.\x02\x03",
            "#10309FIf you can sell you to this degree\x01",
            "It's cheap.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FHere, hey …\x02\x03",
            "#00000FBut well, thanks.\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHuh, you are welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(… … That's right,\x01",
            "I just got it … …)\x02\x03",
            "#00004F(Also from returning something from here\x01",
            "It might be nice. )\x02\x03",
            "#00000F（Wajiが来たおかげで、\x01",
            "The flexibility of the support department also increased in a certain sense,\x01",
            "I also put the meaning of that thank … ….)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(If this pendant of Kim,\x01",
            "  Wajiに似合うかもしれない。）\x02\x03",
            "#00003F(The price is … 10000 Mira.\x01",
            "I do quite well … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7CE6")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Purchase a pendant\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6F")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FThen, in return\x01",
            "Will you give me this pendant?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x2D, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10305FWell, are you sure?\x02\x03",
            "#10300FHuh, your sense too\x01",
            "It is not too bad.\x02\x03",
            "#10302FIt's cheap as a gift,\x01",
            "Well it might be a running point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYou know.\x01",
            "I will not buy it unless I need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha, nothing.\x02\x03",
            "#10302FIt was the one you chose so hard,\x01",
            "I will thank you for accepting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F…… Well, well.\x01",
            "Clerkさんを呼んでこよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd then\x01",
            "買った宝飾品をClerkに包んでもらい、\x01",
            "Wajiにプレゼントするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_7CE1")

    label("loc_7B6F")


    ChrTalk(
        0x101,
        (
            "#00006F(… after all I guess this time it will be strange.\x01",
            "Let's make up on another occasion. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, what's up?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, nothing.\x02\x03",
            "#00000FThere is a little time to wait,\x01",
            "Shall I watch the inside of the shop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはWajiとひとしきり\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7CE1")

    Jump("loc_7E77")

    label("loc_7CE6")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(……, there is not enough Mira in the first place.\x01",
            "I regret that I have to give up … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, what's up?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, nothing.\x02\x03",
            "#00000FThere is a little time to wait,\x01",
            "Shall I watch the inside of the shop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはWajiとひとしきり\x01",
            "Enjoy window shopping,\x01",
            "I left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7E77")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_6DB2 end

    SaveToFile()

Try(main)
