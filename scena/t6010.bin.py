from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t6010.bin",                # FileName
        "t6010",                    # MapName
        "t6010",                    # Location
        0x00A4,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 164, 0, 1, 0, 2],
    )

    BuildStringList((
        "t6010",                  # 0
        "Manager Juan",           # 1
        "Trainee",                # 2
        "Trainee",                # 3
        "Instructor",             # 4
        "Receptionist Rebecca",   # 5
        "Section Chief Joe Ridge",# 6
        "Policeman",              # 7
        "Chief Sergei",           # 8
    ))

    AddCharChip((
        "chr/ch28000.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch30600.itc",                   # 02
        "chr/ch30100.itc",                   # 03
        "chr/ch30400.itc",                   # 04
        "chr/ch30100.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(15500,   0,       12250,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(67300,   0,       5900,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(18000,   0,       12250,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3200,    0,       16090,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(67300,   0,       20149,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(66099,   0,       20149,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       14400,   1000,    0,       1500,    15400,   0x007E, 0,  3,  0x0000)
    DeclActor(2690,    0,       14400,   1000,    3200,    1500,    16090,   0x007E, 0,  12, 0x0000)
    DeclActor(20020,   0,       9890,    1000,    20020,   1500,    9890,    0x007C, 0,  31, 0x0000)
    DeclActor(15360,   0,       12700,   1000,    15360,   1500,    12700,   0x007C, 0,  32, 0x0000)
    DeclActor(17920,   0,       12660,   1000,    17920,   1500,    12660,   0x007C, 0,  32, 0x0000)

    ChipFrameInfo(804, 0)                                        # 0

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_563",          # 02, 2
        "Function_3_5A9",          # 03, 3
        "Function_4_5AD",          # 04, 4
        "Function_5_18C2",         # 05, 5
        "Function_6_31BD",         # 06, 6
        "Function_7_3390",         # 07, 7
        "Function_8_3559",         # 08, 8
        "Function_9_3C9F",         # 09, 9
        "Function_10_4265",        # 0A, 10
        "Function_11_45CE",        # 0B, 11
        "Function_12_4B38",        # 0C, 12
        "Function_13_4B3C",        # 0D, 13
        "Function_14_54EA",        # 0E, 14
        "Function_15_556B",        # 0F, 15
        "Function_16_557A",        # 10, 16
        "Function_17_775B",        # 11, 17
        "Function_18_7861",        # 12, 18
        "Function_19_86D3",        # 13, 19
        "Function_20_956A",        # 14, 20
        "Function_21_A016",        # 15, 21
        "Function_22_A0FE",        # 16, 22
        "Function_23_A1F3",        # 17, 23
        "Function_24_AF74",        # 18, 24
        "Function_25_B151",        # 19, 25
        "Function_26_B397",        # 1A, 26
        "Function_27_CF73",        # 1B, 27
        "Function_28_CFA3",        # 1C, 28
        "Function_29_CFD3",        # 1D, 29
        "Function_30_DAE7",        # 1E, 30
        "Function_31_DB92",        # 1F, 31
        "Function_32_DBF6",        # 20, 32
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_370"),
        (2, "loc_37C"),
        (3, "loc_388"),
        (4, "loc_394"),
        (5, "loc_3A0"),
        (6, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_364")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_370")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_37C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_388")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_394")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3DB")

    Return()

    # Function_0_324 end

    def Function_1_3DC(): pass

    label("Function_1_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17870, 0, 12360, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16670, 0, 12360, 90)
    SetChrFlags(0xA, 0x10)
    Jump("loc_551")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47D")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 67300, 0, 20150, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66100, 0, 20150, 90)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_551")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_551")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_4A3")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_551")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 19000, 0, 9000, 90)
    Jump("loc_551")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 18000, 0, 12250, 0)
    Jump("loc_551")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 66700, 0, 19750, 180)
    Jump("loc_551")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_522")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_551")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_535")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_551")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_548")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_551")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_551")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_562")
    Event(0, 26)

    label("loc_562")

    Return()

    # Function_1_3DC end

    def Function_2_563(): pass

    label("Function_2_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C")
    SetMapObjFrame(0xFF, "t6010:Layer11", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_58C")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2")
    OP_66(0x1, 0x1)

    label("loc_5A2")

    ClearMapObjFlags(0x7, 0x10)
    Return()

    # Function_2_563 end

    def Function_3_5A9(): pass

    label("Function_3_5A9")

    Call(0, 4)
    Return()

    # Function_3_5A9 end

    def Function_4_5AD(): pass

    label("Function_4_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4")
    Call(0, 29)
    Return()

    label("loc_5C4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Give Peculiar Dishes\x01",      # 1
            "Quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63F")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Jump("loc_18A7")

    label("loc_660")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_679")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D6")
    MenuCmd(1, 1, "Bitter Noodles "Severed"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_6CC")
    Call(0, 7)

    label("loc_6CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_717")
    MenuCmd(1, 1, "Gehenna Mapo "Hell King"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_70D")
    Call(0, 7)

    label("loc_70D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_752")
    MenuCmd(1, 1, "Mottled Burnt Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_748")
    Call(0, 7)

    label("loc_748")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78E")
    MenuCmd(1, 1, "Diehard Meat "Rock"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_784")
    Call(0, 7)

    label("loc_784")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CA")
    MenuCmd(1, 1, "Chaos Stew "Impure"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_7C0")
    Call(0, 7)

    label("loc_7C0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80B")
    MenuCmd(1, 1, "Manly Cooking "Mountain"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_801")
    Call(0, 7)

    label("loc_801")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_849")
    MenuCmd(1, 1, "Manly Cooking "River"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_83F")
    Call(0, 7)

    label("loc_83F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87C")
    MenuCmd(1, 1, "Fish Arrow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_872")
    Call(0, 7)

    label("loc_872")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B9")
    MenuCmd(1, 1, "Very Spicy Bomb Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_8AF")
    Call(0, 7)

    label("loc_8AF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EE")
    MenuCmd(1, 1, "Needle Pasta")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_8E4")
    Call(0, 7)

    label("loc_8E4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_924")
    MenuCmd(1, 1, "Bitter Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_91A")
    Call(0, 7)

    label("loc_91A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_961")
    MenuCmd(1, 1, "Quattro Tomato Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_957")
    Call(0, 7)

    label("loc_957")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99D")
    MenuCmd(1, 1, "Protection Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_993")
    Call(0, 7)

    label("loc_993")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DA")
    MenuCmd(1, 1, "Lunch Box "Surprise"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_9D0")
    Call(0, 7)

    label("loc_9D0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0E")
    MenuCmd(1, 1, "Magica Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_A04")
    Call(0, 7)

    label("loc_A04")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A43")
    MenuCmd(1, 1, "Enigma Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_A39")
    Call(0, 7)

    label("loc_A39")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7D")
    MenuCmd(1, 1, "Reflect Chocolate")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_A73")
    Call(0, 7)

    label("loc_A73")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB6")
    MenuCmd(1, 1, "Jiggling Pudding")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_AAC")
    Call(0, 7)

    label("loc_AAC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEB")
    MenuCmd(1, 1, "Recovery Ice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_AE1")
    Call(0, 7)

    label("loc_AE1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B23")
    MenuCmd(1, 1, "Secrecy Popcorn")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_B19")
    Call(0, 7)

    label("loc_B19")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B64")
    MenuCmd(1, 1, "Medicine "Sasa Veitchii"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_B5A")
    Call(0, 7)

    label("loc_B5A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B9A")
    MenuCmd(1, 1, "Purple Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_B90")
    Call(0, 7)

    label("loc_B90")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCF")
    MenuCmd(1, 1, "Brown Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_BC5")
    Call(0, 7)

    label("loc_BC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C03")
    MenuCmd(1, 1, "Pink Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_BF9")
    Call(0, 7)

    label("loc_BF9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C03")

    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C94")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you. If you have something\x01",
            "nice again, please hand it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_C94")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x192, 1)
    SetScenarioFlags(0x20C, 0)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_D05")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D6B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x195, 1)
    SetScenarioFlags(0x20C, 1)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x195),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_D61")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x198, 1)
    SetScenarioFlags(0x20C, 2)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x198),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_DBD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E19")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19B, 1)
    SetScenarioFlags(0x20C, 3)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x19B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_E19")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E75")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19E, 1)
    SetScenarioFlags(0x20C, 4)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x19E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_E75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EDB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A1, 1)
    SetScenarioFlags(0x20C, 5)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_ED1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F37")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A4, 1)
    SetScenarioFlags(0x20C, 6)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_F2D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F89")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A7, 1)
    SetScenarioFlags(0x20C, 7)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_F89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FEF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AA, 1)
    SetScenarioFlags(0x20D, 0)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_FE5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1041")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AD, 1)
    SetScenarioFlags(0x20D, 1)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1041")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B0, 1)
    SetScenarioFlags(0x20D, 2)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_109D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1103")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B3, 1)
    SetScenarioFlags(0x20D, 3)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_10F9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1155")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B6, 1)
    SetScenarioFlags(0x20D, 4)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1155")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_115F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11BB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B9, 1)
    SetScenarioFlags(0x20D, 5)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_11B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1217")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x20D, 6)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_120D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1273")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1269")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BF, 1)
    SetScenarioFlags(0x20D, 7)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1269")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C2, 1)
    SetScenarioFlags(0x20E, 0)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_12C5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_132B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1321")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C5, 1)
    SetScenarioFlags(0x20E, 1)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1321")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1387")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C8, 1)
    SetScenarioFlags(0x20E, 2)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_137D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13E3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CB, 1)
    SetScenarioFlags(0x20E, 3)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_13D9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_143F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1435")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CE, 1)
    SetScenarioFlags(0x20E, 4)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1435")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_143F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1491")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D1, 1)
    SetScenarioFlags(0x20E, 5)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1491")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14ED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D4, 1)
    SetScenarioFlags(0x20E, 6)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_14ED")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1553")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1549")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D7, 1)
    SetScenarioFlags(0x20E, 7)

    AnonymousTalk(
        0xFF,
        (
            "You gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1549")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1553")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188E")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oh, it seems you\x01",
            "brought me a lot of\x01",
            ""peculiar dishes".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the present, these should do good\x01",
            "for training the identification unit too.\x01",
            "...Thank you, you have really helped me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, please don't mind it.\x01",
            "It wasn't a big deal, and...\x02\x03",
            "Well, it seems I was able to\x01",
            "be useful to my alma mater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're commendable, Lloyd...\x01",
            "Yes, that aspect of you hasn't\x01",
            "changed since your student times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right, if you want, \x01",
            "would you like to accept this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a Quartz for the ENIGMA II\x01",
            "we have recently started to use\x01",
            "and they provided us an extra one.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xBD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xBD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThank you very much,\x01",
            "Manager Juan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No no, thank you. I'll be counting\x01",
            "on you if something comes up again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 1)
    TalkEnd(0x8)
    Return()

    label("loc_188E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1898")

    Jump("loc_679")

    label("loc_189D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18A7")

    Jump("loc_5DF")

    label("loc_18AC")

    Jump("loc_18BE")

    label("loc_18B1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_18BE")

    TalkEnd(0x8)
    Return()

    # Function_4_5AD end

    def Function_5_18C2(): pass

    label("Function_5_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C1")

    ChrTalk(
        0x8,
        (
            "After receiving the information\x01",
            "about the President restraint,\x01",
            "the State Guard withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in order to quell the\x01",
            "disturbances in every place,\x01",
            "the State Guard must do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too must do \x01",
            "what we can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A43")

    label("loc_19C1")


    ChrTalk(
        0x8,
        (
            "The reinforcements that came from HQ are\x01",
            "currently coping with the disturbances nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too must do \x01",
            "what we can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    Jump("loc_31B9")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(
        0x8,
        (
            "...That raid incident was\x01",
            "too much gruesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was a small mercy that\x01",
            "the young officers of this\x01",
            "Police Academy were safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that it will still take time\x01",
            "for Crossbell to recover completely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BE7")

    label("loc_1B3D")


    ChrTalk(
        0x8,
        (
            "...In that raid incident\x01",
            "It was a small mercy that\x01",
            "the young officers were safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that it will still take time\x01",
            "for Crossbell to recover completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE7")

    Jump("loc_31B9")

    label("loc_1BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFC")

    ChrTalk(
        0x8,
        (
            "About the gate that was destroyed yesterday...\x01",
            "It seems that it will take some time\x01",
            "for a new one to be prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, it was inconceivable\x01",
            "to be destroyed like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can only count on the CGF\x01",
            "for a while for security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DAF")

    label("loc_1CFC")


    ChrTalk(
        0x8,
        (
            "About the gate that was destroyed yesterday...\x01",
            "It seems that it will take some time\x01",
            "for a new one to be prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can only count on the CGF\x01",
            "for a while for security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAF")

    Jump("loc_31B9")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_206B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2015")

    ChrTalk(
        0x8,
        "Oh, it's Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard a big noise in the\x01",
            "premises just before...\x01",
            "What was that, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...We confirmed that the front\x01",
            "gate was destroyed some time ago.\x01",
            "I think it was probably the sound from that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "W-What do you say!?\x01",
            "Thas special alloy made gate was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't tell it was a "Cryptid"...?\x01",
            "No one reported to me that\x01",
            "it could have that much power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWe too can't say\x01",
            "anything yet, but...\x02\x03",
            "We can't rule out the possibility\x01",
            "it will come here too.\x01",
            "...Please be very vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Y-Yeah...you too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 0)
    Jump("loc_2066")

    label("loc_2015")


    ChrTalk(
        0x8,
        (
            "We too will watch the\x01",
            "environs thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all...\x01",
            "Be very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2066")

    Jump("loc_31B9")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2115")

    ChrTalk(
        0x8,
        (
            "Today, it seems there's no sighting\x01",
            "intel about the Cryptid in the woodlands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that the Bracers too are \x01",
            "investigating a different place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225C")

    ChrTalk(
        0x8,
        (
            "A "Cryptid" has been\x01",
            "spotted in the Knox\x01",
            "Woodlands, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bracers called Ling and Eolia\x01",
            "undertook its extermination, but\x01",
            "in the end it seems they failed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That place is the CGF practice terrain,\x01",
            "so thinking about the future, it seems it\x01",
            "would be better to keep up with the lookouts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_231C")

    label("loc_225C")


    ChrTalk(
        0x8,
        (
            "A "Cryptid" has been\x01",
            "spotted in the Knox\x01",
            "Woodlands, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears it ran away somewhere...\x01",
            "Thinking about the future, it seems it\x01",
            "would be better to keep up with the lookouts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231C")

    Jump("loc_31B9")

    label("loc_2321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A9")

    ChrTalk(
        0x8,
        (
            "The Police Academy curriculum is\x01",
            "strictly done in a half a year period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It mainly focus on classroom lectures and\x01",
            "practical training, and after graduation, you\x01",
            "are assigned to many suitable duty posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So to speak, it's the place where it's taught to\x01",
            "the chick officers how to make their first flight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel especially proud\x01",
            "of serving here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2543")

    label("loc_24A9")


    ChrTalk(
        0x8,
        (
            "The place where it's taught to the chick \x01",
            "officers how to make their first flight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel especially proud of\x01",
            "serving at this Police Academy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2543")

    Jump("loc_31B9")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E5")

    ChrTalk(
        0x8,
        (
            "Douglas, who has become the CGF Vice Commander, \x01",
            "has been an instructor here for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was mainly in charge of practical training\x01",
            "and even showed up often on training grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "Really, he was a strict person.\x02\x03",
            "#00008FThose hellish scenes of falling out\x01",
            "after training one on one, and then again...\x02\x03",
            "#00006FEven remembering it now\x01",
            "I can't stop the shivers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that guy is the type to trust\x01",
            "at you unreasonable demands\x01",
            "while freshly smilin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, it's the reason he was\x01",
            "lately called "Douglas the Ogre".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHowever, being able to learn\x01",
            "fighting techniques from the\x01",
            "CGF hope makes me envious.\x02\x03",
            "#10104FIf possible, I would've liked to learn\x01",
            "from him too when in my rookie days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FW-Well, I'm grateful to him.\x01",
            "What he taught me has been useful\x01",
            "in actual fights many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In practice, thanks to him\x01",
            "we had many excellent\x01",
            "officers, Lloyd included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a Police Academy, he was a man of talent\x01",
            "we wouldn't have wanted to let go no matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, he's originally from the CGF\x01",
            "and since the request came from\x01",
            "Commander Sonya, it couldn't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 6)
    Jump("loc_2A9F")

    label("loc_29E5")


    ChrTalk(
        0x8,
        (
            "Even as a Police Academy, we wouldn't\x01",
            "have wanted to let Douglas go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, he's originally from the CGF\x01",
            "and since the request came from\x01",
            "Commander Sonya, it couldn't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9F")

    Jump("loc_31B9")

    label("loc_2AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCC")

    ChrTalk(
        0x8,
        "Oh, the SSS ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard about it from Sergei,\x01",
            "but it seems you're riding that\x01",
            "new orbal car model every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, yes, more or less.\x01",
            "It has been greatly useful to us\x01",
            "even in activities outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you must drive it by\x01",
            "respecting the traffic rules well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A traffic accident caused by a police officer...\x01",
            "Something like that wouldn't even be a laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, did you hear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI-I wouldn't cause\x01",
            "such an accident...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, it's not that\x01",
            "Noｱl is a speed\x01",
            "freak or anything, but...\x02\x03",
            "#00304FLovin' too much orbal\x01",
            "cars could make her\x01",
            "be shortsighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FY-You too, senior...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, we haven't got used\x01",
            "to it completely yet...\x01",
            "Let's keep that in mind, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 5)
    Jump("loc_2E89")

    label("loc_2DCC")


    ChrTalk(
        0x8,
        (
            "If you're driving a vehicle, you must\x01",
            "respect the traffic rules properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A traffic accident caused by a police officer...\x01",
            "Something like that wouldn't even be a laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E89")

    Jump("loc_31B9")

    label("loc_2E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314B")

    ChrTalk(
        0x8,
        "It appears you finished your short course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's finally down to practical skills, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, well, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FAt any rate, to think that\x01",
            "the Chief could do that\x01",
            "training is quite unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's because he held the post\x01",
            "of driving vehicles instructor\x01",
            "at the Police Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I have no doubt\x01",
            "it was easy to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh, now that I think about it, he\x01",
            "said something like that before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FUhhm, even Chief Sergei is\x01",
            "a person with many secrets.\x02\x03",
            "#10101FPersonally, I'm even curious about his\x01",
            "relationship with Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, after all he's a person\x01",
            "quite secretive about himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 5)
    Jump("loc_31B9")

    label("loc_314B")


    ChrTalk(
        0x8,
        (
            "By the way, isn't Sergei\x01",
            "waiting for you outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You should not make a superior wait.\x01",
            "Go, quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B9")

    Call(0, 8)
    Return()

    # Function_5_18C2 end

    def Function_6_31BD(): pass

    label("Function_6_31BD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_31DA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_31ED")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_3200")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_3213")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_3226")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_3239")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_324C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_324C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_325F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_325F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_3272")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_3285")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_3298")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_32AB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_32BE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_32D1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_32E4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_32F7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_330A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_330A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_331D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_331D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_3330")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_3343")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_3356")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_3369")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_337C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_337C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_338F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_338F")

    Return()

    # Function_6_31BD end

    def Function_7_3390(): pass

    label("Function_7_3390")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A3")
    MenuCmd(3, 1, 0x0)

    label("loc_33A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B6")
    MenuCmd(3, 1, 0x1)

    label("loc_33B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C9")
    MenuCmd(3, 1, 0x2)

    label("loc_33C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DC")
    MenuCmd(3, 1, 0x3)

    label("loc_33DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33EF")
    MenuCmd(3, 1, 0x4)

    label("loc_33EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3402")
    MenuCmd(3, 1, 0x5)

    label("loc_3402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3415")
    MenuCmd(3, 1, 0x6)

    label("loc_3415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3428")
    MenuCmd(3, 1, 0x7)

    label("loc_3428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343B")
    MenuCmd(3, 1, 0x8)

    label("loc_343B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344E")
    MenuCmd(3, 1, 0x9)

    label("loc_344E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3461")
    MenuCmd(3, 1, 0xA)

    label("loc_3461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3474")
    MenuCmd(3, 1, 0xB)

    label("loc_3474")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3487")
    MenuCmd(3, 1, 0xC)

    label("loc_3487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349A")
    MenuCmd(3, 1, 0xD)

    label("loc_349A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AD")
    MenuCmd(3, 1, 0xE)

    label("loc_34AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C0")
    MenuCmd(3, 1, 0xF)

    label("loc_34C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D3")
    MenuCmd(3, 1, 0x10)

    label("loc_34D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E6")
    MenuCmd(3, 1, 0x11)

    label("loc_34E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F9")
    MenuCmd(3, 1, 0x12)

    label("loc_34F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350C")
    MenuCmd(3, 1, 0x13)

    label("loc_350C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351F")
    MenuCmd(3, 1, 0x14)

    label("loc_351F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3532")
    MenuCmd(3, 1, 0x15)

    label("loc_3532")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3545")
    MenuCmd(3, 1, 0x16)

    label("loc_3545")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3558")
    MenuCmd(3, 1, 0x17)

    label("loc_3558")

    Return()

    # Function_7_3390 end

    def Function_8_3559(): pass

    label("Function_8_3559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9E")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "By the way... I know it's sudden,\x01",
            "but wouldn't you have with you\x01",
            "any "peculiar dishes"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F"Peculiar dishes", is it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, actually, I'm looking for samples\x01",
            "to use for the identification unit training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you had dishes made with difficult\x01",
            "to guess ingredients, it would help me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see, samples for identifications.\x02\x03",
            "#00005FHowever...even though you say\x01",
            ""peculiar dishes", what would\x01",
            "be fine, concretely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight, Crossbell police identification\x01",
            "unit is famous for their advanced\x01",
            "analysis equipments...\x02\x03",
            "#00106FI wonder if we, who aren't even cooking\x01",
            "specialists, would be able to be of use?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_389E")

    ChrTalk(
        0x103,
        (
            "#00200FI think we shouldn't ponder too much about it.\x02\x03",
            "#00203FEven just by cooking normally,\x01",
            "sometimes we come up with\x01",
            "unexpected things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C8")

    label("loc_389E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_393A")

    ChrTalk(
        0x105,
        (
            "#10404FHu hu, no need to think too hard about it.\x02\x03",
            "#10400FEven just by cooking normally,\x01",
            "it happens that we make some\x01",
            "unexpected things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C8")

    label("loc_393A")


    ChrTalk(
        0x105,
        (
            "#10304FHu hu, no need to think too hard about it.\x02\x03",
            "#10300FEven just by cooking normally,\x01",
            "it happens that we make some\x01",
            "unexpected things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A34")

    ChrTalk(
        0x109,
        (
            "#10106FI-Indeed...\x01",
            "Every now and then some strange\x01",
            "chemical reactions happen too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A93")

    label("loc_3A34")


    ChrTalk(
        0x104,
        (
            "#00306FYeah, those, right?\x01",
            "Every now and then some strange\x01",
            "chemical reactions happen too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A93")


    ChrTalk(
        0x8,
        (
            "Ooh, it seems you somehow have \x01",
            "a clue to be able to prepare them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Then, please, I'm really counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's always fine, so, when\x01",
            "you have such dishes,\x01",
            "bring them to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, right.\x01",
            "Maybe it's presumptuous of me saying this, but...\x01",
            "I will give you this book.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2EE, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "You can read it when you have time\x01",
            "and sooth your daily fatigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 0)

    label("loc_3C9E")

    Return()

    # Function_8_3559 end

    def Function_9_3C9F(): pass

    label("Function_9_3C9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D4B")

    ChrTalk(
        0xFE,
        (
            "I haven't been attending neither lessons\x01",
            "nor training since a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to this, I wonder if I'll be\x01",
            "able to become a police officer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4261")

    label("loc_3D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DF4")

    ChrTalk(
        0x9,
        (
            "At the time of the raid incident, it seems\x01",
            "bombs were thrown in the police HQ...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*shiver shiver*...I'm scared.\x01",
            "Really, being in the police is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4261")

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E02")
    Jump("loc_4261")

    label("loc_3E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3E10")
    Jump("loc_4261")

    label("loc_3E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E92")

    ChrTalk(
        0x9,
        "Waah, I'm late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today I had training from morning, and yet...\x01",
            "I'm gonna be yelled at by the instructor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4261")

    label("loc_3E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EA0")
    Jump("loc_4261")

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EAE")
    Jump("loc_4261")

    label("loc_3EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3EBC")
    Jump("loc_4261")

    label("loc_3EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_424A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B4")

    ChrTalk(
        0x9,
        (
            "Oh, could it be that you're...\x01",
            "The people of the Special Support Section!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've been always admiring you since\x01",
            "I've seen an article in Crossbell Times\x01",
            "about that Cult incident!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'd even like to be\x01",
            "assigned to the Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, thank you for what you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, wanting to join on purpose\x01",
            "such a tough-like duty post...\x01",
            "You've got strange tastes, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey...\x01",
            "Who's the one who came to join\x01",
            "that duty post on purpose again?\x02\x03",
            "#00000F*cough*, uhmm...\x01",
            "Assignments are decided based on\x01",
            "aptitude, so you can't choose it, but...\x02\x03",
            "#00002FIn case you were assigned to the SSS in \x01",
            "the future, it would be nice working with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes!! I'll do my best!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4245")

    label("loc_41B4")


    ChrTalk(
        0x9,
        (
            "Meeting you all made me\x01",
            "suddenly motivated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know if I'll be able to join \x01",
            "the Special Support Section, but...\x01",
            "I'll do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4245")

    Jump("loc_4261")

    label("loc_424A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_4258")
    Jump("loc_4261")

    label("loc_4258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4261")

    label("loc_4261")

    TalkEnd(0xFE)
    Return()

    # Function_9_3C9F end

    def Function_10_4265(): pass

    label("Function_10_4265")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_431E")

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, I haven't\x01",
            "been able to go back home for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The barrier seems to have vanished...\x01",
            "I guess I should go back at least once...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CA")

    label("loc_431E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_43A6")

    ChrTalk(
        0xA,
        (
            "I've been doing my best\x01",
            "with my curriculum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll do my best to become able to\x01",
            "be of help to my seniors quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CA")

    label("loc_43A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43B4")
    Jump("loc_45CA")

    label("loc_43B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_440A")

    ChrTalk(
        0xA,
        (
            "I've heard a train accident\x01",
            "has happened, but...\x01",
            "How did it occur?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CA")

    label("loc_440A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4418")
    Jump("loc_45CA")

    label("loc_4418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44D1")

    ChrTalk(
        0xA,
        (
            "Even we trainees feel that this independence\x01",
            "proposal has a big meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We wish it becomes a real thing even for \x01",
            "the future growth of the police organisation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CA")

    label("loc_44D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44DF")
    Jump("loc_45CA")

    label("loc_44DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_45A5")

    ChrTalk(
        0xA,
        (
            "Today, a lecture about the autonomous state law\x01",
            "is going to take place in this meeting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For a police officer, law is\x01",
            "something inseparable.\x01",
            "You must firmly abide to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CA")

    label("loc_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_45B3")
    Jump("loc_45CA")

    label("loc_45B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_45C1")
    Jump("loc_45CA")

    label("loc_45C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_45CA")

    label("loc_45CA")

    TalkEnd(0xFE)
    Return()

    # Function_10_4265 end

    def Function_11_45CE(): pass

    label("Function_11_45CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_45DF")
    Jump("loc_4B34")

    label("loc_45DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_47BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DD")

    ChrTalk(
        0xB,
        (
            "Even the trainees seem to be astir\x01",
            "for yesterday's train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, even if they make a noise now,\x01",
            "they can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have to give them a pep talk and\x01",
            "make them focus on their curriculum.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47BA")

    label("loc_46DD")


    ChrTalk(
        0xB,
        (
            "About yesterday's train incident,\x01",
            "even if the trainees here make noise,\x01",
            "they can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now I have to make them focus\x01",
            "on lectures and make them grow for\x01",
            "whatever incident happens in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BA")

    Jump("loc_4B34")

    label("loc_47BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_47CD")
    Jump("loc_4B34")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_47DB")
    Jump("loc_4B34")

    label("loc_47DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47E9")
    Jump("loc_4B34")

    label("loc_47E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4953")

    ChrTalk(
        0xB,
        (
            "Lately, trainees have a more\x01",
            "positive attitude towards their\x01",
            "curriculum than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Having the police been the main solver\x01",
            "of that big incident about that Cult has\x01",
            "probably had a positive effect on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd really wish for the policemen on\x01",
            "active duty to keep showing those\x01",
            "results even for the sake of their juniors.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A40")

    label("loc_4953")


    ChrTalk(
        0xB,
        (
            "The fact that the police mainly solved\x01",
            "that big incident about that Cult has\x01",
            "had a good effect on the trainees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd really wish for the policemen on\x01",
            "active duty to keep showing those\x01",
            "results even for the sake of their juniors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A40")

    Jump("loc_4B34")

    label("loc_4A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A53")
    Jump("loc_4B34")

    label("loc_4A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A61")
    Jump("loc_4B34")

    label("loc_4A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_4B2B")

    ChrTalk(
        0xB,
        (
            "Today too, the CGF men are doing\x01",
            "their best on survival training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just went to watch them, and by the look\x01",
            "of thing, it seems their mood is really back.\x01",
            "Well, I'm really glad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B34")

    label("loc_4B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4B34")

    label("loc_4B34")

    TalkEnd(0xFE)
    Return()

    # Function_11_45CE end

    def Function_12_4B38(): pass

    label("Function_12_4B38")

    Call(0, 13)
    Return()

    # Function_12_4B38 end

    def Function_13_4B3C(): pass

    label("Function_13_4B3C")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA9")

    ChrTalk(
        0xC,
        "Thank you for your hard work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you very much\x01",
            "for coming all the way\x01",
            "here, today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_END)), "loc_4C0F")

    ChrTalk(
        0x101,
        (
            "#00000FAh, no...\x02\x03",
            "#00003FIt seems you'll be working\x01",
            "here for a while...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C67")

    label("loc_4C0F")


    ChrTalk(
        0x101,
        (
            "#00000FAh, no...\x02\x03",
            "#00003FYou had come to work at the\x01",
            "Police Academy, Miss Rebecca?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C67")


    ChrTalk(
        0xC,
        (
            "Yes, after all, the police HQ\x01",
            "reception is still in a state that\x01",
            "can't be opened back to duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, fortunately there\x01",
            "was a data backup in these\x01",
            "terminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By using them, I was able\x01",
            "to resume operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyone too, whenever you need something\x01",
            "at the reception, please talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI see, alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHmm, Miss Rebecca.\x02\x03",
            "#10104FI really want to thank you for\x01",
            "having been the first to come\x01",
            "running when Fran woke up.\x02\x03",
            "#10109FShe was so happy too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        "No, you don't have to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, although I should have\x01",
            "been the one to encourage her,\x01",
            "conversely I was the one encouraged...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, I am really glad\x01",
            "she regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYes, really.\x02\x03",
            "#10100FIf you would like, could you \x01",
            "please go visit her gain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, naturally.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 5)
    TalkEnd(0xC)
    Return()

    label("loc_4FA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_535D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535D")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "My, everyone, what\x01",
            "you have with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could it be a\x01",
            ""fragment"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUhhm, you mean this?\x02\x03",
            "#00000FWe thought it was something\x01",
            "good when we got it, but until now\x01",
            "we didn't figure a way to use it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the fragment to Rebecca.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "My, as I thought...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is a program to restore the\x01",
            "damaged Memory Quartzes data.\x01",
            "The people from forensics were looking for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have that, it should\x01",
            "be possible to analyze a part\x01",
            "of the Cult's terminals data.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51F5")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_51F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_521E")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_521E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5247")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_5247")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_526D")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_526D")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FT-Then...\x01",
            "We can be able to read the parts that\x01",
            "were concealed by Joachim Gｸnther...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, it seems only\x01",
            "a part, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think we will have immediate\x01",
            "results, so, can I send this\x01",
            ""fragment" to forensics?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    TalkEnd(0xC)
    Return()

    label("loc_535D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D9")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x0, 5)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_53EF")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                             # 0
            "Show Combat Notebook\x01",             # 1
            "Check Cult's Terminals Data\x01",      # 2
            "Hand Over Fragments\x01",              # 3
            "Quit\x01",                             # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_544F")

    label("loc_53EF")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                             # 0
            "Show Combat Notebook\x01",             # 1
            "Check Cult's Terminals Data\x01",      # 2
            "Quit\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_544F")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_547D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)
    Jump("loc_54D4")

    label("loc_547D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)
    Call(0, 23)
    Jump("loc_54D4")

    label("loc_54A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54C2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 17)
    Jump("loc_54D4")

    label("loc_54C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D4")
    Call(0, 16)

    label("loc_54D4")

    Jump("loc_5367")

    label("loc_54D9")

    TalkEnd(0xC)
    OP_93(0xC, 0x5A, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    Return()

    # Function_13_4B3C end

    def Function_14_54EA(): pass

    label("Function_14_54EA")


    ChrTalk(
        0xC,
        (
            "At all events...\x01",
            "I am really glad that Fran\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We too must do our best\x01",
            "even for cheering her up.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_14_54EA end

    def Function_15_556B(): pass

    label("Function_15_556B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_5579")
    SetScenarioFlags(0x0, 5)

    label("loc_5579")

    Return()

    # Function_15_556B end

    def Function_16_557A(): pass

    label("Function_16_557A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_5607")

    ChrTalk(
        0xC,
        (
            "My, you have brought\x01",
            "me a "fragment".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order to analyze the Cult\x01",
            "terminals data, do you mind\x01",
            "if I send it to forensics?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5607")


    ChrTalk(
        0x101,
        "#00000FNo, please do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Then, please wait a moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_5654")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7642")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_763D")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56E4")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_56E4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5748")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5748")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57AA")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_57AA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_580C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_580C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617A")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 4 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PAll data from the information terminal No. 1\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 18)

    ChrTalk(
        0xC,
        (
            "#5P...About this data...\x01",
            "It appears it is an entry\x01",
            "regarding the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PA creed that denies the Goddess...\x01",
            "It is really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes...however, it\x01",
            "fits in with Joachim\x01",
            "Gｸnther's testimony.\x02\x03",
            "#00001FAlso, this word, "D"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C65")

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt's the word indicating the "True God" they\x01",
            "believed in instead of the Goddess, right?\x02\x03",
            "#00201FWe have already ascertained that\x01",
            "the "G" in the D∴G Cult name\x01",
            "stands for true wisdom, "Gnosis"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5BFE")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHm, now it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C60")

    label("loc_5BFE")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHm, now it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C60")

    Jump("loc_5D8E")

    label("loc_5C65")


    ChrTalk(
        0x103,
        (
            "#12P#00200FIt's the word indicating the "True God" they\x01",
            "believed in instead of the Goddess, right?\x02\x03",
            "#00201FWe have already ascertained that\x01",
            "the "G" in the D∴G Cult name\x01",
            "stands for true wisdom, "Gnosis"...\x02\x03",
            "With this, it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8E")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut...I'm sure that Professor\x01",
            "Joachim referred to KeA as the\x01",
            "person who would become a "God".\x02\x03",
            "Then, "D" could be also a\x01",
            "word to indicate KeA, but...\x01\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB2")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Gｸnther...\x01",
            "How much did he know...\x02\x03",
            "...We can't figure it out with just this yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FAA")

    label("loc_5EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F45")

    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F...We can't figure it out with just this yet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FAA")

    label("loc_5F45")


    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...\x02\x03",
            "We can't get it with just this yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FAA")


    ChrTalk(
        0x101,
        (
            "#12P#00001FIt also seems that even Mr.\x01",
            "Ernest didn't hear the whole\x01",
            "story from Joachim...\x02\x03",
            "#00003FIf we could have arrested him...\x01",
            "It keeps make you think like that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60CF")

    ChrTalk(
        0xC,
        (
            "#5P...In any case, if we decrypt\x01",
            "the data at this rate, I think we\x01",
            "may understand many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_617A")

    label("loc_60CF")


    ChrTalk(
        0xC,
        (
            "#5P...In any case, if we decrypt\x01",
            "the data at this rate, I think we\x01",
            "may understand many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_617A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DC")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_61DC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6248")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6248")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BAF")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 4 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PAll data from the information terminal No. 2\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 19)

    ChrTalk(
        0xC,
        (
            "#5P...About this data...\x01",
            "It appears there are recorded\x01",
            "details about that "Gnosis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PA drug that has the effect to increase\x01",
            "physical abilities, responsiveness and\x01",
            "furthermore, it draws out latent abilities too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PEven the phenomenon called "Demonize"...\x01",
            "It's a drug full of mysteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FBecause the plant called "Pleroma Grass"\x01",
            "used as raw ingredient grows in colonies\x01",
            "in the Marshlands...\x02\x03",
            "It seems certain that Joachim\x01",
            "was going to collect supplies\x01",
            "in that place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66BA")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data there's a\x01",
            "passage saying that Gnosis...\x02\x03",
            "Is a drug needed to revive their\x01",
            "so-called True God..."D", I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FFrankly, what I'm hearing\x01",
            "is an absurd story...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677D")

    label("loc_66BA")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data there's a\x01",
            "passage saying that Gnosis\x02\x03",
            "is a drug needed to revive their\x01",
            "so-called True God..."D", I mean.\x02\x03",
            "#00108FFrankly, what I'm hearing\x01",
            "is an absurd story...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677D")


    ChrTalk(
        0x103,
        (
            "#12P#00201FEven so, the Cult continued to\x01",
            "research Gnosis with "rituals"\x01",
            "over the span of even 500 years...\x02\x03",
            "#00203F...I was fortunate to be saved\x01",
            "by Mr. Guy, but there have been\x01",
            "quite many victims until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FAnd he phrased that as\x01",
            ""some sacrifices"...\x02\x03",
            "What a really pathetic lot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6909")

    ChrTalk(
        0x105,
        (
            "#12P#10403F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6948")

    label("loc_6909")


    ChrTalk(
        0x105,
        (
            "#12P#10303F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6948")


    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah...although the Cult has disappeared,\x01",
            "maybe we still need to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A37")

    label("loc_69AA")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02\x03",
            "#00001FAlthough the Cult has disappeared,\x01",
            "maybe we still need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A37")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYes...really.\x02\x03",
            "Not only Gnosis, we police\x01",
            "must properly supervise\x01",
            "drugs like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B0C")

    ChrTalk(
        0xC,
        "#5PYes, I agree too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...For the present, I think\x01",
            "this is all regarding Gnosis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BAF")

    label("loc_6B0C")


    ChrTalk(
        0xC,
        "#5PYes, I agree too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...For the present, I think\x01",
            "this is all regarding Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_6BAF")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1B")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6C1B")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763D")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    SetScenarioFlags(0x12A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PAll data from the information terminal No. 3\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 20)

    ChrTalk(
        0xC,
        (
            "#5PThis content...\x01",
            "Is it about KeA who you were\x01",
            "sheltering at the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FKeA was created by the\x01",
            "Crois Clan 500 years ago...\x01",
            "She was presented to the Cult as a religious figure.\x02\x03",
            "As the "Divine Child", their God's vessel,\x01",
            "who keeps slumbering in a "Cradle"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...Even the Cult members didn't\x01",
            "know anything about the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWithout even knowing that they were manipulated\x01",
            "in the shadows for the Crois Clan true goal, they\x01",
            "kept looking for a fantasy called "True God"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7026")

    ChrTalk(
        0x106,
        "#12P#10708F...In a certain sense, they're pitiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70B1")

    label("loc_7026")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7073")

    ChrTalk(
        0x109,
        "#12P#10108F...In a certain sense, they're pitiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70B1")

    label("loc_7073")


    ChrTalk(
        0x105,
        "#12P#10408F...In a certain sense, they're a pitiful lot.\x02",
    )

    CloseMessageWindow()

    label("loc_70B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_710C")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they did,\x01",
            "I don't even pity them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71C1")

    label("loc_710C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7170")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they did,\x01",
            "I have no room for pitying them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71C1")

    label("loc_7170")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they did,\x01",
            "I have no room for pitying them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C1")


    ChrTalk(
        0x101,
        (
            "#12P#00001FPutting the Cult aside,\x01",
            "KeA is completely innocent.\x02\x03",
            "#00003FEven if she's an existence created\x01",
            "for the Crois Clan's goals...\x02\x03",
            "Even if she possesses\x01",
            "miraculous abilities...\x01",
            "Those things don't matter.\x02\x03",
            "That child who woke up before our eyes\x01",
            "was a genuine, normal little girl.\x02\x03",
            "#00001FAnd yet, she was locked up all alone in\x01",
            "a place like that for hundreds of years...\x02\x03",
            "And now, Miss Mariabell\x01",
            "and Lawyer Ian are trying \x01",
            "to use her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...No matter the circumstances,\x01",
            "like hell we're gonna forgive 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...For the present, with this the Cult\x01",
            "data has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI don't know the detailed circumstances\x01",
            "of this incident you are involved in, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI understand so much that it hurts\x01",
            "that Miss KeA is a very precious\x01",
            "existence for you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PPlease...do your best.\x01",
            "I too will cheer for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThank you very much, Miss Rebecca.\x02\x03",
            "We will bring KeA back\x01",
            "with our own hands.\x02\x03",
            "#00007FEven in order to create a future\x01",
            "where our precious KeA...\x01",
            "When that child can live smiling...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7618")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7631")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7631")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)

    label("loc_763D")

    Jump("loc_5654")

    label("loc_7642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_775A")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "If you obtain another "fragment",\x01",
            "please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please ask me again in case you want\x01",
            "to check the decrypted data too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, thank you very much.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_773B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_773B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7754")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7754")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_775A")

    Return()

    # Function_16_557A end

    def Function_17_775B(): pass

    label("Function_17_775B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7765")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7860")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[About The Cult]\x01",              # 0
            "[About Gnosis]\x01",                # 1
            "[About The Divine Child]\x01",      # 2
            "[Nothing]\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7813"),
        (1, "loc_7821"),
        (2, "loc_782F"),
        (3, "loc_783D"),
        (SWITCH_DEFAULT, "loc_784C"),
    )


    label("loc_7813")

    Sound(72, 0, 100, 0)
    Call(0, 18)
    Jump("loc_785B")

    label("loc_7821")

    Sound(72, 0, 100, 0)
    Call(0, 19)
    Jump("loc_785B")

    label("loc_782F")

    Sound(72, 0, 100, 0)
    Call(0, 20)
    Jump("loc_785B")

    label("loc_783D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_785B")

    label("loc_784C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_785B")

    label("loc_785B")

    Jump("loc_7765")

    label("loc_7860")

    Return()

    # Function_17_775B end

    def Function_18_7861(): pass

    label("Function_18_7861")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A8B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01\x01",
            "──My name is Joachim Gｸnther,\x01",
            "High Priest of the "D∴G Cult".\x01",
            "Six years ago, our Cult was almost completely destructed \x01",
            "due to the actions of many powers, Bracers included.\x01",
            "However, only I avoided harm for certain reasons\x01",
            "and was able to escape safely to this land of ■.\x01",
            "I had survived in order to accomplish the Cult\x01",
            "ambition thanks to the great "■"'s guidance.\x01",
            "For when the time comes──\x01",
            "I have decided to record data in each terminal\x01",
            "as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7C92")

    label("loc_7A8B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01\x01",
            "──My name is Joachim Gｸnther,\x01",
            "High Priest of the "D∴G Cult".\x01",
            "Six years ago, our Cult was almost completely destructed \x01",
            "due to the actions of many powers, Bracers included.\x01",
            "However, only I avoided harm for certain reasons\x01",
            "and was able to escape safely to this land of origin.\x01",
            "I had survived in order to accomplish the Cult\x01",
            "ambition thanks to the great "D"'s guidance.\x01",
            "For when the time comes──\x01",
            "I have decided to record data in each terminal\x01",
            "as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7C92")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, I will speak of our Cult's origins.\x01",
            "To do that, I will have to look back at the annoying\x01",
            "history this Zemuria Continent has followed.\x01\x01",
            "──Approximately 1200 years ago, due to the \x01",
            ""Great Collapse", order and an advanced\x01",
            "civilization were lost,  and the "Dark Ages" \x01",
            "where war and poverty  ruled, were brought forth.\x01",
            "Then, the weary people committed a grave error.\x01\x01",
            "Cajoled by the words of imbeciles who had\x01",
            "suddenly appeared, they ended up accepting\x01",
            "the selfish order they had invented.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80C4")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words── The foolish ■■ and the\x01",
            ""■ of ■■", who is the symbol of their faith.\x01",
            "With their order, the "Dark Ages" died, and that\x01",
            "faith spread throughout the continent at once...\x01\x01",
            "I want you to think about this carefully.\x01",
            "If it is true that a "■" exists, shouldn't she\x01",
            "bestow equal salvation to everyone?\x01",
            "However, until this very day the notion of \x01",
            "disparities still exists and people never cease \x01",
            "to lose their lives due to disasters and misfortunes.\x01",
            "So the "■" chooses who to save?\x01",
            "That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8300")

    label("loc_80C4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words── The foolish Septian Church and the\x01",
            ""Goddess of the Sky", who is the symbol of their faith.\x01",
            "With their order, the "Dark Ages" died, and that\x01",
            "faith spread throughout the continent at once...\x01\x01",
            "I want you to think about this carefully.\x01",
            "If it is true that a "Goddess" exists, shouldn't she\x01",
            "bestow equal salvation to everyone?\x01",
            "However, until this very day the notion of \x01",
            "disparities still exists and people never cease \x01",
            "to lose their lives due to disasters and misfortunes.\x01",
            "So the "Goddess" chooses who to save?\x01",
            "That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8300")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84CC")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretence\x01",
            "in order for the "■■" to acquire power.\x01",
            "There is no way something like a "■" exists.\x01\x01",
            "Our predecessors, having arrived at that truth,\x01",
            "set on a long journey in order to meet a "■■".\x01\x01",
            "Then, at the time when the era changed\x01",
            "to the Middle Ages, they finally found it.\x01",
            "■■■■, ■■■■■■■\x01",
            "lying in the depths of this land...\x01\x01",
            ""■"── That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_86BF")

    label("loc_84CC")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretence\x01",
            "in order for the "Septian Church" to acquire power.\x01",
            "There is no way something like a "Goddess" exists.\x01\x01",
            "Our predecessors, having arrived at that truth,\x01",
            "set on a long journey in order to meet a "True God".\x01\x01",
            "Then, at the time when the era changed\x01",
            "to the Middle Ages, they finally found it.\x01",
            "An existence longly asleep, harboring in its body\x01",
            "a great power, lying in the depths of this land...\x01\x01",
            ""D"── That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_86BF")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_18_7861 end

    def Function_19_86D3(): pass

    label("Function_19_86D3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_888C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01\x01",
            ""Gnosis"... It is a secret drug which uses\x01",
            ""Pleroma Grass" as ingredient, a ■■\x01",
            "said to ■■■■.\x01",
            "As for its mixing method, ■■■■■■■.\x01",
            "By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of\x01",
            "drawing out the user's latent abilities.\x01",
            "■■■■■■■■■.\x01",
            "■■■■■■■■■.\x01",
            ""Gnosis" is a drug to ■ the\x01",
            "■'s ■ to "■"'s ■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8A89")

    label("loc_888C")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01\x01",
            ""Gnosis"... It is a secret drug which uses\x01",
            ""Pleroma Grass" as ingredient, a legendary\x01",
            "plant said to bloom above Septium Veins.\x01",
            "As for its mixing method, it goes along with "D".\x01",
            "By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of\x01",
            "drawing out the user's latent abilities.\x01",
            "However, those are nothing more than the beginning.\x01",
            "The true power of this drug laid somewhere else.\x01",
            ""Gnosis" is a drug to link the\x01",
            "user's mind to "D"'s spirit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8A89")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8C12")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy ■ with the ■'s ■,\x01",
            ""■" is able to store ■ and ■.\x01",
            "Sooner or later, when that ■ will lead\x01",
            "to ■, "■" will ■■■■.\x01\x01",
            "Furthermore, there was room\x01",
            "for improvement in "Gnosis".\x01",
            "■■■■■■■■■■■■■,\x01",
            "it is ■■■■■■ to "■".\x01\x01",
            "■■■■■ since then, our Cult has\x01",
            "researched a way higher effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8DF0")

    label("loc_8C12")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy unifying with the user's mind,\x01",
            ""D" is able to store knowledge and grow.\x01",
            "Sooner or later, when that knowledge will lead\x01",
            "to "wisdom", "D" will come back to life.\x01\x01",
            "Furthermore, there was room\x01",
            "for improvement in "Gnosis".\x01",
            "When the user's abilities are forced to the\x01",
            "limit and brought out, it is possible to supply\x01",
            "far more knowledge to "D".\x01",
            "For 500 years since then, our Cult has\x01",
            "researched a way higher effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8DF0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F9C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a ■■\x01",
            "to ■ we ■■■■■■■,\x01",
            "we were close to perfecting "Gnosis",\x01",
            "but a miscalculation arose.\x01\x01",
            "Because the experiments were on a large scale,\x01",
            "Bracers and other authorities smelled our existence\x01",
            "and that was connected to the destruction\x01",
            "of all the lodges as well as the Cult itself.\x01\x01",
            "What foolishness it was, I say.\x01",
            "For our "■■" to ■■■■,\x01",
            "some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_915D")

    label("loc_8F9C")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a speed incomparable\x01",
            "to when we had started 500 years ago,\x01",
            "we were close to perfecting "Gnosis",\x01",
            "but a miscalculation arose.\x01\x01",
            "Because the experiments were on a large scale,\x01",
            "Bracers and other authorities smelled our existence\x01",
            "and that was connected to the destruction\x01",
            "of all the lodges as well as the Cult itself.\x01\x01",
            "What foolishness it was, I say.\x01",
            "For our "True God" to come back to life,\x01",
            "some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_915D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9349")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly\x01",
            "recovered the experimental data and\x01",
            "came to this land of ■, Crossbell.\x01\x01",
            "As for the "Pleroma Grass" which is\x01",
            "a "Gnosis" ingredient, since it ■ in\x01",
            "the ■■ in the ■■\x01",
            "of ■, I had no ■ problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is\x01",
            "a research facility ■ by ■■■\x01",
            "and it is furnished with many high-tech equipment.\x01",
            "Thus, blessed by having a research environment,\x01",
            "I finally completed the secret drug──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_9556")

    label("loc_9349")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly\x01",
            "recovered the experimental data and\x01",
            "came to this land of origin, Crossbell.\x01\x01",
            "As for the "Pleroma Grass" which is\x01",
            "a "Gnosis" ingredient, since it grows in\x01",
            "the Marshlands in the southern part\x01",
            "of Crossbell, I had no supply problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is\x01",
            "a research facility built by Middle Ages alchemists\x01",
            "and it is furnished with many high-tech equipment.\x01",
            "Thus, blessed by having a research environment,\x01",
            "I finally completed the secret drug──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_9556")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_19_86D3 end

    def Function_20_956A(): pass

    label("Function_20_956A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96F4")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01\x01",
            "Crossbell is considered by our "D∴G Cult"\x01",
            "our ■ and ■■■.\x01",
            "The ■ is because it is the place where\x01",
            "the "Divine Child" ■■■■■.\x01\x01",
            "■■■ of the "■■", the "Divine Child"\x01",
            "is a ■■■■ "D∴G Cult".\x01",
            "■■■■■ "Fort of Sun"■,\x01",
            "■■■■■■■■■. ■■\x01",
            "■■■■■■■■■■\x01",
            "■■■■■■ "Fort of Sun"■■■■■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_98F7")

    label("loc_96F4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01\x01",
            "Crossbell is considered by our "D∴G Cult"\x01",
            "our headquarters and land of origin.\x01",
            "The reason is because it is the place where\x01",
            "the "Divine Child" was inherited by our founders.\x01\x01",
            "As the vessel of the "True God", the "Divine Child"\x01",
            "is a symbolic existence for our "D∴G Cult".\x01",
            "Continuing to sleep in the "Fort of Sun" basement,\x01",
            "it has the aspect of a young human maiden. It is\x01",
            "said she has been waiting for the moment to wake\x01",
            "up at the altar of the "Fort of Sun" for 500 years.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_98F7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A7A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a ■ to be able to ■■■■...\x01",
            "It is hard to believe she is a being of this world.\x01\x01",
            "However, I really saw her with my eyes.\x01",
            "A ■■■■■■■■\x01",
            "■■ a ■ called the "■■"──\x01",
            "I saw her ■■.\x01\x01",
            "As for the "■■", it is an "Artifact"\x01",
            "which the ■■, based on the\x01",
            "■■ they were ■, ■.\x01",
            "In this case, even ■■■■\x01",
            "■■■■, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_9C7A")

    label("loc_9A7A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a human to be able to live that much time...\x01",
            "It is hard to believe she is a being of this world.\x01\x01",
            "However, I really saw her with my eyes.\x01",
            "A young girl who keeps sleeping like she is\x01",
            "dozing inside a globe called the "Divine Cradle"──\x01",
            "I saw her divine figure.\x01\x01",
            "As for the "Divine Cradle", it is an "Artifact"\x01",
            "which the Cult predecessors, based on the\x01",
            "alchemists skills they were researching, made.\x01",
            "In this case, even this phenomenon that should\x01",
            "be called a wonder, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_9C7A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E0E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe "Divine Child" ■■■■■\x01",
            "■■■■■■■■■■■\x01",
            "■ "Gnosis" since ■■■■■.\x01\x01",
            "──When she ■ "■", the "Divine Child"\x01",
            "will ■■, and she will ■ "■", the ■■.\x01",
            "Then, ■■'s ■ and ■ will\x01",
            "be ■ in "■" and each person will \x01",
            "be released from the spell of the "■"\x01\x01",
            "This is the prophecy our "D∴G Cult"'s predecessors\x01",
            "left us and the ambition we must fulfill──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_A002")

    label("loc_9E0E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe "Divine Child" is regarded to have accumulated\x01",
            "in her body what could be said to be infinite knowledge\x01",
            "through "Gnosis" since the era she was born.\x01\x01",
            "──When she obtains "wisdom", the "Divine Child"\x01",
            "will wake up, and she will become "D", the True God.\x01",
            "Then, all people's wills and souls will\x01",
            "be consolidated in "D" and each person will \x01",
            "be released from the spell of the "Goddess".\x01\x01",
            "This is the prophecy our "D∴G Cult"'s predecessors\x01",
            "left us and the ambition we must fulfill──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_A002")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_20_956A end

    def Function_21_A016(): pass

    label("Function_21_A016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A03B")
    SetChrPos(0xFE, 3220, 0, 12810, 0)
    Jump("loc_A0EF")

    label("loc_A03B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A060")
    SetChrPos(0xFE, 2220, 0, 12400, 0)
    Jump("loc_A0EF")

    label("loc_A060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A085")
    SetChrPos(0xFE, 4050, 0, 12360, 0)
    Jump("loc_A0EF")

    label("loc_A085")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0AA")
    SetChrPos(0xFE, 3080, 0, 11680, 0)
    Jump("loc_A0EF")

    label("loc_A0AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0CF")
    SetChrPos(0xFE, 2430, 0, 10480, 0)
    Jump("loc_A0EF")

    label("loc_A0CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0EF")
    SetChrPos(0xFE, 3790, 0, 10440, 0)

    label("loc_A0EF")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_A016 end

    def Function_22_A0FE(): pass

    label("Function_22_A0FE")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A11E")
    BeginChrThread(0x101, 1, 0, 21)

    label("loc_A11E")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A135")
    BeginChrThread(0x102, 1, 0, 21)

    label("loc_A135")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14C")
    BeginChrThread(0x103, 1, 0, 21)

    label("loc_A14C")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A163")
    BeginChrThread(0x104, 1, 0, 21)

    label("loc_A163")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A17A")
    BeginChrThread(0x109, 1, 0, 21)

    label("loc_A17A")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A191")
    BeginChrThread(0x105, 1, 0, 21)

    label("loc_A191")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1A8")
    BeginChrThread(0x106, 1, 0, 21)

    label("loc_A1A8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1BF")
    BeginChrThread(0x10A, 1, 0, 21)

    label("loc_A1BF")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A1D9")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A1D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A1F2")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_A1F2")

    Return()

    # Function_22_A0FE end

    def Function_23_A1F3(): pass

    label("Function_23_A1F3")

    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A206")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A429")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A245")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A245")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A279")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A279")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2AD")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A2AD")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2E1")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A2E1")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A315")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A315")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A349")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A349")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A37D")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A37D")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3B1")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_A424")

    label("loc_A3B1")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3E8")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jump("loc_A424")

    label("loc_A3E8")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A41F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    Jump("loc_A424")

    label("loc_A41F")

    Jump("loc_A429")

    label("loc_A424")

    Jump("loc_A206")

    label("loc_A429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_ADD0")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Oh, everyone...\x01",
            "It looks like you have considerably\x01",
            "filled the Combat Notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since I would like to note down the monster information,\x01",
            "I wonder if I could have a look at it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, gladly.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Thank you very much.\x01",
            "I will return your notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is your compensation this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x1 received.\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_A95C")

    label("loc_A65A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6B0")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_A95C")

    label("loc_A6B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A706")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 received.\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_A95C")

    label("loc_A706")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4 received.\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_A95C")

    label("loc_A75C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7B2")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 received.\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_A95C")

    label("loc_A7B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A808")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x6 received.\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_A95C")

    label("loc_A808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A85E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x7 received.\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_A95C")

    label("loc_A85E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 received.\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_A95C")

    label("loc_A8B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A90A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x9 received.\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_A95C")

    label("loc_A90A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "5000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 received.\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_A95C")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A992")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_A9BF")

    label("loc_A992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9BF")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_A9BF")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAF7")

    ChrTalk(
        0xC,
        (
            "Please stop by when you have gathered\x01",
            "monsters information again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA89")

    ChrTalk(
        0x102,
        "#12P#0100FWe will impose on you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAF2")

    label("loc_AA89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC1")

    ChrTalk(
        0x103,
        "#12P#0200FWe will come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAF2")

    label("loc_AAC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAF2")

    ChrTalk(
        0x104,
        "#12P#0300FWe'll come again!\x02",
    )

    CloseMessageWindow()

    label("loc_AAF2")

    Jump("loc_AD68")

    label("loc_AAF7")


    ChrTalk(
        0xC,
        (
            "It looks like you have gathered plenty\x01",
            "of new type monsters information too.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this, I think that our security measures\x01",
            "will become even more perfect from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FHa ha...we're honored to have been of help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uh uh, we are really indebted\x01",
            "towards you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And so, please allow me to give you\x01",
            "a special reward too for this time.\x01",
            "By all means, please accept it.\x02",
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
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "10000 mira\x07\x00",
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    ChrTalk(
        0xC,
        (
            "I will pray for your activities\x01",
            "from now on too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you need anything else, please\x01",
            "visit me again whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD68")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_AD7F")
    ClearScenarioFlags(0x0, 6)

    label("loc_AD7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AD98")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_AD98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ADB1")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_ADB1")

    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2470, 0, 12690, 0)
    EventEnd(0x5)
    TalkBegin(0xC)
    Jump("loc_AF73")

    label("loc_ADD0")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEBE")

    ChrTalk(
        0xC,
        (
            "SInce I think that the information\x01",
            "gathered at HQ is already enough,\x01",
            "let us end the investigation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There could be something else\x01",
            "I will need you your assistance.\x01",
            "I will count on you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF73")

    label("loc_AEBE")


    ChrTalk(
        0xC,
        (
            "It looks like you have been collecting\x01",
            "Combat Notebook contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When you have gathered a little more\x01",
            "information, please show it to me.\x01",
            "I will note down the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF73")

    Return()

    # Function_23_A1F3 end

    def Function_24_AF74(): pass

    label("Function_24_AF74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B14D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B081")

    ChrTalk(
        0xFE,
        "Ooh, Sergei's kids, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I've been entrusted to\x01",
            "guard the Police Academy environs\x01",
            "that lack manpower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while since I was an on-site\x01",
            "commander, but I must do it somehow,\x01",
            "even for the young officers' sake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B14D")

    label("loc_B081")


    ChrTalk(
        0xFE,
        (
            "After I became Section Chief of the District Crime\x01",
            "Prevention Section, I did a lot of desk work, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's an abnormal situation,\x01",
            "somehow I must do it even for\x01",
            "the young officers' sake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B14D")

    TalkEnd(0xFE)
    Return()

    # Function_24_AF74 end

    def Function_25_B151(): pass

    label("Function_25_B151")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B393")
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2FB")

    ChrTalk(
        0xE,
        (
            "As expected, unrest is\x01",
            "spreading to the trainees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even the citizens who casually came for a traffic \x01",
            "short course, having heard that the barrier has \x01",
            "vanished they want to go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, we should really deal\x01",
            "with their impatience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "All right, the policewomen\x01",
            "and I will deal with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You all will continue to be \x01",
            "on the lookout like until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B38F")

    label("loc_B2FB")


    ChrTalk(
        0xD,
        (
            "The policewomen and I will deal\x01",
            "with the trainees and the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You all will continue to be \x01",
            "on the lookout like until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sir!\x02",
    )

    CloseMessageWindow()

    label("loc_B38F")

    OP_4C(0xD, 0xFF)

    label("loc_B393")

    TalkEnd(0xFE)
    Return()

    # Function_25_B151 end

    def Function_26_B397(): pass

    label("Function_26_B397")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(0, 1000, 15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 500, 0, 1000, 0)
    SetChrPos(0x109, -500, 0, 1000, 0)
    SetChrPos(0x102, 500, 0, 0, 0)
    SetChrPos(0x105, -500, 0, 0, 0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 750, 0, 10000, 270)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -750, 0, 10000, 90)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 6000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B4CE():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_B4CE)
    Sleep(50)

    def lambda_B4DE():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B4DE)
    Sleep(50)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B746")

    ChrTalk(
        0xF,
        "#01005F#5POoh, you're finally here.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_B53C():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B53C)
    Sleep(0)

    def lambda_B554():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B554)
    Sleep(0)

    def lambda_B56C():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B56C)
    Sleep(0)

    def lambda_B584():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B584)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Master Sergeant Noｱl,\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PWe have just arrived, we're\x01",
            "terribly sorry for being late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01000F#5PYeah, I've got a call some time ago.\x01",
            "It seems you helped with a\x01",
            "runaway vehicle crackdown.\x02\x03",
            "#01004FWell, being that the case,\x01",
            "I'll overlook your lateness.\x01",
            "...Good job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHa ha, thank you very much.\x02\x03",
            "#00002FAlso, Manager Juan,\x01",
            "it's been a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B87C")

    label("loc_B746")


    ChrTalk(
        0xF,
        "#01005F#5POoh, you're finally here.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_B785():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B785)
    Sleep(0)

    def lambda_B79D():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B79D)
    Sleep(0)

    def lambda_B7B5():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B7B5)
    Sleep(0)

    def lambda_B7CD():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B7CD)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Master Sergeant Noｱl,\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PWe have just arrived.\x02\x03",
            "#00002FManager Juan,\x01",
            "it's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B87C")


    ChrTalk(
        0x109,
        "#10109F#12PI'm glad you look to be healthy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHa ha, with Noｱl we haven't seen \x01",
            "since the recent scheduled trainings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs for Lloyd, I guess it's been ten\x01",
            "months since your graduation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, I hadn't had my eyes on you for a\x01",
            "little while and you've become a fine man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHa ha...\x01",
            "I'm still a novice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PEhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PI presume he's the responsible\x01",
            "party for the Police Academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004F#5PYeah, he's Mr. Juan. He's in charge of the\x01",
            "whole management of the nearby facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, no. I'm not\x01",
            "so important.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#6PThen, Sergei.\x01",
            "Use the meeting\x01",
            "room freely.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "#01002F#11PYes, I'll do.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 27)
    Sleep(3000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01003F#5P──Well then, time is precious.\x02\x03",
            "#01000FFollow me at once,\x01",
            "we'll start immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1280, 1000, 9280, 1500)
    OP_93(0xF, 0x5A, 0x1F4)

    def lambda_BBB1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BBB1)

    def lambda_BBC6():

        label("loc_BBC6")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_BBC6")

    QueueWorkItem2(0x101, 2, lambda_BBC6)

    def lambda_BBD8():

        label("loc_BBD8")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_BBD8")

    QueueWorkItem2(0x102, 2, lambda_BBD8)

    def lambda_BBEA():

        label("loc_BBEA")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_BBEA")

    QueueWorkItem2(0x109, 2, lambda_BBEA)

    def lambda_BBFC():

        label("loc_BBFC")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_BBFC")

    QueueWorkItem2(0x105, 2, lambda_BBFC)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x102,
        "#00105F#12PExcuse me, Chief Sergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PEhm...\x01",
            "What business do you have with us?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01005F#11PWhat, haven't you noticed yet?\x02\x03",
            "#01004FThere should've been many hints...\x01",
            "Eh eh, I guess you're still rookies, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PUgh... P-Please wait!\x02\x03",
            "#00003FMany hints...\x01",
            "The meaning of us having been called here...\x02\x03",
            "#00000FCould it be that──\x02",
        )
    )

    CloseMessageWindow()
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
            "#1KThe reason Sergei called you here is...?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Detective Exam Training]\x01",            # 0
            "[Traffic Basic Rules Training]\x01",       # 1
            "[Orbal Net Technology Training]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BE9A"),
        (1, "loc_BFA6"),
        (2, "loc_C051"),
        (SWITCH_DEFAULT, "loc_C177"),
    )


    label("loc_BE9A")


    ChrTalk(
        0xF,
        (
            "#01006F#11PYou already have a\x01",
            "detective qualification.\x02\x03",
            "#01003FDue to the SSS nature,\x01",
            "there's no need for all\x01",
            "the members to have one.\x02\x03",
            "#01000FThe answer is──\x01",
            "[Traffic Basic Rules Training].\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12PThen, could it mean that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C177")

    label("loc_BFA6")

    OP_2C(0xA1, 0x1)

    ChrTalk(
        0x101,
        (
            "#00002F#6PI see...\x01",
            "[Traffic Basic Rules Training], right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01004F#11PEh eh, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PEhm...\x01",
            "Could it be that...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C177")

    label("loc_C051")


    ChrTalk(
        0xF,
        (
            "#01003F#11PIt's true that in this place too\x01",
            "the Orbal Net is available, but...\x02\x03",
            "If I wanted to make you train in that,\x01",
            "I'd have you go to the Foundation office.\x02\x03",
            "#01000FThe answer is──\x01",
            "[Traffic Basic Rules Training].\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12PThen, could it mean that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C177")

    label("loc_C177")


    ChrTalk(
        0xF,
        (
            "#01004F#11PYeah. It's been decided to \x01",
            "grant an orbal car to the SSS.\x02\x03",
            "#01002FUsing this chance, I'll drive in\x01",
            "your heads the traffic rules ABC.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x3)
    SetChrPos(0x8, 0, 0, 15500, 180)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_68(65000, 3000, 16500, 0)
    MoveCamera(51, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 66840, 150, 16500, 270)
    SetChrPos(0x102, 63210, 150, 16500, 90)
    SetChrPos(0x109, 66800, 150, 13500, 270)
    SetChrPos(0x105, 63230, 150, 13500, 90)
    SetChrPos(0xF, 65000, 0, 20000, 0)
    FadeToBright(1000, 0)
    OP_68(65000, 1000, 16500, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#01003F#5P──That's all. Since you're handling\x01",
            "an orbal car, these are the minimum\x01",
            "basic traffic rules to remember.\x02\x03",
            "#01000FWell, did you get them in your head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PS-Somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh boy, to think that a lecture\x01",
            "was awaiting us in such a place...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C669")

    ChrTalk(
        0x102,
        (
            "#00100F#6P...However, they're only\x01",
            "simpler rules than I thought.\x02\x03",
            "#00103FLike with the previous runaway\x01",
            "vehicle, there're also weak\x01",
            "penalty regulations for foreigners...\x02\x03",
            "#00101FI feel that in the future, with the\x01",
            "orbal cars increase, just those won't\x01",
            "be able to deal with the problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat will be a future issue.\x02\x03",
            "#01001FIt has not even been ten years since orbal\x01",
            "cars for private use have begun to spread.\x02\x03",
            "In time, way stricter rules\x01",
            "will be pursued.\x02\x03",
            "Even regarding penalties for foreigners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7DD")

    label("loc_C669")


    ChrTalk(
        0x102,
        (
            "#00103F#6P...However, they're only\x01",
            "simpler rules than I thought.\x02\x03",
            "#00101FI feel that in the future, with the\x01",
            "orbal cars increase, just those won't\x01",
            "be able to deal with the problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat will be a future issue.\x02\x03",
            "#01001FIt has not even been ten years since orbal\x01",
            "cars for private use have begun to spread.\x02\x03",
            "In time, way stricter\x01",
            "rules will be pursued.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7DD")


    ChrTalk(
        0x109,
        (
            "#10103F#11PIf you apply to the public office\x01",
            "just now, you'll be easily\x01",
            "delivered a driving license, but...\x02\x03",
            "#10101FI'm sure that it's even been in consideration\x01",
            "the introduction of a test system...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5PYeah, when that will be, there\x01",
            "will probably be all kind of\x01",
            "trainings and a practical exam too.\x02\x03",
            "#01000FWell, in any case, for today just\x01",
            "stick the basic rules in your head.\x02\x03",
            "As for the actual driving──\x01",
            "Noｱl, you'll do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#11PYes, roger that!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#5PRight, of course Noｱl\x01",
            "can drive an orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PAfter all, she can drive so much\x01",
            "at will the CGF vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6PEeh, is that so?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha...after I joined the CGF,\x01",
            "the Commander made me learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5PAll right, then I'll grant\x01",
            "you the orbal car at once.\x02\x03",
            "#01000FIt's readied outside, so follow me.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(65000, 1000, 15350, 6000)
    BeginChrThread(0xF, 3, 0, 28)
    WaitChrThread(0xF, 3)
    OP_6F(0x79)
    SetChrFlags(0xF, 0x80)
    Sound(103, 0, 100, 0)
    Sleep(600)
    Sound(104, 0, 100, 0)
    Sleep(600)

    ChrTalk(
        0x101,
        (
            "#00012F#5PHa ha...\x01",
            "What a crazy surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PYes. The Chief too is a hard customer to deal with.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PAnyway, an orbal car, eh?\x02\x03",
            "#10300FI don't know too much about them,\x01",
            "but which will it be, I wonder?\x01",
            "A Verne Corp. one, or a Reinford Corp. one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PYes, when it comes to orbal cars for private use,\x01",
            "those two are the only big manufacturers.\x02\x03",
            "#10102FSo, the Verne Corp. has a long\x01",
            "tradition and an abundant lineup.\x02\x03",
            "From compact cars and medium sized ones,\x01",
            "they even widely deal in buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PAs for the Reinford Corp., they ship\x01",
            "many trucks and limousines, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PYes, if I had to say, many of their\x01",
            "products are sturdy and high class.\x02\x03",
            "#10100FMany of their technologies seem to have been\x01",
            "put to use for orbal trains and orbal tanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PHmmm...\x01",
            "I couldn't feel it yet, but now\x01",
            "I've become a bit excited.\x02\x03",
            "#00000FAll right, let's go have a look.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrPos(0x0, 61500, 0, 18000, 180)
    SetScenarioFlags(0x127, 5)
    OP_29(0xA1, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_26_B397 end

    def Function_27_CF73(): pass

    label("Function_27_CF73")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -3000, 0, 13250, 2000, 0x0)
    OP_95(0xFE, -6500, 0, 13250, 2000, 0x0)
    Return()

    # Function_27_CF73 end

    def Function_28_CFA3(): pass

    label("Function_28_CFA3")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 61500, 0, 18500, 2500, 0x0)
    OP_95(0xFE, 61500, 0, 6500, 2500, 0x0)
    Return()

    # Function_28_CFA3 end

    def Function_29_CFD3(): pass

    label("Function_29_CFD3")

    EventBegin(0x0)
    Fade(500)
    OP_68(-970, 1400, 13500, 0)
    MoveCamera(42, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20360, 0)
    SetChrPos(0x101, -600, 0, 13400, 0)
    SetChrPos(0x102, 600, 0, 13400, 0)
    SetChrPos(0x103, -700, 0, 12200, 0)
    SetChrPos(0x104, 700, 0, 12200, 0)
    SetChrPos(0xF4, -800, 0, 11000, 0)
    SetChrPos(0xF5, 800, 0, 11000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8AF")

    ChrTalk(
        0x8,
        (
            "Oh, aren't you the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm glad\x01",
            "you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FManager Juan...\x01",
            "Likewise, we're glad you're safe too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FIt seems the CGF\x01",
            "has come here.\x02\x03",
            "#00103FWasn't the State Guard\x01",
            "doing security here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. With the news of the President having\x01",
            "been restrained, they withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in order to quell the\x01",
            "disturbances in every place,\x01",
            "the State Guard must do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In their replacement, reinforces came from police\x01",
            "HQ and they coped with this place disturbances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FBy the way...\x01",
            "What's happened to ol'\x01",
            "man Garcｵa in the end?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D377")

    ChrTalk(
        0x105,
        (
            "#12P#10402FWhen you escaped from prison,\x01",
            "he helped you out, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D433")

    label("loc_D377")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D6")

    ChrTalk(
        0x109,
        (
            "#12P#10100FWhen you escaped from prison,\x01",
            "he helped you out, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D433")

    label("loc_D3D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D433")

    ChrTalk(
        0x106,
        (
            "#12P#10702FWhen you escaped from prison,\x01",
            "he helped you out, am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D433")


    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah...he really helped\x01",
            "me out a lot back then.\x02\x03",
            "#00006FWait, you should've got scruples in\x01",
            "saying such a thing in this kind of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, regarding your arrest,\x01",
            "with the President restraint,\x01",
            "it was judged invalid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that respect, you shouldn't\x01",
            "bother about it now of all times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, about Garcｵa...\x01",
            "He put up a fight against the State Guard\x01",
            "and has been restrained since some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Currently, he has been imprisoned once\x01",
            "again and he's receiving treatment.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#00205FTreatment...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D72F")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHe fought the State Guard alone.\x01",
            "I think he should be heavily exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D811")

    label("loc_D72F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7A0")

    ChrTalk(
        0x106,
        (
            "#12P#10703FIf he has fought the State Guard alone...\x01",
            "He's probably severely exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D811")

    label("loc_D7A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D811")

    ChrTalk(
        0x109,
        (
            "#12P#10103FIf he has fought the State Guard alone...\x01",
            "I expect he should be\x01",
            "quite exhausted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D811")


    ChrTalk(
        0x8,
        (
            "Yes, he won't be able\x01",
            "to move for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, if you want, it's also\x01",
            "possible to visit him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FLloyd, what do we do?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 1)
    Jump("loc_D937")

    label("loc_D8AF")


    ChrTalk(
        0x8,
        (
            "Garcｵa has been imprisoned\x01",
            "once again and he's currently\x01",
            "receiving treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want, it's also\x01",
            "possible to visit him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D937")

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
            "Visit Garcｵa\x01",      # 0
            "Do Not\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA43")

    ChrTalk(
        0x101,
        (
            "#12P#00003F(I must thank Garcｵa\x01",
            "for back then...)\x02\x03",
            "#00000F...Manager Juan, if you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll have Melvin guide you.\x01",
            "Go with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Jump("loc_DAB7")

    label("loc_DA43")


    ChrTalk(
        0x101,
        "#12P#00003F...No, not now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hm, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, tell me whenever you want\x01",
            "if you wish to visit him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB7")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_CFD3 end

    def Function_30_DAE7(): pass

    label("Function_30_DAE7")


    ChrTalk(
        0x101,
        (
            "#12P#00003F(I must thank Garcｵa\x01",
            "for back then...)\x02\x03",
            "#00000F...Manager Juan, if you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll have Melvin guide you.\x01",
            "Go with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_DAE7 end

    def Function_31_DB92(): pass

    label("Function_31_DB92")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business\x01",
            "on the other floors. Let's\x01",
            "stop loitering around.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_31_DB92 end

    def Function_32_DBF6(): pass

    label("Function_32_DBF6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_32_DBF6 end

    SaveToFile()

Try(main)
