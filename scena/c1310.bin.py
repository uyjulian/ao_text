from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "Guard Wong",             # 1
        "Guard Paul",             # 2
        "Receptionist Lanfei",    # 3
        "Receptionist Korinna",   # 4
        "Trader Rizel",           # 5
        "Citizen",                # 6
        "Chief Roberts",          # 7
        "Jona",                   # 8
        "Mayor Dieter",           # 9
        "Mariabell",              # 10
    ))

    AddCharChip((
        "chr/ch27900.itc",                   # 00
        "chr/ch29300.itc",                   # 01
        "chr/ch28600.itc",                   # 02
        "chr/ch30500.itc",                   # 03
        "chr/ch21800.itc",                   # 04
        "chr/ch27702.itc",                   # 05
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294961566, 300,     29909,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294962456, 0,       18180,   90,   261,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    385,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6500,    0,       17850,   270,  385,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 30,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  4,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  10, 0x0000)

    ChipFrameInfo(744, 0)                                        # 0

    ScpFunction((
        "Function_0_2E8",          # 00, 0
        "Function_1_3A0",          # 01, 1
        "Function_2_551",          # 02, 2
        "Function_3_558",          # 03, 3
        "Function_4_5B4",          # 04, 4
        "Function_5_5B8",          # 05, 5
        "Function_6_718",          # 06, 6
        "Function_7_2097",         # 07, 7
        "Function_8_27F5",         # 08, 8
        "Function_9_27FF",         # 09, 9
        "Function_10_295C",        # 0A, 10
        "Function_11_2960",        # 0B, 11
        "Function_12_3848",        # 0C, 12
        "Function_13_47AD",        # 0D, 13
        "Function_14_4C53",        # 0E, 14
        "Function_15_59DD",        # 0F, 15
        "Function_16_6661",        # 10, 16
        "Function_17_7D4A",        # 11, 17
        "Function_18_7D73",        # 12, 18
        "Function_19_7D8A",        # 13, 19
        "Function_20_7DA1",        # 14, 20
        "Function_21_7DB8",        # 15, 21
        "Function_22_7DCF",        # 16, 22
        "Function_23_9B96",        # 17, 23
        "Function_24_B659",        # 18, 24
        "Function_25_B936",        # 19, 25
        "Function_26_BA61",        # 1A, 26
        "Function_27_BC13",        # 1B, 27
        "Function_28_BF51",        # 1C, 28
        "Function_29_BFBE",        # 1D, 29
        "Function_30_CD41",        # 1E, 30
    ))


    def Function_0_2E8(): pass

    label("Function_0_2E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_328"),
        (1, "loc_334"),
        (2, "loc_340"),
        (3, "loc_34C"),
        (4, "loc_358"),
        (5, "loc_364"),
        (6, "loc_370"),
        (SWITCH_DEFAULT, "loc_37C"),
    )


    label("loc_328")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_334")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_340")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_34C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_358")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_364")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_37C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_39F")

    Return()

    # Function_0_2E8 end

    def Function_1_3A0(): pass

    label("Function_1_3A0")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    ClearScenarioFlags(0x25, 1)
    Event(0, 2)

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_425")
    Jump("loc_4F4")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_433")
    Jump("loc_4F4")

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_446")
    SetChrFlags(0xB, 0x10)
    Jump("loc_4F4")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4F4")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462")
    Jump("loc_4F4")

    label("loc_462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_470")
    Jump("loc_4F4")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_497")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4F4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4EB")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1")
    SetChrFlags(0xB, 0x10)

    label("loc_4D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0xE, 0x80)

    label("loc_4E6")

    Jump("loc_4F4")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4F4")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    SetChrPos(0x0, 60, 300, 28550, 0)

    label("loc_511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53A")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_550")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_550")

    Return()

    # Function_1_3A0 end

    def Function_2_551(): pass

    label("Function_2_551")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_551 end

    def Function_3_558(): pass

    label("Function_3_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_59D")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_59D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x324, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B3")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5B3")

    Return()

    # Function_3_558 end

    def Function_4_5B4(): pass

    label("Function_4_5B4")

    Call(0, 5)
    Return()

    # Function_4_5B4 end

    def Function_5_5B8(): pass

    label("Function_5_5B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E1")
    Call(0, 29)
    Return()

    label("loc_5E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    Call(0, 24)
    Jump("loc_620")

    label("loc_61D")

    Call(0, 26)

    label("loc_620")

    Return()

    label("loc_621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")
    Call(0, 22)
    Return()

    label("loc_64A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F")
    Call(0, 6)
    Jump("loc_714")

    label("loc_65F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_714")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Cancel\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70F")

    label("loc_6DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F3")
    Jump("loc_70F")

    label("loc_6F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_70F")

    Jump("loc_669")

    label("loc_714")

    TalkEnd(0xA)
    Return()

    # Function_5_5B8 end

    def Function_6_718(): pass

    label("Function_6_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_726")
    Jump("loc_2096")

    label("loc_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_734")
    Jump("loc_2096")

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_89E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_813")

    ChrTalk(
        0xA,
        (
            "To think Mainz is\x01",
            "occupied and civilians\x01",
            "are involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I worry that IBC will be\x01",
            "affected. This could affect\x01",
            "stock prices before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I pray the\x01",
            "people of Mainz are\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_899")

    label("loc_813")


    ChrTalk(
        0xA,
        (
            "I worry that IBC will be\x01",
            "affected. This could affect\x01",
            "stock prices before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I pray the\x01",
            "people of Mainz are\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899")

    Jump("loc_2096")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AC")

    ChrTalk(
        0xA,
        (
            "The more you interact with\x01",
            "the orbal network, the\x01",
            "more fascinating it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Korinna likes the orbal games\x01",
            "best, while I am partial to\x01",
            "the weather forecasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's not 100 percent, but\x01",
            "it's fairly accurate. I\x01",
            "check it every day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A44")

    label("loc_9AC")


    ChrTalk(
        0xA,
        (
            "The weather forecasts\x01",
            "from the orbal network\x01",
            "are fairly accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Today's forecast is "Rain\x01",
            "with some sun― And likely\x01",
            "clear this afternoon".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A44")

    Jump("loc_2096")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA3")

    ChrTalk(
        0xA,
        (
            "Only one or two in our company can\x01",
            "challenge Korinna's skill with the\x01",
            "terminal... Or her skill with the game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Test requests for various game\x01",
            "software come in every now and\x01",
            "then from the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though I call them requests, we\x01",
            "take care of them on a voluntary\x01",
            "basis outside of business hours.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C07")

    label("loc_BA3")


    ChrTalk(
        0xA,
        (
            "Even so, to think one could look\x01",
            "that happy looking at a screen...\x01",
            "Haha, I'm a little envious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C07")

    Jump("loc_2096")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3")

    ChrTalk(
        0xA,
        (
            "Please allow us to\x01",
            "assist you with anything\x01",
            "we're able.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I can assist you in\x01",
            "the future, please do\x01",
            "not hesitate to stop by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6E")

    label("loc_CB3")


    ChrTalk(
        0xA,
        (
            "Acting President Mariabell\x01",
            "returned from her business\x01",
            "trip yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because she just returned, she's been\x01",
            "very busy managing the various\x01",
            "departments since early this morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6E")

    Jump("loc_2096")

    label("loc_D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_178D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D7")

    ChrTalk(
        0xA,
        (
            "Ah, everyone. If you are looking\x01",
            "for Acting President Mariabell,\x01",
            "she is on a trip abroad...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 0)), scpexpr(EXPR_END)), "loc_E52")

    ChrTalk(
        0x101,
        (
            "#00005FActing President\x01",
            "Mariabell...\x02\x03",
            "#00003FOh, they reported that\x01",
            "in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7D")

    label("loc_E52")


    ChrTalk(
        0x101,
        (
            "#00005FActing President\x01",
            "Mariabell...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E7D")


    ChrTalk(
        0x102,
        (
            "#00100FYes. The board of directors took over\x01",
            ""uncle's" presidential duties, and it\x01",
            "seems she was appointed right after that.\x02\x03",
            "#00104FIn other words, Bell is the leader of\x01",
            "IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWow, to get to such a\x01",
            "position at her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIf it's Mariabell, then\x01",
            "I can agree with that,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FYeah. Thinking about it\x01",
            "again, it's unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAnd, I think her workload\x01",
            "can't be compared to how\x01",
            "much it's been up until now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, you're correct, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So that the young lady won't be overburdened\x01",
            "by her responsibilities, the entire board of\x01",
            "directors is supporting her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that she is acting president,\x01",
            "she is required to show up in all\x01",
            "manner of different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... She must be\x01",
            "very busy, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, the young\x01",
            "lady plans to return\x01",
            "this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although she has a schedule\x01",
            "tomorrow filled with meetings,\x01",
            "consultations and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm terribly sorry, but I don't\x01",
            "think you'll be able to see Miss\x01",
            "Mariabell for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1666")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "That's right― The young\x01",
            "lady has a message for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Mariabell's Account]\x01\x07\x00",
            "received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 6)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        (
            "#00005FT-This is... A "Pom!"\x01",
            "account!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMariabell plays too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#18C"Haha, I am of course\x01",
            "interested in this as a member\x01",
            "of the Technology Division."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#18C"Please, register my name. I would\x01",
            "be more than happy to beat you\x01",
            "senseless with my superior skills."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...That's what it says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, that just now\x01",
            "was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FWas she trying to\x01",
            "predict Lloyd's\x01",
            "reaction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F...I think so. Bell's\x01",
            "capable of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As expected of Lady\x01",
            "Elie. That's exactly\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, she's really a big\x01",
            "deal.\x02\x03",
            "#10302FAnd, you do a great\x01",
            "impression of her voice,\x01",
            "miss.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "A-Ah... Perhaps I\x01",
            "projected too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Anyway, that's all\x01",
            "for the message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The young lady is never far\x01",
            "from a terminal, so why not\x01",
            "challenge her right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16CF")

    label("loc_1666")


    ChrTalk(
        0x102,
        (
            "#00104FYes, we understand.\x02\x03",
            "#00100FLanfei, please tell Bell\x01",
            "to not overdo it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()

    label("loc_16CF")

    SetScenarioFlags(0x16D, 0)
    Jump("loc_1788")

    label("loc_16D7")


    ChrTalk(
        0xA,
        (
            "Acting President Mariabell\x01",
            "will be back from her business\x01",
            "trip this evening, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm terribly sorry. For now,\x01",
            "I don't think the young lady\x01",
            "will be able to see you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1788")

    Jump("loc_2096")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B1E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A8")

    ChrTalk(
        0xA,
        (
            "It seems like we'll need to\x01",
            "increase building security\x01",
            "even further going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, thank you very\x01",
            "much for recovering Miss\x01",
            "Mariabell's stolen dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please ask us if you ever\x01",
            "need anything. We will of\x01",
            "course welcome you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1944")

    label("loc_18A8")


    ChrTalk(
        0xA,
        (
            "Anyway, thank you very\x01",
            "much for recovering Miss\x01",
            "Mariabell's stolen dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please ask us if you ever\x01",
            "need anything. We will of\x01",
            "course welcome you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1944")

    Jump("loc_1B19")

    label("loc_1949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A50")

    ChrTalk(
        0xA,
        (
            "If you have that\x01",
            "authentication card, you\x01",
            "can use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You should be able to go\x01",
            "to the same floors as the\x01",
            "one I gave you all before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Miss Mariabell is waiting for\x01",
            "you in the president's office\x01",
            "on 16F, so please go there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B19")

    label("loc_1A50")


    ChrTalk(
        0xA,
        (
            "If you have that authentication\x01",
            "card, you should be able to go to\x01",
            "the same floors as you could before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Miss Mariabell is waiting for\x01",
            "you in the president's office\x01",
            "on 16F, so please go there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B19")

    Jump("loc_2096")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B2C")
    Jump("loc_2096")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E03")

    ChrTalk(
        0xA,
        (
            "Ah, everyone. Welcome to\x01",
            "IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have business here, please\x01",
            "finish it today. Because there is a\x01",
            "special business holiday tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA special holiday?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf I remember correctly, Republican\x01",
            "President Rocksmith is coming to\x01",
            "IBC tomorrow for an inspection.\x02\x03",
            "Is it for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You truly do get\x01",
            "information quickly, Lady\x01",
            "Elie. It is as you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "President Rocksmith is\x01",
            "the VIP of VIPs, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The businesses in this building\x01",
            "are going all out today to be\x01",
            "ready to receive him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FI see. Michelam must be\x01",
            "the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that's only\x01",
            "natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe understand the\x01",
            "situation for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you for letting us\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 7)
    Jump("loc_1EAC")

    label("loc_1E03")


    ChrTalk(
        0xA,
        (
            "Tomorrow is a special\x01",
            "IBC business holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone, if you have business here,\x01",
            "please finish it today. Because there\x01",
            "is a special business holiday tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAC")

    Jump("loc_2096")

    label("loc_1EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F39")

    ChrTalk(
        0xA,
        (
            "It looks like you're\x01",
            "finished with Chief's\x01",
            "request. Haha, good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Allow me to thank you as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE4")

    label("loc_1F39")


    ChrTalk(
        0xA,
        (
            "Chief Roberts is always busy at\x01",
            "the Epstein Foundation branch\x01",
            "office in this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In addition, he has helped\x01",
            "us with many things\x01",
            "relating to the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE4")

    Jump("loc_2096")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2004")
    Call(0, 7)
    Jump("loc_2096")

    label("loc_2004")


    ChrTalk(
        0xA,
        (
            "We want to be of maximum\x01",
            "convenience to everyone at\x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From now on, please tell\x01",
            "me if you ever need\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2096")

    Return()

    # Function_6_718 end

    def Function_7_2097(): pass

    label("Function_7_2097")

    EventBegin(0x0)
    Fade(500)
    OP_68(-370, 1800, 29450, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -770, 300, 29530, 0)
    SetChrPos(0x102, 430, 300, 29130, 0)
    SetChrPos(0x109, -1270, 300, 28130, 0)
    SetChrPos(0x105, 530, 300, 27920, 0)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()
    Sleep(100)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#5POh, Lloyd and Elie. Long\x01",
            "time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt looks like the SSS\x01",
            "has started back up\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWe look forward to\x01",
            "working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PI'm always happy to.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_241F")

    ChrTalk(
        0xA,
        (
            "#5POh yes, I think we received assistance\x01",
            "from the Support Section before in\x01",
            "setting up our new exchange service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PActually, the expiration\x01",
            "date on the card I gave\x01",
            "you before has passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI have prepared a new\x01",
            "one for you, so please\x01",
            "take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#5PPlease present your card\x01",
            "at the exchange counter,\x01",
            "just like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe'll convert sepith to\x01",
            "mira for you at a better\x01",
            "rate than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259C")

    label("loc_241F")


    ChrTalk(
        0xA,
        (
            "#5PCome to think of it, I\x01",
            "have something to give\x01",
            "all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PPlease accept this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00005FThis card is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is card that identifies\x01",
            "you as a preferred\x01",
            "customer at our bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you present it at the counter,\x01",
            "you can exchange sepith for mira\x01",
            "at a higher rate than normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259C")


    ChrTalk(
        0x109,
        (
            "#12P#10105FI-Is it really ok for us\x01",
            "to use a service like\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, of course. You are all\x01",
            "good friends of both Mayor\x01",
            "Crois and Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThis accommodation is\x01",
            "only a matter of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHeh, then I guess we'll\x01",
            "make good use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, let's do just that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHaha. We'll be waiting\x01",
            "for your next visit.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※You can use IBC's exchange service.\x01",
            "The exchange rate is higher than you\x01",
            "get from normal shops.\x02\x03",
            "Just talk to Lanfei and choose\x01",
            "[Exchange] to use this service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x134, 4)
    EventEnd(0x5)
    Return()

    # Function_7_2097 end

    def Function_8_27F5(): pass

    label("Function_8_27F5")

    TalkBegin(0xFE)
    Call(0, 9)
    TalkEnd(0xFE)
    Return()

    # Function_8_27F5 end

    def Function_9_27FF(): pass

    label("Function_9_27FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289B")
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "One moment, please.\x01",
            "(*furious typing*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was just querying your\x01",
            "contracts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, I'm counting on\x01",
            "you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_295B")

    label("loc_289B")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xD,
        (
            "Hmm? What's with you?\x01",
            "You're not thinking of\x01",
            "interrupting me, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm terribly sorry.\x01",
            "Please wait your turn on\x01",
            "that sofa over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_295B")

    Return()

    # Function_9_27FF end

    def Function_10_295C(): pass

    label("Function_10_295C")

    Call(0, 11)
    Return()

    # Function_10_295C end

    def Function_11_2960(): pass

    label("Function_11_2960")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2971")
    Jump("loc_3844")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_297F")
    Jump("loc_3844")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A44")

    ChrTalk(
        0xB,
        (
            "I heard a dangerous\x01",
            "bunch attacked Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, I'm not even sure\x01",
            "our Security Department\x01",
            "could deal with them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My oh my. That's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2ADE")

    label("loc_2A44")


    ChrTalk(
        0xB,
        (
            "Honestly, I'm not even sure our\x01",
            "Security Department could deal with\x01",
            "the armed group that attacked Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My oh my. That's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADE")

    Jump("loc_3844")

    label("loc_2AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B7E")

    ChrTalk(
        0xB,
        (
            "It's troublesome going\x01",
            "out on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When the orbal net is more\x01",
            "widespread, there will also be\x01",
            "jobs that can be done at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E25")

    ChrTalk(
        0xB,
        "(*furious typing*)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(shoom, bang bang bang\x01",
            "bang bang!)\x02",
        )
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1F")

    ChrTalk(
        0x101,
        (
            "#00005FW-What in the world is\x01",
            "that sound?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2C1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")

    ChrTalk(
        0x102,
        (
            "#00105FI-I wonder what sound\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2C5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB4")

    ChrTalk(
        0x103,
        (
            "#00203F...This sound is the\x01",
            "foundation's latest\x01",
            "shooting game.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2CB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE8")

    ChrTalk(
        0x104,
        "#00305FW-What's that sound?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2CE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1D")

    ChrTalk(
        0x109,
        "#10105FA-Are these gunshots?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(
        0x105,
        "#10302FHaha, looks fun.\x02",
    )

    CloseMessageWindow()

    label("loc_2D48")

    Sleep(50)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "I'm terribly sorry, everyone. As\x01",
            "you can see, I'm actually in the\x01",
            "middle of my break time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Accordingly, please speak with\x01",
            "the main receptionist,\x01",
            "whatever your business may be.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FEF")

    label("loc_2E25")


    ChrTalk(
        0xB,
        "(*furious typing*)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(shoooom, ratta ratta\x01",
            "ratta!)\x02",
        )
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB0")

    ChrTalk(
        0x101,
        (
            "#00012F(S-She has amazing\x01",
            "concentration...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEF")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EEE")

    ChrTalk(
        0x102,
        (
            "#00106F(W-We shouldn't bother\x01",
            "her...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEF")

    label("loc_2EEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F49")

    ChrTalk(
        0x103,
        (
            "#00205F(This counterattack!\x01",
            "...She's definitely\x01",
            "better than Jona.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEF")

    label("loc_2F49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F83")

    ChrTalk(
        0x104,
        (
            "#00306F(We shouldn't bother\x01",
            "her.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEF")

    label("loc_2F83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC2")

    ChrTalk(
        0x109,
        (
            "#10106F(Such intense\x01",
            "concentration...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEF")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEF")

    ChrTalk(
        0x105,
        "#10302F(Haha, nice move.)\x02",
    )

    CloseMessageWindow()

    label("loc_2FEF")

    Jump("loc_3844")

    label("loc_2FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30A2")

    ChrTalk(
        0xB,
        (
            "Because of how busy Mariabell\x01",
            "has been lately, sometimes she\x01",
            "doesn't get to have lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While travelling, she\x01",
            "often carries block-type\x01",
            "portable food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_30A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_32D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3235")

    ChrTalk(
        0xB,
        (
            "Ever since the mayor's independence\x01",
            "proposal, it seems continental\x01",
            "financial markets have become unstable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There haven't been extreme deviations,\x01",
            "but there has been an increase in\x01",
            "speculation on both sides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is it a good idea or not?\x01",
            "...Everything is up to\x01",
            "the people of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, they say stock indices\x01",
            "follow the same pattern a\x01",
            "person's life does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32D3")

    label("loc_3235")


    ChrTalk(
        0xB,
        (
            "It seems that Rizel has become more\x01",
            "cautious. I wonder if it's due to\x01",
            "reflection on his past failures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Personally, I think it's\x01",
            "the right decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D3")

    Jump("loc_3844")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3407")

    ChrTalk(
        0xB,
        (
            "Yesterday, I took the\x01",
            "day off for the\x01",
            "President's visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I didn't feel like going out due\x01",
            "to the security, and before I knew\x01",
            "it I spent the whole day in bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had the energy for it, but since\x01",
            "I have an orbal net terminal at\x01",
            "home, I really didn't feel like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34A6")

    label("loc_3407")


    ChrTalk(
        0xB,
        (
            "If I had an orbal net terminal\x01",
            "at home, I really wouldn't\x01",
            "have gone out yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because if I did, I\x01",
            "would have spent the day\x01",
            "playing orbal games.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A6")

    Jump("loc_3844")

    label("loc_34AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34B9")
    Jump("loc_3844")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34CA")
    Call(0, 9)
    Jump("loc_3844")

    label("loc_34CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_35F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3590")

    ChrTalk(
        0xB,
        "(*furious typing*)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        (
            "As expected, there are\x01",
            "fewer customers on rainy\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is a good chance to\x01",
            "take care of the paperwork\x01",
            "that has piled up.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_35EE")

    label("loc_3590")


    ChrTalk(
        0xB,
        (
            "The business just won't run if\x01",
            "there aren't days like this\x01",
            "every once in a while, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EE")

    Jump("loc_3844")

    label("loc_35F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3798")

    ChrTalk(
        0xB,
        (
            "The Technology Division has\x01",
            "cleared the initial stage of\x01",
            "the level 2 orbal network test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Putting it simply, the capabilities are\x01",
            "additional security and higher capacity,\x01",
            "more reliable data transmission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to that, we've started\x01",
            "work on connecting company\x01",
            "terminals to outside networks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This must be the potential\x01",
            "of the Technology Division\x01",
            "staff led by Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3844")

    label("loc_3798")


    ChrTalk(
        0xB,
        (
            "It seems that Mayor Crois\x01",
            "also helped with completing\x01",
            "the level 2 test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As long as it's unclassified\x01",
            "documents, you can already\x01",
            "transfer them over the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3844")

    TalkEnd(0xB)
    Return()

    # Function_11_2960 end

    def Function_12_3848(): pass

    label("Function_12_3848")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3859")
    Jump("loc_47A9")

    label("loc_3859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3867")
    Jump("loc_47A9")

    label("loc_3867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3908")

    ChrTalk(
        0xFE,
        (
            "It seems something\x01",
            "terrible has happened at\x01",
            "Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it hasn't affected\x01",
            "financial markets at present,\x01",
            "it's just a matter of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A9")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5D")

    ChrTalk(
        0xFE,
        (
            "Who will profit from this and\x01",
            "who will suffer losses? The\x01",
            "speculation will tell that tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And one more thing... In the\x01",
            "world of speculation, there is\x01",
            "no such thing as an "absolute".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are getting started in speculation,\x01",
            "I strongly recommend you commit only those\x01",
            "funds you're willing to risk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B54")

    label("loc_3A5D")


    ChrTalk(
        0xFE,
        (
            "If you are getting started in speculation,\x01",
            "I strongly recommend you commit only those\x01",
            "funds you're willing to risk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the world of speculation there are no\x01",
            "absolutes, but... I believe actions that\x01",
            "go above one's stature lead to sorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B54")

    Jump("loc_47A9")

    label("loc_3B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C27")

    ChrTalk(
        0xFE,
        "W-What did you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that a stock whose price\x01",
            "was so high this morning could\x01",
            "have already fallen this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...This is why I don't\x01",
            "understand speculation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CC1")

    label("loc_3C27")


    ChrTalk(
        0xFE,
        (
            "To think that a stock whose price\x01",
            "was so high this morning could\x01",
            "have already fallen this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...This is why I don't\x01",
            "understand speculation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC1")

    Jump("loc_47A9")

    label("loc_3CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB8")

    ChrTalk(
        0xFE,
        (
            "Hmm. Price movements were\x01",
            "seen in the Republic\x01",
            "region this morning, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bought that stock I\x01",
            "had my eye on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what I say at this\x01",
            "late hour, it amounts to\x01",
            "nothing more than hindsight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E41")

    label("loc_3DB8")


    ChrTalk(
        0xFE,
        (
            "I bought that stock I\x01",
            "had my eye on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what I say at this\x01",
            "late hour, it amounts to\x01",
            "nothing more than hindsight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E41")

    Jump("loc_47A9")

    label("loc_3E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F32")

    ChrTalk(
        0xFE,
        (
            "As I thought... Stock\x01",
            "prices are unstable\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. It's rare for prices\x01",
            "to swing this much yet be\x01",
            "so difficult to read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The risk is great... This\x01",
            "is no time for amateurs\x01",
            "to get involved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FA9")

    label("loc_3F32")


    ChrTalk(
        0xFE,
        (
            "Before, I jumped in\x01",
            "without paying attention\x01",
            "to the risk, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it would have been\x01",
            "better if I hadn't.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA9")

    Jump("loc_47A9")

    label("loc_3FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_41E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F8")

    ChrTalk(
        0xFE,
        (
            "As a trader, I have to pay attention\x01",
            "to how the trade conference goes\x01",
            "whether I like it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, if they have the\x01",
            "chance, the Empire and Republic\x01",
            "will try to have their own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What sort of demands will those\x01",
            "nations place on us? It's a chance\x01",
            "for Mayor Dieter to show his skill.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41DD")

    label("loc_40F8")


    ChrTalk(
        0xFE,
        (
            "Regarding our trade relationships, if\x01",
            "they have the chance, the Empire and\x01",
            "Republic will try to have their own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What sort of demands will those\x01",
            "nations place on us? It's a chance\x01",
            "for Mayor Dieter to show his skill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DD")

    Jump("loc_47A9")

    label("loc_41E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41F0")
    Jump("loc_47A9")

    label("loc_41F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D1")

    ChrTalk(
        0xFE,
        (
            "I'm not sure whether it's due to the\x01",
            "trade conference, but stock averages\x01",
            "have risen over the past several days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are some I want to\x01",
            "buy myself, but... I can't\x01",
            "with my current funds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4361")

    label("loc_42D1")


    ChrTalk(
        0xFE,
        (
            "Looking at the stock\x01",
            "prices like this, I want\x01",
            "to buy some, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. For now, I have\x01",
            "no choice but to focus\x01",
            "on my core business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4361")

    Jump("loc_47A9")

    label("loc_4366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4374")
    Jump("loc_47A9")

    label("loc_4374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_47A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4723")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh, you're the Special\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "R-Remember me? I'm that\x01",
            "trader you rescued during\x01",
            "the cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHave you noticed any\x01",
            "change in your health\x01",
            "since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah. I went to see a doctor at\x01",
            "St. Ursula Hospital, and as you\x01",
            "can see, I'm right as rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the incident, my\x01",
            "debt wasn't so high so as\x01",
            "to cause bankruptcy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for your help\x01",
            "back then. I'm grateful\x01",
            "to all of you, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right. If you\x01",
            "like, please take this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FC, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got that from a customer\x01",
            "a while back, but I don't\x01",
            "know how to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, I thought I'd\x01",
            "repay my debt to you\x01",
            "guys with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end it's a\x01",
            "personal gift, so please\x01",
            "just take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood... If that's\x01",
            "how it is, then I'll\x01",
            "gratefully accept it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 5)
    Jump("loc_47A9")

    label("loc_4723")


    ChrTalk(
        0xFE,
        (
            "I'm glad I got to meet\x01",
            "all of you again like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for your help\x01",
            "back then. I'm grateful\x01",
            "to all of you, even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A9")

    TalkEnd(0xFE)
    Return()

    # Function_12_3848 end

    def Function_13_47AD(): pass

    label("Function_13_47AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A30")

    ChrTalk(
        0xFE,
        (
            "Try installing "Pom!" on\x01",
            "the Support Section\x01",
            "terminal for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, contact me\x01",
            "via ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We'll\x01",
            "contact you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FBy the way, is it really\x01",
            "okay for you to install a\x01",
            "game on a police terminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, now that you mention\x01",
            "it... Don't you need\x01",
            "permission for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I already got\x01",
            "permission from the\x01",
            "police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I explained it as a test\x01",
            "case for promotion of the orbal\x01",
            "network, I got permission easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(H-He's good.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Haha. He is the man in\x01",
            "charge of Crossbell's\x01",
            "orbal net after all.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4A9B")

    label("loc_4A30")


    ChrTalk(
        0xFE,
        (
            "Try installing "Pom!" on\x01",
            "the Support Section\x01",
            "terminal for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, contact me\x01",
            "via ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9B")

    Jump("loc_4C4F")

    label("loc_4AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA8")

    ChrTalk(
        0xFE,
        (
            "Thank you for joining me\x01",
            "for a test of "Pom!".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once it's been officially released,\x01",
            "you should speak with various\x01",
            "people and collect their accounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing that and expanding your\x01",
            "circle of friends is the real\x01",
            "pleasure of this game.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4C4F")

    label("loc_4BA8")


    ChrTalk(
        0xFE,
        (
            "When "Pom!" is officially\x01",
            "released, you should\x01",
            "collect a lot of accounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing that and expanding your\x01",
            "circle of friends is the real\x01",
            "pleasure of this game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4F")

    TalkEnd(0xFE)
    Return()

    # Function_13_47AD end

    def Function_14_4C53(): pass

    label("Function_14_4C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C64")
    Jump("loc_59D9")

    label("loc_4C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C72")
    Jump("loc_59D9")

    label("loc_4C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D46")

    ChrTalk(
        0xFE,
        (
            "It seems that armed group\x01",
            "has enough firepower to\x01",
            "overpower even the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard their true identity is Red\x01",
            "Constellation, that jaeger corps of ill\x01",
            "repute... What are we going to do now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D9")

    label("loc_4D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DDA")

    ChrTalk(
        0xFE,
        (
            "I've been busy somehow\x01",
            "ever since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the work's been\x01",
            "difficult. I have to be careful\x01",
            "not to overexert myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D9")

    label("loc_4DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE7")

    ChrTalk(
        0xFE,
        (
            "Now then, it's about\x01",
            "time for the lunch shift\x01",
            "change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what should I have.\x01",
            "I heard today's A lunch\x01",
            "was a meat dish, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, I can't, I cant.\x01",
            "It's not break time yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sheesh. This is a sign\x01",
            "that I'm slacking off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4F66")

    label("loc_4EE7")


    ChrTalk(
        0xFE,
        (
            "When mealtime approaches,\x01",
            "my thoughts inevitably\x01",
            "turn to how hungry I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, my training is\x01",
            "still insufficient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F66")

    Jump("loc_59D9")

    label("loc_4F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5089")

    ChrTalk(
        0xFE,
        (
            "I seems that lately,\x01",
            "unknown monsters have been\x01",
            "appearing within the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We in the Security Department aren't\x01",
            "limited to anti-personnel tactics. We\x01",
            "know a fair bit about fighting monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be extra safe, we\x01",
            "have to be ready for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_513B")

    label("loc_5089")


    ChrTalk(
        0xFE,
        (
            "We in the Security Department aren't\x01",
            "limited to anti-personnel tactics. We\x01",
            "know a fair bit about fighting monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be extra safe, we\x01",
            "have to be ready for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_513B")

    Jump("loc_59D9")

    label("loc_5140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E3")

    ChrTalk(
        0xFE,
        (
            "There's a training room in\x01",
            "this building exclusively\x01",
            "for employee use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, those of us in the\x01",
            "Security Department who need\x01",
            "exercise put it to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been seldom lately,\x01",
            "but I sometimes see Miss\x01",
            "Mariabell in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, I'd never go there to\x01",
            "see her in training gear with\x01",
            "sweat pouring out of her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I put it...\x01",
            "It makes my heart pound.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5364")

    label("loc_52E3")


    ChrTalk(
        0xFE,
        (
            "A-Ahem... I said\x01",
            "something unnecessary\x01",
            "there at the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, our training\x01",
            "room has some of the\x01",
            "best gear around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5364")

    Jump("loc_59D9")

    label("loc_5369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_55DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5463")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5414")

    ChrTalk(
        0xFE,
        (
            "It seems a burglar\x01",
            "entered Miss Mariabell's\x01",
            "room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, I haven't seen any\x01",
            "suspicious persons...\x01",
            "Perhaps I was tricked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_545E")

    label("loc_5414")


    ChrTalk(
        0xFE,
        (
            "Tch, I haven't seen any\x01",
            "suspicious persons...\x01",
            "Perhaps I was tricked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545E")

    Jump("loc_55D9")

    label("loc_5463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(
        0xFE,
        (
            "Thank you for recovering the\x01",
            "young lady's precious dolls.\x01",
            "Please accept my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, we in the\x01",
            "Security Department didn't\x01",
            "sense anyone's presence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of trick\x01",
            "is Phantom Thief B\x01",
            "using!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_55D9")

    label("loc_5553")


    ChrTalk(
        0xFE,
        (
            "Even so, we in the\x01",
            "Security Department didn't\x01",
            "sense anyone's presence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of trick\x01",
            "is Phantom Thief B\x01",
            "using!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D9")

    Jump("loc_59D9")

    label("loc_55DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_55EC")
    Jump("loc_59D9")

    label("loc_55EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_577F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5708")

    ChrTalk(
        0xFE,
        (
            "In advance of the trade conference,\x01",
            "the police and CGF have finally\x01",
            "stepped up their security activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us of the IBC Security\x01",
            "Department are fully\x01",
            "supporting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We received detailed\x01",
            "communications from the\x01",
            "police's security task force.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_577A")

    label("loc_5708")


    ChrTalk(
        0xFE,
        (
            "After all, we have to\x01",
            "help each other out in\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We plan to do all we can\x01",
            "to support you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577A")

    Jump("loc_59D9")

    label("loc_577F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_57FF")

    ChrTalk(
        0xFE,
        (
            "Hmm, our mayor appears\x01",
            "to be very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He must be able to manage\x01",
            "due to the support of\x01",
            "Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D9")

    label("loc_57FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_59D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5923")

    ChrTalk(
        0xFE,
        (
            "Oh, you're the police's\x01",
            "Special Support Section,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome to IBC. If it is something security-\x01",
            "related within the building, we, the\x01",
            "Security Department, will take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us have pride that\x01",
            "our stamina wouldn't lose\x01",
            "to the CGF.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_59D9")

    label("loc_5923")


    ChrTalk(
        0xFE,
        (
            "If it is something security-related\x01",
            "within the building, we, the Security\x01",
            "Department, will take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us have pride that\x01",
            "our stamina wouldn't lose\x01",
            "to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D9")

    TalkEnd(0xFE)
    Return()

    # Function_14_4C53 end

    def Function_15_59DD(): pass

    label("Function_15_59DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_59EE")
    Jump("loc_665D")

    label("loc_59EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_59FC")
    Jump("loc_665D")

    label("loc_59FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5AC1")

    ChrTalk(
        0xFE,
        (
            "It seems that no concrete\x01",
            "demands have come in from\x01",
            "the armed group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even within the Security Department,\x01",
            "guesses are flying about, but... It\x01",
            "can't be helped if it's weird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665D")

    label("loc_5AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B3B")

    ChrTalk(
        0xFE,
        (
            "Good work today,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, it's\x01",
            "raining outside. Please\x01",
            "watch out for your health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665D")

    label("loc_5B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5BDD")

    ChrTalk(
        0xFE,
        (
            "I've hardly seen Mayor\x01",
            "Dieter in this IBC\x01",
            "building recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the mayor is doing\x01",
            "fine, but... I get worried\x01",
            "when I don't see him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665D")

    label("loc_5BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D1D")

    ChrTalk(
        0xFE,
        (
            "It seems the remaining Republican\x01",
            "terrorists that attacked the trade\x01",
            "conference were captured yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand they were discovered trying\x01",
            "to return to the Republic by rail and\x01",
            "there was a disturbance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a real disaster\x01",
            "for everyone else on\x01",
            "board that train.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5DB3")

    label("loc_5D1D")


    ChrTalk(
        0xFE,
        (
            "I understand some terrorist\x01",
            "remnants were discovered on\x01",
            "board a train, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a real disaster\x01",
            "for everyone else on\x01",
            "board that train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB3")

    Jump("loc_665D")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F1C")

    ChrTalk(
        0xFE,
        (
            "More than a month has passed since\x01",
            "Imperial and Republican terrorists\x01",
            "attacked the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that several of the\x01",
            "perpetrators still haven't\x01",
            "been caught, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it won't be that easy for them to return\x01",
            "to their country of origin, it's possible that\x01",
            "even now they're hidden within the state.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5FAF")

    label("loc_5F1C")


    ChrTalk(
        0xFE,
        (
            "I heard that several of the\x01",
            "perpetrators still haven't\x01",
            "been caught, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible that even\x01",
            "now, they're hidden\x01",
            "within the state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FAF")

    Jump("loc_665D")

    label("loc_5FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_602D")

    ChrTalk(
        0xFE,
        (
            "Ah, a robber at IBC... How on\x01",
            "earth could they have slipped\x01",
            "through our security system?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61CB")

    label("loc_602D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6123")

    ChrTalk(
        0xFE,
        (
            "Truly, thank you very\x01",
            "much for resolving the\x01",
            "theft incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was Phantom Thief\x01",
            "B, it's too bad you couldn't\x01",
            "capture the criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, it's a relief\x01",
            "you could safely recover\x01",
            "the stolen property.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_61CB")

    label("loc_6123")


    ChrTalk(
        0xFE,
        (
            "But even so, this\x01",
            "incident was totally a\x01",
            "petty theft, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I'm glad you recovered the\x01",
            "stolen property, I feel there are\x01",
            "even more mysteries now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61CB")

    Jump("loc_665D")

    label("loc_61D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_61DE")
    Jump("loc_665D")

    label("loc_61DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_63AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F4")

    ChrTalk(
        0xFE,
        (
            "An inspection of this IBC building\x01",
            "by the Republican President is\x01",
            "planned for tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In line with that, almost all of\x01",
            "us at the Security Department\x01",
            "will be handling security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm already getting\x01",
            "nervous for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_63A7")

    label("loc_62F4")


    ChrTalk(
        0xFE,
        (
            "An inspection of this IBC building\x01",
            "by the Republican President is\x01",
            "planned for tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think about\x01",
            "tomorrow's security... I'm\x01",
            "already getting nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A7")

    Jump("loc_665D")

    label("loc_63AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6514")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6488")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter and Miss\x01",
            "Mariabell seem even busier\x01",
            "than they were before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even amongst that,\x01",
            "they haven't forgotten to\x01",
            "smile or consider others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that's really\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_650F")

    label("loc_6488")


    ChrTalk(
        0xFE,
        (
            "When I get busy, I never\x01",
            "have time to consider\x01",
            "others, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just on that point\x01",
            "alone, those two are\x01",
            "amazing individuals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_650F")

    Jump("loc_665D")

    label("loc_6514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_665D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65CF")

    ChrTalk(
        0xFE,
        (
            "Welcome to the\x01",
            "International Bank of\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I'm in charge of security,\x01",
            "I can provide simple guidance. What\x01",
            "might your business be today?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_665D")

    label("loc_65CF")


    ChrTalk(
        0xFE,
        (
            "Welcome to the\x01",
            "International Bank of\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are here for banking,\x01",
            "either of the receptionists\x01",
            "on the right can help you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665D")

    TalkEnd(0xFE)
    Return()

    # Function_15_59DD end

    def Function_16_6661(): pass

    label("Function_16_6661")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-640, 1800, 4860, 0)
    MoveCamera(57, 26, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15390, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    SetChrPos(0x101, -610, 300, 2900, 0)
    SetChrPos(0x102, 760, 300, 2650, 0)
    SetChrPos(0x109, -610, 300, 2900, 0)
    SetChrPos(0x105, 760, 300, 2650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("chr/ch05500.itc", 0x1F)
    LoadChrToIndex("apl/ch51116.itc", 0x20)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x10, -610, 300, 24300, 180)
    SetChrPos(0x11, 760, 300, 24800, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_68(-900, 1800, 5640, 3000)

    def lambda_67DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67DF)

    def lambda_67F0():
        OP_98(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67F0)
    Sleep(50)

    def lambda_680D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_680D)

    def lambda_681E():
        OP_98(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_681E)
    Sleep(700)

    def lambda_683B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_683B)

    def lambda_684C():
        OP_98(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_684C)
    Sleep(50)

    def lambda_6869():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6869)

    def lambda_687A():
        OP_98(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_687A)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOk then, we had a\x01",
            "request from Chief\x01",
            "Roberts, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYes. Receptionist Lanfei\x01",
            "will get him for us.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)

    NpcTalk(
        0x10,
        "Man's Voice",
        "Oh, it's all of you...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_68(-1430, 1800, 8130, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15440, 3000)

    def lambda_69D3():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_69D3)
    Sleep(50)

    def lambda_69F0():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_69F0)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#12P#10105FMayor Dieter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAnd Mariabell!\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1700, 14870, 5000)
    MoveCamera(43, 22, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13820, 5000)

    def lambda_6A7B():
        OP_98(0x101, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A7B)
    Sleep(50)

    def lambda_6A98():
        OP_98(0x102, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A98)
    Sleep(50)

    def lambda_6AB5():
        OP_98(0x109, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AB5)
    Sleep(50)

    def lambda_6AD2():
        OP_98(0x105, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6AD2)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10100FYou guys came to IBC\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02800FYeah, work has been\x01",
            "piling up.\x02\x03",
            "#02804FBut thanks to Bell's\x01",
            "help, we just finished\x01",
            "all of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x11,
        (
            "Uhuhu... I feel like it's been so\x01",
            "long since I've seen all of you.\x02\x03",
            "Elie too. How have you been?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha. Fortunately, we\x01",
            "restarted SSS activities\x01",
            "a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#02905FHmm, now let me have a\x01",
            "look at you...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-330, 1500, 14870, 2000)
    MoveCamera(44, 26, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(14510, 2000)

    def lambda_6D14():

        label("loc_6D14")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D14")

    QueueWorkItem2(0x101, 1, lambda_6D14)
    Sleep(50)

    def lambda_6D29():

        label("loc_6D29")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D29")

    QueueWorkItem2(0x109, 1, lambda_6D29)
    Sleep(50)

    def lambda_6D3E():

        label("loc_6D3E")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D3E")

    QueueWorkItem2(0x105, 1, lambda_6D3E)
    OP_99(0x11, 0x102, 0x1F4, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x11, 0x3)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrPos(0x102, 760, 300, 14650, 180)
    SetChrPos(0x11, 760, 300, 15150, 180)

    ChrTalk(
        0x109,
        "#12P#10111FWha...ha..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FWhoo♪\x02",
    )

    CloseMessageWindow()

    def lambda_6DE3():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6DE3)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#12P#00112FW-Wait, Bell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#02902FHmhm, you gained some\x01",
            "muscles.\x02\x03",
            "#02904FThis soft, warm feeling,\x01",
            "your supple muscle response,\x01",
            "the bottom of your limbs....\x02\x03",
            "#02909FOhh, I can't get enough㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FE-Enough! And please\x01",
            "don't say all that so\x01",
            "indecently!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    TurnDirection(0x102, 0x11, 0)

    def lambda_6F50():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6F50)
    Sleep(50)

    def lambda_6F68():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F68)
    Sleep(1000)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#02904FBy the way, Lloyd...\x02\x03",
            "#02901FI'm sure you haven't tried to\x01",
            "pull anything with Elie\x01",
            "without my consent, have you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FUmm, is that how you\x01",
            "start all your\x01",
            "conversations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02903FYou're a dangerous guy Lloyd. It's\x01",
            "only a matter of course that I'd\x01",
            "check up on you every so often.\x02\x03",
            "#02901FYou know what will happen to you\x01",
            "if I find out you actually did...\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FAhaha. Target acquired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00106FOh come on, Bell....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02806FCome now, Bell. We haven't\x01",
            "seen them for a while, so\x01",
            "please be more respectful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71E7)
    Sleep(50)

    def lambda_71F7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71F7)
    Sleep(50)

    def lambda_7207():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7207)
    Sleep(50)

    def lambda_7217():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7217)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x10,
        (
            "Ladies and gents, it's been a\x01",
            "while, although I do repeat\x01",
            "myself.\x02\x03",
            "And above all, it appears your new\x01",
            "members, Noｱl and Wazy, are\x01",
            "getting used to things.\x02\x03",
            "Allow me to take this opportunity\x01",
            "to congratulate the SSS on their\x01",
            "restart of operations.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x105,
        (
            "#12P#10300FHah, thanks for that.\x02\x03",
            "#10309FAllow me to thank you\x01",
            "again for recommending\x01",
            "me for the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FAnd we also have you to\x01",
            "thank for our orbal car!\x02\x03",
            "#10104FIt's like a dream to\x01",
            "drive such a nice car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHaha, I'm just glad\x01",
            "you're making good use\x01",
            "of it.\x02\x03",
            "#02800FI have to give back now\x01",
            "that I've become the\x01",
            "mayor.\x02\x03",
            "#02806FIt's quite tiring to\x01",
            "keep up with being mayor\x01",
            "and also running IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02906FWell in father's case,\x01",
            "him being so busy is\x01",
            "mostly his own fault.\x02\x03",
            "#02900FI keep asking him to let\x01",
            "me help with things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02804FHaha, sorry Bell. I'm just\x01",
            "worried about Crossbell too\x01",
            "much to sit down and relax.\x02\x03",
            "#02800FI tend to take on more than\x01",
            "I can handle, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FEhe. Grandfather seems to\x01",
            "admire your vitality as well,\x01",
            ""uncle".\x02\x03",
            "#00104FHe always happily says, "What\x01",
            "Crossbell needs now is\x01",
            "precisely his youth and vigor".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHaha, I'm flattered\x01",
            "Chairman MacDowell would\x01",
            "say that about me.\x02\x03",
            "#02803FI am still a beginner in\x01",
            "politics myself, though.\x02\x03",
            "#02800FThere are still many\x01",
            "things I must learn from\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#11P#02905FOh, father, it's time to\x01",
            "meet with those people\x01",
            "from the new City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02805FOh, that's right.\x02\x03",
            "#02800FWell then guys, I'll\x01",
            "take my leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSorry for stopping you\x01",
            "like this when you're so\x01",
            "busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FNo no, don't worry about\x01",
            "it. Thanks to you, I was\x01",
            "able to relax a little.\x02\x03",
            "#02804FIf there's ever anything\x01",
            "troubling you, please\x01",
            "let me know anytime.\x02\x03",
            "#02800FIf it's for you guys,\x01",
            "I'll gladly help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThank you very much.\x02\x03",
            "#00104FPlease take care of\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#5P#02909FUhuhu, thanks Elie.\x02\x03",
            "#02900FWell then, we'll take\x01",
            "our leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FThanks for your hard\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-310, 1500, 13600, 3000)
    MoveCamera(44, 24, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15430, 3000)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 19)
    Sleep(500)
    BeginChrThread(0x10, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 17)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 21)
    WaitChrThread(0x11, 3)
    Sound(107, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FBusy as ever, aren't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FWell there is that\x01",
            ""trade conference" at\x01",
            "the end of the month...\x02\x03",
            "#00100FI think their schedules\x01",
            "are planned out down to\x01",
            "the minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. Orbal car aside, it\x01",
            "seems they're doing a lot\x01",
            "for us behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, they're so busy that\x01",
            "I want them to take better\x01",
            "care of themselves.\x02\x03",
            "#00000F...Anyway, now we need to\x01",
            "check in with Chief\x01",
            "Roberts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRight. The receptionist\x01",
            "will get him for us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearMapFlags(0x10000000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x132, 5)
    SetChrPos(0x0, -60, 300, 15630, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_6661 end

    def Function_17_7D4A(): pass

    label("Function_17_7D4A")

    OP_95(0xFE, -330, 300, 15470, 2000, 0x0)
    OP_95(0xFE, -40, 300, 6500, 2000, 0x0)
    Return()

    # Function_17_7D4A end

    def Function_18_7D73(): pass

    label("Function_18_7D73")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_7D73 end

    def Function_19_7D8A(): pass

    label("Function_19_7D8A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x190, 0x7D0, 0x0)
    Return()

    # Function_19_7D8A end

    def Function_20_7DA1(): pass

    label("Function_20_7DA1")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_7DA1 end

    def Function_21_7DB8(): pass

    label("Function_21_7DB8")

    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_7DB8 end

    def Function_22_7DCF(): pass

    label("Function_22_7DCF")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(500)
    OP_68(-20, 1300, 29740, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x109, -810, 300, 27570, 0)
    SetChrPos(0x105, 890, 300, 27520, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#12P#00100FGood day, Lanfei.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F90")

    ChrTalk(
        0xA,
        (
            "#5POh, Lloyd and Elie. Long\x01",
            "time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt looks like the SSS\x01",
            "has started back up\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWe look forward to\x01",
            "working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PI'm always happy to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSo then, what can I help\x01",
            "you with today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FEB")

    label("loc_7F90")


    ChrTalk(
        0xA,
        (
            "#5PMy, it's Elie and the Support\x01",
            "Section. What business might\x01",
            "you have with us today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FEB")


    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're here in regard to\x01",
            "Chief Roberts'\x01",
            "request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh. In that case, I can\x01",
            "get get him for you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_864F")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_822F")

    ChrTalk(
        0xA,
        "#5PAh, but before that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe exchange service access card\x01",
            "I gave to the Support Section a\x01",
            "while back has expired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI have prepared a new\x01",
            "one for you, so please\x01",
            "take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#5PPlease present your card\x01",
            "at the exchange counter,\x01",
            "just like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe'll convert sepith to\x01",
            "mira for you at a better\x01",
            "rate than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B0")

    label("loc_822F")


    ChrTalk(
        0xA,
        (
            "#5POh yes, but before\x01",
            "that... There's something\x01",
            "I must give you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PPlease accept this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00005FThis card is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is card that identifies\x01",
            "you as a preferred\x01",
            "customer at our bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you present it at the counter,\x01",
            "you can exchange sepith for mira\x01",
            "at a higher rate than normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B0")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※You can use IBC's exchange service.\x01",
            "The exchange rate is higher than you\x01",
            "get from normal shops.\x02\x03",
            "Just talk to Lanfei and choose\x01",
            "[Exchange] to use this service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x134, 4)

    ChrTalk(
        0x109,
        (
            "#12P#10105FI-Is it really ok for us\x01",
            "to use a service like\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, of course. You are all\x01",
            "good friends of both Mayor\x01",
            "Crois and Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThis accommodation is\x01",
            "only a matter of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHeh, then I guess we'll\x01",
            "make good use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, let's do just that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHaha. We'll be waiting\x01",
            "for your next visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell then, please wait a\x01",
            "moment while I call\x01",
            "Chief Roberts for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8683")

    label("loc_864F")


    ChrTalk(
        0xA,
        (
            "#5PHe'll receive you, so\x01",
            "please wait a moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8683")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    Sleep(1000)
    OP_68(6520, 1500, 14990, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(13860, 0)
    SetChrPos(0x101, 4820, 0, 16800, 90)
    SetChrPos(0x102, 4820, 0, 15390, 90)
    SetChrPos(0x109, 3530, 0, 16850, 90)
    SetChrPos(0x105, 3470, 0, 15130, 90)
    SetChrPos(0xE, 10590, 0, 16190, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)
    OP_68(4600, 1500, 15420, 2000)

    def lambda_877C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_877C)

    def lambda_878D():
        OP_95(0xFE, 6410, 0, 16170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_878D)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0xE, 1)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        "Hey guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FChief Roberts, thanks\x01",
            "for meeting with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You came for my request\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh that really helps.\x01",
            "It's a job I absolutely\x01",
            "must have you do for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe, this one seems\x01",
            "kind of fun.\x02\x03",
            "#10304FIt was something about\x01",
            "the final test for some\x01",
            "service...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FPom!, I think it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FI feel like that's a\x01",
            "name I've heard before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FNow that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, I'm sure you guys\x01",
            "will love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well then, can you\x01",
            "accept my request right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWill you please explain\x01",
            "the details of the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Actually we plan to\x01",
            "release an orbal game\x01",
            "called "Pom!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The number of net terminal\x01",
            "owners in the city has\x01",
            "been increasing, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FAn orbal game?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FIs it different from\x01",
            "billiards or poker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, it's similar in that\x01",
            "there are fixed rules and\x01",
            "players compete on score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But the biggest difference\x01",
            "is that this game is played\x01",
            "on the terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FThat sounds amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThen, the "test" that's\x01",
            "the subject of your\x01",
            "request is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Of course, I want you to\x01",
            "test this "Pom!" game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After software development,\x01",
            "bugs may appear, so test\x01",
            "cycles are critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHmm, but for a test of this\x01",
            "level, can't the foundation\x01",
            "do it themselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tio has been helping us\x01",
            "with this testing for a\x01",
            "while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Actually, there's two problems.\x01",
            "I'd want help from outside the\x01",
            "foundation no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FTwo problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah. As for the\x01",
            "first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tio sometimes activates\x01",
            "her Aeon system during\x01",
            "testing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So the test data we get\x01",
            "isn't so useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FHer Aeon system...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's that thing that Tio\x01",
            "uses.\x02\x03",
            "#00104FShe explained it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah. It's a system used for\x01",
            "operation of orbal terminals\x01",
            "and staves... she said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, I suppose I should\x01",
            "take this opportunity to\x01",
            "give my own explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Aeon System is the name\x01",
            "of the system inside\x01",
            "Tio's armor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She activates arts from her orbal\x01",
            "staff with no wait, and for her high-\x01",
            "speed data processing abilities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Supporting those\x01",
            "abilities is the\x01",
            "system's main function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It takes incredible\x01",
            "aptitude to master this\x01",
            "system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FR-Right. It doesn't seem\x01",
            "simple at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FTopics like this are\x01",
            "tough when Tio's not\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSo you're saying that\x01",
            "system is not suitable\x01",
            "for testing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "W-Well, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When she uses the Aeon System, she makes gigantic\x01",
            "chains no normal person could ever make, and ends\x01",
            "up wiping the floor with her opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Jona is usually testing\x01",
            "against her but he's\x01",
            "never once won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ah, but I'm not saying\x01",
            "that Tio is cheating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please don't say\x01",
            "anything weird to Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FUmm... So what's the\x01",
            "other reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh right. The other\x01",
            "reason is that this game\x01",
            "is a "versus game".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Though we connected it only\x01",
            "recently, it's possible to play this\x01",
            "game between distant terminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So we wanted to start\x01",
            "out with a practical\x01",
            "test within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FI see. So that's why.\x02\x03",
            "#00100FEven so, it's amazing\x01",
            "that you can play with\x01",
            "someone far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Haha. I know, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This was planned for the\x01",
            "initial stage of the\x01",
            "orbal network project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And once the network becomes\x01",
            "bigger, more and more people\x01",
            "will be able to enjoy the game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "For example, on a rainy day\x01",
            "like this, you could play\x01",
            "with friends from your house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWhat an incredible time\x01",
            "we live in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Sorry for rambling.\x01",
            "That's basically it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...So then, I'd like to\x01",
            "give you this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x339, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00005FThis is... a memory\x01",
            "quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The "Pom!" application\x01",
            "data is stored on that\x01",
            "memory quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you install it on the\x01",
            "SSS terminal, you can\x01",
            "play right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FInstall... In short, it's\x01",
            "an operation that puts the\x01",
            "program in our terminal.\x02\x03",
            "#00104FI saw Tio doing it before,\x01",
            "so I think I can figure it\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell then Elie, we'll\x01",
            "leave it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, yes, very\x01",
            "reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll also give you\x01",
            "these─ my ENIGMA number\x01",
            "and Pom! account.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "Got \x07\x02",
            "[Chief Roberts' Pom!\x01",
            "Account]\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#6P#00005FA-Account?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FW-wait a second please.\x01",
            "This is getting really\x01",
            "complicated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Umm, basically it's a\x01",
            "name used on a network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, just think of it\x01",
            "as something you need to\x01",
            "play with someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Don't worry about the details for\x01",
            "now. Just input my account once\x01",
            "you've installed the beta version.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After that, contact me\x01",
            "and I'll tell you what\x01",
            "to do next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, that's about it.\x01",
            "Can you begin the test\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FS-Sure. Leave it to us.\x02\x03",
            "#00004FFor now, we'll head back\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FYes, let's.\x02",
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
            "Quest [Beta Test\x01",
            "Participation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetScenarioFlags(0x131, 3)
    OP_29(0x6C, 0x1, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    SetChrPos(0xE, 6500, 0, 17850, 270)
    SetChrPos(0x0, 4010, 0, 16140, 90)
    EventEnd(0x5)
    Return()

    # Function_22_7DCF end

    def Function_23_9B96(): pass

    label("Function_23_9B96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x1E)
    LoadChrToIndex("chr/ch06100.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    OP_68(0, 1400, 4600, 0)
    MoveCamera(54, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 500, 300, 2000, 0)
    SetChrPos(0x102, -1000, 300, 800, 0)
    SetChrPos(0x103, -500, 300, 2000, 0)
    SetChrPos(0x104, 1000, 300, 1200, 0)
    SetChrPos(0x109, 500, 300, 0, 0)
    SetChrPos(0x105, -500, 300, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9CA3():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9CA3)
    Sleep(100)

    def lambda_9CC0():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9CC0)
    Sleep(100)

    def lambda_9CDD():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9CDD)
    Sleep(100)

    def lambda_9CFA():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9CFA)
    Sleep(100)

    def lambda_9D17():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9D17)
    Sleep(100)

    def lambda_9D34():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9D34)
    OP_68(-70, 1400, 7250, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)

    def lambda_9D6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D6E)
    Sleep(100)

    def lambda_9D82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9D82)
    Sleep(500)

    def lambda_9D96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9D96)
    Sleep(100)

    def lambda_9DAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9DAA)
    Sleep(500)

    def lambda_9DBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9DBE)
    Sleep(100)

    def lambda_9DD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9DD2)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00000FNow then... I wonder if\x01",
            "Chief Roberts is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PHe's probably on the\x01",
            "foundation's floor.\x02\x03",
            "#00200FI'll contact him via\x01",
            "ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E8B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9E8B)

    def lambda_9E98():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9E98)
    Sleep(50)

    def lambda_9EA8():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9EA8)
    Sleep(50)

    def lambda_9EB8():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9EB8)
    Sleep(50)

    def lambda_9EC8():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9EC8)
    Sleep(50)

    def lambda_9ED8():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9ED8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    SetCameraDistance(15650, 2000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x103, 0x1)
    Sound(823, 0, 100, 0)
    Sleep(2700)

    ChrTalk(
        0x103,
        (
            "#00200F#5PHello, it's Tio.\x02\x03",
            "#00205FNo... I have no\x01",
            "particular intention of\x01",
            "doing that.\x02\x03",
            "#00203F............\x02\x03",
            "#00211FYou're persistent,\x01",
            "Chief. Knock it off\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#00012F(T-They're the same as\x01",
            "always...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F(I wish Tio would go a\x01",
            "little easier on him,\x01",
            "though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11P(Conversely, maybe that\x01",
            "ol' man likes bein'\x01",
            "treated coldly like that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5P...Yes, it's about the\x01",
            "ENIGMA Ⅱ emergency alert\x01",
            "function...\x02\x03",
            "#00200F...Yes... That's\x01",
            "right...\x02\x03",
            "#00203FYes. Please come down.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#00000FWill he help us?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00204F#6PYes. He said he's coming\x01",
            "down right away.\x02\x03",
            "#00202FHe said Jona's with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PWasn't he the one whose\x01",
            "room in the Geofront got\x01",
            "blown up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThe genius hacker from\x01",
            "the Epstein Foundation,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PYeah, he's an\x01",
            "impertinent brat of\x01",
            "questionable value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FIsn't he causing trouble\x01",
            "now that he's back in\x01",
            "the foundation office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PYes... It seems they\x01",
            "were reluctant to take\x01",
            "him back.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15150, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrPos(0x101, 4900, 0, 21000, 90)
    SetChrPos(0x102, 4700, 0, 22200, 135)
    SetChrPos(0x103, 4900, 0, 19900, 90)
    SetChrPos(0x104, 6900, 0, 23000, 180)
    SetChrPos(0x109, 5800, 0, 23000, 135)
    SetChrPos(0x105, 4400, 0, 18500, 45)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 7300, 0, 21000, 270)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 7300, 0, 19900, 270)
    OP_68(6100, 1100, 20450, 0)
    MoveCamera(43, 17, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15000, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "─I see. So that's the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(128, 2, 50, 0)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#02306F#11PThe orbal power's cut\x01",
            "and we can't contact\x01",
            "them, right?\x02\x03",
            "#02301FBut bracers are strong.\x01",
            "Can't we leave them\x01",
            "alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FNow look here, Jona.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FGive me a break. You\x01",
            "can't say things like\x01",
            "that, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P*sigh*, Jona's been like\x01",
            "this a lot lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PEven though I prepared the\x01",
            "most high tech terminal in\x01",
            "the building for him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(200)

    ChrTalk(
        0xF,
        (
            "#02310F#12PNo matter how high the processing\x01",
            "power, I could never be satisfied\x01",
            "with a limited system!\x02\x03",
            "#02307FGive me the security code and set\x01",
            "me free, already!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)

    ChrTalk(
        0xE,
        (
            "#5PYou know I can't do\x01",
            "that, Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf we did, you'd just do\x01",
            "whatever you wanted\x01",
            "again, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIn exchange, I prepared a\x01",
            "special "Pom!" training\x01",
            "program so you can beat Tio~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02311F#12PI-I don't need your\x01",
            "help!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012F(It looks like he's\x01",
            "doing a good job\x01",
            "supervising Jona.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Well, his irritability\x01",
            "aside, he is quite\x01",
            "capable.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xE,
        "#11P─Well, that aside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe ENIGMA Ⅱ has an alert\x01",
            "function but it might not\x01",
            "be that useful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A9F1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A9F1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FSo it really does have\x01",
            "that function?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes, but its orbal wave\x01",
            "is weak and it's almost\x01",
            "impossible to detect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PUnless you're within 10 selge,\x01",
            "you'd never be able to detect\x01",
            "it no matter what you're using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P10 selge...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThat kind of range is\x01",
            "difficult to work\x01",
            "with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301FIf they were in\x01",
            "Crossbell City, we'd\x01",
            "know that already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FWhat if you combine that\x01",
            "instrument with my\x01",
            "sensors?\x02\x03",
            "#00201FIf you need a matrix\x01",
            "transformation system,\x01",
            "Aeon can help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11POh, in that case─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...No, that won't work. If you\x01",
            "operated the sensor with Aeon, the\x01",
            "accuracy would become unstable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThere's the orbal pressure problem too,\x01",
            "and you'd need to consider the surrounding\x01",
            "terrain. I think it'd be quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI-I don't quite\x01",
            "understand what's so bad\x01",
            "about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt seems like a\x01",
            "technical problem...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#02305F#11P─If that's the case.\x02\x03",
            "#02300FWouldn't it be better to\x01",
            "measure from the Orchis\x01",
            "Tower roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AF84():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_AF84)

    ChrTalk(
        0x103,
        "#6P#00205FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PJona?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FUmm, what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02301F#11PThe orbal alert wave is weak, so you can't\x01",
            "detect it unless your instrument is\x01",
            "nearby.\x02\x03",
            "#02303FHaving said that, if you use Tio's sensors\x01",
            "together with the instrument, the output\x01",
            "is insufficient so accuracy suffers.\x02\x03",
            "#02302FBut on top of Orchis Tower, there are no\x01",
            "obstructions so accuracy will be raised.\x01",
            "High output is practically guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PC-Cryptic as always,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)

    ChrTalk(
        0x109,
        "#10100F#5PWhat do you think, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00204FI'm surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PYou've done it, Jona!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI'm amazed at your\x01",
            "abilities as a systems\x01",
            "engineer, Jona!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02309F#12PH-Heheh. Well, I guess\x01",
            "I'm just that great\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B26B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B26B)

    ChrTalk(
        0x101,
        "#6P#00002FWell then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FIt seems like things are\x01",
            "looking up, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FYes. It might work.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#11PI'll contact the Orchis Tower\x01",
            "Management Department immediately and\x01",
            "ask for permission to use the roof.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(150)

    ChrTalk(
        0xE,
        (
            "#5PYou'll help, won't you\x01",
            "Jona?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02302F#12PWhy should I? That's what I\x01",
            "want to say, but... Well, I'm\x01",
            "bored so I guess I'll help.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02301F#11PBut you guys 'll do one\x01",
            "thing for me in\x01",
            "exchange. Alright!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FHaha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FWe'll do whatever you\x01",
            "ask as long as it's not\x01",
            "unreasonable.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Chief Roberts and Jona got permission to use the Orchis\x01",
            "Tower roof and went there in advance with their\x01",
            "equipment.\x02\x03",
            "It seemed that preparing for the detection would take\x01",
            "some time. Lloyd and the others decided to head for the\x01",
            "Orchis Tower roof after finishing their other business.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 0, 300, 8000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 2)
    OP_29(0xA9, 0x1, 0x1)
    ClearMapFlags(0x10000000)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_23_9B96 end

    def Function_24_B659(): pass

    label("Function_24_B659")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5PEveryone... Welcome, and\x01",
            "thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCould it be that you are\x01",
            "here to fulfill Miss\x01",
            "Mariabell's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. So you heard about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI understand that Bell's\x01",
            "collection of antique\x01",
            "dolls has been stolen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FCould they be ones made\x01",
            "by the Rosenberg Studio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, that's right. Miss\x01",
            "Mariabell is terribly\x01",
            "distraught too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCan you accept the young\x01",
            "lady's request right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E7")
    Call(0, 27)

    label("loc_B8E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B910")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B91A")

    label("loc_B910")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B91A")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_B659 end

    def Function_25_B936(): pass

    label("Function_25_B936")

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
            "Accept\x01",      # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B994"),
        (1, "loc_B999"),
        (SWITCH_DEFAULT, "loc_BA60"),
    )


    label("loc_B994")

    Jump("loc_BA60")

    label("loc_B999")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry,\x01",
            "our hands are a little\x01",
            "full right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI see... It can't be\x01",
            "helped, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf by chance you find\x01",
            "the time, please speak\x01",
            "with me once again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C6, 1)
    Jump("loc_BA60")

    label("loc_BA60")

    Return()

    # Function_25_B936 end

    def Function_26_BA61(): pass

    label("Function_26_BA61")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5PMiss Mariabell seems terribly\x01",
            "distraught over her antique\x01",
            "dolls having been stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCan you accept the young\x01",
            "lady's request right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC4")
    Call(0, 27)

    label("loc_BBC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBED")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BBF7")

    label("loc_BBED")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_BBF7")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_26_BA61 end

    def Function_27_BC13(): pass

    label("Function_27_BC13")


    ChrTalk(
        0x101,
        "#00000FYes, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FMariabell has helped us\x01",
            "out plenty of times\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI've issued a card for\x01",
            "you. Please take it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x324),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x324, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x105,
        "#12P#10305FHmm, what's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's an IBC authentication\x01",
            "card, like the one we got\x01",
            "before.\x02\x03",
            "#00103FIf we have this, we can go\x01",
            "to floors we're permitted to\x01",
            "access using the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOh, a security system, eh?\x01",
            "You'd expect the world's\x01",
            "leading bank to have one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBy the way, you can go to\x01",
            "the same floors you could\x01",
            "before using that card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMiss Mariabell is waiting for\x01",
            "you on 16F in the president's\x01",
            "office, so please go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright. Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x7A, 0x1, 0x0)
    SetScenarioFlags(0x157, 0)
    Return()

    # Function_27_BC13 end

    def Function_28_BF51(): pass

    label("Function_28_BF51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [The Missing\x01",
            "Collection]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_28_BF51 end

    def Function_29_BFBE(): pass

    label("Function_29_BFBE")

    EventBegin(0x0)
    SoundLoad(836)
    OP_4B(0xA, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x103, -1190, 300, 27930, 0)
    SetChrPos(0x104, -70, 300, 27510, 0)
    SetChrPos(0x109, 890, 300, 27020, 0)
    SetChrPos(0x105, -810, 300, 26570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5POh, the Special Support\x01",
            "Section... What can I do\x01",
            "for you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, actually... We'd like to\x01",
            "cooperate with IBC on an\x01",
            "investigation we're conducting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FLanfei, can you do an\x01",
            "IBC account search for\x01",
            "us?\x02\x03",
            "We want to investigate\x01",
            "mira transfers related\x01",
            "to a certain account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHmm... An account, you\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHmm... If relation to any\x01",
            "incident is confirmed, I\x01",
            "can get permission, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThat's right. First, can\x01",
            "you tell me the details\x01",
            "of your situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI understand. You see...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the\x01",
            "details of the suspected\x01",
            "fraud case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#5PI see... So that's the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWill that be enough to\x01",
            "get permission to search\x01",
            "the accounts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThis is important for IBC too. If\x01",
            "an IBC account was used for fraud,\x01",
            "it'd damage your bank's reputation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0xA,
        (
            "#5PIndeed, this does seem\x01",
            "related to an\x01",
            "incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI have permission to\x01",
            "tell you what I see on\x01",
            "my terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, that will be fine.\x01",
            "Please go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PUnderstood, then...\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#5PAccount name, "Mr.\x01",
            "Minneth"...\x01",
            "(*typing*...)\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PQuincy Company subsidiary\x01",
            ""Armorica Honey\x01",
            "Company"... (*typing*...)\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#5PI found it. The account\x01",
            "has indeed been opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FW-What's wrong?\x02\x03",
            "Is there some kind of\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#5PUmm... It's not like I\x01",
            "can give you the\x01",
            "balance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe "Armorica Honey\x01",
            "Company" account has a bare\x01",
            "minimum of mira on deposit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm... Then that\x01",
            "means...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, of course. Accounts intended for\x01",
            "corporate use require a certain amount\x01",
            "of capital to be opened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POnly that minimum level of mira is\x01",
            "present... In other words, only tens\x01",
            "of thousands of mira are on deposit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00200FIt must be for the candy factory\x01",
            "construction and field\x01",
            "management...\x02\x03",
            "That amount of mira isn't\x01",
            "sufficient for such activities...\x01",
            "I think we can conclude that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEven though he's already taken custody\x01",
            "of the land deeds and made various\x01",
            "deals, the balance hasn't changed...\x02\x03",
            "Hmm, it's quite unnatural.\x02\x03",
            "It almost as if he prepared the\x01",
            "account solely to gain Derrick's\x01",
            "trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see. That's clearly\x01",
            "contradictory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I think we got\x01",
            "some good evidence here.\x02\x03",
            "Thank you for your\x01",
            "cooperation, Lanfei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PNo, it was our pleasure\x01",
            "to serve you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf I can assist you in\x01",
            "the future, please do\x01",
            "not hesitate to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, we'll do just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBBE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆MacDowell Residence?\x01",
            "(debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",             # 0
            "[Investigated]\x01",          # 1
            "[Not Investigated]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CBA9"),
        (1, "loc_CBAE"),
        (2, "loc_CBB6"),
        (SWITCH_DEFAULT, "loc_CBBE"),
    )


    label("loc_CBA9")

    Jump("loc_CBBE")

    label("loc_CBAE")

    SetScenarioFlags(0x177, 5)
    Jump("loc_CBBE")

    label("loc_CBB6")

    ClearScenarioFlags(0x177, 5)
    Jump("loc_CBBE")

    label("loc_CBBE")

    OP_29(0x87, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_CC83")
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FAlright. With this, we've\x01",
            "collected material on each of\x01",
            "Minneth's suspicious points.\x02\x03",
            "For now, let's return to\x01",
            "Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_CD03")

    label("loc_CC83")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F...We still need to search the\x01",
            "MacDowell residence. Let's\x01",
            "hurry there and investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FRoger!\x02",
    )

    CloseMessageWindow()

    label("loc_CD03")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x177, 4)
    SetChrPos(0x0, 0, 300, 28600, 180)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_BFBE end

    def Function_30_CD41(): pass

    label("Function_30_CD41")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE21")

    ChrTalk(
        0x8,
        (
            "Ladies and gentlemen, you\x01",
            "need an authentication\x01",
            "card to use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business here,\x01",
            "go to the reception desk\x01",
            "and explain yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 6)
    Jump("loc_CEC2")

    label("loc_CE21")


    ChrTalk(
        0x8,
        (
            "Ladies and gentlemen, you\x01",
            "need an authentication\x01",
            "card to use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business here,\x01",
            "go to the reception desk\x01",
            "and explain yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEC2")

    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_30_CD41 end

    SaveToFile()

Try(main)
