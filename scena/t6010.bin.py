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
        "Function_5_184C",         # 05, 5
        "Function_6_3033",         # 06, 6
        "Function_7_3206",         # 07, 7
        "Function_8_33CF",         # 08, 8
        "Function_9_3AD2",         # 09, 9
        "Function_10_4042",        # 0A, 10
        "Function_11_4372",        # 0B, 11
        "Function_12_48CE",        # 0C, 12
        "Function_13_48D2",        # 0D, 13
        "Function_14_5273",        # 0E, 14
        "Function_15_52F7",        # 0F, 15
        "Function_16_5306",        # 10, 16
        "Function_17_7441",        # 11, 17
        "Function_18_7547",        # 12, 18
        "Function_19_836C",        # 13, 19
        "Function_20_9175",        # 14, 20
        "Function_21_9BC6",        # 15, 21
        "Function_22_9CAE",        # 16, 22
        "Function_23_9DA3",        # 17, 23
        "Function_24_AAD4",        # 18, 24
        "Function_25_ACC1",        # 19, 25
        "Function_26_AF02",        # 1A, 26
        "Function_27_C8D1",        # 1B, 27
        "Function_28_C901",        # 1C, 28
        "Function_29_C931",        # 1D, 29
        "Function_30_D3CA",        # 1E, 30
        "Function_31_D475",        # 1F, 31
        "Function_32_D4DE",        # 20, 32
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1836")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Give Peculiar Dishes\x01",      # 1
            "Cancel\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_641")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Jump("loc_1831")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1831")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1827")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D8")
    MenuCmd(1, 1, "Bitter Noodles "Severed"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_6CE")
    Call(0, 7)

    label("loc_6CE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_719")
    MenuCmd(1, 1, "Gehenna Mapo "Hell King"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_70F")
    Call(0, 7)

    label("loc_70F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_754")
    MenuCmd(1, 1, "Mottled Burnt Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_74A")
    Call(0, 7)

    label("loc_74A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_790")
    MenuCmd(1, 1, "Diehard Meat "Rock"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_786")
    Call(0, 7)

    label("loc_786")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CC")
    MenuCmd(1, 1, "Chaos Stew "Impure"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_7C2")
    Call(0, 7)

    label("loc_7C2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80D")
    MenuCmd(1, 1, "Manly Cooking "Mountain"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_803")
    Call(0, 7)

    label("loc_803")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84B")
    MenuCmd(1, 1, "Manly Cooking "River"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_841")
    Call(0, 7)

    label("loc_841")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87E")
    MenuCmd(1, 1, "Fish Arrow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_874")
    Call(0, 7)

    label("loc_874")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB")
    MenuCmd(1, 1, "Very Spicy Bomb Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_8B1")
    Call(0, 7)

    label("loc_8B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F0")
    MenuCmd(1, 1, "Needle Pasta")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_8E6")
    Call(0, 7)

    label("loc_8E6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_926")
    MenuCmd(1, 1, "Bitter Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_91C")
    Call(0, 7)

    label("loc_91C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_963")
    MenuCmd(1, 1, "Quattro Tomato Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_959")
    Call(0, 7)

    label("loc_959")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99F")
    MenuCmd(1, 1, "Protection Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_995")
    Call(0, 7)

    label("loc_995")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DC")
    MenuCmd(1, 1, "Lunch Box "Surprise"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_9D2")
    Call(0, 7)

    label("loc_9D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A10")
    MenuCmd(1, 1, "Magica Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_A06")
    Call(0, 7)

    label("loc_A06")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A45")
    MenuCmd(1, 1, "Enigma Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_A3B")
    Call(0, 7)

    label("loc_A3B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7F")
    MenuCmd(1, 1, "Reflect Chocolate")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_A75")
    Call(0, 7)

    label("loc_A75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB8")
    MenuCmd(1, 1, "Jiggling Pudding")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_AAE")
    Call(0, 7)

    label("loc_AAE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AED")
    MenuCmd(1, 1, "Recovery Ice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_AE3")
    Call(0, 7)

    label("loc_AE3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B25")
    MenuCmd(1, 1, "Secrecy Popcorn")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_B1B")
    Call(0, 7)

    label("loc_B1B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B66")
    MenuCmd(1, 1, "Medicine "Sasa Veitchii"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_B5C")
    Call(0, 7)

    label("loc_B5C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B9C")
    MenuCmd(1, 1, "Purple Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_B92")
    Call(0, 7)

    label("loc_B92")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD1")
    MenuCmd(1, 1, "Brown Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_BC7")
    Call(0, 7)

    label("loc_BC7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C05")
    MenuCmd(1, 1, "Pink Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_BFB")
    Call(0, 7)

    label("loc_BFB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C05")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C98")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you. If you have\x01",
            "something nice again,\x01",
            "please hand it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_C98")

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
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_D05")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D67")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x195, 1)
    SetScenarioFlags(0x20C, 1)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x195),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_D5D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x198, 1)
    SetScenarioFlags(0x20C, 2)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x198),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_DB5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E17")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19B, 1)
    SetScenarioFlags(0x20C, 3)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x19B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_E0D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E6F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E65")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19E, 1)
    SetScenarioFlags(0x20C, 4)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x19E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_E65")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EC7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A1, 1)
    SetScenarioFlags(0x20C, 5)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_EBD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F1F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F15")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A4, 1)
    SetScenarioFlags(0x20C, 6)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_F15")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F77")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A7, 1)
    SetScenarioFlags(0x20C, 7)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_F6D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FCF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AA, 1)
    SetScenarioFlags(0x20D, 0)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_FC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AD, 1)
    SetScenarioFlags(0x20D, 1)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_101D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_107F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1075")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B0, 1)
    SetScenarioFlags(0x20D, 2)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1075")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_107F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10D7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B3, 1)
    SetScenarioFlags(0x20D, 3)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_10CD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B6, 1)
    SetScenarioFlags(0x20D, 4)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1125")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_112F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1187")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B9, 1)
    SetScenarioFlags(0x20D, 5)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_117D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11DF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x20D, 6)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_11D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1237")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BF, 1)
    SetScenarioFlags(0x20D, 7)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_122D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_128F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1285")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C2, 1)
    SetScenarioFlags(0x20E, 0)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1285")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12E7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C5, 1)
    SetScenarioFlags(0x20E, 1)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_12DD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_133F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1335")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C8, 1)
    SetScenarioFlags(0x20E, 2)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1335")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1397")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CB, 1)
    SetScenarioFlags(0x20E, 3)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_138D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CE, 1)
    SetScenarioFlags(0x20E, 4)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_13E5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1447")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D1, 1)
    SetScenarioFlags(0x20E, 5)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_143D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1495")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D4, 1)
    SetScenarioFlags(0x20E, 6)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_1495")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14ED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D7, 1)
    SetScenarioFlags(0x20E, 7)

    AnonymousTalk(
        0xFF,
        (
            "Gave ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " to Manager Juan.\x02",
        )
    )


    label("loc_14ED")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14F7")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1818")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oh, it seems you brought\x01",
            "me a lot of "peculiar\x01",
            "dishes".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These should do for training the\x01",
            "identification unit for now. ...Thank\x01",
            "you, you've really helped me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, please don't worry\x01",
            "about it. It wasn't a\x01",
            "big deal, and...\x02\x03",
            "Well, it seems I was\x01",
            "able to be useful to my\x01",
            "alma mater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're commendable, Lloyd... Yes,\x01",
            "that aspect of you hasn't changed\x01",
            "since your days as a student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right, would you\x01",
            "like to accept this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a quartz for the ENIGMA II\x01",
            "we've recently started using and\x01",
            "they provided us with an extra.\x02",
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
            "No no, thank you. I'll be\x01",
            "counting on you if\x01",
            "something comes up again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 1)
    TalkEnd(0x8)
    Return()

    label("loc_1818")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1822")

    Jump("loc_67B")

    label("loc_1827")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1831")

    Jump("loc_5DF")

    label("loc_1836")

    Jump("loc_1848")

    label("loc_183B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_1848")

    TalkEnd(0x8)
    Return()

    # Function_4_5AD end

    def Function_5_184C(): pass

    label("Function_5_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(
        0x8,
        (
            "After receiving the information\x01",
            "about the President's arrest,\x01",
            "the State Guard withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in order to quell the\x01",
            "disturbances throughout the state,\x01",
            "the State Guard must do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have to do what we\x01",
            "can as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19D8")

    label("loc_1953")


    ChrTalk(
        0x8,
        (
            "The reinforcements that came\x01",
            "from HQ are currently coping\x01",
            "with the disturbances nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have to do what we\x01",
            "can as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D8")

    Jump("loc_302F")

    label("loc_19DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC4")

    ChrTalk(
        0x8,
        (
            "...That attack was too\x01",
            "gruesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was a small mercy that\x01",
            "the young officers of this\x01",
            "police academy were safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that it will be\x01",
            "some time before Crossbell\x01",
            "recovers completely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B6D")

    label("loc_1AC4")


    ChrTalk(
        0x8,
        (
            "...It was a small mercy that\x01",
            "the young officers here were\x01",
            "spared from the attack...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that it will be\x01",
            "some time before Crossbell\x01",
            "recovers completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6D")

    Jump("loc_302F")

    label("loc_1B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C84")

    ChrTalk(
        0x8,
        (
            "About the gate that was destroyed\x01",
            "yesterday... It seems that it will take\x01",
            "some time for a new one to be prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, no one could\x01",
            "have expected it to be\x01",
            "destroyed like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll have to rely on\x01",
            "CGF security for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D30")

    label("loc_1C84")


    ChrTalk(
        0x8,
        (
            "About the gate that was destroyed\x01",
            "yesterday... It seems that it will take\x01",
            "some time for a new one to be prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll have to rely on\x01",
            "CGF security for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D30")

    Jump("loc_302F")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F81")

    ChrTalk(
        0x8,
        (
            "Oh, it's Lloyd and\x01",
            "friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard a big noise in\x01",
            "the premises earlier...\x01",
            "What was it, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...We confirmed destruction of the\x01",
            "front gate some time ago. Most\x01",
            "likely, that was the sound you heard.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "W-What did you say!?\x01",
            "That gate constructed of\x01",
            "a special alloy was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't tell me it was a\x01",
            "Cryptid...? No one told\x01",
            "me they had such power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWe can't say anything yet, but...\x02\x03",
            "We can't rule out the possibility\x01",
            "it will come here either.\x01",
            "...Please remain vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "S-Sure... You too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 0)
    Jump("loc_1FD7")

    label("loc_1F81")


    ChrTalk(
        0x8,
        (
            "We too will watch the\x01",
            "area attentively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone... Please be\x01",
            "very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD7")

    Jump("loc_302F")

    label("loc_1FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_206C")

    ChrTalk(
        0x8,
        (
            "It seems no one has\x01",
            "sighted the cryptid in\x01",
            "the woodlands today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hear the bracers are\x01",
            "investigating elsewhere\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302F")

    label("loc_206C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(
        0x8,
        (
            "A Cryptid has been\x01",
            "spotted in Knox\x01",
            "Woodlands, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bracers named Ling and Eolia took\x01",
            "on its extermination, but in the\x01",
            "end, it seems they failed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That place is the CGF training\x01",
            "ground, so thinking about the future,\x01",
            "it seems we should keep up our watch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_223E")

    label("loc_2196")


    ChrTalk(
        0x8,
        (
            "A Cryptid has been\x01",
            "spotted in Knox\x01",
            "Woodlands, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears it escaped somewhere...\x01",
            "Thinking about the future, it seems\x01",
            "it's best to keep up our watch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223E")

    Jump("loc_302F")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B4")

    ChrTalk(
        0x8,
        (
            "The police academy\x01",
            "curriculum is a strict\x01",
            "half year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It focuses mainly on classroom lectures and\x01",
            "practical training, and after graduation, you\x01",
            "can be assigned to many different duty posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In a manner of speaking, it's\x01",
            "where chick officers are taught\x01",
            "to make their first flight...\x02",
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
    Jump("loc_2451")

    label("loc_23B4")


    ChrTalk(
        0x8,
        (
            "This is the place where the\x01",
            "chick officers are taught how\x01",
            "to make their first flight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel especially proud\x01",
            "of serving at this\x01",
            "police academy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2451")

    Jump("loc_302F")

    label("loc_2456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_29A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E7")

    ChrTalk(
        0x8,
        (
            "Douglas, who became CGF Vice\x01",
            "Commander, was an instructor\x01",
            "here for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was mainly in charge of\x01",
            "practical training and showed up\x01",
            "often at the training grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... He was really strict.\x02\x03",
            "#00008FThose hellish scenes of people\x01",
            "dropping out of training, one\x01",
            "after the next, and then again...\x02\x03",
            "#00006FEven remembering it now I can't\x01",
            "stop shivering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that guy is the type to\x01",
            "thrust unreasonable demands\x01",
            "at you while freshly smilin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. So there's a\x01",
            "reason Lloyd called him\x01",
            "Demon Douglas yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHowever, being able to learn\x01",
            "fighting techniques from the hope\x01",
            "of the CGF makes me envious.\x02\x03",
            "#10104FIf possible, I would've liked to\x01",
            "learn from him too when I was a\x01",
            "recruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FW-Well, I'm grateful to him. What\x01",
            "he taught me has been useful in\x01",
            "actual combat many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've gained many\x01",
            "excellent officers thanks\x01",
            "to him, Lloyd included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the police academy, he was\x01",
            "talented man we didn't want\x01",
            "to let go no matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, he is originally from the CGF, and\x01",
            "since the request came from Commander\x01",
            "Sonya, it couldn't have been helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 6)
    Jump("loc_299C")

    label("loc_28E7")


    ChrTalk(
        0x8,
        (
            "As a police academy, we\x01",
            "didn't want to let\x01",
            "Douglas go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, he is originally from the CGF, and\x01",
            "since the request came from Commander\x01",
            "Sonya, it couldn't have been helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299C")

    Jump("loc_302F")

    label("loc_29A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9C")

    ChrTalk(
        0x8,
        (
            "Oh, the SSS ladies and\x01",
            "gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard about it from Sergei,\x01",
            "but it seems you're riding that\x01",
            "new model orbal car daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well, yes. It's been\x01",
            "very useful to us for our\x01",
            "activities outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you must strictly\x01",
            "adhere to traffic rules\x01",
            "when driving it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A traffic accident caused by\x01",
            "a police officer... That\x01",
            "would be no laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, you said it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FT-There's no way I'd get\x01",
            "into an accident!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, it's not that Noｱl\x01",
            "is a speed freak or\x01",
            "anything, but...\x02\x03",
            "#00304FLovin' orbal cars too\x01",
            "much could make her\x01",
            "shortsighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FY-You too, Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, we're not completely\x01",
            "used to it yet... Let's keep\x01",
            "that in mind, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 5)
    Jump("loc_2D36")

    label("loc_2C9C")


    ChrTalk(
        0x8,
        (
            "If you drive a car, you\x01",
            "must respect traffic\x01",
            "rules properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A traffic accident caused by\x01",
            "a police officer... That\x01",
            "would be no laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D36")

    Jump("loc_302F")

    label("loc_2D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_302F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC1")

    ChrTalk(
        0x8,
        (
            "It appears you've\x01",
            "finished your short\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now it's down to\x01",
            "practical skills, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well, more or\x01",
            "less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FAnyhow, that Chief could\x01",
            "hold that training is\x01",
            "quite unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's because he's been the\x01",
            "police academy driving\x01",
            "instructor before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I'm sure it was\x01",
            "easy to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh, come to think of it,\x01",
            "he said something about\x01",
            "that before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FHmm. Even Chief Sergei\x01",
            "is a man with many\x01",
            "secrets.\x02\x03",
            "#10101FPersonally, I'm curious\x01",
            "about his relationship\x01",
            "with Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, he's not the kind\x01",
            "of person to say much\x01",
            "about himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 5)
    Jump("loc_302F")

    label("loc_2FC1")


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
            "You shouldn't make your\x01",
            "superior wait. Go,\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302F")

    Call(0, 8)
    Return()

    # Function_5_184C end

    def Function_6_3033(): pass

    label("Function_6_3033")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_3050")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_3063")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_3076")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_3089")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_309C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_309C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_30AF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_30C2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_30D5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_30E8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_30FB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_310E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_310E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_3121")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_3134")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_3147")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_315A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_315A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_316D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_316D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_3180")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_3193")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_31A6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_31B9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_31CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_31DF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_31F2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_3205")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3205")

    Return()

    # Function_6_3033 end

    def Function_7_3206(): pass

    label("Function_7_3206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3219")
    MenuCmd(3, 1, 0x0)

    label("loc_3219")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322C")
    MenuCmd(3, 1, 0x1)

    label("loc_322C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323F")
    MenuCmd(3, 1, 0x2)

    label("loc_323F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3252")
    MenuCmd(3, 1, 0x3)

    label("loc_3252")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3265")
    MenuCmd(3, 1, 0x4)

    label("loc_3265")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3278")
    MenuCmd(3, 1, 0x5)

    label("loc_3278")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328B")
    MenuCmd(3, 1, 0x6)

    label("loc_328B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329E")
    MenuCmd(3, 1, 0x7)

    label("loc_329E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B1")
    MenuCmd(3, 1, 0x8)

    label("loc_32B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C4")
    MenuCmd(3, 1, 0x9)

    label("loc_32C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D7")
    MenuCmd(3, 1, 0xA)

    label("loc_32D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32EA")
    MenuCmd(3, 1, 0xB)

    label("loc_32EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32FD")
    MenuCmd(3, 1, 0xC)

    label("loc_32FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3310")
    MenuCmd(3, 1, 0xD)

    label("loc_3310")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3323")
    MenuCmd(3, 1, 0xE)

    label("loc_3323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3336")
    MenuCmd(3, 1, 0xF)

    label("loc_3336")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3349")
    MenuCmd(3, 1, 0x10)

    label("loc_3349")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335C")
    MenuCmd(3, 1, 0x11)

    label("loc_335C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336F")
    MenuCmd(3, 1, 0x12)

    label("loc_336F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3382")
    MenuCmd(3, 1, 0x13)

    label("loc_3382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3395")
    MenuCmd(3, 1, 0x14)

    label("loc_3395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A8")
    MenuCmd(3, 1, 0x15)

    label("loc_33A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33BB")
    MenuCmd(3, 1, 0x16)

    label("loc_33BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33CE")
    MenuCmd(3, 1, 0x17)

    label("loc_33CE")

    Return()

    # Function_7_3206 end

    def Function_8_33CF(): pass

    label("Function_8_33CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD1")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "That aside... Would you all\x01",
            "happen to have any\x01",
            ""peculiar dishes" with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FPeculiar dishes, you\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. Actually, I'm\x01",
            "looking for samples to\x01",
            "train the forensics unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It would be a big help if\x01",
            "you had dishes with hard-to-\x01",
            "guess ingredients, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see. Forensics samples,\x01",
            "huh.\x02\x03",
            "#00005FBut... Peculiar dishes,\x01",
            "you say. What might you be\x01",
            "looking for, specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight. The Crossbell Police\x01",
            "forensics unit is famous for their\x01",
            "advanced analysis equipment...\x02\x03",
            "#00106FI wonder if we, who aren't even\x01",
            "cooking specialists, will be of\x01",
            "any use.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36DB")

    ChrTalk(
        0x103,
        (
            "#00200FMaybe we shouldn't think\x01",
            "about it too hard?\x02\x03",
            "#00203FJust by cooking normally,\x01",
            "we sometimes come up with\x01",
            "unexpected things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3819")

    label("loc_36DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3781")

    ChrTalk(
        0x105,
        (
            "#10404FHaha. Maybe we don't need\x01",
            "to think too hard about\x01",
            "it?\x02\x03",
            "#10400FJust by cooking normally,\x01",
            "we sometimes come up with\x01",
            "unexpected things, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3819")

    label("loc_3781")


    ChrTalk(
        0x105,
        (
            "#10304FHaha. Maybe we don't need\x01",
            "to think too hard about\x01",
            "it?\x02\x03",
            "#10300FJust by cooking normally,\x01",
            "we sometimes come up with\x01",
            "unexpected things, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3819")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(
        0x109,
        (
            "#10106FI-Indeed... There are times\x01",
            "when strange chemical\x01",
            "reactions happen as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_3886")


    ChrTalk(
        0x104,
        (
            "#00306FYeah, there are times\x01",
            "when strange chemical\x01",
            "reactions happen as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D8")


    ChrTalk(
        0x8,
        (
            "Oh, it looks like you\x01",
            "have some ideas as to\x01",
            "how to prepare them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case, I'll be\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anytime is fine, so please\x01",
            "bring them to me if you\x01",
            "get your hands on any.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright. Sure thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "That's right. This isn't\x01",
            "compensation, but... Why don't\x01",
            "I give you all this book.\x02",
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
            "If you have time, read\x01",
            "it to ease your daily\x01",
            "fatigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 0)

    label("loc_3AD1")

    Return()

    # Function_8_33CF end

    def Function_9_3AD2(): pass

    label("Function_9_3AD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B73")

    ChrTalk(
        0xFE,
        (
            "I've attended neither\x01",
            "lessons nor training for\x01",
            "some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder\x01",
            "if I'll be able to become\x01",
            "a police officer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403E")

    label("loc_3B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BFF")

    ChrTalk(
        0x9,
        (
            "At the time of the\x01",
            "attack, police HQ was\x01",
            "bombed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*shiver shiver*... I'm\x01",
            "scared. Really, being in\x01",
            "the police is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403E")

    label("loc_3BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C0D")
    Jump("loc_403E")

    label("loc_3C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3C1B")
    Jump("loc_403E")

    label("loc_3C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C9D")

    ChrTalk(
        0x9,
        "Waah, I'm late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They said there was training\x01",
            "this morning... I'm gonna get\x01",
            "yelled at by the instructor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403E")

    label("loc_3C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CAB")
    Jump("loc_403E")

    label("loc_3CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CB9")
    Jump("loc_403E")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CC7")
    Jump("loc_403E")

    label("loc_3CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0x9,
        (
            "Oh, could it be that\x01",
            "you're... The people of the\x01",
            "Special Support Section!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've always admired you since\x01",
            "I saw that Crossbell Times\x01",
            "about the cult incident!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future, I'd even\x01",
            "like to be assigned to the\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, I'm happy to\x01",
            "hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man, wanting to join such a\x01",
            "tough post specifically...\x01",
            "You've got strange tastes, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey... Who specifically joined\x01",
            "that post again?\x02\x03",
            "#00000F*ahem*, uhmm... Assignments are\x01",
            "decided based on aptitude, so\x01",
            "you don't get to choose, but...\x02\x03",
            "#00002FIf you are assigned to the SSS\x01",
            "in the future, it would be a\x01",
            "pleasure to work with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes!! I'll do my best!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4022")

    label("loc_3F92")


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
            "I don't know if I'll be able to\x01",
            "join the Special Support\x01",
            "Section, but... I'll do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4022")

    Jump("loc_403E")

    label("loc_4027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_4035")
    Jump("loc_403E")

    label("loc_4035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_403E")

    label("loc_403E")

    TalkEnd(0xFE)
    Return()

    # Function_9_3AD2 end

    def Function_10_4042(): pass

    label("Function_10_4042")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_40F5")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I\x01",
            "haven't been able to go\x01",
            "back home for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The barrier seems to have\x01",
            "vanished... I guess I should\x01",
            "go back at least once...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436E")

    label("loc_40F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_417B")

    ChrTalk(
        0xA,
        (
            "I've been doing my best\x01",
            "with the curriculum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll do my best to be of\x01",
            "help to my seniors as\x01",
            "soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436E")

    label("loc_417B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4189")
    Jump("loc_436E")

    label("loc_4189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_41D7")

    ChrTalk(
        0xA,
        (
            "I've heard a train\x01",
            "accident occurred,\x01",
            "but... How, exactly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436E")

    label("loc_41D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41E5")
    Jump("loc_436E")

    label("loc_41E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4290")

    ChrTalk(
        0xA,
        (
            "Even we trainees feel this\x01",
            "independence proposal has\x01",
            "great meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We hope it becomes real\x01",
            "even for the future growth\x01",
            "of the police organization.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436E")

    label("loc_4290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_429E")
    Jump("loc_436E")

    label("loc_429E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4349")

    ChrTalk(
        0xA,
        (
            "A lecture about state\x01",
            "law is going be held in\x01",
            "this meeting room today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To a police officer, the\x01",
            "law is indispensable. One\x01",
            "must firmly abide by it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436E")

    label("loc_4349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4357")
    Jump("loc_436E")

    label("loc_4357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_4365")
    Jump("loc_436E")

    label("loc_4365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_436E")

    label("loc_436E")

    TalkEnd(0xFE)
    Return()

    # Function_10_4042 end

    def Function_11_4372(): pass

    label("Function_11_4372")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4383")
    Jump("loc_48CA")

    label("loc_4383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4560")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4486")

    ChrTalk(
        0xB,
        (
            "Even the trainees seem to\x01",
            "be flustered due to\x01",
            "yesterday's train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, no matter how\x01",
            "agitated they are, there's\x01",
            "nothing they can about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have to encourage them\x01",
            "and make them focus on\x01",
            "their curriculum.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_455B")

    label("loc_4486")


    ChrTalk(
        0xB,
        (
            "Even if the trainees are agitated\x01",
            "about yesterday's accident, there's\x01",
            "nothing they can do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now I have to make them focus on\x01",
            "lectures and help them grow for\x01",
            "whatever future incidents may happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455B")

    Jump("loc_48CA")

    label("loc_4560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_456E")
    Jump("loc_48CA")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_457C")
    Jump("loc_48CA")

    label("loc_457C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_458A")
    Jump("loc_48CA")

    label("loc_458A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E8")

    ChrTalk(
        0xB,
        (
            "Lately, trainees have had a\x01",
            "more positive attitude towards\x01",
            "their curriculum than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The fact that the police were mainly\x01",
            "responsible for solving the cult incident\x01",
            "probably had a big influence on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like the police on active duty\x01",
            "to continue to produce results even\x01",
            "for the sake of their juniors.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47D5")

    label("loc_46E8")


    ChrTalk(
        0xB,
        (
            "The fact that the police were mainly\x01",
            "responsible for solving the cult incident\x01",
            "probably had a big influence on the trainees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like the police on active duty\x01",
            "to continue to produce results even\x01",
            "for the sake of their juniors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D5")

    Jump("loc_48CA")

    label("loc_47DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47E8")
    Jump("loc_48CA")

    label("loc_47E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47F6")
    Jump("loc_48CA")

    label("loc_47F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_48C1")

    ChrTalk(
        0xB,
        (
            "The CGF men are doing\x01",
            "their best with survival\x01",
            "training again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just went to observe them, and by\x01",
            "the looks of things, it seems they're\x01",
            "really back. Well, I'm really glad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_48C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48CA")

    label("loc_48CA")

    TalkEnd(0xFE)
    Return()

    # Function_11_4372 end

    def Function_12_48CE(): pass

    label("Function_12_48CE")

    Call(0, 13)
    Return()

    # Function_12_48CE end

    def Function_13_48D2(): pass

    label("Function_13_48D2")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D32")

    ChrTalk(
        0xC,
        (
            "Thank you for your hard\x01",
            "work, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you very much for\x01",
            "coming all the way here\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_END)), "loc_49A4")

    ChrTalk(
        0x101,
        (
            "#00000FAh, no...\x02\x03",
            "#00003FIt seems you'll be\x01",
            "working here for a\x01",
            "while...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F3")

    label("loc_49A4")


    ChrTalk(
        0x101,
        (
            "#00000FAh, no...\x02\x03",
            "#00003FYou came to work at the\x01",
            "police academy, Rebecca?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F3")


    ChrTalk(
        0xC,
        (
            "Yes. After all, the police\x01",
            "HQ reception desk is still\x01",
            "unserviceable at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fortunately there was a\x01",
            "data backup in these\x01",
            "terminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By using them, I was\x01",
            "able to resume\x01",
            "operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyone, whenever you need\x01",
            "something at the reception\x01",
            "desk, please speak with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI see. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUmm, Rebecca.\x02\x03",
            "#10104FI really want to thank\x01",
            "you for being there for\x01",
            "Fran when she woke up.\x02\x03",
            "#10109FShe was very happy too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        "No, don't say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, even though I should have been\x01",
            "encouraging her, conversely I was the\x01",
            "one who ended up getting encouraged...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, I am really\x01",
            "glad she's regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYes, really.\x02\x03",
            "#10100FIf you would like, could\x01",
            "you please go visit her\x01",
            "again sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, I would be glad to.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 5)
    TalkEnd(0xC)
    Return()

    label("loc_4D32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_50E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E8")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "My, everyone, that thing\x01",
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
            "#00005FUmm, you mean this?\x02\x03",
            "#00000FWe thought it was something good when\x01",
            "we got it, but until now we couldn't\x01",
            "figure out any way to use it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the\x01",
            "fragment to Rebecca.\x07\x00\x02",
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
            "damaged memory quartz data. The\x01",
            "forensics people were looking for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have that, it should be\x01",
            "possible to analyze a portion\x01",
            "of the cult's terminal data.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F85")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4F85")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FAE")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4FAE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD7")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4FD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FFD")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_4FFD")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FT-Then... We'll be able to\x01",
            "read the parts obscured by\x01",
            "Joachim Gｸnther...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes. Only a portion of\x01",
            "it though, it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think we'll have immediate\x01",
            "results, so, may I send this\x01",
            ""fragment" to forensics?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    TalkEnd(0xC)
    Return()

    label("loc_50E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5262")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x0, 5)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5179")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Show Combat Notebook\x01",          # 1
            "Check Cult Terminal Data\x01",      # 2
            "Hand Over Fragments\x01",           # 3
            "Cancel\x01",                        # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_51D8")

    label("loc_5179")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Show Combat Notebook\x01",          # 1
            "Check Cult Terminal Data\x01",      # 2
            "Cancel\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51D8")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5206")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)
    Jump("loc_525D")

    label("loc_5206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_522A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)
    Call(0, 23)
    Jump("loc_525D")

    label("loc_522A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 17)
    Jump("loc_525D")

    label("loc_524B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_525D")
    Call(0, 16)

    label("loc_525D")

    Jump("loc_50F2")

    label("loc_5262")

    TalkEnd(0xC)
    OP_93(0xC, 0x5A, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    Return()

    # Function_13_48D2 end

    def Function_14_5273(): pass

    label("Function_14_5273")


    ChrTalk(
        0xC,
        (
            "In any event... I'm\x01",
            "really glad that Fran has\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We too must do our best\x01",
            "even just to cheer her\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_14_5273 end

    def Function_15_52F7(): pass

    label("Function_15_52F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_5305")
    SetScenarioFlags(0x0, 5)

    label("loc_5305")

    Return()

    # Function_15_52F7 end

    def Function_16_5306(): pass

    label("Function_16_5306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_5390")

    ChrTalk(
        0xC,
        (
            "My, you've brought me a\x01",
            ""fragment".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order to analyze the cult\x01",
            "terminal data, do you mind\x01",
            "if I send it to forensics?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5390")


    ChrTalk(
        0x101,
        "#00000FYes, please go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, please wait a\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_53E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7321")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_731C")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5471")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5471")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D5")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_54D5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5537")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5537")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5599")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5599")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ECA")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 4 decrypted!\x07\x00\x02",
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
            "No. 1 Information Terminal\x01",
            "Data: "About The Cult"\x01",
            "completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 1 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5P...About this data... It\x01",
            "appears it is an entry\x01",
            "regarding the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PA creed that denies the\x01",
            "Goddess... It is really\x01",
            "unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes... However, it fits\x01",
            "with Joachim Gｸnther's\x01",
            "testimony.\x02\x03",
            "#00001FAlso, this word, D...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59CC")

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt's the word indicating the True\x01",
            "God they believed in instead of\x01",
            "the Goddess, right?\x02\x03",
            "#00201FWe've already ascertained that\x01",
            "the "G" in the D∴G Cult's name\x01",
            "stands for true wisdom, Gnosis...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5974")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm. We can now say\x01",
            "we've finally confirmed\x01",
            "the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59C7")

    label("loc_5974")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm. We can now say\x01",
            "we've finally confirmed\x01",
            "the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C7")

    Jump("loc_5AEE")

    label("loc_59CC")


    ChrTalk(
        0x103,
        (
            "#12P#00200FIt's the word indicating the True\x01",
            "God they believed in instead of\x01",
            "the Goddess, right?\x02\x03",
            "#00201FWe've already ascertained that\x01",
            "the "G" in the D∴G Cult's name\x01",
            "stands for true wisdom, Gnosis...\x02\x03",
            "With this, it seems we can now\x01",
            "say we've finally confirmed the\x01",
            "meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AEE")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut... I'm sure that Professor\x01",
            "Joachim referred to KeA as the\x01",
            "one who would become a "God".\x02\x03",
            "Then, "D" could be also a word\x01",
            "to indicate KeA, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C0C")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Gｸnther... How\x01",
            "much did he know...?\x02\x03",
            "...We can't figure it\x01",
            "out with just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D03")

    label("loc_5C0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C9C")

    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F...We can't figure it\x01",
            "out with just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D03")

    label("loc_5C9C")


    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...?\x02\x03",
            "With just this, we still\x01",
            "don't know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D03")


    ChrTalk(
        0x101,
        (
            "#12P#00001FIt also seems that even\x01",
            "Ernest didn't get the whole\x01",
            "story from Joachim...\x02\x03",
            "#00003FIf we could have arrested\x01",
            "him... I just keep thinking\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E1B")

    ChrTalk(
        0xC,
        (
            "#5P...In any case, if we keep\x01",
            "decrypting the data like this, I\x01",
            "think we may learn many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ECA")

    label("loc_5E1B")


    ChrTalk(
        0xC,
        (
            "#5P...In any case, if we keep\x01",
            "decrypting the data like this, I\x01",
            "think we may learn many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_5ECA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5F2C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F98")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5F98")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FE")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 4 decrypted!\x07\x00\x02",
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
            "No. 2 Information Terminal\x01",
            "Data: "About Gnosis"\x01",
            "completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 2 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5P...About this data... It\x01",
            "appears the details of\x01",
            "that Gnosis are recorded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PA drug with the effect of increasing physical\x01",
            "abilities, responsiveness and furthermore, it\x01",
            "draws out one's latent abilities as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt even causes the phenomenon\x01",
            "called Demonize... It's a\x01",
            "drug full of mysteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FBecause the plant called Pleroma\x01",
            "Grass used as raw ingredient grows\x01",
            "in colonies in the Marshlands...\x02\x03",
            "It seems certain that Joachim went\x01",
            "there to collect his supply of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_640A")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data\x01",
            "there's a passage saying\x01",
            "that Gnosis...\x02\x03",
            "is a drug needed to\x01",
            "revive their so-called\x01",
            "True God "D".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FHonestly, what I'm\x01",
            "hearing is complete\x01",
            "nonsense, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64CE")

    label("loc_640A")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data\x01",
            "there's a passage saying\x01",
            "that Gnosis...\x02\x03",
            "is a drug needed to\x01",
            "revive their so-called\x01",
            "True God "D".\x02\x03",
            "#00108FHonestly, what I'm\x01",
            "hearing is complete\x01",
            "nonsense, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64CE")


    ChrTalk(
        0x103,
        (
            "#12P#00201FEven so, the Cult continued to\x01",
            "research Gnosis with its "rituals"\x01",
            "over the span of even 500 years...\x02\x03",
            "#00203F...I was fortunate to be saved by\x01",
            "Guy, but there were a large number\x01",
            "of victims over those many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FAnd he referred to them\x01",
            "as "some sacrifices"...\x02\x03",
            "Those guys were really\x01",
            "beyond help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6674")

    ChrTalk(
        0x105,
        (
            "#12P#10403F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66B3")

    label("loc_6674")


    ChrTalk(
        0x105,
        (
            "#12P#10303F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B3")


    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah... Although the cult\x01",
            "disappeared, we might\x01",
            "still need to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_679B")

    label("loc_6712")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02\x03",
            "#00001FAlthough the cult\x01",
            "disappeared, we might\x01",
            "still need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_679B")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYes... Really.\x02\x03",
            "Not only Gnosis, we\x01",
            "police must keep drugs\x01",
            "like this under control.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6864")

    ChrTalk(
        0xC,
        "#5PYes, I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...I think this is all\x01",
            "regarding Gnosis for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_6864")


    ChrTalk(
        0xC,
        "#5PYes, I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...I think this is all\x01",
            "regarding Gnosis for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_68FE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_696A")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_696A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 3 decrypted!\x07\x00\x02",
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
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 3 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5PThis content... Is it\x01",
            "about KeA who you were\x01",
            "sheltering at the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FKeA was created by the Crois clan\x01",
            "500 years ago... She was presented\x01",
            "to the Cult as a religious figure.\x02\x03",
            "As the Divine Child, their God's\x01",
            "vessel, who continued to slumber\x01",
            "in a "Cradle"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...Even the Cult members\x01",
            "didn't know the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWithout even knowing that they were\x01",
            "manipulated in the shadows for the Crois\x01",
            "Clan's true goal, they kept looking for\x01",
            "a fantasy they called their True God...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D65")

    ChrTalk(
        0x106,
        (
            "#12P#10708F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DCE")

    label("loc_6D65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DA4")

    ChrTalk(
        0x109,
        (
            "#12P#10108F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DCE")

    label("loc_6DA4")


    ChrTalk(
        0x105,
        (
            "#12P#10408F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E2E")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they\x01",
            "did, I have no sympathy\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EE8")

    label("loc_6E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E92")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they\x01",
            "did, there is no room\x01",
            "for compassion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EE8")

    label("loc_6E92")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they\x01",
            "did, there is no room\x01",
            "for compassion, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EE8")


    ChrTalk(
        0x101,
        (
            "#12P#00001FPutting the cult aside, KeA\x01",
            "is completely innocent.\x02\x03",
            "#00003FEven if she is an existence\x01",
            "created for the Crois Clan's\x01",
            "goals...\x02\x03",
            "Even if she possesses\x01",
            "miraculous abilities... Those\x01",
            "things don't matter.\x02\x03",
            "That child who woke up before\x01",
            "our eyes was a genuine,\x01",
            "normal little girl.\x02\x03",
            "#00001FAnd yet, she was locked up\x01",
            "all alone in a place like\x01",
            "that for hundreds of years...\x02\x03",
            "And now, Mariabell and Lawyer\x01",
            "Ian are trying to use her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...No matter the\x01",
            "circumstances, like hell\x01",
            "we're gonna forgive 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...With this, the cult's\x01",
            "data has been completely\x01",
            "analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI don't know the detailed\x01",
            "circumstances of the incident\x01",
            "you are involved in, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI understand how\x01",
            "precious KeA is to you\x01",
            "all so much it hurts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PPlease...do your very\x01",
            "best. I will be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThanks, Rebecca.\x02\x03",
            "We'll bring KeA back with our\x01",
            "own hands.\x02\x03",
            "#00007FEven to create a future where\x01",
            "our precious KeA... When that\x01",
            "child can live smiling...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_72F7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_72F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7310")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7310")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)

    label("loc_731C")

    Jump("loc_53E1")

    label("loc_7321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7440")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "If you obtain any other\x01",
            ""fragments", please\x01",
            "bring them to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please also feel free to ask\x01",
            "me whenever you'd like to\x01",
            "check the decrypted data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7421")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7421")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_743A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_743A")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_7440")

    Return()

    # Function_16_5306 end

    def Function_17_7441(): pass

    label("Function_17_7441")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_744B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7546")
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
        (0, "loc_74F9"),
        (1, "loc_7507"),
        (2, "loc_7515"),
        (3, "loc_7523"),
        (SWITCH_DEFAULT, "loc_7532"),
    )


    label("loc_74F9")

    Sound(72, 0, 100, 0)
    Call(0, 18)
    Jump("loc_7541")

    label("loc_7507")

    Sound(72, 0, 100, 0)
    Call(0, 19)
    Jump("loc_7541")

    label("loc_7515")

    Sound(72, 0, 100, 0)
    Call(0, 20)
    Jump("loc_7541")

    label("loc_7523")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7541")

    label("loc_7532")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7541")

    label("loc_7541")

    Jump("loc_744B")

    label("loc_7546")

    Return()

    # Function_17_7441 end

    def Function_18_7547(): pass

    label("Function_18_7547")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01",
            "─My name is Joachim Gｸnther, High Priest of the "D∴G\x01",
            "Cult". Six years ago, our Cult was almost completely\x01",
            "destroyed due to the actions of many powers, the\x01",
            "bracers included. However, for certain reasons, only\x01",
            "I evaded harm and was able to escape safely to this\x01",
            "land of ■. I had survived in order to accomplish the\x01",
            "Cult's ambition thanks to the great ■'s guidance. For\x01",
            "when the time comes─ I have decided to record data in\x01",
            "each terminal as material for writin\x07\x00",
            "g new Testaments.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7972")

    label("loc_776E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01",
            "─My name is Joachim Gｸnther, High Priest of the "D∴G\x01",
            "Cult". Six years ago, our Cult was almost completely\x01",
            "destroyed due to the actions of many powers, the\x01",
            "bracers included. However, for certain reasons, only I\x01",
            "evaded harm and was able to escape safely to this land\x01",
            "of origin. I had survived in order to accomplish the\x01",
            "Cult's ambition thanks to the great D's guidance. For\x01",
            "when the time comes─ I have decided to record data in\x01",
            "each terminal as material for writin\x07\x00",
            "g new Testaments.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7972")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, I will speak of our Cult's origins. To do that,\x01",
            "I will need to look back at the annoying history this\x01",
            "Zemuria Continent has followed.  ─Approximately 1200\x01",
            "years ago, due to the Great Collapse, order and an\x01",
            "advanced civilization were lost,  and the Dark Ages\x01",
            "where war and poverty ruled, were brought forth. Then,\x01",
            "the weary people committed a grave error. Cajoled by\x01",
            "the words of imbeciles who had suddenly appeared, they\x01",
            "ended up accepting the selfish order they had invented.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D89")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words─ The foolish ■■ and the "■ of ■■", the\x01",
            "symbol of their faith. With their order, the Dark Ages\x01",
            "died, and that faith readily spread throughout the\x01",
            "continent... I want you to consider this carefully. If it\x01",
            "is true that a "■" exists, shouldn't she bestow equal\x01",
            "salvation to everyone? However, even to this very day, the\x01",
            "notion of inequity still exists and people never cease to\x01",
            "lose their lives due to disasters and misfortunes. So the\x01",
            ""■" chooses who to save? That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7FB4")

    label("loc_7D89")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words─ The foolish Septian Church and the\x01",
            ""Goddess of the Sky", the symbol of their faith. With\x01",
            "their order, the Dark Ages died, and that faith readily\x01",
            "spread throughout the continent... I want you to consider\x01",
            "this carefully. If it is true that a "Goddess" exists,\x01",
            "shouldn't she bestow equal salvation to everyone?\x01",
            "However, even to this very day, the notion of inequity\x01",
            "still exists and people never cease to lose their lives\x01",
            "due to disasters and misfortunes. So the "Goddess"\x01",
            "chooses who to save? That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7FB4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8174")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretense\x01",
            "in order for the "■■" to acquire power. There is no way\x01",
            "something like a "■" exists. Our predecessors, having\x01",
            "arrived at that truth, set out on a long journey in order\x01",
            "to meet a "■■".  Then, when the era changed to the Middle\x01",
            "Ages, they finally found it. ■■■■, ■■■■■■■ lying in the\x01",
            "depths of this land... "■"─ That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8358")

    label("loc_8174")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretense in\x01",
            "order for the "Septian Church" to acquire power. There is no\x01",
            "way something like a "Goddess" exists. Our predecessors,\x01",
            "having arrived at that truth, set out on a long journey in\x01",
            "order to meet a "True God".  Then, when the era changed to\x01",
            "the Middle Ages, they finally found it. A long-asleep\x01",
            "existence, harboring a great power in its body, lying in the\x01",
            "depths of this land... "D"─ That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8358")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_18_7547 end

    def Function_19_836C(): pass

    label("Function_19_836C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8525")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01",
            "Gnosis... It is a secret drug which uses Pleroma Grass as\x01",
            "an ingredient, a ■■ said to ■■■■. As for its mixing method,\x01",
            "■■■■■■■. By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of drawing out\x01",
            "the user's latent abilities. ■■■■■■■■■. ■■■■■■■■■. "Gnosis"\x01",
            "is a drug to ■ the ■'s \x07\x00",
            "■ with "■"'s ■.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_86E1")

    label("loc_8525")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01",
            "Gnosis... It is a secret drug which uses Pleroma Grass\x01",
            "as an ingredient, a legendary plant said to bloom atop\x01",
            "septium veins. As for its mixing method, it goes along\x01",
            "with "D". By taking it, physical ability and\x01",
            "responsiveness increase, and furthermore, it has the\x01",
            "effect of drawing out the user's latent abilities.\x01",
            "However, that is only the beginning. "Gnosis" is a\x01",
            "drug to link the user's mind wit\x07\x00",
            "h "D"'s spirit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_86E1")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8863")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy ■ with the ■'s ■, "■" is able to store ■ and ■.\x01",
            "Sooner or later, when that ■ leads to ■, "■" will ■■■■.\x01",
            "Furthermore, there was room for improvement in "Gnosis".\x01",
            "■■■■■■■■■■■■■, it is ■■■■■■ to "■".  ■■■■■ since then,\x01",
            "our Cult has researched a far more effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8A2E")

    label("loc_8863")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy unifying with the user's mind, "D" is able to store\x01",
            "knowledge and grow. Sooner or later, when that knowledge\x01",
            "leads to wisdom, "D" will revive. Furthermore, there was\x01",
            "room for improvement in "Gnosis". When the user's\x01",
            "abilities are forced to the limit and drawn out, it is\x01",
            "possible to supply far more knowledge to "D". In the 500\x01",
            "years since then, our Cult has researched a far more\x01",
            "effective "Gnosis"... And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8A2E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8BCA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a ■■ to ■ we ■■■■■■■, we were close to\x01",
            "perfecting "Gnosis", but a miscalculation arose.\x01",
            "Because the experiments were on a large scale, bracers\x01",
            "and other authorities smelled our existence. That was\x01",
            "connected to the destruction of all lodges as well as\x01",
            "the Cult itself. What foolishness, I say. For our "■■"\x01",
            "to ■■■■, some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8D6D")

    label("loc_8BCA")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a speed incomparable to when we started 500\x01",
            "years ago, we were close to perfecting "Gnosis", but\x01",
            "a miscalculation arose.  Because the experiments\x01",
            "were on a large scale, bracers and other authorities\x01",
            "smelled our existence. That was connected to the\x01",
            "destruction of all lodges as well as the Cult\x01",
            "itself. What foolishness, I say. For our "True God"\x01",
            "to revive, some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8D6D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F56")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly recovered the\x01",
            "experimental data and came to this land of ■, Crossbell.\x01",
            "As for the "Pleroma Grass" which is a "Gnosis" ingredient,\x01",
            "since it ■ in the ■■ in the ■■ of ■, I had no ■ problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is a\x01",
            "research facility ■ by ■■■ and it is furnished with much\x01",
            "high-tech equipment. Thus, blessed with such a research\x01",
            "environment, I finally completed the secret drug─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_9161")

    label("loc_8F56")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly recovered the\x01",
            "experimental data and came to this land of origin,\x01",
            "Crossbell. As for the "Pleroma Grass" which is a "Gnosis"\x01",
            "ingredient, since it grows in the Marshlands in the southern\x01",
            "part of Crossbell, I had no supply problems. Also, in the\x01",
            "depths of this "Fort of Sun", there is a research facility\x01",
            "built by Middles Ages alchemists and it is furnished with\x01",
            "much high-tech equipment. Thus, blessed with such a research\x01",
            "environment, I finally completed the secret drug─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_9161")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_19_836C end

    def Function_20_9175(): pass

    label("Function_20_9175")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_92F7")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01",
            "Crossbell is considered by our D∴G Cult to be our ■\x01",
            "and ■■■. The ■ is because it is the place where the\x01",
            "Divine Child ■■■■■. ■■■ of the "■■", the Divine\x01",
            "Child is a ■■■■ D∴G Cult. ■■■■■ Fort of Sun■,\x01",
            "■■■■■■■■■. ■■ ■■■■■■■■■■\x07\x00",
            " ■■■■■■ Fort of Sun■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_94E8")

    label("loc_92F7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01",
            "Crossbell is considered by our D∴G Cult to be our HQ and\x01",
            "land of origin. The reason is because it is the place\x01",
            "where the Divine Child was inherited by our founders. As\x01",
            "the vessel of the True God, the Divine Child is a symbolic\x01",
            "existence for our D∴G Cult. Continuing to sleep in the\x01",
            "Fort of Sun's basement, it has the aspect of a young human\x01",
            "maiden. She is said to be waiting for the moment of her\x01",
            "awakening at the altar of the F\x07\x00",
            "ort of Sun for 500 years.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_94E8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9668")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a ■ to be able to ■■■■... It is hard to believe\x01",
            "she is a being of this world. However, I really saw\x01",
            "her with my eyes. A ■■■■■■■■ ■■ a ■ called the "■■"─\x01",
            "I saw her ■■.  As for the "■■", it is an "Artifact"\x01",
            "which the ■■, based on the ■■ they were ■, ■. In this\x01",
            "case, even ■■■■ ■■■■, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_9841")

    label("loc_9668")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a human to be able to live that long... It is hard to\x01",
            "believe she is a being of this world. However, I really saw\x01",
            "her with my eyes. A young girl who continues sleeping like\x01",
            "she is dozing inside a globe called the "Divine Cradle"─ I\x01",
            "saw her divine figure. As for the "Divine Cradle", it is an\x01",
            ""Artifact" which the cult predecessors, based on alchemy\x01",
            "skills they were researching, made. In this case, it is\x01",
            "only natural to call this phenomenon a wonder.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_9841")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99CA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe Divine Child ■■■■■ ■■■■■■■■■■■ ■ Gnosis since\x01",
            "■■■■■. ──When she ■ "■", the Divine Child will ■■, and\x01",
            "she will ■ "■", the ■■. Then, ■■'s ■ and ■ will be ■ in\x01",
            ""■" and each person will be released from the spell of\x01",
            "the "■"  This is the prophecy our D∴G Cult predecessors\x01",
            "left to us and the ambition we must fulfill─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_9BB2")

    label("loc_99CA")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe Divine Child is regarded to have accumulated in her body\x01",
            "what could be said to be infinite knowledge through Gnosis\x01",
            "since the era she was born.  ─When she obtains "wisdom", the\x01",
            "Divine Child will wake up, and she will become "D", the True\x01",
            "God. Then, all people's wills and souls will be consolidated\x01",
            "in "D" and each person will be released from the spell of\x01",
            "the "Goddess".  This is the prophecy our D∴G Cult\x01",
            "predecessors left to us and the ambition we must fulfill─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_9BB2")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_20_9175 end

    def Function_21_9BC6(): pass

    label("Function_21_9BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BEB")
    SetChrPos(0xFE, 3220, 0, 12810, 0)
    Jump("loc_9C9F")

    label("loc_9BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C10")
    SetChrPos(0xFE, 2220, 0, 12400, 0)
    Jump("loc_9C9F")

    label("loc_9C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C35")
    SetChrPos(0xFE, 4050, 0, 12360, 0)
    Jump("loc_9C9F")

    label("loc_9C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5A")
    SetChrPos(0xFE, 3080, 0, 11680, 0)
    Jump("loc_9C9F")

    label("loc_9C5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C7F")
    SetChrPos(0xFE, 2430, 0, 10480, 0)
    Jump("loc_9C9F")

    label("loc_9C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C9F")
    SetChrPos(0xFE, 3790, 0, 10440, 0)

    label("loc_9C9F")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_9BC6 end

    def Function_22_9CAE(): pass

    label("Function_22_9CAE")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CCE")
    BeginChrThread(0x101, 1, 0, 21)

    label("loc_9CCE")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CE5")
    BeginChrThread(0x102, 1, 0, 21)

    label("loc_9CE5")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CFC")
    BeginChrThread(0x103, 1, 0, 21)

    label("loc_9CFC")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D13")
    BeginChrThread(0x104, 1, 0, 21)

    label("loc_9D13")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D2A")
    BeginChrThread(0x109, 1, 0, 21)

    label("loc_9D2A")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D41")
    BeginChrThread(0x105, 1, 0, 21)

    label("loc_9D41")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D58")
    BeginChrThread(0x106, 1, 0, 21)

    label("loc_9D58")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D6F")
    BeginChrThread(0x10A, 1, 0, 21)

    label("loc_9D6F")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9D89")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9D89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DA2")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_9DA2")

    Return()

    # Function_22_9CAE end

    def Function_23_9DA3(): pass

    label("Function_23_9DA3")

    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FD9")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DF5")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9DF5")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E29")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9E29")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E5D")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9E5D")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E91")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9E91")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC5")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9EC5")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EF9")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9EF9")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F2D")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9F2D")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F61")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FD4")

    label("loc_9F61")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F98")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jump("loc_9FD4")

    label("loc_9F98")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FCF")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    Jump("loc_9FD4")

    label("loc_9FCF")

    Jump("loc_9FD9")

    label("loc_9FD4")

    Jump("loc_9DB6")

    label("loc_9FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A945")
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
            "Oh, everyone... It looks\x01",
            "like you have filled in the\x01",
            "Combat Notebook quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since I would like to taken\x01",
            "down the monster information,\x01",
            "may I have a look at it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, please do.\x02",
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
            "I'll return your\x01",
            "notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is your\x01",
            "compensation this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A200")

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
    Jump("loc_A502")

    label("loc_A200")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A256")

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
    Jump("loc_A502")

    label("loc_A256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2AC")

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
    Jump("loc_A502")

    label("loc_A2AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A302")

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
    Jump("loc_A502")

    label("loc_A302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A358")

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
    Jump("loc_A502")

    label("loc_A358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3AE")

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
    Jump("loc_A502")

    label("loc_A3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A404")

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
    Jump("loc_A502")

    label("loc_A404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45A")

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
    Jump("loc_A502")

    label("loc_A45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4B0")

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
    Jump("loc_A502")

    label("loc_A4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A502")

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

    label("loc_A502")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A538")
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
    Jump("loc_A565")

    label("loc_A538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A565")
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

    label("loc_A565")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A67E")

    ChrTalk(
        0xC,
        (
            "また魔獣の情報が集まったら\x01",
            "立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, we will.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A612")

    ChrTalk(
        0x102,
        "#12P#0100FWe'll come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A679")

    label("loc_A612")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A648")

    ChrTalk(
        0x103,
        "#12P#0200FWe'll come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A679")

    label("loc_A648")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A679")

    ChrTalk(
        0x104,
        "#12P#0300FWe'll come again!\x02",
    )

    CloseMessageWindow()

    label("loc_A679")

    Jump("loc_A8DD")

    label("loc_A67E")


    ChrTalk(
        0xC,
        (
            "It looks like you have gathered plenty\x01",
            "of new type monster information as\x01",
            "well. Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this, I think that our\x01",
            "security measures will become\x01",
            "even more perfect from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHaha...we're honored to\x01",
            "have been of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. We really are in\x01",
            "your debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And so, please allow me to give\x01",
            "you a special reward this time.\x01",
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
            "I will pray for your\x01",
            "success from now on as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you need anything\x01",
            "else, please visit me\x01",
            "again whenever you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8DD")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_A8F4")
    ClearScenarioFlags(0x0, 6)

    label("loc_A8F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A90D")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_A90D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A926")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_A926")

    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2470, 0, 12690, 0)
    EventEnd(0x5)
    TalkBegin(0xC)
    Jump("loc_AAD3")

    label("loc_A945")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA1D")

    ChrTalk(
        0xC,
        (
            "Since I think we already have\x01",
            "enough information at HQ, let\x01",
            "us end the investigation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I may need your assistance again\x01",
            "in the future. I will be counting\x01",
            "on you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAD3")

    label("loc_AA1D")


    ChrTalk(
        0xC,
        (
            "It looks like you've\x01",
            "been collecting Combat\x01",
            "Notebook information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When you have gathered a little more\x01",
            "information, please show it to me. I\x01",
            "will take down the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD3")

    Return()

    # Function_23_9DA3 end

    def Function_24_AAD4(): pass

    label("Function_24_AAD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABF5")

    ChrTalk(
        0xFE,
        "Oh, Sergei's kids, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I've been entrusted\x01",
            "with guarding the police academy\x01",
            "area due to lack of manpower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while since I was a site\x01",
            "commander, but I've got to do it somehow, even\x01",
            "if just for the sake of the young officers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_ACBD")

    label("loc_ABF5")


    ChrTalk(
        0xFE,
        (
            "After I became Section Chief\x01",
            "of the Patrol Division, I did\x01",
            "a lot of desk work, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's an abnormal situation,\x01",
            "I've got to do it somehow, even if\x01",
            "just for the young officers' sake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACBD")

    TalkEnd(0xFE)
    Return()

    # Function_24_AAD4 end

    def Function_25_ACC1(): pass

    label("Function_25_ACC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AEFE")
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE69")

    ChrTalk(
        0xE,
        (
            "As expected, unrest is\x01",
            "spreading among the\x01",
            "trainees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even the citizens who happened to be here for\x01",
            "driving instruction want to return to the city\x01",
            "after hearing that the barrier has vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. I might've been\x01",
            "impatient in dealing\x01",
            "with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "All right, the\x01",
            "policewomen and I will\x01",
            "deal with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You all, continue to be\x01",
            "on the lookout as you\x01",
            "have been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_AEFA")

    label("loc_AE69")


    ChrTalk(
        0xD,
        (
            "The policewomen and I will\x01",
            "deal with the trainees and\x01",
            "the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You all, continue to be\x01",
            "on the lookout as you\x01",
            "have been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sir!\x02",
    )

    CloseMessageWindow()

    label("loc_AEFA")

    OP_4C(0xD, 0xFF)

    label("loc_AEFE")

    TalkEnd(0xFE)
    Return()

    # Function_25_ACC1 end

    def Function_26_AF02(): pass

    label("Function_26_AF02")

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

    def lambda_B039():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_B039)
    Sleep(50)

    def lambda_B049():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B049)
    Sleep(50)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B267")

    ChrTalk(
        0xF,
        "#01005F#5POh, you're finally here.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_B0A6():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B0A6)
    Sleep(0)

    def lambda_B0BE():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B0BE)
    Sleep(0)

    def lambda_B0D6():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B0D6)
    Sleep(0)

    def lambda_B0EE():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B0EE)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Sgt. Noｱl. It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PWe just arrived. Sorry\x01",
            "for being late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01000F#5PYeah, I heard. Looks\x01",
            "like you helped stop a\x01",
            "reckless driver.\x02\x03",
            "#01004FWell, that being the\x01",
            "case, I'll overlook your\x01",
            "lateness. ...Nice work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PThanks Chief.\x02\x03",
            "#00002FAlso, Manager Juan, it's\x01",
            "been a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B392")

    label("loc_B267")


    ChrTalk(
        0xF,
        (
            "#01005F#5POh, you're finally here,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_B2AA():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B2AA)
    Sleep(0)

    def lambda_B2C2():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B2C2)
    Sleep(0)

    def lambda_B2DA():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B2DA)
    Sleep(0)

    def lambda_B2F2():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B2F2)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Sgt. Noｱl. It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PWe just arrived.\x02\x03",
            "#00002FManager Juan, good to\x01",
            "see you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B392")


    ChrTalk(
        0x109,
        "#10109F#12PYou look well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNoｱl, I haven't seen you\x01",
            "since your regular\x01",
            "training a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd it's about 10 months\x01",
            "since you graduated,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPeople sure do change if\x01",
            "you take your eyes off\x01",
            "them for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha... I'm still a\x01",
            "novice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PI guess he's in charge\x01",
            "of this academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004F#5PYeah. This is Manager Juan,\x01",
            "in charge of this academy\x01",
            "and all related facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, no. I'm not all that\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#6PWell then Sergei. Feel\x01",
            "free to use the meeting\x01",
            "room.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "#01002F#11PWe'll do just that.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 27)
    Sleep(3000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01003F#5P─Well then. Time is\x01",
            "short.\x02\x03",
            "#01000FFollow me. We're\x01",
            "starting.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1280, 1000, 9280, 1500)
    OP_93(0xF, 0x5A, 0x1F4)

    def lambda_B678():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B678)

    def lambda_B68D():

        label("loc_B68D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_B68D")

    QueueWorkItem2(0x101, 2, lambda_B68D)

    def lambda_B69F():

        label("loc_B69F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_B69F")

    QueueWorkItem2(0x102, 2, lambda_B69F)

    def lambda_B6B1():

        label("loc_B6B1")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_B6B1")

    QueueWorkItem2(0x109, 2, lambda_B6B1)

    def lambda_B6C3():

        label("loc_B6C3")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_B6C3")

    QueueWorkItem2(0x105, 2, lambda_B6C3)
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
            "#00001F#6PUmm... What exactly are\x01",
            "we doing today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01005F#11PWhat, you haven't\x01",
            "realized it yet?\x02\x03",
            "#01004FThere were plenty of\x01",
            "hints. Heh heh, I guess\x01",
            "you guys are still green.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PUgh... P-Please wait!\x02\x03",
            "#00003FPlenty of hints.. The\x01",
            "reason you called us\x01",
            "here...\x02\x03",
            "#00000FCould it be─\x02",
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
            "#1KThe reason Sergei called\x01",
            "you here?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Detective Exam Training]\x01",            # 0
            "[Rules of the Road Training]\x01",         # 1
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
        (0, "loc_B947"),
        (1, "loc_BA50"),
        (2, "loc_BAFF"),
        (SWITCH_DEFAULT, "loc_BBF5"),
    )


    label("loc_B947")


    ChrTalk(
        0xF,
        (
            "#01006F#11PYou already have the\x01",
            "detective qualification.\x02\x03",
            "#01003FBecause of the nature of\x01",
            "the SSS, there's no need\x01",
            "for all members to have it.\x02\x03",
            "#01000FThe answer is─ "Rules of\x01",
            "the Road Training".\x02",
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
        "#00102F#12PThen... Could it be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBF5")

    label("loc_BA50")

    OP_2C(0xA1, 0x1)

    ChrTalk(
        0x101,
        (
            "#00002F#6PI see... It's "Rules of\x01",
            "the Road Training",\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01004F#11PHehe, right answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PUmm... Could that be\x01",
            "it...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBF5")

    label("loc_BAFF")


    ChrTalk(
        0xF,
        (
            "#01003F#11PThe orbal net is here too,\x01",
            "but...\x02\x03",
            "If you were going to be\x01",
            "doing that, I'd have you go\x01",
            "to the foundation office.\x02\x03",
            "#01000FThe answer is─ "Rules of\x01",
            "the Road Training".\x02",
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
        "#00102F#12PThen... Could it be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBF5")

    label("loc_BBF5")


    ChrTalk(
        0xF,
        (
            "#01004F#11PYeah. The Special Support\x01",
            "Section has been issued a\x01",
            "car.\x02\x03",
            "#01002FI'm taking this opportunity\x01",
            "to drive the rules of the\x01",
            "road into your heads.\x02",
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
            "#01003F#5P─That'll be all. That's the bare\x01",
            "minimum you need to know if you're\x01",
            "going to be driving an orbal car.\x02\x03",
            "#01000FDid I manage to drill it into your\x01",
            "heads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI-I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PMan, to think a lesson\x01",
            "was waiting for us in a\x01",
            "place like this...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C0B8")

    ChrTalk(
        0x102,
        (
            "#00100F#6P...But the rules are simpler than\x01",
            "I thought.\x02\x03",
            "#00103FThough, like in that reckless\x01",
            "driving incident, there are weak\x01",
            "penalties for foreigners...\x02\x03",
            "#00101FIn the future, when there are more\x01",
            "orbal cars on the road, I feel\x01",
            "just those won't be enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat's a future issue.\x02\x03",
            "#01001FIt hasn't even been 10\x01",
            "years since personal orbal\x01",
            "cars were introduced.\x02\x03",
            "In time, stricter rules\x01",
            "will be pursued.\x02\x03",
            "Even regarding penalties\x01",
            "for foreigners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1FC")

    label("loc_C0B8")


    ChrTalk(
        0x102,
        (
            "#00103F#6P...But the rules are simpler than\x01",
            "I thought.\x02\x03",
            "#00101FIn the future, when there are more\x01",
            "orbal cars on the road, I feel\x01",
            "just those won't be enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat's a future issue.\x02\x03",
            "#01001FIt hasn't even been 10\x01",
            "years since personal orbal\x01",
            "cars were introduced.\x02\x03",
            "In time, stricter rules\x01",
            "will be pursued.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1FC")


    ChrTalk(
        0x109,
        (
            "#10103F#11PIf you apply at City Hall,\x01",
            "you can be easily issued a\x01",
            "driver's license.\x02\x03",
            "#10101FBut, can't they consider\x01",
            "introducing some kind of\x01",
            "test?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5PYeah, in the future, all sorts\x01",
            "of trainings will be added,\x01",
            "and a practical exam, too.\x02\x03",
            "#01000FIn any case, just remember the\x01",
            "basic rules for today.\x02\x03",
            "As for the actual driving...\x01",
            "Noｱl, you do it.\x02",
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
            "#00109F#6PAfter all, she drives\x01",
            "those CGF armored cars\x01",
            "so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6PWow, really?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha... The Commander\x01",
            "made me learn when I\x01",
            "joined the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5PAll right then. I'll\x01",
            "issue your orbal car\x01",
            "immediately.\x02\x03",
            "#01000FIt's parked outside, so\x01",
            "follow me.\x02",
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
            "#00012F#5PHaha, this is quite a\x01",
            "surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PYes. Chief is one tough\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PAn orbal car, huh.\x02\x03",
            "#10300FI don't know much about them,\x01",
            "but I wonder if we're getting\x01",
            "a Reinford or Verne Co. model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PYes, when it comes personal\x01",
            "cars, those two are the\x01",
            "only big manufacturers.\x02\x03",
            "#10102FVerne Co. has been in\x01",
            "business longer, and has a\x01",
            "wide selection.\x02\x03",
            "Small cars, midrange ones\x01",
            "and even buses are all\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PAnd Reinford has lots of\x01",
            "trucks and limousines,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PYes, if I had to say, many of\x01",
            "their products are sturdy and\x01",
            "high quality.\x02\x03",
            "#10100FIt seems like a lot of their\x01",
            "tech was originally developed\x01",
            "for orbal trains and tanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PHmm... I wasn't really\x01",
            "feeling it before but\x01",
            "now I'm excited.\x02\x03",
            "#00000FAlright, let's check it\x01",
            "out.\x02",
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

    # Function_26_AF02 end

    def Function_27_C8D1(): pass

    label("Function_27_C8D1")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -3000, 0, 13250, 2000, 0x0)
    OP_95(0xFE, -6500, 0, 13250, 2000, 0x0)
    Return()

    # Function_27_C8D1 end

    def Function_28_C901(): pass

    label("Function_28_C901")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 61500, 0, 18500, 2500, 0x0)
    OP_95(0xFE, 61500, 0, 6500, 2500, 0x0)
    Return()

    # Function_28_C901 end

    def Function_29_C931(): pass

    label("Function_29_C931")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D19F")

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
            "Well, I'm glad you're\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FManager Juan...\x01",
            "Likewise, we're glad\x01",
            "you're safe too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FThe CGF are here, aren't\x01",
            "they.\x02\x03",
            "#00103FWasn't the State Guard\x01",
            "in charge of this place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. With the news\x01",
            "President's arrest, they\x01",
            "withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The State Guard needs to do their\x01",
            "best to quell disturbances throughout\x01",
            "the state for us, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Reinforcements from police HQ\x01",
            "came to replace them and get\x01",
            "this place under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FBy the way... What\x01",
            "happened to ol' man\x01",
            "Garcｵa in the end?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCB2")

    ChrTalk(
        0x105,
        (
            "#12P#10402FWhen you escaped from\x01",
            "prison, he helped you\x01",
            "out, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD65")

    label("loc_CCB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD11")

    ChrTalk(
        0x109,
        (
            "#12P#10100FWhen you escaped from\x01",
            "prison, he helped you\x01",
            "out, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD65")

    label("loc_CD11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD65")

    ChrTalk(
        0x106,
        (
            "#12P#10702FI heard he helped you\x01",
            "when you escaped from\x01",
            "prison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD65")


    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah... He really helped\x01",
            "me out a lot back then.\x02\x03",
            "#00006FWait. Maybe I shouldn't\x01",
            "say things like that in\x01",
            "a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, regarding your arrest,\x01",
            "with the President's arrest,\x01",
            "it was judged invalid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So regarding that point,\x01",
            "you shouldn't worry about\x01",
            "it at this late date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, about Garcｵa... He put up a\x01",
            "fight against the State Guard\x01",
            "and was arrested some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Currently, he is once\x01",
            "again imprisoned and\x01",
            "receiving treatment.\x02",
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
        "#12P#00205FTreatment, you say?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D043")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHe fought the State Guard\x01",
            "alone. He's probably\x01",
            "rather exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D106")

    label("loc_D043")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0A7")

    ChrTalk(
        0x106,
        (
            "#12P#10703FIf he fought the State\x01",
            "Guard alone... He's\x01",
            "probably exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D106")

    label("loc_D0A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D106")

    ChrTalk(
        0x109,
        (
            "#12P#10103FIf he fought the State\x01",
            "Guard alone... he's\x01",
            "probably exhausted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D106")


    ChrTalk(
        0x8,
        (
            "Yes, he won't be able to\x01",
            "walk for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, if you like,\x01",
            "it's possible to visit\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FLloyd, what do we do?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 1)
    Jump("loc_D21A")

    label("loc_D19F")


    ChrTalk(
        0x8,
        (
            "Garcｵa is once again\x01",
            "imprisoned and is currently\x01",
            "receiving treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you like, it's\x01",
            "possible to visit him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D21A")

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
            "Cancel\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D326")

    ChrTalk(
        0x101,
        (
            "#12P#00003F(I must thank Garcｵa for\x01",
            "back then...)\x02\x03",
            "#00000F...Manager Juan, if you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll have Melvin\x01",
            "guide you. Go with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Jump("loc_D39A")

    label("loc_D326")


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
            "Well, tell me whenever\x01",
            "you want if you wish to\x01",
            "visit him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D39A")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_C931 end

    def Function_30_D3CA(): pass

    label("Function_30_D3CA")


    ChrTalk(
        0x101,
        (
            "#12P#00003F(I must thank Garcｵa for\x01",
            "back then...)\x02\x03",
            "#00000F...Manager Juan, if you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll have Melvin\x01",
            "guide you. Go with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_D3CA end

    def Function_31_D475(): pass

    label("Function_31_D475")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business\x01",
            "on the other floors. Let's\x01",
            "not wander around too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_31_D475 end

    def Function_32_D4DE(): pass

    label("Function_32_D4DE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_32_D4DE end

    SaveToFile()

Try(main)
