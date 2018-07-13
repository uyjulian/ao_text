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
        "Function_6_716",          # 06, 6
        "Function_7_20C7",         # 07, 7
        "Function_8_285B",         # 08, 8
        "Function_9_2865",         # 09, 9
        "Function_10_29C5",        # 0A, 10
        "Function_11_29C9",        # 0B, 11
        "Function_12_3939",        # 0C, 12
        "Function_13_48A0",        # 0D, 13
        "Function_14_4D65",        # 0E, 14
        "Function_15_5AFC",        # 0F, 15
        "Function_16_6785",        # 10, 16
        "Function_17_7F0C",        # 11, 17
        "Function_18_7F35",        # 12, 18
        "Function_19_7F4C",        # 13, 19
        "Function_20_7F63",        # 14, 20
        "Function_21_7F7A",        # 15, 21
        "Function_22_7F91",        # 16, 22
        "Function_23_9E20",        # 17, 23
        "Function_24_B8F4",        # 18, 24
        "Function_25_BBC3",        # 19, 25
        "Function_26_BCEC",        # 1A, 26
        "Function_27_BE9E",        # 1B, 27
        "Function_28_C226",        # 1C, 28
        "Function_29_C293",        # 1D, 29
        "Function_30_D066",        # 1E, 30
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
    Jump("loc_712")

    label("loc_65F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DD")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70D")

    label("loc_6DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F1")
    Jump("loc_70D")

    label("loc_6F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_70D")

    Jump("loc_669")

    label("loc_712")

    TalkEnd(0xA)
    Return()

    # Function_5_5B8 end

    def Function_6_716(): pass

    label("Function_6_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_20C6")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_20C6")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")

    ChrTalk(
        0xA,
        (
            "To think Mainz is occupied\x01",
            "and civilians are involved...\x02",
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
            "Anyway, I pray the people\x01",
            "of Mainz are safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_897")

    label("loc_811")


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
            "Anyway, I pray the people\x01",
            "of Mainz are safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_897")

    Jump("loc_20C6")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")

    ChrTalk(
        0xA,
        (
            "The more you interact\x01",
            "with the orbal net, the\x01",
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
            "It's not 100 percent,\x01",
            "but it's fairly accurate. \x01",
            "I check it every day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A3B")

    label("loc_9A7")


    ChrTalk(
        0xA,
        (
            "The weather forecasts from the\x01",
            "orbal net are fairly accurate.\x02",
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

    label("loc_A3B")

    Jump("loc_20C6")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97")

    ChrTalk(
        0xA,
        (
            "Only one or two in our company can\x01",
            "challenge Korinna's skill with the\x01",
            "terminal... Or her skill with games.\x02",
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
    Jump("loc_BFC")

    label("loc_B97")


    ChrTalk(
        0xA,
        (
            "Even so, to think one could look\x01",
            "that happy looking at a screen...\x01",
            "Uh uh, I'm a little envious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFC")

    Jump("loc_20C6")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")

    ChrTalk(
        0xA,
        (
            "Please, allow us to assist you\x01",
            "with anything we are able.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you ever need anything,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_C9D")


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

    label("loc_D58")

    Jump("loc_20C6")

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FD")

    ChrTalk(
        0xA,
        (
            "Ah, everyone. If you are looking\x01",
            "for Acting President Mariabell,\x01",
            "she is on a trip abroad...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 0)), scpexpr(EXPR_END)), "loc_E3E")

    ChrTalk(
        0x101,
        (
            "#00005F"Acting President" Mariabell...\x02\x03",
            "#00003FOh, they reported that\x01",
            "in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_E3E")


    ChrTalk(
        0x101,
        "#00005F"Acting President" Mariabell...?\x02",
    )

    CloseMessageWindow()

    label("loc_E6B")


    ChrTalk(
        0x102,
        (
            "#00100FYes. The board of directors took over\x01",
            ""uncle"'s presidential duties, and it seems\x01",
            "she was appointed right after that.\x02\x03",
            "#00104FIn other words, Bell\x01",
            "is the leader of IBC.\x02",
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
        "#00200FIt is convincing, being Miss Mariabell, however...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FYeah. Thinking about it\x01",
            "again, it's really crazy.\x02",
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
        "Yes, you are correct, of course.\x02",
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
            "Now that she is Acting President,\x01",
            "she is required to show up in all\x01",
            "manner of different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... She really must\x01",
            "be very busy, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, the young lady\x01",
            "plans to return this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although she has a schedule\x01",
            "tomorrow filled with meeting,\x01",
            "consultations and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am terribly sorry, but I don't\x01",
            "think you will be able to see Lady\x01",
            "Mariabell for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_167D")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Oh, right― \x01",
            "The young lady had\x01",
            "a message for you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Mariabell's Account"\x07\x00",
            " received.\x02",
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
            "#00005FT-This is... \x01",
            "A "Pom!" account!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMiss Mariabell\x01",
            "plays too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#18C"Uh uh, I am of course\x01",
            "interested in this as a member\x01",
            "of the technology division."\x02",
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
        "...That is what she said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FUmm, that just now was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FWas she trying to predict\x01",
            "Lloyd and Tio's reactions?\x02",
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
            "As expected of Lady Elie.\x01",
            "That is exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, she's really a big deal.\x02\x03",
            "#10302FAnd, you do a great impression\x01",
            "of her voice, miss receptionist.\x02",
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
            "...Anyway, that is\x01",
            "all for the message.\x02",
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
        "#00012FHa ha, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F5")

    label("loc_167D")


    ChrTalk(
        0x102,
        (
            "#00104FYes, understood.\x02\x03",
            "#00100FMiss Lanfei, please\x01",
            "tell Bell to not overdo\x01",
            "things too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()

    label("loc_16F5")

    SetScenarioFlags(0x16D, 0)
    Jump("loc_17AF")

    label("loc_16FD")


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
            "I am terribly sorry. For now,\x01",
            "I don't think the young lady\x01",
            "will be able to see you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AF")

    Jump("loc_20C6")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CD")

    ChrTalk(
        0xA,
        (
            "It seems like we'll need to increase building\x01",
            "security even further from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, thank you very\x01",
            "much for recovering Lady\x01",
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
    Jump("loc_1969")

    label("loc_18CD")


    ChrTalk(
        0xA,
        (
            "Anyway, thank you very\x01",
            "much for recovering Lady\x01",
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

    label("loc_1969")

    Jump("loc_1B3E")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A75")

    ChrTalk(
        0xA,
        (
            "If you have that authentication\x01",
            "card, you can use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You should be able to go to the same\x01",
            "floors as the one I gave you all before.\x02",
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
    Jump("loc_1B3E")

    label("loc_1A75")


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

    label("loc_1B3E")

    Jump("loc_20C6")

    label("loc_1B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B51")
    Jump("loc_20C6")

    label("loc_1B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E28")

    ChrTalk(
        0xA,
        (
            "Oh, everyone.\x01",
            "Welcome to IBC.\x02",
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
            "You truly do get information quickly,\x01",
            "Lady Elie. It is as you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "President Rocksmith\x01",
            "is the VIP of VIPs,\x01",
            "after all.\x02",
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
            "#10103FI see. Michelam\x01",
            "must be the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWell, that's only natural.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWe understand the situation for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you for letting us know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 7)
    Jump("loc_1ED3")

    label("loc_1E28")


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
            "Everyone, if you have business here, \x01",
            "please finish it today, because there is \x01",
            "a special business holiday tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED3")

    Jump("loc_20C6")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2019")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(
        0xA,
        (
            "It looks like you're\x01",
            "finished with the Chief's\x01",
            "request. Uh uh, good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Allow me to thank\x01",
            "you as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2014")

    label("loc_1F65")


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
            "In addition, he has helped us with many\x01",
            "things relating to the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2014")

    Jump("loc_20C6")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2034")
    Call(0, 7)
    Jump("loc_20C6")

    label("loc_2034")


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
            "From now on, please tell me\x01",
            "if you ever need anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C6")

    Return()

    # Function_6_716 end

    def Function_7_20C7(): pass

    label("Function_7_20C7")

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
            "#5POh, if it isn't Mr. Lloyd and\x01",
            "Lady Elie. Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt looks like the SSS has\x01",
            "started back up again.\x02",
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
        "#5PYes, that goes without saying.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2470")

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
            "#5PActually, the expiration date on the\x01",
            "card I gave you before has passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI have prepared a new one\x01",
            "for you, so please take it.\x02",
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
            "#5PPlease present your card at the\x01",
            "exchange counter, just like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe will convert Sepith to Mira for\x01",
            "you at a better rate than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_2470")


    ChrTalk(
        0xA,
        (
            "#5PCome to think of it, I have\x01",
            "something to give you.\x02",
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
            "#5PIt is a card that identifies\x01",
            "you as a preferred customer\x01",
            "at our bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you present it at the counter,\x01",
            "you can exchange Sepith for\x01",
            "Mira at a higher rate than normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E8")


    ChrTalk(
        0x109,
        (
            "#12P#10105FI-Is it really ok for us to\x01",
            "use a service like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, of course. You are all\x01",
            "good friends of both Mayor\x01",
            "Crois and Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThis accommodation is only a matter of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, then shall we\x01",
            "make good use of it?\x02",
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
        "#5PUh uh, I will be waiting for you.\x02",
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
            "※Simply talk to Lanfei and after\x01",
            "selecting [Exchange Sepith] choose \x01",
            ""Exchange" to use this service.\x07\x00\x02",
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

    # Function_7_20C7 end

    def Function_8_285B(): pass

    label("Function_8_285B")

    TalkBegin(0xFE)
    Call(0, 9)
    TalkEnd(0xFE)
    Return()

    # Function_8_285B end

    def Function_9_2865(): pass

    label("Function_9_2865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290A")
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "One moment, please.\x01",
            "(*klak klak, klak klak*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am querying your\x01",
            "contract right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm, I'm counting on you, then.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_29C4")

    label("loc_290A")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xD,
        (
            "Hmm? What's with you?\x01",
            "You're not thinking of\x01",
            "cutting in, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm terribly sorry.\x01",
            "Please wait your turn on\x01",
            "the sofa over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_29C4")

    Return()

    # Function_9_2865 end

    def Function_10_29C5(): pass

    label("Function_10_29C5")

    Call(0, 11)
    Return()

    # Function_10_29C5 end

    def Function_11_29C9(): pass

    label("Function_11_29C9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29DA")
    Jump("loc_3935")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_29E8")
    Jump("loc_3935")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAB")

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
            "Honestly, I'm not even sure our security\x01",
            "department could deal with them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My oh my, it's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B43")

    label("loc_2AAB")


    ChrTalk(
        0xB,
        (
            "Honestly, I'm not even sure our\x01",
            "security department could deal with\x01",
            "the armed group that attacked Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My oh my, it's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B43")

    Jump("loc_3935")

    label("loc_2B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BE4")

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
            "When the orbal net is more \x01",
            "widespread, there will also be\x01",
            "jobs that can be done at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3935")

    label("loc_2BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_30A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAD")

    ChrTalk(
        0xB,
        "(*klak klak, klak klak...!*)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(shoom, bang bang bang bang bang!)\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C92")

    ChrTalk(
        0x101,
        "#00005FW-What in the world is that sound...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2C92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD3")

    ChrTalk(
        0x102,
        "#00105FI-I wonder what sound that is...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2CD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2F")

    ChrTalk(
        0x103,
        (
            "#00203F...This sound is from the Foundation's\x01",
            "latest shooting game.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D66")

    ChrTalk(
        0x104,
        "#00305FW-What's that sound...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9B")

    ChrTalk(
        0x109,
        "#10105FA-Are those gunshots?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2D9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DCF")

    ChrTalk(
        0x105,
        "#10302FHu hu, looks fun somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_2DCF")

    Sleep(50)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "I'm terribly sorry, everyone. \x01",
            "As you can see, I'm actually in\x01",
            "the middle of my break time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Accordingly, please speak with the main\x01",
            "receptionist, whatever your business may be.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_309B")

    label("loc_2EAD")


    ChrTalk(
        0xB,
        "(*klak klak, klak klak...!*)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(shoooom, ratta ratta ratta!)\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3A")

    ChrTalk(
        0x101,
        "#00012F(A-Amazing concentration...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_2F3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F78")

    ChrTalk(
        0x102,
        "#00106F(W-We shouldn't bother her...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_2F78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FDC")

    ChrTalk(
        0x103,
        (
            "#00205F(This counterattack!\x01",
            "...It seems she's definitely\x01",
            "better than Jona.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3016")

    ChrTalk(
        0x104,
        "#00306F(We shouldn't bother her.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_3016")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3055")

    ChrTalk(
        0x109,
        (
            "#10106F(Such intense\x01",
            "concentration...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_3055")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309B")

    ChrTalk(
        0x105,
        "#10302F(Hu hu, she's incredibly immersed into it.)\x02",
    )

    CloseMessageWindow()

    label("loc_309B")

    Jump("loc_3935")

    label("loc_30A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3157")

    ChrTalk(
        0xB,
        (
            "Because of how busy Lady Mariabell\x01",
            "has been lately, sometimes she\x01",
            "doesn't get to have lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While travelling, she\x01",
            "often carries block-\x01",
            "type portable rations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3935")

    label("loc_3157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EA")

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
            "Well, they say stock indices follow\x01",
            "the same pattern a person's life does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3390")

    label("loc_32EA")


    ChrTalk(
        0xB,
        (
            "It seems that Mr. Rizel has become\x01",
            "more cautious. I wonder if it's due to\x01",
            "reflection on his past failures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Personally, I think that\x01",
            "was the right decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_3935")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_358E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D8")

    ChrTalk(
        0xB,
        (
            "Yesterday, I took the day off\x01",
            "for the President's visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I didn't feel like going out due to\x01",
            "the security, and before I knew it,\x01",
            "I spent the whole day in bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I recharged my batteries, but since then\x01",
            "I kept thinking about how nice would be if \x01",
            "I had an orbal net terminal at home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3589")

    label("loc_34D8")


    ChrTalk(
        0xB,
        (
            "Yesterday I kept thinking about\x01",
            "how nice would be if I had an \x01",
            "orbal net terminal at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because if I did, I could have amused\x01",
            "myself all day long with orbal games.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3589")

    Jump("loc_3935")

    label("loc_358E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_359C")
    Jump("loc_3935")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35AD")
    Call(0, 9)
    Jump("loc_3935")

    label("loc_35AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3680")

    ChrTalk(
        0xB,
        "(*klak klak, klak klak...!*)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        (
            "As expected, on rainy days\x01",
            "customers decrease in number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is a good chance to take care\x01",
            "of the paperwork that has piled up.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_36DD")

    label("loc_3680")


    ChrTalk(
        0xB,
        (
            "The business just won't run if there aren't\x01",
            "days like this every once in awhile, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DD")

    Jump("loc_3935")

    label("loc_36E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3881")

    ChrTalk(
        0xB,
        (
            "The technology division has\x01",
            "cleared the initial stage of\x01",
            "the level 2 orbal network test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Putting it simply, the capabilities are\x01",
            "more data and faster, more security\x01",
            "and more reliable transmission.\x02",
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
            "This must be the potential of the technology\x01",
            "division staff led by Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3935")

    label("loc_3881")


    ChrTalk(
        0xB,
        (
            "It seems that Mayor Crois\x01",
            "also helped a lot  with \x01",
            "completing the level 2 test.\x02",
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

    label("loc_3935")

    TalkEnd(0xB)
    Return()

    # Function_11_29C9 end

    def Function_12_3939(): pass

    label("Function_12_3939")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_394A")
    Jump("loc_489C")

    label("loc_394A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3958")
    Jump("loc_489C")

    label("loc_3958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39F9")

    ChrTalk(
        0xFE,
        (
            "It seems something terrible\x01",
            "has happened at Mainz.\x02",
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
    Jump("loc_489C")

    label("loc_39F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4F")

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
            "And one more thing... In the world of speculation,\x01",
            "there is no such thing as an "absolute."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are getting started in speculation,\x01",
            "I strongly recommend you commit only \x01",
            "those funds you're willing to risk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C47")

    label("loc_3B4F")


    ChrTalk(
        0xFE,
        (
            "If you are getting started in speculation,\x01",
            "I strongly recommend you commit only \x01",
            "those funds you're willing to risk.\x02",
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

    label("loc_3C47")

    Jump("loc_489C")

    label("loc_3C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D15")

    ChrTalk(
        0xFE,
        "W-What the...?\x02",
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
    Jump("loc_3DAF")

    label("loc_3D15")


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

    label("loc_3DAF")

    Jump("loc_489C")

    label("loc_3DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA6")

    ChrTalk(
        0xFE,
        (
            "Hmm. Price movements were seen in the\x01",
            "Republic region this morning, huh.\x02",
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
            "No matter what I say at this late hour, it\x01",
            "amounts to nothing more than hindsight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F2F")

    label("loc_3EA6")


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
            "No matter what I say at this late hour, it\x01",
            "amounts to nothing more than hindsight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2F")

    Jump("loc_489C")

    label("loc_3F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_409C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4020")

    ChrTalk(
        0xFE,
        (
            "As I thought... Stock prices\x01",
            "are unstable right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. It's rare for prices to swing\x01",
            "this much yet be so difficult to read.\x02",
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
    Jump("loc_4097")

    label("loc_4020")


    ChrTalk(
        0xFE,
        (
            "Before, I jumped in without paying\x01",
            "attention to the risk, but...\x02",
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

    label("loc_4097")

    Jump("loc_489C")

    label("loc_409C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DB")

    ChrTalk(
        0xFE,
        (
            "As a trader, I have to pay attention to how the\x01",
            "Trade Conference goes whether I like it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, if they'll have the chance, the Empire\x01",
            "and Republic will try to have their own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How much we'll be able to demand to both\x01",
            "countries will depend on Mayor Dieter's skills.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_42C2")

    label("loc_41DB")


    ChrTalk(
        0xFE,
        (
            "Regarding the trade relationships arrangement,\x01",
            "if they'll have the chance, the Empire and \x01",
            "Republic will try to have their own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How much we'll be able to demand to both\x01",
            "countries will depend on Mayor Dieter's skills.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C2")

    Jump("loc_489C")

    label("loc_42C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42D5")
    Jump("loc_489C")

    label("loc_42D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4447")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B2")

    ChrTalk(
        0xFE,
        (
            "I'm not sure whether it's due to the\x01",
            "Trade Conference, but stock averages\x01",
            "have risen over the past several days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have loved to buy\x01",
            "a few, but... I can't\x01",
            "with my current funds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4442")

    label("loc_43B2")


    ChrTalk(
        0xFE,
        (
            "Looking at the stock prices like\x01",
            "this, I want to buy some, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. For now, I have no choice\x01",
            "but to focus on my core business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4442")

    Jump("loc_489C")

    label("loc_4447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4455")
    Jump("loc_489C")

    label("loc_4455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_489C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4816")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, you're the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "R-Remember me? I'm that\x01",
            "trader you rescued during\x01",
            "the Cult incident.\x02",
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
            "#00100FHave you noticed any change\x01",
            "in your health since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I went to see a doctor at\x01",
            "St. Ursula Hospital, and as you\x01",
            "can see, I'm right as rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the incident, my debt wasn't\x01",
            "so high so as to cause bankruptcy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for your help back then.\x01",
            "I'm grateful to all of you, even now.\x02",
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
            "awhile back, but I don't\x01",
            "know how to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, I thought I'd repay\x01",
            "my debt to you guys with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end it's a personal gift, so \x01",
            "I'd be glad if you just accepted it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood... \x01",
            "If that's how it is, then\x01",
            "we'll gratefully accept it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 5)
    Jump("loc_489C")

    label("loc_4816")


    ChrTalk(
        0xFE,
        (
            "I'm glad I got to meet all\x01",
            "of you again like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for your help back then.\x01",
            "I'm grateful to all of you, even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_489C")

    TalkEnd(0xFE)
    Return()

    # Function_12_3939 end

    def Function_13_48A0(): pass

    label("Function_13_48A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B44")

    ChrTalk(
        0xFE,
        (
            "Try to install "Pom!" on the\x01",
            "Support Section terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, contact me\x01",
            "via your ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. \x01",
            "We'll contact you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FBy the way, is it really okay for us\x01",
            "to install a game on a police terminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, now that you mention it...\x01",
            "I wonder if we need permission for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, I already got\x01",
            "permission from the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I explained it as a test case\x01",
            "for promotion of the orbal net,\x01",
            "I got permission easily.\x02",
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
        "#10106F(H-He's skillful, in a sort of way.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*. He's the person\x01",
            "in charge of Crossbell's\x01",
            "orbal network, after all.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BAD")

    label("loc_4B44")


    ChrTalk(
        0xFE,
        (
            "Try to install "Pom!" on the\x01",
            "Support Section terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, contact me\x01",
            "via your ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BAD")

    Jump("loc_4D61")

    label("loc_4BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBA")

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
            "Doing that and expanding your circle of\x01",
            "friends is the real pleasure of this game.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D61")

    label("loc_4CBA")


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
            "Doing that and expanding your circle of\x01",
            "friends is the real pleasure of this game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D61")

    TalkEnd(0xFE)
    Return()

    # Function_13_48A0 end

    def Function_14_4D65(): pass

    label("Function_14_4D65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4D76")
    Jump("loc_5AF8")

    label("loc_4D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D84")
    Jump("loc_5AF8")

    label("loc_4D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E5F")

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
            "I heard their true identity is the "Red\x01",
            "Constellation", that jaeger corps of ill\x01",
            "repute... What will happen from now on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF8")

    label("loc_4E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EF3")

    ChrTalk(
        0xFE,
        "I've been busy somehow ever since morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the work's been difficult. I have\x01",
            "to be careful not to overexert myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF8")

    label("loc_4EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFC")

    ChrTalk(
        0xFE,
        "Now then, it's about time for the lunch shift change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what should I have. I heard\x01",
            "today's lunch A was a meat dish, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, I can't,\x01",
            "I can't. It's not\x01",
            "break time yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sheesh. This is a sign I'm slacking off.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_507B")

    label("loc_4FFC")


    ChrTalk(
        0xFE,
        (
            "When mealtime approaches, my thoughts\x01",
            "inevitably turn to how hungry I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, my training is still insufficient.\x02",
    )

    CloseMessageWindow()

    label("loc_507B")

    Jump("loc_5AF8")

    label("loc_5080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519E")

    ChrTalk(
        0xFE,
        (
            "It seems that lately\x01",
            "unknown monsters have been\x01",
            "appearing within the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We in the security department aren't\x01",
            "limited to anti-personnel tactics. We\x01",
            "know a fair bit about fighting monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be extra safe, we have\x01",
            "to be ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5250")

    label("loc_519E")


    ChrTalk(
        0xFE,
        (
            "We in the security department aren't\x01",
            "limited to anti-personnel tactics. We\x01",
            "know a fair bit about fighting monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be extra safe, we have\x01",
            "to be ready for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5250")

    Jump("loc_5AF8")

    label("loc_5255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_547E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F6")

    ChrTalk(
        0xFE,
        (
            "There's a training room in this\x01",
            "building exclusively for employee use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, those of us in the\x01",
            "security department who need\x01",
            "exercise put it to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been seldom lately,\x01",
            "but I sometimes see\x01",
            "Lady Mariabell in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see her in training gear\x01",
            "you would normally never see\x01",
            "her in, dripping sweat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I say it...\x01",
            "It makes my heart pound.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5479")

    label("loc_53F6")


    ChrTalk(
        0xFE,
        (
            "*a-ahem*... I said something\x01",
            "unnecessary there at the end.\x02",
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

    label("loc_5479")

    Jump("loc_5AF8")

    label("loc_547E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_56FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552F")

    ChrTalk(
        0xFE,
        (
            "It seems a burglar entered\x01",
            "Lady Mariabell's room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, I haven't seen any\x01",
            "suspicious persons...\x01",
            "Have I been totally tricked?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_557F")

    label("loc_552F")


    ChrTalk(
        0xFE,
        (
            "Tch, I haven't seen any\x01",
            "suspicious persons...\x01",
            "Have I been totally tricked?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557F")

    Jump("loc_56F8")

    label("loc_5584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5673")

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
            "Even so, we in the security department\x01",
            "didn't sense anyone's presence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of trick did\x01",
            "Phantom Thief B use!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_56F8")

    label("loc_5673")


    ChrTalk(
        0xFE,
        (
            "Even so, we in the security department\x01",
            "didn't sense anyone's presence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of trick did\x01",
            "Phantom Thief B use!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F8")

    Jump("loc_5AF8")

    label("loc_56FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_570B")
    Jump("loc_5AF8")

    label("loc_570B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_589E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5827")

    ChrTalk(
        0xFE,
        (
            "In advance of the Trade Conference,\x01",
            "the police and CGF have finally\x01",
            "stepped up their security activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of the IBC security\x01",
            "department are fully\x01",
            "supporting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We received detailed communications\x01",
            "from the police's security task force.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5899")

    label("loc_5827")


    ChrTalk(
        0xFE,
        (
            "After all, we have to help each\x01",
            "other out in times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We plan to do all we\x01",
            "can to support you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5899")

    Jump("loc_5AF8")

    label("loc_589E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_591E")

    ChrTalk(
        0xFE,
        (
            "Hmm, Mayor Crois seems\x01",
            "to be very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He must be able to manage\x01",
            "due to the support of\x01",
            "Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF8")

    label("loc_591E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A42")

    ChrTalk(
        0xFE,
        (
            "Oh, you're the police's Special\x01",
            "Support Section, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome to IBC. If it is something security-\x01",
            "related within the building, we, the\x01",
            "security department, will take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us have pride that our\x01",
            "stamina wouldn't lose to the CGF.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5AF8")

    label("loc_5A42")


    ChrTalk(
        0xFE,
        (
            "If it is something security-related within the building,\x01",
            "we, the security department, will take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us have pride that our\x01",
            "stamina wouldn't lose to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AF8")

    TalkEnd(0xFE)
    Return()

    # Function_14_4D65 end

    def Function_15_5AFC(): pass

    label("Function_15_5AFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B0D")
    Jump("loc_6781")

    label("loc_5B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B1B")
    Jump("loc_6781")

    label("loc_5B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0xFE,
        (
            "It seems that no concrete demands\x01",
            "have come in from the armed group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even within the security department,\x01",
            "guesses are flying about, but...\x01",
            "It can't be helped if it's weird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6781")

    label("loc_5BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C5A")

    ChrTalk(
        0xFE,
        "Good work today, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, it's raining outside.\x01",
            "Please watch out for your health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6781")

    label("loc_5C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5D02")

    ChrTalk(
        0xFE,
        (
            "Recently, I've hardly\x01",
            "ever seen Mayor Dieter\x01",
            "in this IBC building.\x02",
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
    Jump("loc_6781")

    label("loc_5D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5EDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E41")

    ChrTalk(
        0xFE,
        (
            "It seems the remaining Republican\x01",
            "terrorists who attacked the Trade\x01",
            "Conference were captured yesterday.\x02",
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
            "It was a real disaster for\x01",
            "everyone else on board that train.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5ED9")

    label("loc_5E41")


    ChrTalk(
        0xFE,
        (
            "I understand some remaining terrorists\x01",
            "were discovered on board a train, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a real disaster for\x01",
            "everyone else on board that train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED9")

    Jump("loc_6781")

    label("loc_5EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_60DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6042")

    ChrTalk(
        0xFE,
        (
            "More than a month has passed since\x01",
            "Imperial and Republican terrorists\x01",
            "attacked the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that several of the perpetrators\x01",
            "still haven't been caught, but...\x02",
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
    Jump("loc_60D5")

    label("loc_6042")


    ChrTalk(
        0xFE,
        (
            "I heard that several of the perpetrators\x01",
            "still haven't been caught, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible that even now,\x01",
            "they're hidden within the state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60D5")

    Jump("loc_6781")

    label("loc_60DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_62F4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6151")

    ChrTalk(
        0xFE,
        (
            "Ah, a robber at IBC... How on\x01",
            "earth could he have slipped\x01",
            "through our security system?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62EF")

    label("loc_6151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6247")

    ChrTalk(
        0xFE,
        (
            "Truly, thank you very much for\x01",
            "resolving the theft incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was Phantom Thief B,\x01",
            "it's too bad you couldn't\x01",
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
    Jump("loc_62EF")

    label("loc_6247")


    ChrTalk(
        0xFE,
        (
            "But even so, this incident was\x01",
            "totally a petty theft, wasn't it.\x02",
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

    label("loc_62EF")

    Jump("loc_6781")

    label("loc_62F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6302")
    Jump("loc_6781")

    label("loc_6302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_64CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6412")

    ChrTalk(
        0xFE,
        (
            "And inspection of this IBC building\x01",
            "by the Republican President is\x01",
            "planned for tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In line with that, almost all of us at the\x01",
            "security department will be handling security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I'm already getting nervous, somehow.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_64C6")

    label("loc_6412")


    ChrTalk(
        0xFE,
        (
            "And inspection of this IBC building\x01",
            "by the Republican President is\x01",
            "planned for tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think about tomorrow's\x01",
            "security... I'm already getting nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C6")

    Jump("loc_6781")

    label("loc_64CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A7")

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
        "I think that's really amazing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_662E")

    label("loc_65A7")


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
            "Just on that point alone, those\x01",
            "two are amazing individuals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_662E")

    Jump("loc_6781")

    label("loc_6633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F3")

    ChrTalk(
        0xFE,
        (
            "Welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I'm in charge of security,\x01",
            "I can provide simple guidance too. \x01",
            "What might your business be today?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6781")

    label("loc_66F3")


    ChrTalk(
        0xFE,
        (
            "Welcome to the International\x01",
            "Bank of Crossbell.\x02",
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

    label("loc_6781")

    TalkEnd(0xFE)
    Return()

    # Function_15_5AFC end

    def Function_16_6785(): pass

    label("Function_16_6785")

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

    def lambda_6903():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6903)

    def lambda_6914():
        OP_98(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6914)
    Sleep(50)

    def lambda_6931():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6931)

    def lambda_6942():
        OP_98(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6942)
    Sleep(700)

    def lambda_695F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_695F)

    def lambda_6970():
        OP_98(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6970)
    Sleep(50)

    def lambda_698D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_698D)

    def lambda_699E():
        OP_98(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_699E)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOk then, we had a request\x01",
            "from Chief Roberts, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYes. Let's ask the receptionist,\x01",
            "Miss Lanfei, to announce us.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)

    NpcTalk(
        0x10,
        "Man's Voice",
        "Oh, you are...\x02",
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

    def lambda_6AFF():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6AFF)
    Sleep(50)

    def lambda_6B1C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B1C)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#12P#10105FMayor Dieter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAnd Miss Mariabell.\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1700, 14870, 5000)
    MoveCamera(43, 22, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13820, 5000)

    def lambda_6BAC():
        OP_98(0x101, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BAC)
    Sleep(50)

    def lambda_6BC9():
        OP_98(0x102, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BC9)
    Sleep(50)

    def lambda_6BE6():
        OP_98(0x109, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6BE6)
    Sleep(50)

    def lambda_6C03():
        OP_98(0x105, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C03)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10100FDid you come\x01",
            "to IBC today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02800FYeah, work at the bank\x01",
            "has been piling up a lot.\x02\x03",
            "#02804FBut thanks to Bell's\x01",
            "help, we just finished \x01",
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
            "Uhuhu... I feel like\x01",
            "it's been so long since\x01",
            "I've seen all of you.\x02\x03",
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
            "#12P#00109F*giggle*. Fortunately, we restarted\x01",
            "the SSS activities a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P#02905FHmm, now let me have a look at you...\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1500, 14870, 2000)
    MoveCamera(44, 26, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(14510, 2000)

    def lambda_6E5F():

        label("loc_6E5F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6E5F")

    QueueWorkItem2(0x101, 1, lambda_6E5F)
    Sleep(50)

    def lambda_6E74():

        label("loc_6E74")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6E74")

    QueueWorkItem2(0x109, 1, lambda_6E74)
    Sleep(50)

    def lambda_6E89():

        label("loc_6E89")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6E89")

    QueueWorkItem2(0x105, 1, lambda_6E89)
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
        "#12P#10111FWha...wha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309F*phew*♪\x02",
    )

    CloseMessageWindow()

    def lambda_6F32():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F32)
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
            "#5P#02902FHm hm, your health\x01",
            "looks satisfactory.\x02\x03",
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
            "#12P#00113FE-Enough! And please,\x01",
            "don't say all that in\x01",
            "such an indecent way!\x02",
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

    def lambda_70B2():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_70B2)
    Sleep(50)

    def lambda_70CA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70CA)
    Sleep(1000)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#02904FBy the way, Mr. Lloyd...\x02\x03",
            "#02901FI'm sure you haven't tried\x01",
            "to pull anything with Elie\x01",
            "without my consent, have you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00012FI-Is that how you start all your conversations?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02903FYou're a dangerous man, Mr. Lloyd. It's only\x01",
            "natural that I check up on you every so often.\x02\x03",
            "#02901FYou know what will happen to you if\x01",
            "I find out you actually did... right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FUgh...\x02",
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
            "seen them for awhile, so\x01",
            "please, be more respectful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7343():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7343)
    Sleep(50)

    def lambda_7353():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7353)
    Sleep(50)

    def lambda_7363():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7363)
    Sleep(50)

    def lambda_7373():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7373)
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
            "Ladies and gentlemen, it's\x01",
            "been awhile, although I do\x01",
            "repeat myself.\x02\x03",
            "And above all, your new members,\x01",
            "Noｱl and Wazy, seem they're\x01",
            "getting used to things too.\x02\x03",
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
            "#12P#10300FHu hu, thank you for what you did back then.\x02\x03",
            "#10309FAllow me to thank you again for\x01",
            "recommending me for the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FAnd also, thank you very\x01",
            "much for our orbal car!\x02\x03",
            "#10104FIt's like a\x01",
            "dream to drive\x01",
            "such a nice car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHa ha, I'm just happy if it\x01",
            "proves useful to you guys.\x02\x03",
            "#02800FIt also means that it was worth it for\x01",
            "me to have become the new mayor.\x02\x03",
            "#02806FMayor and IBC President...\x01",
            "It's quite tiring to keep up\x01",
            "with these two roles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02906FWell in father's case,\x01",
            "him being so busy is\x01",
            "mostly his own fault.\x02\x03",
            "#02900FI keep asking him\x01",
            "to let me help\x01",
            "with things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02804FHa ha, sorry Bell. I'm just\x01",
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
            "#12P#00100F*giggle*, grandfather too\x01",
            "seems to admire your\x01",
            "vitality, "uncle".\x02\x03",
            "#00104FHe always happily says, \x01",
            ""What Crossbell needs now is\x01",
            "exactly his youth and vigor".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHa ha, I'm flattered that the veteran\x01",
            "Chairman MacDowell would say that about me.\x02\x03",
            "#02803FEven though I am still\x01",
            "a beginner in politics.\x02\x03",
            "#02800FThere are still many things\x01",
            "I have to learn from him.\x02",
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
            "at the new City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02805FOh, that's right.\x02\x03",
            "#02800FWell then ladies and gentlemen,\x01",
            "I will take my leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSorry for stopping you like\x01",
            "this when you're so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FNo no, don't worry about it. Thanks\x01",
            "to you, I was able to relax a little.\x02\x03",
            "#02804FIf there's ever anything troubling you,\x01",
            "please let me know.\x02\x03",
            "#02800FIf it's for you guys,\x01",
            "I'll gladly help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, thank you so much.\x02\x03",
            "#00104FPlease take care\x01",
            "of yourselves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#5P#02909FUhuhu, thanks Elie.\x02\x03",
            "#02900FWell then, we'll\x01",
            "take our leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FThank you for your hard work!\x02",
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
        "#00000FBusy as ever, aren't they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FWell, there's that "Trade Conference"\x01",
            "at the end of the month...\x02\x03",
            "#00100FI think their schedules are\x01",
            "planned out down to the minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, orbal car aside, it\x01",
            "seems they're doing a lot\x01",
            "for us behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, they're so busy that I wish they\x01",
            "took better care of themselves.\x02\x03",
            "#00000F...Anyway, now we need to\x01",
            "check in with Chief Roberts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYes, let's ask the receptionist\x01",
            "to announce us!\x02",
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

    # Function_16_6785 end

    def Function_17_7F0C(): pass

    label("Function_17_7F0C")

    OP_95(0xFE, -330, 300, 15470, 2000, 0x0)
    OP_95(0xFE, -40, 300, 6500, 2000, 0x0)
    Return()

    # Function_17_7F0C end

    def Function_18_7F35(): pass

    label("Function_18_7F35")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_7F35 end

    def Function_19_7F4C(): pass

    label("Function_19_7F4C")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x190, 0x7D0, 0x0)
    Return()

    # Function_19_7F4C end

    def Function_20_7F63(): pass

    label("Function_20_7F63")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_7F63 end

    def Function_21_7F7A(): pass

    label("Function_21_7F7A")

    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_7F7A end

    def Function_22_7F91(): pass

    label("Function_22_7F91")

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
        "#12P#00100FGood day, Miss Lanfei.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8176")

    ChrTalk(
        0xA,
        (
            "#5POh, if it isn't Mr. Lloyd and\x01",
            "Lady Elie. Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt looks like the SSS has\x01",
            "started back up again.\x02",
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
        "#5PYes, that goes without saying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSo then, what can I\x01",
            "help you with today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D6")

    label("loc_8176")


    ChrTalk(
        0xA,
        (
            "#5PMy, it's Miss Elie and the Support Section.\x01",
            "What business might you have with us today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D6")


    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're here in regard to\x01",
            "Chief Roberts' request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh. In that case,\x01",
            "I know about that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884C")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8413")

    ChrTalk(
        0xA,
        "#5PAh, but before that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe exchange service access card\x01",
            "I gave to the Support Section\x01",
            "awhile back has expired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI have prepared a new one\x01",
            "for you, so please take it.\x02",
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
            "#5PPlease present your card at the\x01",
            "exchange counter, just like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe will convert Sepith to Mira for\x01",
            "you at a better rate than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8593")

    label("loc_8413")


    ChrTalk(
        0xA,
        (
            "#5POh yes, before that... \x01",
            "There's something I must give you.\x02",
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
            "#5PIt is a card that identifies\x01",
            "you as a preferred customer\x01",
            "at our bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you present it at the counter,\x01",
            "you can exchange Sepith for\x01",
            "Mira at a higher rate than normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8593")

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
            "※Simply talk to Lanfei and after\x01",
            "selecting [Exchange Sepith] choose \x01",
            ""Exchange" to use this service.\x07\x00\x02",
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
            "#12P#10105FI-Is it really ok for us to\x01",
            "use a service like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, of course. You are all\x01",
            "good friends of both Mayor\x01",
            "Crois and Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThis accommodation is only a matter of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, then shall we\x01",
            "make good use of it?\x02",
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
        "#5PUh uh, I will be waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell then, please wait\x01",
            "a moment while I call\x01",
            "Chief Roberts for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8882")

    label("loc_884C")


    ChrTalk(
        0xA,
        (
            "#5PHe will receive you, so\x01",
            "please wait a moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8882")

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

    def lambda_897B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_897B)

    def lambda_898C():
        OP_95(0xFE, 6410, 0, 16170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_898C)
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
        "#6P#00000FChief Roberts, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You came after seeing my request, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Man, that really helps me.\x01",
            "It's a job I absolutely\x01",
            "must have you do for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, this one\x01",
            "seems kind of fun.\x02\x03",
            "#10304FIt was something about the\x01",
            "final test for some service...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100F"Pom!",\x01",
            "I think it was.\x02",
        )
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
        "#6P#00005FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hu hu, I'm sure you guys will love it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well then, can you accept\x01",
            "my request right away?\x02",
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
            "The truth is, we plan\x01",
            "to release an orbal\x01",
            "game called "Pom!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The number of orbal net\x01",
            "terminal owners in the city has\x01",
            "been increasing, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FAn orbal game...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FIs it different\x01",
            "from billiards\x01",
            "or poker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, it's similar in that\x01",
            "there're fixed rules and\x01",
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
        (
            "#6P#00003FS-Somehow that\x01",
            "sounds amazing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThen, the "test" that's the\x01",
            "subject of your request is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Of course, I want\x01",
            "you to test this\x01",
            ""Pom!" game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After all, in software development\x01",
            "bugs may appear, so test cycles\x01",
            "are critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHmm, but for a test of this\x01",
            "level, can't the Foundation\x01",
            "do it themselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tio has been helping\x01",
            "us with this testing\x01",
            "for a while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Actually, there're two problems.\x01",
            "I want help from outside the\x01",
            "Foundation no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FTwo problems...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yeah. As for the first...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tio sometimes\x01",
            "activates her "Aeon\x01",
            "System" during testing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So the test data we\x01",
            "get isn't so useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105F"Aeon System"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's that thing that\x01",
            "Tio often uses.\x02\x03",
            "#00104FShe explained\x01",
            "it a little before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, it's a system she uses when operating\x01",
            "orbal terminals and her orbal staff...\x01",
            "I think it's something along those lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, I suppose I should take this\x01",
            "opportunity to give my own explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            ""Aeon System" is the\x01",
            "name of the system built\x01",
            "into Tio's chest protector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Activation of Arts from the orbal\x01",
            "staff with no wait, highspeed\x01",
            "data processing abilities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Supporting those is the\x01",
            "system's main function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It takes incredible aptitude\x01",
            "to master this system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FR-Right. It doesn't\x01",
            "sound simple at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FTopics like this are tough\x01",
            "when Tio's not around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSo you're saying that system\x01",
            "is not suitable for testing?\x02",
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
            "When she uses the Aeon System, she makes \x01",
            "big chains no normal person could ever make, \x01",
            "and ends up wiping the floor with her opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Jona is usually testing\x01",
            "against her, but he's\x01",
            "never won once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Ah, but I'm not saying\x01",
            "that Tio is cheating, ok!?\x02",
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
            "#6P#10105FUmm...\x01",
            "So, what's the\x01",
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
            "Though we connected it only recently,\x01",
            "it's possible to play this game\x01",
            "between distant terminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So we wanted to start out with a\x01",
            "practical test within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FI see...\x01",
            "So that's why.\x02\x03",
            "#00100FEven so, it's amazing\x01",
            "that you can play with\x01",
            "someone far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hu hu, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This was planned for the initial\x01",
            "stage of the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And once the orbal net becomes\x01",
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
            "#6P#00000FWow...what an incredible\x01",
            "time we live in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Sorry for rambling, but...\x01",
            "That's basically it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...So then, I'd like\x01",
            "to give you this.\x02",
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
        "#6P#00005FThis is...a Memory Quartz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The "Pom!" application data is\x01",
            "stored on that Memory Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you install it on\x01",
            "the SSS terminal, you\x01",
            "can play right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FInstall... In short, it's\x01",
            "an operation that puts the\x01",
            "program in our terminal.\x02\x03",
            "#00104FI saw Tio doing it\x01",
            "before, so I think\x01",
            "I can figure it out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell then Elie, \x01",
            "we'll leave it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, yes, very reassuring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll also give you these:\x01",
            "My ENIGMA's number\x01",
            "and "Pom!" account.\x02",
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
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Chief Roberts' Account"\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#6P#00005FA-Account...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FW-Wait a second please. \x01",
            "This is getting really complicated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Umm, basically it's \x01",
            "like a name used\x01",
            "on a network...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, just think of it\x01",
            "as something you need\x01",
            "to play with someone.\x02",
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
            "After that, contact me and\x01",
            "I'll tell you what to do next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, that's about it. Can you\x01",
            "begin the test right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FS-Sure.\x01",
            "Please, leave it to us.\x02\x03",
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
            "Quest [Beta Test Participation]\x07\x00",
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

    # Function_22_7F91 end

    def Function_23_9E20(): pass

    label("Function_23_9E20")

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

    def lambda_9F2D():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9F2D)
    Sleep(100)

    def lambda_9F4A():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9F4A)
    Sleep(100)

    def lambda_9F67():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9F67)
    Sleep(100)

    def lambda_9F84():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F84)
    Sleep(100)

    def lambda_9FA1():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9FA1)
    Sleep(100)

    def lambda_9FBE():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9FBE)
    OP_68(-70, 1400, 7250, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)

    def lambda_9FF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FF8)
    Sleep(100)

    def lambda_A00C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A00C)
    Sleep(500)

    def lambda_A020():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A020)
    Sleep(100)

    def lambda_A034():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A034)
    Sleep(500)

    def lambda_A048():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A048)
    Sleep(100)

    def lambda_A05C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A05C)
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
            "#00203F#6PHe is probably doing nothing\x01",
            "on the Foundation's floor.\x02\x03",
            "#00200FI will contact him via ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A126():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A126)

    def lambda_A133():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A133)
    Sleep(50)

    def lambda_A143():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A143)
    Sleep(50)

    def lambda_A153():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A153)
    Sleep(50)

    def lambda_A163():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A163)
    Sleep(50)

    def lambda_A173():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A173)
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
            "#00200F#5P...Hello, it is Tio.\x02\x03",
            "#00205FNo...\x01",
            "It is not for that at all.\x02\x03",
            "#00203F............\x02\x03",
            "#00211FYou are persistent, Chief.\x01",
            "Please, knock it off already.\x02",
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
        "#11P#00012F(L-Looks the same as always...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F(I wish Tio would be a little\x01",
            "easier on him, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11P(Maybe that ol' man likes\x01",
            "to be treated that way?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5P...Yes, it is about the ENIGMA II\x01",
            "emergency alert function...\x02\x03",
            "#00200F...Yes... That is right...\x02\x03",
            "#00203FYes. Please\x01",
            "come down.\x02",
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
            "#00204F#6PYes. He said he is\x01",
            "coming down right away.\x02\x03",
            "#00202FIt seems Jona is with him too.\x02",
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
            "#10100F#11PWasn't he the one who was using a\x01",
            "room in the Geofront that blew up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThe genius hacker from the\x01",
            "Epstein Foundation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PYeah, he's an impertinent\x01",
            "brat of questionable value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FIsn't he causing trouble now that\x01",
            "he's back in the Foundation office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PYes... It seems they were\x01",
            "reluctant to take him back.\x02",
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
            "──I see. So that's\x01",
            "the situation.\x02",
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
            "#02306F#11PThe orbal power's cut and we\x01",
            "can't contact them, right?\x02\x03",
            "#02301FBut Bracers are strong.\x01",
            "Can't we leave them alone?\x02",
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
            "#6P#00108FHonestly... You can't\x01",
            "say things like that, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P*sigh*, Jona's been\x01",
            "like this a lot lately.\x02",
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
            "with such a limited system!\x02\x03",
            "#02307FGive me the security code\x01",
            "and set me free, already!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)

    ChrTalk(
        0xE,
        "#5PY-You know I can't do that, Jona.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf I did, you'd just do whatever\x01",
            "you wanted again, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIn exchange, I prepared\x01",
            "a special "Pom!" training\x01",
            "program so you can beat Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02311F#12PM-Mind your own business!\x02",
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
            "#6P#00012F(It looks like he's doing a\x01",
            "good job supervising Jona.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Well, resentment aside,\x01",
            "he is quite capable.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xE,
        "#11P──Well, leaving that aside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe ENIGMA II has an alert function\x01",
            "but it might not be that useful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC89():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_AC89)
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
            "#6P#00105FSo it does have\x01",
            "such a function?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes, but its orbal waves are weak and\x01",
            "are almost impossible to detect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PUnless you're within 10 selge, you'd never be\x01",
            "able to detect it no matter what you're using.\x02",
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
        "#00306F#5PThat kind of range is difficult to work with...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301FIf they were in Crossbell City,\x01",
            "we'd know that already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...What if you combine that\x01",
            "instrument with my sensors?\x02\x03",
            "#00201FIf you need a matrix transformation\x01",
            "system, Aeon can help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11POh, in that case──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...No, that wouldn't work. If you\x01",
            "operated the sensors with Aeon, the\x01",
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
            "#6P#00006FI-I don't quite understand\x01",
            "what's so bad about it, but...\x02",
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
            "#02305F#11P──If that's the case.\x02\x03",
            "#02300FWouldn't it be better to measure\x01",
            "from the Orchis Tower roof?\x02",
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

    def lambda_B223():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B223)

    ChrTalk(
        0x103,
        "#6P#00205FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P...Jona?\x02",
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
            "#02301F#11PThe orbal alert waves are weak,\x01",
            "so you can't detect them unless\x01",
            "your instrument is nearby.\x02\x03",
            "#02303FHaving said that, if you use Tio's sensors\x01",
            "together with the instrument, the output\x01",
            "is insufficient so accuracy suffers.\x02\x03",
            "#02302FBut on top of Orchis Tower, there're no\x01",
            "obstructions so accuracy will be raised.\x01",
            "High output is practically guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PC-Cryptic as always, but...\x02",
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
        "#6P#00204F...I am surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PGoodness, well done, Jona!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI'm amazed at your talent\x01",
            "as a systems engineer!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02309F#12PH-Heheh.\x01",
            "Well, I'm that great after all!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B502():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B502)

    ChrTalk(
        0x101,
        "#6P#00002FWell then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FIt seems like things are looking up, then?\x02",
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
            "management department immediately and\x01",
            "ask for permission to use the roof.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(150)

    ChrTalk(
        0xE,
        "#5PYou'll help, won't you Jona?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02302F#12PWhy should I? ──That's what I want to say,\x01",
            "but... Well, I'm bored so I guess I'll help.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02301F#11PBut you guys'll do one thing\x01",
            "for me in exchange. Alright!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FHa ha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FWe'll do whatever you ask as\x01",
            "long as it's not unreasonable.\x02",
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
            "Chief Roberts and Jona got permission\x01",
            "to use the Orchis Tower roof and went\x01",
            "there in advance with their equipment.\x02\x03",
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

    # Function_23_9E20 end

    def Function_24_B8F4(): pass

    label("Function_24_B8F4")

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
            "#5PEveryone...\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCould it be that\x01",
            "you're here for Lady\x01",
            "Mariabell's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we wanted to ask you about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FIt seems that Bell's\x01",
            "precious antique dolls\x01",
            "have been stolen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FCould they be the ones made\x01",
            "by the Rosenberg Studio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, that's right.\x01",
            "Lady Mariabell seems\x01",
            "terribly distraught too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is sudden, but can you \x01",
            "accept milady's request?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB74")
    Call(0, 27)

    label("loc_BB74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB9D")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BBA7")

    label("loc_BB9D")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_BBA7")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_B8F4 end

    def Function_25_BBC3(): pass

    label("Function_25_BBC3")

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
            "Quit\x01",        # 1
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
        (0, "loc_BC1F"),
        (1, "loc_BC24"),
        (SWITCH_DEFAULT, "loc_BCEB"),
    )


    label("loc_BC1F")

    Jump("loc_BCEB")

    label("loc_BC24")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry, our hands\x01",
            "are a little full right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI see... It can't\x01",
            "be helped, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf by chance you find the time,\x01",
            "please speak with me once again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C6, 1)
    Jump("loc_BCEB")

    label("loc_BCEB")

    Return()

    # Function_25_BBC3 end

    def Function_26_BCEC(): pass

    label("Function_26_BCEC")

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
            "#5PLady Mariabell seems terribly\x01",
            "distraught over her antique\x01",
            "dolls having been stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is sudden, but can you \x01",
            "accept milady's request?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE4F")
    Call(0, 27)

    label("loc_BE4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE78")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BE82")

    label("loc_BE78")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_BE82")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_26_BCEC end

    def Function_27_BE9E(): pass

    label("Function_27_BE9E")


    ChrTalk(
        0x101,
        "#00000FYes, allow us to accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FMiss Mariabell has helped us\x01",
            "with various things, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PUh uh, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI will issue you all a card. \x01",
            "Please accept it.\x02",
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
        "#12P#10305FHmm, what kind of thing is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's an IBC authentication card,\x01",
            "like the one we received before.\x02\x03",
            "#00103FIf we have this, we have permission to\x01",
            "go to certain floors using the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FI see, so it's a security\x01",
            "system. As expected of the\x01",
            "biggest bank on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBy the way, using that card, you\x01",
            "should be able to go to the same\x01",
            "floors as the one you had last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PLady Mariabell is waiting for\x01",
            "you in the President's office\x01",
            "on 16F, so please go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x7A, 0x1, 0x0)
    SetScenarioFlags(0x157, 0)
    Return()

    # Function_27_BE9E end

    def Function_28_C226(): pass

    label("Function_28_C226")

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
            "Quest [The Missing Collection]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_28_C226 end

    def Function_29_C293(): pass

    label("Function_29_C293")

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
            "#5POh, the Special Support Section...\x01",
            "What can I do for you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, actually... We'd like to\x01",
            "ask IBC to cooperate on an\x01",
            "investigation we're conducting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMiss Lanfei, could you\x01",
            "do an IBC account\x01",
            "search for us?\x02\x03",
            "We want to investigate\x01",
            "mira transfers related\x01",
            "to a certain account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHmm... An account, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHmm... If relation to any\x01",
            "incident is confirmed, \x01",
            "I can do it, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...That's right. First, can you tell\x01",
            "me the details of your situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I understand.\x01",
            "You see...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the details of\x01",
            "the suspected fraud case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#5PI see... \x01",
            "So that is the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWill that be enough to get\x01",
            "permission to search the accounts?\x02",
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
            "related to an incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI can do it, if you are fine with\x01",
            "me telling you what I see on my\x01",
            "terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, that will be fine. \x01",
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
            "#5PAccount name, "Mr. Minneth"... \x01",
            "(*klak klak, klak klak klak klak*)\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P"Quincy Company" subsidiary,\x01",
            ""Armorica Honey Company"... \x01",
            "(*klak, klak klak, klak klak klak*)\x02",
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
        "#5P...Oh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FW-What's wrong?\x02\x03",
            "Is there some\x01",
            "kind of problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#5PUmm... It is not\x01",
            "like I can give you\x01",
            "the balance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe "Armorica Honey Company" account\x01",
            "has the bare minimum of mira on deposit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm... \x01",
            "Then that means...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PW-Well... Accounts intended for\x01",
            "corporate use require a certain amount\x01",
            "of capital to be opened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POnly that minimum level of\x01",
            "mira is present... In other words,\x01",
            "tens of thousands of mira are missing.\x02",
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
            "#00200FCandy factory construction, \x01",
            "fields management and so on...\x02\x03",
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
            "of the land deeds and made various deals, \x01",
            "the balance hasn't changed...\x02\x03",
            "...Yes, it's quite unnatural.\x01\x02\x03",
            "It's almost as if he prepared\x01",
            "the account solely to gain\x01",
            "Mr. Derrick's trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see. Hu hu, that's \x01",
            "clearly contradictory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I think we got some good evidence here.\x02\x03",
            "Thank you very much for your\x01",
            "cooperation, Miss Lanfei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PNo, I'm glad I\x01",
            "could be of help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you ever need anything,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, we'll do.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE0")
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
            "◆MacDowell Residence? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",             # 0
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
        (0, "loc_CECB"),
        (1, "loc_CED0"),
        (2, "loc_CED8"),
        (SWITCH_DEFAULT, "loc_CEE0"),
    )


    label("loc_CECB")

    Jump("loc_CEE0")

    label("loc_CED0")

    SetScenarioFlags(0x177, 5)
    Jump("loc_CEE0")

    label("loc_CED8")

    ClearScenarioFlags(0x177, 5)
    Jump("loc_CEE0")

    label("loc_CEE0")

    OP_29(0x87, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_CFA8")
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FAlright. With this, we've\x01",
            "collected material on each of\x01",
            "Minneth's suspicious points.\x02\x03",
            "For now, let's return to\x01",
            "Mr. Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes sir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_D028")

    label("loc_CFA8")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F...We still need to search the MacDowell\x01",
            "residence. Let's hurry there and investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FRoger!\x02",
    )

    CloseMessageWindow()

    label("loc_D028")

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

    # Function_29_C293 end

    def Function_30_D066(): pass

    label("Function_30_D066")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D143")

    ChrTalk(
        0x8,
        (
            "Ladies and gentlemen, you need an\x01",
            "authentication card to use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business here, go to the\x01",
            "reception desk and explain yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 6)
    Jump("loc_D1E4")

    label("loc_D143")


    ChrTalk(
        0x8,
        (
            "Ladies and gentlemen, you need an\x01",
            "authentication card to use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business here, go to the\x01",
            "reception desk and explain yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E4")

    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_30_D066 end

    SaveToFile()

Try(main)
