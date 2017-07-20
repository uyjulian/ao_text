from ScenarioHelper import *

def main():
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
        "Secretary General Huang",           # 1
        "Trainee",                 # 2
        "Trainee",                 # 3
        "Instructor",                   # 4
        "Receptionist Rebecca",         # 5
        "Mr. Joe Ridge",       # 6
        "Policeman",                   # 7
        "Sergey Manager",           # 8
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
        "Function_5_17EA",         # 05, 5
        "Function_6_2CBE",         # 06, 6
        "Function_7_2E91",         # 07, 7
        "Function_8_305A",         # 08, 8
        "Function_9_3710",         # 09, 9
        "Function_10_3BA8",        # 0A, 10
        "Function_11_3E8F",        # 0B, 11
        "Function_12_42ED",        # 0C, 12
        "Function_13_42F1",        # 0D, 13
        "Function_14_4C58",        # 0E, 14
        "Function_15_4CE8",        # 0F, 15
        "Function_16_4CF7",        # 10, 16
        "Function_17_6CB8",        # 11, 17
        "Function_18_6DC3",        # 12, 18
        "Function_19_7926",        # 13, 19
        "Function_20_85F9",        # 14, 20
        "Function_21_8F6D",        # 15, 21
        "Function_22_9055",        # 16, 22
        "Function_23_914A",        # 17, 23
        "Function_24_9E58",        # 18, 24
        "Function_25_9FCB",        # 19, 25
        "Function_26_A197",        # 1A, 26
        "Function_27_BA5A",        # 1B, 27
        "Function_28_BA8A",        # 1C, 28
        "Function_29_BABA",        # 1D, 29
        "Function_30_C568",        # 1E, 30
        "Function_31_C636",        # 1F, 31
        "Function_32_C68A",        # 20, 32
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",              # 0
            "Pass unexpected dish\x01",      # 1
            "quit\x01",                # 2
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
    Jump("loc_17CF")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极苦面『断头』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CE")
    MenuCmd(1, 1, "Justice noodle ≪decapitation≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Call(0, 7)

    label("loc_6C4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('炼狱麻婆『阎魔』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_707")
    MenuCmd(1, 1, "Purgatory girl ≪Enma≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_6FD")
    Call(0, 7)

    label("loc_6FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('杂色锅巴饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73C")
    MenuCmd(1, 1, "Stir-fried rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_732")
    Call(0, 7)

    label("loc_732")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('顽固肉排『岩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_771")
    MenuCmd(1, 1, "Stubborn flesh ≪Iwao≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_767")
    Call(0, 7)

    label("loc_767")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('混沌久煮『浊』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AA")
    MenuCmd(1, 1, "Chaotic cooked ≪Hazy≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_7A0")
    Call(0, 7)

    label("loc_7A0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『山』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DF")
    MenuCmd(1, 1, "Men's cuisine ≪mountain≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_7D5")
    Call(0, 7)

    label("loc_7D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『川』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_814")
    MenuCmd(1, 1, "Men's cuisine ≪river≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_80A")
    Call(0, 7)

    label("loc_80A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('箭之鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84D")
    MenuCmd(1, 1, "Fish Arrow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_843")
    Call(0, 7)

    label("loc_843")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('激辣炸弹蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_884")
    MenuCmd(1, 1, "Spicy hot rice bowl")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_87A")
    Call(0, 7)

    label("loc_87A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('细针面', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB")
    MenuCmd(1, 1, "Needle pasta")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_8B1")
    Call(0, 7)

    label("loc_8B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦味汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F2")
    MenuCmd(1, 1, "Bitter burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_8E8")
    Call(0, 7)

    label("loc_8E8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四重番茄比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92D")
    MenuCmd(1, 1, "Quattro tomato pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_923")
    Call(0, 7)

    label("loc_923")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('守护三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_964")
    MenuCmd(1, 1, "Protect Sand")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_95A")
    Call(0, 7)

    label("loc_95A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('不可思议盒饭『仰天』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99F")
    MenuCmd(1, 1, "Wonderland lunch ≪Gaze≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_995")
    Call(0, 7)

    label("loc_995")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇妙汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D4")
    MenuCmd(1, 1, "Magica Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_9CA")
    Call(0, 7)

    label("loc_9CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘密棉花糖', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0F")
    MenuCmd(1, 1, "Enigma Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_A05")
    Call(0, 7)

    label("loc_A05")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('反射巧克力蛋糕', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A48")
    MenuCmd(1, 1, "Reflex Chocolat")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_A3E")
    Call(0, 7)

    label("loc_A3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('爽弹布丁', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7F")
    MenuCmd(1, 1, "Purple Pudding")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_A75")
    Call(0, 7)

    label("loc_A75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('痊愈冰激凌', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB6")
    MenuCmd(1, 1, "Recovery ice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_AAC")
    Call(0, 7)

    label("loc_AAC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('隐秘爆米花', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEF")
    MenuCmd(1, 1, "Covert popcorn")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_AE5")
    Call(0, 7)

    label("loc_AE5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('良药『熊竹』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B24")
    MenuCmd(1, 1, "Good drug ≪Kumasasa≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_B1A")
    Call(0, 7)

    label("loc_B1A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('紫色液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B5D")
    MenuCmd(1, 1, "Purple Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_B53")
    Call(0, 7)

    label("loc_B53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('褐色液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B96")
    MenuCmd(1, 1, "Brown Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_B8C")
    Call(0, 7)

    label("loc_B8C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('粉红液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCF")
    MenuCmd(1, 1, "Momoiro Liquid")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_BC5")
    Call(0, 7)

    label("loc_BC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BCF")

    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4F")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you, something that looks good again\x01",
            "I'm begging you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C0")

    label("loc_C4F")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极苦面『断头』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('极苦面『断头』', 1)
    SetScenarioFlags(0x20C, 0)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '极苦面『断头』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('炼狱麻婆『阎魔』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('炼狱麻婆『阎魔』', 1)
    SetScenarioFlags(0x20C, 1)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '炼狱麻婆『阎魔』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_D18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('杂色锅巴饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D72")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('杂色锅巴饭', 1)
    SetScenarioFlags(0x20C, 2)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '杂色锅巴饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_D72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('顽固肉排『岩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('顽固肉排『岩』', 1)
    SetScenarioFlags(0x20C, 3)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '顽固肉排『岩』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_DCC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('混沌久煮『浊』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E30")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E26")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('混沌久煮『浊』', 1)
    SetScenarioFlags(0x20C, 4)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '混沌久煮『浊』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_E26")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『山』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E80")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('男人料理『山』', 1)
    SetScenarioFlags(0x20C, 5)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '男人料理『山』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_E80")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('男人料理『川』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('男人料理『川』', 1)
    SetScenarioFlags(0x20C, 6)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '男人料理『川』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_EDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('箭之鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F34")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('箭之鱼', 1)
    SetScenarioFlags(0x20C, 7)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '箭之鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_F34")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('激辣炸弹蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F98")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('激辣炸弹蛋包饭', 1)
    SetScenarioFlags(0x20D, 0)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '激辣炸弹蛋包饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_F8E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('细针面', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('细针面', 1)
    SetScenarioFlags(0x20D, 1)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '细针面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_FE8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦味汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1042")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('苦味汉堡', 1)
    SetScenarioFlags(0x20D, 2)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '苦味汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_1042")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四重番茄比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('四重番茄比萨', 1)
    SetScenarioFlags(0x20D, 3)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '四重番茄比萨'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_109C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('守护三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1100")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('守护三明治', 1)
    SetScenarioFlags(0x20D, 4)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '守护三明治'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_10F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('不可思议盒饭『仰天』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1150")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('不可思议盒饭『仰天』', 1)
    SetScenarioFlags(0x20D, 5)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '不可思议盒饭『仰天』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_1150")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_115A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇妙汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11B4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('奇妙汤', 1)
    SetScenarioFlags(0x20D, 6)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '奇妙汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_11AA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘密棉花糖', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('秘密棉花糖', 1)
    SetScenarioFlags(0x20D, 7)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '秘密棉花糖'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_1204")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('反射巧克力蛋糕', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1268")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('反射巧克力蛋糕', 1)
    SetScenarioFlags(0x20E, 0)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '反射巧克力蛋糕'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_125E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('爽弹布丁', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('爽弹布丁', 1)
    SetScenarioFlags(0x20E, 1)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '爽弹布丁'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_12B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('痊愈冰激凌', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_131C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1312")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('痊愈冰激凌', 1)
    SetScenarioFlags(0x20E, 2)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '痊愈冰激凌'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_1312")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('隐秘爆米花', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1376")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('隐秘爆米花', 1)
    SetScenarioFlags(0x20E, 3)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '隐秘爆米花'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_136C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('良药『熊竹』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('良药『熊竹』', 1)
    SetScenarioFlags(0x20E, 4)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '良药『熊竹』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_13C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('紫色液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1420")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('紫色液体', 1)
    SetScenarioFlags(0x20E, 5)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '紫色液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_1420")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('褐色液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1484")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('褐色液体', 1)
    SetScenarioFlags(0x20E, 6)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '褐色液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_147A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('粉红液体', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('粉红液体', 1)
    SetScenarioFlags(0x20E, 7)

    AnonymousTalk(
        0xFF,
        (
            "To Hoang Secretary",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_14D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14DE")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B6")
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oops, a lot and much\x01",
            "Bring me an \"odd dish\"\x01",
            "You seem to have given it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If this is the case also the training of the judgment team\x01",
            "It should cover the time.\x01",
            "…… Thank you, I was really saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDo not mind, please.\x01",
            "It's not a big deal … ….\x02\x03",
            "Once for the role of the alma mater\x01",
            "It seems that it was set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd is a victorious … …\x01",
            "Yeah, that kind of place since I was a student\x01",
            "It has not changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right.\x01",
            "Will you bring this with me today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I recently started using it for training\x01",
            "It is a quartz for Enigma,\x01",
            "I have one extra piece of equipment.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '幻胧'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('幻胧', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThank you,\x01",
            "Secretary Huang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, here it is.\x01",
            "If there is something again, I will ask you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 1)
    TalkEnd(0x8)
    Return()

    label("loc_17B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C0")

    Jump("loc_67B")

    label("loc_17C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CF")

    Jump("loc_5DF")

    label("loc_17D4")

    Jump("loc_17E6")

    label("loc_17D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_17E6")

    TalkEnd(0x8)
    Return()

    # Function_4_5AD end

    def Function_5_17EA(): pass

    label("Function_5_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(
        0x8,
        (
            "The President was detained\x01",
            "The report was entered, the Defense Forces\x01",
            "I withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to get confused about each place,\x01",
            "The defense army has to work hard\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also\x01",
            "I hope to do what I can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1950")

    label("loc_18D4")


    ChrTalk(
        0x8,
        (
            "Now, the cheering team coming from the headquarters\x01",
            "We are confining the confusion around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also\x01",
            "I hope to do what I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1950")

    Jump("loc_2CBA")

    label("loc_1955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A32")

    ChrTalk(
        0x8,
        (
            "… … That raid incident,\x01",
            "It was too terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The site of this police school and\x01",
            "The young policemen were safe\x01",
            "I am fortunate enough but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the crossbell to completely recover\x01",
            "It looks like it will take more time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC3")

    label("loc_1A32")


    ChrTalk(
        0x8,
        (
            "… … In that raid incident,\x01",
            "The young policemen were safe\x01",
            "I am fortunate enough but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the crossbell to completely recover\x01",
            "It looks like it will take more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    Jump("loc_2CBA")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAB")

    ChrTalk(
        0x8,
        (
            "The gate which was destroyed yesterday,\x01",
            "To prepare for a new one\x01",
            "It's going to take a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No way, I do not think such a way to break\x01",
            "Because I did not expect it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For a while to the guard\x01",
            "I guess we have no choice but to ask for security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C30")

    label("loc_1BAB")


    ChrTalk(
        0x8,
        (
            "The gate which was destroyed yesterday,\x01",
            "To prepare for a new one\x01",
            "It's going to take a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For a while to the guard\x01",
            "I guess we have no choice but to ask for security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C30")

    Jump("loc_2CBA")

    label("loc_1C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E53")

    ChrTalk(
        0x8,
        "Oh, Lloyd the guys you like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A while ago in the premises\x01",
            "I heard a tremendous sound ……\x01",
            "What on earth was that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F…… In the meantime, the gate in front of the site\x01",
            "I confirmed that it was destroyed.\x01",
            "Perhaps, I think that sound.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "What? Is it?\x01",
            "That special alloy made gate ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is not it \"eidolon\" …?\x01",
            "I have power to that extent\x01",
            "Although it was not reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYet we also\x01",
            "I can not say anything ……\x02\x03",
            "The possibility of coming here\x01",
            "It should never be zero.\x01",
            "… … be adequate vigilance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, ah … you guys.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 0)
    Jump("loc_1EB5")

    label("loc_1E53")


    ChrTalk(
        0x8,
        (
            "We too, enough around us\x01",
            "Let's be wary of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "you guys……\x01",
            "Be wary of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB5")

    Jump("loc_2CBA")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F38")

    ChrTalk(
        0x8,
        (
            "Today in forest areas\x01",
            "It seems there is no sighting information of the eidolon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even hasten fighters, another place today\x01",
            "You seem to be investigating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CBA")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2043")

    ChrTalk(
        0x8,
        (
            "With \"Phantom Beast\"\x01",
            "Also in the Knox forest area\x01",
            "Have been witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lin, you called Eolia\x01",
            "Although the hypocrite was hit,\x01",
            "It seems that they did not get rid of after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That place is the exercise ground for the guard,\x01",
            "Given the future\x01",
            "It seems better to keep on caution.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20D7")

    label("loc_2043")


    ChrTalk(
        0x8,
        (
            "With \"Phantom Beast\"\x01",
            "Also in the Knox forest area\x01",
            "Have been witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard that he ran away somewhere ……\x01",
            "Given the future\x01",
            "It seems better to keep on caution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D7")

    Jump("loc_2CBA")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_226F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F6")

    ChrTalk(
        0x8,
        (
            "The police school curriculum,\x01",
            "It is done perfectly for half a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Schooling and training became the main,\x01",
            "After graduation according to reasonable\x01",
            "It is assigned to various departments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So to speak to police officers\x01",
            "Place to teach the first way of flying ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To work here,\x01",
            "I feel proud.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_226A")

    label("loc_21F6")


    ChrTalk(
        0x8,
        (
            "To police officers\x01",
            "Place to teach the first way of flying ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To work at this police school,\x01",
            "I feel proud.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226A")

    Jump("loc_2CBA")

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262E")

    ChrTalk(
        0x8,
        (
            "Douglas who became the deputy commander of the guard,\x01",
            "For a while, I was an instructor here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mainly teaching in charge of training,\x01",
            "I often looked at the exercise ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "It was a truly harsh person.\x02\x03",
            "#00008FOne person, one from another and training\x01",
            "That hell picture that drops out … …\x02\x03",
            "#00006FEven though I remember it now\x01",
            "Does not it stop trembling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that older brother\x01",
            "Impossible difficulty while laughing refreshed\x01",
            "It is because it is a type of thrust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, I was saying this\x01",
            "\"Douglas of demons\" It is a border border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FBut, from the guard's Hope\x01",
            "To learn battle techniques,\x01",
            "I am jealous.\x02\x03",
            "#10104FIf possible I am also a new era\x01",
            "I wanted to learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, I'm grateful.\x01",
            "What I was taught was a real battle\x01",
            "You have been useful many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In fact, including Lloyd\x01",
            "An excellent police officer thanks to him\x01",
            "Many people were produced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a police school, anything\x01",
            "It was a talent that I do not want to let go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, originally from the security guard,\x01",
            "Because it is the request of Sogna commander\x01",
            "It is unavoidable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 6)
    Jump("loc_26C3")

    label("loc_262E")


    ChrTalk(
        0x8,
        (
            "Douglas, as a police school,\x01",
            "I did not want to let go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, originally from the security guard,\x01",
            "Because it is the request of Sogna commander\x01",
            "It is unavoidable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C3")

    Jump("loc_2CBA")

    label("loc_26C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2973")

    ChrTalk(
        0x8,
        "Oh, are you those of the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I asked Sergei,\x01",
            "Every day the new type power guide car\x01",
            "You seem to be driving around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, yeah.\x01",
            "Extensive activities in the city\x01",
            "I am making use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, follow the traffic rules well\x01",
            "It is driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The police officer caused a traffic accident ……\x01",
            "How a laugh, it will not be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOh, I like that,\x01",
            "Accidents …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, Noel\x01",
            "Speed frenzy and so on\x01",
            "It will be different …\x02\x03",
            "#00304FAfter the driving car love passed,\x01",
            "Even narrowing my horizons\x01",
            "I wish I could be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, up to my seniors ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, we still\x01",
            "I did not get used to it completely ……\x01",
            "Let's keep it in mind for everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 5)
    Jump("loc_29F7")

    label("loc_2973")


    ChrTalk(
        0x8,
        (
            "If you drive a car,\x01",
            "I have to keep traffic rules well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The police officer caused a traffic accident ……\x01",
            "How a laugh, it will not be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F7")

    Jump("loc_2CBA")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3E")

    ChrTalk(
        0x8,
        "You guys seem to have finished the lesson.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is it the place of practical use at last?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, that is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHowever, that manager\x01",
            "To say that you can do a lecture,\x01",
            "It was pretty surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He said, at the police school\x01",
            "Vehicle driving instructor\x01",
            "Because I was concurrent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, it was easy to understand\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh, that's right.\x01",
            "I was saying before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FWell, Sergey manager also\x01",
            "It is quite a rich mystery.\x02\x03",
            "#10101FPersonally with Sonja command\x01",
            "I also care about relationships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, not much about yourself\x01",
            "Because it is a person who does not want to talk ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 5)
    Jump("loc_2CBA")

    label("loc_2C3E")


    ChrTalk(
        0x8,
        (
            "That's right, Sergei\x01",
            "Is not she waiting outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is not something that makes your boss wait so long.\x01",
            "Go ahead of time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBA")

    Call(0, 8)
    Return()

    # Function_5_17EA end

    def Function_6_2CBE(): pass

    label("Function_6_2CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_2CDB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_2CEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_2D01")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_2D14")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_2D27")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_2D3A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_2D4D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_2D60")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_2D73")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_2D86")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_2D99")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_2DAC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_2DBF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_2DD2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_2DE5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_2DF8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_2E0B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_2E1E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_2E31")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_2E44")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_2E57")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_2E6A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_2E7D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_2E90")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E90")

    Return()

    # Function_6_2CBE end

    def Function_7_2E91(): pass

    label("Function_7_2E91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA4")
    MenuCmd(3, 1, 0x0)

    label("loc_2EA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB7")
    MenuCmd(3, 1, 0x1)

    label("loc_2EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECA")
    MenuCmd(3, 1, 0x2)

    label("loc_2ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EDD")
    MenuCmd(3, 1, 0x3)

    label("loc_2EDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF0")
    MenuCmd(3, 1, 0x4)

    label("loc_2EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F03")
    MenuCmd(3, 1, 0x5)

    label("loc_2F03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F16")
    MenuCmd(3, 1, 0x6)

    label("loc_2F16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F29")
    MenuCmd(3, 1, 0x7)

    label("loc_2F29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3C")
    MenuCmd(3, 1, 0x8)

    label("loc_2F3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F4F")
    MenuCmd(3, 1, 0x9)

    label("loc_2F4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F62")
    MenuCmd(3, 1, 0xA)

    label("loc_2F62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F75")
    MenuCmd(3, 1, 0xB)

    label("loc_2F75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F88")
    MenuCmd(3, 1, 0xC)

    label("loc_2F88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9B")
    MenuCmd(3, 1, 0xD)

    label("loc_2F9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FAE")
    MenuCmd(3, 1, 0xE)

    label("loc_2FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC1")
    MenuCmd(3, 1, 0xF)

    label("loc_2FC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD4")
    MenuCmd(3, 1, 0x10)

    label("loc_2FD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE7")
    MenuCmd(3, 1, 0x11)

    label("loc_2FE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FFA")
    MenuCmd(3, 1, 0x12)

    label("loc_2FFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300D")
    MenuCmd(3, 1, 0x13)

    label("loc_300D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3020")
    MenuCmd(3, 1, 0x14)

    label("loc_3020")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3033")
    MenuCmd(3, 1, 0x15)

    label("loc_3033")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3046")
    MenuCmd(3, 1, 0x16)

    label("loc_3046")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3059")
    MenuCmd(3, 1, 0x17)

    label("loc_3059")

    Return()

    # Function_7_2E91 end

    def Function_8_305A(): pass

    label("Function_8_305A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370F")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "That's … … you guys,\x01",
            "Suddenly something \"strange food\"\x01",
            "Would you like to have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F\"Odd cooking\", is it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, in fact, I use it for the training of the judgment team\x01",
            "Look for samples.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is hard to guess the ingredients,\x01",
            "If such dishes are offered, it will be saved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIndeed, is it a sample for discrimination?\x02\x03",
            "#00005FBut … even if we say unusual food\x01",
            "What exactly is that\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's right, crossbell police\x01",
            "Speaking of a distinguished team\x01",
            "It is famous for advanced analysis equipment ……\x02\x03",
            "#00106FWe are not specialists in cooking,\x01",
            "Whether you can help us or not.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_333A")

    ChrTalk(
        0x103,
        (
            "#00200FDo not you have to think hard enough?\x02\x03",
            "#00203FEven just cooking normally,\x01",
            "What we did not anticipate\x01",
            "It may be completed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345C")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33D2")

    ChrTalk(
        0x105,
        (
            "#10404FHuh, you do not have to think hard?\x02\x03",
            "#10400FEven just cooking normally,\x01",
            "What I did not expect\x01",
            "There are things I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345C")

    label("loc_33D2")


    ChrTalk(
        0x105,
        (
            "#10304FHuh, you do not have to think hard?\x02\x03",
            "#10300FEven just cooking normally,\x01",
            "What I did not expect\x01",
            "There are things I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34C4")

    ChrTalk(
        0x109,
        (
            "#10106FWell, indeed …\x01",
            "Sometimes it seems like a strange chemical reaction\x01",
            "There are things that happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351D")

    label("loc_34C4")


    ChrTalk(
        0x104,
        (
            "#00306FOh, that's right.\x01",
            "Sometimes it seems like a strange chemical reaction\x01",
            "There is something to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_351D")


    ChrTalk(
        0x8,
        (
            "Huh, I can manage it somehow.\x01",
            "It seems there is Ate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If so, certainly will ask you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As always,\x01",
            "If you get such a dish\x01",
            "Bring me to my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "That's right.\x01",
            "What is to say instead … …\x01",
            "Let 's give this book to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝１卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝１卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "When I have time I will also read books,\x01",
            "It is good to heal daily fatigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FThank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 0)

    label("loc_370F")

    Return()

    # Function_8_305A end

    def Function_9_3710(): pass

    label("Function_9_3710")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_377F")

    ChrTalk(
        0xFE,
        (
            "Long ago, both lessons and training\x01",
            "I have not done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I am a police officer like this\x01",
            "I wonder if it will become ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_377F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3807")

    ChrTalk(
        0x9,
        (
            "At the time of a raid incident, to the police headquarters\x01",
            "The bomb seems to have been thrown ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Bulls …… Awesome, I am.\x01",
            "As I thought to the police …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_3807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3815")
    Jump("loc_3BA4")

    label("loc_3815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3823")
    Jump("loc_3BA4")

    label("loc_3823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(
        0x9,
        "Wow, I'm late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even though I had training from morning today ….\x01",
            "The instructor will yell at me ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_3886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3894")
    Jump("loc_3BA4")

    label("loc_3894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_38A2")
    Jump("loc_3BA4")

    label("loc_38A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38B0")
    Jump("loc_3BA4")

    label("loc_38B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B13")

    ChrTalk(
        0x9,
        (
            "Well, you are … …\x01",
            "For the people of the mission support department! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Myself at the Crossbell Times\x01",
            "After seeing the article of that cult's case,\x01",
            "I longing for a long time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the future I will also be at the Special Affairs Support Division\x01",
            "If assigned, and!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuhuu, that is a great story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FBoy, bother to say\x01",
            "I wanted to enter a difficult section,\x01",
            "I'm pretty talented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYou know.\x01",
            "Bother to that department\x01",
            "Who came in?\x02\x03",
            "#00000FKohon, um.\x01",
            "Because assignment is decided upon seeing appropriate\x01",
            "I can not choose it, but …\x02\x03",
            "#00002FIf you are assigned to the Special Affairs Division in the future\x01",
            "That time is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes! It is! I will do my best!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B88")

    label("loc_3B13")


    ChrTalk(
        0x9,
        (
            "Meeting you,\x01",
            "Motivation came suddenly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whether to put in the Special Affairs Support Division\x01",
            "I do not know but …\x01",
            "I will do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B88")

    Jump("loc_3BA4")

    label("loc_3B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3B9B")
    Jump("loc_3BA4")

    label("loc_3B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BA4")

    label("loc_3BA4")

    TalkEnd(0xFE)
    Return()

    # Function_9_3710 end

    def Function_10_3BA8(): pass

    label("Function_10_3BA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C33")

    ChrTalk(
        0xFE,
        (
            "By the way, for a while\x01",
            "I did not return home …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the barrier disappeared,\x01",
            "I guess I should return to my parents house once …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CAF")

    ChrTalk(
        0xA,
        (
            "A curriculum is a matter of time\x01",
            "You did it hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope to become a force of my seniors as soon as possible\x01",
            "Let's do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CBD")
    Jump("loc_3E8B")

    label("loc_3CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3D09")

    ChrTalk(
        0xA,
        (
            "Train accident\x01",
            "I heard that it happened ….\x01",
            "What the hell happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D17")
    Jump("loc_3E8B")

    label("loc_3D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DAB")

    ChrTalk(
        0xA,
        (
            "Independent advocacy of this time, our trainee also\x01",
            "I feel a big meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For the future development of the police organization,\x01",
            "I would like you to realize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DB9")
    Jump("loc_3E8B")

    label("loc_3DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E66")

    ChrTalk(
        0xA,
        (
            "Today at this meeting room\x01",
            "A lecture on autonomous state law is carried out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For police officers the law\x01",
            "Because it is an inseparable presence.\x01",
            "You have to learn firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E74")
    Jump("loc_3E8B")

    label("loc_3E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3E82")
    Jump("loc_3E8B")

    label("loc_3E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E8B")

    label("loc_3E8B")

    TalkEnd(0xFE)
    Return()

    # Function_10_3BA8 end

    def Function_11_3E8F(): pass

    label("Function_11_3E8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EA0")
    Jump("loc_42E9")

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F66")

    ChrTalk(
        0xB,
        (
            "Trainees also took a train accident yesterday\x01",
            "It seems to be gloomy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, as they are making noise\x01",
            "There is nothing I can not do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Activate once, in the curriculum\x01",
            "I should concentrate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_400C")

    label("loc_3F66")


    ChrTalk(
        0xB,
        (
            "Yesterday's train accident,\x01",
            "It is said that the trainees here are making noise\x01",
            "There is nothing I can not do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now concentrate on the lesson,\x01",
            "Towards an incidents that will happen in the future\x01",
            "I have to grow up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400C")

    Jump("loc_42E9")

    label("loc_4011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_401F")
    Jump("loc_42E9")

    label("loc_401F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_402D")
    Jump("loc_42E9")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_403B")
    Jump("loc_42E9")

    label("loc_403B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4223")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415E")

    ChrTalk(
        0xB,
        (
            "Recently trained students,\x01",
            "The attitude towards the curriculum\x01",
            "It is more positive than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A big incident called a cult incident\x01",
            "What the police solved mainly as a result,\x01",
            "I guess it had a good effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For the juniors who have not yet seen,\x01",
            "By all means to the active police officer\x01",
            "I would like you to keep showing its success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_421E")

    label("loc_415E")


    ChrTalk(
        0xB,
        (
            "A big incident called a cult incident\x01",
            "What the police solved mainly as a result,\x01",
            "It has a good influence on trainees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For the juniors who have not yet seen,\x01",
            "By all means to the active police officer\x01",
            "I would like you to keep showing its success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421E")

    Jump("loc_42E9")

    label("loc_4223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4231")
    Jump("loc_42E9")

    label("loc_4231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_423F")
    Jump("loc_42E9")

    label("loc_423F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_42E0")

    ChrTalk(
        0xB,
        (
            "Today the guards\x01",
            "I am diligent in survival training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As I looked at it a while ago\x01",
            "It seems that the condition has returned considerably.\x01",
            "No, it was really nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E9")

    label("loc_42E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42E9")

    label("loc_42E9")

    TalkEnd(0xFE)
    Return()

    # Function_11_3E8F end

    def Function_12_42ED(): pass

    label("Function_12_42ED")

    Call(0, 13)
    Return()

    # Function_12_42ED end

    def Function_13_42F1(): pass

    label("Function_13_42F1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471F")

    ChrTalk(
        0xC,
        "Everyone, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Take a bother today\x01",
            "Please go over here\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_END)), "loc_43C1")

    ChrTalk(
        0x101,
        (
            "#00000FOh my …\x02\x03",
            "#00003FAnything, for a while\x01",
            "Are you going to do business here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4414")

    label("loc_43C1")


    ChrTalk(
        0x101,
        (
            "#00000FOh my …\x02\x03",
            "#00003FRebecca-\x01",
            "Did you come to the police school?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4414")


    ChrTalk(
        0xC,
        (
            "Yes, police headquarters receptionist\x01",
            "I can still resume business very much\x01",
            "It is not a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fortunately,\x01",
            "Data on this terminal\x01",
            "Because there was backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the form of using it\x01",
            "We resumed work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyone, when there is business on reception\x01",
            "Please tell me anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FOk, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, Rebecca.\x02\x03",
            "#10104FWhen Fran was awake,\x01",
            "You rushed me first\x01",
            "I'm really thankful to you.\x02\x03",
            "#10109FThat girl was also very pleased.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        "No, such a thing ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If true, here is cheerful\x01",
            "I need to give it\x01",
            "On the contrary, I get energetic ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is, but really\x01",
            "It was nice being awake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FYeah, it's totally.\x02\x03",
            "#10100FAlso,\x01",
            "Can you show me your face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 5)
    TalkEnd(0xC)
    Return()

    label("loc_471F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_4ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACA")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Oh, everyone\x01",
            "That which you have is … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Perhaps, \"fragment\"\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEr, is this about that?\x02\x03",
            "#00000FAlthough I got it,\x01",
            "It is not used any more\x01",
            "I did not understand ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is in Rebecca\x01",
            "I showed fragments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "Well, after all … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is because the person in the district judgment section was looking for\x01",
            "Damaged memory crystals#8RMemory Quartz#Data\x01",
            "It is a program to restore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With that,\x01",
            "Part of the organization's terminal data\x01",
            "It should be able to analyze.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4962")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4962")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_498B")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_498B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49B4")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_49B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49DA")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_49DA")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FWell then, then …\x01",
            "By Joachim Gunter\x01",
            "To be able to read hidden sentences …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, in part\x01",
            "I heard there is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think that results will come out soon,\x01",
            "Even when \"fragment\" is used for discrimination\x01",
            "Is it OK?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    TalkEnd(0xC)
    Return()

    label("loc_4ACA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C47")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x0, 5)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B5C")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                        # 0
            "Show battle notebook\x01",                # 1
            "Confirm terminal data of the cult\x01",      # 2
            "Passing fragments\x01",              # 3
            "quit\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_4BBD")

    label("loc_4B5C")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                        # 0
            "Show battle notebook\x01",                # 1
            "Confirm terminal data of the cult\x01",      # 2
            "quit\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BBD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BBD")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BEB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)
    Jump("loc_4C42")

    label("loc_4BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)
    Call(0, 23)
    Jump("loc_4C42")

    label("loc_4C0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 17)
    Jump("loc_4C42")

    label("loc_4C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C42")
    Call(0, 16)

    label("loc_4C42")

    Jump("loc_4AD4")

    label("loc_4C47")

    TalkEnd(0xC)
    OP_93(0xC, 0x5A, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    Return()

    # Function_13_42F1 end

    def Function_14_4C58(): pass

    label("Function_14_4C58")


    ChrTalk(
        0xC,
        (
            "Anyway …\x01",
            "Fran was awake\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To cheer her up,\x01",
            "We also have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_14_4C58 end

    def Function_15_4CE8(): pass

    label("Function_15_4CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_4CF6")
    SetScenarioFlags(0x0, 5)

    label("loc_4CF6")

    Return()

    # Function_15_4CE8 end

    def Function_16_4CF7(): pass

    label("Function_16_4CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_4D95")

    ChrTalk(
        0xC,
        (
            "Oh, \"Fragment\"\x01",
            "You brought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To analyze the terminal data of the cult,\x01",
            "Even when \"fragment\" is used for discrimination\x01",
            "Is it OK?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D95")


    ChrTalk(
        0x101,
        "#00000FWell, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well then, please wait a moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BA0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_6B9B")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber('结晶碎片', 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E76")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 1 of \"About the cult\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E76")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED2")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 3 of \"About the cult\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4ED2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F34")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 1 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F34")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F96")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 2 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F96")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5853")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 4 of \"About the cult\"!\x07\x00\x02",
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
            "01 th information terminal data\x01",
            "Completed analysis of \"About the cult\"!\x07\x00\x02",
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
            "#5PAll data of the 01 th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWould you like to check it now?\x02",
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
            "#5P…… In this data,\x01",
            "An outline on the cult\x01",
            "It seems to have been described.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDoctrine of denial of the goddess … ….\x01",
            "I really can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes …\x01",
            "Joachim Gunter's\x01",
            "I also agree with the testimony.\x02\x03",
            "#00001FAnd this word \"D\" …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_538A")

    ChrTalk(
        0x103,
        (
            "#12P#00203FThey believed on behalf of the goddess\x01",
            "It is a word pointing to \"true God\".\x02\x03",
            "#00201FD∴ G \"G\" in the name of the organization\x01",
            "\"True wisdom#10RGnosis#\"To point to\x01",
            "It is already located … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5335")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm, this also means \"D∴ G\"\x01",
            "I heard that it is finally found out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5385")

    label("loc_5335")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm, this also means \"D∴ G\"\x01",
            "I heard that it is finally found out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5385")

    Jump("loc_5493")

    label("loc_538A")


    ChrTalk(
        0x103,
        (
            "#12P#00200FThey believed on behalf of the goddess\x01",
            "It is a word pointing to \"true God\".\x02\x03",
            "#00201FD∴ G \"G\" in the name of the organization\x01",
            "\"True wisdom#10RGnosis#\"To point to\x01",
            "It is already located … …\x02\x03",
            "This also means \"D∴ G\"\x01",
            "It can be said that it finally turned out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5493")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut … … Dr. Joachim,\x01",
            "Ka'a thing\x01",
            "You were saying \"the Godhead\", are not you?\x02\x03",
            "Then, \"D\" is\x01",
            "As for words pointing to Ka'aa\x01",
            "It will become … ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55BB")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Gunter\x01",
            "How far did you know … ….\x02\x03",
            "…… I do not know yet by just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56A1")

    label("loc_55BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5643")

    ChrTalk(
        0x104,
        (
            "#12P#00301FJoachim's bastard\x01",
            "How far did you know … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F…… I do not know yet by just this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56A1")

    label("loc_5643")


    ChrTalk(
        0x104,
        (
            "#12P#00301FJoachim's bastard\x01",
            "How far did you know … ….\x02\x03",
            "I can not tell by just this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A1")


    ChrTalk(
        0x101,
        (
            "#12P#00001FErnest also from Joachim\x01",
            "I was listening to everything\x01",
            "It seems not to be ……\x02\x03",
            "#00003FIf he could be arrested … …\x01",
            "Do not keep thinking so.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57AD")

    ChrTalk(
        0xC,
        (
            "#5P…… Anyway, in this condition\x01",
            "If you analyze data,\x01",
            "I think that various things will be visible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5853")

    label("loc_57AD")


    ChrTalk(
        0xC,
        (
            "#5P…… Anyway, in this condition\x01",
            "If you analyze data,\x01",
            "I think that various things will be visible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThe remaining \"fragment\" is also\x01",
            "Let's try it for analysis.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_5853")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B5")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 3 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_58B5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5911")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 1 of \"About Miko\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5911")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6230")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 4 of \"About Gnostic\"!\x07\x00\x02",
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
            "02 th information terminal data\x01",
            "Completed analysis of \"About Gnostic\"!\x07\x00\x02",
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
            "#5PAll data of the 02 th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWould you like to check it now?\x02",
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
            "#5P…… In this data,\x01",
            "About that \"Gnostic\"\x01",
            "It seems that details are written.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PImprove physical ability and sensitivity,\x01",
            "Even potential potential\x01",
            "Drug with efficacy to withdraw … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt is called phenomenon such as \"demonization\"\x01",
            "It is quite a mystery drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FIt was used as raw material\x01",
            "Plants called \"Pleroma grass\"\x01",
            "Because it was clustered in a wetland … …\x02\x03",
            "Joachim puts the material in wetland belt\x01",
            "Things that seem to have gone to collect\x01",
            "It seems that there is no mistake in the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D00")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, Gnostic is included in the data\x01",
            "A true God that they say … …\x02\x03",
            "That is, to restore \"D\"\x01",
            "There is a passage that is drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FTo be honest, to a stupid story\x01",
            "I can hear it ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DBB")

    label("loc_5D00")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, Gnostic is included in the data\x01",
            "A true God that they say … …\x02\x03",
            "That is, to restore \"D\"\x01",
            "There is a passage that is drug.\x02\x03",
            "#00108FTo be honest, to a stupid story\x01",
            "I can hear it ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBB")


    ChrTalk(
        0x103,
        (
            "#12P#00201FStill, the cult has for 500 years\x01",
            "In the form of \"ritual\"\x01",
            "I have been studying Gnostic … …\x02\x03",
            "#00203F…… I am lucky to Mr. Guy\x01",
            "I was rescued, but until now\x01",
            "There seems to be a considerable number of victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI thought it was \"some sacrifice\"\x01",
            "I'm talking about you ….\x02\x03",
            "They are like guys who really help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F59")

    ChrTalk(
        0x105,
        (
            "#12P#10403F…… Also, recently Waldo\x01",
            "You were taking Gnostic, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5F59")


    ChrTalk(
        0x105,
        (
            "#12P#10303F…… Also, recently Waldo\x01",
            "You were taking Gnostic, are not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA9")


    ChrTalk(
        0x101,
        (
            "#12P#00001FOh … … Although the cult has gone,\x01",
            "We may still need attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608E")

    label("loc_6002")


    ChrTalk(
        0x101,
        (
            "#12P#00003F…… Also, recently Waldo\x01",
            "I was taking Gnostic.\x02\x03",
            "#00001FAlthough the cult has disappeared,\x01",
            "We may still need attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_608E")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYeah … That's really true.\x02\x03",
            "Not limited to Gnostic,\x01",
            "Such drugs, our police\x01",
            "You have to get it under control.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6180")

    ChrTalk(
        0xC,
        "#5PYes, I really think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P… for the time being about Gnostic\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6230")

    label("loc_6180")


    ChrTalk(
        0xC,
        "#5PYes, I really think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P… for the time being about Gnostic\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThe remaining \"fragment\" is also\x01",
            "Let's try it for analysis.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_6230")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 2 of \"About Miko\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_628C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9B")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 3 of \"About Miko\"!\x07\x00\x02",
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
            "03 th information terminal data\x01",
            "I completed the analysis of \"About Miko\"!\x07\x00\x02",
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
            "#5PAll data of the 03th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWould you like to check it now?\x02",
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
            "#5PThis content,\x01",
            "It was protected by support section\x01",
            "Kaoru's … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F500 years ago, by the Clois family\x01",
            "Keya was born … ….\x01",
            "It was given to the cult as object of religion.\x02\x03",
            "The chest#4RCradle#\"Asleep on,\x01",
            "As a \"God's Child\" \"Child\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Human beings of the cult also have truth\x01",
            "You probably did not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FFor the true purpose of the Clois family\x01",
            "Without knowing that it was guided by shadows,\x01",
            "I continued seeking the illusion of \"true God\" …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65F5")

    ChrTalk(
        0x106,
        "#12P#10708F…… In a sense, they are pathetic people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_666C")

    label("loc_65F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_663D")

    ChrTalk(
        0x109,
        "#12P#10108F…… In a sense, they are pathetic people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_666C")

    label("loc_663D")


    ChrTalk(
        0x105,
        "#12P#10408F… … In a sense, pathetic people.\x02",
    )

    CloseMessageWindow()

    label("loc_666C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66C3")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they came up with\x01",
            "I do not even feel sympathy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676C")

    label("loc_66C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6720")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they came up with\x01",
            "There is no room for sympathy though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676C")

    label("loc_6720")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they came up with\x01",
            "There is no room for sympathy … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676C")


    ChrTalk(
        0x101,
        (
            "#12P#00001FRegardless of cults ……\x01",
            "There must have been no sin in Ka'aa.\x02\x03",
            "#00003FEven for the purpose of the Clois family\x01",
            "Even if it was a made existence ……\x02\x03",
            "Even a magical ability\x01",
            "Even if I have … …\x01",
            "Such a thing has nothing to do with it.\x02\x03",
            "That girl that awakens in front of us\x01",
            "It should be genuine, ordinary girl.\x02\x03",
            "#00001FEven so, for hundreds of years like that\x01",
            "It's been locked in alone … …\x02\x03",
            "Now also with Mr. Marybele\x01",
            "By Professor Ian\x01",
            "It is about to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F…… Regardless of circumstances,\x01",
            "Absolutely I can not forgive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P…… For now, the cult's data\x01",
            "All analysis is completed with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI am about as much as you guys\x01",
            "I am not familiar with detailed circumstances … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PFor everyone, Mr.\x01",
            "That it is a very important existence\x01",
            "I understand it painfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PPlease … Good luck.\x01",
            "I will support you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThank you, Rebecca.\x02\x03",
            "Absolutely with our hands,\x01",
            "I will get back Ka'aa.\x02\x03",
            "#00007FOur precious kea … …\x01",
            "That child can spend herself with a smile\x01",
            "To make a future … ….!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B76")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_6B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B8F")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_6B8F")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)

    label("loc_6B9B")

    Jump("loc_4DEE")

    label("loc_6BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CB7")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Also, if you get \"fragments\"\x01",
            "Please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even when checking the analyzed data\x01",
            "Please tell us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6C98")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_6C98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6CB1")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_6CB1")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_6CB7")

    Return()

    # Function_16_4CF7 end

    def Function_17_6CB8(): pass

    label("Function_17_6CB8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC2")
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
            "【About the cult】\x01",            # 0
            "【About Gnostic】\x01",      # 1
            "【About Miko】\x01",            # 2
            "【do nothing】\x01",              # 3
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
        (0, "loc_6D75"),
        (1, "loc_6D83"),
        (2, "loc_6D91"),
        (3, "loc_6D9F"),
        (SWITCH_DEFAULT, "loc_6DAE"),
    )


    label("loc_6D75")

    Sound(72, 0, 100, 0)
    Call(0, 18)
    Jump("loc_6DBD")

    label("loc_6D83")

    Sound(72, 0, 100, 0)
    Call(0, 19)
    Jump("loc_6DBD")

    label("loc_6D91")

    Sound(72, 0, 100, 0)
    Call(0, 20)
    Jump("loc_6DBD")

    label("loc_6D9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DBD")

    label("loc_6DAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DBD")

    label("loc_6DBD")

    Jump("loc_6CC2")

    label("loc_6DC2")

    Return()

    # Function_17_6CB8 end

    def Function_18_6DC3(): pass

    label("Function_18_6DC3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the cult\"\x01\x01",
            "── My name is Joachim Gunter.\x01",
            "It is an executive priest belonging to the \"D∴G organization\".\x01",
            "Six years ago, with the hands of many forces, including hushman\x01",
            "Our group fell into destruction.\x01",
            "However, I alone escaped the hardship,\x01",
            "I was able to surmount to this land of ■■.\x01",
            "By the guidance of the great \"■\"\x01",
            "I have been a long time to make ambitions for the cult.\x01",
            "Any time that comes - ─\x01",
            "As a document to write a new scripture\x01",
            "Data is recorded in each terminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_712B")

    label("loc_6F8A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the cult\"\x01\x01",
            "── My name is Joachim Gunter.\x01",
            "It is an executive priest belonging to the \"D∴G organization\".\x01",
            "Six years ago, with the hands of many forces, including hushman\x01",
            "Our group fell into destruction.\x01",
            "However, I alone escaped the hardship,\x01",
            "I could survive to the land of this origin.\x01",
            "By the guidance of the great \"D\"\x01",
            "I have been a long time to make ambitions for the cult.\x01",
            "Any time that comes - ─\x01",
            "As a document to write a new scripture\x01",
            "Data is recorded in each terminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_712B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, let's talk about the origins of our cult.\x01",
            "To this end, the continent of Zemria followed\x01",
            "It is necessary to look back on the abominable history.\x01\x01",
            "── About 1,200 years ago by the \"Great Collapse\"\x01",
            "The continent has lost advanced civilization and order,\x01",
            "The \"dark era\" which dominates war and poverty has come.\x01",
            "And the people who are exhausted\x01",
            "I made a big mistake.\x01\x01",
            "Suddenly misled by the foolish comments of the foolish people,\x01",
            "The autonomous order created by them\x01",
            "It has accepted it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7472")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThat is - __- stupid\x01",
            "It is \"■ ■ ■\" which is a symbol of faith.\x01",
            "By their order the \"dark era\" will end,\x01",
            "That faith quickly spread throughout the continent … …\x01\x01",
            "Please think carefully.\x01",
            "If truly \"■ ■\" exists\x01",
            "Should everyone receive equal salvation?\x01",
            "However, the concept of disparity still remains,\x01",
            "Those who lose their lives due to disasters and misfortunes are also followed.\x01\x01",
            "Does \"■ ■\" choose people to save?\x01",
            "Is not that a foolish story?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7619")

    label("loc_7472")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThat is ─ ─ a foolish seven chaos church\x01",
            "It is a \"goddess of the sky\" symbolizing faith.\x01",
            "By their order the \"dark era\" will end,\x01",
            "That faith quickly spread throughout the continent … …\x01\x01",
            "Please think carefully.\x01",
            "If it is true that \"goddess\" exists\x01",
            "Should everyone receive equal salvation?\x01",
            "However, the concept of disparity still remains,\x01",
            "Those who lose their lives due to disasters and misfortunes are also followed.\x01\x01",
            "Does \"Goddess\" choose a human being to save?\x01",
            "Is not that a foolish story?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7619")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_779F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SAfter all, because ■■■■ gains authority\x01",
            "It is nothing but a virtual image created.\x01",
            "It can not exist, such as \"■ ■\".\x01\x01",
            "Our predecessors who arrived at the truth,\x01",
            "I got on a long journey to encounter \"■ ■ ■ ■\".\x01\x01",
            "And when the times change to the Middle Ages,\x01",
            "At last they found it.\x01",
            "In the depths of this place ■ ■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■ ……\x01\x01",
            "\"■\" ── It was called so.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7912")

    label("loc_779F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SAfter all, the seven chaos church gets authority\x01",
            "It is nothing but a virtual image created.\x01",
            "\"Goddess\" etc, such as existence can not exist.\x01\x01",
            "Our predecessors who arrived at the truth,\x01",
            "I entered a long journey to encounter \"true god\".\x01\x01",
            "And when the times change to the Middle Ages,\x01",
            "At last they found it.\x01",
            "With deep inside of this place, with a long sleep\x01",
            "Presence of great power in his body ……\x01\x01",
            "\"D\" ── It was called so.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7912")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_18_6DC3 end

    def Function_19_7926(): pass

    label("Function_19_7926")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7ADB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About Gnostic\"\x01\x01",
            "\"Gnostic\" … … that,\x01",
            "■■■■■■■■ ■■■■■,\x01",
            "It is a secret medicine made from \"praroma grass\" as a raw material.\x01\x01",
            "The preparation method is: ■■■■■■■■■,\x01",
            "By enhancing physical ability and responsiveness by taking it,\x01",
            "Furthermore it has an efficacy to bring out even potential potential.\x01",
            "■■■■■■■■■■■■■■■■■.\x01",
            "■■■■■■■■■■■■■■■.\x01",
            "\"Gnostic\", the ■ ■ ■ ■ ■\x01",
            "It is a ■ ■ ■ ■ ■ ■ ■ medicine to ■ ■ ■ of \"■ ■\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7C6A")

    label("loc_7ADB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About Gnostic\"\x01\x01",
            "\"Gnostic\" … … that,\x01",
            "Legendary plants that bloom on the seventy -\x01",
            "It is a secret medicine made from \"praroma grass\" as a raw material.\x01\x01",
            "The mixing method is transmitted together with \"D\"\x01",
            "By enhancing physical ability and responsiveness by taking it,\x01",
            "Furthermore it has an efficacy to bring out even potential potential.\x01",
            "But they are merely mockets.\x01",
            "The true power of this medicine was another.\x01",
            "\"Gnostic\", the spirit of the recipients\x01",
            "It is a medicine to connect to the \"D\" heart.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7C6A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E08")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"■ ■\" By ■ ■ ■ ■ ■ ■ ■\x01",
            "It has the property of storing ■ and ■ ■.\x01",
            "When either of those ■ ■ \"■ ■\" reached,\x01",
            "\"■\" means to ■ ■.\x01\x01",
            "In addition, \"Gnostic\"\x01",
            "There was room for improvement.\x01",
            "■■■■■■■■■■■■■■■■■,\x01",
            "■■■■■■■ to \"■\" ■ ■■■■■.\x01\x01",
            "Then, ■■■■■■■, our group is\x01",
            "A study on \"Gnostic\" which is more effective ……\x01",
            "We have repeated so-called \"ceremonies\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7F93")

    label("loc_7E08")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"D\" by integrating the spirit of the recipients\x01",
            "It has the property of accumulating knowledge and growing up.\x01",
            "When that knowledge reached \"wisdom\"\x01",
            "\"D\" is resurrected.\x01\x01",
            "In addition, \"Gnostic\"\x01",
            "There was room for improvement.\x01",
            "If you can withdraw the ability of the recipient to the limit,\x01",
            "You can supply more knowledge to \"D\".\x01\x01",
            "For 500 years, my group\x01",
            "A study on \"Gnostic\" which is more effective ……\x01",
            "We have repeated so-called \"ceremonies\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7F93")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8125")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, with ■■■ of ■■■■■\x01",
            "■■■■■■■■■■■■\x01",
            "\"Gnostic\" approached completion,\x01",
            "Miscalculation will occur at the first step.\x01\x01",
            "By increasing the scale of the experiment\x01",
            "Having been felt in existence by hooked guys and other forces,\x01",
            "To the extinction of each lodge, and the cult itself\x01",
            "It was connected.\x01\x01",
            "It is inevitable to say that it is a foolish thing.\x01",
            "For ■■ of \"■■■■\"\x01",
            "Although somewhat sacrifice is a provision … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A4")

    label("loc_8125")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, when it was 500 years ago when it was launched\x01",
            "At comparable speed\x01",
            "\"Gnostic\" approached completion,\x01",
            "Miscalculation will occur at the first step.\x01\x01",
            "By increasing the scale of the experiment\x01",
            "Having been felt in existence by hooked guys and other forces,\x01",
            "To the extinction of each lodge, and the cult itself\x01",
            "It was connected.\x01\x01",
            "It is inevitable to say that it is a foolish thing.\x01",
            "For the resurrection of \"the true God\"\x01",
            "Although somewhat sacrifice is a provision … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_82A4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_844E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI am from a devastated lodge\x01",
            "We collected the experiment data secretly,\x01",
            "It reached the cross-bell belt of this ■.\x01\x01",
            "It is a material of \"Gnostic\"\x01",
            "\"Pleroma grass\" is a ■■■■■■■\x01",
            "Because it is ■ ■ ■ ■ ■,\x01",
            "There was nothing troubled by ■■■■■.\x01",
            "Also, the depth of this \"Fort of the Sun\"\x01",
            "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ research facilities,\x01",
            "It has many advanced facilities.\x01",
            "Thus I got a blessed research environment\x01",
            "Finally I finished this prescription ─ ─.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_85E5")

    label("loc_844E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI am from a devastated lodge\x01",
            "We collected the experiment data secretly,\x01",
            "It reached the earth crossbell of this origin.\x01\x01",
            "It is a material of \"Gnostic\"\x01",
            "\"Pleroma grass\" is the southern part of Crossbell\x01",
            "Because it is clustered in wetlands,\x01",
            "There was nothing to worry about procuring materials.\x01",
            "Also, the depth of this \"Fort of the Sun\"\x01",
            "It is a research facility built by a medieval alchemist,\x01",
            "It has many advanced facilities.\x01",
            "Thus I got a blessed research environment\x01",
            "Finally I finished this prescription ─ ─.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_85E5")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_19_7926 end

    def Function_20_85F9(): pass

    label("Function_20_85F9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87BC")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the Son\"\x01\x01",
            "This crossbell is our \"D∴G organization\"\x01",
            "In addition to being ■■■, it is set as ■■■■.\x01",
            "That's the \"child\"\x01",
            "That's why it is ■■■■■■■■■■■■■.\x01\x01",
            "\"Son\" is \"■ ■■■\" ■■■■■■■\x01",
            "■■ \"D∴G Church\" ■■■■■■■■■■.\x01",
            "\"Fort of the Sun\" ■■■■■■■■■■■■,\x01",
            "■■■■■■■■■■■■■■■■■,\x01",
            "■■■■■■■ \"Fort of the Sun\" ■■■■\x01",
            "It is ■■■■■■■■■■■■■■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8959")

    label("loc_87BC")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the Son\"\x01\x01",
            "This crossbell is our \"D∴G organization\"\x01",
            "It is the home base and the place of origin.\x01",
            "The reason is that \"Child\"\x01",
            "It is a place that has been inherited from the founder.\x01\x01",
            "\"Son\" is the substitution of the \"true God\"\x01",
            "It is a symbol of our \"D∴G organization\".\x01",
            "It keeps sleeping in the basement of \"The Fort of the Sun\"\x01",
            "At first glance it is a girl of a human being,\x01",
            "In the altar of \"Fort of the Sun\" for 500 years\x01",
            "He is waiting for the awakening time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8959")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AE9")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■ ■ ■ ■ ■ ■ ■ so much,\x01",
            "It will be an incredible story for those who are alive.\x01\x01",
            "But I saw it with my own eyes.\x01",
            "In ■ of ■ ■ ■ ■ ■ ■ ■ called\x01",
            "■■■■■■■■■■■■■■ ──\x01",
            "That shit divine ■ ■.\x01\x01",
            "\"■■■■■\" means \"ancient relics\"\x01",
            "Based on the ■ ■ ■ ■ ■ ■ ■ ■ ■\x01",
            "It is ■■■■■■■■■■■■■■■.\x01",
            "Then, even this ■■■■■■■■■■\x01",
            "There is no mystery.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8C72")

    label("loc_8AE9")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SHuman beings live so much time,\x01",
            "It will be an incredible story for those who are alive.\x01\x01",
            "But I saw it with my own eyes.\x01",
            "\"Holy One Pillar#4RCradle#In a sphere called\x01",
            "A girl keeps sleeping like a slumber ----\x01",
            "Its Shinto shrine.\x01\x01",
            "\"Sacred throne\", \"ancient relics\"\x01",
            "Based on the technique of the alchemists I was studying\x01",
            "It was created by the predecessors of the cult.\x01",
            "Then, even as a phenomenon which is also called this miracle\x01",
            "There is no mystery.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8C72")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DEF")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"Son\" is from ■■■■■■\x01",
            "\"Gnostic\" as ■■■, ■■■■■■■\x01",
            "■■■■■■■■■■■■■.\x01\x01",
            "── \"■■\" ■■■■■ \"Son\" is ■■■,\x01",
            "It will be ■■■■ \"■\" ■ ■■.\x01",
            "And ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\x01",
            "It is done under the \"■ ■\"\x01",
            "Release people from the spell of \"■ ■\".\x01\x01",
            "That was left by the predecessor of our \"D∴G Church\"\x01",
            "It is a prophecy, an ambition to be formed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8F59")

    label("loc_8DEF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"Son\" was born and from the times\x01",
            "Through \"Gnostic\", you can say infinite\x01",
            "It is said that you have lodged knowledge.\x01\x01",
            "── When it reaches \"wisdom\", \"Son\" wakes up,\x01",
            "It will be a true god \"D\".\x01",
            "And the intention and soul of all people\x01",
            "It is consolidated under \"D\"\x01",
            "Unleash people from the spell of \"goddess\".\x01\x01",
            "That was left by the predecessor of our \"D∴G Church\"\x01",
            "It is a prophecy, an ambition to be formed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8F59")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_20_85F9 end

    def Function_21_8F6D(): pass

    label("Function_21_8F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F92")
    SetChrPos(0xFE, 3220, 0, 12810, 0)
    Jump("loc_9046")

    label("loc_8F92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB7")
    SetChrPos(0xFE, 2220, 0, 12400, 0)
    Jump("loc_9046")

    label("loc_8FB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FDC")
    SetChrPos(0xFE, 4050, 0, 12360, 0)
    Jump("loc_9046")

    label("loc_8FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9001")
    SetChrPos(0xFE, 3080, 0, 11680, 0)
    Jump("loc_9046")

    label("loc_9001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9026")
    SetChrPos(0xFE, 2430, 0, 10480, 0)
    Jump("loc_9046")

    label("loc_9026")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9046")
    SetChrPos(0xFE, 3790, 0, 10440, 0)

    label("loc_9046")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_8F6D end

    def Function_22_9055(): pass

    label("Function_22_9055")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9075")
    BeginChrThread(0x101, 1, 0, 21)

    label("loc_9075")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_908C")
    BeginChrThread(0x102, 1, 0, 21)

    label("loc_908C")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90A3")
    BeginChrThread(0x103, 1, 0, 21)

    label("loc_90A3")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90BA")
    BeginChrThread(0x104, 1, 0, 21)

    label("loc_90BA")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D1")
    BeginChrThread(0x109, 1, 0, 21)

    label("loc_90D1")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90E8")
    BeginChrThread(0x105, 1, 0, 21)

    label("loc_90E8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90FF")
    BeginChrThread(0x106, 1, 0, 21)

    label("loc_90FF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9116")
    BeginChrThread(0x10A, 1, 0, 21)

    label("loc_9116")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9130")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9149")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_9149")

    Return()

    # Function_22_9055 end

    def Function_23_914A(): pass

    label("Function_23_914A")

    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_915D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9380")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_919C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91D0")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_91D0")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9204")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9204")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9238")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9238")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_926C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92A0")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_92A0")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92D4")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_92D4")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9308")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9308")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_933F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jump("loc_937B")

    label("loc_933F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9376")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    Jump("loc_937B")

    label("loc_9376")

    Jump("loc_9380")

    label("loc_937B")

    Jump("loc_915D")

    label("loc_9380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_9D15")
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
            "Oh, everyone ……\x01",
            "Combat notebook\x01",
            "It seems that Oita is getting buried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want to refrain from the monster's information\x01",
            "Would you mind letting me see it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYeah, pleased.\x02",
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
            "I will return the notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This will be for this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9585")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received one.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 1)
    Jump("loc_98FC")

    label("loc_9585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95E8")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received two.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 2)
    Jump("loc_98FC")

    label("loc_95E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Three, received.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 3)
    Jump("loc_98FC")

    label("loc_964B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96AE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received four.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 4)
    Jump("loc_98FC")

    label("loc_96AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9711")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received five.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 5)
    Jump("loc_98FC")

    label("loc_9711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9774")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 6 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 6)
    Jump("loc_98FC")

    label("loc_9774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D7")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 7 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 7)
    Jump("loc_98FC")

    label("loc_97D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_983A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received eight.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 8)
    Jump("loc_98FC")

    label("loc_983A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_989D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 9 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 9)
    Jump("loc_98FC")

    label("loc_989D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98FC")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "5000 mirrors\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 10 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 10)

    label("loc_98FC")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9938")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received two.\x02",
        )
    )

    AddItemNumber('神圣布料', 2)
    CloseMessageWindow()
    Jump("loc_9969")

    label("loc_9938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9969")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('神圣布料', 1)
    CloseMessageWindow()

    label("loc_9969")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AA6")

    ChrTalk(
        0xC,
        (
            "And if the monster's information gathers\x01",
            "Please stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A2E")

    ChrTalk(
        0x102,
        "#12P#0100FI will bother you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AA1")

    label("loc_9A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A65")

    ChrTalk(
        0x103,
        "#12P#0200FI will also bother you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AA1")

    label("loc_9A65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA1")

    ChrTalk(
        0x104,
        "#12P#0300FI will also let you interfere.\x02",
    )

    CloseMessageWindow()

    label("loc_9AA1")

    Jump("loc_9CAD")

    label("loc_9AA6")


    ChrTalk(
        0xC,
        (
            "Information on the new demons\x01",
            "You seem to have gathered enough.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This also means future safety measures\x01",
            "I think that it can be made more thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FHaha … … it is an honor to serve you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Huhu, you guys really\x01",
            "I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well then, this time\x01",
            "Special remuneration will be given as well.\x01",
            "Please accept it.\x02",
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
            "10000 Mira\x07\x00",
            "Received.\x02",
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
            "Your success in the future\x01",
            "I pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If there is something again\x01",
            "You can come anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CAD")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9CC4")
    ClearScenarioFlags(0x0, 6)

    label("loc_9CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CDD")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CF6")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_9CF6")

    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2470, 0, 12690, 0)
    EventEnd(0x5)
    TalkBegin(0xC)
    Jump("loc_9E57")

    label("loc_9D15")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DCC")

    ChrTalk(
        0xC,
        (
            "Information gathered at headquarters is also\x01",
            "I think that it is sufficient already,\x01",
            "Survey will be done so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Also something to ask of you\x01",
            "There may be.\x01",
            "At that time I would appreciate your favor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E57")

    label("loc_9DCC")


    ChrTalk(
        0xC,
        (
            "The content of the fighting notebook is also\x01",
            "It seems they are getting collected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If more information gathers\x01",
            "Please show me.\x01",
            "Because you have me refrain from the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E57")

    Return()

    # Function_23_914A end

    def Function_24_9E58(): pass

    label("Function_24_9E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F3C")

    ChrTalk(
        0xFE,
        "Oh, who is Sergei's and this child?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I ran out of hands\x01",
            "Security around the police school\x01",
            "It is supposed to be left off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is the command direction after a long absence,\x01",
            "Even for young policemen,\x01",
            "I do not know what to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9FC7")

    label("loc_9F3C")


    ChrTalk(
        0xFE,
        (
            "After becoming the section manager of the wide area security office\x01",
            "Desk work was abundant, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is an emergency,\x01",
            "Even for young policemen,\x01",
            "I do not know what to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC7")

    TalkEnd(0xFE)
    Return()

    # Function_24_9E58 end

    def Function_25_9FCB(): pass

    label("Function_25_9FCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A193")
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A123")

    ChrTalk(
        0xE,
        (
            "Again to the trainees\x01",
            "It seems that anxiety is spreading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I happened to come to the lecture on traffic\x01",
            "Citizens also heard the annihilation of the barrier\x01",
            "I want to go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, after all, there is dealing with that\x01",
            "I guess it might be hasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Okay, the correspondence there is\x01",
            "Let's do with me and women police officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You guys continue\x01",
            "Please keep on guarding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ha!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A18F")

    label("loc_A123")


    ChrTalk(
        0xD,
        (
            "Response of trainees and citizens\x01",
            "Let's do with me and women police officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You guys continue\x01",
            "Please keep on guarding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ha!\x02",
    )

    CloseMessageWindow()

    label("loc_A18F")

    OP_4C(0xD, 0xFF)

    label("loc_A193")

    TalkEnd(0xFE)
    Return()

    # Function_25_9FCB end

    def Function_26_A197(): pass

    label("Function_26_A197")

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

    def lambda_A2CE():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A2CE)
    Sleep(50)

    def lambda_A2DE():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A2DE)
    Sleep(50)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A527")

    ChrTalk(
        0xF,
        "#01005F#5POh, you're finally here\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_A33D():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A33D)
    Sleep(0)

    def lambda_A355():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A355)
    Sleep(0)

    def lambda_A36D():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A36D)
    Sleep(0)

    def lambda_A385():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A385)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Noel 's sergeant.\x01",
            "It has been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PI am arriving,\x01",
            "Sorry I'm late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01000F#5POh, I got in touch a while ago\x01",
            "Crackdown on runaway vehicles\x01",
            "I heard he was helping.\x02\x03",
            "#01004FWell, if that's the case\x01",
            "Let's look at the lag too.\x01",
            "… … It was a hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PThank you.\x02\x03",
            "#00002FAlso, Secretary Huang,\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A653")

    label("loc_A527")


    ChrTalk(
        0xF,
        "#01005F#5POh, did you come back?\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_A561():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A561)
    Sleep(0)

    def lambda_A579():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A579)
    Sleep(0)

    def lambda_A591():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A591)
    Sleep(0)

    def lambda_A5A9():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A5A9)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PLloyd, Noel 's sergeant.\x01",
            "It has been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PWe just arrived\x02\x03",
            "#00002FSecretary Huang,\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A653")


    ChrTalk(
        0x109,
        "#10109F#12PI'm glad you look so good\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHaha, with Noel\x01",
            "Since last regular exercise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLloyd since you graduated\x01",
            "I wonder if it will be the first time in ten months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, I have not seen it for a while\x01",
            "It has become quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11Pmy mother……\x01",
            "It is still half a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PUh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PTo police the police school\x01",
            "Is it the place of responsibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004F#5POh, the general management of the surrounding facilities\x01",
            "He is in charge of secretary Juan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, no.\x01",
            "It is not such a big deal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#6PWell then, Sergei.\x01",
            "The meeting room\x01",
            "Please use it freely.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0xF,
        "#01002F#11PYeah we will\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 27)
    Sleep(3000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01003F#5PWell then we don't have much time\x02\x03",
            "#01000FI will start right away.\x01",
            "Come along quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1280, 1000, 9280, 1500)
    OP_93(0xF, 0x5A, 0x1F4)

    def lambda_A936():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A936)

    def lambda_A94B():

        label("loc_A94B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A94B")

    QueueWorkItem2(0x101, 2, lambda_A94B)

    def lambda_A95D():

        label("loc_A95D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A95D")

    QueueWorkItem2(0x102, 2, lambda_A95D)

    def lambda_A96F():

        label("loc_A96F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A96F")

    QueueWorkItem2(0x109, 2, lambda_A96F)

    def lambda_A981():

        label("loc_A981")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A981")

    QueueWorkItem2(0x105, 2, lambda_A981)
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
        "#00105F#12PUh, Director Sergei…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PUh\x01",
            "In the end what kind of business is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01005F#11PYou still haven't noticed?\x02\x03",
            "#01004FThere should have been various hints … …\x01",
            "Kuku, are you still having Toyoko?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PW-wait a second!\x02\x03",
            "#00003FVarious tips ……\x01",
            "The meaning of calling us in this place ……\x02\x03",
            "#00000FCould it be\x02",
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
            "#1KWhat was Sergei's call?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Training Course of the Investigator Test】\x01",          # 0
            "【Training on Basic Traffic Law】\x01",          # 1
            "【Course of power net technology】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ABDB"),
        (1, "loc_ACD8"),
        (2, "loc_AD7E"),
        (SWITCH_DEFAULT, "loc_AE6B"),
    )


    label("loc_ABDB")


    ChrTalk(
        0xF,
        (
            "#01006F#11PInvestigator qualifications already\x01",
            "I guess you have it.\x02\x03",
            "#01003FDue to the nature of the Special Affairs Support Division,\x01",
            "All members have investigator qualification\x01",
            "You do not have to have it.\x02\x03",
            "#01000FThe answer is ──\x01",
            "It is \"Training of basic traffic law\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12PSo could that be\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_ACD8")

    OP_2C(0xA1, 0x1)

    ChrTalk(
        0x101,
        (
            "#00002F#6PReally……\x01",
            "Is it a lecture on the basic traffic law?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01004F#11PHah. Exactly\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PUh\x01",
            "Could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_AD7E")


    ChrTalk(
        0xF,
        (
            "#01003F#11PThere is definitely a power net\x01",
            "Although it is being drawn … …\x02\x03",
            "If you let it do it\x01",
            "I will let you go around the office of the Foundation.\x02\x03",
            "#01000FThe answer is ──\x01",
            "It is \"Training of basic traffic law\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12PSo could that be\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_AE6B")


    ChrTalk(
        0xF,
        (
            "#01004F#11POh, this time to the Special Affairs Support Division\x01",
            "It was decided that a guided vehicle would be provided.\x02\x03",
            "#01002FWith this, Iraha of the traffic law\x01",
            "You will be knocked down in your head.\x02",
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
            "#01003F#5P── This is the reason why\x01",
            "It is the basic transportation law to remember at minimum.\x02\x03",
            "#01000FDid I manage to drill it into your heads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI- I guess\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PWell, in such a place\x01",
            "It is said that classes are waiting … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B2B6")

    ChrTalk(
        0x102,
        (
            "#00100F#6P…… But, than I thought\x01",
            "There are only simple rules.\x02\x03",
            "#00103FLike the incident of a runaway car just before,\x01",
            "Penalties for foreigners are also weak\x01",
            "Of course there are … …\x02\x03",
            "#00101FIf the number of driving vehicles is increasing\x01",
            "It seems impossible to deal with this alone\x01",
            "I feel like that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat's something we're thinking\x02\x03",
            "#01001FSince private-use guided vehicles started to spread\x01",
            "It has not passed ten years.\x02\x03",
            "Both, more rigid rules\x01",
            "You will be asked.\x02\x03",
            "Regarding penalties for foreigners as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3F7")

    label("loc_B2B6")


    ChrTalk(
        0x102,
        (
            "#00103F#6P…… But, than I thought\x01",
            "There are only simple rules.\x02\x03",
            "#00101FIf the number of driving vehicles is increasing\x01",
            "It seems impossible to deal with this alone\x01",
            "I feel like that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01006F#5PThat's something we're thinking\x02\x03",
            "#01001FSince private-use guided vehicles started to spread\x01",
            "It has not passed ten years.\x02\x03",
            "Both, more rigid rules\x01",
            "You will be asked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3F7")


    ChrTalk(
        0x109,
        (
            "#10103F#11PIf you apply to a government office now\x01",
            "Easy driver license\x01",
            "It will be delivered ….\x02\x03",
            "#10101FWe have also introduced the test system\x01",
            "It is being studied, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5POh, in that case\x01",
            "Practical examinations for various courses\x01",
            "I will come in.\x02\x03",
            "#01000FWell, for now, for today\x01",
            "Dedicate the basic rules.\x02\x03",
            "Actual driving is ──\x01",
            "Noel, let me do this.\x02",
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
            "#00002F#5PRight, Noel naturally,\x01",
            "You can drive a driven car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PKeep the security guard free\x01",
            "I guess you can drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6POh is that right\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11PHaha … … Since joining,\x01",
            "Because it was crushed by the commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01003F#5PWell then, then,\x01",
            "I will give you guided cars.\x02\x03",
            "#01000FIt's parked just outside so come along\x02",
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
            "#00012F#5Pmy mother……\x01",
            "It's a soldier surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PYeah the director has his moments\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PBut an orbal car…\x02\x03",
            "#10300FI am not really familiar with it\x01",
            "Verne or Rheinfault's\x01",
            "Is it going to be one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PYeah, if I speak of a personal use guide car\x01",
            "There are only two big manufacturers.\x02\x03",
            "#10102FSo, Verne is more\x01",
            "Long-established store#4RCare#And the lineup is abundant.\x02\x03",
            "From small cars to medium size cars,\x01",
            "I handle it extensively to the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PLinefault has issued\x01",
            "There are many trucks and limousines right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PWell, if anything\x01",
            "There are many sturdy and upscale items.\x02\x03",
            "#10100FTechnique of power train and power tank\x01",
            "It seems that there are many things diverted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PWell …\x01",
            "I did not realize it suddenly\x01",
            "I was a bit nervous.\x02\x03",
            "#00000FOk let's go check it out\x02",
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

    # Function_26_A197 end

    def Function_27_BA5A(): pass

    label("Function_27_BA5A")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -3000, 0, 13250, 2000, 0x0)
    OP_95(0xFE, -6500, 0, 13250, 2000, 0x0)
    Return()

    # Function_27_BA5A end

    def Function_28_BA8A(): pass

    label("Function_28_BA8A")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 61500, 0, 18500, 2500, 0x0)
    OP_95(0xFE, 61500, 0, 6500, 2500, 0x0)
    Return()

    # Function_28_BA8A end

    def Function_29_BABA(): pass

    label("Function_29_BABA")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C308")

    ChrTalk(
        0x8,
        (
            "Oh, you guys\x01",
            "Is not it a mission support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, it was good.\x01",
            "It was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSecretary Huang ……\x01",
            "That is safe and than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FHere is the police force\x01",
            "You seem to be coming.\x02\x03",
            "#00103FAround this area the National Defense Forces\x01",
            "You guarded it … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, it is said that the President was detained\x01",
            "I got a newsletter and withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to get confused about each place,\x01",
            "The defense army has to work hard\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In exchange, support from the police headquarters came,\x01",
            "It is correcting the confusion of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303Fby the way……\x01",
            "Garcia's Osan\x01",
            "I wonder what happened after all?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE36")

    ChrTalk(
        0x105,
        (
            "#12P#10402FAlthough Lloyd is escaping a detention house\x01",
            "It was a story of lending power.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEF9")

    label("loc_BE36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE9B")

    ChrTalk(
        0x109,
        (
            "#12P#10100FAlthough Mr. Lloyd is escaping a detention house\x01",
            "It was a story of lending power.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEF9")

    label("loc_BE9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEF9")

    ChrTalk(
        0x106,
        (
            "#12P#10702FAlthough Mr. Lloyd is escaping a detention house\x01",
            "It was a story that I lent the power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEF9")


    ChrTalk(
        0x101,
        (
            "#12P#00000FOh … at that time\x01",
            "It really helped me.\x02\x03",
            "#00006FIt's truly like this\x01",
            "To say in such a place is#2RHida#Although it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, regarding your arrest,\x01",
            "Taking the President's detention\x01",
            "The unfairness was acknowledged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Regarding that point,\x01",
            "It will not be long before morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's Garcia ….\x01",
            "He roamed the defense army opponent heavily,\x01",
            "I was detained after a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now being detained again in detention centers,\x01",
            "I am receiving treatment.\x02",
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
        "#12P#00205FTreatment ……?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1A7")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHe fought with the Defense Army alone.\x01",
            "Its wear and tear should be known.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C277")

    label("loc_C1A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C20C")

    ChrTalk(
        0x106,
        (
            "#12P#10703FIf you fought with the Defense Forces alone ……\x01",
            "It probably was exhausted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C277")

    label("loc_C20C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C277")

    ChrTalk(
        0x109,
        (
            "#12P#10103FIf you fought with the Defense Forces alone ……\x01",
            "After all considerable\x01",
            "I guess there was exhaustion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C277")


    ChrTalk(
        0x8,
        (
            "Oh, for a while\x01",
            "Do not move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, if you wish,\x01",
            "It is possible to visit, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FLloyd, what are you going to do?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 1)
    Jump("loc_C383")

    label("loc_C308")


    ChrTalk(
        0x8,
        (
            "Garcia,\x01",
            "I was detained again in a jail\x01",
            "I am receiving treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish,\x01",
            "It is possible to visit, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C383")

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
            "To meet Garcia\x01",      # 0
            "To give up\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4BC")

    ChrTalk(
        0x101,
        (
            "#12P#00003F(To Garcia, at that time\x01",
            "I should reward you … …)\x02\x03",
            "#00000F…… Hoang Secretary, please come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me show you to Mr. Melvin.\x01",
            "Please come along with me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Jump("loc_C538")

    label("loc_C4BC")


    ChrTalk(
        0x101,
        "#12P#00003F…… I will stop now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you would like to see us\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C538")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_BABA end

    def Function_30_C568(): pass

    label("Function_30_C568")


    ChrTalk(
        0x101,
        (
            "#12P#00003F(To Garcia, at that time\x01",
            "I should reward you … …)\x02\x03",
            "#00000F…… Hoang Secretary, please come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me show you to Mr. Melvin.\x01",
            "Please come along with me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_C568 end

    def Function_31_C636(): pass

    label("Function_31_C636")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FThere is no errands on the other floor.\x01",
            "Too much uroplo\x01",
            "I will stop it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_31_C636 end

    def Function_32_C68A(): pass

    label("Function_32_C68A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_32_C68A end

    SaveToFile()

Try(main)
