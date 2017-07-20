from ScenarioHelper import *

def main():
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
        "Chaco",                 # 1
        "Wendy",             # 2
        "Fernando",           # 3
        "Midget",               # 4
        "Basilio",               # 5
        "tourist",                 # 6
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
        "Function_5_564",          # 05, 5
        "Function_6_21D5",         # 06, 6
        "Function_7_29E6",         # 07, 7
        "Function_8_2A66",         # 08, 8
        "Function_9_2A6A",         # 09, 9
        "Function_10_2B46",        # 0A, 10
        "Function_11_2CE0",        # 0B, 11
        "Function_12_39FE",        # 0C, 12
        "Function_13_3A76",        # 0D, 13
        "Function_14_3B71",        # 0E, 14
        "Function_15_3CC8",        # 0F, 15
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_560")
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CC")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55B")

    label("loc_4CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F0")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55B")

    label("loc_4F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55B")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_53F")
    OP_AF(0xC0)
    Jump("loc_551")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_54F")
    OP_AF(0xBF)
    Jump("loc_551")

    label("loc_54F")

    OP_AF(0xBE)

    label("loc_551")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55B")

    Jump("loc_405")

    label("loc_560")

    TalkEnd(0x8)
    Return()

    # Function_4_3F8 end

    def Function_5_564(): pass

    label("Function_5_564")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D4")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    MenuCmd(1, 0, "Wearing CPD (Lloyd)")
    Jump("loc_6AC")

    label("loc_68A")

    MenuCmd(1, 0, "Exchange CPD (Lloyd)")

    label("loc_6AC")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6EE")
    MenuCmd(1, 0, "Blue Sheriff on board")
    Jump("loc_740")

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_71E")
    MenuCmd(1, 0, "Blue Sherif replace")
    Jump("loc_740")

    label("loc_71E")

    MenuCmd(1, 0, "Blue Sheriff 1000 Mira")

    label("loc_740")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_778")
    MenuCmd(1, 0, "Howling wolf installed")
    Jump("loc_7CA")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_7A8")
    MenuCmd(1, 0, "Change howling wolf")
    Jump("loc_7CA")

    label("loc_7A8")

    MenuCmd(1, 0, "Howling Wolf 1000 Mira")

    label("loc_7CA")

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
    Jump("loc_879")

    label("loc_85B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_879")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BD")
    MenuCmd(1, 0, "Wearing CPD (Ellie)")
    Jump("loc_8DF")

    label("loc_8BD")

    MenuCmd(1, 0, "Exchange CPD (Eiry)")

    label("loc_8DF")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_921")
    MenuCmd(1, 0, "Wearing piece green")
    Jump("loc_973")

    label("loc_921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_951")
    MenuCmd(1, 0, "Piece green exchange")
    Jump("loc_973")

    label("loc_951")

    MenuCmd(1, 0, "Peace Green 1000 Mira")

    label("loc_973")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_9AB")
    MenuCmd(1, 0, "Spring bird installed")
    Jump("loc_9FD")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_9DB")
    MenuCmd(1, 0, "Replace spring bird")
    Jump("loc_9FD")

    label("loc_9DB")

    MenuCmd(1, 0, "Spring Bird 1000 Mira")

    label("loc_9FD")

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
    Jump("loc_A8E")

    label("loc_A70")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD2")
    MenuCmd(1, 0, "Wearing CPD (Tio)")
    Jump("loc_AF4")

    label("loc_AD2")

    MenuCmd(1, 0, "Exchange CPD (Tio)")

    label("loc_AF4")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_B38")
    MenuCmd(1, 0, "Black Cat replaced")
    Jump("loc_B8A")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_B68")
    MenuCmd(1, 0, "Exchange black cat")
    Jump("loc_B8A")

    label("loc_B68")

    MenuCmd(1, 0, "Black Cat 1000 Mira")

    label("loc_B8A")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_BC2")
    MenuCmd(1, 0, "Shadow circle installed")
    Jump("loc_C14")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_BF2")
    MenuCmd(1, 0, "Shadow circle exchange")
    Jump("loc_C14")

    label("loc_BF2")

    MenuCmd(1, 0, "Shadow Circle 1000 Mira")

    label("loc_C14")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C87")

    label("loc_C69")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCB")
    MenuCmd(1, 0, "Wearing CPD (Randy)")
    Jump("loc_CED")

    label("loc_CCB")

    MenuCmd(1, 0, "Exchange CPD (Randy)")

    label("loc_CED")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_D2F")
    MenuCmd(1, 0, "Danger orange installed")
    Jump("loc_D81")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_D5F")
    MenuCmd(1, 0, "Exchange Danger Orange")
    Jump("loc_D81")

    label("loc_D5F")

    MenuCmd(1, 0, "Danger Orange 1000 Mira")

    label("loc_D81")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_DB9")
    MenuCmd(1, 0, "Midnight kiss on board")
    Jump("loc_E0B")

    label("loc_DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_DE9")
    MenuCmd(1, 0, "Midnight kiss to exchange")
    Jump("loc_E0B")

    label("loc_DE9")

    MenuCmd(1, 0, "Midnight kiss 1000 Mira")

    label("loc_E0B")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E60")

    label("loc_E42")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9F")
    MenuCmd(1, 0, "Wearing CGF (Noel)")
    Jump("loc_EC1")

    label("loc_E9F")

    MenuCmd(1, 0, "Exchange CGF (Noel)")

    label("loc_EC1")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_EF9")
    MenuCmd(1, 0, "Liberty Road installed")
    Jump("loc_F4B")

    label("loc_EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_F29")
    MenuCmd(1, 0, "Exchange Liberty Road")
    Jump("loc_F4B")

    label("loc_F29")

    MenuCmd(1, 0, "Liberty Road 1000 Mira")

    label("loc_F4B")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F82")

    label("loc_F6E")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_107C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC1")
    MenuCmd(1, 0, "Wearing white creed")
    Jump("loc_FE3")

    label("loc_FC1")

    MenuCmd(1, 0, "Exchange white creed")

    label("loc_FE3")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_101B")
    MenuCmd(1, 0, "Crest face is being worn")
    Jump("loc_106D")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_104B")
    MenuCmd(1, 0, "Crest face replacement")
    Jump("loc_106D")

    label("loc_104B")

    MenuCmd(1, 0, "Crest Face 1000 Mira")

    label("loc_106D")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1090")

    label("loc_107C")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1090")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C3")
    Sleep(1)
    Return()

    label("loc_10C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1101")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_149E")

    label("loc_1101")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_149E")

    label("loc_113F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_149E")

    label("loc_117D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_149E")

    label("loc_11BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_149E")

    label("loc_11F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1237")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_149E")

    label("loc_1237")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1275")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_149E")

    label("loc_1275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B3")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_149E")

    label("loc_12B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_149E")

    label("loc_12F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_149E")

    label("loc_132F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_149E")

    label("loc_136D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AB")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_149E")

    label("loc_13AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_149E")

    label("loc_13E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1427")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_149E")

    label("loc_1427")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_149E")

    label("loc_1465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149E")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_149E")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_156D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Lloyd.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_156D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_160E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Ellie only.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_160E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16AF")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Tio.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_16AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1752")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Randy.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_1752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17EB")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for Noel.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_17EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_187D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is only for wadi.\x01",
            "When exchanged, it will be displayed in [ORBMENT] of the camp menu\x01",
            "The cover of the tactical auction changes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187D")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B7")
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193E")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_193E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1957")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1970")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1970")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198F")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_198F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A8")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_19A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19C1")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_19C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E0")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_19E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F9")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_19F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A12")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A31")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A4A")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A63")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A7D")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A96")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1A96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AB0")
    SetScenarioFlags(0x0, 6)
    Jump("loc_1AC4")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC4")
    SetScenarioFlags(0x0, 6)

    label("loc_1AC4")

    ClearScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ADC")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1ADC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF5")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1AF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0E")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B23")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3C")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B55")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6A")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B83")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9C")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB1")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BCA")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE3")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1BE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF8")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C11")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1C11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C26")
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C3A")

    label("loc_1C26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C3A")
    SetScenarioFlags(0x0, 7)

    label("loc_1C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C87")

    ChrTalk(
        0x8,
        (
            "That ~ is already wearing it?\x01",
            "Please choose another one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CE8")

    ChrTalk(
        0x8,
        (
            "It seems that Mira is not enough?\x01",
            "Then we can not exchange it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1CE8")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DFD")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Lloyd's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC0")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_1DF8")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDA")
    SetScenarioFlags(0x2C, 0)

    label("loc_1DDA")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_1DF8")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF2")
    SetScenarioFlags(0x2C, 1)

    label("loc_1DF2")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_1DF8")

    Jump("loc_20F0")

    label("loc_1DFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EAD")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Elie 's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5E")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_1EA8")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E81")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E81")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_1EA8")

    label("loc_1E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA2")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EA2")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_1EA8")

    Jump("loc_20F0")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F5D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged Tio's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0E")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_1F58")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F31")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F31")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_1F58")

    label("loc_1F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F52")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F52")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_1F58")

    Jump("loc_20F0")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200F")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I replaced Randy 's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC0")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_200A")

    label("loc_1FC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE3")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FE3")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_200A")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2004")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2004")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_200A")

    Jump("loc_20F0")

    label("loc_200F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2083")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged noel's enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2065")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_207E")

    label("loc_2065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207B")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_207B")

    SetScenarioFlags(0x2F, 0)

    label("loc_207E")

    Jump("loc_20F0")

    label("loc_2083")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20F0")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I exchanged wadi's Enigma cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D7")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_20F0")

    label("loc_20D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20ED")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_20ED")

    SetScenarioFlags(0x2E, 4)

    label("loc_20F0")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2167")
    OP_E0(0x16, 0x0)

    label("loc_2167")


    ChrTalk(
        0x8,
        (
            "Hehe, use of\x01",
            "We look forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A8")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_21A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21C1")

    label("loc_21B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21C1")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_56E")

    label("loc_21D4")

    Return()

    # Function_5_564 end

    def Function_6_21D5(): pass

    label("Function_6_21D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E5")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('白金', 0x4)"), scpexpr(EXPR_END)), "loc_2221")
    MenuCmd(1, 0, "Platinum purchased")
    MenuCmd(3, 0, 0x0)
    Jump("loc_223D")

    label("loc_2221")

    MenuCmd(1, 0, "Platinum 1000 Mira")

    label("loc_223D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('幻象', 0x4)"), scpexpr(EXPR_END)), "loc_226D")
    MenuCmd(1, 0, "Mirage purchased")
    MenuCmd(3, 0, 0x1)
    Jump("loc_2289")

    label("loc_226D")

    MenuCmd(1, 0, "Mirage 5000 Mira")

    label("loc_2289")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_232F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('神佑', 0x4)"), scpexpr(EXPR_END)), "loc_22C7")
    MenuCmd(1, 0, "Aegis purchased")
    MenuCmd(3, 0, 0x2)
    Jump("loc_22E3")

    label("loc_22C7")

    MenuCmd(1, 0, "Aegis 20000 Mira")

    label("loc_22E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('王权', 0x4)"), scpexpr(EXPR_END)), "loc_2313")
    MenuCmd(1, 0, "Buyer purchased")
    MenuCmd(3, 0, 0x3)
    Jump("loc_232F")

    label("loc_2313")

    MenuCmd(1, 0, "Scepter 50000 Mira")

    label("loc_232F")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_236E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_236E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_238B")
    Sleep(1)
    Return()

    label("loc_238B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CB")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_2486")

    label("loc_23CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_2486")

    label("loc_240B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_2486")

    label("loc_244B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2486")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_2486")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2517")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Master quartz with sky attribute.\x01",
            "* HP / ADF reinforced type · HP recovery when stabbing the enemy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263D")

    label("loc_2517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a phantom attribute master quartz.\x01",
            "※ EP / ATS reinforced type · Episodic recovery by stabbing the enemy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263D")

    label("loc_257A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E2")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is master quartz of earth attribute.\x01",
            "※ DEF / ADF reinforced type · \"complete defense\" effect under specified conditions\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263D")

    label("loc_25E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is Master Quartz with water attribute.\x01",
            "※ STR / ATS reinforced type · Sepis obtained for each attack\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263D")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2779")

    ChrTalk(
        0x8,
        (
            "It seems that Mira is not enough?\x01",
            "Then you can not purchase.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2779")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2852")
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
    Jump("loc_298B")

    label("loc_2852")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BC")
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
    Jump("loc_298B")

    label("loc_28BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2926")
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
    Jump("loc_298B")

    label("loc_2926")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298B")
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

    label("loc_298B")


    ChrTalk(
        0x8,
        (
            "Hehe, use of\x01",
            "We look forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_29B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29D2")

    label("loc_29C8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29D2")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_21DF")

    label("loc_29E5")

    Return()

    # Function_6_21D5 end

    def Function_7_29E6(): pass

    label("Function_7_29E6")


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
    Return()

    # Function_7_29E6 end

    def Function_8_2A66(): pass

    label("Function_8_2A66")

    Call(0, 9)
    Return()

    # Function_8_2A66 end

    def Function_9_2A6A(): pass

    label("Function_9_2A6A")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B42")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2AE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B01")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2B3D")

    label("loc_2B01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B21")
    OP_AF(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B3D")

    label("loc_2B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_2B3D")

    Jump("loc_2A77")

    label("loc_2B42")

    TalkEnd(0x9)
    Return()

    # Function_9_2A6A end

    def Function_10_2B46(): pass

    label("Function_10_2B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C82")

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
            "#00004FOh, hey\x01",
            "An urgent investigation has entered.\x02\x03",
            "#00000FThe shop is still okay?\x02",
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
    Jump("loc_2CDF")

    label("loc_2C82")


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

    label("loc_2CDF")

    Return()

    # Function_10_2B46 end

    def Function_11_2CE0(): pass

    label("Function_11_2CE0")


    ChrTalk(
        0x9,
        (
            "Okay.\x01",
            "What do you want to ask?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39F0")
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
            "About Master Quartz\x01",        # 6
            "quit\x01",                          # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E03")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_2E03")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2E37"),
        (1, "loc_2FFC"),
        (2, "loc_312B"),
        (3, "loc_3259"),
        (4, "loc_33CC"),
        (5, "loc_35C8"),
        (6, "loc_3796"),
        (SWITCH_DEFAULT, "loc_39DC"),
    )


    label("loc_2E37")


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
    Jump("loc_39EB")

    label("loc_2FFC")


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
    Jump("loc_39EB")

    label("loc_312B")


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
    Jump("loc_39EB")

    label("loc_3259")


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
    Jump("loc_39EB")

    label("loc_33CC")


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
    Jump("loc_39EB")

    label("loc_35C8")


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
    Jump("loc_39EB")

    label("loc_3796")


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
    Jump("loc_39EB")

    label("loc_39DC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39EB")

    label("loc_39EB")

    Jump("loc_2D11")

    label("loc_39F0")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_2CE0 end

    def Function_12_39FE(): pass

    label("Function_12_39FE")

    TalkBegin(0xFE)

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
    TalkEnd(0xFE)
    Return()

    # Function_12_39FE end

    def Function_13_3A76(): pass

    label("Function_13_3A76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEC")

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
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B6D")

    label("loc_3AEC")


    ChrTalk(
        0xFE,
        (
            "For the latest type of power range,\x01",
            "Not just warming up\x01",
            "You can use it for various cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, handy\x01",
            "It is something that has become world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3A76 end

    def Function_14_3B71(): pass

    label("Function_14_3B71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5B")

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
            "I'd like to return with Chaco … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To that extent,\x01",
            "Chako will hate you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, what is it ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CC4")

    label("loc_3C5B")


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

    label("loc_3CC4")

    TalkEnd(0xFE)
    Return()

    # Function_14_3B71 end

    def Function_15_3CC8(): pass

    label("Function_15_3CC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D45")

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
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D9B")

    label("loc_3D45")


    ChrTalk(
        0xFE,
        (
            "Sprinkle courage\x01",
            "Voice to Chaco-chan ……\x02",
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

    label("loc_3D9B")

    TalkEnd(0xFE)
    Return()

    # Function_15_3CC8 end

    SaveToFile()

Try(main)
