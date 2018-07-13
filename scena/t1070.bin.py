from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Mariah",                 # 1
        "Tyra",                   # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Wazy",                   # 7
        "Randy",                  # 8
        "Noｱl",                  # 9
        "Fran",                   # 10
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
        "Function_4_736",          # 04, 4
        "Function_5_AFA",          # 05, 5
        "Function_6_C86",          # 06, 6
        "Function_7_11EC",         # 07, 7
        "Function_8_12DE",         # 08, 8
        "Function_9_12E2",         # 09, 9
        "Function_10_1990",        # 0A, 10
        "Function_11_1D53",        # 0B, 11
        "Function_12_1F20",        # 0C, 12
        "Function_13_1FA8",        # 0D, 13
        "Function_14_2129",        # 0E, 14
        "Function_15_22E9",        # 0F, 15
        "Function_16_2D89",        # 10, 16
        "Function_17_2DE2",        # 11, 17
        "Function_18_2E3B",        # 12, 18
        "Function_19_2E94",        # 13, 19
        "Function_20_2EDF",        # 14, 20
        "Function_21_2F31",        # 15, 21
        "Function_22_418B",        # 16, 22
        "Function_23_41DD",        # 17, 23
        "Function_24_4261",        # 18, 24
        "Function_25_42BA",        # 19, 25
        "Function_26_430C",        # 1A, 26
        "Function_27_4357",        # 1B, 27
        "Function_28_4383",        # 1C, 28
        "Function_29_43CE",        # 1D, 29
        "Function_30_54FF",        # 1E, 30
        "Function_31_6331",        # 1F, 31
        "Function_32_7387",        # 20, 32
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
    Jump("loc_732")

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_551")
    Jump("loc_732")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_55F")
    Jump("loc_732")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638")

    ChrTalk(
        0x11,
        (
            "#06406FBig sis has been acting\x01",
            "strange since some time.\x02\x03",
            "#06402FHas something happened at the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well...\x01",
            "That would be a little\x01",
            "hard for me to explain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#06405F???\x02",
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_638")


    ChrTalk(
        0x11,
        (
            "#06406FBig sis has been acting\x01",
            "strange since some time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675")

    Jump("loc_732")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_70D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695")
    Call(0, 5)
    Jump("loc_708")

    label("loc_695")


    ChrTalk(
        0x11,
        (
            "#06409FMr. Lloyd, please give her\x01",
            "this necklace as a present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-No no, that would be prohibitive.\x02",
    )

    CloseMessageWindow()

    label("loc_708")

    Jump("loc_732")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_71B")
    Jump("loc_732")

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_729")
    Jump("loc_732")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_732")

    label("loc_732")

    TalkEnd(0xFE)
    Return()

    # Function_3_532 end

    def Function_4_736(): pass

    label("Function_4_736")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_747")
    Jump("loc_AF6")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_755")
    Jump("loc_AF6")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_763")
    Jump("loc_AF6")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_A26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E")

    ChrTalk(
        0x10,
        (
            "#10106F*haah*...Although there was the danger,\x01",
            "I can't believe my swimsuit was really torn...\x02\x03",
            "#10101FNot being able to defend from that kind of attack\x01",
            "means that I still have a lot of training to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...*c-cough*.\x01",
            "Me too. If I had somehow \x01",
            "noticed it a little quicker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10114FAh, n-no!\x01",
            "I wasn't seriously injured!\x02\x03",
            "#10103FI-It's true that it was embarrassing, but...\x01",
            "I'll devote myself driven by this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(T-To what will you...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A21")

    label("loc_94E")


    ChrTalk(
        0x10,
        (
            "#10106F*sigh*...not being able to defend \x01",
            "from that kind of attack means that\x01",
            "I still have a lot of training to do.\x02\x03",
            "#10101FBecause of that, it was embarrassing...\x01",
            "I must devote myself more driven by this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A21")

    Jump("loc_AF6")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A41")
    Call(0, 5)
    Jump("loc_ABE")

    label("loc_A41")


    ChrTalk(
        0x10,
        (
            "#10106FS-Such a wonderful necklace...\x01",
            "Who could buy it?\x02\x03",
            "#10101FIt could have the price level\x01",
            "of a national treasure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABE")

    Jump("loc_AF6")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AD1")
    Jump("loc_AF6")

    label("loc_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_ADF")
    Jump("loc_AF6")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AED")
    Jump("loc_AF6")

    label("loc_AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AF6")

    label("loc_AF6")

    TalkEnd(0xFE)
    Return()

    # Function_4_736 end

    def Function_5_AFA(): pass

    label("Function_5_AFA")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x10,
        "#10109F*siiigh*, what a very pretty necklace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06402FIt seems it's this store's loss leader.\x02\x03",
            "#06405FUhhm, I'm interested in the price...\x01",
            "...So the zeros are one, two, three...\x02",
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
            "#10106F...J-Just with this one necklace\x01",
            "you could buy some orbal cars...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#06406FI-It's really a complete different world.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_5_AFA end

    def Function_6_C86(): pass

    label("Function_6_C86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C97")
    Jump("loc_11E8")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CA5")
    Jump("loc_11E8")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_CB3")
    Jump("loc_11E8")

    label("loc_CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBD")

    ChrTalk(
        0xF,
        (
            "#00300FYo, Lloyd.\x01",
            "It seems you've found Keddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FEheheh, sorry for wandering around on my own.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00303F...Alright, I forgive you!\x01",
            "No way I couldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha...\x02\x03",
            "#00005F...Oh, by the way, Randy,\x01",
            "were you buying something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00302FYeah, I was thinkin' about a\x01",
            "small present for Mireille.\x02\x03",
            "#00304FHer promotion seems close,\x01",
            "so something that could celebrate that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEeh, I see...\x02\x03",
            "#00012FSay, could it be that you...\x01",
            "About 2nd Lt. Mireille...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00304FHa ha, what nonsense\x01",
            "are you talkin' about?\x02\x03",
            "#00300FI owe her for my time at the CGF,\x01",
            "so this is just good manners, you see?\x02\x03",
            "#00309FAlso, my aims are\x01",
            "on Miss Cecil!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI can't allow that statement to pass, but...\x01",
            "Well, so that's how things are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 1)
    Jump("loc_1048")

    label("loc_FBD")


    ChrTalk(
        0xF,
        (
            "#00300FI'll be goin' to the meeting place with\x01",
            "Noｱl and the others in a little while.\x02\x03",
            "#00304FI'll do some window\x01",
            "shopping 'til then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1048")

    Jump("loc_11E8")

    label("loc_104D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(
        0xF,
        (
            "#00301FHmm, a necklace...?\x02\x03",
            "#00306FKnowin' how she is, she'd likely \x01",
            "say that such a thing would be \x01",
            "in the way durin' practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(It seems he's choosing\x01",
            "it seriously...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_11BE")

    label("loc_1123")


    ChrTalk(
        0xF,
        (
            "#00303FMaybe some small accessory that doesn't \x01",
            "get too much in the way would be better.\x02\x03",
            "#00300FI guess I'll give a look\x01",
            "to the brooches over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BE")

    Jump("loc_11E8")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_11D1")
    Jump("loc_11E8")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11DF")
    Jump("loc_11E8")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11E8")

    label("loc_11E8")

    TalkEnd(0xFE)
    Return()

    # Function_6_C86 end

    def Function_7_11EC(): pass

    label("Function_7_11EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_11FD")
    Jump("loc_12DA")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_120B")
    Jump("loc_12DA")

    label("loc_120B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1219")
    Jump("loc_12DA")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(
        0xE,
        (
            "#10305F...Oh, this jewel is similar to one\x01",
            "I received from that lady lately.\x02\x03",
            "#10302FHu hu, could she have bought it here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DA")

    label("loc_12A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12B5")
    Jump("loc_12DA")

    label("loc_12B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_12C3")
    Jump("loc_12DA")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12D1")
    Jump("loc_12DA")

    label("loc_12D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12DA")

    label("loc_12DA")

    TalkEnd(0xFE)
    Return()

    # Function_7_11EC end

    def Function_8_12DE(): pass

    label("Function_8_12DE")

    Call(0, 9)
    Return()

    # Function_8_12DE end

    def Function_9_12E2(): pass

    label("Function_9_12E2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1618")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 7)), scpexpr(EXPR_END)), "loc_1432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")

    ChrTalk(
        0x8,
        (
            "Ho ho ho...\x01",
            "Thank you very much for your purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jewelry is a lifetime present\x01",
            "you can truly put many\x01",
            "thoughts in it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am sure you will pray the\x01",
            "Goddess to hold it safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_142D")

    label("loc_13C7")


    ChrTalk(
        0x8,
        "Jewelry is truly a lifetime present...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am sure you will pray the\x01",
            "Goddess to hold it safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142D")

    Jump("loc_1613")

    label("loc_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153E")

    ChrTalk(
        0x8,
        (
            "Jewelry is a lifetime present\x01",
            "you can truly put many\x01",
            "thoughts in it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although seizing the chance to give it\x01",
            "is, well, up to the person itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho...\x01",
            "The next time you come, please do it\x01",
            "after having freely lined up your purse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1613")

    label("loc_153E")


    ChrTalk(
        0x8,
        (
            "Jewelry is truly a lifetime present...\x01",
            "Although seizing the chance to give it\x01",
            "is, well, up to the person itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho...\x01",
            "The next time you come, please do it\x01",
            "after having freely lined up your purse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1613")

    Jump("loc_198C")

    label("loc_1618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_184D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1769")

    ChrTalk(
        0x8,
        (
            "Our members only system is in\x01",
            "place to offer a top service to\x01",
            "our trusted regular patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When the customers increase, the service\x01",
            "quality ends up lowering no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It means that a business is not done\x01",
            "only by attracting limitless customers.\x01",
            "Ho ho ho, was it a good learning experience?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1848")

    label("loc_1769")


    ChrTalk(
        0x8,
        (
            "Our members only system is in\x01",
            "place to offer a top service to\x01",
            "our trusted regular patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It means that a business is not done\x01",
            "only by attracting limitless customers.\x01",
            "Ho ho ho, was it a good learning experience?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1848")

    Jump("loc_198C")

    label("loc_184D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_198C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1905")

    ChrTalk(
        0x8,
        (
            "Ho ho ho...\x01",
            "Welcome to my\x01",
            ""Diamante".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here we have only\x01",
            "top-class jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if you have the right to\x01",
            "have this eternal brilliance...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_198C")

    label("loc_1905")


    ChrTalk(
        0x8,
        (
            "At "Diamante"\x01",
            "we have only\x01",
            "top-class jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho ho...\x01",
            "I wonder if you have the right to\x01",
            "have this eternal brilliance...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198C")

    TalkEnd(0x8)
    Return()

    # Function_9_12E2 end

    def Function_10_1990(): pass

    label("Function_10_1990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19CB")

    ChrTalk(
        0x9,
        (
            "...We will wait for\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4F")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4C")

    ChrTalk(
        0x9,
        (
            "The necklace displayed in the\x01",
            "show window over there is\x01",
            "called "The Saint's Tears".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We are exceptionally allowed to display it. It was\x01",
            "excavated from a Middle Ages ruins and is thought\x01",
            "to be the possession of a feudal lord of that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has a price for a matter of convenience,\x01",
            "but we cannot sell it.\x01",
            "Please acknowledge this, just in case.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C14")

    label("loc_1B4C")


    ChrTalk(
        0x9,
        (
            "The necklace displayed in the\x01",
            "show window over there is\x01",
            "called "The Saint's Tears".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has a price for a matter of convenience,\x01",
            "but we cannot sell it.\x01",
            "Please acknowledge this, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C14")

    Jump("loc_1D4F")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD2")

    ChrTalk(
        0x9,
        "I am very sorry for before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From now on, we will respectfully\x01",
            "receive you as special members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please feel free to ask me\x01",
            "if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D4F")

    label("loc_1CD2")


    ChrTalk(
        0x9,
        (
            "From now on, we will respectfully\x01",
            "receive you as special members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please feel free to ask me\x01",
            "if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1990 end

    def Function_11_1D53(): pass

    label("Function_11_1D53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1D64")
    Jump("loc_1F1C")

    label("loc_1D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1D72")
    Jump("loc_1F1C")

    label("loc_1D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E86")

    ChrTalk(
        0xA,
        (
            "Crossbell possess Mainz Mine,\x01",
            "where a great quantity of Septium is excavated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The jewelry on display in this store...\x01",
            "It looks like they have high quality jewel,\x01",
            "especially crafted from Septium...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hm, as expected from such a place.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F1C")

    label("loc_1E86")


    ChrTalk(
        0xA,
        (
            "It looks like this store has high\x01",
            "quality jewels crafted from Septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess it's to be expected from Crossbell,\x01",
            "owner of the Mainz Mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1D53 end

    def Function_12_1F20(): pass

    label("Function_12_1F20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1F31")
    Jump("loc_1FA4")

    label("loc_1F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1F3F")
    Jump("loc_1FA4")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1FA4")

    ChrTalk(
        0xB,
        "Hu hu, it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it is for you,\x01",
            "one or two necklaces\x01",
            "are no trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA4")

    TalkEnd(0xFE)
    Return()

    # Function_12_1F20 end

    def Function_13_1FA8(): pass

    label("Function_13_1FA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_20BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(
        0xC,
        "Uh uh, sorry for before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Despite the appearances,\x01",
            "we have a darling we love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B6")

    label("loc_201D")


    ChrTalk(
        0xC,
        (
            "Yes. Recently I often\x01",
            "visit the Empire region, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's nothing at all like this\x01",
            "store that has a superior quality\x01",
            "selection of jewelry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B6")

    Jump("loc_2125")

    label("loc_20BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_20C9")
    Jump("loc_2125")

    label("loc_20C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2125")

    ChrTalk(
        0xC,
        (
            "Isn't this necklace\x01",
            "quite lovely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Say, darling,\x01",
            "won't you buy it for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2125")

    TalkEnd(0xFE)
    Return()

    # Function_13_1FA8 end

    def Function_14_2129(): pass

    label("Function_14_2129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_223D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B4")

    ChrTalk(
        0xD,
        "Playing somewhat with love is charming, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I really think that a lady's\x01",
            "fidelity is important.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2238")

    label("loc_21B4")


    ChrTalk(
        0xD,
        (
            "Uh uh, you can\x01",
            "really say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As expected, the Septium crafts produced in\x01",
            "Crossbell aren't outdone by other countries'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2238")

    Jump("loc_22E5")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_22DC")

    ChrTalk(
        0xD,
        (
            "I can't quite find\x01",
            "appropriate jewels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, the encounter with a jewel is a once-\x01",
            "in-a-lifetime thing... I think I'll look patiently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E5")

    label("loc_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_22E5")

    label("loc_22E5")

    TalkEnd(0xFE)
    Return()

    # Function_14_2129 end

    def Function_15_22E9(): pass

    label("Function_15_22E9")

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
        "#00005FThis place is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FI'm sure it's a members only jewelry.\x02\x03",
            "#10304FI think I entered here sometimes\x01",
            "with the club's customers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_253E")

    ChrTalk(
        0x104,
        (
            "#6P#00306FI remember that when we came before,\x01",
            "we were driven away in front of the store.\x02\x03",
            "#00301FThat clerk's attitude\x01",
            "slightly pissed me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAh, now that you mention it,\x01",
            "this time we weren't stopped...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C5")

    label("loc_253E")


    ChrTalk(
        0x104,
        (
            "#6P#00306FNo first customers, huh...?\x01",
            "Somehow that's unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FOh, so does it mean that\x01",
            "it's bad we got inside?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C5")

    OP_68(-3330, 400, 5840, 2500)
    OP_6F(0x1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    NpcTalk(
        0x9,
        "Clerk",
        "Mister customers.\x02",
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

    def lambda_2673():

        label("loc_2673")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2673")

    QueueWorkItem2(0x101, 2, lambda_2673)

    def lambda_2685():

        label("loc_2685")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2685")

    QueueWorkItem2(0x104, 2, lambda_2685)

    def lambda_2697():

        label("loc_2697")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2697")

    QueueWorkItem2(0x105, 2, lambda_2697)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x105, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, speak of the devil.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2705")

    label("loc_26ED")


    ChrTalk(
        0x101,
        "#12P#00011FWhoa...\x02",
    )

    CloseMessageWindow()

    label("loc_2705")


    ChrTalk(
        0x9,
        (
            "#5PWelcome to jewelry\x01",
            "shop "Diamante".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...Apologies for asking you this,\x01",
            "but do you have a letter of\x01",
            "introduction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FU-Uhmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FUnfortunately, we don't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PThen please, leave the shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThis store is membership only,\x01",
            "limited to selected customers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306FTch, can't be helped...\x01",
            "Let's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FRight, we also have an\x01",
            "appointment at the beach...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PMr. Lloyd...?\x02",
    )

    CloseMessageWindow()

    def lambda_28EF():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28EF)
    Sleep(50)

    def lambda_28FF():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_28FF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x9,
        (
            "#5P...Mister customers.\x01",
            "Are you perhaps from the\x01",
            ""Special Support Section"?\x02",
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
        "#12P#00005FYes, you're right...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#5P#4SI-I'm terribly sorry!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FW-What the...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P*c-cough*...\x01",
            "We received a communication\x01",
            "from Lady Mariabell before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIt was about giving you a special\x01",
            "permission for today to enter the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PPlease forgive my rudeness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUhhm, so it means that...\x01",
            "We can use it too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PCorrect. From now on, we will respectfully\x01",
            "receive you as special members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThen, please feel free to ask\x01",
            "me if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 3)
    OP_4C(0x9, 0xFF)

    def lambda_2BEA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BEA)

    def lambda_2BF7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BF7)

    def lambda_2C04():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C04)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_93(0x105, 0x13B, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, it seems that lady was sensible\x01",
            "enough to do this for us, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FEven so, what a quick change\x01",
            "of stance that clerk had...\x02\x03",
            "#00300FWell, bein' this the case, let's make\x01",
            "use of this as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012FHa ha, because everything looks expensive,\x01",
            "all items could be out of our reach.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15B, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 800, 0)
    EventEnd(0x5)
    Return()

    # Function_15_22E9 end

    def Function_16_2D89(): pass

    label("Function_16_2D89")


    def lambda_2D8E():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D8E)

    def lambda_2DA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DA8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2DC1():
        OP_95(0xFE, 0, 0, 800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DC1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2D89 end

    def Function_17_2DE2(): pass

    label("Function_17_2DE2")


    def lambda_2DE7():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DE7)

    def lambda_2E01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E01)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2E1A():
        OP_95(0xFE, -790, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E1A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_2DE2 end

    def Function_18_2E3B(): pass

    label("Function_18_2E3B")


    def lambda_2E40():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E40)

    def lambda_2E5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E5A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2E73():
        OP_95(0xFE, 870, 0, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E73)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_2E3B end

    def Function_19_2E94(): pass

    label("Function_19_2E94")


    def lambda_2E99():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E99)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x0)

    def lambda_2EBE():
        OP_95(0xFE, -3560, 0, 2870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EBE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_2E94 end

    def Function_20_2EDF(): pass

    label("Function_20_2EDF")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2EEB():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EEB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x0)

    def lambda_2F10():
        OP_95(0xFE, -6300, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F10)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_20_2EDF end

    def Function_21_2F31(): pass

    label("Function_21_2F31")

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
            "#00105FThis is "Diamante"...\x02\x03",
            "#00104FAs expected, it looks like they have\x01",
            "an assortment of many pretty jewels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. During the day you\x01",
            "went to the boutique, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, by the way...\x01",
            "Aren't you a member of this place, Elie?\x02\x03",
            "#00000FYou're Miss Mariabell's childhood friend...\x01",
            "I thought you had a complete VIP treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FHmm, when I came here with Bell before,\x01",
            "we didn't enter the jewelry shop.\x02\x03",
            "#00100FI think looking at clothes at the boutique\x01",
            "suits her personality more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha, I see.\x02\x03",
            "#00000FThen, why don't we look at\x01",
            "various things since we're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYes, let's do it.\x02",
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
            "#6P#00000FNecklaces, rings, brooches...\x02\x03",
            "#00003FThere's really a lot of jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100F*giggle*, right.\x01",
            "Although they're all pretty expensive\x01",
            "articles out of our reach...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00102FLook, Lloyd.\x01",
            "Don't you think this ring is lovely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FLet me see...\x02\x03",
            "#00000FYes, indeed...\x01",
            "I think it would suit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00109F*giggle*, you don't\x01",
            "have to flatter me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo no, I mean it.\x02\x03",
            "#00003F(The price is about three\x01",
            "months of my salary...\x01",
            "It's really a lot for me.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011F(Wait, this corner is...!)\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 24)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x9,
        "Mister customer, are you looking for a wedding ring?\x02",
    )

    CloseMessageWindow()

    def lambda_3564():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3564)
    Sleep(50)

    def lambda_3574():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3574)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x9,
        (
            "If you want, I could\x01",
            "choose one for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x102,
        "#6P#00105F#4SWHAT.#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FHa ha, no, ehhhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, aren't you two\x01",
            "getting married...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My apologies, you were looking in the\x01",
            "engagement rings corner and I thought...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#6P#00112FEh, ah...!\x02\x03",
            "#00112FI-It's not...like that!\x01",
            "We aren't...like that yet...!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00112FL-Lloyd, it's not like that, ok!?\x02\x03",
            "#00113FIt's not that I was trying\x01",
            "to induce you to...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FI-I know, you don't\x01",
            "need to be so agitated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Hm, then you\x01",
            "were going to\x01",
            "discuss about it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#6P#00112FL-Like I said...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012F(Ha ha, it's a pity in its\x01",
            "own right she's explaining\x01",
            "that desperately...)\x02\x03",
            "#00004F(...But, that's right.\x01",
            "Elie is always helping me out.)\x02\x03",
            "#00000F(Leaving aside a wedding ring, there may be\x01",
            "something nice I could give her as a present.)\x02",
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
            "#12P#00000F(This esmelas brooch...\x01",
            "It looks like it would suit her.)\x02\x03",
            "#00003F(The price is...10000 mira, eh?)\x01",
            "(It's quite a lot, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3FD0")
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
            "Purchase the Brooch\x01",      # 0
            "Quit\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E50")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FExcuse me, could you\x01",
            "wrap me this brooch...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#11P#00112FL-Loyd...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHa ha, you help me\x01",
            "out every day, Elie.\x02\x03",
            "#00000FIt's not that it has a particular meaning,\x01",
            "but would you like to accept this present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00113F(I-I feel like it has quite\x01",
            "a lot of a particular\x01",
            "meaning, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FI-Is it really not good?\x01",
            "To receive a present from me...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#11P#00112FN-No, it's not that...\x02\x03",
            "#00104F...*cough*.\x01",
            "Thank you, I'm happy Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00100FThen, in return...\x01",
            "I believe I will choose something\x01",
            "that could look good on you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh, is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100F*giggle*, since we're here...\x02\x03",
            "#00109FThen, please wait a little,\x01",
            "I'll look for something nice.\x02",
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
            "Afterwards, Lloyd and Elie had each of the\x01",
            "jewels they bought wrapped by the clerk\x01",
            "and exchanged them as presents.\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x398),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x398, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_3FCB")

    label("loc_3E50")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(...As expected, maybe it's a little serious.\x01",
            "I guess I'll pass this time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F...L-Like I said, we aren't\x01",
            "even lovers yet, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "R-Right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00113FW-Wait, Lloyd!\x01",
            "Please explain this too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#00012FY-Yeah...I got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Elie  \x01",
            "left the jewelry shop while\x01",
            "feeling awkward.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3FCB")

    Jump("loc_417B")

    label("loc_3FD0")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(...Wait, first of all, I don't have enough mira.\x01",
            "It's a pity, but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F...L-Like I said, we aren't\x01",
            "even lovers yet, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "R-Right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00113FW-Wait, Lloyd!\x01",
            "Please explain this too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#00012FY-Yeah...I got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Elie  \x01",
            "left the jewelry shop while\x01",
            "feeling awkward.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_417B")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2F31 end

    def Function_22_418B(): pass

    label("Function_22_418B")


    def lambda_4190():
        OP_95(0xFE, 800, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4190)

    def lambda_41AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41AA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_41C3():
        OP_95(0xFE, 800, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41C3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_418B end

    def Function_23_41DD(): pass

    label("Function_23_41DD")


    def lambda_41E2():
        OP_95(0xFE, -200, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41E2)

    def lambda_41FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41FC)
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

    def lambda_4247():
        OP_95(0xFE, -200, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4247)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_41DD end

    def Function_24_4261(): pass

    label("Function_24_4261")


    def lambda_4266():
        OP_95(0xFE, 4120, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4266)

    def lambda_4280():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4280)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_42A0():
        OP_95(0xFE, 4120, 0, 7340, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42A0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_4261 end

    def Function_25_42BA(): pass

    label("Function_25_42BA")


    def lambda_42BF():
        OP_95(0xFE, -500, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42BF)

    def lambda_42D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42D9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_42F2():
        OP_95(0xFE, -500, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42F2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_42BA end

    def Function_26_430C(): pass

    label("Function_26_430C")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_4318():
        OP_95(0xFE, 650, 0, 8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4318)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_433D():
        OP_95(0xFE, 650, 0, 6000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_433D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_430C end

    def Function_27_4357(): pass

    label("Function_27_4357")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4382")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jump("Function_27_4357")

    label("loc_4382")

    Return()

    # Function_27_4357 end

    def Function_28_4383(): pass

    label("Function_28_4383")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_438F():
        OP_95(0xFE, -3800, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_438F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_43B4():
        OP_95(0xFE, -3800, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43B4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_4383 end

    def Function_29_43CE(): pass

    label("Function_29_43CE")

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
            "#00205FThis is a jewelry shop...\x02\x03",
            "#00202FMr. Lloyd,\x01",
            "can we have a look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, we still have time,\x01",
            "so I think it's fine.\x02\x03",
            "#00012FEven so...\x01",
            "You wanted to come that much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FY-Yes, well...\x01",
            "I heard they have a lot\x01",
            "of pretty accessories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha, is that so?\x02\x03",
            "#00000FThen, let's have a look together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209F...Yes.\x02",
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
            "#12P#00005FThis is quite an\x01",
            "amazing necklace.\x02\x03",
            "#00004FA Middle Ages jewel, eh...?\x01",
            "Somehow you can feel the history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F...Ehm, Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F...Ah, n-no.\x02\x03",
            "#00204FSince it is so pretty,\x01",
            "I was in a loss for words...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F...What is it?\x01",
            "Your eyes are wide open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FW-Well...\x01",
            "I thought it's unexpected.\x02\x03",
            "#00003FI thought about this other times too,\x01",
            "but to see that you show an interest\x01",
            "in these worldly things is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FE-Even I sometimes earnestly think\x01",
            "that these things are pretty.\x02\x03",
            "#00204F...Well, although in a certain sense it is thanks\x01",
            "to Mr. Lloyd and the others I started to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FAh...\x02\x03",
            "#00004F(That's right...thinking about it,\x01",
            "Tio too is an adolescent girl.)\x02\x03",
            "(Although the first time we met she\x01",
            "gave us the impression to be mature...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F...Mr. Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, it's nothing.\x02\x03",
            "#00004F(Oh, right, it's not to\x01",
            "curry her favor, but...)\x02\x03",
            "(It could be nice to give Tio\x01",
            "some kind of present.)\x02\x03",
            "#00000F(Something that could make her happy...)\x02",
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
            "#5P#00000F(This sapphirl hair ornament...\x01",
            "It looks like it would suit Tio perfectly.)\x02\x03",
            "#00003F(The price is...10000 mira, eh?)\x01",
            "(It's quite a lot, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5349")
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
            "Purchase the Hair Ornament\x01",      # 0
            "Quit\x01",                            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E9")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FTio, would you like that hair ornament\x01",
            "over there for a present?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        "#00205FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha, as you can imagine\x01",
            "I can't buy you a necklace\x01",
            "like that one there, but...\x02\x03",
            "#00000FI thought you too would want to\x01",
            "have something stylish like a girl, Tio.\x02\x03",
            "Of course it doesn't hold any\x01",
            "special meaning...what do you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204F...It makes me happy.\x02\x03",
            "#00200FHowever, can I say \x01",
            "just one thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F"Of course it doesn't hold any special meaning"...\x02\x03",
            "#00211FIsn't it in a certain sense rude to\x01",
            "assert that toward a woman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FHuh, i-is that so?\x02\x03",
            "#00002FI was thinking you could accept it as a present\x01",
            "between older brother and younger sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...*sigh*.\x02\x03",
            "#00211FWell, let's leave it at that\x01",
            "point of compromise for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00003FU-Uhhm...\x01",
            "Why aren't you convinced?\x02\x03",
            "#00012FAs I thought, do you prefer a Michey's\x01",
            "goods instead of a hair ornament...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00206F(This man is really...)\x02\x03",
            "#00202F...Oh, right.\x01",
            "If you want, please let me buy a\x01",
            "present for you too, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh, is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, since we are here...\x02\x03",
            "#00204FThen, please wait a little,\x01",
            "I'll look for something good.\x02",
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
            "Afterwards, Lloyd and Tio had each of the\x01",
            "jewels they bought wrapped by the clerk\x01",
            "and exchanged them as presents.\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x399),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x399, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_5344")

    label("loc_51E9")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Maybe I shouldn't.\x01",
            "It could spell trouble...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F...Mr. Lloyd, why don't\x01",
            "we have a look over there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FY-Yeah, got it. I'll keep you \x01",
            "company until you're satisfied.\x02",
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
            "Afterwards, Lloyd and Tio enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5344")

    Jump("loc_54EF")

    label("loc_5349")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Wait, first of all, I don't have enough mira.\x01",
            "It's a pity, but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F...Mr. Lloyd, why don't\x01",
            "we have a look over there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FY-Yeah, got it. I'll keep you \x01",
            "company until you're satisfied.\x02",
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
            "Afterwards, Lloyd and Tio enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_54EF")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_43CE end

    def Function_30_54FF(): pass

    label("Function_30_54FF")

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
        "#12P#00000FWe came to the jewelry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright, then I'll stay\x01",
            "with you to search\x01",
            "for a present.\x02\x03",
            "#00309FSo, who's your target?\x01",
            "Say it to your big bro here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No no.\x01",
            "It's not like that.\x02\x03",
            "#00000FIn any case, we have some time,\x01",
            "so let's have a look inside the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FYeah, got it.\x02",
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
            "#12P#00001FHow can I put it...\x02\x03",
            "#00006FThe more I look around, the more\x01",
            "I feel like it's not a store two men\x01",
            "alone should enter at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHey now, what about me\x01",
            "then who entered here\x01",
            "alone in broad daylight?\x02\x03",
            "#00300FWell, I agree with you, though.\x01",
            "Might as well go at the theme park\x01",
            "and hit on some girls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FL-Like I told you, we don't have the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBy the way, wasn't that the original\x01",
            "plan when we talked on the water bus?\x02\x03",
            "#00301FUnbelievable, you're one of those herbivores...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00302FAlright, since we're here, I'll buy you\x01",
            "an accessory as a present that will\x01",
            "increase your handsomeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...i-is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, I just saw something\x01",
            "in the show window over\x01",
            "there that could suit you.\x02\x03",
            "#00309FHa ha, it's just to have fun so\x01",
            "you have no need to be nervous.\x02\x03",
            "#00304FOf course it doesn't have\x01",
            "any particular meaning.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, no...\x01",
            "It would be a problem if it had one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, I'm jokin'.\x02\x03",
            "#00304FThen, I'll go have it\x01",
            "wrapped by the clerk.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4210, 1400, 7590, 2000)
    OP_6F(0x79)
    TurnDirection(0x104, 0xC, 500)

    ChrTalk(
        0x104,
        (
            "#11P#00309FAnd while I'm there, I'll get\x01",
            "an appointment with those\x01",
            "ladies over there for tonight!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 2, 0, 27)
    BeginChrThread(0x104, 3, 0, 26)

    def lambda_5C1D():

        label("loc_5C1D")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5C1D")

    QueueWorkItem2(0x101, 2, lambda_5C1D)
    WaitChrThread(0x104, 3)
    EndChrThread(0x104, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    def lambda_5C3F():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5C3F)
    TurnDirection(0xD, 0x104, 500)
    EndChrThread(0x101, 0xFF)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha, oh man...\x02\x03",
            "#00004F(However, we're all helped\x01",
            "by his caring attitude.)\x02\x03",
            "(I'd like to express to him my thanks\x01",
            "as the Support Section leader...)\x02\x03",
            "#00000F(We're in a jewelry after all, I guess\x01",
            "I will carefully look for something too.)\x02",
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
            "#5P#00000F(This carnelia-studded bracelet...\x01",
            "It could suit Randy.)\x02\x03",
            "#00003F(The price is...10000 mira, eh?)\x01",
            "(It's quite a lot, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6179")
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
            "Purchase the Bracelet\x01",      # 0
            "Quit\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6003")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FUhm, excuse me.\x01",
            "I would like this bracelet...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4B(0x9, 0xFF)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "#5PYes, right away.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd made jokes to console a shrugged\x01",
            "Randy for having failed to hit on the girls...\x02\x03",
            "They had their jewelry wrapped by the clerk\x01",
            "and they gave them as present to each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_6174")

    label("loc_6003")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Somehow it's awkward,\x01",
            "so I won't purchase it.)\x02\x03",
            "#00000F(As for my feelings of gratitude for\x01",
            "Randy... I'll have to express them\x01",
            "in a different way another day.)\x02",
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
            "Afterwards, Lloyd made jokes to console a shrugged\x01",
            "Randy for having failed to hit on the girls...\x02\x03",
            "After receiving the jewel from Randy,\x01",
            "they left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6174")

    Jump("loc_62EA")

    label("loc_6179")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Wait, first of all, I don't have enough mira.)\x02\x03",
            "#00008F(It's rude but it seems I have to give up \x01",
            "the idea to make him a present...)\x02",
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
            "Afterwards, Lloyd made jokes to console a shrugged\x01",
            "Randy for having failed to hit on the girls...\x02\x03",
            "After receiving the jewel from Randy,\x01",
            "they left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_62EA")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39A, 1)
    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_54FF end

    def Function_31_6331(): pass

    label("Function_31_6331")

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
            "#10108FUhhm, I looked around it briefly\x01",
            "with Fran during the day, but...\x02\x03",
            "#10106F*haah*, I really\x01",
            "feel out of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FTo begin with, if Miss\x01",
            "Mariabell hadn't mediated,\x01",
            "we couldn't have entered.\x02\x03",
            "#00000FWell, we're here, so do you want\x01",
            "to look around with me this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, allow me to keep you company!\x02",
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
        "#5P#10103FUhhm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00005FIs something wrong, Noｱl?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10101FNo, it's just that, I was thinking about\x01",
            "this when I was having a look before...\x02\x03",
            "#10106FSomehow, aren't there a lot of\x01",
            "jewels that are useless?\x02\x03",
            "#10108FWhen wearing them it\x01",
            "looks difficult to move and\x01",
            "they're a hindrance for work...\x02",
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
            "#6P#10111FAh, I-I'm sorry!\x01",
            "You were enjoying looking at them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, well, somehow it's a point\x01",
            "of view I'd expect from you, Noｱl.\x02\x03",
            "#00000FNow that I think about it, Noｱl, \x01",
            "your civilian clothes look easy to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FAhaha...\x01",
            "I pay attention in selecting them\x01",
            "putting a lot of importance on that regard.\x02\x03",
            "#10106FIf I choose them alone,\x01",
            "they tend to turn out very\x01",
            "mannish and that's a problem.\x02\x03",
            "#10100FThat's why I always ask Fran and\x01",
            "have her coordinate them for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, I see.\x02\x03",
            "#00000FThen, could there be something\x01",
            "you're interested in this store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FLet's see...\x02",
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
            "#5P#10102FOh, this choker\x01",
            "with an amberl in...\x02\x03",
            "#10109FWhen I saw it this morning\x01",
            "with Fran, I thought it was\x01",
            "somehow nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, indeed, it'll suit you, Noｱl.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(That's right, we came here together,\x01",
            "so it could be nice giving it to her as a present.)\x02\x03",
            "#00003F(The price is...10000 mira, eh?)\x01",
            "(It's quite a lot, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_71AE")
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
            "Purchase the Choker\x01",      # 0
            "Quit\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7004")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FNoｱl, this choker...\x01",
            "Would you accept it as a present from me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FEh............\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10111FEEEEEEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh, could I have bothered you?\x02\x03",
            "#00004FYou're doing your best having been\x01",
            "assigned to the Support Section...\x01",
            "It's to express my appreciation,\x01",
            "it doesn't have a particular meaning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10111FE-Eehm...no, it's not that!!\x01",
            "I-I'm happy, but...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI-Is there any problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F...N-No!!\x01",
            "It's not that...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#6P#10101F...T-Then!\x01",
            "Since you proposed it,\x01",
            "I'll humbly accept it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHa ha, you don't have to humble yourself...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FN-No...\x01",
            "Really, thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10103FOh, right, then...\x02\x03",
            "#10100FMr. Lloyd, would you accept\x01",
            "some present from me too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh, is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, we're here and...\x02\x03",
            "#10100FPlease wait a moment,\x01",
            "I'll look for something nice.\x02",
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
            "Afterwards, Lloyd and Noｱl had each of the\x01",
            "jewels they bought wrapped by the clerk\x01",
            "and exchanged them as presents.\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x39B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39B, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_71A9")

    label("loc_7004")


    ChrTalk(
        0x101,
        (
            "#00006F(...Uhhm, as I thought, I'll pass.\x01",
            "It could create a misunderstanding with Fran...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FMr. Lloyd, is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, no, it's nothing.\x02\x03",
            "#00000FLet's see if there're other\x01",
            "articles that could be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYes, you're right!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Noｱl enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_71A9")

    Jump("loc_7377")

    label("loc_71AE")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, first of all, I don't have enough mira.\x01",
            "It's a pity, but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#6P#10105FMr. Lloyd, is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, no, it's nothing.\x02\x03",
            "#00000FLet's see if there're other\x01",
            "articles that could be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYes, I agree!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Noｱl enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7377")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6331 end

    def Function_32_7387(): pass

    label("Function_32_7387")

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
        "#12P#00000FWell, it seems we came to the jewelry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWe have some time until the dinner party...\x01",
            "Do you want to have a look together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah, since we're already here,\x01",
            "that could be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, it's decided then.\x01",
            "Then, let's have a brief tour.\x02",
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
            "#00003FUhhm, as expected, because it's a members\x01",
            "only store, they have high priced articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, since we're here, \x01",
            "giving KeA a ring or\x01",
            "something could be nice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00006FHey there, that's not\x01",
            "something to give a kid.\x02\x03",
            "#00005F...By the way, Wazy, you've\x01",
            "been pretty popular since before\x01",
            "You joined the SSS, right?\x02\x03",
            "#00003FIt seems you also had tactical\x01",
            "orbments when we met...\x02\x03",
            "#00000FIt's something they commonly say,\x01",
            "but a host club is really\x01",
            "quite profitable, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FNo? After all it's only a side job,\x01",
            "so because I help occasionally,\x01",
            "my actual pay is not that much.\x02\x03",
            "#10304FAt the club, if I have to say, there're many\x01",
            "other sources of income than your pay.\x02\x03",
            "#10302FSometimes it happens that\x01",
            "you receive jewels as pocket\x01",
            "mira from the wealthy mesdames.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I-I see.\x01",
            "I can't agree with that very much,\x01",
            "but those become your income...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, no no.\x01",
            "I don't exchange what I receive from\x01",
            "the customers for mira, you know?\x02\x03",
            "#10304FThe ENIGMA I had before too,\x01",
            "I purchased that with my own mira\x01",
            "from Miss Ashley's store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005F...Then, in the end, where's\x01",
            "that mira coming from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10309FHu hu, that's a trade secret.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FT-The heck is that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, well, leaving those\x01",
            "trivial things aside...\x02\x03",
            "#10302FLloyd, could you accept this,\x01",
            "if you want?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x39C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt's an accessory I found\x01",
            "just before in the show\x01",
            "case over there.\x02\x03",
            "#10304FI thought it would've suited you,\x01",
            "and since I was here, I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-When did you...?\x02\x03",
            "#00005FBut, can I really have something\x01",
            "so expensive-looking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, it's a simple whim of mine,\x01",
            "so don't think too much about it.\x02\x03",
            "#10309FIt's cheap stuff if I can\x01",
            "get your gratitude with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FH-Hey there...\x02\x03",
            "#00000FBut, well, thanks.\x01",
            "Thank you, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHu hu, you're welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(...Right, only receiving\x01",
            "this wouldn't be nice...)\x02\x03",
            "#00004F(Maybe it would be nice to\x01",
            "give him something in return.)\x02\x03",
            "#00000F(Thanks to Wazy joining, the Support Section\x01",
            "flexibility has increased in a certain sense...\x01",
            "Something that could convey my thanks for that...)\x02",
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
            "#00000F(It looks like this goldia pendant\x01",
            "would suit Wazy.)\x02\x03",
            "#00003F(The price is...10000 mira, eh?)\x01",
            "(It's quite a lot, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83E7")
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
            "Purchase the Pendant\x01",      # 0
            "Quit \x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823C")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FThen, could you accept this\x01",
            "pendant as a gift in return?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x2D, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10305FEeh, are you sure?\x02\x03",
            "#10300FHu hu, your tact\x01",
            "is not bad at all.\x02\x03",
            "#10302FIt's cheap as a gift, but,\x01",
            "well, I guess it can pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now...\x01",
            "If you don't want it, I won't buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAh ah ha, not at all.\x02\x03",
            "#10302FIt's something you chose putting your heart into it.\x01",
            "I'll humbly accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F...Ha ha,  oh, well.\x01",
            "I'll go call the clerk.\x02",
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
            "Afterwards, Lloyd had the jewel\x01",
            "he bought wrapped by the clerk\x01",
            "and gave it to Wazy as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_83E2")

    label("loc_823C")


    ChrTalk(
        0x101,
        (
            "#00006F(...As I thought, I guess I won't buy it this time.\x01",
            "I'll make up for this on another occasion.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's nothing.\x02\x03",
            "#00000FWe have some time until the appointment,\x01",
            "so let's have a look inside the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Wazy enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_83E2")

    Jump("loc_85AA")

    label("loc_83E7")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, first of all, I don't have enough mira.\x01",
            "It's a pity, but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's nothing.\x02\x03",
            "#00000FWe have some time until the appointment,\x01",
            "so let's have a look inside the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and Wazy enjoyed\x01",
            "window shopping for a little while\x01",
            "and then left the jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_85AA")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_7387 end

    SaveToFile()

Try(main)
