from ScenarioHelper import *

def main():
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
        "Chaco",                 # 1
        "Wendy",             # 2
        "Fernando",           # 3
        "Midget",               # 4
        "Basilio",               # 5
        "Haas",                 # 6
        "Citizen",                   # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "Raines",               # 10
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
        "Function_5_A90",          # 05, 5
        "Function_6_2701",         # 06, 6
        "Function_7_2F12",         # 07, 7
        "Function_8_3B19",         # 08, 8
        "Function_9_3B23",         # 09, 9
        "Function_10_3FBE",        # 0A, 10
        "Function_11_5A0B",        # 0B, 11
        "Function_12_6729",        # 0C, 12
        "Function_13_6988",        # 0D, 13
        "Function_14_7AE4",        # 0E, 14
        "Function_15_8555",        # 0F, 15
        "Function_16_90FE",        # 10, 16
        "Function_17_924A",        # 11, 17
        "Function_18_96AA",        # 12, 18
        "Function_19_9937",        # 13, 19
        "Function_20_9A8A",        # 14, 20
        "Function_21_9B8E",        # 15, 21
        "Function_22_A937",        # 16, 22
        "Function_23_B2E9",        # 17, 23
        "Function_24_C8E3",        # 18, 24
        "Function_25_D360",        # 19, 25
        "Function_26_D910",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B")

    ChrTalk(
        0x8,
        (
            "Welcome to ☆\x01",
            "This is your purchase counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "あ、皆さんはWendy先輩の\x01",
            "It is people of acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, here new\x01",
            "I got the enigma cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, once you purchase it,\x01",
            "Subsequent cover replacement is always available\x01",
            "Because we accept it free of charge ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "もうじゃんじゃん、Chacoのことを\x01",
            "Please do not stick around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 4)

    label("loc_85B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8C")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94B")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                            # 0
            "Purchase and exchange an enigma cover\x01",      # 1
            "Purchase Master Quartz\x01",          # 2
            "Purchase a power train option\x01",          # 3
            "quit\x01",                              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_946")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_946")

    Jump("loc_9E0")

    label("loc_94B")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                            # 0
            "Purchase and exchange an enigma cover\x01",      # 1
            "Purchase Master Quartz\x01",          # 2
            "quit\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A25")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A87")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A6B")
    OP_AF(0xC0)
    Jump("loc_A7D")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A7B")
    OP_AF(0xBF)
    Jump("loc_A7D")

    label("loc_A7B")

    OP_AF(0xBE)

    label("loc_A7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A87")

    Jump("loc_865")

    label("loc_A8C")

    TalkEnd(0x8)
    Return()

    # Function_4_6C3 end

    def Function_5_A90(): pass

    label("Function_5_A90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2700")
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
        "Which one do you exchange?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB6")
    MenuCmd(1, 0, "Wearing CPD (Lloyd)")
    Jump("loc_BD8")

    label("loc_BB6")

    MenuCmd(1, 0, "Exchange CPD (Lloyd)")

    label("loc_BD8")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_C1A")
    MenuCmd(1, 0, "Blue Sheriff on board")
    Jump("loc_C6C")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_C4A")
    MenuCmd(1, 0, "Blue Sherif replace")
    Jump("loc_C6C")

    label("loc_C4A")

    MenuCmd(1, 0, "Blue Sheriff 1000 Mira")

    label("loc_C6C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_CA4")
    MenuCmd(1, 0, "Howling wolf installed")
    Jump("loc_CF6")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_CD4")
    MenuCmd(1, 0, "Change howling wolf")
    Jump("loc_CF6")

    label("loc_CD4")

    MenuCmd(1, 0, "Howling Wolf 1000 Mira")

    label("loc_CF6")

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
    Jump("loc_DA5")

    label("loc_D87")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE9")
    MenuCmd(1, 0, "Wearing CPD (Ellie)")
    Jump("loc_E0B")

    label("loc_DE9")

    MenuCmd(1, 0, "Exchange CPD (Eiry)")

    label("loc_E0B")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_E4D")
    MenuCmd(1, 0, "Wearing piece green")
    Jump("loc_E9F")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_E7D")
    MenuCmd(1, 0, "Piece green exchange")
    Jump("loc_E9F")

    label("loc_E7D")

    MenuCmd(1, 0, "Peace Green 1000 Mira")

    label("loc_E9F")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_ED7")
    MenuCmd(1, 0, "Spring bird installed")
    Jump("loc_F29")

    label("loc_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_F07")
    MenuCmd(1, 0, "Replace spring bird")
    Jump("loc_F29")

    label("loc_F07")

    MenuCmd(1, 0, "Spring Bird 1000 Mira")

    label("loc_F29")

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
    Jump("loc_FBA")

    label("loc_F9C")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FFE")
    MenuCmd(1, 0, "Wearing CPD (Tio)")
    Jump("loc_1020")

    label("loc_FFE")

    MenuCmd(1, 0, "Exchange CPD (Tio)")

    label("loc_1020")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_1064")
    MenuCmd(1, 0, "Black Cat replaced")
    Jump("loc_10B6")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_1094")
    MenuCmd(1, 0, "Exchange black cat")
    Jump("loc_10B6")

    label("loc_1094")

    MenuCmd(1, 0, "Black Cat 1000 Mira")

    label("loc_10B6")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_10EE")
    MenuCmd(1, 0, "Shadow circle installed")
    Jump("loc_1140")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_111E")
    MenuCmd(1, 0, "Shadow circle exchange")
    Jump("loc_1140")

    label("loc_111E")

    MenuCmd(1, 0, "Shadow Circle 1000 Mira")

    label("loc_1140")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_11B3")

    label("loc_1195")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_136E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F7")
    MenuCmd(1, 0, "Wearing CPD (Randy)")
    Jump("loc_1219")

    label("loc_11F7")

    MenuCmd(1, 0, "Exchange CPD (Randy)")

    label("loc_1219")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_125B")
    MenuCmd(1, 0, "Danger orange installed")
    Jump("loc_12AD")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_128B")
    MenuCmd(1, 0, "Exchange Danger Orange")
    Jump("loc_12AD")

    label("loc_128B")

    MenuCmd(1, 0, "Danger Orange 1000 Mira")

    label("loc_12AD")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_12E5")
    MenuCmd(1, 0, "Midnight kiss on board")
    Jump("loc_1337")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_1315")
    MenuCmd(1, 0, "Midnight kiss to exchange")
    Jump("loc_1337")

    label("loc_1315")

    MenuCmd(1, 0, "Midnight kiss 1000 Mira")

    label("loc_1337")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_138C")

    label("loc_136E")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_149A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CB")
    MenuCmd(1, 0, "Wearing CGF (Noel)")
    Jump("loc_13ED")

    label("loc_13CB")

    MenuCmd(1, 0, "Exchange CGF (Noel)")

    label("loc_13ED")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_1425")
    MenuCmd(1, 0, "Liberty Road installed")
    Jump("loc_1477")

    label("loc_1425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_1455")
    MenuCmd(1, 0, "Exchange Liberty Road")
    Jump("loc_1477")

    label("loc_1455")

    MenuCmd(1, 0, "Liberty Road 1000 Mira")

    label("loc_1477")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_149A")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14ED")
    MenuCmd(1, 0, "Wearing white creed")
    Jump("loc_150F")

    label("loc_14ED")

    MenuCmd(1, 0, "Exchange white creed")

    label("loc_150F")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_1547")
    MenuCmd(1, 0, "Crest face is being worn")
    Jump("loc_1599")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_1577")
    MenuCmd(1, 0, "Crest face replacement")
    Jump("loc_1599")

    label("loc_1577")

    MenuCmd(1, 0, "Crest Face 1000 Mira")

    label("loc_1599")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_15BC")

    label("loc_15A8")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BC")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15EF")
    Sleep(1)
    Return()

    label("loc_15EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_162D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_19CA")

    label("loc_166B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_19CA")

    label("loc_16A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_16E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1725")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_19CA")

    label("loc_1725")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1763")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_19CA")

    label("loc_1763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_17A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_19CA")

    label("loc_17DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_19CA")

    label("loc_181D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_185B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1899")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_19CA")

    label("loc_1899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_19CA")

    label("loc_18D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_19CA")

    label("loc_1915")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1953")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_19CA")

    label("loc_1953")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1991")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_19CA")

    label("loc_1991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CA")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_19CA")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A99")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Lloyd.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B3A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Ellie only.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BDB")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Tio.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C7E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Randy.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D17")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Noel.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1D17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DA9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for wadi.\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA9")


    AnonymousTalk(
        0x8,
        "Yes, is this OK?\x02",
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
            "【Asking for exchange】\x01",      # 0
            "【I will stop it】\x01",      # 1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E3")
    ClearScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6A")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E83")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBB")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED4")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1EED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F0C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F25")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3E")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F5D")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F76")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8F")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA9")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC2")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FDC")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FF0")
    SetScenarioFlags(0x1, 1)

    label("loc_1FF0")

    ClearScenarioFlags(0x1, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2008")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2008")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203A")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_203A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_204F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2068")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2068")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2081")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2081")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2096")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2096")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20AF")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C8")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F6")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_210F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2124")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2124")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213D")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_213D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2152")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2152")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2166")
    SetScenarioFlags(0x1, 2)

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_21B3")

    ChrTalk(
        0x8,
        (
            "That ~ is already wearing it?\x01",
            "Please choose another one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2214")

    ChrTalk(
        0x8,
        (
            "It seems that Mira is not enough?\x01",
            "Then we can not exchange it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_2214")


    ChrTalk(
        0x8,
        (
            "I understand.\x01",
            "Please wait a moment ~ Eruption\x02",
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
        "Yes, I will keep you waiting.\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2329")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Lloyd's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22EC")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_2324")

    label("loc_22EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2306")
    SetScenarioFlags(0x2C, 0)

    label("loc_2306")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_2324")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231E")
    SetScenarioFlags(0x2C, 1)

    label("loc_231E")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_2324")

    Jump("loc_261C")

    label("loc_2329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23D9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Elie 's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238A")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_23D4")

    label("loc_238A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23AD")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23AD")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_23D4")

    label("loc_23B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CE")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23CE")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_23D4")

    Jump("loc_261C")

    label("loc_23D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2489")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged Tio's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243A")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_2484")

    label("loc_243A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245D")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_245D")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_2484")

    label("loc_2468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_247E")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_2484")

    Jump("loc_261C")

    label("loc_2489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_253B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Randy 's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EC")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_2536")

    label("loc_24EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250F")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_250F")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_2536")

    label("loc_251A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2530")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2530")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_2536")

    Jump("loc_261C")

    label("loc_253B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25AF")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged noel's enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2591")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_25AA")

    label("loc_2591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A7")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25A7")

    SetScenarioFlags(0x2F, 0)

    label("loc_25AA")

    Jump("loc_261C")

    label("loc_25AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_261C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged wadi's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2603")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_261C")

    label("loc_2603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2619")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2619")

    SetScenarioFlags(0x2E, 4)

    label("loc_261C")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2693")
    OP_E0(0x16, 0x0)

    label("loc_2693")


    ChrTalk(
        0x8,
        (
            "Hehe, use of\x01",
            "We look forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D4")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_26D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26ED")

    label("loc_26E3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26ED")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_A9A")

    label("loc_2700")

    Return()

    # Function_5_A90 end

    def Function_6_2701(): pass

    label("Function_6_2701")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_270B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F11")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('白金', 0x4)"), scpexpr(EXPR_END)), "loc_274D")
    MenuCmd(1, 0, "Platinum purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_2769")

    label("loc_274D")

    MenuCmd(1, 0, "Platinum 1000 Mira")

    label("loc_2769")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('幻象', 0x4)"), scpexpr(EXPR_END)), "loc_2799")
    MenuCmd(1, 0, "Mirage purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_27B5")

    label("loc_2799")

    MenuCmd(1, 0, "Mirage 5000 Mira")

    label("loc_27B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_285B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('神佑', 0x4)"), scpexpr(EXPR_END)), "loc_27F3")
    MenuCmd(1, 0, "Aegis purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_280F")

    label("loc_27F3")

    MenuCmd(1, 0, "Aegis 20000 Mira")

    label("loc_280F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('王权', 0x4)"), scpexpr(EXPR_END)), "loc_283F")
    MenuCmd(1, 0, "Buyer purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_285B")

    label("loc_283F")

    MenuCmd(1, 0, "Scepter 50000 Mira")

    label("loc_285B")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_289A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_289A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28B7")
    Sleep(1)
    Return()

    label("loc_28B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_29B2")

    label("loc_28F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2937")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_29B2")

    label("loc_2937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2977")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_29B2")

    label("loc_2977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B2")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_29B2")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A43")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Master quartz with sky attribute.\x01",
            "* HP / ADF reinforced type · HP recovery when stabbing the enemy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA6")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a phantom attribute master quartz.\x01",
            "※ EP / ATS reinforced type · Episodic recovery by stabbing the enemy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is master quartz of earth attribute.\x01",
            "※ DEF / ADF reinforced type · \"complete defense\" effect under specified conditions\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B69")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is Master Quartz with water attribute.\x01",
            "※ STR / ATS reinforced type · Sepis obtained for each attack\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B69")


    AnonymousTalk(
        0x8,
        "Yes, is this OK?\x02",
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
            "【Purchase】\x01",        # 0
            "【I will stop it】\x01",      # 1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0x8,
        (
            "It seems that Mira is not enough?\x01",
            "Then you can not purchase.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE5")

    label("loc_2CA5")


    ChrTalk(
        0x8,
        (
            "I understand.\x01",
            "Please wait a moment ~ Eruption\x02",
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
        "Yes, I will keep you waiting.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '白金'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('白金', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2D7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE8")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '幻象'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('幻象', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E52")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '神佑'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神佑', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2E52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '王权'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('王权', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2EB7")


    ChrTalk(
        0x8,
        (
            "Hehe, use of\x01",
            "We look forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2EE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EFE")

    label("loc_2EF4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EFE")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_270B")

    label("loc_2F11")

    Return()

    # Function_6_2701 end

    def Function_7_2F12(): pass

    label("Function_7_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA2")

    ChrTalk(
        0x8,
        (
            "Daddy will always stare at you\x01",
            "Chaco、穴が開いちゃいそうです……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But I wonder how worried you are so much\x01",
            "It is appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_2FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_30BC")

    ChrTalk(
        0x8,
        (
            "When martial law was issued,\x01",
            "店長からChacoは帰るように\x01",
            "I was instructed, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wendy先輩がもしもの時のための\x01",
            "As it was a story that it would remain as a human hand,\x01",
            "Chacoも留まることにしたんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A little bad thing to Dad\x01",
            "I feel I did it,\x01",
            "You surely understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_30BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_313A")

    ChrTalk(
        0x8,
        (
            "President Dieter's speech ……\x01",
            "It was awesome force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Chaco、聞いている最中に\x01",
            "I stopped breath in spite of myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_313A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31CE")

    ChrTalk(
        0x8,
        (
            "During this week, both at work and at home\x01",
            "I am with Daddy for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's just like this\x01",
            "It's cash, but I guarantee it all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3241")

    ChrTalk(
        0x8,
        "People in Mainz are really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How come this is\x01",
            "I wonder what happened ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3328")

    ChrTalk(
        0x8,
        (
            "Yesterday, my father died\x01",
            "Interview of our store\x01",
            "It seems that he received it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Papa has technology as a technician\x01",
            "There is no reason, of course\x01",
            "I heard he was not accepting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "うう、Chaco恥ずかしいですぅ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3390")

    label("loc_3328")


    ChrTalk(
        0x8,
        (
            "Dad is the shop in our house\x01",
            "面接をIt seems that he received it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "うう、Chaco、\x01",
            "I would like to enter a hole if I have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_3B18")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33DE")

    ChrTalk(
        0x8,
        (
            "I do not think the train will protrude from the track\x01",
            "It is frightening …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3455")

    ChrTalk(
        0x8,
        "Something papa is sowing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not sure but …\x01",
            "I'm pretty bad feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_3455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34C2")

    ChrTalk(
        0x8,
        (
            "Dad is worried about me\x01",
            "I understand, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anyway, it is excessive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_350F")

    ChrTalk(
        0x8,
        (
            "To preach to customers … …\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_359C")

    ChrTalk(
        0x8,
        (
            "Well, today is almost time.\x01",
            "It's time for a shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Papa as usual\x01",
            "It looks like you are in a shop ….\x01",
            "I want you to return soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_364D")

    ChrTalk(
        0x8,
        (
            "For the exhibition which I always use\x01",
            "導力カメラを、Wendy先輩に\x01",
            "I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Chaco、クローディア姫や\x01",
            "I wish I had taken the Prince Albert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_364D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")

    ChrTalk(
        0x8,
        "Everyone, welcome ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This time, at our shop is a guided car\x01",
            "Option parts and car paint\x01",
            "I started selling sets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not mind, by all means\x01",
            "Please consider purchasing ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 1)
    Jump("loc_3860")

    label("loc_3727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EA")

    ChrTalk(
        0x8,
        (
            "However, Dad also everyday everyday,\x01",
            "I do not get bored often ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I will not stop coming even if I say\x01",
            "Recently I left it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It also pampering too much\x01",
            "It may not be good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3860")

    label("loc_37EA")


    ChrTalk(
        0x8,
        (
            "Even if you say I will not come\x01",
            "Recently I left it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It also pampering too much\x01",
            "It may not be good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3860")

    Jump("loc_3B18")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BA")

    ChrTalk(
        0x8,
        (
            "For the moment,\x01",
            "Wendy先輩に対する\x01",
            "The attitude has changed obviously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I used to have been abandoned before\x01",
            "Suddenly, I started to take care of you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Afterwards to seniors\x01",
            "Carefully speechless words\x01",
            "I started to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first, my seniors were eloquent,\x01",
            "I'm completely settled now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3A5B")

    label("loc_39BA")


    ChrTalk(
        0x8,
        (
            "For the moment,\x01",
            "Wendy先輩に対する\x01",
            "The attitude has changed obviously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first, my seniors were eloquent,\x01",
            "I'm completely settled now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")

    Jump("loc_3B18")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B18")

    ChrTalk(
        0x8,
        (
            "At this counter\x01",
            "Besides sales and exchange of Enigma cover\x01",
            "Master quartz is also on sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "もうじゃんじゃん、Chacoのことを\x01",
            "Please do not stick around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B18")

    Return()

    # Function_7_2F12 end

    def Function_8_3B19(): pass

    label("Function_8_3B19")

    OP_C9(0x1, 0x80)
    Call(0, 9)
    Return()

    # Function_8_3B19 end

    def Function_9_3B23(): pass

    label("Function_9_3B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B51")
    Call(0, 25)
    Return()

    label("loc_3B51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CFC")
    TalkBegin(0x9)

    ChrTalk(
        0x9,
        "Yahoo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What on earth have you done?\x01",
            "Take such a cute girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, hey\x01",
            "To acquaintance's children\x01",
            "It is where I guide the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What I mean is that child\x01",
            "You have not been around here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Hey you, this shop,\x01",
            "It is pretty rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take a look around slowly,\x01",
            "Love with absolutely go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Oh, ah … (I love you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DD, 0)
    TalkEnd(0x9)
    Jump("loc_3D6D")

    label("loc_3CFC")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "Town guide information,\x01",
            "It sounds like fun something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, even so\x01",
            "Lloyd's also do various things\x01",
            "Do it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3D6D")

    Return()

    label("loc_3D73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D9D")
    Call(0, 21)
    Return()

    label("loc_3D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF4")
    Call(0, 22)
    Jump("loc_3E6B")

    label("loc_3DF4")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "First of all, Master Quartz\x01",
            "Can you get it set on the auction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I will let you know the rest of the story.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3E6B")

    Return()

    label("loc_3E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E92")
    Call(0, 23)
    Return()

    label("loc_3E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EB2")
    SetScenarioFlags(0x0, 1)
    TalkBegin(0x9)
    Call(0, 12)
    TalkEnd(0x9)
    Return()

    label("loc_3EB2")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FBA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "To remodel and synthesize\x01",      # 1
            "Question\x01",            # 2
            "quit\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F28")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F49")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_3FB5")

    label("loc_3F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F68")
    OP_AF(0xD)
    Jump("loc_3F8A")

    label("loc_3F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F78")
    OP_AF(0xC)
    Jump("loc_3F8A")

    label("loc_3F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F88")
    OP_AF(0xB)
    Jump("loc_3F8A")

    label("loc_3F88")

    OP_AF(0xA)

    label("loc_3F8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FB5")

    label("loc_3F99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3FB5")

    Jump("loc_3EBF")

    label("loc_3FBA")

    TalkEnd(0x9)
    Return()

    # Function_9_3B23 end

    def Function_10_3FBE(): pass

    label("Function_10_3FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_434B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BE")

    ChrTalk(
        0x9,
        (
            "Everyone in Lloyd -\x01",
            "President's detention,\x01",
            "I really appreciate your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then Lloyd, from now on\x01",
            "I think that suffering will continue\x01",
            "Let's keep going and do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, yes.\x02\x03",
            "#00000FWendyも何があっても\x01",
            "Keep your work here.\x02\x03",
            "Not long ago,\x01",
            "About the auction\x01",
            "I will depend on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hehe, OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And then, really\x01",
            "It's not a big deal\x01",
            "Bring this to me.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received three.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ填充剂Ⅲ', 3)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Wendy。\x01",
            "It will be awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hehe, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, from now on\x01",
            "When going into a dangerous place\x01",
            "Be careful again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And when it calms down again,\x01",
            "With Oscar and 3 people\x01",
            "Let's go for a meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOh, yes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 6)
    Jump("loc_4346")

    label("loc_42BE")


    ChrTalk(
        0x9,
        (
            "From now on\x01",
            "I think that suffering will continue,\x01",
            "Let's keep going and do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you calm down again,\x01",
            "With Oscar and 3 people\x01",
            "Let's go for a meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4346")

    Jump("loc_5A0A")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4409")

    ChrTalk(
        0x9,
        (
            "Although I heard that it seems to be safe … …\x01",
            "In this way when you actually look at your face\x01",
            "I guess it is safe after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When there is a business in the workshop\x01",
            "Please say it anytime.\x01",
            "I will support you with full power.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_458B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E7")

    ChrTalk(
        0x9,
        (
            "No way to go forward with such a rapid deployment\x01",
            "I did not expect it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Anyway, it looks like a lot harder from now on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When it is necessary to enter Lloyd, the workshop\x01",
            "Please say it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4586")

    label("loc_44E7")


    ChrTalk(
        0x9,
        (
            "No way to go forward with such a rapid deployment\x01",
            "I did not expect it … ….\x01",
            "Anyway, it looks like a lot harder from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When it is necessary to enter Lloyd, the workshop\x01",
            "Please say it anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4586")

    Jump("loc_5A0A")

    label("loc_458B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4642")

    ChrTalk(
        0x9,
        (
            "I also took the Oita section on the reconstruction of the city,\x01",
            "The direction of the old town is still too much\x01",
            "It seems not to catch up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today, even at the end of the work\x01",
            "I wonder if she will show her face to Guillaume.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_4642")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4706")

    ChrTalk(
        0x9,
        (
            "Miscon ah ~ ……\x01",
            "Well, everything is experienced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am asking for my best friendhood\x01",
            "I will accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until the program starts\x01",
            "Since I am working, when I need it\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4858")

    ChrTalk(
        0x9,
        (
            "Lloyd's, good work.\x01",
            "I also arrived from the event venue just now\x01",
            "I came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… Anyway, that\x01",
            "A child of a moderator Roy,\x01",
            "It was rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Such an introduction,\x01",
            "Always my customers with a spanner\x01",
            "It sounds like you're hitting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Does Lloyd think so, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, yeah, that's right.\x01",
            "(I can not deny it completely … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48CA")

    label("loc_4858")


    ChrTalk(
        0x9,
        (
            "Well, I also enjoyed misconceptions unexpectedly.\x01",
            "Thank you for inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have not come back.\x01",
            "I have to get back to work quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CA")

    Jump("loc_5A0A")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AE")

    ChrTalk(
        0x9,
        (
            "The ridiculous thing in Mainz\x01",
            "It sounds like it happened …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If Lloyd's also involved in the investigation\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you are adjusting for Enigma\x01",
            "Because I will undertake it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A1E")

    label("loc_49AE")


    ChrTalk(
        0x9,
        (
            "The ridiculous thing in Mainz\x01",
            "It sounds like it happened …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If Lloyd's also involved in the investigation\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A1E")

    Jump("loc_5A0A")

    label("loc_4A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4AB4")

    ChrTalk(
        0x9,
        (
            "どうやらChacoのお父様の\x01",
            "Worriedness seems hardcore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not think it's a bad thing,\x01",
            "Chacoの気持ちも\x01",
            "I want you to think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B18")

    ChrTalk(
        0x9,
        "Everything the driving train derailed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder if it happened even with machine trouble ……?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C41")

    ChrTalk(
        0x9,
        (
            "With a respect for craftsmen,\x01",
            "Muddy interior reminiscent of an old workshop\x01",
            "How to remodel …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The shop is also doing very well\x01",
            "Even though we are increasingly good people,\x01",
            "Then the customer just got confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The store manager recognizes craftsmen\x01",
            "I am glad that I revised it,\x01",
            "I want another way to think about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4CDC")

    label("loc_4C41")


    ChrTalk(
        0x9,
        (
            "Even if you only change the appearance of the store this time\x01",
            "Just confusing customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The store manager recognizes craftsmen\x01",
            "I am glad that I revised it,\x01",
            "I want another way to think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDC")

    Jump("loc_5A0A")

    label("loc_4CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF3")

    ChrTalk(
        0x9,
        (
            "Whether it's independent, when I first heard it\x01",
            "Anyway I was surprised, but when I listen to it\x01",
            "The mayor's claim is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I keep silent like this\x01",
            "Army of two major powers to the border gate\x01",
            "There are talks about stationing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wish for real peace\x01",
            "It may be time to raise a voice now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E98")

    label("loc_4DF3")


    ChrTalk(
        0x9,
        (
            "Whether it's independent, when I first heard it\x01",
            "Anyway I was surprised, but when I listen to it\x01",
            "The mayor's claim is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wish for real peace\x01",
            "It may be time to raise a voice now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E98")

    Jump("loc_5A0A")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F21")

    ChrTalk(
        0x9,
        (
            "う〜ん、Chacoのお父様も\x01",
            "You do it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, there are no employees in business\x01",
            "I think that he is bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_50C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505F")

    ChrTalk(
        0x9,
        (
            "Oh, Lloyd.\x01",
            "It is unusual at such time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, hey\x01",
            "An urgent investigation has entered.\x02\x03",
            "The shop is still okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh yeah, basically until 8 o'clock\x01",
            "I do it normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see, I am glad.\x01",
            "Then I will ask for adjustments when necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, I got it.\x01",
            "Then call me out anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_50BC")

    label("loc_505F")


    ChrTalk(
        0x9,
        (
            "If there is something related to Enigma\x01",
            "Say it anytime you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'll adjust it perfectly.\x02",
    )

    CloseMessageWindow()

    label("loc_50BC")

    Jump("loc_5A0A")

    label("loc_50C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_546F")

    ChrTalk(
        0x9,
        (
            "Hehe, \"Arsei\".\x01",
            "Although it is a long distance,\x01",
            "I put it in a perfect camera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I tried developing it at once,\x01",
            "If you do not mind, are there also Lloyds?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FWell then.\x01",
            "Maybe I'll show you.\x02",
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
        "#00106FEr, this is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FIs this really \"Arseille\"?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FBarely silhouette\x01",
            "I do not know if I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Eh, see everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the bow and this is the stern.\x01",
            "Far away, barely understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuff, if you are told\x01",
            "Sure it looks like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI guess that is unique to mecha lovers ……\x01",
            "Wendyはいつも見る所が違うよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well … I guess so.\x01",
            "I think it's normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHahaha ……\x01",
            "(Tomorrow is not normal for the time being\x01",
            "Only things are certain. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 4)
    Jump("loc_54EF")

    label("loc_546F")


    ChrTalk(
        0x9,
        (
            "It's a bit far-reaching, but properly\x01",
            "I could put the figure of \"Arsei\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahoeh, this picture,\x01",
            "I will stretch it and paste it on the wall of the room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EF")

    Jump("loc_5A0A")

    label("loc_54F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571B")

    ChrTalk(
        0x9,
        (
            "It is a trade meeting,\x01",
            "After all, Libert's representative\x01",
            "I wonder if it will come with that \"Arseille\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F\"Arseille\" … ….\x01",
            "Oh, it's a high-speed cruiser of the Ribeire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, he gathered the chic of ZCF's technology\x01",
            "It is perfectly suited to call it the highest masterpiece\x01",
            "An airship inside an airship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it is likely to cross the sky,\x01",
            "You have to take a picture even if you stop working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI do not know how I feel.\x01",
            "Can you moderate it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "No, ya. (Kippari)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FHey, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309Fはは、流石はWendyちゃん。\x01",
            "It's a splendid answer like broken bamboo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 3)
    Jump("loc_57BD")

    label("loc_571B")


    ChrTalk(
        0x9,
        (
            "通商会議かぁ、After all, Libert's representative\x01",
            "I wonder if it will come with that \"Arseille\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it is likely to cross the sky,\x01",
            "You have to take a picture even if you stop working!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BD")

    Jump("loc_5A0A")

    label("loc_57C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5859")

    ChrTalk(
        0x9,
        (
            "Than I thought she was the manager of our store\x01",
            "I am keen to study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is it because it was originally a designer?\x01",
            "What I mean is something like knowledge\x01",
            "There seems to be considerable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_5859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_595C")

    ChrTalk(
        0x9,
        (
            "Anyway, master quartz\x01",
            "Since it is OK to set it once\x01",
            "Come with the battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then, after the battle is properly\x01",
            "Do not forget to come and report to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Otherwise, this course\x01",
            "Because it will not end even when you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_595C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A0A")

    ChrTalk(
        0x9,
        (
            "Huhu, that's it for now\x01",
            "Master Quartz\x01",
            "Do not forget to love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The more you pour in affection,\x01",
            "Master Quartz always works\x01",
            "Because I will repay you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0A")

    Return()

    # Function_10_3FBE end

    def Function_11_5A0B(): pass

    label("Function_11_5A0B")


    ChrTalk(
        0x9,
        (
            "Okay.\x01",
            "What do you want to ask?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_671B")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "About tactical auction\x01",        # 0
            "About Quartz\x01",                # 1
            "About opening the slot\x01",          # 2
            "About slot reinforcement\x01",          # 3
            "About conductivity magic (Arts)\x01",      # 4
            "About Enigma\x01",              # 5
            "マスターAbout Quartz\x01",        # 6
            "quit\x01",                          # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2E")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_5B2E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5B62"),
        (1, "loc_5D27"),
        (2, "loc_5E56"),
        (3, "loc_5F84"),
        (4, "loc_60F7"),
        (5, "loc_62F3"),
        (6, "loc_64C1"),
        (SWITCH_DEFAULT, "loc_6707"),
    )


    label("loc_5B62")


    ChrTalk(
        0x9,
        (
            "\"Tactical orbement\"\x01",
            "Specialized for battle\x01",
            "It's a small portable power guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In addition to enhancing the user's abilities\x01",
            "Power magic#8RArts#It also supports the use of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Generally, simply \"an aim\"\x01",
            "There are many things called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ordered to individuals\x01",
            "Because it is perfectly adjusted,\x01",
            "The structure differs depending on the owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are slots with attribute limitations,\x01",
            "Line connecting slots#2Rline#There are different forms.\x01",
            "It may be good to compare them once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5D27")


    ChrTalk(
        0x9,
        (
            "Quartz is made by refining sepis\x01",
            "About \"crystal circuit\" for the orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you bring even the necessary sepises\x01",
            "I can synthesize with my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are various effects depending on quartz,\x01",
            "When the attribute value becomes equal to or greater than a certain value\x01",
            "Power magic#8RArts#You will be able to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If sepis gathers up try it a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5E56")


    ChrTalk(
        0x9,
        (
            "The slot of the auction\x01",
            "In the beginning most of it is unopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So to set quartz\x01",
            "First of all I need to open the slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you open the slot,\x01",
            "That's why we can also add quartz\x01",
            "The maximum EP will also rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For opening it requires sepice,\x01",
            "I think it will not be damaged as soon as possible to open it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5F84")


    ChrTalk(
        0x9,
        (
            "In the quartz, \"Top Quartz\" and\x01",
            "There is something called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is too strong, it's an ordinary slot\x01",
            "I can not set it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then,\x01",
            "It is strengthening the slot itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sepis is necessary as well as opening,\x01",
            "The maximum EP will also rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not think that strengthening will be impatient,\x01",
            "To power up the auction\x01",
            "It can be said to be an indispensable element.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_60F7")


    ChrTalk(
        0x9,
        (
            "Magic to activate using tactical orbient\x01",
            "The so-called guiding magic#8ROval Arts#Right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "There are many things called simply \"Arts\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Arts, the set quartz\x01",
            "By \"sum of attribute values per line\"\x01",
            "The type that can be activated is decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, the set quartz\x01",
            "The higher the attribute value,\x01",
            "You can increase the number of available arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Incidentally, more powerful arts\x01",
            "If you want to use it, also combine attribute values\x01",
            "It gets important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For more information about that,\x01",
            "Because the list is listed in the investigation notebook\x01",
            "Please refer to that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_62F3")


    ChrTalk(
        0x9,
        (
            "Taking over the communication function of Enigma,\x01",
            "A successor to which a bold remodeling was given -\x01",
            "That is \"Enigma 嘦\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The only biggest change is that,\x01",
            "Newly referred to as \"Master Quartz\"\x01",
            "It has been dealt with special quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, it seems mostly ….\x01",
            "With this version upgrade\x01",
            "There is a change in the basic architecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, with compatibility issues\x01",
            "Quartz used in old Enigma\x01",
            "I can not do any set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, to use Enigma\x01",
            "You will need a new standard quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_64C1")


    ChrTalk(
        0x9,
        (
            "Master Quartz,\x01",
            "Fits in the center of Enigma\x01",
            "It's about special quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What is decisively different from traditional quartz\x01",
            "That means that it \"grows\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With it set in the auction\x01",
            "By repeating battle, the level got higher\x01",
            "It will show more powerful effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Enhance user ability,\x01",
            "Special effect of quartz, attribute value … ….\x01",
            "These are three major growth factors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way Master Quartz\x01",
            "If you nurture anything to the end\x01",
            "It seems to be very powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How to raise the level\x01",
            "It seems that it will take quite a while … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Without cheating, what you like\x01",
            "It may be important to keep using it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_6707")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6716")

    label("loc_6716")

    Jump("loc_5A3C")

    label("loc_671B")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_5A0B end

    def Function_12_6729(): pass

    label("Function_12_6729")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    def lambda_673A():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_673A)

    def lambda_6747():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6747)
    TurnDirection(0xA, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_67A3")

    ChrTalk(
        0x8,
        "Oh, you guys … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd …\x01",
            "You were ok!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6820")

    label("loc_67A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_67D8")

    ChrTalk(
        0x9,
        (
            "Lloyd …\x01",
            "You were ok!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6820")

    label("loc_67D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6820")

    ChrTalk(
        0xA,
        "Hey, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd …\x01",
            "You were ok!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6820")


    ChrTalk(
        0x101,
        "#00000FOh, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the most part, police\x01",
            "I heard from your colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys, this situation\x01",
            "You manage to do something.\x01",
            "I have really asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That wonderful person, even at the shop\x01",
            "I will support you so ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whether you are going ahead\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you.\x02",
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

    # Function_12_6729 end

    def Function_13_6988(): pass

    label("Function_13_6988")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6999")
    Jump("loc_7AE0")

    label("loc_6999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B7")
    SetScenarioFlags(0x0, 3)
    Call(0, 12)
    Jump("loc_6A2D")

    label("loc_69B7")


    ChrTalk(
        0xFE,
        (
            "However, this situation …\x01",
            "It is very confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future this crossbell will\x01",
            "What will happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A2D")

    Jump("loc_7AE0")

    label("loc_6A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B24")

    ChrTalk(
        0xFE,
        (
            "\"Crossbell independent country\" … …\x01",
            "With this we will completely\x01",
            "You have turned to the enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Result Naturally, with Linefault\x01",
            "Vernes' products will be available at our store in the future\x01",
            "It will not come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, my head hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BA4")

    label("loc_6B24")


    ChrTalk(
        0xFE,
        (
            "It is no doubt that we will stop economic activity\x01",
            "To break independent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is the case,\x01",
            "I did not approve of independence … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA4")

    Jump("loc_7AE0")

    label("loc_6BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C3B")

    ChrTalk(
        0xFE,
        (
            "Residents 'vote over the independence'\x01",
            "Finally we approached three days later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that day, I changed my shop and I got an answering machine,\x01",
            "All employees will vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_6C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CFC")

    ChrTalk(
        0xFE,
        (
            "Hmm, what is the occupation case?\x01",
            "It became an indisputable incident …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the Empire is holding hands behind the scenes\x01",
            "Although it is said that it is not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I'd like you to solve it sooner.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D69")

    label("loc_6CFC")


    ChrTalk(
        0xFE,
        (
            "If the Empire is holding hands behind the scenes\x01",
            "Although it is said that it is not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I'd like you to solve it sooner.\x02",
    )

    CloseMessageWindow()

    label("loc_6D69")

    Jump("loc_7AE0")

    label("loc_6D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4B")

    ChrTalk(
        0xFE,
        (
            "昨日、Chacoのお父上が\x01",
            "I was at the interview of our shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because my daughter is concerned\x01",
            "It was a story of letting me work … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, as a criterion for our adoption\x01",
            "Because it was not the case\x01",
            "I refrained.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6ED4")

    label("loc_6E4B")


    ChrTalk(
        0xFE,
        (
            "Because my daughter is concerned\x01",
            "It was a story of letting me work … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, as a criterion for our adoption\x01",
            "Because it was not the case\x01",
            "I refrained.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED4")

    Jump("loc_7AE0")

    label("loc_6ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6F50")

    ChrTalk(
        0xFE,
        (
            "I heard from customers,\x01",
            "It seems that the train has derailed by everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope everyone is safe, but …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_6F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_70B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7031")

    ChrTalk(
        0xFE,
        (
            "About plans to refurbish the store muddy\x01",
            "Wendy君とChacoに\x01",
            "I asked the opinion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before finishing all the story\x01",
            "It has been dismissed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it is not bad at all.\x01",
            "I thought it was an idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_70AB")

    label("loc_7031")


    ChrTalk(
        0xFE,
        (
            "Hmm, it is not bad at all.\x01",
            "I thought it was an idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, two people over there\x01",
            "It can not be helped if it is opposed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70AB")

    Jump("loc_7AE0")

    label("loc_70B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71BC")

    ChrTalk(
        0xFE,
        (
            "Mr. Guillaume who was once in my place,\x01",
            "Due to disagreement on management policy\x01",
            "Although it became a different way … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, for him\x01",
            "I think I did a bit of a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was noticed recently,\x01",
            "What does this industry say?\x01",
            "Because there is a craftsman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_726E")

    label("loc_71BC")


    ChrTalk(
        0xFE,
        (
            "そういえば、Wendyも\x01",
            "The atmosphere of the old factory is better\x01",
            "I told you I liked it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, at least with interior alone\x01",
            "Like the old genre studio\x01",
            "It might be okay to make it muddy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_726E")

    Jump("loc_7AE0")

    label("loc_7273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7311")

    ChrTalk(
        0xFE,
        "Is today the day of the plenary session of the Trade Council?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell, and eventually the whole continent\x01",
            "An important international conference that dominates the economic outlook … …\x01",
            "I do not care what the content is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_7311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7390")

    ChrTalk(
        0xFE,
        "Good evening, Welcome to \"Genten\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since there is still time until closing,\x01",
            "Please slowly see without being rash.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_7390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A6")

    ChrTalk(
        0xFE,
        (
            "ふう、Wendy君にも\x01",
            "It is troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The reason why I got out of work,\x01",
            "To bring out the shop's camera ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… and if I were a previous one\x01",
            "It is a place I spilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially for conspicuous work\x01",
            "There was no trouble,\x01",
            "This thing is cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_753B")

    label("loc_74A6")


    ChrTalk(
        0xFE,
        (
            "Even using a camera for exhibition,\x01",
            "If you think it will be a feature promotion\x01",
            "Rather it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which, later on I took pictures taken\x01",
            "Let's show it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_753B")

    Jump("loc_7AE0")

    label("loc_7540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7645")

    ChrTalk(
        0xFE,
        "Customers, is there anything we need to help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for a vacuum cleaner,\x01",
            "Here made by Verne\x01",
            "I recommend the latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Three removable head parts\x01",
            "By using properly, in every scene\x01",
            "It is a very convenient superior item that can handle it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_76FF")

    label("loc_7645")


    ChrTalk(
        0xFE,
        (
            "If you are looking for a power vacuum cleaner,\x01",
            "Here made by Verne\x01",
            "I recommend the latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Three removable head parts\x01",
            "By using properly, in every scene\x01",
            "It is a very convenient superior item that can handle it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76FF")

    Jump("loc_7AE0")

    label("loc_7704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_791C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7895")

    ChrTalk(
        0xFE,
        (
            "I am embarrassed so far,\x01",
            "I can say that it is quite tough about the conductors\x01",
            "I did not have any knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as the store gets in orbit\x01",
            "I was noticed that I should not do it,\x01",
            "Although I started studying at a delay, …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いやはや、うちのWendy君然り、\x01",
            "It is amazing how a power engineer is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also challenged to acquire technical knowledge,\x01",
            "It was too complicated for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7917")

    label("loc_7895")


    ChrTalk(
        0xFE,
        (
            "いやはや、うちのWendy君然り、\x01",
            "It is amazing how a power engineer is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In me and others, superficial\x01",
            "I will do my utmost to learn the knowledge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7917")

    Jump("loc_7AE0")

    label("loc_791C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A2B")

    ChrTalk(
        0xFE,
        (
            "Welcome.\x01",
            "Welcome to the oval store \"Genten\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In our shop, of course leading-edge power products,\x01",
            "A true-hearted community-based type\x01",
            "We are doing our after-sales service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have anything to discuss,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7AE0")

    label("loc_7A2B")


    ChrTalk(
        0xFE,
        (
            "In our shop, of course leading-edge power products,\x01",
            "A true-hearted community-based type\x01",
            "We are doing our after-sales service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have anything to discuss,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE0")

    TalkEnd(0xFE)
    Return()

    # Function_13_6988 end

    def Function_14_7AE4(): pass

    label("Function_14_7AE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B8D")

    ChrTalk(
        0xFE,
        (
            "To be honest, I do not feel like shopping ….\x01",
            "Even though I was at home, I came to the shop because I feel uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa …… Everything is refreshing as soon as possible.\x01",
            "I want to settle and regain everyday life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7B9B")
    Jump("loc_8551")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7C3C")

    ChrTalk(
        0xFE,
        (
            "President Dieter's speech,\x01",
            "There was force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be hard for me in the future,\x01",
            "The lady together\x01",
            "I felt like I had to work hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7CEB")

    ChrTalk(
        0xFE,
        (
            "I usually have an aunt who is not interested in politics,\x01",
            "Only independence problem is different to drift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on the latest case\x01",
            "I thought of various things, but as expected\x01",
            "I think crossbell should be independent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7D5A")

    ChrTalk(
        0xFE,
        "It is horrible to say that the occupation case … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something also for my lady\x01",
            "I wish I had something I could do ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E23")

    ChrTalk(
        0xFE,
        (
            "When it becomes independent, a part of tax is put on two major powers\x01",
            "You do not have to pay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then the crossbell economy\x01",
            "It's a story to develop even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aunt, I think that is important.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7EC4")

    label("loc_7E23")


    ChrTalk(
        0xFE,
        (
            "Independently, in two major powers\x01",
            "You do not have to pay taxes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then the crossbell economy\x01",
            "It's a story to develop even more.\x01",
            "Aunt, I think that is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EC4")

    Jump("loc_8551")

    label("loc_7EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7EFB")

    ChrTalk(
        0xFE,
        "Oh, something outside is noisy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_806E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FDF")

    ChrTalk(
        0xFE,
        (
            "Products manufactured by Rheinfault\x01",
            "Anyway to sell large capacity · high output\x01",
            "There seems to be a lot of things you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meanwhile, Verne is rich in functions\x01",
            "It is characterized by a lot of affordable prices as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I wonder if this is also a country.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8069")

    label("loc_7FDF")


    ChrTalk(
        0xFE,
        (
            "Rheinfault offers high capacity, high output,\x01",
            "Verne is convenient and economical\x01",
            "It seems that there is a tendency to put power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I wonder if this is also a country.\x02",
    )

    CloseMessageWindow()

    label("loc_8069")

    Jump("loc_8551")

    label("loc_806E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8120")

    ChrTalk(
        0xFE,
        (
            "I recently knew it,\x01",
            "The one that is hardest to break when using\x01",
            "It seems to be made by ZCF by any chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared to others, expensive products\x01",
            "I thought it was a lot,\x01",
            "It seems there is only that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_8120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_81AC")

    ChrTalk(
        0xFE,
        (
            "Even if it looks like a similar product at first sight\x01",
            "It seems there is personality by manufacturer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, also to your lady\x01",
            "I gradually understood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_81AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8228")

    ChrTalk(
        0xFE,
        "Oh, it is already such a time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, boasting back home soon\x01",
            "I have to cook with a range of power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8284")

    label("loc_8228")


    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "Convenient range is useful ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was quite expensive,\x01",
            "I'm glad I bought it ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8284")

    Jump("loc_8551")

    label("loc_8289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8327")

    ChrTalk(
        0xFE,
        (
            "Trade meeting?\x01",
            "Well, to be honest lady\x01",
            "I have no direct relationship, I am not interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here, look more than that.\x01",
            "Do not you think this new product is cute?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_838F")

    label("loc_8327")


    ChrTalk(
        0xFE,
        (
            "The screw attached here is\x01",
            "If it is omen,\x01",
            "Look, it looks like a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, you are cute.\x02",
    )

    CloseMessageWindow()

    label("loc_838F")

    Jump("loc_8551")

    label("loc_8394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_843B")

    ChrTalk(
        0xFE,
        (
            "The store manager here, in the past few months\x01",
            "It seems like I knew well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not asked, but when explained it\x01",
            "Somewhat annoying but ……\x01",
            "Only enthusiasm will be transmitted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_843B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_84B6")

    ChrTalk(
        0xFE,
        "It's attractive to produce a product of power.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you do not plan to shop separately,\x01",
            "I will want to come to see the shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_84B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8551")

    ChrTalk(
        0xFE,
        (
            "Oh no, the vacuum cleaner I bought this before\x01",
            "I heard that the next-generation model appears as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already ~ If you say more quickly\x01",
            "Aunt, I did not buy it at that time ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8551")

    TalkEnd(0xFE)
    Return()

    # Function_14_7AE4 end

    def Function_15_8555(): pass

    label("Function_15_8555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_85CA")

    ChrTalk(
        0xFE,
        (
            "おお、Chaco……\x01",
            "まさしく私の娘のChacoだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Father,\x01",
            "I am worried about you … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_85CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_85D8")
    Jump("loc_90FA")

    label("loc_85D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_867A")

    ChrTalk(
        0xFE,
        (
            "Even if you say \"defense army\"\x01",
            "Do you really want to protect us …?\x01",
            "I am anxious to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……but it's okay.\x01",
            "何があってもChacoのことは\x01",
            "Because I will protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_867A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_871B")

    ChrTalk(
        0xFE,
        (
            "Chacoの許しが出たから\x01",
            "Both of us went to work with us this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chaco、お前のことは\x01",
            "Whatever it may be\x01",
            "It is because my father always protects.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_871B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87BB")

    ChrTalk(
        0xFE,
        (
            "Armed groups of mining towns\x01",
            "I took over the occupation ……\x01",
            "What a stupid talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And anyway today\x01",
            "Chacoに何を言われても\x01",
            "I will go home together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_87BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8838")

    ChrTalk(
        0xFE,
        (
            "Well, the manager\x01",
            "You do not understand the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, oh well.\x01",
            "Then, as before\x01",
            "Until you come as a customer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_888A")

    ChrTalk(
        0xFE,
        (
            "Is it a derailment accident ……\x01",
            "I have heard it sometimes in the past,\x01",
            "Strange, is not it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_888A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_88D8")

    ChrTalk(
        0xFE,
        (
            "Today, I will interview this store\x01",
            "I decided to take it.\x01",
            "Throb……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_88D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89DB")

    ChrTalk(
        0xFE,
        (
            "No matter what my daughter says\x01",
            "I am worried about worried things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, yet more\x01",
            "Will you work as a power engineer here …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, to the last I\x01",
            "Because it is human in design field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can do as much as an easy adjustment … …\x01",
            "Will you hire it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8A2D")

    label("loc_89DB")


    ChrTalk(
        0xFE,
        (
            "Well, I am the last one\x01",
            "Because it is human in design field.\x01",
            "Will you hire it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A2D")

    Jump("loc_90FA")

    label("loc_8A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8AD3")

    ChrTalk(
        0xFE,
        (
            "Targeting the end of work yesterday\x01",
            "Chacoに近づく輩がいたので\x01",
            "I thought carefully though ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そのことで、Chacoに\x01",
            "I got very angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BC3")

    ChrTalk(
        0xFE,
        (
            "Well, I still have time,\x01",
            "It's time to close while I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The night road is dangerous, in reality\x01",
            "Chacoと一緒に帰りたい所だけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To that extent,\x01",
            "Chacoに嫌われてしまうしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, what is it ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8C2C")

    label("loc_8BC3")


    ChrTalk(
        0xFE,
        (
            "As you go along with Kosori from behind\x01",
            "I will become a suspicious person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I suppose I should go home quietly today ….\x02",
    )

    CloseMessageWindow()

    label("loc_8C2C")

    Jump("loc_90FA")

    label("loc_8C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8D03")

    ChrTalk(
        0xFE,
        (
            "Chacoの先輩のWendy君だったか。\x01",
            "She can hear the engine sound of the flying boat,\x01",
            "I rushed out the store in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then for a while\x01",
            "I did not come back,\x01",
            "I wonder what was going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8D68")

    ChrTalk(
        0xFE,
        (
            "Hmm, as my daughter\x01",
            "Chacoには華があるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm worried whether bad insects will not come around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EAB")

    ChrTalk(
        0xFE,
        (
            "For the design of the appearance of a conductive product\x01",
            "By manufacturer\x01",
            "There are things like trends ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no unnecessary decoration and no waste,\x01",
            "In terms of functional beauty ZCF made\x01",
            "The Epstein foundation is missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Rhinfault Corporation\x01",
            "There are lots of spectacular things, Vernes made\x01",
            "There are a lot of pop things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8F54")

    label("loc_8EAB")


    ChrTalk(
        0xFE,
        (
            "I do not need extra decoration in the product\x01",
            "It is a type I think is unnecessary at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For wasteful decoration,\x01",
            "When I think that Mira is extra\x01",
            "I am irritated and it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F54")

    Jump("loc_90FA")

    label("loc_8F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_90FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906C")

    ChrTalk(
        0xFE,
        (
            "Until last year,\x01",
            "As a design engineer for power products\x01",
            "I worked, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because my daughter has taken a job,\x01",
            "I also got a house on the bank\x01",
            "I dared to retire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not that I am not skilled in my work,\x01",
            "The time to spend with my family more than anything\x01",
            "I'm glad that things increased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_90FA")

    label("loc_906C")


    ChrTalk(
        0xFE,
        (
            "so,\x01",
            "今日も娘のChacoの働きぶりを\x01",
            "I came to see … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, as always\x01",
            "You seem to be working hard.\x01",
            "My father is impressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FA")

    TalkEnd(0xFE)
    Return()

    # Function_15_8555 end

    def Function_16_90FE(): pass

    label("Function_16_90FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_91BC")

    ChrTalk(
        0xFE,
        (
            "It is called a guided vehicle, it is called a guiding terminal,\x01",
            "It is a sort of thing that people can not reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the price is going down gradually ….\x01",
            "To the extent that it spreads to ordinary households,\x01",
            "I wonder if it goes down?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9246")

    label("loc_91BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9246")

    ChrTalk(
        0xFE,
        (
            "Uh, this is\x01",
            "It is a rumor notebook type power terminal.\x01",
            "Well the price ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……… Well, a terrible 0 number.\x01",
            "It is unbelievable to buy such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9246")

    TalkEnd(0xFE)
    Return()

    # Function_16_90FE end

    def Function_17_924A(): pass

    label("Function_17_924A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_933A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F1")

    ChrTalk(
        0xFE,
        (
            "Chacoちゃんのことがどうしても\x01",
            "I could not forget it but I came again … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… That father, are you still there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa, I guess I will give up and leave.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9335")

    label("loc_92F1")


    ChrTalk(
        0xFE,
        "…… That father is still there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa, are you supposed to give up and get home?\x02",
    )

    CloseMessageWindow()

    label("loc_9335")

    Jump("loc_96A6")

    label("loc_933A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93BD")

    ChrTalk(
        0xFE,
        (
            "It will be business closing time soon.\x01",
            "The customer is still\x01",
            "It seems quite enough ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………… Voice, why do not you try it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9413")

    label("loc_93BD")


    ChrTalk(
        0xFE,
        (
            "Sprinkle courage\x01",
            "Chacoちゃんに声を……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, hey\x01",
            "Do you think calmly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9413")

    Jump("loc_96A6")

    label("loc_9418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_957C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9520")

    ChrTalk(
        0xFE,
        (
            "Especially I do not plan to shop ….\x01",
            "To the face of the child of the sale\x01",
            "I came to the shop again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way nameplate\x01",
            "I confirmed it, but she\x01",
            "Chacoちゃんって言うんだって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In keeping with the innocent appearance,\x01",
            "It's a very cute name!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9577")

    label("loc_9520")


    ChrTalk(
        0xFE,
        "I do not care about the unveiling ceremony!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can watch that girl's smile\x01",
            "That's good!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9577")

    Jump("loc_96A6")

    label("loc_957C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_96A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9650")

    ChrTalk(
        0xFE,
        "Well, this shop is wonderful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not a guide,\x01",
            "Anyway the clerk is pretty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Muffu, the engineer is also nice,\x01",
            "For me it's a sales counter\x01",
            "Girls are do-strike gush\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_96A6")

    label("loc_9650")


    ChrTalk(
        0xFE,
        (
            "Well, this is\x01",
            "It is a reward of an unexpected trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ask me for a photo\x01",
            "Will you let me take it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96A6")

    TalkEnd(0xFE)
    Return()

    # Function_17_924A end

    def Function_18_96AA(): pass

    label("Function_18_96AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9729")

    ChrTalk(
        0xFE,
        (
            "Hmm, something disturbing incident\x01",
            "It seems awake …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Round up the schedule of travel earlier\x01",
            "I suppose I should go home early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_9729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_97C5")

    ChrTalk(
        0xFE,
        (
            "An accident happened yesterday\x01",
            "Electricity train also this morning\x01",
            "That seems to have been completely restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I got hit by accident\x01",
            "It's also a guard\x01",
            "It seems quite good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_97C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9821")

    ChrTalk(
        0xFE,
        (
            "Hmm, the sound of a while ago\x01",
            "It's a siren.\x01",
            "It is a sound that I do not want to hear much, but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_9821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_98AA")

    ChrTalk(
        0xFE,
        (
            "No, but\x01",
            "Conductive products are beautiful things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even products with the same function,\x01",
            "Various shapes are also made by manufacturers\x01",
            "It is really interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_98AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9933")

    ChrTalk(
        0xFE,
        (
            "Hmm, this shop is the manufacturer of each country\x01",
            "We have a well-balanced product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The drifting is a crossbell.\x01",
            "It is only a trading city of the continent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9933")

    TalkEnd(0xFE)
    Return()

    # Function_18_96AA end

    def Function_19_9937(): pass

    label("Function_19_9937")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A15")

    ChrTalk(
        0xFE,
        "I wonder what it is, this situation …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, even if I go home\x01",
            "Because I did not even have enough rice\x01",
            "It is better for me to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Ha, I have nothing to do,\x01",
            "I wonder if I am adjusting the airing machine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A86")

    label("loc_9A15")


    ChrTalk(
        0xFE,
        "I wonder what it is, this situation …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I do not have anything to do,\x01",
            "I wonder if I am adjusting the airing machine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A86")

    TalkEnd(0xFE)
    Return()

    # Function_19_9937 end

    def Function_20_9A8A(): pass

    label("Function_20_9A8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B15")

    ChrTalk(
        0xFE,
        "Photosensitive quartz, sensitive quartz, and …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, the latest type has different capacity.\x01",
            "If it is 2 or 3 in this case will you surpass?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_9B8A")

    label("loc_9B15")


    ChrTalk(
        0xFE,
        (
            "In preparation for the unveiling ceremony for tomorrow,\x01",
            "Preliminary photosensitive quartz\x01",
            "I came to buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it is expired at the time of emergency\x01",
            "It is serious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_9A8A end

    def Function_21_9B8E(): pass

    label("Function_21_9B8E")

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
        "#11PLloyd, I was waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso, everyone …\x01",
            "Half is a face that is not familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, with this member\x01",
            "I just started to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FNice to meet you,\x01",
            "It is called Noel Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWadi Hemisphere, best regards.\x02\x03",
            "#10300FBy the way, you -\x01",
            "You are childhood friend of Lloyd?\x02\x03",
            "If you do not mind, next time Lloyd's\x01",
            "A funny funny episode of a young age\x01",
            "I'd like to hear it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11PHuhu, that's fine ~!\x01",
            "You want to grab the weakness of Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FWhat is that story ……\x02\x03",
            "#00000F- Tentatively,\x01",
            "Go ahead quickly.\x02\x03",
            "A course of Enigma を\x01",
            "Did not you do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWell, it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh hon, then at once ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P- Lloyds, too,\x01",
            "I already use Enigma\x01",
            "I think that he knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Epstein Foundation did,\x01",
            "This version upgrade\x01",
            "The only biggest change point ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhatever it is,\x01",
            "It's in the center slot structure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen, fit in the center\x01",
            "A special quartz\x01",
            "I call it \"Master Quartz\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, this pattern was engraved\x01",
            "It's about quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, that spherical quartz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd that master quartz\x01",
            "The point which is decisively different from conventional quartz\x01",
            "It means \"to grow\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWith it set in the auction\x01",
            "It was refined by battle repeatedly,\x01",
            "It is going to be strengthened step by step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FWhat is it …?\x01",
            "I feel a little mysterious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYeah, as if\x01",
            "He seems to have a life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, by the way from now\x01",
            "The principle and something\x01",
            "Will you give a lecture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh, no, that's\x01",
            "I'm sorry but it's not a researcher\x01",
            "I do not know the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POriginally rather than growth,\x01",
            "I will draw out secret powers\x01",
            "It seems to be an image ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnyway, to everyone\x01",
            "I want to remember\x01",
            "How to treat Enigma - -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIn other words, it is more practical than argument.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo, first\x01",
            "I wonder if I will receive this.\x02",
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
            "Eli is",
            scpstr(SCPSTR_CODE_ITEM, '妖精'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('妖精', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Wadi is",
            scpstr(SCPSTR_CODE_ITEM, '利爪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('利爪', 1)

    ChrTalk(
        0x102,
        "#6P#00105FThis is Master Quartz ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FHmm, certainly ordinary quartz\x01",
            "Something like a presence is completely different.\x02\x03",
            "#10300FWould you mind if I got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYeah, all good and nice\x01",
            "Originally from the police headquarters\x01",
            "Because it is goods given to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, Master Quartz\x01",
            "It can not be synthesized in ordinary studio\x01",
            "It seems that it can not be mass produced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom my research laboratory at Utsunomiya\x01",
            "I have received some stocks, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBasically, one type\x01",
            "I can only sell one piece\x01",
            "Be treated with care and care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI see……\x01",
            "That means that it is a rare item.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005Fそれは分かったけどWendy、\x01",
            "What on earth do you practice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, first of all, everyone,\x01",
            "Master quartz as an auction\x01",
            "I wonder if you can set it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo matter who can attach any\x01",
            "When all four people set\x01",
            "Please give me a voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, even for Master Quartz\x01",
            "Although there are specific attributes,\x01",
            "There is no \"tie\" in the slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn other words, Master Quartz\x01",
            "It's a dimension that you can set without choosing people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FIndeed, that is useful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, that's right\x01",
            "Let me set it.\x02",
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
            "Quest 【Training course of Enigma】\x07\x00",
            "I started!\x02",
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

    # Function_21_9B8E end

    def Function_22_A937(): pass

    label("Function_22_A937")

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
            "#11POk, apparently everyone\x01",
            "ちゃんとMaster Quartz\x01",
            "You seem to have set it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FSo, what are you going to do next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHehe, simple clarity -\x01",
            "Now the effect of Master Quartz\x01",
            "I really want you to check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105Fthat is……\x01",
            "Is that thing through battle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, that is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLloyd and Noel\x01",
            "I already seem to have experienced it,\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBy the way, are there any conditions?\x01",
            "The place to fight or the number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo, nothing special.\x01",
            "I leave the place and the partner completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlthough the number of battles is enough once,\x01",
            "But do not run away and fight properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHuh, you are reasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FSo, Lloyd, what about the place?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AD12")

    ChrTalk(
        0x101,
        (
            "#6P#00003FThat's right, for now\x01",
            "I do not plan to go outside the city … …\x02\x03",
            "#00000FDemon Beast in Maison Imerda\x01",
            "You might as well make it a partner.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_AD9E")

    label("loc_AD12")


    ChrTalk(
        0x101,
        (
            "#6P#00003FBy the way, to Maison Imelda\x01",
            "There was a magical beast to arrange.\x02\x03",
            "#00000FBeyond tearing it away\x01",
            "You might as well try it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AD9E")


    ChrTalk(
        0x109,
        (
            "#6P#10100FIndeed, there\x01",
            "You seem to be able to try it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHuhu, apparently\x01",
            "It seems that the place has also been decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, next time I will qualify this quartz\x01",
            "Please take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神１', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, it is also a supply from the police headquarters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you put that quartz into a normal slot,\x01",
            "New Arts for Enigma\x01",
            "Because \"Analyze\" will be available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThose who control information\x01",
            "I mean to control the battle.\x01",
            "Use it for battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, that's OK.\x02\x03",
            "#00003F(There is no Tio now ……\x01",
            "For a while, collecting information on monsters\x01",
            "It seems necessary to depend on Arts. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell then,\x01",
            "Take care and have a beat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PModification of the auction\x01",
            "When you want to synthesize quartz,\x01",
            "Please say it anytime.\x02",
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
            "※Wendyに話しかけ、\x01",
            "If you select \"Modify / synthesize\"\x01",
            "Synthesis of new quartz and\x01",
            "Slot opening and strengthening of tactical ornament can be done.\x02\x03",
            "* Combine new quartz and set it\x01",
            "You will be able to use various arts.\x02\x03",
            "※ If you open and strengthen the slot,\x01",
            "As the number of quartz that can be set increases\x01",
            "You can increase the maximum EP.\x02\x03",
            "Note that in order to use these functions,\x01",
            "It is necessary to have a piece of seven ice stone called \"sepice\".\x01",
            "(Sepis can be obtained mainly by defeating demonic beasts.)\x07\x00\x02",
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

    # Function_22_A937 end

    def Function_23_B2E9(): pass

    label("Function_23_B2E9")

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
            "#11POh, cheers for good work.\x01",
            "Apparently\x01",
            "You seem to have done battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, Mr. Ellie,\x01",
            "I actually tried using Master Quartz\x01",
            "How was your impression?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYeah, I was surprised at what.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FOh, no way with quartz\x01",
            "That's all that performance\x01",
            "That's what you can do.\x02\x03",
            "#10300FHonestly, I wonder if I thought it was far.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62C")

    ChrTalk(
        0x9,
        "#11PHehe, it is a good reaction ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, if you grow to the final stage,\x01",
            "I will be able to do something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, that is\x01",
            "I am looking forward to actually growing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FOh, still a surprise\x01",
            "It is prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha, I will look forward to it.\x02\x03",
            "#00000FSo, what is lecture?\x01",
            "Is it okay with the end?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71C")

    label("loc_B62C")


    ChrTalk(
        0x9,
        "#11PHehe, it is a good reaction ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat is it, the Epstein Foundation's\x01",
            "It may be wanting to deliver it to people involved in development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha, surely praised\x01",
            "I guess I do not feel bad.\x02\x03",
            "#00000FSo, what is lecture?\x01",
            "Is it okay with the end?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B71C")


    ChrTalk(
        0x9,
        (
            "#11PYes, even the police headquarters\x01",
            "I will let you report from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell then in the end -\x01",
            "If there is a question about the auction\x01",
            "I will let you answer anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PDo you have anything you would like to ask again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FThat's right.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C548")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "About tactical auction\x01",        # 0
            "About Quartz\x01",                # 1
            "About opening the slot\x01",          # 2
            "About slot reinforcement\x01",          # 3
            "About conductivity magic (Arts)\x01",      # 4
            "About Enigma\x01",              # 5
            "マスターAbout Quartz\x01",        # 6
            "quit\x01",                          # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B8F7"),
        (1, "loc_BAD8"),
        (2, "loc_BC17"),
        (3, "loc_BD55"),
        (4, "loc_BEDC"),
        (5, "loc_C0F0"),
        (6, "loc_C2D2"),
        (SWITCH_DEFAULT, "loc_C534"),
    )


    label("loc_B8F7")


    ChrTalk(
        0x9,
        (
            "#11P#11P\"Tactical orbement\"\x01",
            "Specialized for battle\x01",
            "It's a small portable power guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#11PIn addition to enhancing the user's abilities\x01",
            "Power magic#8RArts#It also supports the use of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PGenerally, simply \"an aim\"\x01",
            "There are many things called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POrdered to individuals\x01",
            "Because it is perfectly adjusted,\x01",
            "The structure differs depending on the owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere are slots with attribute limitations,\x01",
            "Line connecting slots#2Rline#There are different forms.\x01",
            "It may be good to compare them once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BAD8")


    ChrTalk(
        0x9,
        (
            "#11PQuartz is made by refining sepis\x01",
            "About \"crystal circuit\" for the orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you bring even the necessary sepises\x01",
            "I can synthesize with my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere are various effects depending on quartz,\x01",
            "When the attribute value becomes equal to or greater than a certain value\x01",
            "Power magic#8RArts#You will be able to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIf sepis gathers up try it a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BC17")


    ChrTalk(
        0x9,
        (
            "#11PThe slot of the auction\x01",
            "In the beginning most of it is unopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo to set quartz\x01",
            "First of all I need to open the slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you open the slot,\x01",
            "That's why we can also add quartz\x01",
            "The maximum EP will also rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFor opening it requires sepice,\x01",
            "I think it will not be damaged as soon as possible to open it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BD55")


    ChrTalk(
        0x9,
        (
            "#11PIn the quartz, \"Top Quartz\" and\x01",
            "There is something called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThis is too strong, it's an ordinary slot\x01",
            "I can not set it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen,\x01",
            "It is strengthening the slot itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSepis is necessary as well as opening,\x01",
            "The maximum EP will also rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI do not think that strengthening will be impatient,\x01",
            "To power up the auction\x01",
            "It can be said to be an indispensable element.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BEDC")


    ChrTalk(
        0x9,
        (
            "#11PMagic to activate using tactical orbient\x01",
            "The so-called guiding magic#8ROval Arts#Right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThere are many things called simply \"Arts\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PArts, the set quartz\x01",
            "By \"sum of attribute values per line\"\x01",
            "The type that can be activated is decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn other words, the set quartz\x01",
            "The higher the attribute value,\x01",
            "You can increase the number of available arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIncidentally, more powerful arts\x01",
            "If you want to use it, also combine attribute values\x01",
            "It gets important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFor more information about that,\x01",
            "Because the list is listed in the investigation notebook\x01",
            "Please refer to that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C0F0")


    ChrTalk(
        0x9,
        (
            "#11PTaking over the communication function of Enigma,\x01",
            "A successor to which a bold remodeling was given -\x01",
            "That is \"Enigma 嘦\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe only biggest change is that,\x01",
            "Newly referred to as \"Master Quartz\"\x01",
            "It has been dealt with special quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way, it seems mostly ….\x01",
            "With this version upgrade\x01",
            "There is a change in the basic architecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo, with compatibility issues\x01",
            "Quartz used in old Enigma\x01",
            "I can not do any set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo, to use Enigma\x01",
            "You will need a new standard quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C2D2")


    ChrTalk(
        0x9,
        (
            "#11PMaster Quartz,\x01",
            "Fits in the center of Enigma\x01",
            "It's about special quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat is decisively different from traditional quartz\x01",
            "That means that it \"grows\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWith it set in the auction\x01",
            "By repeating battle, the level got higher\x01",
            "It will show more powerful effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEnhance user ability,\x01",
            "Special effect of quartz, attribute value … ….\x01",
            "These are three major growth factors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way Master Quartz\x01",
            "If you nurture anything to the end\x01",
            "It seems to be very powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHow to raise the level\x01",
            "It seems that it will take quite a while … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWithout cheating, what you like\x01",
            "It may be important to keep using it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C534")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C543")

    label("loc_C543")

    Jump("loc_B7FF")

    label("loc_C548")


    ChrTalk(
        0x101,
        (
            "#6P#00004F…… Is this enough?\x02\x03",
            "#00000Fありがとう、Wendy。\x01",
            "I learned today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHehe, I wish it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy the way,\x01",
            "Quartz of the new standard for Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom me to the Special Affairs Support Division\x01",
            "Celebrate the restart and give a present.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '鹰目'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鹰目', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00002F悪いな、Wendy。\x01",
            "I will surely use it effectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FIt really helps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHehe, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnyway, something again\x01",
            "If there is something you do not understand\x01",
            "Please listen anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven at the next counter\x01",
            "A variety of new services\x01",
            "I plan to offer it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom now on,\x01",
            "Oval store \"Genten\"\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHuh, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FThank you for today.\x01",
            "Thank you very much.\x02",
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
            "Quest 【Training course of Enigma】\x07\x00",
            "Achieved!\x02",
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

    # Function_23_B2E9 end

    def Function_24_C8E3(): pass

    label("Function_24_C8E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-6460, 1500, 2290, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CA5D")
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

    def lambda_C9AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_C9AE)

    def lambda_C9BF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C9BF)

    def lambda_C9D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C9D4)

    def lambda_C9E5():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C9E5)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CA0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CA0E)

    def lambda_CA1F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA1F)
    Sleep(100)

    def lambda_CA37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA37)

    def lambda_CA48():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CA48)
    Jump("loc_CCD8")

    label("loc_CA5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CB9D")
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

    def lambda_CAEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_CAEE)

    def lambda_CAFF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CAFF)

    def lambda_CB14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CB14)

    def lambda_CB25():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB25)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CB4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CB4E)

    def lambda_CB5F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB5F)
    Sleep(100)

    def lambda_CB77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CB77)

    def lambda_CB88():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CB88)
    Jump("loc_CCD8")

    label("loc_CB9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CCD8")
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

    def lambda_CC2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_CC2E)

    def lambda_CC3F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CC3F)

    def lambda_CC54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC54)

    def lambda_CC65():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC65)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CC8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CC8E)

    def lambda_CC9F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC9F)
    Sleep(100)

    def lambda_CCB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CCB7)

    def lambda_CCC8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CCC8)

    label("loc_CCD8")

    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        (
            "Even in various magazines here\x01",
            "Have been taken up\x01",
            "It's an oval store ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Interior decoration is good, it is good to put in place,\x01",
            "It feels like cutting edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Probably also in the Republic\x01",
            "I think that there was no store of scale … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, certainly the products of each country\x01",
            "In this way all that comes together\x01",
            "It's about cross bells.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAnd, to say the cutting edge\x01",
            "Here is a powerful net terminal\x01",
            "I'm leaving.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Derive force net … … what is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CEBB")

    def lambda_CE9E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE9E)
    Sleep(50)

    def lambda_CEAE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEAE)
    Jump("loc_CF0C")

    label("loc_CEBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CEE6")

    def lambda_CEC9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEC9)
    Sleep(50)

    def lambda_CED9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CED9)
    Jump("loc_CF0C")

    label("loc_CEE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CF0C")

    def lambda_CEF4():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEF4)
    Sleep(50)

    def lambda_CF04():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CF04)

    label("loc_CF0C")


    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, easy to say and traditional\x01",
            "Technology that developed communication equipment.\x02\x03",
            "#00004FThe place called Epstein Foundation\x01",
            "At the center, these plans\x01",
            "I am progressing … ….\x02\x03",
            "#00000FIf you use a terminal, not only voice\x01",
            "Information such as characters and images\x01",
            "We can send each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "To, hehe … ….\x01",
            "Can you do such a thing?\x02",
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
            "Fu, Fun, I am different\x01",
            "I am not surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It was about showing off such knowledge\x01",
            "You do not feel bad!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D197")
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
            "#6P#00006FNo, I do not care\x01",
            "It is not becoming ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FHa, it is not obedient, is a small boy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D334")

    label("loc_D197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D271")
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
            "#6P#00006FNo, I do not care\x01",
            "It is not becoming ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHe says he is not honest,\x01",
            "It seems I was badly regretted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D334")

    label("loc_D271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D334")
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
            "#6P#00006FNo, I do not care\x01",
            "It is not becoming ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHuh, yeah\x01",
            "I guess it was frustrating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D334")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 5)
    OP_29(0x73, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4800, 0, 2530, 90)
    EventEnd(0x5)
    Return()

    # Function_24_C8E3 end

    def Function_25_D360(): pass

    label("Function_25_D360")

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
        "Oh Lloyd, something for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Miscon's 'craftsman' frame … …\x01",
            "I wonder if she is right? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Well, this kind of thing is\x01",
            "It seems not to be very interesting, but …\x01",
            "Would you like to ask and ask? )\x02\x03",
            "#00000F……Wendy、ちょっといいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "Misako … …? what is that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Of the new orb\x01",
            "Is it a part or something?\x02",
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
            "#00306FNo, no no.\x01",
            "全然違うぜWendyちゃん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FTruly a craftsman ……\x01",
            "Is it obvious that I am not secular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, let's go.\x01",
            "You know that to fossil.\x01",
            "In short it's about the girls contest, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is that so, it looks interesting ……\x01",
            "May I join you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs it true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHehe, it is somewhat surprising.\x01",
            "I can get OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, everything is an experience ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am asking for my best friendhood\x01",
            "I will accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until the program starts\x01",
            "Since I am working, when I need it\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I understand.\x01",
            "ありがとな、Wendy。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8DD")

    ChrTalk(
        0x101,
        (
            "#00000F─ ─ Now, at last\x01",
            "Participants' frame was filled.\x02\x03",
            "Citizen会館に行って\x01",
            "Let 's report to Roy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_D8DD")

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

    # Function_25_D360 end

    def Function_26_D910(): pass

    label("Function_26_D910")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, now I am going to shop\x01",
            "I can not come out.\x02\x03",
            "After setting the master quartz\x01",
            "Wendyに声を掛けよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 0, 2230, 90)
    EventEnd(0x4)
    Return()

    # Function_26_D910 end

    SaveToFile()

Try(main)
