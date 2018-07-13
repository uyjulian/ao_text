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
        "Function_5_A28",          # 05, 5
        "Function_6_26A0",         # 06, 6
        "Function_7_2ECF",         # 07, 7
        "Function_8_3A91",         # 08, 8
        "Function_9_3A9B",         # 09, 9
        "Function_10_3F37",        # 0A, 10
        "Function_11_5C8F",        # 0B, 11
        "Function_12_6B2B",        # 0C, 12
        "Function_13_6D55",        # 0D, 13
        "Function_14_80E5",        # 0E, 14
        "Function_15_8D22",        # 0F, 15
        "Function_16_991E",        # 10, 16
        "Function_17_9AB9",        # 11, 17
        "Function_18_9F56",        # 12, 18
        "Function_19_A280",        # 13, 19
        "Function_20_A3DB",        # 14, 20
        "Function_21_A51D",        # 15, 21
        "Function_22_B314",        # 16, 22
        "Function_23_BD4F",        # 17, 23
        "Function_24_D584",        # 18, 24
        "Function_25_E032",        # 19, 25
        "Function_26_E615",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C")

    ChrTalk(
        0x8,
        (
            "Welcooome☆\x01",
            "This is the purchasing counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, you're all acquaintances\x01",
            "of senior Wendy, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, we have received\x01",
            "some new ENIGMA covers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, once you buy them\x01",
            "you can then switch them whenever\x01",
            "you want free of charge at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please work Chalk \x01",
            "hard non-stop!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 4)

    label("loc_82C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_836")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A24")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FD")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                       # 0
            "Buy - Change Covers\x01",        # 1
            "Buy Master Quartz\x01",          # 2
            "Buy Orbal Car Options\x01",      # 3
            "Quit\x01",                       # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F8")

    Jump("loc_978")

    label("loc_8FD")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                     # 0
            "Buy - Change Covers\x01",      # 1
            "Buy Master Quartz\x01",        # 2
            "Quit\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_978")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_978")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_999")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1F")

    label("loc_999")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BD")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1F")

    label("loc_9BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1F")

    label("loc_9E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A03")
    OP_AF(0xC0)
    Jump("loc_A15")

    label("loc_A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A13")
    OP_AF(0xBF)
    Jump("loc_A15")

    label("loc_A13")

    OP_AF(0xBE)

    label("loc_A15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1F")

    Jump("loc_836")

    label("loc_A24")

    TalkEnd(0x8)
    Return()

    # Function_4_6C3 end

    def Function_5_A28(): pass

    label("Function_5_A28")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269F")
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
        "Which will you switch to?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B51")
    MenuCmd(1, 0, "CPD (Lloyd)         Equipped")
    Jump("loc_B72")

    label("loc_B51")

    MenuCmd(1, 0, "CPD (Lloyd)         Change To")

    label("loc_B72")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_BB4")
    MenuCmd(1, 0, "Blue Sheriff        Equipped")
    Jump("loc_C04")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_BE3")
    MenuCmd(1, 0, "Blue Sheriff        Change To")
    Jump("loc_C04")

    label("loc_BE3")

    MenuCmd(1, 0, "Blue Sheriff        1000 mira")

    label("loc_C04")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_C3C")
    MenuCmd(1, 0, "Howling Wolf        Equipped")
    Jump("loc_C8C")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_C6B")
    MenuCmd(1, 0, "Howling Wolf        Change To")
    Jump("loc_C8C")

    label("loc_C6B")

    MenuCmd(1, 0, "Howling Wolf        1000 mira")

    label("loc_C8C")

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
    Jump("loc_D3B")

    label("loc_D1D")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7F")
    MenuCmd(1, 0, "CPD (Elie)          Equipped")
    Jump("loc_DA0")

    label("loc_D7F")

    MenuCmd(1, 0, "CPD (Elie)          Change To")

    label("loc_DA0")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_DE2")
    MenuCmd(1, 0, "Peace Green         Equipped")
    Jump("loc_E32")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_E11")
    MenuCmd(1, 0, "Peace Green         Change To")
    Jump("loc_E32")

    label("loc_E11")

    MenuCmd(1, 0, "Peace Green         1000 mira")

    label("loc_E32")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_E6A")
    MenuCmd(1, 0, "Spring Bird         Equipped")
    Jump("loc_EBA")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_E99")
    MenuCmd(1, 0, "Spring Bird         Change To")
    Jump("loc_EBA")

    label("loc_E99")

    MenuCmd(1, 0, "Spring Bird         1000 mira")

    label("loc_EBA")

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
    Jump("loc_F4B")

    label("loc_F2D")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_111F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8F")
    MenuCmd(1, 0, "CPD (Tio)           Equipped")
    Jump("loc_FB0")

    label("loc_F8F")

    MenuCmd(1, 0, "CPD (Tio)           Change To")

    label("loc_FB0")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_FF2")
    MenuCmd(1, 0, "Black Cat           Equipped")
    Jump("loc_1042")

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_1021")
    MenuCmd(1, 0, "Black Cat           Change To")
    Jump("loc_1042")

    label("loc_1021")

    MenuCmd(1, 0, "Black Cat           1000 mira")

    label("loc_1042")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_107A")
    MenuCmd(1, 0, "Shadow Circle       Equipped")
    Jump("loc_10CA")

    label("loc_107A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_10A9")
    MenuCmd(1, 0, "Shadow Circle       Change To")
    Jump("loc_10CA")

    label("loc_10A9")

    MenuCmd(1, 0, "Shadow Circle       1000 mira")

    label("loc_10CA")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_113D")

    label("loc_111F")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_113D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1181")
    MenuCmd(1, 0, "CPD (Randy)         Equipped")
    Jump("loc_11A2")

    label("loc_1181")

    MenuCmd(1, 0, "CPD (Randy)         Change To")

    label("loc_11A2")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_11E4")
    MenuCmd(1, 0, "Danger Orange       Equipped")
    Jump("loc_1234")

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_1213")
    MenuCmd(1, 0, "Danger Orange       Change To")
    Jump("loc_1234")

    label("loc_1213")

    MenuCmd(1, 0, "Danger Orange       1000 mira")

    label("loc_1234")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_126C")
    MenuCmd(1, 0, "Midnight Kiss       Equipped")
    Jump("loc_12BC")

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_129B")
    MenuCmd(1, 0, "Midnight Kiss       Change To")
    Jump("loc_12BC")

    label("loc_129B")

    MenuCmd(1, 0, "Midnight Kiss       1000 mira")

    label("loc_12BC")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1311")

    label("loc_12F3")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1311")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1350")
    MenuCmd(1, 0, "CGF (Noｱl)          Equipped")
    Jump("loc_1371")

    label("loc_1350")

    MenuCmd(1, 0, "CGF (Noｱl)          Change To")

    label("loc_1371")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_13A9")
    MenuCmd(1, 0, "Liberty Road        Equipped")
    Jump("loc_13F9")

    label("loc_13A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_13D8")
    MenuCmd(1, 0, "Liberty Road        Change To")
    Jump("loc_13F9")

    label("loc_13D8")

    MenuCmd(1, 0, "Liberty Road        1000 mira")

    label("loc_13F9")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1430")

    label("loc_141C")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1430")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146F")
    MenuCmd(1, 0, "White Creed         Equipped")
    Jump("loc_1490")

    label("loc_146F")

    MenuCmd(1, 0, "White Creed         Change To")

    label("loc_1490")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_14C8")
    MenuCmd(1, 0, "Crest Face          Equipped")
    Jump("loc_1518")

    label("loc_14C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_14F7")
    MenuCmd(1, 0, "Crest Face          Change To")
    Jump("loc_1518")

    label("loc_14F7")

    MenuCmd(1, 0, "Crest Face          1000 mira")

    label("loc_1518")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_153B")

    label("loc_1527")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_153B")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_156C")
    Sleep(1)
    Return()

    label("loc_156C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1947")

    label("loc_15AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E8")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_1947")

    label("loc_15E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1626")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_1947")

    label("loc_1626")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1664")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1947")

    label("loc_1664")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A2")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_1947")

    label("loc_16A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E0")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_1947")

    label("loc_16E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171E")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1947")

    label("loc_171E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175C")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_1947")

    label("loc_175C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179A")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_1947")

    label("loc_179A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D8")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1947")

    label("loc_17D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1816")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_1947")

    label("loc_1816")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1854")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_1947")

    label("loc_1854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1892")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_1947")

    label("loc_1892")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D0")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_1947")

    label("loc_18D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190E")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_1947")

    label("loc_190E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1947")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_1947")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A1A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Lloyd's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D39")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1ABE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Elie's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D39")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B61")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Tio's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D39")

    label("loc_1B61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C06")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Randy's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D39")

    label("loc_1C06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CA2")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Noｱl's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D39")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D39")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Wazy's use only.\x01",
            "You can change the displayed tactical orbment\x01",
            "cover under [ORBMENT] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D39")


    AnonymousTalk(
        0x8,
        "Alright, are you fine with this?\x02",
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
            "[Quit]\x01",                 # 1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2682")
    ClearScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DFB")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E14")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2D")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E65")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E7E")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9D")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1E9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB6")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ECF")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1ECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEE")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F07")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1F07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F20")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1F20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3A")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F53")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1F53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F6D")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1F81")

    label("loc_1F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F81")
    SetScenarioFlags(0x1, 1)

    label("loc_1F81")

    ClearScenarioFlags(0x1, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F99")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_1F99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB2")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FCB")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE0")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FF9")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2012")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_2012")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2027")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_2027")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2040")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_2040")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2059")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_2059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206E")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_206E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2087")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_2087")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A0")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_20A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B5")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_20B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20CE")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_20CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E3")
    SetScenarioFlags(0x1, 2)
    Jump("loc_20F7")

    label("loc_20E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F7")
    SetScenarioFlags(0x1, 2)

    label("loc_20F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(
        0x8,
        (
            "Whaaat, you've got it already equipped?\x01",
            "Please choose another one, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2673")

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B9")

    ChrTalk(
        0x8,
        (
            "Whaaat, it looks like you're short on mira?\x01",
            "Then, you can't exchange it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2673")

    label("loc_21B9")


    ChrTalk(
        0x8,
        (
            "Roger!\x01",
            "Please wait a moment㈱\x02",
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
        "Here, sorry to have made you waiting.\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22CA")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228D")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_22C5")

    label("loc_228D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    SetScenarioFlags(0x2C, 0)

    label("loc_22A7")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_22C5")

    label("loc_22B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BF")
    SetScenarioFlags(0x2C, 1)

    label("loc_22BF")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_22C5")

    Jump("loc_25B3")

    label("loc_22CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2378")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2329")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_2373")

    label("loc_2329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2357")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234C")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_234C")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_2373")

    label("loc_2357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236D")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_236D")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_2373")

    Jump("loc_25B3")

    label("loc_2378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2425")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D6")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_2420")

    label("loc_23D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F9")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23F9")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_2420")

    label("loc_2404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241A")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_241A")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_2420")

    Jump("loc_25B3")

    label("loc_2425")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24D4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2485")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_24CF")

    label("loc_2485")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A8")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_24A8")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_24CF")

    label("loc_24B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C9")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_24C9")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_24CF")

    Jump("loc_25B3")

    label("loc_24D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2546")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2528")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_2541")

    label("loc_2528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253E")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_253E")

    SetScenarioFlags(0x2F, 0)

    label("loc_2541")

    Jump("loc_25B3")

    label("loc_2546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25B3")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259A")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_25B3")

    label("loc_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B0")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25B0")

    SetScenarioFlags(0x2E, 4)

    label("loc_25B3")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_262A")
    OP_E0(0x16, 0x0)

    label("loc_262A")


    ChrTalk(
        0x8,
        (
            "Uh uh, I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2673")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2673")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_268C")

    label("loc_2682")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_268C")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_A32")

    label("loc_269F")

    Return()

    # Function_5_A28 end

    def Function_6_26A0(): pass

    label("Function_6_26A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECE")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x4)"), scpexpr(EXPR_END)), "loc_26ED")
    MenuCmd(1, 0, "Platinum        Purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_270B")

    label("loc_26ED")

    MenuCmd(1, 0, "Platinum         1000 mira")

    label("loc_270B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x4)"), scpexpr(EXPR_END)), "loc_273C")
    MenuCmd(1, 0, "Mirage          Purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_2759")

    label("loc_273C")

    MenuCmd(1, 0, "Mirage          5000 mira")

    label("loc_2759")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x4)"), scpexpr(EXPR_END)), "loc_2798")
    MenuCmd(1, 0, "Aegis           Purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_27B6")

    label("loc_2798")

    MenuCmd(1, 0, "Aegis           20000 mira")

    label("loc_27B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x4)"), scpexpr(EXPR_END)), "loc_27E7")
    MenuCmd(1, 0, "Scepter         Purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_2805")

    label("loc_27E7")

    MenuCmd(1, 0, "Scepter         50000 mira")

    label("loc_2805")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2842")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2842")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_285F")
    Sleep(1)
    Return()

    label("loc_285F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_295A")

    label("loc_289F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28DF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_295A")

    label("loc_28DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_295A")

    label("loc_291F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295A")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_295A")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F6")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Space element Master Quartz.\x01",
            "※Raises HP/ADF, recovers HP on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3A")

    label("loc_29F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A65")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mirage element Master Quartz.\x01",
            "※Raises EP/ATS, recovers EP on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3A")

    label("loc_2A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD7")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Earth element Master Quartz.\x01",
            "※Raises DEF/ADF, gain MAX GUARD in certain conditions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3A")

    label("loc_2AD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water element Master Quartz.\x01",
            "※Raises STR/ATS, gain Sepith when attacking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3A")


    AnonymousTalk(
        0x8,
        "Alright, are you fine with this?\x02",
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
            "[Buy]\x01",       # 0
            "[Quit]\x01",      # 1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C6D")

    ChrTalk(
        0x8,
        (
            "Whaaat, it looks like you're short on mira?\x01",
            "Then, you can't buy it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA2")

    label("loc_2C6D")


    ChrTalk(
        0x8,
        (
            "Roger!\x01",
            "Please wait a moment㈱\x02",
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
        "Here, sorry to have made you waiting.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3F")
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
    Jump("loc_2E6C")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA5")
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
    Jump("loc_2E6C")

    label("loc_2DA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0B")
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
    Jump("loc_2E6C")

    label("loc_2E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6C")
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

    label("loc_2E6C")


    ChrTalk(
        0x8,
        (
            "Uh uh, I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2EA2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EBB")

    label("loc_2EB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EBB")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_26AA")

    label("loc_2ECE")

    Return()

    # Function_6_26A0 end

    def Function_7_2ECF(): pass

    label("Function_7_2ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F62")

    ChrTalk(
        0x8,
        (
            "Papa's been staring this whole time.\x01",
            "He's gonna burn a hole right through Chalk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, I'm glad he's\x01",
            "this worried about me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_2F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3055")

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
            "Senior Wendy said she'd stay\x01",
            "behind to help if needed,\x01",
            "so Chalk decided to stay too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My dad won't like it, \x01",
            "but I'm sure\x01",
            "he'll understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30DA")

    ChrTalk(
        0x8,
        (
            "President Dieter's speech...\x01",
            "That was impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Chalk unconsciously stopped\x01",
            "breathing in the middle of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_30DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3194")

    ChrTalk(
        0x8,
        (
            "This past week, I was always together with papa\x01",
            "when leaving home for work and coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if it's only for those specific times,\x01",
            "Chalk is really relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3209")

    ChrTalk(
        0x8,
        "I'm really worried about the people of Mainz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why did something like\x01",
            "this have to happen...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F0")

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
        "Man, that was so embarrassing for Chalk.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_335C")

    label("loc_32F0")


    ChrTalk(
        0x8,
        (
            "It seems my dad interviewed\x01",
            "for a position at our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ooh, Chalk just wants\x01",
            "to hide right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335C")

    Jump("loc_3A90")

    label("loc_3361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3397")

    ChrTalk(
        0x8,
        (
            "A train derailment...\x01",
            "How awful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3415")

    ChrTalk(
        0x8,
        "My dad seems nervous somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't explain it, but... I'm getting\x01",
            "a really bad feeling about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(
        0x8,
        (
            "I understand why my dad's\x01",
            "worried about me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anyway, it's excessive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B8")

    ChrTalk(
        0x8,
        (
            "To scold a customer...\x01",
            "I can't believe this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_34B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3559")

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
    Jump("loc_3A90")

    label("loc_3559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3602")

    ChrTalk(
        0x8,
        (
            "Senior Wendy is always borrowing\x01",
            "the orbal camera I use\x01",
            "for our demo unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Chalk wanted to take a photo of Princess\x01",
            "Klaudia and Archduke Albert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A1")

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
    Jump("loc_37FF")

    label("loc_36A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377B")

    ChrTalk(
        0x8,
        (
            "In any case, my dad never gets\x01",
            "tired of coming here, day after day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I say anything he won't stop,\x01",
            "so I've been ignoring him lately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe it's not good\x01",
            "spoiling him too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_37FF")

    label("loc_377B")


    ChrTalk(
        0x8,
        (
            "He'll come even if I tell him not to,\x01",
            "so I've been ignoring him lately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe it's not good\x01",
            "spoiling him too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FF")

    Jump("loc_3A90")

    label("loc_3804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395F")

    ChrTalk(
        0x8,
        (
            "The store manager's attitude\x01",
            "towards senior Wendy has\x01",
            "clearly changed recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before, he addressed her informally, but\x01",
            "he suddenly started respecting her more...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After that, he started\x01",
            "to use more formal\x01",
            "words towards her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first, senior too was bewildered,\x01",
            "but now she's got totally used to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3A04")

    label("loc_395F")


    ChrTalk(
        0x8,
        (
            "The store manager's attitude\x01",
            "towards senior Wendy has\x01",
            "clearly changed recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first, senior too was bewildered,\x01",
            "but now she's got totally used to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A04")

    Jump("loc_3A90")

    label("loc_3A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A90")

    ChrTalk(
        0x8,
        (
            "At this counter we sell and\x01",
            "change orbment covers, and\x01",
            "we sell Master Quartz too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please work Chalk \x01",
            "hard non-stop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A90")

    Return()

    # Function_7_2ECF end

    def Function_8_3A91(): pass

    label("Function_8_3A91")

    OP_C9(0x1, 0x80)
    Call(0, 9)
    Return()

    # Function_8_3A91 end

    def Function_9_3A9B(): pass

    label("Function_9_3A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC9")
    Call(0, 25)
    Return()

    label("loc_3AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C64")
    TalkBegin(0x9)

    ChrTalk(
        0x9,
        "Yoohoo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What's up? You've got such\x01",
            "a cute little boy with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we're showing\x01",
            "this boy we know\x01",
            "around town.\x02",
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
            "So he's not from\x01",
            "around here, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Hey you, this kind of store's\x01",
            "not all that common, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Relax, take your time,\x01",
            "and give it plenty of love.\x02",
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
    Jump("loc_3CE3")

    label("loc_3C64")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "Giving tours of the\x01",
            "city sure looks fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha ha, but even so, you\x01",
            "guys do a lot of different\x01",
            "things, don't you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3CE3")

    Return()

    label("loc_3CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D13")
    Call(0, 21)
    Return()

    label("loc_3D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D6A")
    Call(0, 22)
    Jump("loc_3DE3")

    label("loc_3D6A")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "First off, will each of you\x01",
            "set a Master Quartz for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Speak to me after that, and we'll go from there.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3DE3")

    Return()

    label("loc_3DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E0A")
    Call(0, 23)
    Return()

    label("loc_3E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E2A")
    SetScenarioFlags(0x0, 1)
    TalkBegin(0x9)
    Call(0, 12)
    TalkEnd(0x9)
    Return()

    label("loc_3E2A")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F33")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                     # 0
            "Modify - Synthesize\x01",      # 1
            "Questions?\x01",               # 2
            "Quit\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_3F2E")

    label("loc_3EC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EE1")
    OP_AF(0xD)
    Jump("loc_3F03")

    label("loc_3EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EF1")
    OP_AF(0xC)
    Jump("loc_3F03")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F01")
    OP_AF(0xB)
    Jump("loc_3F03")

    label("loc_3F01")

    OP_AF(0xA)

    label("loc_3F03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F2E")

    label("loc_3F12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3F2E")

    Jump("loc_3E37")

    label("loc_3F33")

    TalkEnd(0x9)
    Return()

    # Function_9_3A9B end

    def Function_10_3F37(): pass

    label("Function_10_3F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4275")

    ChrTalk(
        0x9,
        (
            "Lloyd and everyone―\x01",
            "Nice work breaking through\x01",
            "the President's blockade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And Lloyd, I think things will\x01",
            "be tough from here on out,\x01",
            "so let's both do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, you're right.\x02\x03",
            "#00000FAnd the same to you Wendy. Even with all that's\x01",
            "happened, you're here continuing your work.\x02\x03",
            "We'll be relying on you\x01",
            "to maintain our orbments\x01",
            "for a long time to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But anyway, it's\x01",
            "really no big deal,\x01",
            "so please take these.\x02",
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
            "#00000FThanks Wendy.\x01",
            "This is a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh, you're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, if you're going\x01",
            "anywhere dangerous,\x01",
            "be very careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then once things have calmed down, \x01",
            "let's have a meal with Oscar, \x01",
            "just the three of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, let's.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 6)
    Jump("loc_431F")

    label("loc_4275")


    ChrTalk(
        0x9,
        (
            "I think things will be \x01",
            "tough from here on out, \x01",
            "so let's both do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once things have calmed down, \x01",
            "let's have a meal with Oscar, \x01",
            "just the three of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431F")

    Jump("loc_5C8E")

    label("loc_4324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_43EA")

    ChrTalk(
        0x9,
        (
            "I heard you were all right, but...\x01",
            "It's really a relief to see \x01",
            "your face like this.\x02",
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
    Jump("loc_5C8E")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E5")

    ChrTalk(
        0x9,
        (
            "I didn't think things\x01",
            "would unfold this fast...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, it looks like things are\x01",
            "gonna be tough from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, if you need the workshop\x01",
            "just say the word whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_459D")

    label("loc_44E5")


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
            "Lloyd, if you need the workshop\x01",
            "just say the word whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459D")

    Jump("loc_5C8E")

    label("loc_45A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_492B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4671")

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
            "After work today, I'll head to Master\x01",
            "Guillaume's place to see how I can help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_4671")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475C")

    ChrTalk(
        0x9,
        (
            "The pageant, huh...? \x01",
            "Well, everything is an experience, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's a request from my childhood friend,\x01",
            "I'll help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got work to do until the\x01",
            "program starts, so call me\x01",
            "when you need me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_475C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489F")

    ChrTalk(
        0x9,
        (
            "Nice work guys.\x01",
            "I just got back from\x01",
            "the event hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...But even so,\x01",
            "that Roy's emceeing\x01",
            "was quite rude.\x02",
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
        "Does Lloyd think that too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FH-Hmm, I wonder. \x01",
            "(I can't deny it totally, but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4926")

    label("loc_489F")


    ChrTalk(
        0x9,
        (
            "Well, it was a lot more fun than\x01",
            "I thought it'd be. Thanks for inviting me.\x02",
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

    label("loc_4926")

    Jump("loc_5C8E")

    label("loc_492B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A26")

    ChrTalk(
        0x9,
        (
            "Is seem an outrageous thing\x01",
            "has happened in Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Guys, please be very careful if you're\x01",
            "involved in the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you need ENIGMA II maintenance,\x01",
            "all you gotta do is ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4AAB")

    label("loc_4A26")


    ChrTalk(
        0x9,
        (
            "Is seem an outrageous thing\x01",
            "has happened in Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Guys, please be very careful if you're\x01",
            "involved in the investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAB")

    Jump("loc_5C8E")

    label("loc_4AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B4B")

    ChrTalk(
        0x9,
        (
            "Is seems that Chalk's dad\x01",
            "is a hardcore worrywart.\x02",
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
    Jump("loc_5C8E")

    label("loc_4B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4BB9")

    ChrTalk(
        0x9,
        "I hear an orbal train has derailed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Could they have run into some machine trouble...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C8E")

    label("loc_4BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D31")

    ChrTalk(
        0x9,
        (
            "To think the store manager would\x01",
            "remodel store making it look like the\x01",
            "old one out of respect for his workers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The store is finally doing well and\x01",
            "the regulars have increased too...\x01",
            "That would only confuse the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy that the store manager\x01",
            "officially recognized his workers,\x01",
            "but I wish he thought something different.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E05")

    label("loc_4D31")


    ChrTalk(
        0x9,
        (
            "Changing the store's appearance at this late\x01",
            "date would only confuse all of the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy that the store manager\x01",
            "officially recognized his workers,\x01",
            "but I wish he thought something different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E05")

    Jump("loc_5C8E")

    label("loc_4E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_504B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6B")

    ChrTalk(
        0x9,
        (
            "Independence, eh? When I heard it at first,\x01",
            "I was shocked, but the more I hear about it,\x01",
            "the Mayor's opinions are quite plausible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's talk that the two major\x01",
            "powers are going to station troops\x01",
            "at our border gates before long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we want true peace, maybe this is the \x01",
            "very time we have to make us heard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5046")

    label("loc_4F6B")


    ChrTalk(
        0x9,
        (
            "Independence, eh? When I heard it at first,\x01",
            "I was shocked, but the more I hear about it,\x01",
            "the Mayor's opinions are quite plausible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we want true peace, maybe this is the \x01",
            "very time we have to make us heard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5046")

    Jump("loc_5C8E")

    label("loc_504B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50E2")

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
            "Well, I think nothing but bad things about\x01",
            "people who hit on employees during work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8E")

    label("loc_50E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_52B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5244")

    ChrTalk(
        0x9,
        (
            "Ah, it's you guys. You're not\x01",
            "usually around at this hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we got an emergency\x01",
            "investigation request.\x02\x03",
            "Can we shop here now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, yes, we normally\x01",
            "are opened until 8:00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, good then. I'll count on you for\x01",
            "help with our orbment maintenance then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yep, roger that.\x01",
            "Just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_52AE")

    label("loc_5244")


    ChrTalk(
        0x9,
        (
            "If you need help with your\x01",
            "ENIGMA IIs, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'll have it done for you in a jiffy.\x02",
    )

    CloseMessageWindow()

    label("loc_52AE")

    Jump("loc_5C8E")

    label("loc_52B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5736")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568D")

    ChrTalk(
        0x9,
        (
            "Uhuhu, the "Arseille". Though it\x01",
            "was from far away, I was able to\x01",
            "capture it on our orbal camera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I had it developed immediately.\x01",
            "You guys want a copy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FWow, let me have\x01",
            "a look then.\x02",
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
        "#00306FThis is really the "Arseille"?\x02",
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
        "Huh? Take a good look, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the bow and this is the stern.\x01",
            "You should be able to see it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, now that you mention it,\x01",
            "I guess you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's your love for mechas, I guess... \x01",
            "Wendy, there's more than meets the eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh, really? I think it's\x01",
            "how I always am, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha ha... \x01",
            "(For now, it's certain that\x01",
            "it's not how you always are.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 4)
    Jump("loc_5731")

    label("loc_568D")


    ChrTalk(
        0x9,
        (
            "Though it was from a distance, I was able\x01",
            "to capture the form of the "Arseille".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uhuhu, I think I'll have it enlarged\x01",
            "and hang it on the wall in my room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5731")

    Jump("loc_5C8E")

    label("loc_5736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5999")

    ChrTalk(
        0x9,
        (
            "The Trade Conference, huh?\x01",
            "I bet the Liberl representative\x01",
            "is going to come in on that "Arseille".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe "Arseille"... Oh, it's the\x01",
            "Liberl Kingdom's high-speed cruiser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Exactly! It's got all of ZCF's latest tech.\x01",
            "It's a true masterpiece.\x01",
            "The airship of airships!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When something is flying through the sky,\x01",
            "I've got to stop work and take a photo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's not like I don't understand how you\x01",
            "feel, but... Everything in moderation, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, nope. (*bluntly*)\x02",
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
            "#00309FHa ha, that's Wendy for you.\x01",
            "A fine, straightforward answer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 3)
    Jump("loc_5A58")

    label("loc_5999")


    ChrTalk(
        0x9,
        (
            "The Trade Conference, huh? I bet the Liberl\x01",
            "representative is going to come in on that "Arseille".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When something is flying through the sky,\x01",
            "I've got to stop work and take a photo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A58")

    Jump("loc_5C8E")

    label("loc_5A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5AF8")

    ChrTalk(
        0x9,
        (
            "Our store manager is more\x01",
            "studious than I thought.\x02",
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
    Jump("loc_5C8E")

    label("loc_5AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BEE")

    ChrTalk(
        0x9,
        (
            "Anyway, just one battle with\x01",
            "a Master Quartz set is fine,\x01",
            "so finish it for me, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't forget to come report\x01",
            "to me after you're done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can't complete the\x01",
            "training if you don't, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8E")

    label("loc_5BEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5C8E")

    ChrTalk(
        0x9,
        (
            "Uh uh, give plenty of love\x01",
            "to your Master Quartz\x01",
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

    label("loc_5C8E")

    Return()

    # Function_10_3F37 end

    def Function_11_5C8F(): pass

    label("Function_11_5C8F")


    ChrTalk(
        0x9,
        (
            "Okay. What do you\x01",
            "want to ask about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B1D")
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
            "About the ENIGMA II\x01",            # 5
            "About Master Quartz\x01",            # 6
            "Quit\x01",                           # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DA8")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_5DA8")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5DDC"),
        (1, "loc_5FBB"),
        (2, "loc_611B"),
        (3, "loc_6274"),
        (4, "loc_6402"),
        (5, "loc_6670"),
        (6, "loc_685B"),
        (SWITCH_DEFAULT, "loc_6B09"),
    )


    label("loc_5DDC")


    ChrTalk(
        0x9,
        (
            ""Tactical Orbments" are small, \x01",
            "portable orbal devices\x01",
            "specialized for use in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In addition to strengthening the user, they\x01",
            "support the user with the use of Arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're usually simply\x01",
            "called "Orbments".\x02",
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
            "the shape of the connecting lines differs.\x01",
            "It might be good to compare them once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_5FBB")


    ChrTalk(
        0x9,
        (
            "Quartz are "crystal circuits" for use\x01",
            "in Orbments made by smelting Sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you bring the required Sepith,\x01",
            "we can synthesize the Quartz here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Depending on the Quartz, there are various\x01",
            "effects, and when the property values are over\x01",
            " fixed number, Arts become able to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "When you've gathered some Sepith, give it a try.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_611B")


    ChrTalk(
        0x9,
        (
            "Orbment slots are, from the\x01",
            "start, sealed for the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to set a Quartz,\x01",
            "first you need an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you open a slot, the number\x01",
            "of Quartz you can use increases,\x01",
            "as well as your maximum EP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though you need Sepith to open slots, it'll be pretty\x01",
            "useful for you. I think you should proactively open them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_6274")


    ChrTalk(
        0x9,
        (
            "Among Quartz, some are\x01",
            "designated "High-Rank Quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're too strong, so you\x01",
            "can't set them in normal slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What you need to do is\x01",
            "strengthen the slot itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You need Sepith to do that, and your maximum\x01",
            "EP increases, the same as with sealed slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't think you should rush to strengthen, \x01",
            "but it is an indispensable component \x01",
            "of powering up your Orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_6402")


    ChrTalk(
        0x9,
        (
            ""Magic invoked using Tactical Orbments."\x01",
            "In other words, Orbal Arts, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "They're often referred to simply as "Arts."\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The kinds of Arts that can be invoked are\x01",
            "decided by the sum total of the attribute\x01",
            "values of the Quartz on each line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, the higher the attribute\x01",
            "values of the Quartz you have set,\x01",
            "the more Arts you'll be able to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, if you want to use high-\x01",
            "level Arts, you'll need to pay attention\x01",
            "to the attribute value combinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "All the detailed information regarding that\x01",
            "is in a list in your Detective Notebook,\x01",
            "so refer to it whenever you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_6670")


    ChrTalk(
        0x9,
        (
            "Inheriting the ENIGMA's communication\x01",
            "function, the successor model has been\x01",
            "boldly remodeled― That's the "ENIGMA II".\x02",
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
            "you can't set Quartz that could be\x01",
            "used with the old ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And so, you need new standard\x01",
            "Quartz for use with ENIGMA II.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_685B")


    ChrTalk(
        0x9,
        (
            "Master Quartz are special\x01",
            "Quartz that are inserted in\x01",
            "the center of your ENIGMA IIs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A definite difference from your usual Quartz\x01",
            "is that the Master Quartz itself "grows."\x02",
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
            "Strengthening the user, the Quartz's special\x01",
            "effect and the attribute values... Those\x01",
            "three components are affected by Quartz growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, to discover the true\x01",
            "powers of each Master Quartz, it seems\x01",
            "you need to bring them to max level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems it'll take a long \x01",
            "time to level them up, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It might be important to not mess around\x01",
            "and continue to use your favorite ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B18")

    label("loc_6B09")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B18")

    label("loc_6B18")

    Jump("loc_5CC3")

    label("loc_6B1D")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_5C8F end

    def Function_12_6B2B(): pass

    label("Function_12_6B2B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    def lambda_6B3C():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6B3C)

    def lambda_6B49():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6B49)
    TurnDirection(0xA, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B96")

    ChrTalk(
        0x8,
        "Ah, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd...\x01",
            "You're safe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BFC")

    label("loc_6B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6BBF")

    ChrTalk(
        0x9,
        (
            "Lloyd...\x01",
            "You're safe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BFC")

    label("loc_6BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6BFC")

    ChrTalk(
        0xA,
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd...\x01",
            "You're safe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BFC")


    ChrTalk(
        0x101,
        "#00000FYeah, somehow.\x02",
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
            "Umm, ahh, we'll support you as\x01",
            "much as we can with our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, be careful\x01",
            "if you're going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
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

    # Function_12_6B2B end

    def Function_13_6D55(): pass

    label("Function_13_6D55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6D66")
    Jump("loc_80E1")

    label("loc_6D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D84")
    SetScenarioFlags(0x0, 3)
    Call(0, 12)
    Jump("loc_6DF9")

    label("loc_6D84")


    ChrTalk(
        0xFE,
        (
            "In any case, this situation...\x01",
            "It's like pure chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what's going to\x01",
            "happen to our Crossbell now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DF9")

    Jump("loc_80E1")

    label("loc_6DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F10")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of Crossbell"...\x01",
            "For sure, it will make us enemies\x01",
            "of the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The natural result is that products\x01",
            "from the Reinford Corp. and Verne Corp.\x01",
            "will no longer be sold in our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahh, my head hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FB6")

    label("loc_6F10")


    ChrTalk(
        0xFE,
        (
            "I can't believe that we're asserting our\x01",
            "independence by halting economic activity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's going to be like this,\x01",
            "I can't agree with our independence...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FB6")

    Jump("loc_80E1")

    label("loc_6FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7073")

    ChrTalk(
        0xFE,
        (
            "The independence referendum\x01",
            "will be held in just three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that day, we plan to take turns watching the store,\x01",
            "so that each employee has a chance to vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E1")

    label("loc_7073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_71BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7144")

    ChrTalk(
        0xFE,
        (
            "Hmm, that occupation incident\x01",
            "has become an unusual situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been said if the Empire isn't\x01",
            "leading it behind the scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I hope it's resolved quickly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_71B6")

    label("loc_7144")


    ChrTalk(
        0xFE,
        (
            "It's been said if the Empire isn't\x01",
            "leading it behind the scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I hope it's resolved quickly.\x02",
    )

    CloseMessageWindow()

    label("loc_71B6")

    Jump("loc_80E1")

    label("loc_71BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7375")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72BE")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Chalk's father\x01",
            "came for an interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Worried about his daughter, he asked\x01",
            "me to let him work for us, but...\x02",
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
    Jump("loc_7370")

    label("loc_72BE")


    ChrTalk(
        0xFE,
        (
            "Worried about his daughter, he asked\x01",
            "me to let him work for us, but...\x02",
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

    label("loc_7370")

    Jump("loc_80E1")

    label("loc_7375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_73E2")

    ChrTalk(
        0xFE,
        (
            "I heard it from a customer.\x01",
            "They said a train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope everyone's all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80E1")

    label("loc_73E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74CD")

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
            "They dismissed the idea before\x01",
            "I even finished explaining it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I don't think it's\x01",
            "that bad an idea, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7560")

    label("loc_74CD")


    ChrTalk(
        0xFE,
        (
            "Hmm, I don't think it's\x01",
            "that bad an idea, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if those two are that opposed to it,\x01",
            "I suppose I'll have to give up on the idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7560")

    Jump("loc_80E1")

    label("loc_7565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C1")

    ChrTalk(
        0xFE,
        (
            "Mr. Guillaume once worked here, but we had a\x01",
            "difference of opinion regarding management\x01",
            "policies and decided to part ways, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking about it now, I might\x01",
            "have done something bad to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I'm late in realizing it, after\x01",
            "all is said and done, this business\x01",
            "only exists because of its employees.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_778F")

    label("loc_76C1")


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
            "That's right, even if it was just the interior...\x01",
            "It would be nice if it smelled\x01",
            "like the old Genten workshop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_778F")

    Jump("loc_80E1")

    label("loc_7794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7891")

    ChrTalk(
        0xFE,
        "So today is the Trade Conference's main session, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an important conference that will determine the future\x01",
            "of not just Crossbell's economy, but that of the whole\x01",
            "continent. So of course I'm concerned about the contents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E1")

    label("loc_7891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7920")

    ChrTalk(
        0xFE,
        "Good evening, and welcome to "Genten".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still some time until closing,\x01",
            "so please take your time and don't rush.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E1")

    label("loc_7920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A5E")

    ChrTalk(
        0xFE,
        (
            "*sigh*, that Wendy is\x01",
            "a troublesome one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think she'd abandon her work and rush\x01",
            "out with an orbal camera from the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I would've complained about it\x01",
            "if I was the same me as before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was no real obstacle to\x01",
            "our business though, I thought\x01",
            "that act was cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7B08")

    label("loc_7A5E")


    ChrTalk(
        0xFE,
        (
            "If I think that even using a demo\x01",
            "camera could be a way to advertise\x01",
            "its functions, I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll have her show me\x01",
            "the photos she took later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B08")

    Jump("loc_80E1")

    label("loc_7B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C3A")

    ChrTalk(
        0xFE,
        "Can I help you with anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for an orbal vacuum, \x01",
            "allow me to recommend this one,\x01",
            "Verne Corp.'s latest model.\x02",
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
    Jump("loc_7D29")

    label("loc_7C3A")


    ChrTalk(
        0xFE,
        (
            "If you are looking for an orbal vacuum, \x01",
            "allow me to recommend this one,\x01",
            "Verne Corp.'s latest model.\x02",
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

    label("loc_7D29")

    Jump("loc_80E1")

    label("loc_7D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB0")

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
            "Dear me, that Wendy of ours is\x01",
            "one amazing orbal engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried to learn some of her technical knowledge,\x01",
            "but being too complicated I don't get it at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7F40")

    label("loc_7EB0")


    ChrTalk(
        0xFE,
        (
            "Dear me, that Wendy of ours is\x01",
            "one amazing orbal engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone like me does it's best just\x01",
            "to memorize the superficial knowledge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F40")

    Jump("loc_80E1")

    label("loc_7F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_80E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8039")

    ChrTalk(
        0xFE,
        (
            "Hello, and welcome to\x01",
            "Orbal Store "Genten".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally, our store has all the\x01",
            "latest orbal goods, and we offer a\x01",
            "warmhearted local after-sale service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need any advice,\x01",
            "please feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_80E1")

    label("loc_8039")


    ChrTalk(
        0xFE,
        (
            "Naturally, our store has all the\x01",
            "latest orbal goods, and we offer a\x01",
            "warmhearted local after-sale service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need any advice,\x01",
            "please feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80E1")

    TalkEnd(0xFE)
    Return()

    # Function_13_6D55 end

    def Function_14_80E5(): pass

    label("Function_14_80E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_81B7")

    ChrTalk(
        0xFE,
        (
            "To be honest, I don't really feel like shopping, but...\x01",
            "I can't calm down at home, so I came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I want everything to resolve quickly \x01",
            "so I can get my everyday life back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_81B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_81C5")
    Jump("loc_8D1E")

    label("loc_81C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_828A")

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
            "It seems many things will be tough from now on,\x01",
            "but this middle age woman too felt she has to\x01",
            "do her best together with everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_828A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8367")

    ChrTalk(
        0xFE,
        (
            "I am normally disinterested in politics, however\x01",
            "the question of independence is a different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The more I think about recent\x01",
            "incidents in Crossbell, the more\x01",
            "I think it should be independent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_8367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_83D8")

    ChrTalk(
        0xFE,
        "An occupation incident... How scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too hope something can\x01",
            "be done about it, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_83D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84CB")

    ChrTalk(
        0xFE,
        (
            "If we become independent, we won't have to pay a\x01",
            "portion of our taxes to either of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given that, Crossbell's economy will\x01",
            "grow even faster than it already is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think that's important.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_858D")

    label("loc_84CB")


    ChrTalk(
        0xFE,
        (
            "If we become independent, we won't have to\x01",
            "pay taxes to either of the major powers.\x02",
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

    label("loc_858D")

    Jump("loc_8D1E")

    label("loc_8592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85C3")

    ChrTalk(
        0xFE,
        "My, it sure is noisy outside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_85C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C8")

    ChrTalk(
        0xFE,
        (
            "It seems Reinford Corp.\x01",
            "sells many high-capacity,\x01",
            "high-output goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the contrary, Verne Corp. sells many reasonably\x01",
            "priced goods with many different functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, this must reflect the character of each nation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8771")

    label("loc_86C8")


    ChrTalk(
        0xFE,
        (
            "Reinford Corp. focuses on high capacity\x01",
            "and output, and Verne Corp. focuses on\x01",
            "convenience and economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, this must reflect the character of each nation.\x02",
    )

    CloseMessageWindow()

    label("loc_8771")

    Jump("loc_8D1E")

    label("loc_8776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8825")

    ChrTalk(
        0xFE,
        (
            "I just found this out.\x01",
            "It seems ZCF makes the\x01",
            "most reliable devices.\x02",
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
    Jump("loc_8D1E")

    label("loc_8825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_88C8")

    ChrTalk(
        0xFE,
        (
            "Though at first glance they seem the same, the\x01",
            "manufacturer gives each device a unique personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, even I came\x01",
            "to understand that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_88C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_89B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8945")

    ChrTalk(
        0xFE,
        "My, it's already this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I've got to get home and\x01",
            "cook on my new orbal range.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_89B3")

    label("loc_8945")


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
            "but I'm glad I bought one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89B3")

    Jump("loc_8D1E")

    label("loc_89B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8B")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference? \x01",
            "Hmm, honestly, I'm not interested in\x01",
            "anything that directly involves me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But more importantly, look at this. \x01",
            "This new product, isn't it just so cute?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8AEC")

    label("loc_8A8B")


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

    label("loc_8AEC")

    Jump("loc_8D1E")

    label("loc_8AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8BD5")

    ChrTalk(
        0xFE,
        (
            "The manager here has gotten better informed\x01",
            "about his products over the past few months.\x02",
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
    Jump("loc_8D1E")

    label("loc_8BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8C63")

    ChrTalk(
        0xFE,
        "Orbal goods are just so fascinating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm not planning on buying anything,\x01",
            "I find myself coming to this store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1E")

    label("loc_8C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8D1E")

    ChrTalk(
        0xFE,
        (
            "Well look at that. The next generation of the\x01",
            "vacuum cleaner I bought is on sale already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww. If they had said something sooner,\x01",
            "I wouldn't have bought one back then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D1E")

    TalkEnd(0xFE)
    Return()

    # Function_14_80E5 end

    def Function_15_8D22(): pass

    label("Function_15_8D22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8D9B")

    ChrTalk(
        0xFE,
        (
            "Oh, Chalk...\x01",
            "My daughter, Chalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your father has been so worried\x01",
            "about you this whole time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_8D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8DA9")
    Jump("loc_991A")

    label("loc_8DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E69")

    ChrTalk(
        0xFE,
        (
            "Though they call themselves the\x01",
            ""State Guard"... I worry about\x01",
            "whether they can really protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But it's all right.\x01",
            "I will protect Chalk no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_8E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8F0A")

    ChrTalk(
        0xFE,
        (
            "Chalk forgave me, so we came\x01",
            "here together this morning too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You mean all the world to me, Chalk. \x01",
            "Your father will always protect you.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_8F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8FAC")

    ChrTalk(
        0xFE,
        (
            "To think an armed group\x01",
            "occupied Mainz... \x01",
            "W-What a disturbing story.\x02",
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
    Jump("loc_991A")

    label("loc_8FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_903A")

    ChrTalk(
        0xFE,
        (
            "Hmm, the manager\x01",
            "too is unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. In that case,\x01",
            "I'll come as a customer, \x01",
            "as I have up until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_903A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9094")

    ChrTalk(
        0xFE,
        (
            "A derailment, huh...?\x01",
            "They've happened before,\x01",
            "but they're quite rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_9094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_90F8")

    ChrTalk(
        0xFE,
        (
            "Today, I've decided to\x01",
            "interview for a position at\x01",
            "this store. I'm so nervous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_90F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921A")

    ChrTalk(
        0xFE,
        (
            "No matter what my daughter says,\x01",
            "Worrisome things are worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think I'll work here\x01",
            "as an orbal engineer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, at the end of the\x01",
            "day, I'm a designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can do simple maintenance all right, but... \x01",
            "Will the manager end up hiring me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_926E")

    label("loc_921A")


    ChrTalk(
        0xFE,
        (
            "Hmm. At the end of the day,\x01",
            "I'm a designer. Will the\x01",
            "manager end up hiring me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_926E")

    Jump("loc_991A")

    label("loc_9273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_92FD")

    ChrTalk(
        0xFE,
        (
            "Yesterday, when a fellow\x01",
            "got close to Chalk after work,\x01",
            "I warned him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I did that,\x01",
            "Chalk got very mad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_92FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_943B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D8")

    ChrTalk(
        0xFE,
        (
            "There's still some\x01",
            "time until closing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The roads at night are dangerous, so I\x01",
            "really want to walk Chalk home, but...\x02",
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
    Jump("loc_9436")

    label("loc_93D8")


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
        "I guess I'll go home for the day...\x02",
    )

    CloseMessageWindow()

    label("loc_9436")

    Jump("loc_991A")

    label("loc_943B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_950C")

    ChrTalk(
        0xFE,
        (
            "Wasn't that Wendy, Chalk's senior?\x01",
            "That girl heard the sound of an airship\x01",
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
    Jump("loc_991A")

    label("loc_950C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_958B")

    ChrTalk(
        0xFE,
        (
            "Hmm, though she's my daughter,\x01",
            "Chalk is quite the beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I worry that undesirables will approach her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_991A")

    label("loc_958B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_976C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96D7")

    ChrTalk(
        0xFE,
        (
            "The appearance of various\x01",
            "orbal goods reveals the values\x01",
            "of their manufacturers, but...\x02",
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
            "By the way, the Reinford Corp.\x01",
            "goes for a flashy appearance\x01",
            "and Verne Corp. goes for "pop".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9767")

    label("loc_96D7")


    ChrTalk(
        0xFE,
        (
            "Orbal goods have no need of useless\x01",
            "ornamentation, if you ask me.\x02",
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

    label("loc_9767")

    Jump("loc_991A")

    label("loc_976C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_991A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987E")

    ChrTalk(
        0xFE,
        (
            "Until last year,\x01",
            "I worked as an orbal\x01",
            "goods designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter secured a job and\x01",
            "my family's finances are in order,\x01",
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
    Jump("loc_991A")

    label("loc_987E")


    ChrTalk(
        0xFE,
        (
            "And so, today too I came\x01",
            "to see Chalk, my daughter,\x01",
            "working here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it seems she's doing\x01",
            "her best as usual. As her\x01",
            "father, I'm proud of her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_991A")

    TalkEnd(0xFE)
    Return()

    # Function_15_8D22 end

    def Function_16_991E(): pass

    label("Function_16_991E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_99F7")

    ChrTalk(
        0xFE,
        (
            "Orbal cars and terminals are fine, but they're\x01",
            "out of reach of most people, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems prices are steadily falling, but...\x01",
            "I wonder if they'll ever be in range of\x01",
            "ordinary families.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AB5")

    label("loc_99F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9AB5")

    ChrTalk(
        0xFE,
        (
            "Wah! It's the rumored notebook-\x01",
            "type orbal terminal. Now let's\x01",
            "check the price tag...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wow, that's a huge number of zeroes.\x01",
            "No way I could ever buy something like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AB5")

    TalkEnd(0xFE)
    Return()

    # Function_16_991E end

    def Function_17_9AB9(): pass

    label("Function_17_9AB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B68")

    ChrTalk(
        0xFE,
        (
            "To not ever forget Chalk,\x01",
            "I came here again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...That father of hers is still here, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, I give up. I'm going home.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9BC0")

    label("loc_9B68")


    ChrTalk(
        0xFE,
        "...That father of hers is still here, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, I give up. I'm going home.\x02",
    )

    CloseMessageWindow()

    label("loc_9BC0")

    Jump("loc_9F52")

    label("loc_9BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C4E")

    ChrTalk(
        0xFE,
        (
            "It's almost closing time, huh?\x01",
            "There's still a lot of\x01",
            "customers, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Should I talk to her?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9CA0")

    label("loc_9C4E")


    ChrTalk(
        0xFE,
        (
            "I'll muster my\x01",
            "courage, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I've got to\x01",
            "calm down and think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA0")

    Jump("loc_9F52")

    label("loc_9CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D9D")

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
            "seems she's named "Chalk".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A very cute name that\x01",
            "suits her appearance!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9E05")

    label("loc_9D9D")


    ChrTalk(
        0xFE,
        "I don't care about the inauguration ceremony!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just seeing that girl's\x01",
            "smile is enough for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E05")

    Jump("loc_9F52")

    label("loc_9E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EDA")

    ChrTalk(
        0xFE,
        "Hmm, this store is really amazing!\x02",
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
            "Muhuhu, that engineer girl\x01",
            "is cute too, but the sales\x01",
            "counter girl is more my type㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9F52")

    label("loc_9EDA")


    ChrTalk(
        0xFE,
        (
            "Hmm, I guess this is an\x01",
            "unexpected reward for my trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll let me take\x01",
            "her picture if I asked?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F52")

    TalkEnd(0xFE)
    Return()

    # Function_17_9AB9 end

    def Function_18_9F56(): pass

    label("Function_18_9F56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9FE7")

    ChrTalk(
        0xFE,
        (
            "Hmm, an unsettling incident\x01",
            "has occurred for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll cut the trip's schedule short\x01",
            "and I'll go home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27C")

    label("loc_9FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A0A3")

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
            "are very good at\x01",
            "dealing with accidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27C")

    label("loc_A0A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A104")

    ChrTalk(
        0xFE,
        (
            "Hmm, those sounds just now\x01",
            "were sirens. Sounds you\x01",
            "want to not hear at all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27C")

    label("loc_A104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A1BA")

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
            "Though the function is the same, the\x01",
            "shapes are different depending on the\x01",
            "manufacturer. That's quite interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27C")

    label("loc_A1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A27C")

    ChrTalk(
        0xFE,
        (
            "Hmm, this store has a good balance of\x01",
            "orbal goods from different manufacturers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's Crossbell for you. They don't call this\x01",
            "the continent's leading trade city for nothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A27C")

    TalkEnd(0xFE)
    Return()

    # Function_18_9F56 end

    def Function_19_A280(): pass

    label("Function_19_A280")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A365")

    ChrTalk(
        0xFE,
        "Just what is going on...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, if I went home,\x01",
            "I wouldn't have anything to eat,\x01",
            "so it's better to stay here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I have nothing to do, so I might\x01",
            "as well servicing the air pump.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A3D7")

    label("loc_A365")


    ChrTalk(
        0xFE,
        "Just what is going on...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I have nothing to do, so I\x01",
            "might as well servicing the air pump.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3D7")

    TalkEnd(0xFE)
    Return()

    # Function_19_A280 end

    def Function_20_A3DB(): pass

    label("Function_20_A3DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A479")

    ChrTalk(
        0xFE,
        "Photo Quartz, photo Quartz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's not that many of the latest model.\x01",
            "Will I be able to get by with just two or three?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_A519")

    label("loc_A479")


    ChrTalk(
        0xFE,
        (
            "I came to buy photo Quartz in\x01",
            "preparation for tomorrow's\x01",
            "inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as luck would have it, they're\x01",
            "sold out, and it's a huge problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A519")

    TalkEnd(0xFE)
    Return()

    # Function_20_A3DB end

    def Function_21_A51D(): pass

    label("Function_21_A51D")

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
            "#11PAnd you guys... I don't\x01",
            "recognize you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, these members\x01",
            "just started with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FHow do you do.\x01",
            "I'm Noｱl Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWazy Hemisphere. It's a pleasure.\x02\x03",
            "#10300FBy the way, don't you and\x01",
            "Lloyd go way back?\x02\x03",
            "If you want, next time you could\x01",
            "tell me some juicy details about\x01",
            "Lloyd's childhood...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11PUh uh, yeah! I'll bet you want\x01",
            "to catch his weaknesses, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FW-What're you talking about...\x02\x03",
            "#00000FAnyway, can we get back\x01",
            "on topic now please?\x02\x03",
            "Weren't you going to train\x01",
            "us on these ENIGMA IIs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh, I totally forgot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P*ahem*, well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAs I'm sure you're all aware,\x01",
            "you are now using the brand-\x01",
            "new ENIGMA II units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's the latest version of\x01",
            "the technology released by\x01",
            "the Epstein Foundation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe main difference is the center\x01",
            "slot in the middle of the unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Quartz that is used\x01",
            "in this slot is called\x01",
            ""Master Quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, they're Quartz with a\x01",
            "pattern engraved on them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThose are them. They're big and spherical.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA Master Quartz's main\x01",
            "difference from a normal\x01",
            "one is that it "grows."\x02",
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
            "#6P#10100FWhat to say...\x01",
            "It feels kind of surreal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYes, it's as if the Master\x01",
            "Quartz is actually alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, I'm assuming\x01",
            "we're about to hear the\x01",
            "story behind that next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAh, well, sorry, but I'm\x01",
            "not a researcher and I\x01",
            "don't know those details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRather than it grows, I get\x01",
            "this image of drawing out\x01",
            "the Quartz's hidden power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, that aside, I can at least\x01",
            "tell you what you need to know about\x01",
            "how to use your ENIGMA II units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PNot the theory behind them, but how to use them practically.\x02",
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
        "#6P#00105FSo this is a Master Quartz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThere's no question it has a different\x01",
            "feel to it than a normal Quartz.\x02\x03",
            "#10300FBut is it really okay for us to have these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYes, they were given to\x01",
            "me by CSPD HQ to give\x01",
            "to you in the first place.\x02",
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
            "from the Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBasically, we're able to sell only\x01",
            "one Master Quartz of each type,\x01",
            "so please be careful with them.\x02",
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
            "#6P#00005FSo do you have any practical tips for\x01",
            "us before we give them a shot, Wendy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRight. First, can\x01",
            "you all please equip\x01",
            "your Master Quartz?\x02",
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
            "#11PIn other words, a Master Quartz can\x01",
            "be set regardless of the person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FI see. That's rather convenient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, well what are we waiting\x01",
            "for then, let's set them in.\x02",
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
            "Quest [ENIGMA II Training]\x07\x00",
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

    # Function_21_A51D end

    def Function_22_B314(): pass

    label("Function_22_B314")

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
            "#11POk great, everyone\x01",
            "has a Master\x01",
            "Quartz set.\x02",
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
            "#11PUh uh, it's simple── I want you to\x01",
            "see the power of Master Quartz for\x01",
            "yourselves in a practical test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FYou mean you want us\x01",
            "to fight with them?\x02",
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
            "#6P#00005FBy the way, are there any specific requirements,\x01",
            "like a location or number of battles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo, nothing special. The location\x01",
            "and opponent is up to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PJust beat one battle and don't run away.\x01",
            "That'll be good enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHu hu, well, I think we can manage that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FLloyd, do you have any ideas on where we should go?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B757")

    ChrTalk(
        0x101,
        (
            "#6P#00003FHmm, I'd like to stay in the\x01",
            "city for the time being...\x02\x03",
            "#00000FThe monsters in Maison Imelda\x01",
            "might be the perfect opponents.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_B806")

    label("loc_B757")


    ChrTalk(
        0x101,
        (
            "#6P#00003FOh yeah, we have a request to clear\x01",
            "out some monsters that are roaming\x01",
            "around Maison Imelda, don't we?\x02\x03",
            "#00000FIt'll be like killing two\x01",
            "birds with one stone.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B806")


    ChrTalk(
        0x109,
        (
            "#6P#10100FIt certainly would be an\x01",
            "easy way to test them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PUh uh, looks like you've\x01",
            "decided on a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PActually, please take\x01",
            "this Quartz with you too.\x02",
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
        "#11PYes, that's another gift from HQ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you set it in a normal slot,\x01",
            "you'll be able to use the new\x01",
            "ENIGMA II Art, "Analyze".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHe who controls information,\x01",
            "controls the battle, they say.\x01",
            "Be my guest and test it out in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, got it.\x02\x03",
            "#00003F(Now that Tio's not around... \x01",
            "We'll need to rely on Arts to\x01",
            "get enemy info for a while.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell then,\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd don't forget that you can\x01",
            "always count on me for orbment\x01",
            "remodeling and Quartz synthesis!\x02",
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
            "※By speaking to Wendy and selecting\x01",
            ""Remodel - Synthesize", you can \x01",
            "synthesize new Quartz or unseal \x01",
            "or enhance tactical orbment slots.\x02\x03",
            "※By synthesizing new Quartz and equipping\x01",
            "them, you'll be able to use various Arts.\x02\x03",
            "※By opening or enhancing slots,\x01",
            "you can equip more Quartz, and\x01",
            "your maximum EP also increases.\x02\x03",
            "※To use those functions, septium fragments\x01",
            "called "Sepith" are required. (Sepith is\x01",
            "obtained mainly from defeating monsters.)\x07\x00\x02",
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

    # Function_22_B314 end

    def Function_23_BD4F(): pass

    label("Function_23_BD4F")

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
            "Miss Elie and Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FWell actually I was pretty surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, I never thought we'd\x01",
            "be able to get so much power\x01",
            "out of a single Quartz.\x02\x03",
            "#10300FTo be honest, it exceeded my expectations.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0CC")

    ChrTalk(
        0x9,
        "#11PUh uh, that's the reaction I was hoping for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, something special happens\x01",
            "when you grow them to their final stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBut I think I'll let you\x01",
            "guys discover it as you go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FWow, there's still more\x01",
            "surprises left in this thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHa ha, well that's something to look forward to.\x02\x03",
            "#00000FSo, will that be all\x01",
            "for today's training?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1D0")

    label("loc_C0CC")


    ChrTalk(
        0x9,
        "#11PUh uh, that's the reaction I was hoping for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI want to send it to the Epstein\x01",
            "Foundation development staff, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHa ha, I've got to give you credit here. \x01",
            "That wasn't too bad.\x02\x03",
            "#00000FSo, will that be all\x01",
            "for today's training?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1D0")


    ChrTalk(
        0x9,
        (
            "#11PYeah, I'll send my\x01",
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
        "#11POr anything you want to hear again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FLet's see...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C2BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D17F")

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
            "About the ENIGMA II\x01",            # 5
            "About Master Quartz\x01",            # 6
            "Quit\x01",                           # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C3A6"),
        (1, "loc_C5A1"),
        (2, "loc_C711"),
        (3, "loc_C87A"),
        (4, "loc_CA1C"),
        (5, "loc_CCA2"),
        (6, "loc_CEA1"),
        (SWITCH_DEFAULT, "loc_D16B"),
    )


    label("loc_C3A6")


    ChrTalk(
        0x9,
        (
            "#11P#11P"Tactical Orbments" are small, \x01",
            "portable orbal devices\x01",
            "specialized for use in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#11PIn addition to strengthening the user, they\x01",
            "support the user with the use of Arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey're usually simply\x01",
            "called "Orbments".\x02",
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
            "the shape of the connecting lines differs.\x01",
            "It might be good to compare them once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_C5A1")


    ChrTalk(
        0x9,
        (
            "#11PQuartz are "crystal circuits" for use\x01",
            "in Orbments made by smelting Sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you bring the required Sepith,\x01",
            "we can synthesize the Quartz here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PDepending on the Quartz, there are various\x01",
            "effects, and when the property values are over\x01",
            " fixed number, Arts become able to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWhen you've gathered some Sepith, give it a try.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_C711")


    ChrTalk(
        0x9,
        (
            "#11POrbment slots are, from the\x01",
            "start, sealed for the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn order to set a Quartz,\x01",
            "first you need an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you open a slot, the number\x01",
            "of Quartz you can use increases,\x01",
            "as well as your maximum EP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough you need Sepith to open slots, it'll be pretty\x01",
            "useful for you. I think you should proactively open them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_C87A")


    ChrTalk(
        0x9,
        (
            "#11PAmong Quartz, some are\x01",
            "designated "High-Rank Quartz".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey're too strong, so you\x01",
            "can't set them in normal slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat you need to do is\x01",
            "strengthen the slot itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou need Sepith to do that, and your maximum\x01",
            "EP increases, the same as with sealed slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI don't think you should rush to strengthen, \x01",
            "but it is an indispensable component \x01",
            "of powering up your Orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_CA1C")


    ChrTalk(
        0x9,
        (
            "#11P"Magic invoked using Tactical Orbments."\x01",
            "In other words, Orbal Arts, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThey're often referred to simply as "Arts."\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe kinds of Arts that can be invoked are\x01",
            "decided by the sum total of the attribute\x01",
            "values of the Quartz on each line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn other words, the higher the attribute\x01",
            "values of the Quartz you have set,\x01",
            "the more Arts you'll be able to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, if you want to use high-\x01",
            "level Arts, you'll need to pay attention\x01",
            "to the attribute value combinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAll the detailed information regarding that\x01",
            "is in a list in your Detective Notebook,\x01",
            "so refer to it whenever you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_CCA2")


    ChrTalk(
        0x9,
        (
            "#11PInheriting the ENIGMA's communication\x01",
            "function, the successor model has been\x01",
            "boldly remodeled― That's the "ENIGMA II".\x02",
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
            "you can't set Quartz that could be\x01",
            "used with the old ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd so, you need new standard\x01",
            "Quartz for use with ENIGMA II.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_CEA1")


    ChrTalk(
        0x9,
        (
            "#11PMaster Quartz are special\x01",
            "Quartz that are inserted in\x01",
            "the center of your ENIGMA IIs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA definite difference from your usual Quartz\x01",
            "is that the Master Quartz itself "grows."\x02",
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
            "#11PStrengthening the user, the Quartz's special\x01",
            "effect and the attribute values... Those\x01",
            "three components are affected by Quartz growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, to discover the true\x01",
            "powers of each Master Quartz, it seems\x01",
            "you need to bring them to max level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt seems it'll take a long \x01",
            "time to level them up, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt might be important to not mess around\x01",
            "and continue to use your favorite ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17A")

    label("loc_D16B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D17A")

    label("loc_D17A")

    Jump("loc_C2BB")

    label("loc_D17F")


    ChrTalk(
        0x101,
        (
            "#6P#00004F...That's plenty I think.\x02\x03",
            "#00000FThank you so much Wendy.\x01",
            "We really learned a ton today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PUh uh, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh by the way, here's a new\x01",
            "standard ENIGMA II Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PConsider it a gift in celebration\x01",
            "of the restart of SSS activities.\x02",
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
            "We'll put it to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FReally. You were a huge help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PUh uh, you're welcome.\x02",
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
            "counter next to me as well...\x02",
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
        "#6P#10302FHu hu, will do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FThank you very much\x01",
            "for your help today!\x02",
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
            "Quest [ENIGMA II Training]\x07\x00",
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

    # Function_23_BD4F end

    def Function_24_D584(): pass

    label("Function_24_D584")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-6460, 1500, 2290, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D6FE")
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

    def lambda_D64F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D64F)

    def lambda_D660():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D660)

    def lambda_D675():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D675)

    def lambda_D686():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D686)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D6AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D6AF)

    def lambda_D6C0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6C0)
    Sleep(100)

    def lambda_D6D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D6D8)

    def lambda_D6E9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D6E9)
    Jump("loc_D979")

    label("loc_D6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D83E")
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

    def lambda_D78F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D78F)

    def lambda_D7A0():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D7A0)

    def lambda_D7B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D7B5)

    def lambda_D7C6():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7C6)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D7EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D7EF)

    def lambda_D800():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D800)
    Sleep(100)

    def lambda_D818():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D818)

    def lambda_D829():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D829)
    Jump("loc_D979")

    label("loc_D83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D979")
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

    def lambda_D8CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_D8CF)

    def lambda_D8E0():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D8E0)

    def lambda_D8F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D8F5)

    def lambda_D906():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D906)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_D92F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D92F)

    def lambda_D940():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D940)
    Sleep(100)

    def lambda_D958():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D958)

    def lambda_D969():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D969)

    label("loc_D979")

    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        (
            "So this is the orbal store\x01",
            "that appeared in all those\x01",
            "magazines, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It has a nice interior and practically\x01",
            "all the goods are cutting edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I don't think there's a store of\x01",
            "this scale in the Republic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it's very like Crossbell to\x01",
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
            "orbal net terminal.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DB7C")

    def lambda_DB5F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB5F)
    Sleep(50)

    def lambda_DB6F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DB6F)
    Jump("loc_DBCD")

    label("loc_DB7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DBA7")

    def lambda_DB8A():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB8A)
    Sleep(50)

    def lambda_DB9A():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DB9A)
    Jump("loc_DBCD")

    label("loc_DBA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_DBCD")

    def lambda_DBB5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DBB5)
    Sleep(50)

    def lambda_DBC5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBC5)

    label("loc_DBCD")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah. To put it simply, it's an\x01",
            "advanced communication device.\x02\x03",
            "#00004FThe entire project is\x01",
            "progressing led by the\x01",
            "Epstein Foundation...\x02\x03",
            "#00000FBy using a terminal, you can\x01",
            "transmit not just your voice, but\x01",
            "letters and pictures as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "W-Wow... So you can do\x01",
            "those sort of things?\x02",
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
            "H-Hmph, I'm not\x01",
            "surprised or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Displaying this level of\x01",
            "knowledge is just showing off!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_DE5F")
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
            "#6P#00006FWell, I'm not\x01",
            "showing off or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FHah, the brat can't be honest, huh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E006")

    label("loc_DE5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_DF45")
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
            "#6P#00006FWell, I'm not\x01",
            "showing off or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRather than not being honest, maybe\x01",
            "you should say he hates to lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E006")

    label("loc_DF45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E006")
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
            "#6P#00006FWell, I'm not\x01",
            "showing off or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHu hu, he hates to\x01",
            "lose, doesn't he.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E006")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 5)
    OP_29(0x73, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4800, 0, 2530, 90)
    EventEnd(0x5)
    Return()

    # Function_24_D584 end

    def Function_25_E032(): pass

    label("Function_25_E032")

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
        "Oh, Lloyd. Need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Wouldn't she make a fine\x01",
            ""craftman" for the pageant?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm, she's not into this\x01",
            "sort of things. But, since\x01",
            "we're here, I'll ask her.)\x02\x03",
            "#00000F...Wendy, do you have a minute?\x02",
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
            "#00306FNo, no, no. That's totally\x01",
            "not it, dear Wendy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAs expected from those on her profession...\x01",
            "So ignorant of the outside world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahaha, I kid, I kid.\x01",
            "I know what a\x01",
            "beauty contest is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, interesting...\x01",
            "So I can participate?\x02",
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
            "#10102FHa ha, I'm surprised. I never\x01",
            "expected an OK from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, nothing ventured nothing gained.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's a request from my childhood friend,\x01",
            "I'll help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got work to do until the\x01",
            "program starts, so call me\x01",
            "when you need me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, will do.\x01",
            "Thanks, Wendy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E2")

    ChrTalk(
        0x101,
        (
            "#00000F──Alright. With this we've\x01",
            "finally filled our quota.\x02\x03",
            "Let's head to City Meeting Hall and\x01",
            "report to Mr. Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_E5E2")

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

    # Function_25_E032 end

    def Function_26_E615(): pass

    label("Function_26_E615")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, we can't leave\x01",
            "the store right now.\x02\x03",
            "Let's speak with Wendy once\x01",
            "we've set the Master Quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 0, 2230, 90)
    EventEnd(0x4)
    Return()

    # Function_26_E615 end

    SaveToFile()

Try(main)
