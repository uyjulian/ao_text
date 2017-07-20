from ScenarioHelper import *

def main():
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
        "Security guard wong",         # 1
        "Security guard Paul",           # 2
        "Receptionist Lanfi",         # 3
        "Receptionist Colinna",         # 4
        "Trade quotient rezero",           # 5
        "Citizen",                   # 6
        "Roberts boss",           # 7
        "Yona",                   # 8
        "Mayor of Dieter",         # 9
        "Marybele",             # 10
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
        "Function_6_71E",          # 06, 6
        "Function_7_2023",         # 07, 7
        "Function_8_278A",         # 08, 8
        "Function_9_2794",         # 09, 9
        "Function_10_2901",        # 0A, 10
        "Function_11_2905",        # 0B, 11
        "Function_12_377D",        # 0C, 12
        "Function_13_4448",        # 0D, 13
        "Function_14_488E",        # 0E, 14
        "Function_15_54AF",        # 0F, 15
        "Function_16_5FD8",        # 10, 16
        "Function_17_7656",        # 11, 17
        "Function_18_767F",        # 12, 18
        "Function_19_7696",        # 13, 19
        "Function_20_76AD",        # 14, 20
        "Function_21_76C4",        # 15, 21
        "Function_22_76DB",        # 16, 22
        "Function_23_9598",        # 17, 23
        "Function_24_AEE6",        # 18, 24
        "Function_25_B1DA",        # 19, 25
        "Function_26_B300",        # 1A, 26
        "Function_27_B4B1",        # 1B, 27
        "Function_28_B814",        # 1C, 28
        "Function_29_B888",        # 1D, 29
        "Function_30_C5D7",        # 1E, 30
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

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('ＩＢＣ认证卡片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B3")
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
    Jump("loc_71A")

    label("loc_65F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To exchange money\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_715")

    label("loc_6E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_715")

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_715")

    Jump("loc_669")

    label("loc_71A")

    TalkEnd(0xA)
    Return()

    # Function_5_5B8 end

    def Function_6_71E(): pass

    label("Function_6_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_2022")

    label("loc_72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_73A")
    Jump("loc_2022")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(
        0xA,
        (
            "In a form involving the general population\x01",
            "I will occupy Mainz … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There is also a concern about the impact on IBC,\x01",
            "As soon as this happens, stock prices say that\x01",
            "It is not a story of level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, everyone in Mainz\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8F8")

    label("loc_849")


    ChrTalk(
        0xA,
        (
            "There is also a concern about the impact on IBC,\x01",
            "As soon as this happens, stock prices say that\x01",
            "It is not a story of level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, everyone in Mainz\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F8")

    Jump("loc_2022")

    label("loc_8FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(
        0xA,
        (
            "As for the power net,\x01",
            "The more you touch it\x01",
            "You will notice that charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Corinna is a guiding game\x01",
            "Although I say it is the best,\x01",
            "My favorite is the weather forecast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it is not 100 to flowing,\x01",
            "I admire it quite well so I admire every day\x01",
            "I'm seeing you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AAD")

    label("loc_A18")


    ChrTalk(
        0xA,
        (
            "It is being swept by the power net\x01",
            "The weather forecast is quite right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, today's forecast is\x01",
            "\"Rainy weather - in the afternoon\x01",
            "It seems to be a chance to recover completely \".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD")

    Jump("loc_2022")

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(
        0xA,
        (
            "The skill of Corinna's terminal operation ……\x01",
            "Rather than the skill of the guiding game\x01",
            "It was enough to contest 1 or 2 even inside the company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From time to time, from the Epstein Foundation\x01",
            "Various game software\x01",
            "Test requests may come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well saying that well,\x01",
            "I do it within the range that I can do outside my business hours\x01",
            "It is voluntary though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C4D")

    label("loc_BE9")


    ChrTalk(
        0xA,
        (
            "Even so, towards the screen\x01",
            "I can not help being so fun ……\x01",
            "Hehe, I'm a little envious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4D")

    Jump("loc_2022")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0xA,
        (
            "If we can do\x01",
            "I will cooperate with anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there is something again\x01",
            "Please do not hesitate to come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7D")

    label("loc_CE3")


    ChrTalk(
        0xA,
        (
            "Marybele Governor\x01",
            "From business trips safely yesterday\x01",
            "I was returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As soon as you return,\x01",
            "Today with the department from the first morning\x01",
            "Although I am busy with adjustment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7D")

    Jump("loc_2022")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169B")

    ChrTalk(
        0xA,
        (
            "Oh, everyone.\x01",
            "If you are Mr. Mary Bell president\x01",
            "I'm on a business trip abroad ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 0)), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(
        0x101,
        (
            "#00005FMaria Bell \"Governor of the Government\" … …\x02\x03",
            "#00003FOh, surely at the Crossbell Times\x01",
            "I was on top.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6D")

    label("loc_E44")


    ChrTalk(
        0x101,
        "#00005FMaria Bell \"Governor of the Governor\" … ….?\x02",
    )

    CloseMessageWindow()

    label("loc_E6D")


    ChrTalk(
        0x102,
        (
            "#00100FYeah, my job as president of my uncle\x01",
            "Since the Board of Directors took over,\x01",
            "She seems to have been appointed shortly afterwards.\x02\x03",
            "#00104FIn other words,\x01",
            "Bell can be said to be the top of IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSomehow, at that age\x01",
            "At last it feels like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIf Maria Bell, I will nod, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FYup.\x01",
            "When I think about it again, it is ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo, she's also working\x01",
            "It is not proportional to the past\x01",
            "Is it a feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, it will be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Do not overload your lady\x01",
            "The board of directors is united\x01",
            "I am supporting the situation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As it was in the position of acting Governor of the Governor,\x01",
            "Show your face everywhere\x01",
            "Because necessity comes out by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see……\x01",
            "I heard that you are quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, the lady is\x01",
            "I will be back on the evening of this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, from tomorrow it is also\x01",
            "Schedule at various meetings and talks etc\x01",
            "I was completely filled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry but,\x01",
            "For the time being for the lady\x01",
            "I think that I can not see you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F9")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "That's right -\x01",
            "From the lady to everyone\x01",
            "There was a message.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Account of Maria Bell\"\x07\x00",
            "I got it.\x02",
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
            "#00005FThis is \"Pomto! \"of\x01",
            "account……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMarybele also\x01",
            "Are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#18C\"Huh, this is\x01",
            "As a person engaged in the technical department\x01",
            "It is a natural taste. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#18C\"Come and register, please.\x01",
            "With my transcendental skill\x01",
            "I will give you a coat bottle. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "… That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FEr, now ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FNo way, Lloyd's reaction\x01",
            "Did you read it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F……I guess.\x01",
            "I can do it if the bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Truly Ellie Lady.\x01",
            "That's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, it really is a big deal.\x02\x03",
            "#10302FBesides, your sister's voice is also\x01",
            "It was pretty.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "No……\x01",
            "I imitated too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tentatively,\x01",
            "The message will be over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The lady even makes a claim\x01",
            "Since we will not release the terminal,\x01",
            "How about trying a game quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1693")

    label("loc_15F9")


    ChrTalk(
        0x102,
        (
            "#00104FYes, I understand.\x02\x03",
            "#00100FFrom Ranfi's also\x01",
            "Do not push yourself too hard\x01",
            "Please tell the bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, I got it.\x02",
    )

    CloseMessageWindow()

    label("loc_1693")

    SetScenarioFlags(0x16D, 0)
    Jump("loc_1733")

    label("loc_169B")


    ChrTalk(
        0xA,
        (
            "Marybele Governor\x01",
            "Today's night, returning from a business trip\x01",
            "It is planned to be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry but,\x01",
            "For the time being for the lady\x01",
            "I do not think we can meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1733")

    Jump("loc_2022")

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(
        0xA,
        (
            "In the future we will further improve the security aspects of the building\x01",
            "It seems necessary to strengthen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, Mary Bell lady's\x01",
            "Retrieve the stolen doll\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there is something again\x01",
            "Please come over at any time.\x01",
            "Everyone is welcome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1900")

    label("loc_185A")


    ChrTalk(
        0xA,
        (
            "Mary Bell lady's\x01",
            "Retrieve the stolen doll\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there is something again\x01",
            "Please come over at any time.\x01",
            "Everyone is welcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_1AA9")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F1")

    ChrTalk(
        0xA,
        (
            "With that authentication card,\x01",
            "An elevator is available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the same floor as you gave it to everyone before\x01",
            "You should be able to get off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mr. Maria Bell is the president of the 16th floor\x01",
            "Since I am waiting,\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AA9")

    label("loc_19F1")


    ChrTalk(
        0xA,
        (
            "With that authentication card,\x01",
            "On the same floor as you gave it to everyone before\x01",
            "You should be able to get off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mr. Maria Bell is the president of the 16th floor\x01",
            "Since I am waiting,\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA9")

    Jump("loc_2022")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1ABC")
    Jump("loc_2022")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC2")

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
            "If there is something you need\x01",
            "Please do as much as possible today.\x01",
            "Because it will be a temporary rest day tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FTemporary rest days, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FTo be sure, tomorrow afternoon, Republic\x01",
            "President Rock Smith\x01",
            "I will be observing IBC.\x02\x03",
            "After all, for that reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Eli, you are early ears.\x01",
            "Yes, that's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No matter what you say,\x01",
            "President Locksmith is in the VIP\x01",
            "Because it comes with VIP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the day of the event, it is also for business people in the building\x01",
            "I ask you to pay for it at all\x01",
            "We are planning to pick you up in a perfect system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIndeed, toward Michelam\x01",
            "Is it the equivalent response?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWell, of course it is natural.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAnyway, I understood the circumstances.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fthank you for your politeness.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 7)
    Jump("loc_1E3A")

    label("loc_1DC2")


    ChrTalk(
        0xA,
        (
            "Tomorrow, IBC\x01",
            "It is a temporary rest day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone, if there is something you need\x01",
            "Please do as much as possible today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3A")

    Jump("loc_2022")

    label("loc_1E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(
        0xA,
        (
            "The matter of the chief's request\x01",
            "It seems that it ended successfully.\x01",
            "Hehe, thanks for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you also from me\x01",
            "I will tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7F")

    label("loc_1EDA")


    ChrTalk(
        0xA,
        (
            "Roberts is in the IBC building\x01",
            "Always at the Epstein foundation branch\x01",
            "We are keeping you busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We are also conducting net relations\x01",
            "I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_2022")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9F")
    Call(0, 7)
    Jump("loc_2022")

    label("loc_1F9F")


    ChrTalk(
        0xA,
        (
            "To the Special Affairs Support Division\x01",
            "For maximum convenience\x01",
            "We accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the future, if there is something\x01",
            "Please come at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2022")

    Return()

    # Function_6_71E end

    def Function_7_2023(): pass

    label("Function_7_2023")

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
            "#5POh, Ms. Lloyd, Mr. Eli.\x01",
            "It is after a long absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PApparently, the Special Affairs Division's\x01",
            "It seems that your work has been resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FFrom now on again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PYes, of course.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2398")

    ChrTalk(
        0xA,
        (
            "#5PBy the way, to the support department before\x01",
            "For operation test of new cash service\x01",
            "I think that you have cooperated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PActually, the card you handed at that time\x01",
            "The expiration date has expired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAs it is newly prepared,\x01",
            "Please accept me here.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#5PThis card as before\x01",
            "Please present at reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWith a higher cash rate than usual\x01",
            "Let me change sepis to Mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250F")

    label("loc_2398")


    ChrTalk(
        0xA,
        (
            "#5PBy the way, to everyone\x01",
            "There was something to hand it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PPlease accept me here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00005FIs this card …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, there,\x01",
            "Be a privileged member\x01",
            "It is a card to show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you can present it at the reception desk,\x01",
            "With a higher cash rate than usual\x01",
            "Let me change sepis to Mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250F")


    ChrTalk(
        0x109,
        (
            "#12P#10105FWell, that kind of service\x01",
            "Can we accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, everyone is Mayor of Cloes,\x01",
            "As well as Mary Bell\x01",
            "Because I am an important friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PIt is a matter of course to take advantage of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, I'd appreciate it\x01",
            "I wonder if you accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FCome and I will use it next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHehe, I will be waiting.\x02",
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
            "* IBC's cashing service is now available.\x01",
            "From the usual shop menu,\x01",
            "You can cash a sepice at a high rate.\x02\x03",
            "※ Talk to Ranfi,\x01",
            "After choosing \"Sepis cash on delivery\"\x01",
            "If you choose <EXCHANGE> you can do cash.\x07\x00\x02",
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

    # Function_7_2023 end

    def Function_8_278A(): pass

    label("Function_8_278A")

    TalkBegin(0xFE)
    Call(0, 9)
    TalkEnd(0xFE)
    Return()

    # Function_8_278A end

    def Function_9_2794(): pass

    label("Function_9_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2848")
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "Please wait a while.\x01",
            "(Kata Kata, Qatat … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am currently accepting the contents of your contract\x01",
            "We will inquire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, thank you.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2900")

    label("loc_2848")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xD,
        (
            "Wh … what the hell are you?\x01",
            "No way to interrupt\x01",
            "I guess not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sorry,\x01",
            "On that sofa\x01",
            "Please wait for the turn.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_2900")

    Return()

    # Function_9_2794 end

    def Function_10_2901(): pass

    label("Function_10_2901")

    Call(0, 11)
    Return()

    # Function_10_2901 end

    def Function_11_2905(): pass

    label("Function_11_2905")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2916")
    Jump("loc_3779")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2924")
    Jump("loc_3779")

    label("loc_2924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DE")

    ChrTalk(
        0xB,
        (
            "What hit Mainz was\x01",
            "It seems equivalent dangerous people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To be honest, even at the security department of our place\x01",
            "Level which can not be dealt with … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whew.\x01",
            "It is not a funny story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A5F")

    label("loc_29DE")


    ChrTalk(
        0xB,
        (
            "The armed group that struck Mainz\x01",
            "To be honest, even at the security department of our place\x01",
            "Level which can not be dealt with … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whew.\x01",
            "It is not a funny story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5F")

    Jump("loc_3779")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AF7")

    ChrTalk(
        0xB,
        (
            "When going out on a rainy day\x01",
            "It is bullshit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If the power net expands further,\x01",
            "Even at work you can at home\x01",
            "I'd like to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3779")

    label("loc_2AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    ChrTalk(
        0xB,
        "(Katakatakata, Kataatatachi ……!)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(Tuyen, Zhu Dada Dada!)\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B9E")

    ChrTalk(
        0x101,
        "#00005FWell, what the heck is that …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD4")

    ChrTalk(
        0x102,
        "#00105FI wonder what kind of sound …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2BD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C31")

    ChrTalk(
        0x103,
        (
            "#00203F…… This sound was recently developed by the foundation\x01",
            "It is a shooting game.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2C31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C71")

    ChrTalk(
        0x104,
        "#00305FWhat kind of sounds are you announcing …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0x109,
        "#10105FThis is a gunshot …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDA")

    ChrTalk(
        0x105,
        "#10302FHuh, she seems to be enjoying something.\x02",
    )

    CloseMessageWindow()

    label("loc_2CDA")

    Sleep(50)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "I'm sorry, the customer.\x01",
            "Looking like this, I am now\x01",
            "It was in the middle of a break time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Therefore, various consultation\x01",
            "Thank you in the front reception.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F9E")

    label("loc_2D88")


    ChrTalk(
        0xB,
        "(Katakatakata, Kataatatachi ……!)\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(Queen, Zedo Doodo Doo!)\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E28")

    ChrTalk(
        0x101,
        "#00012F(It looks like I'm really concentrating … …)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2E28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E68")

    ChrTalk(
        0x102,
        "#00106F(Oh, it seems not to bother you …).\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2E68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2")

    ChrTalk(
        0x103,
        (
            "#00205F(This turnover … …!\x01",
            "…… Apparently certainly\x01",
            "It seems to be better than Jonah. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F16")

    ChrTalk(
        0x104,
        "#00306F(Well, it seems that you did not get in the way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2F16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F63")

    ChrTalk(
        0x109,
        (
            "#10106F(Even\x01",
            "It seems you are concentrating … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2F63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9E")

    ChrTalk(
        0x105,
        "#10302F(Huh, it's a stunning entrance.)\x02",
    )

    CloseMessageWindow()

    label("loc_2F9E")

    Jump("loc_3779")

    label("loc_2FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_306B")

    ChrTalk(
        0xB,
        (
            "Recent Maria Bell Lady\x01",
            "Too busy, lunch time too\x01",
            "You do not seem to be stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Often it is done during the move,\x01",
            "Always block type portable meals\x01",
            "It seems to be carried around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3779")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D1")

    ChrTalk(
        0xB,
        (
            "Since the mayor's independent advocacy,\x01",
            "Continental financial market is pretty\x01",
            "It sounds like it is shaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although there is no extreme bias,\x01",
            "Selling and buying both quotes\x01",
            "It was in a net increase trend, respectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether the judgment is positive or not …\x01",
            "Everything depends on future crossbells\x01",
            "It is decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, the fluctuation of the stock price index is\x01",
            "It is a life pattern as it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3254")

    label("loc_31D1")


    ChrTalk(
        0xB,
        (
            "Mr. Rezero gave a past failure\x01",
            "Being reflective, becoming rather careful\x01",
            "It seems to be like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I personally\x01",
            "I think that it is a correct judgment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3254")

    Jump("loc_3779")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3375")

    ChrTalk(
        0xB,
        (
            "Yesterday for a presidential visit\x01",
            "My work was off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I could not feel like going out to the alert situation city,\x01",
            "If you notice it one day on the bed\x01",
            "I have spent it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As it was, I fostered spirit,\x01",
            "With a conducting net terminal at home\x01",
            "I have thought thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33FC")

    label("loc_3375")


    ChrTalk(
        0xB,
        (
            "Yesterday at home\x01",
            "With a conductive net terminal\x01",
            "I have thought thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If that happens, the day will be a full day\x01",
            "I played a game of leadership.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FC")

    Jump("loc_3779")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_340F")
    Jump("loc_3779")

    label("loc_340F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3420")
    Call(0, 9)
    Jump("loc_3779")

    label("loc_3420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E1")

    ChrTalk(
        0xB,
        "(Katakatakata, Kataatatachi ……!)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        (
            "After all, on a rainy day\x01",
            "There will be few customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Put off collected administrative procedures\x01",
            "It is a great opportunity.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3524")

    label("loc_34E1")


    ChrTalk(
        0xB,
        (
            "Sometimes there are days like this,\x01",
            "It seems that work does not go easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3524")

    Jump("loc_3779")

    label("loc_3529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")

    ChrTalk(
        0xB,
        (
            "Dynamic network of technical department\x01",
            "Finally the second test finally\x01",
            "It is clear at the initial stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Simply put, more data\x01",
            "Faster, more securely and stably\x01",
            "Is it possible to send and receive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks, so far it was private only for the company\x01",
            "Some of the terminals also go to the outside network\x01",
            "I started the connection step by step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is lady Mary Bell\x01",
            "It is the guy who is the strength of the staff of the technical department.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3779")

    label("loc_36C5")


    ChrTalk(
        0xB,
        (
            "Mayor Clois\x01",
            "The results of this secondary test\x01",
            "She seems to be quite helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although it is limited to documents with low confidentiality,\x01",
            "Already with Bang Bang power net\x01",
            "I heard that they are interacting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3779")

    TalkEnd(0xB)
    Return()

    # Function_11_2905 end

    def Function_12_377D(): pass

    label("Function_12_377D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_378E")
    Jump("loc_4444")

    label("loc_378E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_379C")
    Jump("loc_4444")

    label("loc_379C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3839")

    ChrTalk(
        0xFE,
        (
            "Apparently, Mainz\x01",
            "It seems to be a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is still on the financial market yet\x01",
            "Although little influence is seen,\x01",
            "I guess it will be a matter of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_3839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3931")

    ChrTalk(
        0xFE,
        (
            "If someone gets it,\x01",
            "On the other hand someone loses … …\x01",
            "It is a truth of the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And one more …\x01",
            "There is no \"absolute\" in the price world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you intend to start investing,\x01",
            "Within the range where self-responsibility can be taken\x01",
            "We will strongly recommend investing in funds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39E7")

    label("loc_3931")


    ChrTalk(
        0xFE,
        (
            "If you intend to start investing,\x01",
            "Within the range where self-responsibility can be taken\x01",
            "We will strongly recommend investing in funds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is not absolutely in the market world, but …\x01",
            "Behavior beyond body length\x01",
            "I think that absolutely misery is accompanied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E7")

    Jump("loc_4444")

    label("loc_39EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9A")

    ChrTalk(
        0xFE,
        "Why, what …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got such a value this morning\x01",
            "Stocks are far away\x01",
            "I was down ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Because this is it,\x01",
            "I do not know who's called the market.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B13")

    label("loc_3A9A")


    ChrTalk(
        0xFE,
        (
            "I got such a value this morning\x01",
            "Stocks are far away\x01",
            "I was down ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Because this is it,\x01",
            "I do not know who's called the market.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B13")

    Jump("loc_4444")

    label("loc_3B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCE")

    ChrTalk(
        0xFE,
        (
            "Hmm, this morning for the Republic\x01",
            "You can see price movements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also the stocks that I was eyeing\x01",
            "It seems it was buying … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say now,\x01",
            "It's just a result.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C36")

    label("loc_3BCE")


    ChrTalk(
        0xFE,
        (
            "The stock that I was watching was\x01",
            "It seems it was buying … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say now,\x01",
            "It's just a result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C36")

    Jump("loc_4444")

    label("loc_3C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D18")

    ChrTalk(
        0xFE,
        (
            "As I thought …\x01",
            "The market seems to be quite unstable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, the tremor is intermittent so far\x01",
            "And market prices are also unusual to read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Risk is also considerable … …\x01",
            "Even if you mistake amateurs\x01",
            "I think you better not give out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D86")

    label("loc_3D18")


    ChrTalk(
        0xFE,
        (
            "Before me I would not mind risking\x01",
            "I was just jumping in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, this is\x01",
            "The one who does not put out a hand is safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D86")

    Jump("loc_4444")

    label("loc_3D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E69")

    ChrTalk(
        0xFE,
        (
            "The trade meeting's position as a trader\x01",
            "It is a place to worry even a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the Imperial Republic,\x01",
            "I will try to pass on me if I do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where can we promote concessions to both countries,\x01",
            "It is a place to show off the mayor of the mayor of Dieter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F04")

    label("loc_3E69")


    ChrTalk(
        0xFE,
        (
            "Concerning trade related agreements\x01",
            "The Empire and the Republic\x01",
            "I will try to pass on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where can we promote concessions to both countries,\x01",
            "It is a place to show off the mayor of the mayor of Dieter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F04")

    Jump("loc_4444")

    label("loc_3F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F17")
    Jump("loc_4444")

    label("loc_3F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD6")

    ChrTalk(
        0xFE,
        (
            "From the influence of the trade meeting\x01",
            "For the last few days, the average share price is also\x01",
            "It seems to be on an upward trend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would like to buy even by me\x01",
            "I have stocks ……\x01",
            "I can not help it with the former hand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_404C")

    label("loc_3FD6")


    ChrTalk(
        0xFE,
        (
            "Looking at the market in this way,\x01",
            "I'm getting tired of buying stocks … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, for a while\x01",
            "Do you have to earn with your main business on a steady path?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404C")

    Jump("loc_4444")

    label("loc_4051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_405F")
    Jump("loc_4444")

    label("loc_405F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4444")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D8")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, you are the Special Affairs Division … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, do you remember me?\x01",
            "You guys were helped by you in the case of the example\x01",
            "He is a trader.\x02",
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
            "#00100FSince then\x01",
            "Does your body change?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, now at Ursula hospital\x01",
            "I have been examined,\x01",
            "This street is healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I had a debt after the incident\x01",
            "It was not enough for the company to crush … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you very much for that time.\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "Will you accept this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, before from a business partner\x01",
            "I got it,\x01",
            "It is something I can not use for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And even a little to you guys\x01",
            "I want to return my favor with some form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a personal gift to the end,\x01",
            "I'm glad if you accept it silently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understand……\x01",
            "That's it.\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 5)
    Jump("loc_4444")

    label("loc_43D8")


    ChrTalk(
        0xFE,
        (
            "To you guys\x01",
            "It was nice to meet you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you very much for that time.\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4444")

    TalkEnd(0xFE)
    Return()

    # Function_12_377D end

    def Function_13_4448(): pass

    label("Function_13_4448")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BA")

    ChrTalk(
        0xFE,
        (
            "\"Pomutto! To the terminal of the support department\x01",
            "Please install it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Afterwards with Enigma\x01",
            "You should give me a call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understand,\x01",
            "I will contact you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FBy the way, to the police terminal\x01",
            "Is it ok to put games or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, remember that … …\x01",
            "Do I need permission?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh, already to the police\x01",
            "I got permission from myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Promote a conducting net\x01",
            "I explained one of the test cases\x01",
            "Please do not accept permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(No, I do have a good deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Huhu, once for the crossbell\x01",
            "Conductive network related\x01",
            "Because it seems to be responsible. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4728")

    label("loc_46BA")


    ChrTalk(
        0xFE,
        (
            "\"Pomutto! To the terminal of the support department\x01",
            "Please install it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Afterwards with Enigma\x01",
            "You should give me a call.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4728")

    Jump("loc_488A")

    label("loc_472D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4803")

    ChrTalk(
        0xFE,
        (
            "\"Pomutto! \"Test of,\x01",
            "I thank you for going out with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once officially started spreading,\x01",
            "Talk to various people\x01",
            "You can collect accounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then it's time to spread the circle\x01",
            "It's the real pleasure of that game.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_488A")

    label("loc_4803")


    ChrTalk(
        0xFE,
        (
            "Formally \"Pomto! \"of\x01",
            "Once popularization began,\x01",
            "You can collect a lot of accounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then it's time to spread the circle\x01",
            "It's the real pleasure of that game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488A")

    TalkEnd(0xFE)
    Return()

    # Function_13_4448 end

    def Function_14_488E(): pass

    label("Function_14_488E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_489F")
    Jump("loc_54AB")

    label("loc_489F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48AD")
    Jump("loc_54AB")

    label("loc_48AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4955")

    ChrTalk(
        0xFE,
        (
            "Anything armed group,\x01",
            "Fire power to overwhelm the guard as well\x01",
            "It seems to be equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The identity is the unknown hunting corps\x01",
            "I heard that it is \"red constellation\" … …\x01",
            "How are you going to get out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_4955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49C0")

    ChrTalk(
        0xFE,
        "Somehow, it seems to be busy from the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that it is various difficulties,\x01",
            "Do not over taste too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_49C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAA")

    ChrTalk(
        0xFE,
        "Well, it is almost time for change in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what shall I eat?\x01",
            "Today 's A lunch seems meat dish … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I do not mind.\x01",
            "Still in a break\x01",
            "I did not mean it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is absolutely evidence that it is lax.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4B17")

    label("loc_4AAA")


    ChrTalk(
        0xFE,
        (
            "When rice time approaches, thinking is indeed\x01",
            "Anything for people with appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I still have a lack of training.\x02",
    )

    CloseMessageWindow()

    label("loc_4B17")

    Jump("loc_54AB")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C1C")

    ChrTalk(
        0xFE,
        (
            "Anything recently, within autonomous state\x01",
            "The incomprehensible monster\x01",
            "It seems that it came to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our security department not only interpersonal\x01",
            "Regarding battle with demons\x01",
            "I have some knowledge … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, in case of emergency\x01",
            "Do whatever you do with all your attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4CB5")

    label("loc_4C1C")


    ChrTalk(
        0xFE,
        (
            "We as security department not only interpersonal\x01",
            "Regarding battle with demons\x01",
            "I have some knowledge … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, in case of emergency\x01",
            "Do whatever you do with all your attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB5")

    Jump("loc_54AB")

    label("loc_4CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E47")

    ChrTalk(
        0xFE,
        (
            "This IBC building has a dedicated employee\x01",
            "I have a training room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We, IBC Security Department, of course,\x01",
            "Even for employees with shortage of exercise\x01",
            "It is actively used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, opportunities have decreased recently,\x01",
            "Mary Bell Lady\x01",
            "There are also quite a few things to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally I can never see you anymore\x01",
            "In the form of training wear\x01",
            "I'm going sweating ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What to say ……\x01",
            "That will be exciting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4ED2")

    label("loc_4E47")


    ChrTalk(
        0xFE,
        (
            "Ko, Kohon …… a little at the end\x01",
            "I have told extra things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And anyway, our company\x01",
            "Training room\x01",
            "The facilities are fulfilling and it is the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED2")

    Jump("loc_54AB")

    label("loc_4ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_512C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8A")

    ChrTalk(
        0xFE,
        (
            "In the room of Maria Bell Lady\x01",
            "The pirate seems to have entered ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cut, you see something of suspicious person\x01",
            "It was supposed to have been … …\x01",
            "Is that thing fooled cheaply?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4FE2")

    label("loc_4F8A")


    ChrTalk(
        0xFE,
        (
            "Cut, you see something of suspicious person\x01",
            "It was supposed to have been … …\x01",
            "Is that thing fooled cheaply?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE2")

    Jump("loc_5127")

    label("loc_4FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BB")

    ChrTalk(
        0xFE,
        (
            "Lady's precious dolls\x01",
            "Thank you for replying.\x01",
            "I will also reward you from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, we are in the security department\x01",
            "I do not even understand the sign … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kaitou B is a monster\x01",
            "How did you use it! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5127")

    label("loc_50BB")


    ChrTalk(
        0xFE,
        (
            "Anyway, we are in the security department\x01",
            "I do not even understand the sign … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kaitou B is a monster\x01",
            "How did you use it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5127")

    Jump("loc_54AB")

    label("loc_512C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_513A")
    Jump("loc_54AB")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523C")

    ChrTalk(
        0xFE,
        (
            "Before the trade meeting,\x01",
            "Police and guard watch out for\x01",
            "It has finally gone into full swing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even our IBC security department\x01",
            "To those alert activities fully\x01",
            "It is supposed to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Close with the police's security guard headquarters\x01",
            "I will get in touch with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_52B0")

    label("loc_523C")


    ChrTalk(
        0xFE,
        (
            "Anyway, at such times\x01",
            "You are helping each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can do it,\x01",
            "I will cooperate with everything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B0")

    Jump("loc_54AB")

    label("loc_52B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_535C")

    ChrTalk(
        0xFE,
        (
            "Hmm, we are mayor of Clois\x01",
            "It is quite a busy scene as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still it is something I can do\x01",
            "Cooperation of Maria Bell Old Lady\x01",
            "Thanks to you I do not think otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_535C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_54AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5435")

    ChrTalk(
        0xFE,
        (
            "Okay, you guys\x01",
            "Was it the police 's Special Affairs Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome to IBC.\x01",
            "If it is related to conservation inside the building\x01",
            "Leave it to us security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will not lose to the guard at our place\x01",
            "I am proud of my strength.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_54AB")

    label("loc_5435")


    ChrTalk(
        0xFE,
        (
            "If it is related to conservation inside the building\x01",
            "Leave it to us security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will not lose to the guard at our place\x01",
            "I am proud of my strength.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AB")

    TalkEnd(0xFE)
    Return()

    # Function_14_488E end

    def Function_15_54AF(): pass

    label("Function_15_54AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_54C0")
    Jump("loc_5FD4")

    label("loc_54C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54CE")
    Jump("loc_5FD4")

    label("loc_54CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5577")

    ChrTalk(
        0xFE,
        (
            "Armed groups still have nothing concrete\x01",
            "I heard he does not make a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even within the security department, already various\x01",
            "The speculation is on the flight … …\x01",
            "It is creepy and unavoidable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_5577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_55EC")

    ChrTalk(
        0xFE,
        "Everyone, thank you for your work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is unfortunately rain outside,\x01",
            "Please take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_55EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_56B0")

    ChrTalk(
        0xFE,
        (
            "Recently, at this IBC building\x01",
            "I see the mayor of Dieter\x01",
            "Opportunities almost disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As it is about the mayor, please take care\x01",
            "I think that it is being done … …\x01",
            "I am a little worried if I can not see your face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_56B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AE")

    ChrTalk(
        0xFE,
        (
            "I hit the trade meeting\x01",
            "Remnants of Republic-based terrorists\x01",
            "You seem to have been caught yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything by train to the Republic\x01",
            "I was discovered where I was about to return,\x01",
            "It seems there was a riot … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got on such a train.\x01",
            "The customer is really a disaster.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_582C")

    label("loc_57AE")


    ChrTalk(
        0xFE,
        (
            "The remnants of any terrorist\x01",
            "It is said that it was found in the train … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got on such a train.\x01",
            "The customer is really a disaster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582C")

    Jump("loc_5FD4")

    label("loc_5831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5953")

    ChrTalk(
        0xFE,
        (
            "By the terrorists of the Imperial and Republic\x01",
            "From the incident of the trade council\x01",
            "It's been more than a month since early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some of the executing offenders still\x01",
            "I heard that they are not caught … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will not be able to return home easily so easily,\x01",
            "Perhaps it is still in autonomous state\x01",
            "Perhaps you are doing it too late.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_59D9")

    label("loc_5953")


    ChrTalk(
        0xFE,
        (
            "Some of the executing offenders still\x01",
            "I heard that they are not caught … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it is still in autonomous state\x01",
            "Perhaps you are doing it too late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D9")

    Jump("loc_5FD4")

    label("loc_59DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A53")

    ChrTalk(
        0xFE,
        (
            "Oh, a thief to IBC … …\x01",
            "This security system\x01",
            "So how can I get together?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAD")

    label("loc_5A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B28")

    ChrTalk(
        0xFE,
        (
            "Please solve the theft case\x01",
            "thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How much is Kaitou B,\x01",
            "The criminal did not get caught\x01",
            "I'm sorry, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, as a result\x01",
            "There was not any damage\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5BAD")

    label("loc_5B28")


    ChrTalk(
        0xFE,
        (
            "Anyway, this incident is\x01",
            "It is a completely pleasant offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The stolen goods came back\x01",
            "Is it something ……\x01",
            "I feel that the mystery has grown more and more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAD")

    Jump("loc_5FD4")

    label("loc_5BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BC0")
    Jump("loc_5FD4")

    label("loc_5BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C90")

    ChrTalk(
        0xFE,
        (
            "President of the Republic tomorrow afternoon\x01",
            "This IBC building\x01",
            "I will be visiting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Along with that, our security department\x01",
            "It is almost planned to be guarded by the total figure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I feel nervous as soon as possible.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5D1B")

    label("loc_5C90")


    ChrTalk(
        0xFE,
        (
            "President of the Republic tomorrow afternoon\x01",
            "This IBC building\x01",
            "I will be visiting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think about security of the day ……\x01",
            "I feel nervous as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1B")

    Jump("loc_5FD4")

    label("loc_5D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E01")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter and Mary Bell,\x01",
            "Now more than ever\x01",
            "It sounds like he's busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the two of us are\x01",
            "The concern to the surroundings\x01",
            "I will never forget smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think that it is truly amazing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5E9C")

    label("loc_5E01")


    ChrTalk(
        0xFE,
        (
            "When I am busy,\x01",
            "I can not afford to be concerned about things around me\x01",
            "I can never have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you take only one point,\x01",
            "The two of you are wonderfully wonderful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9C")

    Jump("loc_5FD4")

    label("loc_5EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F53")

    ChrTalk(
        0xFE,
        (
            "Welcome.\x01",
            "Welcome to Cros Bell International Bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am in charge of security,\x01",
            "You can do as much as a simple guide.\x01",
            "What are your requirements today?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5FD4")

    label("loc_5F53")


    ChrTalk(
        0xFE,
        (
            "Welcome.\x01",
            "Welcome to Cros Bell International Bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With various bank procedures\x01",
            "Front and right hand reception, either\x01",
            "We can correspond.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD4")

    TalkEnd(0xFE)
    Return()

    # Function_15_54AF end

    def Function_16_5FD8(): pass

    label("Function_16_5FD8")

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

    def lambda_6156():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6156)

    def lambda_6167():
        OP_98(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6167)
    Sleep(50)

    def lambda_6184():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6184)

    def lambda_6195():
        OP_98(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6195)
    Sleep(700)

    def lambda_61B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_61B2)

    def lambda_61C3():
        OP_98(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_61C3)
    Sleep(50)

    def lambda_61E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_61E0)

    def lambda_61F1():
        OP_98(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61F1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell, from the Roberts Director\x01",
            "There was a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYes, immediately, Mr. Ranfi at reception\x01",
            "Shall I take it over?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)

    NpcTalk(
        0x10,
        "Male voice",
        "Oh, you are …\x02",
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

    def lambda_634C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_634C)
    Sleep(50)

    def lambda_6369():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6369)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#12P#10105FMayor of Dieter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlso, Mr. Marybele.\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1700, 14870, 5000)
    MoveCamera(43, 22, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13820, 5000)

    def lambda_6401():
        OP_98(0x101, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6401)
    Sleep(50)

    def lambda_641E():
        OP_98(0x102, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_641E)
    Sleep(50)

    def lambda_643B():
        OP_98(0x109, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_643B)
    Sleep(50)

    def lambda_6458():
        OP_98(0x105, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6458)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10100FToday for the IBC\x01",
            "You had it, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#02800FOh, the job at the bank\x01",
            "It was so much accumulated.\x02\x03",
            "#02804FWhile helping the bell,\x01",
            "Just a while ago\x01",
            "It is the place that has finished.\x02",
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
            "Uhufu, everyone … ….\x01",
            "You can also face each other\x01",
            "It is a while ago.\x02\x03",
            "I wonder Ellie was doing well, too?\x02",
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
            "#12P#00109FHehe, thanks to the other day,\x01",
            "The support department also restarted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P#02905FHmm, how old … ….\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1500, 14870, 2000)
    MoveCamera(44, 26, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(14510, 2000)

    def lambda_66B9():

        label("loc_66B9")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66B9")

    QueueWorkItem2(0x101, 1, lambda_66B9)
    Sleep(50)

    def lambda_66CE():

        label("loc_66CE")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66CE")

    QueueWorkItem2(0x109, 1, lambda_66CE)
    Sleep(50)

    def lambda_66E3():

        label("loc_66E3")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66E3")

    QueueWorkItem2(0x105, 1, lambda_66E3)
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
        "#12P#10111FUnderstand\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FHu ♪\x02",
    )

    CloseMessageWindow()

    def lambda_678A():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_678A)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#12P#00112FWait a minute, bell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#02902FHmm, health state is\x01",
            "It seems to be good.\x02\x03",
            "#02904FThis soft and warm feeling,\x01",
            "I certainly feel under the limbs\x01",
            "Flexible muscle response ……\x02\x03",
            "#02909FWell, I do not collect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FEven ….!\x01",
            "A dangerous way of speaking one by one\x01",
            "Do not do it!\x02",
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

    def lambda_690C():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_690C)
    Sleep(50)

    def lambda_6924():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6924)
    Sleep(1000)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#02904FBy the way Mr. Lloyd ……\x02\x03",
            "#02901FIn my opinion without any notice,\x01",
            "Affiliation with Ellie\x01",
            "You did not put out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00012FOh, is it it suddenly it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02903FMr. Lloyd is a dangerous figure,\x01",
            "Periodic checks are obvious.\x02\x03",
            "#02901FIf you take such action\x01",
            "When you discover … … You know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FWow ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FAhaha, I'm wary of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00106FAlready, if the bell ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02806FWell, bell.\x01",
            "Because I saw it for the first time in a long time\x01",
            "Please be a little more self-weighted.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B51():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B51)
    Sleep(50)

    def lambda_6B61():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B61)
    Sleep(50)

    def lambda_6B71():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B71)
    Sleep(50)

    def lambda_6B81():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B81)
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
            "It's been a long time, everyone.\x02\x03",
            "New members Noel and Waz\x01",
            "It seems that you are familiar with anything else.\x02\x03",
            "Restart of the Special Affairs Support Division,\x01",
            "Let me celebrate with this opportunity.\x02",
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
            "#12P#10300FHuh, for that reason.\x02\x03",
            "#10309FThe matter of recommendation to support department,\x01",
            "I will thank you once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FThe matter of paying a guided vehicle\x01",
            "Thank you very much!\x02\x03",
            "#10104FSuch a nice guided car\x01",
            "To be able to drive,\x01",
            "It seems like a dream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHaha, your\x01",
            "I would be fortunate if it helped.\x02\x03",
            "#02800FIt is worthwhile for me to become a new mayor\x01",
            "It is said that it was.\x02\x03",
            "#02806FMayor and IBC president ……\x01",
            "It is because of these two\x01",
            "It's pretty difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#02906FWell, in the case of your father\x01",
            "Almost busy\x01",
            "It will be your own fault, though.\x02\x03",
            "#02900FI accepted everything and everything,\x01",
            "I will also be helping you here\x01",
            "I want you to get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02804FHaha, sorry bell.\x01",
            "When thinking for crossbell\x01",
            "I do not understand the location of the hand.\x02\x03",
            "#02800FWork beyond your height\x01",
            "It tends to take over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHuhu, the grandfather too\x01",
            "To the uncle's vitality\x01",
            "It seems that you are admiring.\x02\x03",
            "#00104F\"A young politician like him is\x01",
            "It is necessary for the current crossbell,\x01",
            "I am glad to hear that you are happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FHaha, to the chairman of the senior McDaely\x01",
            "I will not be embarrassed if you say so.\x02\x03",
            "#02803FHowever, as I am a politician\x01",
            "It's still a brisk youthful.\x02\x03",
            "#02800FA lot more\x01",
            "I have to study it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#11P#02905FOh, my father.\x01",
            "It is about New Town Hall building soon.\x01",
            "It's time for a meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02805FOops, was that so.\x02\x03",
            "#02800FWell then, everyone, I will\x01",
            "I will excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI am sorry, but\x01",
            "I've stopped you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#02809FNo, it is not such a thing.\x01",
            "Thanks to you I was able to relax.\x02\x03",
            "#02804FIf there is something troubled\x01",
            "Tell me anytime.\x02\x03",
            "#02800FIf it 's all for you guys,\x01",
            "I will be lucky to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHehe, thank you.\x02\x03",
            "#00104FBoth the uncle and the bell,\x01",
            "Please only take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#5P#02909FUhufu, thank you Ellie.\x02\x03",
            "#02900FOkay, let me get rude.\x01",
            "I will get it.\x02",
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
        "#00000FAfter all, it seems quite busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FThe trade conference at the end of the month is approaching ….\x02\x03",
            "#00100FThe minute schedule is\x01",
            "I think there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, Yesterday's power car and say,\x01",
            "Variety for us\x01",
            "It looks like we're turning our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, so as not to break your body by too busy\x01",
            "I want you to be careful ……\x02\x03",
            "#00000F…… Anyway, now it's Roberts's boss\x01",
            "Shall I take on work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYes, those who are accepting\x01",
            "Let's get involved!\x02",
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

    # Function_16_5FD8 end

    def Function_17_7656(): pass

    label("Function_17_7656")

    OP_95(0xFE, -330, 300, 15470, 2000, 0x0)
    OP_95(0xFE, -40, 300, 6500, 2000, 0x0)
    Return()

    # Function_17_7656 end

    def Function_18_767F(): pass

    label("Function_18_767F")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_767F end

    def Function_19_7696(): pass

    label("Function_19_7696")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x190, 0x7D0, 0x0)
    Return()

    # Function_19_7696 end

    def Function_20_76AD(): pass

    label("Function_20_76AD")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_76AD end

    def Function_21_76C4(): pass

    label("Function_21_76C4")

    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_76C4 end

    def Function_22_76DB(): pass

    label("Function_22_76DB")

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
        "#12P#00100FHello, Mr. Ranfi.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C3")

    ChrTalk(
        0xA,
        (
            "#5POh, Ms. Lloyd, Mr. Eli.\x01",
            "It is after a long absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PApparently, the Special Affairs Division's\x01",
            "It seems that your work has been resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FFrom now on again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell then, today\x01",
            "What kind of matter is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_78C3")


    ChrTalk(
        0xA,
        (
            "#5POh, everyone of the support department to Eli.\x01",
            "What kind of message is it today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")


    ChrTalk(
        0x101,
        (
            "#12P#00000FTo the Roberts Director of the Epstein Foundation\x01",
            "It is a matter that I was asked for ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, in that case\x01",
            "We accept.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F89")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7B46")

    ChrTalk(
        0xA,
        "#5PThat's right, before that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPreviously, I handed it to everyone in the support section\x01",
            "Cards used for cashing services\x01",
            "The expiration date has expired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAs it is newly prepared,\x01",
            "Please accept me here.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xA,
        (
            "#5PThis card as before\x01",
            "Please present at reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWith a higher cash rate than usual\x01",
            "Let me change sepis to Mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC9")

    label("loc_7B46")


    ChrTalk(
        0xA,
        (
            "#5PThat's right, before that … …\x01",
            "There was something to give to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PPlease accept me here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00005FIs this card …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, there,\x01",
            "Be a privileged member\x01",
            "It is a card to show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you can present it at the reception desk,\x01",
            "With a higher cash rate than usual\x01",
            "Let me change sepis to Mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CC9")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "* IBC's cashing service is now available.\x01",
            "From the usual shop menu,\x01",
            "You can cash a sepice at a high rate.\x02\x03",
            "※ Talk to Ranfi,\x01",
            "After choosing \"Sepis cash on delivery\"\x01",
            "If you choose <EXCHANGE> you can do cash.\x07\x00\x02",
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
            "#12P#10105FWell, that kind of service\x01",
            "Can we accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYes, everyone is Mayor of Cloes,\x01",
            "As well as Mary Bell\x01",
            "Because I am an important friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PIt is a matter of course to take advantage of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, I'd appreciate it\x01",
            "I wonder if you accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FCome and I will use it next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHehe, I will be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSo, to Roberts chief\x01",
            "Because I will hand over\x01",
            "just a moment please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FBF")

    label("loc_7F89")


    ChrTalk(
        0xA,
        (
            "#5PBecause I will hand over\x01",
            "just a moment please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FBF")

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

    def lambda_80B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_80B8)

    def lambda_80C9():
        OP_95(0xFE, 6410, 0, 16170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80C9)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0xE, 1)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        "Hey you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FCongratulations, Roberts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You saw the request, did not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No, really, I am saved.\x01",
            "By all means\x01",
            "It was a job I wanted to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, it seems like somehow fun\x01",
            "It was content.\x02\x03",
            "#10304FSomehow the service\x01",
            "How about the final test ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FCertainly …\x01",
            "\"Pomutto! Was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FSomehow, somewhere\x01",
            "It's a name I've heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FIt is certainly true …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Huhu, I think it will be fun ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well then, it's quick\x01",
            "Can I get a job?\x02",
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
            "#6P#00100FThen, the contents of work\x01",
            "Could you explain it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Huhu, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Actually, soon\x01",
            "\"Pomutto! It is called\x01",
            "I am planning to distribute a power game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "City's power guide net terminal\x01",
            "Develop for owners\x01",
            "I was just going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FDemand game … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FIt's billiards and\x01",
            "What is like poker\x01",
            "Is not it different?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, according to certain rules\x01",
            "In terms of winning and losing and competing for points\x01",
            "Is it similar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The most different are:\x01",
            "The ones on the terminal screen\x01",
            "It's a place to move and play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FIs not it something?\x01",
            "That sounds great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWell then, at this request\x01",
            "\"Test\" is …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Of course this\x01",
            "\"Pomutto! Test of\x01",
            "I want you to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Building a program As mentioned above,\x01",
            "A bug will come out\x01",
            "Repetition of the test is essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWell ……\x01",
            "But, for that degree of testing\x01",
            "You can do it with the Foundation, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, this test\x01",
            "Helping Mr. Tio a while ago\x01",
            "I was getting it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Actually, there are two problems.\x01",
            "Just by the Foundation\x01",
            "I'd like some help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FTwo problems …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, it is the first one … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tio is sometimes tested\x01",
            "\"Aion system\"\x01",
            "I guess it was taking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So, a bit of useful data\x01",
            "It is said that it can not be said that it was possible … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FWhat is Aion system ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FTio is a few times\x01",
            "I used it.\x02\x03",
            "#00104FBefore a little bit\x01",
            "You taught me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, surely a guiding terminal or magician\x01",
            "System used when handling …\x01",
            "It was a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, because it's this time again,\x01",
            "I'd like to explain from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "\"Aion system\"\x01",
            "For Tio's chest protector\x01",
            "It's the name of the built-in system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "With no weight by magic wand\x01",
            "Activate magic powers,\x01",
            "Tio's high speed processing ability ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To support them\x01",
            "Will it become the main function?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "How to master this system\x01",
            "I need quite aptitude, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWell,\x01",
            "It's not easy at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FAs long as there is no Tio\x01",
            "The topic of this hand is tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIn short, the system itself\x01",
            "Is not it suitable for testing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anything, with the Aion system\x01",
            "A large chain that can not be assembled by an ordinary person\x01",
            "I hope to build up and push ahead with victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Jonah to test\x01",
            "I hope to go out with you,\x01",
            "He said he had never won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Ah, but Tio is sloppy\x01",
            "I am not saying that! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To Tio you very much\x01",
            "Do not say strange things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FEr …\x01",
            "One reason for the rest\x01",
            "What kind of thing are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, the other one … …\x01",
            "When this game is a \"battle game\"\x01",
            "It's in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I mentioned a little while ago,\x01",
            "This game is far away from each other\x01",
            "I can play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So, by all means in the city\x01",
            "I wanted to do a field test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FI see……\x01",
            "Is that something like that?\x02\x03",
            "#00100FEven so\x01",
            "You can play in remote places,\x01",
            "That's pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hehe, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This is\x01",
            "It was originally planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If the power net becomes more popular,\x01",
            "Many people have fun\x01",
            "You will be able to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "For example, on such a rainy day\x01",
            "While staying in the house\x01",
            "I can enjoy it with my friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh\x01",
            "It was a wonderful era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I was a bit strange but … …\x01",
            "Well, the situation is such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… … so that you are\x01",
            "Let's give this a present.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '波波碰！β版'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('波波碰！β版', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005FThis … … memory crystals#8RMemory Quartz#Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To that memory crystal, just before completion\x01",
            "\"Pomutto! It contains the data \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I will put it in the terminal of the support department\x01",
            "Once installed,\x01",
            "You ought to be able to play right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FInstallation ……\x01",
            "In short the program to the terminal\x01",
            "It's work to incorporate.\x02\x03",
            "#00104FBefore Tio chan\x01",
            "I have seen what I am doing,\x01",
            "I think that it will manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell then Erie,\x01",
            "It will be a pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yeah yeah, it's encouraging.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I'll hand it over.\x01",
            "The number of my enigma,\x01",
            "\"Pomutto! It's an account.\x02",
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
            "\"Roberts Chief Account\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#6P#00005FA, account …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWait a moment, please.\x01",
            "Difficult terms in succession … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, in short,\x01",
            "Use on the network\x01",
            "It's like a name ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, to play matches\x01",
            "Just as necessary\x01",
            "You only have to think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Since you can leave difficult things,\x01",
            "For the time being when installing beta version\x01",
            "You only have to enter it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Then when you contact us at Enigma,\x01",
            "I will teach you the next step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… Well, it is such a place.\x01",
            "Will you start testing soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes.\x01",
            "Please choose for me.\x02\x03",
            "#00004FTentatively,\x01",
            "Let's say we return to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FWell, let's do that.\x02",
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
            "Quest 【Request for participation in β test】\x07\x00",
            "I started!\x02",
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

    # Function_22_76DB end

    def Function_23_9598(): pass

    label("Function_23_9598")

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

    def lambda_96A5():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_96A5)
    Sleep(100)

    def lambda_96C2():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_96C2)
    Sleep(100)

    def lambda_96DF():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_96DF)
    Sleep(100)

    def lambda_96FC():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_96FC)
    Sleep(100)

    def lambda_9719():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9719)
    Sleep(100)

    def lambda_9736():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9736)
    OP_68(-70, 1400, 7250, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)

    def lambda_9770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9770)
    Sleep(100)

    def lambda_9784():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9784)
    Sleep(500)

    def lambda_9798():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9798)
    Sleep(100)

    def lambda_97AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97AC)
    Sleep(500)

    def lambda_97C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97C0)
    Sleep(100)

    def lambda_97D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97D4)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00000FWell ……\x01",
            "Is Roberts the chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PProbably, on the Foundation's floor\x01",
            "I think that it is trying to keep it.\x02\x03",
            "#00200FLet's try to call him on the Enigma\x02",
        )
    )

    CloseMessageWindow()

    def lambda_988D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_988D)

    def lambda_989A():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_989A)
    Sleep(50)

    def lambda_98AA():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_98AA)
    Sleep(50)

    def lambda_98BA():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_98BA)
    Sleep(50)

    def lambda_98CA():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_98CA)
    Sleep(50)

    def lambda_98DA():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_98DA)
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
            "#00200F#5PHello, this is Tio\x02\x03",
            "#00205FHouse……\x01",
            "Separately, I will do that.\x02\x03",
            "#00203F….\x02\x03",
            "#00211FI am persistent, the boss.\x01",
            "Please be careful.\x02",
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
        "#11P#00012F(L-Looks the same as always)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F(Tio also a little more\x01",
            "I wish I could get in touch gently … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11P(If that Osassin\x01",
            "Are not you glad about being cold? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5P…… Yeah, Enigma's\x01",
            "About emergency alert function ……\x02\x03",
            "#00200FYes… Right…\x02\x03",
            "#00203FYes, as I am under\x01",
            "Thank you.\x02",
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
        "#11P#00000FIs he going to help us?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00204F#6PYeah, right away here\x01",
            "It seems to come down.\x02\x03",
            "#00202FIt sounds like Jona is there too\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FOh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PIt certainly was blown up\x01",
            "Have you used the Geo Front room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FFrom the Epstein Foundation\x01",
            "Was it genius hacker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11POh, I'm cheeky\x01",
            "It is a subtle hedgey little boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FTruly now to the Foundation's office\x01",
            "You seem to be troubling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PYeah ….\x01",
            "It seems to be an eye-cat.\x02",
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
            "─ ─ I see.\x01",
            "Was it such a circumstance?\x02",
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
            "#02306F#11PHappy, do not let it go out\x01",
            "You just can not contact?\x02\x03",
            "#02301FGood guys who bastard wrestlers,\x01",
            "You should leave it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FJona, come on\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FAlready……\x01",
            "Do not say such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PHa, when you come with Jonah\x01",
            "It has been like this all along recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIn a corner of the office\x01",
            "Newest dedicated terminal room\x01",
            "You said you prepared.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(200)

    ChrTalk(
        0xF,
        (
            "#02310F#12PHow much processing power is high\x01",
            "With such a restricted system\x01",
            "I'm satisfied with Katsu!\x02\x03",
            "#02307FFinally the security code\x01",
            "Release me! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)

    ChrTalk(
        0xE,
        "#5POh you know we cant\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf you do such a thing,\x01",
            "Do you want to do it again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PInstead \"Pomutto! \"To Mr. Tio\x01",
            "I will prepare a special training program so that I can win\x01",
            "I made it because I organized it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02311F#12PD-don't say things that aren't necessary\x02",
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
            "#6P#00012F(Thinking a little, Jonah's thing,\x01",
            "He seems to be directing properly. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Well, anywhere you wish to irritate\x01",
            "Because it is an able person. )\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xE,
        "#11PWell anyway\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt is an alert function of Enigma\x01",
            "Maybe I can not help you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A3C4)
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
        "#6P#00011FR-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FSuch a function\x01",
            "Is there something there, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYeah, the power wave is weak\x01",
            "I can hardly perceive it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P10 If you do not get close to Serge\x01",
            "I can not sense it even with measuring instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P10 selge..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PThat range makes it difficult\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301FIf you are in Crossbell city\x01",
            "It seems to be able to perceive it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F…… With my sensor\x01",
            "How about combining?\x02\x03",
            "#00201FFor a matrixed system\x01",
            "It seems possible to link with Aion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11POh in that case\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P…… No, it is no use after all.\x01",
            "How to link with Aion\x01",
            "The accuracy of the measuring instrument is too unstable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThere is also a problem of the guide pressure,\x01",
            "Because reflection of the surrounding topography is also conceivable\x01",
            "I think it is quite impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWhat, what is wrong?\x01",
            "I do not know but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FApparently technical\x01",
            "It seems there is a problem …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#02305F#11PIn that case…\x02\x03",
            "#02300FOn the roof of the Orchis Tower\x01",
            "You only have to measure it, right?\x02",
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

    def lambda_A8D7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A8D7)

    ChrTalk(
        0x103,
        "#6P#00205FHuh….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PJona?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FUh, what do you mean\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02301F#11PThe guiding wave for alert is too weak\x01",
            "If it is not near the measuring instrument\x01",
            "I can not sense it.\x02\x03",
            "#02303FIn other words,\x01",
            "Even if it is linked with Tio's sensor\x01",
            "Output is insufficient and accuracy is not enough?\x02\x03",
            "#02302FBut if the roof of a tower without obstructions\x01",
            "You will be able to increase the accuracy of sensing\x01",
            "You can ensure high output power?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PI don't get it as usual\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)

    ChrTalk(
        0x109,
        "#10100F#5PHow's that Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00204FI'm surprised!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PThat's our Jona!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PTalent as a system engineer\x01",
            "There are striking things!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02309F#12PHuh Hoon.\x01",
            "Well there are so!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB82():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AB82)

    ChrTalk(
        0x101,
        "#6P#00002FWell then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FIt sounds like we have a path forward\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FYes. It might work\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#11PImmediately, in the management department of Orkis Tower\x01",
            "Can you get permission to use the rooftop\x01",
            "Let's multiply.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(150)

    ChrTalk(
        0xE,
        "#5PJona, you'll help right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02302F#12PWhy do you want me to say ─ ─\x01",
            "Well, it's a free time and I will help you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#02301F#11PInstead, you are.\x01",
            "With this I will lend you one! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FHaha, got it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FUnless it is unreasonable request\x01",
            "I'm sure I will return it.\x02",
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
            "After that, from the administration department of Orkis Tower\x01",
            "The chiefs who got permission to use the rooftop\x01",
            "I headed to the tower ahead of time with the equipment.\x02\x03",
            "It seems that it takes some time to prepare,\x01",
            "Lloyd's tidied up other errands\x01",
            "I decided to head to the Orkis Tower.\x02",
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

    # Function_23_9598 end

    def Function_24_AEE6(): pass

    label("Function_24_AEE6")

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
            "#5Pladies and gentlemen……\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPerhaps,\x01",
            "On the request of Mr. Maria Bell\x01",
            "Could you please come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I asked in that matter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FWhatever you cherish the bell\x01",
            "Antique doll is\x01",
            "You seem to have stolen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FPerhaps, for example\x01",
            "What is made by Rosenberg Kobo …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell, that's right.\x01",
            "Mary's daughter too\x01",
            "It looks like she is very disappointed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is quickly, but the request of the lady\x01",
            "Would you accept it?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B18B")
    Call(0, 27)

    label("loc_B18B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1B4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B1BE")

    label("loc_B1B4")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B1BE")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_AEE6 end

    def Function_25_B1DA(): pass

    label("Function_25_B1DA")

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
            "undertake\x01",      # 0
            "quit\x01",          # 1
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
        (0, "loc_B23C"),
        (1, "loc_B241"),
        (SWITCH_DEFAULT, "loc_B2FF"),
    )


    label("loc_B23C")

    Jump("loc_B2FF")

    label("loc_B241")


    ChrTalk(
        0x101,
        (
            "#00006FI am sorry but,\x01",
            "Now I can not take my hand …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIs that so …?\x01",
            "There is no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf you have plenty of time to spare,\x01",
            "Please call out now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C6, 1)
    Jump("loc_B2FF")

    label("loc_B2FF")

    Return()

    # Function_25_B1DA end

    def Function_26_B300(): pass

    label("Function_26_B300")

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
            "#5PWith the antique doll's theft,\x01",
            "Mary's daughter too\x01",
            "It looks like she is very disappointed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is quickly, but the request of the lady\x01",
            "Would you accept it?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B462")
    Call(0, 27)

    label("loc_B462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B48B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B495")

    label("loc_B48B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B495")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_26_B300 end

    def Function_27_B4B1(): pass

    label("Function_27_B4B1")


    ChrTalk(
        0x101,
        "#00000FYes, I will accept it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FTo Mariavel\x01",
            "I am indebted to various people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSo, we issue cards\x01",
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
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ认证卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ认证卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x105,
        "#12P#10305FHmm, what is this like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThis was previously received by us as well\x01",
            "It's an IBC certification card.\x02\x03",
            "#00103FIf you have this elevator\x01",
            "I will be able to go to the permitted floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FI see,\x01",
            "Is it a security system?\x01",
            "I am impressed by IBC in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBy the way,\x01",
            "On the same floor as when we handed it to everyone last time\x01",
            "You can get off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PLady Marybele is the president of the 16th floor\x01",
            "Since I am waiting,\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x7A, 0x1, 0x0)
    SetScenarioFlags(0x157, 0)
    Return()

    # Function_27_B4B1 end

    def Function_28_B814(): pass

    label("Function_28_B814")

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
            "Quest 【Searching for missing collections】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_28_B814 end

    def Function_29_B888(): pass

    label("Function_29_B888")

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
            "#5POh, everyone at the Special Affairs Division ……\x01",
            "What kind of matter is today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, actually …\x01",
            "I would like the IBC to cooperate\x01",
            "There is an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRanfi,\x01",
            "Account used in IBC\x01",
            "Can you investigate?\x02\x03",
            "In that regard,\x01",
            "Movement of Mira of an account etc\x01",
            "I would like to wash it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh an account\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PNo……\x01",
            "If incidentality can be confirmed,\x01",
            "I can do it but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P… Well, first\x01",
            "Would you please let me know the detailed situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I understand.\x01",
            "Well then ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is suspected of fraud\x01",
            "I explained about this case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#5PI see……\x01",
            "Was that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTo some reason for investigation\x01",
            "Why not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAs an IBC, as it is a crime\x01",
            "When an account is used\x01",
            "It will also be involved in credit problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0xA,
        (
            "#5PYes, enough\x01",
            "I seem to be able to confirm the incidentality … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POral information of the terminal\x01",
            "If I tell you\x01",
            "I think you can approve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, that's fine.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PUnderstood, well then\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#5PName of account is \"Minnes\" ……\x01",
            "(Rattling, rattling rattling)\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P\"Quincy Company\" subsidiary,\x01",
            "\"Armorica · Honey Company\" … …\x01",
            "(Kata, rattling, rattling)\x02",
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
            "#5Pwas.\x01",
            "It is surely opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FW-what's wrong?\x02\x03",
            "After all something,\x01",
            "I was wondering if there was a problem ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#5PUh …… Detailed deposit amount etc\x01",
            "To tell you\x01",
            "I do not wish, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIn the account of \"Armorica · Honey Company\"\x01",
            "It seems that only minimal mirrors are deposited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEr …\x01",
            "What does that mean …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell, uhh.\x01",
            "In order to open an account for corporations\x01",
            "I need capital money … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThat is necessary for opening an account\x01",
            "Minimum Mira …… That is,\x01",
            "It is only about tens of thousands of mirrors.\x02",
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
            "#00200FConstruction of confectionery factory,\x01",
            "And management of each field etc. …\x02\x03",
            "To do such a thing\x01",
            "Obviously Mira is not enough …\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHe keeps the land rights document,\x01",
            "I should have dealings in various ways\x01",
            "If there is no change around that … …\x02\x03",
            "……Yup,\x01",
            "You can say that it is rather unnatural.\x02\x03",
            "To earn Derrick's credit\x01",
            "We prepared an account of only form ……\x01",
            "I wonder if that is the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI see.\x01",
            "Huh, this is an obvious contradiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSo we know they hae the funds already\x02\x03",
            "Ranfi,\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PNo, if we can do it\x01",
            "By what amount\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf there is something again\x01",
            "Please do not hesitate to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FEhe, thanks again!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C46B")
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
            "◆ McDaill House (for testing)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                  # 0
            "【We will investigate】\x01",            # 1
            "[Let's not investigate]\x01",      # 2
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
        (0, "loc_C456"),
        (1, "loc_C45B"),
        (2, "loc_C463"),
        (SWITCH_DEFAULT, "loc_C46B"),
    )


    label("loc_C456")

    Jump("loc_C46B")

    label("loc_C45B")

    SetScenarioFlags(0x177, 5)
    Jump("loc_C46B")

    label("loc_C463")

    ClearScenarioFlags(0x177, 5)
    Jump("loc_C46B")

    label("loc_C46B")

    OP_29(0x87, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_C52A")
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FAlright …. For now,\x01",
            "Pursue allegations of Minnes\x01",
            "Materials should have gathered.\x02\x03",
            "Once at Harold's house\x01",
            "Let's go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes sir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_C599")

    label("loc_C52A")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F…… The only thing left is the investigation at McDaill's house.\x01",
            "Let's go looking up quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FI understand.\x02",
    )

    CloseMessageWindow()

    label("loc_C599")

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

    # Function_29_B888 end

    def Function_30_C5D7(): pass

    label("Function_30_C5D7")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C68D")

    ChrTalk(
        0x8,
        (
            "You guys, if you use an elevator\x01",
            "You need an authentication card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have something to do\x01",
            "Go to the reception and tell the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 6)
    Jump("loc_C703")

    label("loc_C68D")


    ChrTalk(
        0x8,
        (
            "You guys, if you use an elevator\x01",
            "You need an authentication card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have something to do\x01",
            "Go to the reception and tell the matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C703")

    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_30_C5D7 end

    SaveToFile()

Try(main)
