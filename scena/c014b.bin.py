from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c014b.bin",                # FileName
        "c014b",                    # MapName
        "c014b",                    # Location
        0x0006,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c014b",                  # 0
        "Chalk",                  # 1
        "Wendy",                  # 2
        "Fernando",               # 3
        "Misette",                # 4
        "Basilio",                # 5
        "Tourist",                # 6
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
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(9329,    0,       4294965946, 270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294965777, 0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294962816, 0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11470,   4000,    4294965576, 90,   385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       4294965936, 1000,    9330,    1500,    4294965946, 0x007E, 0,  8,  0x0000)

    ChipFrameInfo(488, 0)                                        # 0

    ScpFunction((
        "Function_0_1E8",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_3F1",          # 02, 2
        "Function_3_3F7",          # 03, 3
        "Function_4_3F8",          # 04, 4
        "Function_5_545",          # 05, 5
        "Function_6_21BD",         # 06, 6
        "Function_7_29EC",         # 07, 7
        "Function_8_2A80",         # 08, 8
        "Function_9_2A84",         # 09, 9
        "Function_10_2B61",        # 0A, 10
        "Function_11_2D2C",        # 0B, 11
        "Function_12_3BC8",        # 0C, 12
        "Function_13_3C50",        # 0D, 13
        "Function_14_3D5D",        # 0E, 14
        "Function_15_3E94",        # 0F, 15
    ))


    def Function_0_1E8(): pass

    label("Function_0_1E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1E8 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
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
    Jump("Function_1_2A0")

    label("loc_3F0")

    Return()

    # Function_1_2A0 end

    def Function_2_3F1(): pass

    label("Function_2_3F1")

    ClearChrFlags(0xD, 0x80)
    Return()

    # Function_2_3F1 end

    def Function_3_3F7(): pass

    label("Function_3_3F7")

    Return()

    # Function_3_3F7 end

    def Function_4_3F8(): pass

    label("Function_4_3F8")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541")
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53C")

    label("loc_4AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D1")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53C")

    label("loc_4D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53C")

    label("loc_4F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53C")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_520")
    OP_AF(0xC0)
    Jump("loc_532")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_530")
    OP_AF(0xBF)
    Jump("loc_532")

    label("loc_530")

    OP_AF(0xBE)

    label("loc_532")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53C")

    Jump("loc_405")

    label("loc_541")

    TalkEnd(0x8)
    Return()

    # Function_4_3F8 end

    def Function_5_545(): pass

    label("Function_5_545")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BC")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E")
    MenuCmd(1, 0, "CPD (Lloyd)         Equipped")
    Jump("loc_68F")

    label("loc_66E")

    MenuCmd(1, 0, "CPD (Lloyd)         Change To")

    label("loc_68F")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6D1")
    MenuCmd(1, 0, "Blue Sheriff        Equipped")
    Jump("loc_721")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_700")
    MenuCmd(1, 0, "Blue Sheriff        Change To")
    Jump("loc_721")

    label("loc_700")

    MenuCmd(1, 0, "Blue Sheriff        1000 mira")

    label("loc_721")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_759")
    MenuCmd(1, 0, "Howling Wolf        Equipped")
    Jump("loc_7A9")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_788")
    MenuCmd(1, 0, "Howling Wolf        Change To")
    Jump("loc_7A9")

    label("loc_788")

    MenuCmd(1, 0, "Howling Wolf        1000 mira")

    label("loc_7A9")

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
    Jump("loc_858")

    label("loc_83A")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    MenuCmd(1, 0, "CPD (Elie)          Equipped")
    Jump("loc_8BD")

    label("loc_89C")

    MenuCmd(1, 0, "CPD (Elie)          Change To")

    label("loc_8BD")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_8FF")
    MenuCmd(1, 0, "Peace Green         Equipped")
    Jump("loc_94F")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_92E")
    MenuCmd(1, 0, "Peace Green         Change To")
    Jump("loc_94F")

    label("loc_92E")

    MenuCmd(1, 0, "Peace Green         1000 mira")

    label("loc_94F")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_987")
    MenuCmd(1, 0, "Spring Bird         Equipped")
    Jump("loc_9D7")

    label("loc_987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_9B6")
    MenuCmd(1, 0, "Spring Bird         Change To")
    Jump("loc_9D7")

    label("loc_9B6")

    MenuCmd(1, 0, "Spring Bird         1000 mira")

    label("loc_9D7")

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
    Jump("loc_A68")

    label("loc_A4A")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAC")
    MenuCmd(1, 0, "CPD (Tio)           Equipped")
    Jump("loc_ACD")

    label("loc_AAC")

    MenuCmd(1, 0, "CPD (Tio)           Change To")

    label("loc_ACD")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_B0F")
    MenuCmd(1, 0, "Black Cat           Equipped")
    Jump("loc_B5F")

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_B3E")
    MenuCmd(1, 0, "Black Cat           Change To")
    Jump("loc_B5F")

    label("loc_B3E")

    MenuCmd(1, 0, "Black Cat           1000 mira")

    label("loc_B5F")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_B97")
    MenuCmd(1, 0, "Shadow Circle       Equipped")
    Jump("loc_BE7")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_BC6")
    MenuCmd(1, 0, "Shadow Circle       Change To")
    Jump("loc_BE7")

    label("loc_BC6")

    MenuCmd(1, 0, "Shadow Circle       1000 mira")

    label("loc_BE7")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C5A")

    label("loc_C3C")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9E")
    MenuCmd(1, 0, "CPD (Randy)         Equipped")
    Jump("loc_CBF")

    label("loc_C9E")

    MenuCmd(1, 0, "CPD (Randy)         Change To")

    label("loc_CBF")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_D01")
    MenuCmd(1, 0, "Danger Orange       Equipped")
    Jump("loc_D51")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_D30")
    MenuCmd(1, 0, "Danger Orange       Change To")
    Jump("loc_D51")

    label("loc_D30")

    MenuCmd(1, 0, "Danger Orange       1000 mira")

    label("loc_D51")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_D89")
    MenuCmd(1, 0, "Midnight Kiss       Equipped")
    Jump("loc_DD9")

    label("loc_D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_DB8")
    MenuCmd(1, 0, "Midnight Kiss       Change To")
    Jump("loc_DD9")

    label("loc_DB8")

    MenuCmd(1, 0, "Midnight Kiss       1000 mira")

    label("loc_DD9")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E2E")

    label("loc_E10")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")
    MenuCmd(1, 0, "CGF (Noｱl)          Equipped")
    Jump("loc_E8E")

    label("loc_E6D")

    MenuCmd(1, 0, "CGF (Noｱl)          Change To")

    label("loc_E8E")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_EC6")
    MenuCmd(1, 0, "Liberty Road        Equipped")
    Jump("loc_F16")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_EF5")
    MenuCmd(1, 0, "Liberty Road        Change To")
    Jump("loc_F16")

    label("loc_EF5")

    MenuCmd(1, 0, "Liberty Road        1000 mira")

    label("loc_F16")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F4D")

    label("loc_F39")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8C")
    MenuCmd(1, 0, "White Creed         Equipped")
    Jump("loc_FAD")

    label("loc_F8C")

    MenuCmd(1, 0, "White Creed         Change To")

    label("loc_FAD")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_FE5")
    MenuCmd(1, 0, "Crest Face          Equipped")
    Jump("loc_1035")

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_1014")
    MenuCmd(1, 0, "Crest Face          Change To")
    Jump("loc_1035")

    label("loc_1014")

    MenuCmd(1, 0, "Crest Face          1000 mira")

    label("loc_1035")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1058")

    label("loc_1044")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1058")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1089")
    Sleep(1)
    Return()

    label("loc_1089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1464")

    label("loc_10C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1105")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_1464")

    label("loc_1105")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1143")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_1464")

    label("loc_1143")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1181")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1464")

    label("loc_1181")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_1464")

    label("loc_11BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FD")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_1464")

    label("loc_11FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1464")

    label("loc_123B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1279")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_1464")

    label("loc_1279")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_1464")

    label("loc_12B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F5")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1464")

    label("loc_12F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1333")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_1464")

    label("loc_1333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1371")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_1464")

    label("loc_1371")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_1464")

    label("loc_13AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13ED")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_1464")

    label("loc_13ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_1464")

    label("loc_142B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1464")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_1464")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1537")

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
    Jump("loc_1856")

    label("loc_1537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15DB")

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
    Jump("loc_1856")

    label("loc_15DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_167E")

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
    Jump("loc_1856")

    label("loc_167E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1723")

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
    Jump("loc_1856")

    label("loc_1723")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17BF")

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
    Jump("loc_1856")

    label("loc_17BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1856")

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

    label("loc_1856")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219F")
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1918")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1931")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194A")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_194A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1969")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1982")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_199B")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_199B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19BA")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_19BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19D3")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_19D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19EC")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_19EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A0B")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A24")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3D")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A57")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A70")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8A")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A9E")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A9E")
    SetScenarioFlags(0x0, 6)

    label("loc_1A9E")

    ClearScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB6")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1AB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ACF")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE8")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1AE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AFD")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1AFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B16")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B2F")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B44")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B5D")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B76")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8B")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA4")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1BA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BBD")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1BBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD2")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BEB")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C00")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C14")

    label("loc_1C00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C14")
    SetScenarioFlags(0x0, 7)

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C70")

    ChrTalk(
        0x8,
        (
            "Whaaat, you've got it already equipped?\x01",
            "Please choose another one, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2190")

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD6")

    ChrTalk(
        0x8,
        (
            "Whaaat, it looks like you're short on mira?\x01",
            "Then, you can't exchange it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2190")

    label("loc_1CD6")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DE7")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAA")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_1DE2")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC4")
    SetScenarioFlags(0x2C, 0)

    label("loc_1DC4")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_1DE2")

    label("loc_1DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDC")
    SetScenarioFlags(0x2C, 1)

    label("loc_1DDC")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_1DE2")

    Jump("loc_20D0")

    label("loc_1DE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E95")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E46")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_1E90")

    label("loc_1E46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E69")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E69")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_1E90")

    label("loc_1E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8A")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E8A")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_1E90")

    Jump("loc_20D0")

    label("loc_1E95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F42")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF3")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_1F3D")

    label("loc_1EF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F16")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F16")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_1F3D")

    label("loc_1F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F37")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F37")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_1F3D")

    Jump("loc_20D0")

    label("loc_1F42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FF1")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA2")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_1FEC")

    label("loc_1FA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC5")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FC5")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_1FEC")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE6")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FE6")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_1FEC")

    Jump("loc_20D0")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2063")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2045")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_205E")

    label("loc_2045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205B")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_205B")

    SetScenarioFlags(0x2F, 0)

    label("loc_205E")

    Jump("loc_20D0")

    label("loc_2063")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20D0")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy's ENIGMA cover was changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B7")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_20D0")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CD")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_20CD")

    SetScenarioFlags(0x2E, 4)

    label("loc_20D0")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2147")
    OP_E0(0x16, 0x0)

    label("loc_2147")


    ChrTalk(
        0x8,
        (
            "Uh uh, I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2190")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2190")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21A9")

    label("loc_219F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21A9")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_54F")

    label("loc_21BC")

    Return()

    # Function_5_545 end

    def Function_6_21BD(): pass

    label("Function_6_21BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29EB")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x4)"), scpexpr(EXPR_END)), "loc_220A")
    MenuCmd(1, 0, "Platinum        Purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_2228")

    label("loc_220A")

    MenuCmd(1, 0, "Platinum         1000 mira")

    label("loc_2228")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x4)"), scpexpr(EXPR_END)), "loc_2259")
    MenuCmd(1, 0, "Mirage          Purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_2276")

    label("loc_2259")

    MenuCmd(1, 0, "Mirage          5000 mira")

    label("loc_2276")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2322")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x4)"), scpexpr(EXPR_END)), "loc_22B5")
    MenuCmd(1, 0, "Aegis           Purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_22D3")

    label("loc_22B5")

    MenuCmd(1, 0, "Aegis           20000 mira")

    label("loc_22D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x4)"), scpexpr(EXPR_END)), "loc_2304")
    MenuCmd(1, 0, "Scepter         Purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_2322")

    label("loc_2304")

    MenuCmd(1, 0, "Scepter         50000 mira")

    label("loc_2322")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_235F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_235F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_237C")
    Sleep(1)
    Return()

    label("loc_237C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BC")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_2477")

    label("loc_23BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23FC")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_2477")

    label("loc_23FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243C")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_2477")

    label("loc_243C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2477")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_2477")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2513")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Space element Master Quartz.\x01",
            "※Raises HP/ADF, recovers HP on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2657")

    label("loc_2513")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2582")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mirage element Master Quartz.\x01",
            "※Raises EP/ATS, recovers EP on defeating an enemy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2657")

    label("loc_2582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Earth element Master Quartz.\x01",
            "※Raises DEF/ADF, gain MAX GUARD in certain conditions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2657")

    label("loc_25F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2657")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water element Master Quartz.\x01",
            "※Raises STR/ATS, gain Sepith when attacking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2657")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_278A")

    ChrTalk(
        0x8,
        (
            "Whaaat, it looks like you're short on mira?\x01",
            "Then, you can't buy it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BF")

    label("loc_278A")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285C")
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
    Jump("loc_2989")

    label("loc_285C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C2")
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
    Jump("loc_2989")

    label("loc_28C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2928")
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
    Jump("loc_2989")

    label("loc_2928")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2989")
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

    label("loc_2989")


    ChrTalk(
        0x8,
        (
            "Uh uh, I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_29BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29D8")

    label("loc_29CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29D8")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_21C7")

    label("loc_29EB")

    Return()

    # Function_6_21BD end

    def Function_7_29EC(): pass

    label("Function_7_29EC")


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
    Return()

    # Function_7_29EC end

    def Function_8_2A80(): pass

    label("Function_8_2A80")

    Call(0, 9)
    Return()

    # Function_8_2A80 end

    def Function_9_2A84(): pass

    label("Function_9_2A84")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AFB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2B58")

    label("loc_2B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3C")
    OP_AF(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B58")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B58")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_2B58")

    Jump("loc_2A91")

    label("loc_2B5D")

    TalkEnd(0x9)
    Return()

    # Function_9_2A84 end

    def Function_10_2B61(): pass

    label("Function_10_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC1")

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
            "#00004FYeah, we got an emergency\x01",
            "investigation request.\x02\x03",
            "#00000FCan we shop here now?\x02",
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
    Jump("loc_2D2B")

    label("loc_2CC1")


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

    label("loc_2D2B")

    Return()

    # Function_10_2B61 end

    def Function_11_2D2C(): pass

    label("Function_11_2D2C")


    ChrTalk(
        0x9,
        (
            "Okay. What do you\x01",
            "want to ask about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BBA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E45")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_2E45")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2E79"),
        (1, "loc_3058"),
        (2, "loc_31B8"),
        (3, "loc_3311"),
        (4, "loc_349F"),
        (5, "loc_370D"),
        (6, "loc_38F8"),
        (SWITCH_DEFAULT, "loc_3BA6"),
    )


    label("loc_2E79")


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
    Jump("loc_3BB5")

    label("loc_3058")


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
    Jump("loc_3BB5")

    label("loc_31B8")


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
    Jump("loc_3BB5")

    label("loc_3311")


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
    Jump("loc_3BB5")

    label("loc_349F")


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
    Jump("loc_3BB5")

    label("loc_370D")


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
    Jump("loc_3BB5")

    label("loc_38F8")


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
    Jump("loc_3BB5")

    label("loc_3BA6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BB5")

    label("loc_3BB5")

    Jump("loc_2D60")

    label("loc_3BBA")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_2D2C end

    def Function_12_3BC8(): pass

    label("Function_12_3BC8")

    TalkBegin(0xFE)

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
    TalkEnd(0xFE)
    Return()

    # Function_12_3BC8 end

    def Function_13_3C50(): pass

    label("Function_13_3C50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC7")

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
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D59")

    label("loc_3CC7")


    ChrTalk(
        0xFE,
        (
            "The latest orbal ranges\x01",
            "don't just heat. They have a\x01",
            "range of cooking functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, the world is getting\x01",
            "more convenient, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D59")

    TalkEnd(0xFE)
    Return()

    # Function_13_3C50 end

    def Function_14_3D5D(): pass

    label("Function_14_3D5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E32")

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
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E90")

    label("loc_3E32")


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

    label("loc_3E90")

    TalkEnd(0xFE)
    Return()

    # Function_14_3D5D end

    def Function_15_3E94(): pass

    label("Function_15_3E94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F17")

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
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F69")

    label("loc_3F17")


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

    label("loc_3F69")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E94 end

    SaveToFile()

Try(main)
