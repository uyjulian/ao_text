from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "Chalk",                  # 1
        "Wendy",                  # 2
        "Fernando",               # 3
        "Misette",                # 4
        "Basilio",                # 5
        "Haas",                   # 6
        "Citizen",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Reins",                  # 10
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24500.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch28100.itc",                   # 09
        "chr/ch26000.itc",                   # 0A
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(9329,    0,       4294965946, 270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294965777, 0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294962816, 0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294965777, 0,       14659,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(11319,   4000,    8640,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(11470,   4000,    4294965576, 90,   385,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(11300,   4000,    4294965126, 90,   385,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294962617, 0,       4294965476, 90,   389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       4294965936, 1000,    9330,    1500,    4294965946, 0x007E, 0,  8,  0x0000)

    ChipFrameInfo(652, 0)                                        # 0

    ScpFunction((
        "Function_0_28C",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_495",          # 02, 2
        "Function_3_677",          # 03, 3
        "Function_4_6C3",          # 04, 4
        "Function_5_A19",          # 05, 5
        "Function_6_2657",         # 06, 6
        "Function_7_2E70",         # 07, 7
        "Function_8_398E",         # 08, 8
        "Function_9_3998",         # 09, 9
        "Function_10_3E36",        # 0A, 10
        "Function_11_5AB4",        # 0B, 11
        "Function_12_6962",        # 0C, 12
        "Function_13_6B82",        # 0D, 13
        "Function_14_7E78",        # 0E, 14
        "Function_15_8A74",        # 0F, 15
        "Function_16_964E",        # 10, 16
        "Function_17_97F1",        # 11, 17
        "Function_18_9C91",        # 12, 18
        "Function_19_9FC4",        # 13, 19
        "Function_20_A10A",        # 14, 20
        "Function_21_A249",        # 15, 21
        "Function_22_B03E",        # 16, 22
        "Function_23_B9FF",        # 17, 23
        "Function_24_D250",        # 18, 24
        "Function_25_DD25",        # 19, 25
        "Function_26_E2E3",        # 1A, 26
    ))


    def Function_0_28C(): pass

    label("Function_0_28C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2CC"),
        (1, "loc_2D8"),
        (2, "loc_2E4"),
        (3, "loc_2F0"),
        (4, "loc_2FC"),
        (5, "loc_308"),
        (6, "loc_314"),
        (SWITCH_DEFAULT, "loc_320"),
    )


    label("loc_2CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_308")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_314")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_343")

    Return()

    # Function_0_28C end

    def Function_1_344(): pass

    label("Function_1_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_494")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_344")

    label("loc_494")

    Return()

    # Function_1_344 end

    def Function_2_495(): pass

    label("Function_2_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B9")
    SetChrPos(0xC, 7140, 0, 3340, 90)
    SetChrFlags(0xA, 0x80)
    Jump("loc_649")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 7390, 0, -250, 270)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_649")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_649")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_503")
    Jump("loc_649")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_516")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_53C")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54F")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_588")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AC")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E4")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF")
    SetChrFlags(0x11, 0x10)

    label("loc_5DF")

    Jump("loc_649")

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_619")
    SetChrPos(0xC, 11470, 4000, 8119, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2040, 0, 12670, 0)
    Jump("loc_649")

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_649")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11470, 4000, 8119, 90)

    label("loc_649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_676")

    Return()

    # Function_2_495 end

    def Function_3_677(): pass

    label("Function_3_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6AB")
    Sound(128, 1, 50, 0)

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_6C2")

    Return()

    # Function_3_677 end

    def Function_4_6C3(): pass

    label("Function_4_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E3")
    SetScenarioFlags(0x0, 0)
    TalkBegin(0x8)
    Call(0, 12)
    TalkEnd(0x8)
    Return()

    label("loc_6E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")

    ChrTalk(
        0x8,
        (
            "Welcooome☆ This is the\x01",
            "purchasing counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, you're all\x01",
            "acquaintances of Wendy,\x01",
            "am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. We've received\x01",
            "some new Enigma covers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, once you've bought\x01",
            "them, we'll exchange them for you\x01",
            "whenever you like at this counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please work Chalk hard\x01",
            "non-stop!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 4)

    label("loc_81D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8EE")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                       # 0
            "Buy/Change Covers\x01",          # 1
            "Buy Master Quartz\x01",          # 2
            "Buy Orbal Car Options\x01",      # 3
            "Cancel\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E9")

    Jump("loc_969")

    label("loc_8EE")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Buy/Change Covers\x01",      # 1
            "Buy Master Quartz\x01",      # 2
            "Cancel\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_969")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_969")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98A")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A10")

    label("loc_98A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AE")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A10")

    label("loc_9AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D2")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A10")

    label("loc_9D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A10")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_9F4")
    OP_AF(0xC0)
    Jump("loc_A06")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A04")
    OP_AF(0xBF)
    Jump("loc_A06")

    label("loc_A04")

    OP_AF(0xBE)

    label("loc_A06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A10")

    Jump("loc_827")

    label("loc_A15")

    TalkEnd(0x8)
    Return()

    # Function_4_6C3 end

    def Function_5_A19(): pass

    label("Function_5_A19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2656")
    MenuCmd(0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "Which will you switch\x01",
            "to?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B42")
    MenuCmd(1, 0, "CPD (Lloyd)         Equipped")
    Jump("loc_B63")

    label("loc_B42")

    MenuCmd(1, 0, "CPD (Lloyd)         Change To")

    label("loc_B63")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_BA5")
    MenuCmd(1, 0, "Blue Sheriff        Equipped")
    Jump("loc_BF5")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_BD4")
    MenuCmd(1, 0, "Blue Sheriff        Change To")
    Jump("loc_BF5")

    label("loc_BD4")

    MenuCmd(1, 0, "Blue Sheriff        1000 mira")

    label("loc_BF5")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_C2D")
    MenuCmd(1, 0, "Howling Wolf        Equipped")
    Jump("loc_C7D")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_C5C")
    MenuCmd(1, 0, "Howling Wolf        Change To")
    Jump("loc_C7D")

    label("loc_C5C")

    MenuCmd(1, 0, "Howling Wolf        1000 mira")

    label("loc_C7D")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D2C")

    label("loc_D0E")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D70")
    MenuCmd(1, 0, "CPD (Elie)          Equipped")
    Jump("loc_D91")

    label("loc_D70")

    MenuCmd(1, 0, "CPD (Elie)          Change To")

    label("loc_D91")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_DD3")
    MenuCmd(1, 0, "Peace Green         Equipped")
    Jump("loc_E23")

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_E02")
    MenuCmd(1, 0, "Peace Green         Change To")
    Jump("loc_E23")

    label("loc_E02")

    MenuCmd(1, 0, "Peace Green         1000 mira")

    label("loc_E23")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_E5B")
    MenuCmd(1, 0, "Spring Bird         Equipped")
    Jump("loc_EAB")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_E8A")
    MenuCmd(1, 0, "Spring Bird         Change To")
    Jump("loc_EAB")

    label("loc_E8A")

    MenuCmd(1, 0, "Spring Bird         1000 mira")

    label("loc_EAB")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F3C")

    label("loc_F1E")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1110")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F80")
    MenuCmd(1, 0, "CPD (Tio)           Equipped")
    Jump("loc_FA1")

    label("loc_F80")

    MenuCmd(1, 0, "CPD (Tio)           Change To")

    label("loc_FA1")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_FE3")
    MenuCmd(1, 0, "Black Cat           Equipped")
    Jump("loc_1033")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_1012")
    MenuCmd(1, 0, "Black Cat           Change To")
    Jump("loc_1033")

    label("loc_1012")

    MenuCmd(1, 0, "Black Cat           1000 mira")

    label("loc_1033")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_106B")
    MenuCmd(1, 0, "Shadow Circle       Equipped")
    Jump("loc_10BB")

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_109A")
    MenuCmd(1, 0, "Shadow Circle       Change To")
    Jump("loc_10BB")

    label("loc_109A")

    MenuCmd(1, 0, "Shadow Circle       1000 mira")

    label("loc_10BB")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_112E")

    label("loc_1110")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_112E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1172")
    MenuCmd(1, 0, "CPD (Randy)         Equipped")
    Jump("loc_1193")

    label("loc_1172")

    MenuCmd(1, 0, "CPD (Randy)         Change To")

    label("loc_1193")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_11D5")
    MenuCmd(1, 0, "Danger Orange       Equipped")
    Jump("loc_1225")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_1204")
    MenuCmd(1, 0, "Danger Orange       Change To")
    Jump("loc_1225")

    label("loc_1204")

    MenuCmd(1, 0, "Danger Orange       1000 mira")

    label("loc_1225")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_125D")
    MenuCmd(1, 0, "Midnight Kiss       Equipped")
    Jump("loc_12AD")

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_128C")
    MenuCmd(1, 0, "Midnight Kiss       Change To")
    Jump("loc_12AD")

    label("loc_128C")

    MenuCmd(1, 0, "Midnight Kiss       1000 mira")

    label("loc_12AD")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1302")

    label("loc_12E4")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1302")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_140D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1341")
    MenuCmd(1, 0, "CGF (Noｱl)          Equipped")
    Jump("loc_1362")

    label("loc_1341")

    MenuCmd(1, 0, "CGF (Noｱl)          Change To")

    label("loc_1362")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_139A")
    MenuCmd(1, 0, "Liberty Road        Equipped")
    Jump("loc_13EA")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_13C9")
    MenuCmd(1, 0, "Liberty Road        Change To")
    Jump("loc_13EA")

    label("loc_13C9")

    MenuCmd(1, 0, "Liberty Road        1000 mira")

    label("loc_13EA")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1421")

    label("loc_140D")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1421")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1518")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1460")
    MenuCmd(1, 0, "White Creed         Equipped")
    Jump("loc_1481")

    label("loc_1460")

    MenuCmd(1, 0, "White Creed         Change To")

    label("loc_1481")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_14B9")
    MenuCmd(1, 0, "Crest Face          Equipped")
    Jump("loc_1509")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_14E8")
    MenuCmd(1, 0, "Crest Face          Change To")
    Jump("loc_1509")

    label("loc_14E8")

    MenuCmd(1, 0, "Crest Face          1000 mira")

    label("loc_1509")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_152C")

    label("loc_1518")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_152C")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155F")
    Sleep(1)
    Return()

    label("loc_155F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_193A")

    label("loc_159D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DB")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_193A")

    label("loc_15DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1619")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_193A")

    label("loc_1619")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1657")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_193A")

    label("loc_1657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1695")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_193A")

    label("loc_1695")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D3")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_193A")

    label("loc_16D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1711")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_193A")

    label("loc_1711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_193A")

    label("loc_174F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_193A")

    label("loc_178D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CB")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_193A")

    label("loc_17CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1809")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_193A")

    label("loc_1809")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1847")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_193A")

    label("loc_1847")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1885")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_193A")

    label("loc_1885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C3")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_193A")

    label("loc_18C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1901")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_193A")

    label("loc_1901")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_193A")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_193A")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A07")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Lloyd only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AA5")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Elie only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B42")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Tio only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1B42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE1")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Randy only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1BE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C77")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Noｱl only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1C77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D08")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Wazy only. You can\x01",
            "change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D08")


    AnonymousTalk(
        0x8,
        (
            "There you go. Is this\x01",
            "okay~?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exchange Covers]\x01",      # 0
            "[Cancel]\x01",               # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2639")
    ClearScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DC8")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE1")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1DE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DFA")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E19")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E32")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4B")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6A")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E83")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBB")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED4")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1EED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F07")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1F07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F20")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1F20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3A")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F4E")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F4E")
    SetScenarioFlags(0x1, 1)

    label("loc_1F4E")

    ClearScenarioFlags(0x1, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F66")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1F66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F7F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F98")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1F98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAD")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC6")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1FC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FDF")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1FDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF4")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_1FF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200D")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_200D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2026")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_2026")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203B")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_203B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2054")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_2054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206D")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_206D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2082")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_2082")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209B")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_209B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B0")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20C4")

    label("loc_20B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C4")
    SetScenarioFlags(0x1, 2)

    label("loc_20C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_211E")

    ChrTalk(
        0x8,
        (
            "Whaaat, you already have\x01",
            "it equipped? Please\x01",
            "choose another one, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262A")

    label("loc_211E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2175")

    ChrTalk(
        0x8,
        (
            "Whaaat, you're short on\x01",
            "mira? You can't exchange\x01",
            "it then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262A")

    label("loc_2175")


    ChrTalk(
        0x8,
        (
            "Roger! Please wait a\x01",
            "moment~㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Here, sorry to keep you\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2282")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2245")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_227D")

    label("loc_2245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225F")
    SetScenarioFlags(0x2C, 0)

    label("loc_225F")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_227D")

    label("loc_226A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2277")
    SetScenarioFlags(0x2C, 1)

    label("loc_2277")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_227D")

    Jump("loc_256B")

    label("loc_2282")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2330")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E1")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_232B")

    label("loc_22E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2304")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2304")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_232B")

    label("loc_230F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2325")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2325")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_232B")

    Jump("loc_256B")

    label("loc_2330")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23DD")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238E")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_23D8")

    label("loc_238E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B1")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23B1")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_23D8")

    label("loc_23BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D2")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23D2")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_23D8")

    Jump("loc_256B")

    label("loc_23DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_248C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243D")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_2487")

    label("loc_243D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_246B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2460")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2460")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_2487")

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2481")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2481")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_2487")

    Jump("loc_256B")

    label("loc_248C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24FE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E0")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_24F9")

    label("loc_24E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F6")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_24F6")

    SetScenarioFlags(0x2F, 0)

    label("loc_24F9")

    Jump("loc_256B")

    label("loc_24FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_256B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2552")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_256B")

    label("loc_2552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2568")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2568")

    SetScenarioFlags(0x2E, 4)

    label("loc_256B")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25E2")
    OP_E0(0x16, 0x0)

    label("loc_25E2")


    ChrTalk(
        0x8,
        (
            "Haha. I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262A")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_262A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2643")

    label("loc_2639")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2643")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_A23")

    label("loc_2656")

    Return()

    # Function_5_A19 end

    def Function_6_2657(): pass

    label("Function_6_2657")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2661")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6F")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x4)"), scpexpr(EXPR_END)), "loc_26A4")
    MenuCmd(1, 0, "Platinum        Purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_26C1")

    label("loc_26A4")

    MenuCmd(1, 0, "Platinum        1000 mira")

    label("loc_26C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x4)"), scpexpr(EXPR_END)), "loc_26F2")
    MenuCmd(1, 0, "Mirage          Purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_270F")

    label("loc_26F2")

    MenuCmd(1, 0, "Mirage          5000 mira")

    label("loc_270F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27B9")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x4)"), scpexpr(EXPR_END)), "loc_274E")
    MenuCmd(1, 0, "Aegis           Purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_276B")

    label("loc_274E")

    MenuCmd(1, 0, "Aegis          20000 mira")

    label("loc_276B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x4)"), scpexpr(EXPR_END)), "loc_279C")
    MenuCmd(1, 0, "Scepter         Purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_27B9")

    label("loc_279C")

    MenuCmd(1, 0, "Scepter        50000 mira")

    label("loc_27B9")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2815")
    Sleep(1)
    Return()

    label("loc_2815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2855")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_2910")

    label("loc_2855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2895")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_2910")

    label("loc_2895")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D5")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_2910")

    label("loc_28D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2910")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_2910")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AC")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Space element Master Quartz.\x01",
            "※Raises HP/ADF, recovers HP\x01",
            "on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF0")

    label("loc_29AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mirage element Master Quartz.\x01",
            "※Raises EP/ATS, recovers EP\x01",
            "on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF0")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A8D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Earth element Master Quartz.\x01",
            "※Raises DEF/ADF, gain MAX\x01",
            "GUARD in certain conditions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF0")

    label("loc_2A8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF0")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water element Master Quartz.\x01",
            "※Raises STR/ATS, gain Sepith\x01",
            "when attacking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF0")


    AnonymousTalk(
        0x8,
        (
            "There you go. Is this\x01",
            "okay~?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Buy]\x01",         # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E52")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C13")

    ChrTalk(
        0x8,
        (
            "Whaaat, you're short of\x01",
            "mira? You can't buy it,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2C13")


    ChrTalk(
        0x8,
        (
            "Roger! Please wait a\x01",
            "moment~㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Here, sorry to keep you\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE1")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2E0E")

    label("loc_2CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D47")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE1, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2E0E")

    label("loc_2D47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAD")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2E0E")

    label("loc_2DAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE6, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2E0E")


    ChrTalk(
        0x8,
        (
            "Haha. I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2E43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E5C")

    label("loc_2E52")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E5C")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_2661")

    label("loc_2E6F")

    Return()

    # Function_6_2657 end

    def Function_7_2E70(): pass

    label("Function_7_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F00")

    ChrTalk(
        0x8,
        (
            "Papa's been staring this\x01",
            "whole time. He's gonna burn\x01",
            "a hole right through me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, I'm glad he's this\x01",
            "worried about me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_2F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2FE7")

    ChrTalk(
        0x8,
        (
            "When martial law was\x01",
            "declared, the shop manager\x01",
            "told me to go home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wendy said she'd stay\x01",
            "behind to help if needed,\x01",
            "so I decided to stay too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My dad won't like it,\x01",
            "but I'm sure he'll\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_2FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3068")

    ChrTalk(
        0x8,
        (
            "President Dieter's\x01",
            "speech... That was\x01",
            "impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I unconsciously stopped\x01",
            "breathing in the middle\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_30FD")

    ChrTalk(
        0x8,
        (
            "This past week, my father\x01",
            "has been following me to\x01",
            "work and taking me home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a relief to have\x01",
            "money in times like\x01",
            "these.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_30FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_316F")

    ChrTalk(
        0x8,
        (
            "I'm really worried about\x01",
            "the people of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why did something like\x01",
            "this have to happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_316F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324C")

    ChrTalk(
        0x8,
        (
            "I didn't realize my dad\x01",
            "came to interview for a\x01",
            "position at our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He doesn't have any\x01",
            "engineering skills, so of\x01",
            "course he was rejected, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, that was so\x01",
            "embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32B2")

    label("loc_324C")


    ChrTalk(
        0x8,
        (
            "I heard my dad\x01",
            "interviewed for a\x01",
            "position at our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ooh, I just want to hide\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B2")

    Jump("loc_398D")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32ED")

    ChrTalk(
        0x8,
        (
            "A train derailment...\x01",
            "How awful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_32ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3373")

    ChrTalk(
        0x8,
        (
            "My dad seems nervous for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't explain it, but...\x01",
            "I'm getting a really bad\x01",
            "feeling about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33D6")

    ChrTalk(
        0x8,
        (
            "I understand why my\x01",
            "dad's worried about me,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anyway, it's excessive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_33D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_341E")

    ChrTalk(
        0x8,
        (
            "To be scolded by a\x01",
            "customer... I can't\x01",
            "believe this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_341E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_34BF")

    ChrTalk(
        0x8,
        (
            "It's about time to close\x01",
            "up shop for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Looks like my dad came by the\x01",
            "shop as usual, but... Anyway,\x01",
            "I want him to go home already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_34BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_355D")

    ChrTalk(
        0x8,
        (
            "Wendy is always borrowing\x01",
            "the orbal camera I use\x01",
            "for our demo unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wanted to take a photo\x01",
            "of Princess Klaudia and\x01",
            "Archduke Albert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398D")

    label("loc_355D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FC")

    ChrTalk(
        0x8,
        "Welcome, everyone☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've started selling\x01",
            "orbal car option\x01",
            "packages and car paint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, consider\x01",
            "purchasing them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 1)
    Jump("loc_372C")

    label("loc_35FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B8")

    ChrTalk(
        0x8,
        (
            "But, my dad never gets\x01",
            "tired of it, day after\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He won't stop no matter\x01",
            "what I say, so I've been\x01",
            "ignoring him lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I shouldn't to spoil him\x01",
            "so much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_372C")

    label("loc_36B8")


    ChrTalk(
        0x8,
        (
            "He'll come even if I tell\x01",
            "him not to, so I've been\x01",
            "ignoring him lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I shouldn't to spoil him\x01",
            "so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372C")

    Jump("loc_398D")

    label("loc_3731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3877")

    ChrTalk(
        0x8,
        (
            "The manager's attitude\x01",
            "towards Wendy has clearly\x01",
            "changed recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before, he addressed her without an\x01",
            "honorific, but he suddenly started\x01",
            "attaching "-kun" to her name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After that, he started\x01",
            "using honorific language\x01",
            "with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She was confused at\x01",
            "first, but she's used to\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_38F9")

    label("loc_3877")


    ChrTalk(
        0x8,
        (
            "The manager's attitude\x01",
            "towards Wendy has clearly\x01",
            "changed recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She was confused at\x01",
            "first, but she's used to\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F9")

    Jump("loc_398D")

    label("loc_38FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_398D")

    ChrTalk(
        0x8,
        (
            "At this counter we sell and\x01",
            "change orbment covers, and we\x01",
            "sell master quartz here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please work Chalk hard\x01",
            "non-stop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398D")

    Return()

    # Function_7_2E70 end

    def Function_8_398E(): pass

    label("Function_8_398E")

    OP_C9(0x1, 0x80)
    Call(0, 9)
    Return()

    # Function_8_398E end

    def Function_9_3998(): pass

    label("Function_9_3998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C6")
    Call(0, 25)
    Return()

    label("loc_39C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B64")
    TalkBegin(0x9)

    ChrTalk(
        0x9,
        "Hey there, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What's up? You've got\x01",
            "such a cute little boy\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we're showing this\x01",
            "boy we know around town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So he's not from around\x01",
            "here, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Hey you, this kind of\x01",
            "store's not all that\x01",
            "common, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Relax, take your time,\x01",
            "and give it plenty of\x01",
            "love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "S-Sure... (Love?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DD, 0)
    TalkEnd(0x9)
    Jump("loc_3BE2")

    label("loc_3B64")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "Giving tours of the city\x01",
            "sure looks fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, but even so, you\x01",
            "guys do a lot of different\x01",
            "things, don't you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3BE2")

    Return()

    label("loc_3BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C12")
    Call(0, 21)
    Return()

    label("loc_3C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C69")
    Call(0, 22)
    Jump("loc_3CE2")

    label("loc_3C69")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "First off, will each of\x01",
            "you set a master quartz\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Speak to me after that,\x01",
            "and we'll go from there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3CE2")

    Return()

    label("loc_3CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D09")
    Call(0, 23)
    Return()

    label("loc_3D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D29")
    SetScenarioFlags(0x0, 1)
    TalkBegin(0x9)
    Call(0, 12)
    TalkEnd(0x9)
    Return()

    label("loc_3D29")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E32")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Questions?\x01",             # 2
            "Cancel\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_3E2D")

    label("loc_3DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DE0")
    OP_AF(0xD)
    Jump("loc_3E02")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DF0")
    OP_AF(0xC)
    Jump("loc_3E02")

    label("loc_3DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E00")
    OP_AF(0xB)
    Jump("loc_3E02")

    label("loc_3E00")

    OP_AF(0xA)

    label("loc_3E02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E2D")

    label("loc_3E11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3E2D")

    Jump("loc_3D36")

    label("loc_3E32")

    TalkEnd(0x9)
    Return()

    # Function_9_3998 end

    def Function_10_3E36(): pass

    label("Function_10_3E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4164")

    ChrTalk(
        0x9,
        (
            "Lloyd and everyone― Nice\x01",
            "work breaking through the\x01",
            "President's blockade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And Lloyd. I think things will\x01",
            "be tough from here on out, so\x01",
            "let's do our best, together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, let's.\x02\x03",
            "#00000FAnd the same to you Wendy. Even\x01",
            "with all that's happened, you're\x01",
            "here continuing your work.\x02\x03",
            "We'll be relying on you to\x01",
            "maintain our orbments for a long\x01",
            "time to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But anyway, it's really\x01",
            "no big deal, so please\x01",
            "take these.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FA, 3)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThanks Wendy. This is a\x01",
            "big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, you're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, if you're going\x01",
            "anywhere dangerous, be\x01",
            "careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once things have calmed\x01",
            "down, let's have a meal with\x01",
            "Oscar, just the three of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, let's.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 6)
    Jump("loc_420F")

    label("loc_4164")


    ChrTalk(
        0x9,
        (
            "I think things will be tough\x01",
            "from here on out, so let's\x01",
            "do our best, together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once things have calmed\x01",
            "down, let's have a meal with\x01",
            "Oscar, just the three of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420F")

    Jump("loc_5AB3")

    label("loc_4214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_42D9")

    ChrTalk(
        0x9,
        (
            "I heard you were all right,\x01",
            "but... It's really a relief\x01",
            "to see your face like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you need to use the workshop,\x01",
            "just say the word. I'll do my\x01",
            "very best to support you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_42D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CF")

    ChrTalk(
        0x9,
        (
            "I didn't think things\x01",
            "would unfold this\x01",
            "fast...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, it looks like\x01",
            "things are gonna be\x01",
            "tough from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, if you ever need\x01",
            "to use the workshop,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4482")

    label("loc_43CF")


    ChrTalk(
        0x9,
        (
            "I didn't think things would unfold\x01",
            "this fast, but... Anyway, things are\x01",
            "gonna be tough from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, if you ever need\x01",
            "to use the workshop,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4482")

    Jump("loc_5AB3")

    label("loc_4487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4556")

    ChrTalk(
        0x9,
        (
            "Though the city reconstruction\x01",
            "is mostly complete, I just knew\x01",
            "Downtown would be left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After work today, I'll head\x01",
            "to Master Guillaume's place\x01",
            "to see how I can help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FC")

    label("loc_4556")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4633")

    ChrTalk(
        0x9,
        (
            "The pageant, huh?\x01",
            "...Man, what an\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's my childhood\x01",
            "friend asking, I'll take\x01",
            "you up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have work to do until the\x01",
            "program starts, so call me\x01",
            "when you need me, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FC")

    label("loc_4633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4776")

    ChrTalk(
        0x9,
        (
            "Nice work guys. I just\x01",
            "got back from the event\x01",
            "hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...But even so, that\x01",
            "Roy's emceeing was quite\x01",
            "rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In my introduction, he made it\x01",
            "sound like I'm always smacking\x01",
            "customers with my spanner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Does Roy really think\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FH-Hmm, I wonder. (I\x01",
            "can't deny it totally,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_47FC")

    label("loc_4776")


    ChrTalk(
        0x9,
        (
            "But, it was a lot more fun\x01",
            "than I thought it'd be.\x01",
            "Thanks for inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I just got back, so I've\x01",
            "gotta get back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FC")

    Jump("loc_5AB3")

    label("loc_4801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_494C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48DF")

    ChrTalk(
        0x9,
        (
            "It seems an unbelievable\x01",
            "thing happened in\x01",
            "Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you're going there,\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you need ENIGMA Ⅱ\x01",
            "maintenance, all you\x01",
            "gotta do is ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4947")

    label("loc_48DF")


    ChrTalk(
        0x9,
        (
            "It seems an unbelievable\x01",
            "thing happened in\x01",
            "Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you're going there,\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4947")

    Jump("loc_5AB3")

    label("loc_494C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49D9")

    ChrTalk(
        0x9,
        (
            "Chalk's dad is a\x01",
            "hardcore worrywart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think he means well, but I\x01",
            "wish he'd consider Chalk's\x01",
            "feelings a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_49D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4A44")

    ChrTalk(
        0x9,
        (
            "I hear an orbal train\x01",
            "has derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Could they have run into\x01",
            "some machine trouble?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_4A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB8")

    ChrTalk(
        0x9,
        (
            "To think the manager would remodel the\x01",
            "store to be reminiscent of the old\x01",
            "workshop out of respect for his workers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The store's finally doing well and we\x01",
            "have more regular customers too... Doing\x01",
            "that would only confuse the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm glad the manager respects\x01",
            "all that we do, but I wish he'd\x01",
            "think of another way to show it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C7D")

    label("loc_4BB8")


    ChrTalk(
        0x9,
        (
            "Changing the store's appearance\x01",
            "at this late date is going to\x01",
            "confuse all of the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm glad the manager respects\x01",
            "all that we do, but I wish he'd\x01",
            "think of another way to show it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C7D")

    Jump("loc_5AB3")

    label("loc_4C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD1")

    ChrTalk(
        0x9,
        (
            "Independence, eh? I was surprised when I first\x01",
            "heard about it, but I was even more surprised\x01",
            "to learn of the mayor's support for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's talk that the major powers\x01",
            "are going to station troops at our\x01",
            "border gates before long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we desire true peace,\x01",
            "we may need to raise our\x01",
            "voices now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E9E")

    label("loc_4DD1")


    ChrTalk(
        0x9,
        (
            "Independence, eh? I was surprised when I first\x01",
            "heard about it, but I was even more surprised\x01",
            "to learn of the mayor's support for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we desire true peace,\x01",
            "we may need to raise our\x01",
            "voices now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E9E")

    Jump("loc_5AB3")

    label("loc_4EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F44")

    ChrTalk(
        0x9,
        (
            "Hmm, Chalk's dad is\x01",
            "really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I think nothing but bad\x01",
            "things about people who hit on\x01",
            "employees right at opening time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_4F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_510B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509C")

    ChrTalk(
        0x9,
        (
            "Ah, it's you guys.\x01",
            "You're not usually\x01",
            "around at this hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we got an\x01",
            "emergency investigation\x01",
            "request.\x02\x03",
            "Can we shop here now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, we're normally open\x01",
            "until 8.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, good then. I'll count\x01",
            "on you for help with our\x01",
            "orbment maintenance then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yep, roger that. Just\x01",
            "say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5106")

    label("loc_509C")


    ChrTalk(
        0x9,
        (
            "If you need help with\x01",
            "your ENIGMA Ⅱs, just say\x01",
            "the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll have it done for\x01",
            "you in a jiffy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5106")

    Jump("loc_5AB3")

    label("loc_510B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E8")

    ChrTalk(
        0x9,
        (
            "Hahaha, the Arseille. Though it\x01",
            "was from far away, I was able to\x01",
            "capture it on our orbal camera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I had it developed\x01",
            "immediately. You guys\x01",
            "want a copy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FWow, let me have a look\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00106FLet's see, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThis is really the\x01",
            "Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FI can just barely make\x01",
            "out its silhouette.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh? Take a good look,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the bow and this\x01",
            "is the stern. You should\x01",
            "be able to see it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, now that you\x01",
            "mention it, I guess\x01",
            "you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's your love for mecha, I\x01",
            "guess... That's a different\x01",
            "side of you than I usually see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh, really? I think\x01",
            "it's how I usually am,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHahaha... (For now, it's\x01",
            "certain that it's not\x01",
            "how she usually is.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 4)
    Jump("loc_558B")

    label("loc_54E8")


    ChrTalk(
        0x9,
        (
            "Though it was from a distance,\x01",
            "I was able to capture the form\x01",
            "of the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahaha. I think I'll have\x01",
            "it enlarged and hang it\x01",
            "on the wall in my room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_558B")

    Jump("loc_5AB3")

    label("loc_5590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_588F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D2")

    ChrTalk(
        0x9,
        (
            "The trade conference, huh? I\x01",
            "bet the Liberl representative\x01",
            "came in on that Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe Arseille... Oh, it's\x01",
            "Liberl's high-speed\x01",
            "cruiser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Exactly! It's got all of ZCF's latest\x01",
            "tech. It's a true masterpiece. The\x01",
            "airship of airships!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's something that flies\x01",
            "through the sky, I've got to\x01",
            "stop working and take a photo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's not like I don't\x01",
            "understand how you feel, but...\x01",
            "Everything in moderation, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmmm, nope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FHey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, that's Wendy for\x01",
            "you. A fine,\x01",
            "straightforward answer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 3)
    Jump("loc_588A")

    label("loc_57D2")


    ChrTalk(
        0x9,
        (
            "The trade conference, huh? I\x01",
            "bet the Liberl representative\x01",
            "came in on that Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's something that flies\x01",
            "through the sky, I've got to\x01",
            "stop working and take a photo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588A")

    Jump("loc_5AB3")

    label("loc_588F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5920")

    ChrTalk(
        0x9,
        (
            "Our manager works harder\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He was originally a designer,\x01",
            "I guess? He has quite the\x01",
            "appetite for knowledge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A14")

    ChrTalk(
        0x9,
        (
            "Anyway, just one battle with\x01",
            "master quartz set is fine, so\x01",
            "finish it for me, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't forget to come\x01",
            "report to me after\x01",
            "you're done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can't complete the\x01",
            "training if you don't,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB3")

    label("loc_5A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5AB3")

    ChrTalk(
        0x9,
        (
            "Haha, take very good care\x01",
            "of your master quartz\x01",
            "from here on out, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The more you love them,\x01",
            "the more they'll love\x01",
            "you back, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB3")

    Return()

    # Function_10_3E36 end

    def Function_11_5AB4(): pass

    label("Function_11_5AB4")


    ChrTalk(
        0x9,
        (
            "Okay. What do you want\x01",
            "to ask about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6954")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "About Tactical Orbments\x01",        # 0
            "About Quartz\x01",                   # 1
            "About Opening Slots\x01",            # 2
            "About Strengthening Slots\x01",      # 3
            "About Orbal Magic (Arts)\x01",       # 4
            "About the ENIGMA Ⅱ\x01",            # 5
            "About Master Quartz\x01",            # 6
            "Cancel\x01",                         # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BCF")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_5BCF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5C03"),
        (1, "loc_5DE8"),
        (2, "loc_5F4C"),
        (3, "loc_60A5"),
        (4, "loc_6236"),
        (5, "loc_64A2"),
        (6, "loc_6691"),
        (SWITCH_DEFAULT, "loc_6940"),
    )


    label("loc_5C03")


    ChrTalk(
        0x9,
        (
            "Tactical Orbments are small,\x01",
            "portable orbal devices\x01",
            "specialized for use in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In addition to strengthening\x01",
            "the user, they support the\x01",
            "user with the use of arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're usually simply\x01",
            "called "orbments".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orbments are completely aligned and\x01",
            "optimized for the individual, so the\x01",
            "structure varies depending on the user.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are slots with attribute limits, and\x01",
            "the shape of the connecting lines differs. It\x01",
            "might be good to compare them at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_5DE8")


    ChrTalk(
        0x9,
        (
            "Quartz are "crystal circuits"\x01",
            "for use in orbments made by\x01",
            "smelting sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you bring me the\x01",
            "required sepith, we can\x01",
            "synthesize the quartz here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Depending on the quartz, there are various\x01",
            "effects, and when the property values are over\x01",
            "a fixed number, arts become able to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once you've gathered\x01",
            "some sepith, give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_5F4C")


    ChrTalk(
        0x9,
        (
            "Orbment slots are, from\x01",
            "the start, sealed for\x01",
            "the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to set a\x01",
            "quartz, you first need\x01",
            "an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you open a slot, the number\x01",
            "of quartz you can use increases,\x01",
            "as well as your maximum EP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though you need sepith to open slots,\x01",
            "it'll be pretty useful for you. I think\x01",
            "you should proactively open them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_60A5")


    ChrTalk(
        0x9,
        (
            "Among quartz, some are\x01",
            "designated "high-rank\x01",
            "quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're too strong, so\x01",
            "you can't set them in\x01",
            "normal slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What you need to do is\x01",
            "strengthen the slot\x01",
            "itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You need sepith to do that,\x01",
            "and your maximum EP increases,\x01",
            "the same as with sealed slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't think you should rush to strengthen\x01",
            "them, but it is an indispensable component\x01",
            "of powering up your orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_6236")


    ChrTalk(
        0x9,
        (
            "Magic invoked using\x01",
            "tactical orbments. In other\x01",
            "words, orbal arts, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're often referred\x01",
            "to simply as "arts."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The kinds of arts that can be invoked are\x01",
            "decided by the sum total of the attribute\x01",
            "values of the quartz on each line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, the higher the attribute\x01",
            "values of the quartz you have set, the\x01",
            "more arts you'll be able to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, if you want to use high-\x01",
            "level arts, you'll need to pay attention\x01",
            "to the attribute value combinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "All the detailed information regarding that\x01",
            "is in a list in your detective notebook, so\x01",
            "refer to it whenever you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_64A2")


    ChrTalk(
        0x9,
        (
            "Inheriting the ENIGMA's communication\x01",
            "function, the successor model has been\x01",
            "boldly remodeled― That's the "ENIGMA Ⅱ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Far and away the biggest change from\x01",
            "the previous model is compatibility\x01",
            "with special "Master Quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though it's mostly the same...\x01",
            "The new version's basic\x01",
            "architecture has changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of compatibility problems,\x01",
            "you can't set quartz that could be\x01",
            "used with the old ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And so, you need new\x01",
            "standard quartz for use\x01",
            "with the ENIGMA Ⅱ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_6691")


    ChrTalk(
        0x9,
        (
            "Master quartz are special\x01",
            "quartz that are inserted in\x01",
            "the center of your ENIGMA Ⅱs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A definite difference from\x01",
            "your usual quartz is that the\x01",
            "master quartz itself "grows".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By accumulating battles with\x01",
            "them set, they will level up and\x01",
            "exhibit more powerful effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Strengthening the user, the quartz's special\x01",
            "effect and the attribute values... Those three\x01",
            "components are affected by the quartz's growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, to discover the true\x01",
            "powers of each master quartz, it seems\x01",
            "you need to bring them to max level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though it seems to take\x01",
            "a long time to level\x01",
            "them up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It might be important to not\x01",
            "mess around and continue to\x01",
            "use your favorites.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694F")

    label("loc_6940")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_694F")

    label("loc_694F")

    Jump("loc_5AE8")

    label("loc_6954")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_5AB4 end

    def Function_12_6962(): pass

    label("Function_12_6962")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    def lambda_6973():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6973)

    def lambda_6980():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6980)
    TurnDirection(0xA, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_69CD")

    ChrTalk(
        0x8,
        "Ah, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lloyd... You're safe!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A32")

    label("loc_69CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_69F6")

    ChrTalk(
        0x9,
        "Lloyd... You're safe!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A32")

    label("loc_69F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6A32")

    ChrTalk(
        0xA,
        "Oh, you all are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lloyd... You're safe!\x02",
    )

    CloseMessageWindow()

    label("loc_6A32")


    ChrTalk(
        0x101,
        "#00000FYeah... somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I got the rundown from\x01",
            "the other officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys are gonna do\x01",
            "something about the situation,\x01",
            "aren't you. That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Umm, ahh, we'll support\x01",
            "you as much as we can\x01",
            "with our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, be careful out\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright, and thanks.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1BB, 5)
    Return()

    # Function_12_6962 end

    def Function_13_6B82(): pass

    label("Function_13_6B82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B93")
    Jump("loc_7E74")

    label("loc_6B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB1")
    SetScenarioFlags(0x0, 3)
    Call(0, 12)
    Jump("loc_6C1D")

    label("loc_6BB1")


    ChrTalk(
        0xFE,
        (
            "But this situation...\x01",
            "It's like pure chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what's going to\x01",
            "happen to our Crossbell\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C1D")

    Jump("loc_7E74")

    label("loc_6C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2F")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of\x01",
            "Crossbell"... It will make us enemies\x01",
            "of the major powers for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The natural result is that products\x01",
            "from Reinford Corporation and Verne Co.\x01",
            "will no longer be sold in our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahh, my head hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DD1")

    label("loc_6D2F")


    ChrTalk(
        0xFE,
        (
            "I don't believe this. Asserting\x01",
            "our independence by halting\x01",
            "economic activity is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's going to be like\x01",
            "this, I can't agree with\x01",
            "our independence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD1")

    Jump("loc_7E74")

    label("loc_6DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6E8E")

    ChrTalk(
        0xFE,
        (
            "The independence\x01",
            "referendum will be held\x01",
            "in just three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that day, we plan to take turns\x01",
            "watching the store, so that each\x01",
            "employee has a chance to vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E74")

    label("loc_6E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F51")

    ChrTalk(
        0xFE,
        (
            "Hmm. That occupation\x01",
            "incident has turned into\x01",
            "an unusual situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say the Empire\x01",
            "might be behind it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope it's\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6FB0")

    label("loc_6F51")


    ChrTalk(
        0xFE,
        (
            "They say the Empire\x01",
            "might be behind it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope it's\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FB0")

    Jump("loc_7E74")

    label("loc_6FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_716F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B8")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Chalk's\x01",
            "father came for an\x01",
            "interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Worried about his daughter,\x01",
            "he asked me to let him work\x01",
            "for us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad. He didn't fulfill our\x01",
            "minimum requirements for\x01",
            "employment, so I had to reject him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_716A")

    label("loc_70B8")


    ChrTalk(
        0xFE,
        (
            "Worried about his daughter,\x01",
            "he asked me to let him work\x01",
            "for us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad. He didn't fulfill our\x01",
            "minimum requirements for\x01",
            "employment, so I had to reject him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_716A")

    Jump("loc_7E74")

    label("loc_716F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_71DC")

    ChrTalk(
        0xFE,
        (
            "I heard it from a\x01",
            "customer. They said a\x01",
            "train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope everyone's all\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E74")

    label("loc_71DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_735F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C7")

    ChrTalk(
        0xFE,
        (
            "I tried asking Wendy and\x01",
            "Chalk their opinions about\x01",
            "remodeling the store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They dismissed the idea\x01",
            "before I even finished\x01",
            "explaining it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I don't think it's\x01",
            "that bad an idea,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_735A")

    label("loc_72C7")


    ChrTalk(
        0xFE,
        (
            "Hmm, I don't think it's\x01",
            "that bad an idea,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if those two are that\x01",
            "opposed to it, I suppose I'll\x01",
            "have to give up on the idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735A")

    Jump("loc_7E74")

    label("loc_735F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B6")

    ChrTalk(
        0xFE,
        (
            "Guillaume once worked here, but we had a\x01",
            "difference of opinion regarding management\x01",
            "policies and decided to part ways, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking about it now, I\x01",
            "might have done\x01",
            "something bad to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I'm late in realizing it, after\x01",
            "all is said and done, this business\x01",
            "only exists because of my employees.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7561")

    label("loc_74B6")


    ChrTalk(
        0xFE,
        (
            "Come to think of it, Wendy\x01",
            "said she likes the atmosphere\x01",
            "of the old workshop, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, a little\x01",
            "remodeling of the old Genten\x01",
            "workshop might be good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7561")

    Jump("loc_7E74")

    label("loc_7566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7662")

    ChrTalk(
        0xFE,
        (
            "So today is the trade\x01",
            "conference's main\x01",
            "session, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an important conference that will determine the future\x01",
            "of not just Crossbell's economy, but that of the whole\x01",
            "continent. So of course I'm concerned about the results.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E74")

    label("loc_7662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_76EF")

    ChrTalk(
        0xFE,
        (
            "Good evening, and\x01",
            "welcome to Genten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still some time until\x01",
            "closing, so please take your\x01",
            "time and don't rush.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E74")

    label("loc_76EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_780E")

    ChrTalk(
        0xFE,
        (
            "*sigh*, that Wendy is a\x01",
            "troublesome one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think she'd abandon her\x01",
            "work and rush out of the\x01",
            "store with an orbal camera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I complained about it\x01",
            "before, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no real obstacle to our\x01",
            "business though. I guess\x01",
            "this much could be cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_78B3")

    label("loc_780E")


    ChrTalk(
        0xFE,
        (
            "If I think that using a demo\x01",
            "camera could be a way to advertise\x01",
            "its functions, I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll have her\x01",
            "show me the photos she\x01",
            "took later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B3")

    Jump("loc_7E74")

    label("loc_78B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E2")

    ChrTalk(
        0xFE,
        (
            "Can I help you with\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for an orbal\x01",
            "vacuum, allow me to recommend this\x01",
            "one, Verne Co.'s latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its three changeable heads mean you'll be able\x01",
            "to clean any surface. It is an extraordinary\x01",
            "machine, the height of convenience.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7ACE")

    label("loc_79E2")


    ChrTalk(
        0xFE,
        (
            "If you are looking for an orbal\x01",
            "vacuum, allow me to recommend this\x01",
            "one, Verne Co.'s latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its three changeable heads mean you'll be able\x01",
            "to clean any surface. It is an extraordinary\x01",
            "machine, the height of convenience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ACE")

    Jump("loc_7E74")

    label("loc_7AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C56")

    ChrTalk(
        0xFE,
        (
            "It pains me to say it, but I\x01",
            "don't have enough information\x01",
            "regarding orbal devices at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Realizing this might cause the\x01",
            "store to go off track, I've\x01",
            "started to study them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, that Wendy of ours\x01",
            "is one amazing orbal\x01",
            "engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried to learn some of her technical\x01",
            "knowledge, but it's very complicated\x01",
            "and I don't get it at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7CD7")

    label("loc_7C56")


    ChrTalk(
        0xFE,
        (
            "Haha, that Wendy of ours\x01",
            "is one amazing orbal\x01",
            "engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all I can do to\x01",
            "memorize even the most\x01",
            "basic information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CD7")

    Jump("loc_7E74")

    label("loc_7CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DCD")

    ChrTalk(
        0xFE,
        (
            "Hello, and welcome to\x01",
            "Orbal Store Genten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally, our store has all the\x01",
            "latest orbal goods, and we offer\x01",
            "outstanding, local after-sale service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need any advice,\x01",
            "please feel free to ask\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7E74")

    label("loc_7DCD")


    ChrTalk(
        0xFE,
        (
            "Naturally, our store has all the\x01",
            "latest orbal goods, and we offer\x01",
            "outstanding, local after-sale service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need any advice,\x01",
            "please feel free to ask\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E74")

    TalkEnd(0xFE)
    Return()

    # Function_13_6B82 end

    def Function_14_7E78(): pass

    label("Function_14_7E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F49")

    ChrTalk(
        0xFE,
        (
            "To be honest, I don't really feel\x01",
            "like shopping, but... I can't calm\x01",
            "down at home, so I came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I want everything\x01",
            "to resolve quickly so I can\x01",
            "get my everyday life back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_7F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7F57")
    Jump("loc_8A70")

    label("loc_7F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7FFB")

    ChrTalk(
        0xFE,
        (
            "President Dieter's\x01",
            "address was impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems things will be tough\x01",
            "from now on, but I feel I must do\x01",
            "my best, together with everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_7FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_80D8")

    ChrTalk(
        0xFE,
        (
            "I am normally disinterested in\x01",
            "politics, however the question of\x01",
            "independence is a different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The more I think about recent\x01",
            "incidents in Crossbell, the more\x01",
            "I think we should be independent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_80D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8145")

    ChrTalk(
        0xFE,
        (
            "An occupation\x01",
            "incident... How scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope something can be\x01",
            "done about it, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_8145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_82FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8238")

    ChrTalk(
        0xFE,
        (
            "If we become independent, we won't\x01",
            "have to pay a portion of our taxes\x01",
            "to either of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given that, Crossbell's\x01",
            "economy will grow even\x01",
            "faster than it already is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that's\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_82FA")

    label("loc_8238")


    ChrTalk(
        0xFE,
        (
            "If we become independent, we\x01",
            "won't have to pay taxes to\x01",
            "either of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given that, Crossbell's economy will\x01",
            "grow even faster than it already is.\x01",
            "I think that's important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82FA")

    Jump("loc_8A70")

    label("loc_82FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8330")

    ChrTalk(
        0xFE,
        (
            "My, it sure is noisy\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_8330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_84D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8435")

    ChrTalk(
        0xFE,
        (
            "It seems Reinford Company\x01",
            "sells many high-capacity,\x01",
            "high-output goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the contrary, Verne Co. sells\x01",
            "many reasonably priced goods\x01",
            "with many different functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, this must reflect\x01",
            "the character of each\x01",
            "nation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_84D2")

    label("loc_8435")


    ChrTalk(
        0xFE,
        (
            "Reinford focuses on high capacity\x01",
            "and output, and Verne focuses on\x01",
            "convenience and economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, this must reflect\x01",
            "the character of each\x01",
            "nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D2")

    Jump("loc_8A70")

    label("loc_84D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8584")

    ChrTalk(
        0xFE,
        (
            "I just learned this. It\x01",
            "seems ZCF makes the most\x01",
            "reliable devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their goods are fairly\x01",
            "expensive compared to others,\x01",
            "but it seems that's not all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_8584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_862E")

    ChrTalk(
        0xFE,
        (
            "Though at first glance they seem\x01",
            "the same, the manufacturer gives\x01",
            "each device a unique personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. I am coming to\x01",
            "understand that myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_862E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_871E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86AB")

    ChrTalk(
        0xFE,
        (
            "My, it's already this\x01",
            "late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I've got to get\x01",
            "home and cook on my new\x01",
            "orbal range.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8719")

    label("loc_86AB")


    ChrTalk(
        0xFE,
        (
            "Orbal ranges are really\x01",
            "convenient, aren't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're very expensive,\x01",
            "but I'm glad I bought\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8719")

    Jump("loc_8A70")

    label("loc_871E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87DD")

    ChrTalk(
        0xFE,
        (
            "The trade conference? Hmm.\x01",
            "I'm not directly involved,\x01",
            "so I'm not interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But more importantly, look\x01",
            "at this. This new product,\x01",
            "isn't it just so cute?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_883E")

    label("loc_87DD")


    ChrTalk(
        0xFE,
        (
            "If you think of these\x01",
            "screws like eyes, it looks\x01",
            "kind of like a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, how cute.\x02",
    )

    CloseMessageWindow()

    label("loc_883E")

    Jump("loc_8A70")

    label("loc_8843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8927")

    ChrTalk(
        0xFE,
        (
            "The manager here has gotten better\x01",
            "informed about his products over\x01",
            "the past few months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's a little annoying getting\x01",
            "a product explanation without asking\x01",
            "for it... I can sense his enthusiasm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_8927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_89B5")

    ChrTalk(
        0xFE,
        (
            "Orbal goods are just so\x01",
            "fascinating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm not planning on\x01",
            "buying anything, I find\x01",
            "myself coming to this store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A70")

    label("loc_89B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8A70")

    ChrTalk(
        0xFE,
        (
            "Well look at that. The next\x01",
            "generation of the vacuum cleaner\x01",
            "I bought is on sale already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww. If they had said\x01",
            "something sooner, I wouldn't\x01",
            "have bought one back then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A70")

    TalkEnd(0xFE)
    Return()

    # Function_14_7E78 end

    def Function_15_8A74(): pass

    label("Function_15_8A74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8AED")

    ChrTalk(
        0xFE,
        (
            "Oh, Chalk... My\x01",
            "daughter, Chalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your father has been so\x01",
            "worried about you this\x01",
            "whole time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8AFB")
    Jump("loc_964A")

    label("loc_8AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8BB8")

    ChrTalk(
        0xFE,
        (
            "Though they call themselves the\x01",
            ""State Guard"... I worry about\x01",
            "whether they can really protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But it's all right.\x01",
            "I'll protect Chalk no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8C4D")

    ChrTalk(
        0xFE,
        (
            "Chalk forgave me, so we\x01",
            "came here together this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No one can replace you,\x01",
            "Chalk. Your father will\x01",
            "always protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8CEC")

    ChrTalk(
        0xFE,
        (
            "To think an armed group\x01",
            "occupied Mainz... What a\x01",
            "disturbing story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, no matter what\x01",
            "anyone says, I'm walking\x01",
            "Chalk home today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8D7F")

    ChrTalk(
        0xFE,
        (
            "Hmm, even the manager is\x01",
            "unreasonable, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. In that case,\x01",
            "I'll come as a customer, as I\x01",
            "have up until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8DD5")

    ChrTalk(
        0xFE,
        (
            "A derailment, huh?\x01",
            "They've happened before\x01",
            "but they're quite rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8E39")

    ChrTalk(
        0xFE,
        (
            "Today, I've decided to\x01",
            "interview for a position at\x01",
            "this store. I'm so nervous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_8E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5C")

    ChrTalk(
        0xFE,
        (
            "No matter what my\x01",
            "daughter says, I'll worry\x01",
            "about worrisome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think I'll work\x01",
            "here as an orbal\x01",
            "engineer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, at the end of the\x01",
            "day, I'm a planner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can do simple maintenance\x01",
            "all right, but... Will the\x01",
            "manager end up hiring me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8FAF")

    label("loc_8F5C")


    ChrTalk(
        0xFE,
        (
            "Hmm. At the end of the day,\x01",
            "I'm a planner. Will the\x01",
            "manager end up hiring me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FAF")

    Jump("loc_964A")

    label("loc_8FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_903E")

    ChrTalk(
        0xFE,
        (
            "Yesterday when some guys\x01",
            "got close to Chalk after\x01",
            "work I warned them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I did that, Chalk\x01",
            "got very mad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_903E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_917C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9119")

    ChrTalk(
        0xFE,
        (
            "There's still some time\x01",
            "until closing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The roads at night are\x01",
            "dangerous, so I really want\x01",
            "to walk Chalk home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I did that, Chalk\x01",
            "would hate me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, what to do...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9177")

    label("loc_9119")


    ChrTalk(
        0xFE,
        (
            "It'll look suspicious if\x01",
            "I secretly follow her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll go home for\x01",
            "the day...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9177")

    Jump("loc_964A")

    label("loc_917C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_924D")

    ChrTalk(
        0xFE,
        (
            "So Wendy is Chalk's superior, huh. That\x01",
            "girl heard the sound of an airship\x01",
            "engine and rushed out of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, she didn't\x01",
            "return for a little while.\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_924D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_92CC")

    ChrTalk(
        0xFE,
        (
            "Hmm, though she's my\x01",
            "daughter, Chalk is quite\x01",
            "the beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I worry that\x01",
            "undesirables will\x01",
            "approach her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964A")

    label("loc_92CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_94A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_940D")

    ChrTalk(
        0xFE,
        (
            "The appearance of various\x01",
            "orbal goods reveals the values\x01",
            "of their makers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unnecessary ornamentation is useless.\x01",
            "ZCF and the Epstein Foundation excel\x01",
            "on the point of functional beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Reinford Company\x01",
            "goes for a flashy appearance\x01",
            "and Verne Co. goes for "pop".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_949D")

    label("loc_940D")


    ChrTalk(
        0xFE,
        (
            "Orbal goods have no need\x01",
            "of useless ornamentation,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get angry when I think\x01",
            "I've paid extra for\x01",
            "worthless decorations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_949D")

    Jump("loc_964A")

    label("loc_94A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_964A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95B4")

    ChrTalk(
        0xFE,
        (
            "Until last year, I\x01",
            "worked as an orbal goods\x01",
            "designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter secured a job and my\x01",
            "family's finances are in order,\x01",
            "so I boldly decided to retire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't dislike working, but\x01",
            "above all, I want to spend\x01",
            "more time with my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_964A")

    label("loc_95B4")


    ChrTalk(
        0xFE,
        (
            "And so today, I came to\x01",
            "see my daughter's\x01",
            "workplace, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it's seems she's doing\x01",
            "her best as usual. As her\x01",
            "father, I'm proud of her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_964A")

    TalkEnd(0xFE)
    Return()

    # Function_15_8A74 end

    def Function_16_964E(): pass

    label("Function_16_964E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9727")

    ChrTalk(
        0xFE,
        (
            "Orbal cars and terminals are\x01",
            "fine, but they're out of reach\x01",
            "of most people, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems prices are steadily falling,\x01",
            "but... I wonder if they'll ever be in\x01",
            "range of ordinary families.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97ED")

    label("loc_9727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_97ED")

    ChrTalk(
        0xFE,
        (
            "Wah! It's the rumored notebook-\x01",
            "type orbal terminal! Now let's\x01",
            "check the price tag...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wow, that's a huge number of\x01",
            "zeroes. There's no way I could\x01",
            "ever buy something like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97ED")

    TalkEnd(0xFE)
    Return()

    # Function_16_964E end

    def Function_17_97F1(): pass

    label("Function_17_97F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A7")

    ChrTalk(
        0xFE,
        (
            "I didn't want to forget\x01",
            "Chalk so I came here\x01",
            "again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That father of hers\x01",
            "is still here, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I give up. I'm\x01",
            "going home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9902")

    label("loc_98A7")


    ChrTalk(
        0xFE,
        (
            "...So that father of\x01",
            "hers is still here, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I give up. I'm\x01",
            "going home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9902")

    Jump("loc_9C8D")

    label("loc_9907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_99E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9990")

    ChrTalk(
        0xFE,
        (
            "It's almost closing time,\x01",
            "huh. There's still a lot\x01",
            "of customers, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Should I talk to her?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_99E2")

    label("loc_9990")


    ChrTalk(
        0xFE,
        (
            "I'll muster my courage,\x01",
            "and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I've got to calm\x01",
            "down and think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99E2")

    Jump("loc_9C8D")

    label("loc_99E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AE7")

    ChrTalk(
        0xFE,
        (
            "I'm not planning on buying\x01",
            "anything but... I keep coming here\x01",
            "to see the sales girl's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, I checked\x01",
            "her name tag, and it\x01",
            "seems her name is Chalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She has an innocent\x01",
            "appearance, and a very\x01",
            "cute name!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9B4A")

    label("loc_9AE7")


    ChrTalk(
        0xFE,
        (
            "I don't care about the\x01",
            "unveiling ceremony!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just seeing that girl\x01",
            "smile is enough for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B4A")

    Jump("loc_9C8D")

    label("loc_9B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C20")

    ChrTalk(
        0xFE,
        (
            "Hmm, this store is\x01",
            "really amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not their orbal devices,\x01",
            "but their employees!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Muhuhu, that engineer girl is\x01",
            "cute too, but the sales\x01",
            "counter girl is more my type.㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9C8D")

    label("loc_9C20")


    ChrTalk(
        0xFE,
        (
            "Hmm, I guess this is an\x01",
            "unexpected reward for my\x01",
            "trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll let\x01",
            "me take her picture?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C8D")

    TalkEnd(0xFE)
    Return()

    # Function_17_97F1 end

    def Function_18_9C91(): pass

    label("Function_18_9C91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9D26")

    ChrTalk(
        0xFE,
        (
            "Hmm, an unsettling\x01",
            "incident has occurred\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They cut the trip's\x01",
            "schedule short, so I'll\x01",
            "be going home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC0")

    label("loc_9D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9DE2")

    ChrTalk(
        0xFE,
        (
            "It seems the orbal train damaged\x01",
            "in yesterday's accident has been\x01",
            "fully repaired as of this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. It seems the CGF\x01",
            "are very good at dealing\x01",
            "with accidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC0")

    label("loc_9DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9E46")

    ChrTalk(
        0xFE,
        (
            "Hmm, that sound just now\x01",
            "was a siren. I hope I don't\x01",
            "hear them too often, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC0")

    label("loc_9E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EFE")

    ChrTalk(
        0xFE,
        (
            "Man, these orbal goods\x01",
            "are just beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though the functions are the same, the\x01",
            "shapes are different depending on the\x01",
            "manufacturer. That's quite interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC0")

    label("loc_9EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9FC0")

    ChrTalk(
        0xFE,
        (
            "Hmm, this store has a good\x01",
            "balance of orbal goods from\x01",
            "different manufacturers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's Crossbell for you. They\x01",
            "don't call this the continent's\x01",
            "leading trade city for nothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC0")

    TalkEnd(0xFE)
    Return()

    # Function_18_9C91 end

    def Function_19_9FC4(): pass

    label("Function_19_9FC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0A1")

    ChrTalk(
        0xFE,
        "Just what is going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, if I went home, I\x01",
            "wouldn't have anything to eat, so\x01",
            "it's better to stay here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I have nothing\x01",
            "to do, so I guess I'll\x01",
            "service the air pump.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A106")

    label("loc_A0A1")


    ChrTalk(
        0xFE,
        "Just what is going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have nothing to do for\x01",
            "now, so I guess I'll\x01",
            "service the air pump.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A106")

    TalkEnd(0xFE)
    Return()

    # Function_19_9FC4 end

    def Function_20_A10A(): pass

    label("Function_20_A10A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1A8")

    ChrTalk(
        0xFE,
        (
            "Photo quartz, photo\x01",
            "quartz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's not that many of the\x01",
            "latest model. Will I be able to\x01",
            "get by with just two or three?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_A245")

    label("loc_A1A8")


    ChrTalk(
        0xFE,
        (
            "I came to buy photo quartz in\x01",
            "preparation for tomorrow's\x01",
            "unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as luck would have\x01",
            "it, they're sold out,\x01",
            "and it's a huge problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A245")

    TalkEnd(0xFE)
    Return()

    # Function_20_A10A end

    def Function_21_A249(): pass

    label("Function_21_A249")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#11POh Lloyd, there you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd the rest of you\x01",
            "too... Wait, I don't two\x01",
            "of you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, these members just\x01",
            "started with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FHow do you do. I'm Noｱl\x01",
            "Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWazy Hemisphere. It's a\x01",
            "pleasure.\x02\x03",
            "#10300FHey, don't you and Lloyd\x01",
            "go way back?\x02\x03",
            "Ooh, finally we can get\x01",
            "some juicy details about\x01",
            "Lloyd's childhood.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11POh, yeah I have plenty of those!\x01",
            "I'll bet you're looking for\x01",
            "something you can use against him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FOh come on Wendy, knock\x01",
            "it off already.\x02\x03",
            "#00000FAnyway, can we get back\x01",
            "on topic now please?\x02\x03",
            "Weren't you going to\x01",
            "train us on these ENIGMA\x01",
            "Ⅱs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh yeah! I totally\x01",
            "forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PAhem, well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAs I'm sure you're all\x01",
            "aware, you're now using the\x01",
            "brand-new Enigma Ⅱ model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's the latest version of\x01",
            "the technology released by\x01",
            "the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe main difference is\x01",
            "the center slot in the\x01",
            "middle of the unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe quartz that is used\x01",
            "in this slot is called a\x01",
            "Master Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRight, they're quartz\x01",
            "with a pattern engraved\x01",
            "on them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThose are them. They're\x01",
            "big and spherical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA master quartz's main\x01",
            "difference from a normal\x01",
            "one is called "growth".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy fighting battles with one set\x01",
            "in your orbment, it will gain\x01",
            "experience and grow in power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FWoah, that feels kind of\x01",
            "surreal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYeah, it's as if the\x01",
            "Master Quartz is\x01",
            "actually alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHehe, I'm assuming we're\x01",
            "about to hear the story\x01",
            "behind that next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAh, well, sorry, but I'm\x01",
            "not a researcher and\x01",
            "don't know those details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRather than growth, I get\x01",
            "this image of drawing out\x01",
            "the quartz's hidden power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, that aside, I can at least\x01",
            "tell you what you need to know about\x01",
            "how to use your Enigma II units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNot the theory behind\x01",
            "them, but how to use\x01",
            "them practically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBefore that though,\x01",
            "please take these.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Elie received ",
            scpstr(SCPSTR_CODE_ITEM, 0xDE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xDE, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Wazy received ",
            scpstr(SCPSTR_CODE_ITEM, 0xDF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xDF, 1)

    ChrTalk(
        0x102,
        (
            "#6P#00105FSo this is a Master\x01",
            "Quartz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThere's no question it\x01",
            "has a different feel to\x01",
            "it than a normal quartz.\x02\x03",
            "#10300FBut is it really okay\x01",
            "for us to have these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYes, they were given to\x01",
            "me by CSPD HQ to give to\x01",
            "you in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, Master Quartz can't be\x01",
            "synthesized at normal workshops,\x01",
            "and can't be mass produced either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe only received a few\x01",
            "from the foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBasically, we're able to sell only\x01",
            "one Master Quartz of each type, so\x01",
            "please be careful with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI see. So they're quite\x01",
            "rare, in other words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FSo do you have any practical\x01",
            "tips for us before we give\x01",
            "them a shot, Wendy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRight. First, can you\x01",
            "all please equip your\x01",
            "Master Quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt doesn't matter who has\x01",
            "which set. Let me know\x01",
            "once everyone's equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, although Master\x01",
            "Quartz have elemental types,\x01",
            "their slots have no restrictions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn other words, anyone\x01",
            "can use any Master\x01",
            "Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FI see. That's rather\x01",
            "convenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHeh, well what are we\x01",
            "waiting for then, let's\x01",
            "pop them in!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Enigma Ⅱ\x01",
            "Training]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x132, 6)
    OP_29(0x65, 0x1, 0x0)
    OP_1B(0x0, 0x0, 0x1A)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_A249 end

    def Function_22_B03E(): pass

    label("Function_22_B03E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11POk great, everyone has a\x01",
            "Master Quartz set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FSo, what do we do next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHaha, it's simple― I want you to\x01",
            "see the power of Master Quartz for\x01",
            "yourselves in a practical test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FYou mean you want us to\x01",
            "fight with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, precisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLloyd, Noｱl, I heard you have some\x01",
            "experience with them but I'd like\x01",
            "you guys to give it another shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBy the way, are there any\x01",
            "specific requirements, like a\x01",
            "location or number of battles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo, nothing special. The\x01",
            "location and opponent\x01",
            "are up to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POne battle should be\x01",
            "plenty. Just make sure to\x01",
            "fight without running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHeh, well I think we can\x01",
            "manage that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLloyd, do you have any\x01",
            "ideas on where we should\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B47D")

    ChrTalk(
        0x101,
        (
            "#6P#00003FHmm, I'd like to stay in\x01",
            "the city for the time\x01",
            "being.\x02\x03",
            "#00000FThe monsters in Maison\x01",
            "Imelda might be the\x01",
            "perfect opponents.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_B523")

    label("loc_B47D")


    ChrTalk(
        0x101,
        (
            "#6P#00003FOh yeah, we have a request to\x01",
            "clear out some monsters roaming\x01",
            "around Maison Imelda, don't we?\x02\x03",
            "#00000FIt'll be like killing two birds\x01",
            "with one stone.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B523")


    ChrTalk(
        0x109,
        (
            "#6P#10100FIt certainly would be an\x01",
            "easy way to test them\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHaha, looks like you've\x01",
            "decided on a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PActually, please take\x01",
            "this quartz with you\x01",
            "too.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x74, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYes, it's another gift\x01",
            "from HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you set it in a normal slot,\x01",
            "you'll be able to use the new\x01",
            "ENIGMA Ⅱ art, "Analyze".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHe who controls information,\x01",
            "controls the battle, they say. Be\x01",
            "my guest and test it out in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, got it.\x02\x03",
            "#00003F(Tio's not around... We'll\x01",
            "need to rely on arts to obtain\x01",
            "enemy info for a while.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWell then, best of luck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd don't forget that you can\x01",
            "always count on me for orbment\x01",
            "modifications and quartz synthesis!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Select the [Quartz/Slot] option\x01",
            "at the orbal store to get new\x01",
            "quartz and open more slots.\x02\x03",
            "Once you make new quartz, you\x01",
            "can equip them by selecting\x01",
            "[QUARTZ] from the Camp menu.\x02\x03",
            "By opening more slots, you can\x01",
            "equip more quartz, and your\x01",
            "maximum EP also increases.\x02\x03",
            "You need Sepith to open slots\x01",
            "or create quartz. You get\x01",
            "sepith from defeating monsters.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x132, 7)
    OP_29(0x65, 0x1, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_B03E end

    def Function_23_B9FF(): pass

    label("Function_23_B9FF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11POh, nice work everyone.\x01",
            "So you were able to use\x01",
            "it in combat then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat are your impressions\x01",
            "of the Master Quartz,\x01",
            "Elie and Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell, I was actually\x01",
            "pretty surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, I never thought we'd\x01",
            "be able to get so much power\x01",
            "out of a single quartz.\x02\x03",
            "#10300FTo be honest, it exceeded my\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8B")

    ChrTalk(
        0x9,
        (
            "#11PHaha, that's the\x01",
            "reaction I was hoping\x01",
            "for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, something special\x01",
            "happens when you grow them to\x01",
            "their final stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBut I think I'll let you\x01",
            "guys discover it as you\x01",
            "go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FWow, there's still more\x01",
            "surprises left in this\x01",
            "thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha, well that's\x01",
            "something to look\x01",
            "forward to as we train.\x02\x03",
            "#00000FSo do you need us for\x01",
            "anything else right now,\x01",
            "Wendy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE97")

    label("loc_BD8B")


    ChrTalk(
        0x9,
        (
            "#11PHaha, that's the\x01",
            "reaction I was hoping\x01",
            "for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI want to send it to the\x01",
            "Epstein Foundation\x01",
            "development staff, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha, I've got to give\x01",
            "you credit here. That\x01",
            "wasn't too bad.\x02\x03",
            "#00000FSo do you need us for\x01",
            "anything else right now,\x01",
            "Wendy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE97")


    ChrTalk(
        0x9,
        (
            "#11PNope, I'll send my\x01",
            "report to HQ right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PDo you guys have any other\x01",
            "questions about how to use these\x01",
            "orbments before I let you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POr anything you want to\x01",
            "hear again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRight...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE54")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "About Tactical Orbments\x01",        # 0
            "About Quartz\x01",                   # 1
            "About Opening Slots\x01",            # 2
            "About Strengthening Slots\x01",      # 3
            "About Orbal Magic (Arts)\x01",       # 4
            "About the ENIGMA Ⅱ\x01",            # 5
            "About Master Quartz\x01",            # 6
            "Cancel\x01",                         # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C06B"),
        (1, "loc_C26C"),
        (2, "loc_C3E0"),
        (3, "loc_C549"),
        (4, "loc_C6EE"),
        (5, "loc_C972"),
        (6, "loc_CB75"),
        (SWITCH_DEFAULT, "loc_CE40"),
    )


    label("loc_C06B")


    ChrTalk(
        0x9,
        (
            "#11P#11PTactical Orbments are small,\x01",
            "portable orbal devices\x01",
            "specialized for use in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#11PIn addition to strengthening\x01",
            "the user, they support the\x01",
            "user with the use of arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey're usually simply\x01",
            "called "orbments".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POrbments are completely aligned and\x01",
            "optimized for the individual, so the\x01",
            "structure varies depending on the user.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere are slots with attribute limits, and\x01",
            "the shape of the connecting lines differs. It\x01",
            "might be good to compare them at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_C26C")


    ChrTalk(
        0x9,
        (
            "#11PQuartz are "crystal circuits"\x01",
            "for use in orbments made by\x01",
            "smelting sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you bring me the\x01",
            "required sepith, we can\x01",
            "synthesize the quartz here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PDepending on the quartz, there are various\x01",
            "effects, and when the property values are over\x01",
            "a fixed number, arts become able to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POnce you've gathered\x01",
            "some sepith, give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_C3E0")


    ChrTalk(
        0x9,
        (
            "#11POrbment slots are, from\x01",
            "the start, sealed for\x01",
            "the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn order to set a\x01",
            "quartz, you first need\x01",
            "an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you open a slot, the number\x01",
            "of quartz you can use increases,\x01",
            "as well as your maximum EP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough you need sepith to open slots,\x01",
            "it'll be pretty useful for you. I think\x01",
            "you should proactively open them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_C549")


    ChrTalk(
        0x9,
        (
            "#11PAmong quartz, some are\x01",
            "designated "high-rank\x01",
            "quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey're too strong, so\x01",
            "you can't set them in\x01",
            "normal slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat you need to do is\x01",
            "strengthen the slot\x01",
            "itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou need sepith to do that,\x01",
            "and your maximum EP increases,\x01",
            "the same as with sealed slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI don't think you should rush to strengthen\x01",
            "them, but it is an indispensable component\x01",
            "of powering up your orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_C6EE")


    ChrTalk(
        0x9,
        (
            "#11PMagic invoked using\x01",
            "tactical orbments. In other\x01",
            "words, orbal arts, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey're often referred\x01",
            "to simply as "arts."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe kinds of arts that can be invoked are\x01",
            "decided by the sum total of the attribute\x01",
            "values of the quartz on each line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn other words, the higher the attribute\x01",
            "values of the quartz you have set, the\x01",
            "more arts you'll be able to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, if you want to use high-\x01",
            "level arts, you'll need to pay attention\x01",
            "to the attribute value combinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAll the detailed information regarding that\x01",
            "is in a list in your detective notebook, so\x01",
            "refer to it whenever you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_C972")


    ChrTalk(
        0x9,
        (
            "#11PInheriting the ENIGMA's communication\x01",
            "function, the successor model has been\x01",
            "boldly remodeled― That's the "ENIGMA Ⅱ".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFar and away the biggest change from\x01",
            "the previous model is compatibility\x01",
            "with special "Master Quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough it's mostly the same...\x01",
            "The new version's basic\x01",
            "architecture has changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBecause of compatibility problems,\x01",
            "you can't set quartz that could be\x01",
            "used with the old ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd so, you need new\x01",
            "standard quartz for use\x01",
            "with the ENIGMA Ⅱ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_CB75")


    ChrTalk(
        0x9,
        (
            "#11PMaster quartz are special\x01",
            "quartz that are inserted in\x01",
            "the center of your ENIGMA Ⅱs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA definite difference from\x01",
            "your usual quartz is that the\x01",
            "master quartz itself "grows".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy accumulating battles with\x01",
            "them set, they will level up and\x01",
            "exhibit more powerful effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PStrengthening the user, the quartz's special\x01",
            "effect and the attribute values... Those three\x01",
            "components are affected by the quartz's growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, to discover the true\x01",
            "powers of each master quartz, it seems\x01",
            "you need to bring them to max level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough it seems to take\x01",
            "a long time to level\x01",
            "them up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt might be important to not\x01",
            "mess around and continue to\x01",
            "use your favorites.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_CE40")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CE4F")

    label("loc_CE4F")

    Jump("loc_BF7E")

    label("loc_CE54")


    ChrTalk(
        0x101,
        (
            "#6P#00004FThat's plenty I think.\x02\x03",
            "#00000FThank you so much Wendy.\x01",
            "We really learned a ton\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHaha, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh by the way, here's a\x01",
            "new standard ENIGMA Ⅱ\x01",
            "quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConsider it a gift in\x01",
            "celebration of the restart\x01",
            "of SSS activities.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xB7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xB7, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00002FThanks so much Wendy.\x01",
            "We'll put it to good\x01",
            "use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FReally. You were a huge\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHaha. It's my pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh by the way, if there's ever\x01",
            "something you don't fully understand,\x01",
            "feel free to ask me anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI should mention that we offer\x01",
            "various new services at the\x01",
            "counter next to me as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo I hope you continue to make\x01",
            "use of Orbal Store Genten for\x01",
            "all your orbment needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHehe, will do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FThanks again for all\x01",
            "your help today!\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Enigma II\x01",
            "Training]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_29(0x65, 0x1, 0x3)
    OP_29(0x65, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x2)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_B9FF end

    def Function_24_D250(): pass

    label("Function_24_D250")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-6460, 1500, 2290, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D3CA")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x104, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_D31B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D31B)

    def lambda_D32C():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D32C)

    def lambda_D341():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D341)

    def lambda_D352():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D352)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D37B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D37B)

    def lambda_D38C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D38C)
    Sleep(100)

    def lambda_D3A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D3A4)

    def lambda_D3B5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D3B5)
    Jump("loc_D645")

    label("loc_D3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D50A")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x109, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_D45B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D45B)

    def lambda_D46C():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D46C)

    def lambda_D481():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D481)

    def lambda_D492():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D492)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D4BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D4BB)

    def lambda_D4CC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4CC)
    Sleep(100)

    def lambda_D4E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D4E4)

    def lambda_D4F5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D4F5)
    Jump("loc_D645")

    label("loc_D50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D645")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x105, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_D59B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D59B)

    def lambda_D5AC():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D5AC)

    def lambda_D5C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D5C1)

    def lambda_D5D2():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5D2)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D5FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D5FB)

    def lambda_D60C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D60C)
    Sleep(100)

    def lambda_D624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D624)

    def lambda_D635():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D635)

    label("loc_D645")

    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        (
            "So this is the orbal\x01",
            "store from all those\x01",
            "magazines, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It has a nice atmosphere,\x01",
            "and practically all the\x01",
            "goods are cutting edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I don't think there's a\x01",
            "store this big in the\x01",
            "Republic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, it's very like Crossbell to\x01",
            "have goods from many different\x01",
            "nations all in one place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSpeaking of cutting edge,\x01",
            "this is what they call an\x01",
            "orbal network terminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Orbal n-e-t... you say?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D83A")

    def lambda_D81D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D81D)
    Sleep(50)

    def lambda_D82D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D82D)
    Jump("loc_D88B")

    label("loc_D83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D865")

    def lambda_D848():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D848)
    Sleep(50)

    def lambda_D858():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D858)
    Jump("loc_D88B")

    label("loc_D865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D88B")

    def lambda_D873():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D873)
    Sleep(50)

    def lambda_D883():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D883)

    label("loc_D88B")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah. To put it simply, it's an\x01",
            "advanced communication device.\x02\x03",
            "#00004FThe orbal network plan is\x01",
            "progressing led by the Epstein\x01",
            "Foundation, but...\x02\x03",
            "#00000FBy using a terminal, you can\x01",
            "transmit not just your voice, but\x01",
            "letters and pictures as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "W-Wow... So they have\x01",
            "this sort of thing\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_93(0x1A2, 0x5A, 0x1F4)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "H-Hmph, not that I'm\x01",
            "surprised or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Displaying this level of\x01",
            "knowledge is just\x01",
            "showing off!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DB48")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FAh, I don't think it's\x01",
            "really showing off,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FHah, the brat can't be\x01",
            "honest about anything,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCF9")

    label("loc_DB48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DC30")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FAh, I don't think it's\x01",
            "really showing off,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRather than dishonest,\x01",
            "maybe you should say he\x01",
            "hates to lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCF9")

    label("loc_DC30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DCF9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FAh, I don't think it's\x01",
            "really showing off,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHaha. He hates to lose,\x01",
            "doesn't he.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCF9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 5)
    OP_29(0x73, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4800, 0, 2530, 90)
    EventEnd(0x5)
    Return()

    # Function_24_D250 end

    def Function_25_DD25(): pass

    label("Function_25_DD25")

    EventBegin(0x0)
    Fade(500)
    OP_68(7160, 1500, -1600, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 6940, 0, -1330, 90)
    SetChrPos(0x102, 6850, 0, -320, 90)
    SetChrPos(0x103, 6730, 0, -2450, 90)
    SetChrPos(0x104, 5780, 0, -1390, 90)
    SetChrPos(0x105, 5400, 0, -2610, 90)
    SetChrPos(0x109, 5680, 0, -160, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "Oh, Lloyd. Need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Wouldn't she make a\x01",
            "fine "worker" for the\x01",
            "pageant?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm. She's not into this\x01",
            "sort of thing. But, since\x01",
            "we're here, I'll ask her.)\x02\x03",
            "#00000FWendy, do you have a\x01",
            "minute?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Wendy to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "Pageant? What's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is it a new orbment\x01",
            "component or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FNo, no, no. That's\x01",
            "totally not it, Wendy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThat's a worker for\x01",
            "you... So ignorant of\x01",
            "the outside world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahaha, I kid, I kid. I\x01",
            "know what a beauty\x01",
            "contest is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, interesting... So I\x01",
            "can participate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHaha, I'm surprised. I\x01",
            "never expected an OK\x01",
            "from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, nothing ventured\x01",
            "nothing gained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's my childhood\x01",
            "friend asking, I'll take\x01",
            "you up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have work to do until the\x01",
            "program starts, so call me\x01",
            "when you need me, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, will do. Thanks,\x01",
            "Wendy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2B0")

    ChrTalk(
        0x101,
        (
            "#00000F─Alright. With this\x01",
            "we've finally filled our\x01",
            "quota.\x02\x03",
            "Let's head to City\x01",
            "Meeting Hall and report\x01",
            "to Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_E2B0")

    SetScenarioFlags(0x199, 5)
    OP_4C(0x9, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7330, 0, -1350, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_DD25 end

    def Function_26_E2E3(): pass

    label("Function_26_E2E3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, we can't leave\x01",
            "the store right now.\x02\x03",
            "Let's speak with Wendy\x01",
            "once we've set the\x01",
            "Master Quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 0, 2230, 90)
    EventEnd(0x4)
    Return()

    # Function_26_E2E3 end

    SaveToFile()

Try(main)
