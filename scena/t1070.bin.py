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
        "Function_4_740",          # 04, 4
        "Function_5_B16",          # 05, 5
        "Function_6_C8E",          # 06, 6
        "Function_7_11DF",         # 07, 7
        "Function_8_12D2",         # 08, 8
        "Function_9_12D6",         # 09, 9
        "Function_10_19A6",        # 0A, 10
        "Function_11_1D5E",        # 0B, 11
        "Function_12_1F3A",        # 0C, 12
        "Function_13_1FC7",        # 0D, 13
        "Function_14_213E",        # 0E, 14
        "Function_15_22F9",        # 0F, 15
        "Function_16_2D58",        # 10, 16
        "Function_17_2DB1",        # 11, 17
        "Function_18_2E0A",        # 12, 18
        "Function_19_2E63",        # 13, 19
        "Function_20_2EAE",        # 14, 20
        "Function_21_2F00",        # 15, 21
        "Function_22_4144",        # 16, 22
        "Function_23_4196",        # 17, 23
        "Function_24_421A",        # 18, 24
        "Function_25_4273",        # 19, 25
        "Function_26_42C5",        # 1A, 26
        "Function_27_4310",        # 1B, 27
        "Function_28_433C",        # 1C, 28
        "Function_29_4387",        # 1D, 29
        "Function_30_545D",        # 1E, 30
        "Function_31_62BB",        # 1F, 31
        "Function_32_72B5",        # 20, 32
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
    Jump("loc_73C")

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_551")
    Jump("loc_73C")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_55F")
    Jump("loc_73C")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_676")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635")

    ChrTalk(
        0x11,
        (
            "#06406FNoｱl has been acting\x01",
            "strange for some time\x01",
            "now.\x02\x03",
            "#06402FDid something happen at\x01",
            "the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well... That would be\x01",
            "a little hard for me to\x01",
            "explain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#06405F???\x02",
    )

    CloseMessageWindow()
    Jump("loc_671")

    label("loc_635")


    ChrTalk(
        0x11,
        (
            "#06406FNoｱl has been acting\x01",
            "strange for some time\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671")

    Jump("loc_73C")

    label("loc_676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_691")
    Call(0, 5)
    Jump("loc_712")

    label("loc_691")


    ChrTalk(
        0x11,
        (
            "#06409FLloyd, please give her\x01",
            "this necklace as a\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FN-No, no. As you\x01",
            "probably guessed, I\x01",
            "can't afford it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_712")

    Jump("loc_73C")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_725")
    Jump("loc_73C")

    label("loc_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_733")
    Jump("loc_73C")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_73C")

    label("loc_73C")

    TalkEnd(0xFE)
    Return()

    # Function_3_532 end

    def Function_4_740(): pass

    label("Function_4_740")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_751")
    Jump("loc_B12")

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_75F")
    Jump("loc_B12")

    label("loc_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_76D")
    Jump("loc_B12")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_957")

    ChrTalk(
        0x10,
        (
            "#10106F*sigh*... I knew there was the\x01",
            "danger, but I can't believe my\x01",
            "swimsuit was really torn...\x02\x03",
            "#10101FNot being able to defend against\x01",
            "that level of attack means I still\x01",
            "have a lot of training to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...*c-cough*. Me too. If\x01",
            "I had somehow noticed it\x01",
            "a little sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10114FAh, n-no! I wasn't\x01",
            "seriously injured!\x02\x03",
            "#10103FI-It's true that it was\x01",
            "embarrassing, but... I'll\x01",
            "let this drive my training!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(T-Training for\x01",
            "what...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A27")

    label("loc_957")


    ChrTalk(
        0x10,
        (
            "#10106F*sigh*... Not being able to defend\x01",
            "against that level of attack means that\x01",
            "I still have a lot of training to do.\x02\x03",
            "#10101FBecause of that, it was embarrassing...\x01",
            "I must let this drive my training!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A27")

    Jump("loc_B12")

    label("loc_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A47")
    Call(0, 5)
    Jump("loc_ADA")

    label("loc_A47")


    ChrTalk(
        0x10,
        (
            "#10106FS-Such a wonderful\x01",
            "necklace... But who could\x01",
            "afford something like this?\x02\x03",
            "#10101FIt might be priced the same\x01",
            "as a national treasure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADA")

    Jump("loc_B12")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AED")
    Jump("loc_B12")

    label("loc_AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_AFB")
    Jump("loc_B12")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B09")
    Jump("loc_B12")

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B12")

    label("loc_B12")

    TalkEnd(0xFE)
    Return()

    # Function_4_740 end

    def Function_5_B16(): pass

    label("Function_5_B16")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x10,
        (
            "#10109F*siiigh*, what a pretty\x01",
            "necklace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06402FIt seems it's this\x01",
            "store's showpiece.\x02\x03",
            "#06405FHmm, what about the\x01",
            "price... ...So the zeros\x01",
            "are one, two, three...\x02",
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
            "#10106F...You could buy several\x01",
            "orbal cars with just\x01",
            "this one necklace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#06406FI-It really is a whole\x01",
            "other world.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_5_B16 end

    def Function_6_C8E(): pass

    label("Function_6_C8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C9F")
    Jump("loc_11DB")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CAD")
    Jump("loc_11DB")

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_CBB")
    Jump("loc_11DB")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1043")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(
        0xF,
        (
            "#00300FYo, Lloyd. It seems\x01",
            "you've found Keddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109FEhehe, sorry for\x01",
            "wandering around on my\x01",
            "own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00303F...Alright, I forgive\x01",
            "you! There's no way I\x01",
            "couldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha...\x02\x03",
            "#00005F...Oh Randy, were you\x01",
            "buying something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00302FYeah, I was thinkin' about\x01",
            "a small present for\x01",
            "Mireille.\x02\x03",
            "#00304FHer promotion seems close,\x01",
            "so I was looking for\x01",
            "something to celebrate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow, I see...\x02\x03",
            "#00012FSay, could it be that\x01",
            "you... About 2nd Lt.\x01",
            "Mireille...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#00304FHaha, what nonsense are\x01",
            "you spoutin' this time?\x02\x03",
            "#00300FI owe her for my time at\x01",
            "the CGF, so it's just\x01",
            "good manners, see?\x02\x03",
            "#00309FAlso, my eye is on\x01",
            "Cecil!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI can't allow that statement\x01",
            "to pass, but... Well, I\x01",
            "guess that's how it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 1)
    Jump("loc_103E")

    label("loc_FBC")


    ChrTalk(
        0xF,
        (
            "#00300FI'll be goin' to the\x01",
            "meeting place with Noｱl\x01",
            "and the others in a bit.\x02\x03",
            "#00304FI'll do some window\x01",
            "shopping 'til then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103E")

    Jump("loc_11DB")

    label("loc_1043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(
        0xF,
        (
            "#00301FHmm, a necklace...?\x02\x03",
            "#00306FKnowin' how she is, she'd likely\x01",
            "say something like that'd be in\x01",
            "the way durin' training.\x02",
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
    Jump("loc_11B1")

    label("loc_1115")


    ChrTalk(
        0xF,
        (
            "#00303FMaybe some small accessory\x01",
            "that doesn't get in the way\x01",
            "too much would be better.\x02\x03",
            "#00300FI guess I'll have a look at\x01",
            "those brooches over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_11DB")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_11C4")
    Jump("loc_11DB")

    label("loc_11C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11D2")
    Jump("loc_11DB")

    label("loc_11D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11DB")

    label("loc_11DB")

    TalkEnd(0xFE)
    Return()

    # Function_6_C8E end

    def Function_7_11DF(): pass

    label("Function_7_11DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_11F0")
    Jump("loc_12CE")

    label("loc_11F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11FE")
    Jump("loc_12CE")

    label("loc_11FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_120C")
    Jump("loc_12CE")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_129B")

    ChrTalk(
        0xE,
        (
            "#10305F...Oh, this jewel is\x01",
            "similar to one I received\x01",
            "from that lady recently.\x02\x03",
            "#10302FHehe, could she have\x01",
            "bought it here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CE")

    label("loc_129B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12A9")
    Jump("loc_12CE")

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_12B7")
    Jump("loc_12CE")

    label("loc_12B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12C5")
    Jump("loc_12CE")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12CE")

    label("loc_12CE")

    TalkEnd(0xFE)
    Return()

    # Function_7_11DF end

    def Function_8_12D2(): pass

    label("Function_8_12D2")

    Call(0, 9)
    Return()

    # Function_8_12D2 end

    def Function_9_12D6(): pass

    label("Function_9_12D6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 7)), scpexpr(EXPR_END)), "loc_1420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B8")

    ChrTalk(
        0x8,
        (
            "Hohoho... Thank you very\x01",
            "much for your purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jewelry is a gift that can\x01",
            "truly express different\x01",
            "emotions in one's life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pray to the Goddess that\x01",
            "it is well-received.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_141B")

    label("loc_13B8")


    ChrTalk(
        0x8,
        (
            "Jewelry is truly the\x01",
            "gift of a lifetime...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pray to the Goddess that\x01",
            "it is well-received.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141B")

    Jump("loc_15FA")

    label("loc_1420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152A")

    ChrTalk(
        0x8,
        (
            "Jewelry is a gift that can\x01",
            "truly express different\x01",
            "emotions in one's life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although, seizing the chance\x01",
            "to give it is, well, up to\x01",
            "the person themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hohoho... Next time you\x01",
            "come, please do it after\x01",
            "having lined up your purse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FA")

    label("loc_152A")


    ChrTalk(
        0x8,
        (
            "Jewelry is truly the gift of a lifetime...\x01",
            "Although seizing the chance to give it is,\x01",
            "well, up to the person themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hohoho... Next time you\x01",
            "come, please do it after\x01",
            "having lined up your purse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FA")

    Jump("loc_19A2")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_185F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176D")

    ChrTalk(
        0x8,
        (
            "Our members-only system is in\x01",
            "place to offer top service to\x01",
            "our trusted regular customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When the number of customers\x01",
            "increases, the quality of service\x01",
            "always goes down, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It means simply that attracting as many\x01",
            "customers as possible isn't the only way to do\x01",
            "business. Hohoho, perhaps you learned something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_185A")

    label("loc_176D")


    ChrTalk(
        0x8,
        (
            "Our members-only system is in\x01",
            "place to offer top service to\x01",
            "our trusted regular customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It means simply that attracting as many\x01",
            "customers as possible isn't the only way to do\x01",
            "business. Hohoho, perhaps you learned something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185A")

    Jump("loc_19A2")

    label("loc_185F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_19A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(
        0x8,
        (
            "Hohoho... Welcome to my\x01",
            "Diamante Jewelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here we stock only the\x01",
            "finest jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if you have the\x01",
            "right to have this\x01",
            "eternal brilliance...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19A2")

    label("loc_191E")


    ChrTalk(
        0x8,
        (
            "At Diamante we have only\x01",
            "the finest jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hohoho... I wonder if you\x01",
            "have the right to have this\x01",
            "eternal brilliance...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A2")

    TalkEnd(0x8)
    Return()

    # Function_9_12D6 end

    def Function_10_19A6(): pass

    label("Function_10_19A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19E5")

    ChrTalk(
        0x9,
        (
            "...We'll be waiting for\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5A")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1C23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B55")

    ChrTalk(
        0x9,
        (
            "The necklace displayed in the\x01",
            "display case over there is\x01",
            "called "The Saint's Tears".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This necklace was excavated from a ruin thought\x01",
            "to have been the property of a middle ages\x01",
            "feudal lord. We have it on special display.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has a price for a matter of\x01",
            "convenience, but we cannot sell it.\x01",
            "Please be aware of this, just in case.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C1E")

    label("loc_1B55")


    ChrTalk(
        0x9,
        (
            "The necklace displayed in the\x01",
            "display case over there is\x01",
            "called "The Saint's Tears".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has a price for a matter of\x01",
            "convenience, but we cannot sell it.\x01",
            "Please be aware of this, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1E")

    Jump("loc_1D5A")

    label("loc_1C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDD")

    ChrTalk(
        0x9,
        (
            "I am very sorry for\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From now on, we will\x01",
            "respectfully receive you\x01",
            "as special members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please feel free to ask\x01",
            "me if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D5A")

    label("loc_1CDD")


    ChrTalk(
        0x9,
        (
            "From now on, we will\x01",
            "respectfully receive you\x01",
            "as special members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please feel free to ask\x01",
            "me if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5A")

    TalkEnd(0xFE)
    Return()

    # Function_10_19A6 end

    def Function_11_1D5E(): pass

    label("Function_11_1D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1D6F")
    Jump("loc_1F36")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1D7D")
    Jump("loc_1F36")

    label("loc_1D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")

    ChrTalk(
        0xA,
        (
            "Crossbell possesses Mainz\x01",
            "Mine, where a great quantity\x01",
            "of septium is excavated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The jewelry on display in this store...\x01",
            "It looks like they have high quality\x01",
            "jewels, specially crafted from septium...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, as expected from a\x01",
            "place like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F36")

    label("loc_1E99")


    ChrTalk(
        0xA,
        (
            "It looks like this store\x01",
            "has high quality jewelry\x01",
            "crafted from septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess it's to be expected\x01",
            "from Crossbell, with its\x01",
            "access to Mainz Mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F36")

    TalkEnd(0xFE)
    Return()

    # Function_11_1D5E end

    def Function_12_1F3A(): pass

    label("Function_12_1F3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1F4B")
    Jump("loc_1FC3")

    label("loc_1F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1F59")
    Jump("loc_1FC3")

    label("loc_1F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1FC3")

    ChrTalk(
        0xB,
        (
            "Hehe, it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it's for you, one or\x01",
            "two necklaces are no\x01",
            "trouble at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC3")

    TalkEnd(0xFE)
    Return()

    # Function_12_1F3A end

    def Function_13_1FC7(): pass

    label("Function_13_1FC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_20D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203D")

    ChrTalk(
        0xC,
        "Haha, sorry for earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Despite appearances, we\x01",
            "each have a darling we\x01",
            "love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CB")

    label("loc_203D")


    ChrTalk(
        0xC,
        (
            "Yes. I've been visiting\x01",
            "the Empire often lately,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's nothing at all like\x01",
            "this store's high quality\x01",
            "selection of jewelry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CB")

    Jump("loc_213A")

    label("loc_20D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_20DE")
    Jump("loc_213A")

    label("loc_20DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_213A")

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
            "Say, darling, won't you\x01",
            "buy it for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213A")

    TalkEnd(0xFE)
    Return()

    # Function_13_1FC7 end

    def Function_14_213E(): pass

    label("Function_14_213E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21C7")

    ChrTalk(
        0xD,
        (
            "Playing with love\x01",
            "somewhat is charming,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think that a lady's\x01",
            "fidelity is very\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224F")

    label("loc_21C7")


    ChrTalk(
        0xD,
        (
            "Haha, you can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As expected, the septium crafts\x01",
            "produced in other countries don't\x01",
            "hold a candle to Crossbell's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224F")

    Jump("loc_22F5")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_22EC")

    ChrTalk(
        0xD,
        (
            "I can't quite find\x01",
            "suitable jewels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, encounters with jewels are\x01",
            "once-in-a-lifetime... I think\x01",
            "I'll keep looking patiently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F5")

    label("loc_22EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_22F5")

    label("loc_22F5")

    TalkEnd(0xFE)
    Return()

    # Function_14_213E end

    def Function_15_22F9(): pass

    label("Function_15_22F9")

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
            "#6P#10300FIf I'm not mistaken,\x01",
            "it's a members-only\x01",
            "jeweler.\x02\x03",
            "#10304FI've been here several\x01",
            "times with customers\x01",
            "from the nightclub.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_2556")

    ChrTalk(
        0x104,
        (
            "#6P#00306FThey turned us away at\x01",
            "the entrance when we came\x01",
            "here last time, right?\x02\x03",
            "#00301FThat clerk's attitude\x01",
            "pisses me off a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAh, now that you mention\x01",
            "it, we weren't stopped\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C6")

    label("loc_2556")


    ChrTalk(
        0x104,
        (
            "#6P#00306FRegulars only, huh...?\x01",
            "How unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FHuh, then I guess we\x01",
            "shouldn't go inside?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C6")

    OP_68(-3330, 400, 5840, 2500)
    OP_6F(0x1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    NpcTalk(
        0x9,
        "Clerk",
        "Gentlemen.\x02",
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

    def lambda_266D():

        label("loc_266D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_266D")

    QueueWorkItem2(0x101, 2, lambda_266D)

    def lambda_267F():

        label("loc_267F")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_267F")

    QueueWorkItem2(0x104, 2, lambda_267F)

    def lambda_2691():

        label("loc_2691")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2691")

    QueueWorkItem2(0x105, 2, lambda_2691)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x105, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_26E6")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHehe. Speak of the\x01",
            "devil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FE")

    label("loc_26E6")


    ChrTalk(
        0x101,
        "#12P#00011FWhoa...\x02",
    )

    CloseMessageWindow()

    label("loc_26FE")


    ChrTalk(
        0x9,
        (
            "#5PWelcome to Diamante\x01",
            "Jewelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...Pardon me gentlemen. Would\x01",
            "any of you happen to have a\x01",
            "letter of introduction?\x02",
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
        (
            "#5PThen please refrain from\x01",
            "entering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POur store's memberships\x01",
            "are limited to select\x01",
            "customers, you see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306FTch, it can't be\x01",
            "helped... Let's go,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FRight, we also have an\x01",
            "appointment at the\x01",
            "beach...\x02",
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

    def lambda_28F5():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28F5)
    Sleep(50)

    def lambda_2905():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2905)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x9,
        (
            "#5P...Gentlemen. Might you\x01",
            "be from the "Special\x01",
            "Support Section"?\x02",
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
        (
            "#12P#00005FYes, that's right,\x01",
            "but...\x02",
        )
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
        "#6P#00305FW-What is it now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PA-Ahem... Lady Mariabell\x01",
            "contacted us not long\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PShe said to give you all\x01",
            "special permission to\x01",
            "enter the shop today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PPlease forgive my\x01",
            "rudeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUmm, then... Does that\x01",
            "mean we can shop here as\x01",
            "well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIndeed. We shall treat\x01",
            "you all as special\x01",
            "guests from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThen, please feel free\x01",
            "to ask me if you need\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 3)
    OP_4C(0x9, 0xFF)

    def lambda_2BD3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BD3)

    def lambda_2BE0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BE0)

    def lambda_2BED():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BED)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_93(0x105, 0x13B, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. It seems she was\x01",
            "considerate enough to do\x01",
            "this for us, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FEven so, that clerk sure\x01",
            "came around quickly.\x02\x03",
            "#00300FWell since that's\x01",
            "settled, let's make good\x01",
            "use of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012FHaha. But everything's so\x01",
            "expensive. We might not be\x01",
            "able to afford anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15B, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 800, 0)
    EventEnd(0x5)
    Return()

    # Function_15_22F9 end

    def Function_16_2D58(): pass

    label("Function_16_2D58")


    def lambda_2D5D():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D5D)

    def lambda_2D77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D77)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2D90():
        OP_95(0xFE, 0, 0, 800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D90)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2D58 end

    def Function_17_2DB1(): pass

    label("Function_17_2DB1")


    def lambda_2DB6():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DB6)

    def lambda_2DD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DD0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2DE9():
        OP_95(0xFE, -790, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DE9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_2DB1 end

    def Function_18_2E0A(): pass

    label("Function_18_2E0A")


    def lambda_2E0F():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E0F)

    def lambda_2E29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E29)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2E42():
        OP_95(0xFE, 870, 0, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E42)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_2E0A end

    def Function_19_2E63(): pass

    label("Function_19_2E63")


    def lambda_2E68():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E68)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x0)

    def lambda_2E8D():
        OP_95(0xFE, -3560, 0, 2870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E8D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_2E63 end

    def Function_20_2EAE(): pass

    label("Function_20_2EAE")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2EBA():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EBA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x0)

    def lambda_2EDF():
        OP_95(0xFE, -6300, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EDF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_20_2EAE end

    def Function_21_2F00(): pass

    label("Function_21_2F00")

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
            "#00105FThis is Diamante...\x02\x03",
            "#00104FAs expected, they have\x01",
            "an assortment of pretty\x01",
            "jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. You went to the\x01",
            "boutique during the day,\x01",
            "didn't you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, by the way... You're not a\x01",
            "member of this place, are you\x01",
            "Elie.\x02\x03",
            "#00000FBeing Mariabell's childhood\x01",
            "friend, I thought you'd receive\x01",
            "the VIP treatment, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FHmm. When I came here with\x01",
            "Bell before, we didn't\x01",
            "visit the jewelry store.\x02\x03",
            "#00100FI feel like looking at\x01",
            "clothes at the boutique\x01",
            "suits her personality more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, I see.\x02\x03",
            "#00000FThen, since we're here,\x01",
            "why don't we have a\x01",
            "look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYes, let's.\x02",
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
            "#6P#00000FNecklaces, rings,\x01",
            "brooches...\x02\x03",
            "#00003FThere's really a lot of\x01",
            "different kinds of\x01",
            "jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100F*giggle*, right. Although each\x01",
            "is rather expensive and not\x01",
            "easily within our reach...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00102FLook at this, Lloyd.\x01",
            "Isn't this ring just\x01",
            "lovely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FLet's see...\x02\x03",
            "#00000FYes, indeed... It looks\x01",
            "good on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00109F*giggle*, you don't have\x01",
            "to flatter me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo, no. I mean it.\x02\x03",
            "#00003F(The price is about three\x01",
            "months' salary, huh...\x01",
            "That's quite a bit.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00011F(Wait, this corner\x01",
            "is...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 24)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x9,
        (
            "Sir and madam, might you\x01",
            "be looking for a wedding\x01",
            "ring?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_352C():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_352C)
    Sleep(50)

    def lambda_353C():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_353C)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x9,
        (
            "If you like, I could\x01",
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
        "#6P#00012FHaha, no, ummm...\x02",
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
            "My apologies. You seemed to be\x01",
            "browsing our selection of\x01",
            "engagement rings and I assumed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#6P#00112FUmm, uh...!\x02\x03",
            "#00112FU-Umm... T-That's not\x01",
            "it! We aren't like that\x01",
            "yet...!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00112FL-Lloyd, it's not like\x01",
            "that, ok!?\x02\x03",
            "#00113FI wasn't trying to get\x01",
            "you to...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FI-I know, you don't have\x01",
            "to get so flustered...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Hmm, then were you\x01",
            "discussing it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#6P#00112FI-I already told you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012F(Haha... It's too bad she had\x01",
            "to explain things so\x01",
            "desperately like that, but...)\x02\x03",
            "#00004F(...But, that's right. Elie is\x01",
            "always helping me out.)\x02\x03",
            "#00000F(Setting aside the wedding\x01",
            "ring, a gift should be plenty\x01",
            "to thank her for that.)\x02",
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
            "I think it would look\x01",
            "great on Elie.)\x02\x03",
            "#00003F(And the price... 10,000\x01",
            "mira, huh. It's quite a\x01",
            "bit, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F7A")
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
            "Purchase the brooch\x01",      # 0
            "Refuse\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E08")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FExcuse me, could you\x01",
            "wrap this brooch for me?\x02",
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
        "#11P#00112FL-Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha. You help me out\x01",
            "every day, Elie.\x02\x03",
            "#00000FIt doesn't have any\x01",
            "special meaning, but will\x01",
            "you accept this present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00113F(I-I feel like it has\x01",
            "plenty of special\x01",
            "meaning, though, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FI-It's really no good?\x01",
            "As I thought, a present\x01",
            "from me is...\x02",
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
            "#00104F...Ahem. Thank you. I'm\x01",
            "happy Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00100FThen, in return... I wonder if\x01",
            "I could choose something that\x01",
            "will look good on you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100F*giggle*, since we're\x01",
            "here...\x02\x03",
            "#00109FThen, please wait a\x01",
            "moment. I'll find\x01",
            "something nice for you.\x02",
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
            "Afterwards, Lloyd and Elie had the\x01",
            "jewelry they each bought wrapped by the\x01",
            "clerk and exchanged them as presents.\x07\x00\x02",
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
    Jump("loc_3F75")

    label("loc_3E08")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(...It's a little too\x01",
            "serious. I guess I'll\x01",
            "pass this time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F...L-Like I said, we're\x01",
            "not even lovers yet,\x01",
            "and...\x02",
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
            "#11P#00113FW-Wait, Lloyd! Please\x01",
            "explain this too!\x02",
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
            "Afterwards, Lloyd and Elie\x01",
            "left the jewelry shop\x01",
            "feeling slightly awkward.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3F75")

    Jump("loc_4134")

    label("loc_3F7A")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(...Wait, I don't have enough mira for\x01",
            "this in the first place. It's a pity,\x01",
            "but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00112F...L-Like I said, we're\x01",
            "not even lovers yet,\x01",
            "and...\x02",
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
            "#11P#00113FW-Wait, Lloyd! Please\x01",
            "explain this too!\x02",
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
            "Afterwards, Lloyd and Elie\x01",
            "left the jewelry shop\x01",
            "feeling slightly awkward.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4134")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2F00 end

    def Function_22_4144(): pass

    label("Function_22_4144")


    def lambda_4149():
        OP_95(0xFE, 800, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4149)

    def lambda_4163():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4163)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_417C():
        OP_95(0xFE, 800, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_417C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_4144 end

    def Function_23_4196(): pass

    label("Function_23_4196")


    def lambda_419B():
        OP_95(0xFE, -200, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_419B)

    def lambda_41B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41B5)
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

    def lambda_4200():
        OP_95(0xFE, -200, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4200)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_4196 end

    def Function_24_421A(): pass

    label("Function_24_421A")


    def lambda_421F():
        OP_95(0xFE, 4120, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_421F)

    def lambda_4239():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4239)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_4259():
        OP_95(0xFE, 4120, 0, 7340, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4259)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_421A end

    def Function_25_4273(): pass

    label("Function_25_4273")


    def lambda_4278():
        OP_95(0xFE, -500, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4278)

    def lambda_4292():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4292)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_42AB():
        OP_95(0xFE, -500, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42AB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_4273 end

    def Function_26_42C5(): pass

    label("Function_26_42C5")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_42D1():
        OP_95(0xFE, 650, 0, 8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42D1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_42F6():
        OP_95(0xFE, 650, 0, 6000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42F6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_42C5 end

    def Function_27_4310(): pass

    label("Function_27_4310")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_433B")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jump("Function_27_4310")

    label("loc_433B")

    Return()

    # Function_27_4310 end

    def Function_28_433C(): pass

    label("Function_28_433C")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_4348():
        OP_95(0xFE, -3800, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4348)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_436D():
        OP_95(0xFE, -3800, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_436D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_433C end

    def Function_29_4387(): pass

    label("Function_29_4387")

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
            "#00205FThis is a jewelry\x01",
            "store...\x02\x03",
            "#00202FLloyd, can we have a\x01",
            "look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. There's still\x01",
            "time, so I think it's\x01",
            "fine.\x02\x03",
            "#00012FEven so... You wanted to\x01",
            "come here that badly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FY-Yes, well... I heard\x01",
            "they have lots of pretty\x01",
            "accessories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, is that so?\x02\x03",
            "#00000FThen, let's have a look\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209FRight.\x02",
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
            "#12P#00005FThis necklace is amazing\x01",
            "too.\x02\x03",
            "#00004FA Middle Age jewel,\x01",
            "huh... You can feel its\x01",
            "history somehow.\x02",
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
        "#12P#00005F...Umm, Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F...Ah, n-no.\x02\x03",
            "#00204FIt's so pretty, I was at\x01",
            "a loss for words...\x02",
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
            "#00205F...What is it? You're\x01",
            "staring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No... I was just thinking it's\x01",
            "unexpected.\x02\x03",
            "#00003FI've thought this before, but I\x01",
            "can't believe you show an interest\x01",
            "in these kinds of worldly things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FE-Even I sometimes\x01",
            "honestly think these kinds\x01",
            "of things are pretty.\x02\x03",
            "#00204FWell, in a way, I came to\x01",
            "like them because of you\x01",
            "and the others, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FAh...\x02\x03",
            "#00004F(That's right... If you think about\x01",
            "it, Tio is around the age where\x01",
            "girls like this stuff, right?)\x02\x03",
            "(Around when we first me, I got the\x01",
            "impression she was already grown-\x01",
            "up, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F...Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, nevermind.\x02\x03",
            "#00004F(That's right. It's not\x01",
            "the case that I'm trying\x01",
            "to win her over, but...)\x02\x03",
            "(It might be nice to\x01",
            "give Tio some kind of\x01",
            "present.)\x02\x03",
            "#00000F(Something that she\x01",
            "would like...)\x02",
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
            "#5P#00000F(This sapphirl hair\x01",
            "ornament... It would\x01",
            "look great on Tio.)\x02\x03",
            "#00003F(And the price... 10,000\x01",
            "mira, huh. It's quite a\x01",
            "bit, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_529E")
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
            "Purchase the hair ornament\x01",      # 0
            "Refuse\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5142")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FTio, how would you like\x01",
            "that hair ornament for a\x01",
            "present?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        "#00205FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha. Obviously I can't\x01",
            "buy you a necklace like\x01",
            "that one, but...\x02\x03",
            "#00000FI thought you might like\x01",
            "something girly and\x01",
            "stylish.\x02\x03",
            "There is no special\x01",
            "meaning in it, of course,\x01",
            "but... What do you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204FI'm happy.\x02\x03",
            "#00200FHowever, can I say just\x01",
            "one thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F"There is no special\x01",
            "meaning in it, of\x01",
            "course"...\x02\x03",
            "#00211FIn a way, isn't it rude\x01",
            "to say that to a woman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FUm, ah, I guess you're right?\x02\x03",
            "#00002FI was thinking you could\x01",
            "accept it as an brother's\x01",
            "present to his sister, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...*sigh*.\x02\x03",
            "#00211FWell, let's leave that\x01",
            "as a point of compromise\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00003FU-Umm... Why aren't you\x01",
            "convinced?\x02\x03",
            "#00012FWould a Mishy item have\x01",
            "been better than a hair\x01",
            "ornament?\x02",
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
            "#00202FOh, right. Please let me\x01",
            "buy a present for you\x01",
            "too, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, since we're here...\x02\x03",
            "#00204FThen, please wait a\x01",
            "moment. I'll find\x01",
            "something good for you.\x02",
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
            "Afterwards, Lloyd and Tio had the\x01",
            "jewelry they each bought wrapped by the\x01",
            "clerk and exchanged them as presents.\x07\x00\x02",
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
    Jump("loc_5299")

    label("loc_5142")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(...I really shouldn't.\x01",
            "It could spell\x01",
            "trouble...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F...Lloyd, why don't we\x01",
            "have a look over there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FY-Yeah, got it. I'll\x01",
            "keep you company until\x01",
            "you're satisfied.\x02",
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

    label("loc_5299")

    Jump("loc_544D")

    label("loc_529E")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Wait, I don't have enough mira for\x01",
            "this in the first place. It's a pity,\x01",
            "but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00202F...Lloyd, why don't we\x01",
            "have a look over there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00012FY-Yeah, got it. I'll\x01",
            "keep you company until\x01",
            "you're satisfied.\x02",
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

    label("loc_544D")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4387 end

    def Function_30_545D(): pass

    label("Function_30_545D")

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
        (
            "#12P#00000FWe've arrived at the\x01",
            "jewelry store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright then, I'll keep\x01",
            "you company while you\x01",
            "look for your present.\x02\x03",
            "#00309FSo, who's your target?\x01",
            "You can tell your bro,\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No, no. It's not like\x01",
            "that.\x02\x03",
            "#00000FIn any case, we have\x01",
            "some time, so let's have\x01",
            "a look around the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FSure, got it.\x02",
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
            "#12P#00001FHow can I say this...\x02\x03",
            "#00006FThe more I look around, the more\x01",
            "I feel like it's a store two men\x01",
            "shouldn't enter alone at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHey now, what about me who came\x01",
            "in alone in broad daylight,\x01",
            "then?\x02\x03",
            "#00300FWell, I agree with you, though.\x01",
            "Might as well go to the theme\x01",
            "park and hit on some girls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FL-Like I told you, we\x01",
            "don't have the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBy the way, wasn't that\x01",
            "the original plan when we\x01",
            "talked on the water bus?\x02\x03",
            "#00301FUnbelievable, you're one\x01",
            "of those herbivores...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00302FAlright, since we're here,\x01",
            "I'll buy you an accessory to\x01",
            "increase your handsomeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh... A-Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, I just saw something in\x01",
            "the display window over there\x01",
            "that would look good on you.\x02\x03",
            "#00309FHaha, it's just for fun so\x01",
            "there's no need to be\x01",
            "nervous.\x02\x03",
            "#00304FOf course it doesn't have any\x01",
            "particular meaning.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, no... It would be a\x01",
            "problem if it did have\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, I'm jokin'.\x02\x03",
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
            "#11P#00309FAnd while I'm there, I'll get an\x01",
            "appointment with those lovely ladies\x01",
            "over there for later tonight!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 2, 0, 27)
    BeginChrThread(0x104, 3, 0, 26)

    def lambda_5B95():

        label("loc_5B95")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5B95")

    QueueWorkItem2(0x101, 2, lambda_5B95)
    WaitChrThread(0x104, 3)
    EndChrThread(0x104, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    def lambda_5BB7():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5BB7)
    TurnDirection(0xD, 0x104, 500)
    EndChrThread(0x101, 0xFF)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha, oh man...\x02\x03",
            "#00004F(However, we're all helped by\x01",
            "his caring attitude.)\x02\x03",
            "(I'd like to express my thanks\x01",
            "to him as the Support Section\x01",
            "leader...)\x02\x03",
            "#00000F(We're in a jewelry store after\x01",
            "all, I guess I'll boldly look\x01",
            "for something for him, too.)\x02",
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
            "#5P#00000F(This carnelia-studded\x01",
            "bracelet... It would\x01",
            "look good on Randy.)\x02\x03",
            "#00003F(And the price... 10,000\x01",
            "mira, huh. It's quite a\x01",
            "bit, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6103")
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
            "Purchase the bracelet\x01",      # 0
            "Refuse\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F96")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FUhm, excuse me. I would\x01",
            "like this bracelet...\x02",
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
            "Afterwards, Lloyd joked with Randy\x01",
            "to console him for having failed to\x01",
            "hit on the girls...\x02\x03",
            "Lloyd and Randy had the jewelry they\x01",
            "each bought wrapped by the clerk and\x01",
            "exchanged them as presents.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_60FE")

    label("loc_5F96")


    ChrTalk(
        0x101,
        (
            "#5P#00006F(...It's awkward, so I think I'll\x01",
            "pass on it.)\x02\x03",
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
            "Afterwards, Lloyd joked with\x01",
            "Randy to console him for having\x01",
            "failed to hit on the girls...\x02\x03",
            "After receiving the jewelry\x01",
            "from Randy, they left the\x01",
            "jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_60FE")

    Jump("loc_6274")

    label("loc_6103")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006F(...Wait, I don't have\x01",
            "that much mira in the\x01",
            "first place.)\x02\x03",
            "#00008F(It's too bad, but I'll\x01",
            "have to give up the idea\x01",
            "of giving this to him...)\x02",
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
            "Afterwards, Lloyd joked with\x01",
            "Randy to console him for having\x01",
            "failed to hit on the girls...\x02\x03",
            "After receiving the jewelry\x01",
            "from Randy, they left the\x01",
            "jewelry shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6274")

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

    # Function_30_545D end

    def Function_31_62BB(): pass

    label("Function_31_62BB")

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
            "#10108FHmm. I looked around\x01",
            "this place with Fran\x01",
            "earlier today, but...\x02\x03",
            "#10106F*sigh*, I really feel\x01",
            "out of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FWe wouldn't have been able to\x01",
            "come in in the first place\x01",
            "without Mariabell's influence.\x02\x03",
            "#00000FWell we're here. Want to look\x01",
            "around with me this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, allow me to keep\x01",
            "you company!\x02",
        )
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
        "#5P#10103FHmm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00005FIs something wrong,\x01",
            "Noｱl?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10101FNo, I've just been thinking\x01",
            "about this ever since I\x01",
            "looked in here earlier...\x02\x03",
            "#10106FIsn't there a lot of\x01",
            "pointless jewelry?\x02\x03",
            "#10108FThey're hard to move in and\x01",
            "get in the way of work...\x02",
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
            "#6P#10111FAh, I-I'm sorry! You\x01",
            "were enjoying looking at\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha. Well, it's a point\x01",
            "of view I'd expect from\x01",
            "you, Noｱl.\x02\x03",
            "#00000FNow that I think about\x01",
            "it, your civilian clothes\x01",
            "look easy to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FAhaha... I pick them putting\x01",
            "a lot of importance on that\x01",
            "point.\x02\x03",
            "#10106FIf I choose them alone, they\x01",
            "tend to turn out very mannish\x01",
            "and that's a problem.\x02\x03",
            "#10100FThat's why I always ask Fran\x01",
            "to help me coordinate them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I see.\x02\x03",
            "#00000FThen, is there something\x01",
            "you'd like in this\x01",
            "store?\x02",
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
            "#5P#10102FAh, amberl-studded\x01",
            "choker...\x02\x03",
            "#10109FWhen I saw it this morning\x01",
            "with Fran, I thought it\x01",
            "was somehow nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed, it'll\x01",
            "suit you, Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(That's right, we came here\x01",
            "together, so it might make\x01",
            "a nice present for her.)\x02\x03",
            "#00003F(And the price... 10,000\x01",
            "mira, huh. It's quite a\x01",
            "bit, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_70CF")
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
            "Purchase the choker\x01",      # 0
            "Refuse\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F16")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FNoｱl, this choker... Can\x01",
            "I give it to you as a\x01",
            "present?\x02",
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
            "#00004FYou're doing your best with your\x01",
            "assignment to the Support Section... It's\x01",
            "to express my appreciation for that, and\x01",
            "doesn't have a special meaning, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10111FU-Umm... No, but!! I'm\x01",
            "happy I'm happy,\x01",
            "but...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is there some kind of\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F...N-no!! That's not\x01",
            "it...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#6P#10101F...B-But! Seeing as how\x01",
            "you proposed it, I\x01",
            "humbly accept!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha. You don't have to\x01",
            "be so humble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FN-No... Really, thank\x01",
            "you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10103FOh, right, in that\x01",
            "case...\x02\x03",
            "#10100FWould you accept a\x01",
            "present from me too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, since we're here.\x02\x03",
            "#10100FPlease wait a moment.\x01",
            "I'll find something nice\x01",
            "for you.\x02",
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
            "Afterwards, Lloyd and Noｱl had the\x01",
            "jewelry they each bought wrapped by the\x01",
            "clerk and exchanged them as presents.\x07\x00\x02",
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
    Jump("loc_70CA")

    label("loc_6F16")


    ChrTalk(
        0x101,
        (
            "#00006F(...Hmm, as I thought, I'll pass.\x01",
            "It could create a misunderstanding\x01",
            "with Fran and the others...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10105FMr. Lloyd, is something\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAh, no, it's nothing.\x02\x03",
            "#00000FLet's see if there's any\x01",
            "other things that could\x01",
            "be interesting.\x02",
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

    label("loc_70CA")

    Jump("loc_72A5")

    label("loc_70CF")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, I don't have enough mira for\x01",
            "this in the first place. It's a pity,\x01",
            "but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10105FMr. Lloyd, is something\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAh, no, it's nothing.\x02\x03",
            "#00000FLet's see if there's any\x01",
            "other things that could\x01",
            "be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FYes, let's!\x02",
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

    label("loc_72A5")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_62BB end

    def Function_32_72B5(): pass

    label("Function_32_72B5")

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
        (
            "#12P#00000FWell, we're here at the\x01",
            "jewelry store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThere's some time until\x01",
            "the dinner party... Want\x01",
            "to have a look together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah, since we're\x01",
            "already here, that might\x01",
            "be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, it's decided then.\x01",
            "Then, let's take a look\x01",
            "around.\x02",
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
            "#00003FUmm, it's a members only\x01",
            "store, so they have only\x01",
            "high-priced articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe. Since we're here, a\x01",
            "ring or something to give\x01",
            "to KeA later might be nice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00006FHey, that's not something to\x01",
            "give a kid.\x02\x03",
            "#00005FBy the way, Wazy, you've been\x01",
            "pretty popular since before\x01",
            "you joined the SSS, right?\x02\x03",
            "#00003FIt looks like you also had a\x01",
            "tactical orbment as well when\x01",
            "we met...\x02\x03",
            "#00000FI hear it quite often, but\x01",
            "are host clubs are really\x01",
            "that profitable?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FNo? After all it's only a side job.\x01",
            "Because I only help every now and\x01",
            "them, my pay is not all that much.\x02\x03",
            "#10304FAt the club, if I have to say,\x01",
            "there're many other sources of\x01",
            "income than your pay.\x02\x03",
            "#10302FEvery now and then, you can receive\x01",
            "jewels as pocket mira from the\x01",
            "wealthy mesdames.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI-I see. I can't really agree\x01",
            "with that, but I can at least see\x01",
            "where your mira comes from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHehe, no, no. I don't exchange\x01",
            "what I receive from the\x01",
            "customers for mira, you know?\x02\x03",
            "#10304FAnd I bought the ENIGMA I had\x01",
            "before from Ashley's shop with\x01",
            "my own mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005FThen in the end, where's\x01",
            "that mira coming from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10309FHehe, trade secret.\x02",
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
            "#6P#10304FHehe. Well, leaving\x01",
            "those trivial things\x01",
            "aside...\x02\x03",
            "#10302FLloyd, if you like,\x01",
            "could you accept this?\x02",
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
        "#00005FTh-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FI found it in the\x01",
            "showcase over there just\x01",
            "now.\x02\x03",
            "#10304FI thought it would look\x01",
            "good on you, and since\x01",
            "we're here, I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-When did you...?\x02\x03",
            "#00005FBut, is it really okay\x01",
            "for me to have something\x01",
            "so expensive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe. I bought it on a\x01",
            "whim, so no need to\x01",
            "think too hard about it.\x02\x03",
            "#10309FIt's cheap stuff if I\x01",
            "can buy your gratitude\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FH-Hey now...\x02\x03",
            "#00000FBut, well, thanks. Thank\x01",
            "you, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHehe, you're welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F(...Right, just getting this wouldn't be...)\x02\x03",
            "#00004F(It might be nice to give him something in\x01",
            "return.)\x02\x03",
            "#00000F(Thanks to Wazy joining, the flexibility of\x01",
            "the Support Section has increased, in way...\x01",
            "This would be a way to thank him for that.)\x02",
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
            "#00000F(This goldia pendant\x01",
            "might look good on\x01",
            "Wazy.)\x02\x03",
            "#00003F(And the price... 10,000\x01",
            "mira, huh. It's quite a\x01",
            "bit, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_82B7")
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
            "Purchase the pendant\x01",      # 0
            "Refuse\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8128")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FThen, could you accept\x01",
            "this pendant as a return\x01",
            "gift?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x2D, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10305FWow, you sure?\x02\x03",
            "#10300FHehe, your fashion sense\x01",
            "isn't too bad.\x02\x03",
            "#10302FIt's cheap for a gift,\x01",
            "but, well, I guess you\x01",
            "pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now... If you don't\x01",
            "want it, I won't buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha, perish the\x01",
            "thought.\x02\x03",
            "#10302FYou worked hard picking\x01",
            "it out for me. I'll\x01",
            "humbly accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, well it's fine.\x01",
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
            "Afterwards, Lloyd and Wazy had the\x01",
            "jewelry they each bought wrapped by the\x01",
            "clerk and exchanged them as presents.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_82B2")

    label("loc_8128")


    ChrTalk(
        0x101,
        (
            "#00006F(I guess I'll pass on it\x01",
            "this time. I'll make up\x01",
            "for it some other time.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, something wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's nothing.\x02\x03",
            "#00000FThere's some time until\x01",
            "dinner, so let's have a\x01",
            "look inside the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHehe, roger.\x02",
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
            "and then left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_82B2")

    Jump("loc_8482")

    label("loc_82B7")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, I don't have enough mira for\x01",
            "this in the first place. It's a pity,\x01",
            "but I can only give up on this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, something wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's nothing.\x02\x03",
            "#00000FThere's some time until\x01",
            "dinner, so let's have a\x01",
            "look inside the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHehe, roger.\x02",
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
            "and then left the jewelry store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8482")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_72B5 end

    SaveToFile()

Try(main)
