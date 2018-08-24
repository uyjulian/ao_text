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
        "Function_6_2183",         # 06, 6
        "Function_7_299C",         # 07, 7
        "Function_8_2A30",         # 08, 8
        "Function_9_2A34",         # 09, 9
        "Function_10_2B11",        # 0A, 10
        "Function_11_2CD2",        # 0B, 11
        "Function_12_3B80",        # 0C, 12
        "Function_13_3C06",        # 0D, 13
        "Function_14_3D13",        # 0E, 14
        "Function_15_3E4A",        # 0F, 15
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
            "Buy/Change Covers\x01",          # 1
            "Buy Master Quartz\x01",          # 2
            "Buy Orbal Car Options\x01",      # 3
            "Cancel\x01",                     # 4
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2182")
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

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_108B")
    Sleep(1)
    Return()

    label("loc_108B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1466")

    label("loc_10C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1107")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_1466")

    label("loc_1107")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1145")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_1466")

    label("loc_1145")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1466")

    label("loc_1183")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_1466")

    label("loc_11C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_1466")

    label("loc_11FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1466")

    label("loc_123D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_1466")

    label("loc_127B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_1466")

    label("loc_12B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_1466")

    label("loc_12F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1335")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_1466")

    label("loc_1335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_1466")

    label("loc_1373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_1466")

    label("loc_13B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_1466")

    label("loc_13EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_1466")

    label("loc_142D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1466")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_1466")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1533")

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
    Jump("loc_1834")

    label("loc_1533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D1")

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
    Jump("loc_1834")

    label("loc_15D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_166E")

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
    Jump("loc_1834")

    label("loc_166E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_170D")

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
    Jump("loc_1834")

    label("loc_170D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A3")

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
    Jump("loc_1834")

    label("loc_17A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1834")

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

    label("loc_1834")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2165")
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F4")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_18F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_190D")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_190D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1926")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1926")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1945")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1945")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195E")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_195E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1977")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1996")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19AF")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_19AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19C8")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_19C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E7")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_19E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A00")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A19")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1A19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A33")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1A33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A4C")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A66")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1A7A")

    label("loc_1A66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A7A")
    SetScenarioFlags(0x0, 6)

    label("loc_1A7A")

    ClearScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A92")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AAB")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC4")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD9")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1AD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF2")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0B")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B20")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B39")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B52")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B67")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B80")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B99")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAE")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC7")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BDC")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BF0")

    label("loc_1BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF0")
    SetScenarioFlags(0x0, 7)

    label("loc_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C4A")

    ChrTalk(
        0x8,
        (
            "Whaaat, you already have\x01",
            "it equipped? Please\x01",
            "choose another one, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2156")

    label("loc_1C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA1")

    ChrTalk(
        0x8,
        (
            "Whaaat, you're short on\x01",
            "mira? You can't exchange\x01",
            "it then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2156")

    label("loc_1CA1")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DAE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D71")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_1DA9")

    label("loc_1D71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8B")
    SetScenarioFlags(0x2C, 0)

    label("loc_1D8B")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_1DA9")

    label("loc_1D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA3")
    SetScenarioFlags(0x2C, 1)

    label("loc_1DA3")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_1DA9")

    Jump("loc_2097")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E5C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0D")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_1E57")

    label("loc_1E0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E30")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E30")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_1E57")

    label("loc_1E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E51")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E51")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_1E57")

    Jump("loc_2097")

    label("loc_1E5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F09")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBA")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_1F04")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDD")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EDD")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_1F04")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFE")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EFE")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_1F04")

    Jump("loc_2097")

    label("loc_1F09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FB8")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F69")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_1FB3")

    label("loc_1F69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8C")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F8C")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_1FB3")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAD")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FAD")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_1FB3")

    Jump("loc_2097")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_202A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200C")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_2025")

    label("loc_200C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2022")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2022")

    SetScenarioFlags(0x2F, 0)

    label("loc_2025")

    Jump("loc_2097")

    label("loc_202A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2097")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy's ENIGMA cover was\x01",
            "changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207E")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_2097")

    label("loc_207E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2094")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2094")

    SetScenarioFlags(0x2E, 4)

    label("loc_2097")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210E")
    OP_E0(0x16, 0x0)

    label("loc_210E")


    ChrTalk(
        0x8,
        (
            "Haha. I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2156")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2156")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_216F")

    label("loc_2165")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_216F")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_54F")

    label("loc_2182")

    Return()

    # Function_5_545 end

    def Function_6_2183(): pass

    label("Function_6_2183")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_218D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299B")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x4)"), scpexpr(EXPR_END)), "loc_21D0")
    MenuCmd(1, 0, "Platinum        Purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_21ED")

    label("loc_21D0")

    MenuCmd(1, 0, "Platinum        1000 mira")

    label("loc_21ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x4)"), scpexpr(EXPR_END)), "loc_221E")
    MenuCmd(1, 0, "Mirage          Purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_223B")

    label("loc_221E")

    MenuCmd(1, 0, "Mirage          5000 mira")

    label("loc_223B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22E5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x4)"), scpexpr(EXPR_END)), "loc_227A")
    MenuCmd(1, 0, "Aegis           Purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_2297")

    label("loc_227A")

    MenuCmd(1, 0, "Aegis          20000 mira")

    label("loc_2297")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x4)"), scpexpr(EXPR_END)), "loc_22C8")
    MenuCmd(1, 0, "Scepter         Purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_22E5")

    label("loc_22C8")

    MenuCmd(1, 0, "Scepter        50000 mira")

    label("loc_22E5")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2324")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2324")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2324")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2341")
    Sleep(1)
    Return()

    label("loc_2341")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2381")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_243C")

    label("loc_2381")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_243C")

    label("loc_23C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2401")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_243C")

    label("loc_2401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243C")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_243C")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D8")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Space element Master Quartz.\x01",
            "※Raises HP/ADF, recov\x07\x00",
            "ers HP\x01",
            "on defeating an enemy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_24D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2547")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mirage element Master Quartz.\x01",
            "※Raises EP/ATS, reco\x07\x00",
            "vers EP\x01",
            "on defeating an enemy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_2547")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Earth element Master Quartz.\x01",
            "※Raises DEF/ADF, gain MAX\x07\x00\x01",
            "GUARD in certain conditions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_25B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water element Master Quartz.\x01",
            "※Raises STR/ATS\x07\x00",
            ", gain Sepith\x01",
            "when attacking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261C")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_297E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_273F")

    ChrTalk(
        0x8,
        (
            "Whaaat, you're short of\x01",
            "mira? You can't buy it,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296F")

    label("loc_273F")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280D")
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
    Jump("loc_293A")

    label("loc_280D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2873")
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
    Jump("loc_293A")

    label("loc_2873")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D9")
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
    Jump("loc_293A")

    label("loc_28D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293A")
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

    label("loc_293A")


    ChrTalk(
        0x8,
        (
            "Haha. I look forward to\x01",
            "serving you all again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_296F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2988")

    label("loc_297E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2988")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_218D")

    label("loc_299B")

    Return()

    # Function_6_2183 end

    def Function_7_299C(): pass

    label("Function_7_299C")


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

    # Function_7_299C end

    def Function_8_2A30(): pass

    label("Function_8_2A30")

    Call(0, 9)
    Return()

    # Function_8_2A30 end

    def Function_9_2A34(): pass

    label("Function_9_2A34")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AAB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2AAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ACC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2B08")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEC")
    OP_AF(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B08")

    label("loc_2AEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_2B08")

    Jump("loc_2A41")

    label("loc_2B0D")

    TalkEnd(0x9)
    Return()

    # Function_9_2A34 end

    def Function_10_2B11(): pass

    label("Function_10_2B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C67")

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
            "#00004FYeah, we got an\x01",
            "emergency investigation\x01",
            "request.\x02\x03",
            "#00000FCan we shop here now?\x02",
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
    Jump("loc_2CD1")

    label("loc_2C67")


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

    label("loc_2CD1")

    Return()

    # Function_10_2B11 end

    def Function_11_2CD2(): pass

    label("Function_11_2CD2")


    ChrTalk(
        0x9,
        (
            "Okay. What do you want\x01",
            "to ask about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B72")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DED")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_2DED")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2E21"),
        (1, "loc_3006"),
        (2, "loc_316A"),
        (3, "loc_32C3"),
        (4, "loc_3454"),
        (5, "loc_36C0"),
        (6, "loc_38AF"),
        (SWITCH_DEFAULT, "loc_3B5E"),
    )


    label("loc_2E21")


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
    Jump("loc_3B6D")

    label("loc_3006")


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
    Jump("loc_3B6D")

    label("loc_316A")


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
    Jump("loc_3B6D")

    label("loc_32C3")


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
    Jump("loc_3B6D")

    label("loc_3454")


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
    Jump("loc_3B6D")

    label("loc_36C0")


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
    Jump("loc_3B6D")

    label("loc_38AF")


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
    Jump("loc_3B6D")

    label("loc_3B5E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B6D")

    label("loc_3B6D")

    Jump("loc_2D06")

    label("loc_3B72")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_2CD2 end

    def Function_12_3B80(): pass

    label("Function_12_3B80")

    TalkBegin(0xFE)

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
    TalkEnd(0xFE)
    Return()

    # Function_12_3B80 end

    def Function_13_3C06(): pass

    label("Function_13_3C06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7D")

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
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D0F")

    label("loc_3C7D")


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
            "Uhuhu, the world is\x01",
            "getting more convenient,\x01",
            "isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0F")

    TalkEnd(0xFE)
    Return()

    # Function_13_3C06 end

    def Function_14_3D13(): pass

    label("Function_14_3D13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE8")

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
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E46")

    label("loc_3DE8")


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

    label("loc_3E46")

    TalkEnd(0xFE)
    Return()

    # Function_14_3D13 end

    def Function_15_3E4A(): pass

    label("Function_15_3E4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ECD")

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
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F1F")

    label("loc_3ECD")


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

    label("loc_3F1F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E4A end

    SaveToFile()

Try(main)
