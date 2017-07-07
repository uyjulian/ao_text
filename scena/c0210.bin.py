from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0210.bin",                # FileName
        "c0210",                    # MapName
        "c0210",                    # Location
        0x000B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 11, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0210",                  # 0
        "Oscar",               # 1
        "Morges",               # 2
        "Bennett",               # 3
        "Katerina",             # 4
        "Chiluru",                 # 5
        "Tully's",               # 6
        "Elsa",                 # 7
        "peach",                   # 8
        "Pete",                 # 9
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
        "chr/ch22200.itc",                   # 09
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(119120,  0,       4294966636, 275,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(58540,   0,       4294964967, 0,    261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(57799,   0,       4294965096, 0,    389,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(2589,    0,       1830,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  5,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  20, 0x0000)
    DeclActor(4294894916, 0,       8250,    1200,    4294894916, 2450,    8250,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(668, 0)                                        # 0

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_34C",          # 01, 1
        "Function_2_377",          # 02, 2
        "Function_3_662",          # 03, 3
        "Function_4_6BF",          # 04, 4
        "Function_5_772",          # 05, 5
        "Function_6_78C",          # 06, 6
        "Function_7_8F1",          # 07, 7
        "Function_8_2114",         # 08, 8
        "Function_9_24A4",         # 09, 9
        "Function_10_2586",        # 0A, 10
        "Function_11_2677",        # 0B, 11
        "Function_12_2759",        # 0C, 12
        "Function_13_3759",        # 0D, 13
        "Function_14_384B",        # 0E, 14
        "Function_15_3B1C",        # 0F, 15
        "Function_16_49BD",        # 10, 16
        "Function_17_4BDA",        # 11, 17
        "Function_18_5719",        # 12, 18
        "Function_19_57E1",        # 13, 19
        "Function_20_5872",        # 14, 20
        "Function_21_5876",        # 15, 21
        "Function_22_67B1",        # 16, 22
        "Function_23_6EFF",        # 17, 23
        "Function_24_7009",        # 18, 24
        "Function_25_73BB",        # 19, 25
        "Function_26_7AAE",        # 1A, 26
        "Function_27_905F",        # 1B, 27
        "Function_28_9537",        # 1C, 28
        "Function_29_A5B7",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2D4"),
        (1, "loc_2E0"),
        (2, "loc_2EC"),
        (3, "loc_2F8"),
        (4, "loc_304"),
        (5, "loc_310"),
        (6, "loc_31C"),
        (SWITCH_DEFAULT, "loc_328"),
    )


    label("loc_2D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_304")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_310")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_31C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_328")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_34B")

    Return()

    # Function_0_29C end

    def Function_1_34C(): pass

    label("Function_1_34C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_94(0xFE, 0xFFFFF308, 0x438, 0x7ED, 0x10B8, 0x3E8)
    Sleep(300)
    Jump("Function_1_34C")

    label("loc_376")

    Return()

    # Function_1_34C end

    def Function_2_377(): pass

    label("Function_2_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E6")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 123090, 0, 580, 90)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrPos(0xF, -68700, 0, 340, 180)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_652")

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_405")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    Jump("loc_652")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_440")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 56290, 0, 2020, 270)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    BeginChrThread(0xF, 0, 0, 1)
    Jump("loc_652")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_45D")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A8")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xF, 51240, 1000, 11020, 0)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C5")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_522")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_513")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_513")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_535")
    SetChrFlags(0xE, 0x80)
    Jump("loc_652")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_548")
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xF, -68700, 0, 340, 180)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A4")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_63F")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xA, 52620, 0, 4250, 90)
    SetChrPos(0xF, 53630, 0, 4250, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63A")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_63A")

    Jump("loc_652")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_652")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_661")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_661")

    Return()

    # Function_2_377 end

    def Function_3_662(): pass

    label("Function_3_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_695")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_6BE")

    Return()

    # Function_3_662 end

    def Function_4_6BF(): pass

    label("Function_4_6BF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Sweet Kingdom Volume 1\" is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_76E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Mix gelato\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_76E")

    TalkEnd(0xFF)
    Return()

    # Function_4_6BF end

    def Function_5_772(): pass

    label("Function_5_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_788")
    Call(0, 13)
    Jump("loc_78B")

    label("loc_788")

    Call(0, 6)

    label("loc_78B")

    Return()

    # Function_5_772 end

    def Function_6_78C(): pass

    label("Function_6_78C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C3")
    Call(0, 28)
    Return()

    label("loc_7C3")

    Jump("loc_7ED")

    label("loc_7C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED")
    Call(0, 26)
    Return()

    label("loc_7ED")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_858")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_858")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_877")
    OP_AF(0xCC)
    Jump("loc_8A9")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_887")
    OP_AF(0xCB)
    Jump("loc_8A9")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_897")
    OP_AF(0xCA)
    Jump("loc_8A9")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8A7")
    OP_AF(0xC9)
    Jump("loc_8A9")

    label("loc_8A7")

    OP_AF(0xC8)

    label("loc_8A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E8")

    label("loc_8B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_8E8")

    label("loc_8CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_8E8")

    Jump("loc_7FA")

    label("loc_8ED")

    TalkEnd(0x8)
    Return()

    # Function_6_78C end

    def Function_7_8F1(): pass

    label("Function_7_8F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90C")
    Call(0, 8)
    Jump("loc_2113")

    label("loc_90C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_927")
    Call(0, 9)
    Jump("loc_2113")

    label("loc_927")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Call(0, 10)
    Jump("loc_2113")

    label("loc_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95D")
    Call(0, 11)
    Jump("loc_2113")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A0E")

    ChrTalk(
        0x8,
        (
            "The earlier \"moist crisp sandwich\"\x01",
            "It is a prototype, it is not lining up in the shop front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "俺的にはBennettのパンを\x01",
            "I wanted to recommend it … ….\x01",
            "Well, I do not know a woman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF3")

    ChrTalk(
        0x8,
        "Oh, well came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For this time, for you\x01",
            "I made a special new bread.\x01",
            "Here, take it!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '最终旅途'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('最终旅途', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002FOh, it smells really nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FYeah, it looks very delicious ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, right?\x01",
            "It's the best we can do recently here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys will also be seriously tough,\x01",
            "I was eating that guy\x01",
            "Let's do our best and get over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh … That's right.\x01",
            "ありがとう、Oscar。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 4)
    Jump("loc_D70")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(
        0x8,
        (
            "It's such a time,\x01",
            "Bread of ours to various people\x01",
            "I want you to eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I make delicious bread\x01",
            "I can only do it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even a little guest who ate\x01",
            "If you can heal my uneasy feelings\x01",
            "There is nothing more than that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D70")

    label("loc_CD6")


    ChrTalk(
        0x8,
        (
            "anytime,\x01",
            "Keep making delicious bread\x01",
            "It's our job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A guest who ate bread 's bread\x01",
            "If it makes me happy a little\x01",
            "There is nothing more than that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D70")

    Jump("loc_2113")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F67")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "You … … Lloyd? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOscar……\x01",
            "Good, it looks like it was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, we have nothing but … …\x01",
            "Were you all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I mean Lloyd, you\x01",
            "I was wishing to be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, ah ……\x01",
            "Talking will get longer.\x02\x03",
            "#00000Fとにかく、Oscarたちは\x01",
            "Do not leave the room as it is\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well …\x01",
            "I do not know well what,\x01",
            "I understand it for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, you also\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 3)
    Jump("loc_FD1")

    label("loc_F67")


    ChrTalk(
        0x8,
        (
            "I do not know well what,\x01",
            "You guys were safe and relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, you also\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD1")

    Jump("loc_2113")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E6")

    ChrTalk(
        0x8,
        (
            "The railroad stopped stopping,\x01",
            "The stock of bread stocked\x01",
            "It seems to be missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, there is Almorika village\x01",
            "Even if you do not purchase ingredients from a foreign country\x01",
            "Surprisingly it seems to be managed somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, no matter what circumstances I am\x01",
            "I just keep making delicious bread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_117D")

    label("loc_10E6")


    ChrTalk(
        0x8,
        (
            "There is Almorika village\x01",
            "Even if you do not purchase ingredients from a foreign country\x01",
            "Surprisingly it seems to be managed somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, no matter what circumstances I am\x01",
            "I just keep making delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117D")

    Jump("loc_2113")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1190")
    Jump("loc_2113")

    label("loc_1190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1258")

    ChrTalk(
        0x8,
        (
            "Today from the morning,\x01",
            "Come visitors are complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Apparently from around the night of yesterday\x01",
            "She seems to be doing a mound in the mining direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a stuff … ….\x01",
            "I hope I do not have anything more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AB")

    label("loc_1258")


    ChrTalk(
        0x8,
        (
            "Denpatches in the direction of mines,\x01",
            "It's a stuff … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I hope I do not have anything more.\x02",
    )

    CloseMessageWindow()

    label("loc_12AB")

    Jump("loc_2113")

    label("loc_12B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(
        0x8,
        (
            "Bennettはなかなか\x01",
            "I'm having trouble with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though I heard about making bread,\x01",
            "While talking about stupidity\x01",
            "It tells us properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Look ah,\x01",
            "The roots are gentle guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13EE")

    label("loc_1377")


    ChrTalk(
        0x8,
        (
            "Well, you guys\x01",
            "Will you buy me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is a rainy day,\x01",
            "Freshly baked bread baked\x01",
            "Please eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EE")

    Jump("loc_2113")

    label("loc_13F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(
        0x8,
        (
            "Bennettの奴、厨房で\x01",
            "Kneading the wheat kneadingly,\x01",
            "I got hurt in my arm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I just had a poultice\x01",
            "I put it on … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is not good too much,\x01",
            "I have to look properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_154F")

    label("loc_14C6")


    ChrTalk(
        0x8,
        (
            "Well, that's a hard worker\x01",
            "Bennettのいいところでも\x01",
            "I have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To prevent your body from being destroyed too much,\x01",
            "I have to look properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F6")

    Jump("loc_2113")

    label("loc_15FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_175A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(
        0x8,
        (
            "Bennettの新作パン、\x01",
            "The sales are good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you praise that\x01",
            "\"Because I will not lose to you! \"And\x01",
            "I say while speaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I guess mightbe\x01",
            "I wonder if they are being hated ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1755")

    label("loc_16D2")


    ChrTalk(
        0x8,
        (
            "If you said something bad,\x01",
            "I should apologize later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bennettとはこれからも\x01",
            "Build delicious bread with strength\x01",
            "I want to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1755")

    Jump("loc_2113")

    label("loc_175A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(
        0x8,
        (
            "Bennettの新作パンは\x01",
            "I was also tasted,\x01",
            "Seriously my cheeks were about to fall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いやあ、さすがBennettだ。\x01",
            "I am losing too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_187B")

    label("loc_1804")


    ChrTalk(
        0x8,
        (
            "最近、Bennettは\x01",
            "Really tasty bread\x01",
            "I started to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is truly my daughter.\x01",
            "I am losing too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187B")

    Jump("loc_2113")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196A")

    ChrTalk(
        0x8,
        (
            "From early in the morning, reporters\x01",
            "I've caught up for a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Always, early morning customers are\x01",
            "A salaryman or a businessman\x01",
            "There are many … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the busy people\x01",
            "It is also easy to eat,\x01",
            "It is one of the appeal of bread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F8")

    label("loc_196A")


    ChrTalk(
        0x8,
        (
            "Busy people\x01",
            "It is also easy to eat,\x01",
            "It is one of the appeal of bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Morning reporters also\x01",
            "After eating our bread,\x01",
            "I hope you do your best day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_2113")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(
        0x8,
        (
            "At such a time\x01",
            "I do not know why\x01",
            "It is unusual, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once closing time is\x01",
            "It has passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you are OK.\x01",
            "Please do not hesitate to see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fサンキュー、Oscar。\x01",
            "We will do so by all means … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Or, even if you decide to shop\x01",
            "You'd better have done so early. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BBD")

    label("loc_1B59")


    ChrTalk(
        0x8,
        (
            "Once closing time is\x01",
            "It has passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you are OK.\x01",
            "Please do not hesitate to see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBD")

    Jump("loc_2113")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D87")

    ChrTalk(
        0x8,
        (
            "In the meantime, from a girl\x01",
            "\"I'm your fan\"……\x01",
            "I got a letter like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm different\x01",
            "Artists of alkane shell\x01",
            "Sorry about that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could you possibly give the opponent\x01",
            "I wonder if I made a mistake.\x01",
            "I will not return it when I come next time.\x02",
        )
    )

    CloseMessageWindow()
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
        0x101,
        (
            "#00006FWell, to return it indeed\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, is that so?\x01",
            "I do not understand well …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E1B")

    label("loc_1D87")


    ChrTalk(
        0x8,
        (
            "Even so ……\x01",
            "When I received a letter,\x01",
            "Bennettの様子が変だったな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "About content\x01",
            "I will ask you kindly ……\x01",
            "Did you want to read so much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1B")

    Jump("loc_2113")

    label("loc_1E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F24")

    ChrTalk(
        0x8,
        (
            "近頃、Bennettが前以上に\x01",
            "I started to make delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyday, even after the closing time has passed\x01",
            "I kept myself in the kitchen\x01",
            "It seems I'm practicing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I do not feel like this.\x01",
            "Bennettに負けないように、\x01",
            "I have to practice more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA3")

    label("loc_1F24")


    ChrTalk(
        0x8,
        (
            "Bennettに負けないように、\x01",
            "I have to practice more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right, it's all right.\x01",
            "Do not you let me practice?\x01",
            "Let's ask it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA3")

    Jump("loc_2113")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2089")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2084")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(
        0x8,
        (
            "Meilin-\x01",
            "Morse old man on east street\x01",
            "He should have been a granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry,\x01",
            "I will ask you afterwards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_203E")


    ChrTalk(
        0x8,
        "Thanks to you I was saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys are\x01",
            "I will depend on you ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")

    Return()

    label("loc_2084")

    Jump("loc_2113")

    label("loc_2089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2113")

    ChrTalk(
        0x8,
        (
            "Recently, more than before\x01",
            "You are challenging various new breads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I sometimes give free samples,\x01",
            "If you like it a lot\x01",
            "Please buy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2113")

    Return()

    # Function_7_8F1 end

    def Function_8_2114(): pass

    label("Function_8_2114")


    ChrTalk(
        0x8,
        "Oh, it is Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FやあOscar、久しぶり。\x01",
            "How is your work going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ou, the day after tomorrow\x01",
            "I am baking bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so,\x01",
            "I did not see the face much\x01",
            "Where have you been going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in a long stay in Michelin\x01",
            "Did you do it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FYou know.\x01",
            "I do not think so?\x02\x03",
            "#00001FAlso, \"for training\x01",
            "I will leave the support department once \"\x01",
            "You surely greeted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Was that so?\x01",
            "I was completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "whatever,\x01",
            "For the time being to commemorate the reunion\x01",
            "Please accept this one.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '赏月面包'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('赏月面包', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00105Fthis is……\x01",
            "It is an annual new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FOh, you have a nice smell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FIt looks delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, it's freshly baked,\x01",
            "I'm sure it will be delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To, if you like\x01",
            "Please buy any number of items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Oscar。\x01",
            "I will have it delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)
    Return()

    # Function_8_2114 end

    def Function_9_24A4(): pass

    label("Function_9_24A4")


    ChrTalk(
        0x8,
        "Oh, well came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "New bread is made today as well.\x01",
            "Try it to try it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '奶油菠萝包'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('奶油菠萝包', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Oscar。\x01",
            "I will have it delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 1)
    Return()

    # Function_9_24A4 end

    def Function_10_2586(): pass

    label("Function_10_2586")


    ChrTalk(
        0x8,
        "Oh, well came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this new bread,\x01",
            "Bennettの作ったパンだ。\x01",
            "Try it to try it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '贝奈特绝品'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贝奈特绝品', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Oscar。\x01",
            "I will have it delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Return()

    # Function_10_2586 end

    def Function_11_2677(): pass

    label("Function_11_2677")


    ChrTalk(
        0x8,
        "Oh, well came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "New bread is made today as well.\x01",
            "Try it to try it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '极厚猪排三明治'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('极厚猪排三明治', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Oscar。\x01",
            "I will have it delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Return()

    # Function_11_2677 end

    def Function_12_2759(): pass

    label("Function_12_2759")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285E")

    ChrTalk(
        0xFE,
        (
            "Whether it is government-supplied wheat flour\x01",
            "Delicious breads are decent\x01",
            "It was a place I could not make … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the traffic is restored\x01",
            "You get fresh Armorican produce.\x01",
            "Finally it is going to be restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OscarとBennettにも、\x01",
            "I guess you do not work harder than ever.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2903")

    label("loc_285E")


    ChrTalk(
        0xFE,
        (
            "Now that the traffic is restored\x01",
            "You get fresh Armorican wheat flour.\x01",
            "Finally I can make delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OscarとBennettにも、\x01",
            "I guess you do not work harder than ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2903")

    Jump("loc_3755")

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2988")

    ChrTalk(
        0xFE,
        (
            "No customers came by martial law,\x01",
            "Even in the study of new bread slowly\x01",
            "I thought I was going to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What is it all about?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7C")

    ChrTalk(
        0xFE,
        (
            "Two major powers to purchase ingredients\x01",
            "It became impossible to rely on,\x01",
            "A little stupid pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow,\x01",
            "Most bread ingredients are\x01",
            "It was imported from another country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a while only from Crossbell\x01",
            "Do you only have to work on it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B22")

    label("loc_2A7C")


    ChrTalk(
        0xFE,
        (
            "Hmm, but … …\x01",
            "\"Using 100 Crossbell Production\"\x01",
            "Rather it may be crap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, to that extent\x01",
            "What is not a story is nothing\x01",
            "I know that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B22")

    Jump("loc_3755")

    label("loc_2B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFE")

    ChrTalk(
        0xFE,
        (
            "Rebuild support sale\x01",
            "Although it is good to do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今日はOscarがいないから\x01",
            "Sorry for female customers ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, unusually parent-child only\x01",
            "Do the shop, as it is\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C89")

    label("loc_2BFE")


    ChrTalk(
        0xFE,
        (
            "今日はOscarがいないから\x01",
            "Sorry for female customers ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, unusually parent-child only\x01",
            "Do the shop, as it is\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C89")

    Jump("loc_3755")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D0A")

    ChrTalk(
        0xFE,
        (
            "Come on, the mining town\x01",
            "I heard that they were occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which on earth are you doing?\x01",
            "I can not forgive you … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD9")

    ChrTalk(
        0xFE,
        (
            "If it is true it will rainy day\x01",
            "What is a bakery?\x01",
            "The customer's foot will decrease, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will come even if it rains\x01",
            "There are many good customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, thankfully.\x01",
            "Thanks for keeping this for years as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5E")

    label("loc_2DD9")


    ChrTalk(
        0xFE,
        (
            "I will come even if it rains\x01",
            "There are many good people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, thank you.\x01",
            "This time, thankfully\x01",
            "I should do it even at sale.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5E")

    Jump("loc_3755")

    label("loc_2E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EAC")

    ChrTalk(
        0xFE,
        (
            "As the table says it is noisy … …\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F35")

    ChrTalk(
        0xFE,
        (
            "Bennettのやつ、\x01",
            "Thank you for your compliment\x01",
            "There is a rebound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder why it is … …\x01",
            "Well, son's personality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3013")

    ChrTalk(
        0xFE,
        (
            "Oscarの奴が\x01",
            "Bring me a disciple,\x01",
            "It will be a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "BennettもOscarのことを\x01",
            "It seems to be conscious …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "へへ、Oscarには\x01",
            "As it is as a son-in-law as it is\x01",
            "I suppose you will come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_308D")

    label("loc_3013")


    ChrTalk(
        0xFE,
        (
            "Oscarには、\x01",
            "Even as a son-in-law\x01",
            "I suppose you will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, for me, too\x01",
            "A traceable son is made\x01",
            "You know what I mean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308D")

    Jump("loc_3755")

    label("loc_3092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3121")

    ChrTalk(
        0xFE,
        (
            "I am going to cover the trade meeting this morning\x01",
            "It was a great success with reporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can sell so much,\x01",
            "More\x01",
            "I wish I had burned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_3121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_31AE")

    ChrTalk(
        0xFE,
        (
            "Let me see.\x01",
            "Are you going to clean up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bakery 's preparation,\x01",
            "Early in the morning from 3 o'clock.\x01",
            "Let's get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_31AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A0")

    ChrTalk(
        0xFE,
        (
            "Oscarは、ちょくちょく\x01",
            "Fan letter\x01",
            "I guess you got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since being introduced earlier in the magazine\x01",
            "Sometimes I feel like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, sales are also good,\x01",
            "Oscarのファンたちは\x01",
            "I hope you do not care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3330")

    label("loc_32A0")


    ChrTalk(
        0xFE,
        (
            "Also for sales of stores\x01",
            "Oscarのファンたちは\x01",
            "I hope you do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ただ、Bennettが\x01",
            "It is getting sick\x01",
            "I have scratches on the ball.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3330")

    Jump("loc_3755")

    label("loc_3335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_347F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FB")

    ChrTalk(
        0xFE,
        (
            "やれやれ、Bennettに\x01",
            "I was kicked out of the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently against bread making\x01",
            "It's a sense of imminence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess that's coming from improvement\x01",
            "It's a nice thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_347A")

    label("loc_33FB")


    ChrTalk(
        0xFE,
        (
            "Well, it's mumbling and pretty\x01",
            "I can hear my own solve\x01",
            "It is charming though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To motivate it\x01",
            "If it connects, it is OK in a sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_347A")

    Jump("loc_3755")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_35F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F5")

    ChrTalk(
        0xFE,
        (
            "You, you ….\x01",
            "Did you come by work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "詳しくはOscarたちに\x01",
            "Please listen to the story.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_34F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357C")

    ChrTalk(
        0xFE,
        (
            "Hurry up the bread dough\x01",
            "If you do not make it, to the baked afternoon\x01",
            "I can not make it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bad, but the matter of work\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_357C")


    ChrTalk(
        0xFE,
        (
            "An umbrella, is it a foundation?\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at peace of mind\x01",
            "Are you supposed to resume making bread?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EC")

    Jump("loc_3755")

    label("loc_35F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CA")

    ChrTalk(
        0xFE,
        (
            "Recently, most of new bread\x01",
            "OscarとBennett任せなのよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those are competing with each other\x01",
            "I have grown steadily,\x01",
            "I started to make good bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I leave the store among them\x01",
            "I guess it might be good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3755")

    label("loc_36CA")


    ChrTalk(
        0xFE,
        (
            "特に、娘のBennettの成長は\x01",
            "It's a nice miscalculation for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscarの存在が\x01",
            "I guess it is impossible to do it.\x01",
            "Rival is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3755")

    TalkEnd(0xFE)
    Return()

    # Function_12_2759 end

    def Function_13_3759(): pass

    label("Function_13_3759")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3787")
    Call(0, 29)
    Return()

    label("loc_3787")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3794")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3847")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_37F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3812")
    OP_AF(0xCB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3842")

    label("loc_3812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3826")
    Jump("loc_3842")

    label("loc_3826")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3842")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3842")

    Jump("loc_3794")

    label("loc_3847")

    TalkEnd(0xA)
    Return()

    # Function_13_3759 end

    def Function_14_384B(): pass

    label("Function_14_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_38D8")

    ChrTalk(
        0xA,
        (
            "Bad, but Miscon,\x01",
            "It is not a glass … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Charity cuisine,\x01",
            "Because I also helped\x01",
            "Then please forgive me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B1B")

    label("loc_38D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C0")

    ChrTalk(
        0xA,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As new bread is made,\x01",
            "Please eat it if you like.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '极厚猪排三明治'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('极厚猪排三明治', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThank you,\x01",
            "I will have it delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Jump("loc_3B1B")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A99")

    ChrTalk(
        0xA,
        (
            "Oscarは、\x01",
            "Charity event\x01",
            "I'm going to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although I could have done it\x01",
            "まあ、笑顔の素敵なOscarの方が\x01",
            "Energize everyone ………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… No, no now!\x01",
            "Please forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B1B")

    label("loc_3A99")


    ChrTalk(
        0xA,
        (
            "Well, well ….\x01",
            "I will protect the shop by myself\x01",
            "There is a mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The charity is\x01",
            "Oscarに任せたってわけ。\x01",
            "…… That's it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1B")

    Return()

    # Function_14_384B end

    def Function_15_3B1C(): pass

    label("Function_15_3B1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3BA2")

    ChrTalk(
        0xFE,
        (
            "Oscarめ……\x01",
            "My own bread into a magazine without permission\x01",
            "I'm trying to recommend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…, Huh, huh.\x01",
            "I wonder if I am going to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAD")

    ChrTalk(
        0xFE,
        (
            "私もOscarに負けないように、\x01",
            "New bread that makes everyone happy\x01",
            "I have to make a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However……\x01",
            "私のパンってOscarのには\x01",
            "I do not have enemies yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "こうなったら、Oscarに\x01",
            "May I have some advice?\x01",
            "… …. I am a little disappointed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D38")

    label("loc_3CAD")


    ChrTalk(
        0xFE,
        (
            "私のパンってOscarのには\x01",
            "I do not have enemies yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "こうなったら、Oscarに\x01",
            "May I have some advice?\x01",
            "… …. I am a little disappointed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D38")

    Jump("loc_49B9")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE4")

    ChrTalk(
        0xFE,
        "It's OK for the door lock …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… What is that monster?\x01",
            "We are attacking the citizens\x01",
            "It does not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is somewhat creepy …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E47")

    label("loc_3DE4")


    ChrTalk(
        0xFE,
        "Outside things are too creepy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because you do not attack citizens,\x01",
            "You can not be relieved as expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E47")

    Jump("loc_49B9")

    label("loc_3E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3D")

    ChrTalk(
        0xFE,
        (
            "Oscarも父さんも、\x01",
            "It is surprisingly positive for this situation, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I wonder if it's okay.\x01",
            "No matter how much Arios is\x01",
            "As expected two big countries are opponents ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, where I was worried\x01",
            "I do not care what happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FBB")

    label("loc_3F3D")


    ChrTalk(
        0xFE,
        (
            "No matter how much Arios is\x01",
            "As expected two big countries are opponents ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, where I was worried\x01",
            "I do not care what happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBB")

    Jump("loc_49B9")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FD5")
    TalkEnd(0xFE)
    Call(0, 13)
    Return()

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_40E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407D")

    ChrTalk(
        0xFE,
        (
            "… … That's right, for the next new work\x01",
            "Mix that herb … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Wow, sorry!\x01",
            "I was thinking for a moment.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_40DB")

    label("loc_407D")


    ChrTalk(
        0xFE,
        (
            "Next new bread\x01",
            "I was thinking about the idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, surely that herb is\x01",
            "It should have stockpile …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    Jump("loc_49B9")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40F1")
    Call(0, 16)
    Jump("loc_49B9")

    label("loc_40F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418A")

    ChrTalk(
        0xFE,
        "……むう、Oscarめ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put such a wet cloth\x01",
            "If you think that you can get in a good mood\x01",
            "It's a big mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … Hmm.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41EA")

    label("loc_418A")


    ChrTalk(
        0xFE,
        "Oscarめ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put such a wet cloth\x01",
            "If you think that you can get in a good mood\x01",
            "Because it is a big mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EA")

    Jump("loc_49B9")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_433D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B9")

    ChrTalk(
        0xFE,
        (
            "ぐぬぬ、Oscarめ……\x01",
            "I can not afford it … already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But that expression when I ate it,\x01",
            "It looks really tasty ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…, Different!\x01",
            "I was not happy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4338")

    label("loc_42B9")


    ChrTalk(
        0xFE,
        (
            "Wickedness, retirement, falling … …!\x01",
            "(Do not you know me?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar……\x01",
            "Next time is absolutely ~ ~ ~ ~ In pair,\x01",
            "I'm going to regret it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4338")

    Jump("loc_49B9")

    label("loc_433D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440E")

    ChrTalk(
        0xFE,
        (
            "せっかくOscarに勝てる\x01",
            "Although bread is finished,\x01",
            "Such a happy feeling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is different, is not it!\x01",
            "私が見たいのはOscarの\x01",
            "It is a face I regret … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ううう、Oscarめっ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_446E")

    label("loc_440E")


    ChrTalk(
        0xFE,
        (
            "Oscarめっ……\x01",
            "Why are you eating my bread\x01",
            "Such a happy feeling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please regret, you already!\x02",
    )

    CloseMessageWindow()

    label("loc_446E")

    Jump("loc_49B9")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_457B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450E")

    ChrTalk(
        0xFE,
        (
            "Customers, with my bread\x01",
            "Oscarのパンが並んでたら、\x01",
            "だいたいOscarのをとっていくの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, what is different … …!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4576")

    label("loc_450E")


    ChrTalk(
        0xFE,
        (
            "Eee, when that comes\x01",
            "There is no choice but to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "《Bennettスペシャル》を超える、\x01",
            "Have the supreme bread …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4576")

    Jump("loc_49B9")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_45E5")

    ChrTalk(
        0xFE,
        (
            "My bread,\x01",
            "Oscarのに\x01",
            "I'm losing in sales …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nearly, tomorrow is … !.\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_45E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AE")

    ChrTalk(
        0xFE,
        (
            "Oscar、この間は\x01",
            "She seems to have got a strange letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps, that way\x01",
            "Love letter … What! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little bread making\x01",
            "Because it is better than me\x01",
            "I feel bad!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_473C")

    label("loc_46AE")


    ChrTalk(
        0xFE,
        (
            "Oscarに\x01",
            "To give out a love letter,\x01",
            "Who is this guy …?! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, ___ ___ ___ 0\x01",
            "Well, I do not want to get such a thing\x01",
            "Oscarめっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473C")

    Jump("loc_49B9")

    label("loc_4741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47AB")

    ChrTalk(
        0xFE,
        "(Kitten: Do not worry)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grumbling ……\x01",
            "絶対Oscarなんかには\x01",
            "I will not lose … ….!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4885")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480D")

    ChrTalk(
        0xA,
        (
            "I left it for the umbrella.\x01",
            "Because this child takes care of me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4846")

    label("loc_480D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4822")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_4846")

    label("loc_4822")


    ChrTalk(
        0xA,
        "I am totally care of … …\x02",
    )

    CloseMessageWindow()

    label("loc_4846")

    TalkEnd(0xFE)
    Return()

    label("loc_484A")


    ChrTalk(
        0xA,
        "Hey, do not cry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You will definitely find it, are not you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_4885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494D")

    ChrTalk(
        0xFE,
        (
            "Welcome,\x01",
            "Freshly baked bread is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……ほとんどOscar作なのが\x01",
            "I'm pretty disappointed, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscarめ、いつか絶対に\x01",
            "I will overtake … …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49B9")

    label("loc_494D")


    ChrTalk(
        0xFE,
        (
            "Oscarめ、\x01",
            "I can not help it because it's really good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look now, absolutely\x01",
            "I will overtake … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B9")

    TalkEnd(0xFE)
    Return()

    # Function_15_3B1C end

    def Function_16_49BD(): pass

    label("Function_16_49BD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AB5")

    ChrTalk(
        0xA,
        (
            "Well then,\x01",
            "Tully'sさんちに\x01",
            "I will send it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… This time the forgotten thing is\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ah……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Freshly baked\x01",
            "I'm completely cooled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "… … Husband.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, now,\x01",
            "I will not cry because I replace it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD1")

    label("loc_4AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B89")

    ChrTalk(
        0xA,
        "You came to use today, did not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also losing umbrella\x01",
            "Do not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, yeah, good.\x01",
            "Together with the name here,\x01",
            "I also wrote the poster ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I see.\x01",
            "Then I'm relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4BD1")

    label("loc_4B89")


    ChrTalk(
        0xA,
        (
            "Huhu, you quite\x01",
            "The character is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I see.\x01",
            "Err …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD1")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_16_49BD end

    def Function_17_4BDA(): pass

    label("Function_17_4BDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7B")

    ChrTalk(
        0xFE,
        (
            "After all the bread here\x01",
            "It matches me, is not it?\x01",
            "I guess you get better when you eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My family also\x01",
            "I'd buy a lot and go home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CE5")

    label("loc_4C7B")


    ChrTalk(
        0xFE,
        (
            "そういえばChiluru、\x01",
            "I was talking about going on a trip again ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it is OK.\x01",
            "The road is still dangerous … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE5")

    Jump("loc_5715")

    label("loc_4CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CF8")
    Jump("loc_5715")

    label("loc_4CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D82")

    ChrTalk(
        0xFE,
        (
            "Chiluruも、\x01",
            "She seems to have returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What will happen now?\x01",
            "I do not know,\x01",
            "You ought to be with your family …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DAF")

    label("loc_4D82")


    ChrTalk(
        0xFE,
        (
            "I do not want to get down today.\x01",
            "I wonder if I will return …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAF")

    Jump("loc_5715")

    label("loc_4DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E34")

    ChrTalk(
        0xFE,
        (
            "Today it is a reconstruction supportive sale,\x01",
            "Some bread is half price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's painful,\x01",
            "I am going to buy a lot, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EB4")

    ChrTalk(
        0xFE,
        (
            "Today my mother,\x01",
            "Say it 's coming home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a case is going on,\x01",
            "There is no choice but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F4C")

    ChrTalk(
        0xFE,
        (
            "by the way……\x01",
            "The performance of the alkane shell\x01",
            "I wonder if it was tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I want to see it.\x01",
            "What kind of acts are rumored newcomers\x01",
            "I wonder … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F5A")
    Jump("loc_5715")

    label("loc_4F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F75")
    Call(0, 18)
    Jump("loc_4FEF")

    label("loc_4F75")


    ChrTalk(
        0xFE,
        (
            "… … that, somehow, from the back of the shop\x01",
            "Bennettさんの声が……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, new bread seems to be popular\x01",
            "You seem to be stuck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FEF")

    Jump("loc_5715")

    label("loc_4FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511C")

    ChrTalk(
        0xFE,
        (
            "Mumumu, this time the new bread\x01",
            "Bennettさんが作ったのね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To soft fluffy coppépan\x01",
            "Sandwiching strawberries and cream,\x01",
            "It's unbearably tasty …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luxurious toppings and ingredients\x01",
            "Contrary to the previous work which was characteristic,\x01",
            "Very cute bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I have to eat this!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5192")

    label("loc_511C")


    ChrTalk(
        0xFE,
        (
            "This time the new bread\x01",
            "Bennettさんが作ったみたい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Very pretty bread ……\x01",
            "Well, I have to eat this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5192")

    Jump("loc_5715")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51E9")

    ChrTalk(
        0xFE,
        (
            "Ah, my favorite\x01",
            "Morning Bread\x01",
            "It is sold out - ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_51E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_51F7")
    Jump("loc_5715")

    label("loc_51F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    ChrTalk(
        0xFE,
        (
            "そういえばChiluru、\x01",
            "I heard that he has returned from a trip this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come home when I return home\x01",
            "I wish I could contact him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's no problem\x01",
            "I wanted to have tea together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5321")

    label("loc_52B7")


    ChrTalk(
        0xFE,
        (
            "That girl, indeed at home\x01",
            "Someday you do not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While returning,\x01",
            "I wanted to have tea together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5321")

    Jump("loc_5715")

    label("loc_5326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53FD")

    ChrTalk(
        0xFE,
        (
            "Oh, this new bread …\x01",
            "It looks delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the moist melon\x01",
            "Custard cream\x01",
            "Gissiri included …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ちょっと太りそうHowever……\x01",
            "Yeah, I did not mind buying it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5454")

    label("loc_53FD")


    ChrTalk(
        0xFE,
        (
            "Such a delicious new bread,\x01",
            "If you do not eat it, it will be Son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I gotta buy some and go home.\x02",
    )

    CloseMessageWindow()

    label("loc_5454")

    Jump("loc_5715")

    label("loc_5459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_55DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_558A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551C")

    ChrTalk(
        0xFE,
        (
            "To be told, indeed,\x01",
            "Another pair of brother and sister came … …\x01",
            "It feels like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あのpeachって子と\x01",
            "It was about the same age\x01",
            "It may not be amusing …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_551C")


    ChrTalk(
        0xFE,
        (
            "Huhu, an umbrella was found\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I also bought some bread\x01",
            "I wonder if I will go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5586")

    TalkEnd(0xFE)
    Return()

    label("loc_558A")


    ChrTalk(
        0xFE,
        (
            "That crying child,\x01",
            "That's the daughter of the shop there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_55DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568E")

    ChrTalk(
        0xFE,
        "This time the new bread is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A fried egg like a full moon\x01",
            "Sandpaper muffin …\x01",
            "Oh, it looks delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He bought this new bread,\x01",
            "A cup of tea and going home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5715")

    label("loc_568E")


    ChrTalk(
        0xFE,
        (
            "Since I started attending this shop,\x01",
            "New bread checks\x01",
            "It has become a daily routine, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He bought this new bread,\x01",
            "A cup of tea and going home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5715")

    TalkEnd(0xFE)
    Return()

    # Function_17_4BDA end

    def Function_18_5719(): pass

    label("Function_18_5719")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Chiluru、どのパンが好き？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way, my recommendation is\x01",
            "This new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……Well then,\x01",
            "Let's do this.\x01",
            "It is somewhat cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is not it, is it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_18_5719 end

    def Function_19_57E1(): pass

    label("Function_19_57E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57F2")
    Jump("loc_586E")

    label("loc_57F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_586E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580D")
    Call(0, 18)
    Jump("loc_586E")

    label("loc_580D")


    ChrTalk(
        0xFE,
        (
            "When traveling, always here\x01",
            "I'm going to buy a boxed lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, this bread is cute ……\x02",
    )

    CloseMessageWindow()

    label("loc_586E")

    TalkEnd(0xFE)
    Return()

    # Function_19_57E1 end

    def Function_20_5872(): pass

    label("Function_20_5872")

    Call(0, 21)
    Return()

    # Function_20_5872 end

    def Function_21_5876(): pass

    label("Function_21_5876")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67AD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_58E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5900")
    OP_AF(0x31)
    Jump("loc_5982")

    label("loc_5900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5910")
    OP_AF(0x30)
    Jump("loc_5982")

    label("loc_5910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5920")
    OP_AF(0x2F)
    Jump("loc_5982")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5930")
    OP_AF(0x2E)
    Jump("loc_5982")

    label("loc_5930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5940")
    OP_AF(0x2D)
    Jump("loc_5982")

    label("loc_5940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5950")
    OP_AF(0x2C)
    Jump("loc_5982")

    label("loc_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5960")
    OP_AF(0x2B)
    Jump("loc_5982")

    label("loc_5960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5970")
    OP_AF(0x2A)
    Jump("loc_5982")

    label("loc_5970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5980")
    OP_AF(0x29)
    Jump("loc_5982")

    label("loc_5980")

    OP_AF(0x28)

    label("loc_5982")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67A8")

    label("loc_5991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59A5")
    Jump("loc_67A8")

    label("loc_59A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABD")

    ChrTalk(
        0xD,
        (
            "The situation where trade is impossible is still continuing,\x01",
            "The circumstances that you can not stock items satisfactorily\x01",
            "Sure there are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For the first time in the form of the original crossbell\x01",
            "I was relieved to be back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let your family live with peace of mind\x01",
            "I also have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B68")

    label("loc_5ABD")


    ChrTalk(
        0xD,
        (
            "There is still pain that I can not trade ….\x01",
            "For the first time in the form of the original crossbell\x01",
            "I was relieved to be back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let your family live with peace of mind\x01",
            "I also have to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B68")

    Jump("loc_67A8")

    label("loc_5B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C16")

    ChrTalk(
        0xD,
        (
            "Wow, what on earth is it,\x01",
            "What medicine like a medieval armor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyway, even at such times\x01",
            "He came to the store … ….\x01",
            "If you have something you want, tell me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD9")

    ChrTalk(
        0xD,
        (
            "When asking Mr. Dieter's speech,\x01",
            "I think that independence is useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Before this, what kind of danger\x01",
            "I do not know whether there are … …\x01",
            "peachとElsaは、\x01",
            "At any rate I must protect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5D3E")

    label("loc_5CD9")


    ChrTalk(
        0xD,
        (
            "Before this, what kind of danger\x01",
            "I do not know whether there are … …\x01",
            "peachとElsaは、\x01",
            "At any rate I must protect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D3E")

    Jump("loc_67A8")

    label("loc_5D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DCA")

    ChrTalk(
        0xD,
        (
            "Hi, welcome,\x01",
            "Tully's商店へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Focusing on essential necessities\x01",
            "Because I am selling,\x01",
            "Take a look if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E91")

    ChrTalk(
        0xD,
        (
            "Example of Mainz incident ……\x01",
            "Empire is drawing strings behind\x01",
            "There is also rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What innocent civilians\x01",
            "I do not get involved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If rumors are true,\x01",
            "I can not forgive the empire.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F0C")

    label("loc_5E91")


    ChrTalk(
        0xD,
        (
            "Perhaps,\x01",
            "What was the target\x01",
            "It might have been this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If rumors are true,\x01",
            "I can not forgive the empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F0C")

    Jump("loc_67A8")

    label("loc_5F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5FBF")

    ChrTalk(
        0xD,
        (
            "Yesterday's derailment accident,\x01",
            "It seems that some injured people have come out\x01",
            "It seems that I managed to recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I am relying on rail services for stocking\x01",
            "There will be many places, too,\x01",
            "Everyone was relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_60EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6080")

    ChrTalk(
        0xD,
        (
            "The ambulance sounded,\x01",
            "I hurried out of the store … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Fuu …\x01",
            "peachじゃなかったようで\x01",
            "I was relieved a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But there are so many … …\x01",
            "What on earth happened?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60EA")

    label("loc_6080")


    ChrTalk(
        0xD,
        (
            "There are many ambulances\x01",
            "It seems to be passing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To children playing on the street\x01",
            "I have to tell him to keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EA")

    Jump("loc_67A8")

    label("loc_60EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_616D")

    ChrTalk(
        0xD,
        (
            "今日はpeachたちは、\x01",
            "It looks like I'm playing on the street there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Traffic volume is increasing recently,\x01",
            "I want you to be careful about the car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_616D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_62A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6234")

    ChrTalk(
        0xD,
        (
            "From the Empire and the Republic\x01",
            "Crossbell is independent\x01",
            "I think it's a good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, if you become independent\x01",
            "To turn the two major powers into enemies\x01",
            "It will be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, it's a difficult problem.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_629E")

    label("loc_6234")


    ChrTalk(
        0xD,
        (
            "Crossbell is independent\x01",
            "I think it's a good thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To turn the empire and the republic into enemies\x01",
            "After all it is scary, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_629E")

    Jump("loc_67A8")

    label("loc_62A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6329")

    ChrTalk(
        0xD,
        (
            "Next Crossbell Times\x01",
            "The topic of the trade council is one aspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It seems to be able to anticipate sales,\x01",
            "Let's stock in more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_6329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_63A2")

    ChrTalk(
        0xD,
        (
            "Well done,\x01",
            "Do you need anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Store a bit more\x01",
            "Because I am planning to open it,\x01",
            "You may be slow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_63A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_64EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6466")

    ChrTalk(
        0xD,
        (
            "Today is the Orkis Tower\x01",
            "It was a showcase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, even if I take out the shop\x01",
            "I wanted to go see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huhu, huge buildings and vehicles\x01",
            "Because the boy's eternal longing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64E9")

    label("loc_6466")


    ChrTalk(
        0xD,
        (
            "Like the Orkis Tower\x01",
            "Huge buildings and vehicles,\x01",
            "Because the boy's eternal longing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At any age\x01",
            "It is a thing to beat up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E9")

    Jump("loc_67A8")

    label("loc_64EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_664A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C6")

    ChrTalk(
        0xD,
        (
            "Well in the city\x01",
            "I'll see a police guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At the Trade Council each country\x01",
            "It seems that we are coming,\x01",
            "It seems to be prepared for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "僕も、peachが何かの事件に\x01",
            "I am in trouble if I get caught,\x01",
            "I hope you do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6645")

    label("loc_65C6")


    ChrTalk(
        0xD,
        (
            "Police alert in the city\x01",
            "It seems to be strengthening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "僕も、peachが何かの事件に\x01",
            "I am in trouble if I get caught,\x01",
            "I hope you do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6645")

    Jump("loc_67A8")

    label("loc_664A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_672D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F5")

    ChrTalk(
        0xD,
        (
            "peachが今日、パン屋へ\x01",
            "I am going to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But …\x01",
            "I wish I could go home lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What was the bread you ordered?\x01",
            "I do not understand\x01",
            "Did I do it …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6728")

    label("loc_66F5")


    ChrTalk(
        0xD,
        (
            "peach、随分帰りが遅いなあ。\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6728")

    Jump("loc_67A8")

    label("loc_672D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_67A8")

    ChrTalk(
        0xD,
        (
            "Hi, welcome.\x01",
            "《Tully's商店》にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If it is a daily necessity leave it to me.\x01",
            "Please feel free to use it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A8")

    Jump("loc_5883")

    label("loc_67AD")

    TalkEnd(0xD)
    Return()

    # Function_21_5876 end

    def Function_22_67B1(): pass

    label("Function_22_67B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_695F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B5")

    ChrTalk(
        0xFE,
        (
            "peachったら、友達と一緒に\x01",
            "I want to do something for everyone in the city\x01",
            "I jumped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachがあんなふうに一所懸命に\x01",
            "It was the first time I claimed my intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外で遊ばせるのはまだ心配However……\x01",
            "今はpeachの気持ちを尊重したいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_695A")

    label("loc_68B5")


    ChrTalk(
        0xFE,
        (
            "peachったら、友達と一緒に\x01",
            "I want to do something for everyone in the city\x01",
            "I jumped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外で遊ばせるのはまだ心配However……\x01",
            "今はpeachの気持ちを尊重したいかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_695A")

    Jump("loc_6EFB")

    label("loc_695F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69D9")

    ChrTalk(
        0xFE,
        (
            "No way, that sort of thing\x01",
            "It appears to appear in the city …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the president's offer\x01",
            "I wonder what was the meaning of martial law …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_69D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAC")

    ChrTalk(
        0xFE,
        (
            "The situation of the crossbell is now\x01",
            "It seems to be unstable …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachには悪いけど……\x01",
            "After all, for a while\x01",
            "I can not let you play outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without reaching the eyes\x01",
            "I can not help it anxious … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6B27")

    label("loc_6AAC")


    ChrTalk(
        0xFE,
        (
            "peachには悪いけど……\x01",
            "After all, for a while\x01",
            "I can not let you play outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without reaching the eyes\x01",
            "I can not help it anxious … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B27")

    Jump("loc_6EFB")

    label("loc_6B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BBA")

    ChrTalk(
        0xFE,
        (
            "……peachを外で遊ばせるのが\x01",
            "I was completely scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a week since then,\x01",
            "I'd like to think it's okay ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_6BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6BC8")
    Jump("loc_6EFB")

    label("loc_6BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C33")

    ChrTalk(
        0xFE,
        (
            "Take a beef stew today\x01",
            "バゲットをpeachに頼んだの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I will return soon ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_6C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C41")
    Jump("loc_6EFB")

    label("loc_6C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C4F")
    Jump("loc_6EFB")

    label("loc_6C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C5D")
    Jump("loc_6EFB")

    label("loc_6C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2B")

    ChrTalk(
        0xFE,
        (
            "peach、今日もリュウくんたちと\x01",
            "I'm going out to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That child was a shy away idea,\x01",
            "It seems that it has gone recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, to Ryu-kun\x01",
            "I must thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D6B")

    label("loc_6D2B")


    ChrTalk(
        0xFE,
        (
            "さてと、peachは今日も\x01",
            "Let me hunger\x01",
            "I wonder if they will come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D6B")

    Jump("loc_6EFB")

    label("loc_6D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D90")
    Call(0, 23)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_6DC7")

    label("loc_6D90")


    ChrTalk(
        0xFE,
        (
            "ふふ、peachったらよっぽど\x01",
            "I guess it was fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC7")

    Jump("loc_6EFB")

    label("loc_6DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DDA")
    Jump("loc_6EFB")

    label("loc_6DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DE8")
    Jump("loc_6EFB")

    label("loc_6DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7F")

    ChrTalk(
        0xFE,
        (
            "peachったら、雨なのに\x01",
            "Excitingly\x01",
            "You went to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, to your father\x01",
            "The umbrella you bought\x01",
            "You seemed to want to use it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6EED")

    label("loc_6E7F")


    ChrTalk(
        0xFE,
        (
            "peachの傘は、お父さんが\x01",
            "I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachの好きなピンク色で、\x01",
            "You seem to like it very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EED")

    Jump("loc_6EFB")

    label("loc_6EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6EFB")

    label("loc_6EFB")

    TalkEnd(0xFE)
    Return()

    # Function_22_67B1 end

    def Function_23_6EFF(): pass

    label("Function_23_6EFF")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "… That's why.\x01",
            "Ryu at the Orkis Tower\x01",
            "I tried getting into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "そしたら、peachとアンリちゃんまで\x01",
            "Police officers are getting upset …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh dear……\x01",
            "It was a difficult task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But you know.\x01",
            "It was a lot of fun …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_23_6EFF end

    def Function_24_7009(): pass

    label("Function_24_7009")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_701A")
    Jump("loc_73B7")

    label("loc_701A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7068")

    ChrTalk(
        0xFE,
        "Uoo, outside Kawai …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ryu-kun, are you okay …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_7068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_70D2")

    ChrTalk(
        0xFE,
        (
            "Mom and Dad,\x01",
            "It looks very uneasy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachも、なんだか\x01",
            "I got worried … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_70D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7149")

    ChrTalk(
        0xFE,
        (
            "Recently, outside\x01",
            "When I go to play\x01",
            "I will be stopped by Mama … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With Ryu kimitachi\x01",
            "You want to play ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_7149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7157")
    Jump("loc_73B7")

    label("loc_7157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7168")
    Call(0, 16)
    Jump("loc_73B7")

    label("loc_7168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7176")
    Jump("loc_73B7")

    label("loc_7176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7184")
    Jump("loc_73B7")

    label("loc_7184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_71F3")

    ChrTalk(
        0xFE,
        "I am helping the shop today ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can not just play around.\x01",
            "I have to help you properly …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_71F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7201")
    Jump("loc_73B7")

    label("loc_7201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_72BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721C")
    Call(0, 23)
    Jump("loc_72B6")

    label("loc_721C")


    ChrTalk(
        0xFE,
        (
            "But Ryuu was funny.\x01",
            "Because of everything Henri\x01",
            "I tried to do … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it got caught quickly,\x01",
            "I got scolded more.\x01",
            "Giggle\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B6")

    Jump("loc_73B7")

    label("loc_72BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_72C9")
    Jump("loc_73B7")

    label("loc_72C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72D7")
    Jump("loc_73B7")

    label("loc_72D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_73AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7391")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7353")

    ChrTalk(
        0xF,
        "That umbrella is an important thing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Dusk, dusk … …\x01",
            "Please, my brother ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_738D")

    label("loc_7353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7368")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_738D")

    label("loc_7368")


    ChrTalk(
        0xF,
        (
            "Well,\x01",
            "I'm kind with your sister ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738D")

    TalkEnd(0xFE)
    Return()

    label("loc_7391")


    ChrTalk(
        0xF,
        "Dusk, dusk … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_73AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73B7")

    label("loc_73B7")

    TalkEnd(0xFE)
    Return()

    # Function_24_7009 end

    def Function_25_73BB(): pass

    label("Function_25_73BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A47")

    ChrTalk(
        0xFE,
        "Oh, everyone at the Special Affairs Support Division … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou are Mr. Ian's assistant\x01",
            "Pete君じゃないか。\x02\x03",
            "#00001F１人みたいHowever……\x01",
            "What did the teacher do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Ian saw this situation\x01",
            "To protest to the Orkis Tower\x01",
            "I have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After taking care of me here,\x01",
            "I can not get in touch ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_78D2")

    ChrTalk(
        0x102,
        "#00106FMr. Ian is … I am worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FWhen I go to the tower,\x01",
            "Maybe the president\x01",
            "It may have been restrained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FYou'd better hurry but it looks good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F……Pete君。\x02\x03",
            "#00001FIn addition to Dr. Ian,\x01",
            "Did not you say something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "by the way……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The teacher, what?\x01",
            "I was saying something to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once this situation has been met,\x01",
            "Go back to the office and bring your teacher's desk\x01",
            "Please clean it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fclean up……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I will hurry and go out first\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always cleaning my teacher who I am leaving\x01",
            "Try not to touch the desk as much as possible\x01",
            "I usually said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For work, assistant's servant\x01",
            "Because many things can not be shown\x01",
            "I was leaving it as it was ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FMr. Ian is … …\x01",
            "Certainly it is interesting …\x02\x03",
            "#00106FAt such timing\x01",
            "To ask for cleaning,\x01",
            "I'm not sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",
            "#00000FPete君、イアン先生のことは\x01",
            "Leave it to us, you are like this\x01",
            "Please evacuate here.\x02\x03",
            "If you know something\x01",
            "I will contact you soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A08")

    label("loc_78D2")


    ChrTalk(
        0x102,
        "#00106FMr. Ian is … I am worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FWhen I go to the tower,\x01",
            "Maybe the president\x01",
            "It may have been restrained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FYou'd better hurry but it looks good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x02\x03",
            "#00000FPete君、イアン先生のことは\x01",
            "Leave it to us, you are like this\x01",
            "Please evacuate here.\x02\x03",
            "If you know something\x01",
            "I will contact you soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A08")


    ChrTalk(
        0xFE,
        (
            "Wow, I understand …\x01",
            "Nice to meet you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 5)
    Jump("loc_7AAA")

    label("loc_7A47")


    ChrTalk(
        0xFE,
        (
            "Everyone, Professor Ian is\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Teacher … I hope it is safe.\x02",
    )

    CloseMessageWindow()

    label("loc_7AAA")

    TalkEnd(0xFE)
    Return()

    # Function_25_73BB end

    def Function_26_7AAE(): pass

    label("Function_26_7AAE")

    EventBegin(0x0)
    Fade(500)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_END)), "loc_7C01")

    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、Oscar。\x01",
            "I asked for a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POu, Lloyd!\x01",
            "I thought you would come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FSoon it is,\x01",
            "Please listen to the circumstances in detail\x01",
            "Is that okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E5D")

    label("loc_7C01")


    ChrTalk(
        0x101,
        (
            "#6P#00000FやあOscar、久しぶり。\x01",
            "I asked for a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, it is Lloyd!\x01",
            "I thought you would come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven so,\x01",
            "I did not see the face much\x01",
            "Where have you been going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven in a long stay in Michelin\x01",
            "Did you do it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FYou know.\x01",
            "I do not think so?\x02\x03",
            "#00001FAlso, \"for training\x01",
            "I will leave the support department once \"\x01",
            "You surely greeted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWas that so?\x01",
            "I was completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Oh, the story has gone.\x01",
            "Do not talk about this request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell, immediately,\x01",
            "Please let me know the details in detail.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)

    label("loc_7E5D")


    ChrTalk(
        0x8,
        (
            "#11POh, I asked,\x01",
            "そこにいるpeachちゃんの事でな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTully's商店さんちの子供なんだが、\x01",
            "Today I was wearing a rainy umbrella\x01",
            "He came to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHowever……\x02",
    )

    CloseMessageWindow()
    OP_68(53460, 1500, 2390, 2000)

    def lambda_7F28():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7F28)
    Sleep(10)

    def lambda_7F38():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7F38)
    Sleep(10)

    def lambda_7F48():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F48)
    Sleep(10)

    def lambda_7F58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F58)
    Sleep(10)

    def lambda_7F68():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7F68)
    Sleep(10)

    def lambda_7F78():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7F78)
    WaitChrThread(0x105, 2)
    OP_6F(0x1)

    ChrTalk(
        0xF,
        "……Dusk, dusk … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "peachの、peachの、\x01",
            "An important pink umbrella\x01",
            "I went somewhere …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P…… That's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005Fgot it……\x02\x03",
            "#00001FDid you try looking inside and outside the shop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "一応、Oscarと私で\x01",
            "I searched for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then then …\x01",
            "Such a thing came out.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennettはピンクの傘を差し出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10105FLet me see……?\x01",
            "This pink umbrella ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FThis is that girl's\x01",
            "Is not it an umbrella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "私もそう思ったんHowever……\x01",
            "Look at the part here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennettは、傘の柄の部分を\x01",
            "I pointed to Lloyd's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#12P#00100F\"Melin\" ……\x01",
            "I have written it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003Fgot it……\x02\x03",
            "#00000FIn short, wrong\x01",
            "Been taken\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, it looks like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PToday it is raining and few customers,\x01",
            "There were a couple of other customers in the\x01",
            "I remember … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBy no means\x01",
            "\"Meirin\" is the name\x01",
            "I do not know who it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI managed to find this owner,\x01",
            "I got it by mistake\x01",
            "I would like you to collect your umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHow are you likely to do?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, I understand.\x01",
            "Leave it to us.\x02\x03",
            "I'm surely finding an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, I asked, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut that's right.\x01",
            "This \"Meirin\" is a name ……\x01",
            "I want a little more clues.\x02\x03",
            "#00100FLloyd, did not I?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84E9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E9)
    Sleep(50)

    def lambda_84F9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_84F9)
    Sleep(50)

    def lambda_8509():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8509)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FI agree,\x01",
            "I talked about once\x01",
            "Would you mind?\x02\x03",
            "#10106FAt least, which city block\x01",
            "I hope I can understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FWell, how was it ……\x01",
            "(Surely something I heard somewhere\x01",
            "There is sort of such, not like ……)\x02\x03",
            "#00000F\"Melin\" is a child, sure …\x02",
        )
    )

    CloseMessageWindow()
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
            "Residents of the central square\x01",      # 0
            "Residents of Nishi-dori\x01",        # 1
            "Residents of residential areas\x01",        # 2
            "Residents of east street\x01",        # 3
            "Residents of the port area\x01",        # 4
            "Residents of the province\x01",        # 5
            "Residents of the red light district\x01",        # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8890")
    OP_2C(0x6B, 0x1)

    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in East Street\x01",
            "Was not she the name of a girl?\x02\x03",
            "Certainly Mr. Mrs., Chairman of the Chamber of Commerce\x01",
            "I feel like I was a grandchild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#12P#00105FOh, that's right … …!\x01",
            "I have spoken a number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FRoy's\x01",
            "A child with an older brother.\x02\x03",
            "#10300FThen here is my brother and sister\x01",
            "Have you come to shopping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Oh, that's right!\x01",
            "Certainly there were some customers who came with brothers and sisters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHowever, Mr. Morse 's grandson.\x01",
            "I certainly have seen it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D15")

    label("loc_8890")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_88BE"),
        (1, "loc_8909"),
        (2, "loc_8952"),
        (4, "loc_899B"),
        (5, "loc_89E4"),
        (6, "loc_8A2D"),
        (SWITCH_DEFAULT, "loc_8A76"),
    )


    label("loc_88BE")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in central square\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8909")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in Nishi-dori\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8952")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in a residential area\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_899B")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in a port area\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_89E4")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in an administrative district\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8A2D")


    ChrTalk(
        0x101,
        (
            "#11P#00000F…… I live in the red light district\x01",
            "Was not she the name of a girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8A76")


    ChrTalk(
        0x105,
        "#6P#10304FNo, it is not.\x02",
    )

    CloseMessageWindow()

    def lambda_8A99():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A99)
    Sleep(50)

    def lambda_8AA9():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8AA9)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSpeaking of \"Meilin\"\x01",
            "Chairman of the Chamber of Commerce of East Road,\x01",
            "It's Mr. Mrs's granddaughter's name.\x02\x03",
            "#10304FThere is an older brother Roy,\x01",
            "Maybe here are brothers and sisters\x01",
            "I guess it was coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Oh, that's right!\x01",
            "Certainly there were some customers who came with brothers and sisters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FReally……\x01",
            "Was it Mr. Mrs.'s grandchild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBy the way, several times\x01",
            "I had something to talk about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FBut you know well, are not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWhen I have a byte of host, host\x01",
            "Information comes in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI see, I see … ….\x01",
            "I can not admire it much though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FSomewhat.\x01",
            "Anyway, I was saved, Wadi.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D15")


    ChrTalk(
        0x8,
        (
            "#11PAll right, then\x01",
            "Meilin's umbrella\x01",
            "I'll leave it with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, this is it.\x02",
    )

    CloseMessageWindow()

    def lambda_8D74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D74)
    Sleep(50)

    def lambda_8D84():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D84)
    Sleep(50)

    def lambda_8D94():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D94)
    Sleep(50)

    def lambda_8DA4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8DA4)
    Sleep(50)

    def lambda_8DB4():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8DB4)
    WaitChrThread(0xA, 2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '梅琳的伞'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('梅琳的伞', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0xA, 0xB4, 0x3E8, 0x5DC, 0x0)

    ChrTalk(
        0x8,
        (
            "#11PTo Meirin chan\x01",
            "返した上で、peachちゃんの傘を\x01",
            "Please take care of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI asked, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Dusk, dusk … …\x01",
            "Onii-chan, please …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell then,\x01",
            "Once you have Mr. Morse's house\x01",
            "It looks good to visit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F3B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F3B)
    Sleep(50)

    def lambda_8F4B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8F4B)
    Sleep(50)

    def lambda_8F5B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8F5B)

    ChrTalk(
        0x101,
        (
            "#5P#00000FTo be sure, it is out of east street\x01",
            "It was your home.\x02\x03",
            "Tentatively\x01",
            "Let's go and try.\x02",
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
            "Quest 【Searching for missing umbrellas】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x132, 3)
    OP_29(0x6B, 0x1, 0x0)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    EventEnd(0x5)
    Return()

    # Function_26_7AAE end

    def Function_27_905F(): pass

    label("Function_27_905F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11POh, Lloyd!\x01",
            "How was the success?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, I could recover safely.\x02",
    )

    CloseMessageWindow()

    def lambda_9161():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9161)
    Sleep(10)

    def lambda_9171():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9171)
    Sleep(10)

    def lambda_9181():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9181)
    Sleep(10)

    def lambda_9191():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9191)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000Fはい、peachちゃん。\x01",
            "Please do this.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Ipeachの傘\x07\x00",
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('梅琳的伞', 1)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)

    ChrTalk(
        0xF,
        (
            "Gusun …\x01",
            "あっ……peachの傘……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "これ、お父さんがpeachのために\x01",
            "It is an important thing that I bought … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, thanks …\x01",
            "Thank you so much …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOh, it was.\x02\x03",
            "#10100FHuhu, come back.\x01",
            "good for you\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Wow …!\x02",
    )

    CloseMessageWindow()

    def lambda_9345():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9345)
    Sleep(50)

    def lambda_9355():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9355)
    Sleep(50)

    def lambda_9365():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9365)
    Sleep(50)

    def lambda_9375():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9375)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, at this\x01",
            "It's a case of one settling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PThanks to you I was saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou guys are\x01",
            "I will depend on you ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there is something again\x01",
            "I'm begging for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYes, you can always make a request\x01",
            "We look forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000Fそれじゃあな、Oscar。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Searching for missing umbrellas】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_29(0x6B, 0x1, 0x5)
    OP_29(0x6B, 0x1, 0x6)
    OP_29(0x6B, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_27_905F end

    def Function_28_9537(): pass

    label("Function_28_9537")

    EventBegin(0x0)
    Fade(500)
    OP_68(52330, 2200, -660, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23210, 0)
    SetChrPos(0x101, 53850, 0, 1490, 90)
    SetChrPos(0x102, 53850, 0, 500, 90)
    SetChrPos(0x103, 52650, 0, 1490, 90)
    SetChrPos(0x109, 52650, 0, 500, 90)
    SetChrPos(0x104, 51450, 0, 1490, 90)
    SetChrPos(0x105, 51450, 0, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_971A")

    ChrTalk(
        0x8,
        "Oh, well came Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this new bread,\x01",
            "Bennettの作ったパンだ。\x01",
            "Try it to try it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '贝奈特绝品'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贝奈特绝品', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、Oscar。\x01",
            "後でI will have it delicious.\x02\x03",
            "I came here at work today ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9786")

    label("loc_971A")


    ChrTalk(
        0x8,
        (
            "Oh, well came Lloyd.\x01",
            "Did you come to buy our bread?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fえっと、I came here at work today ….\x02",
    )

    CloseMessageWindow()

    label("loc_9786")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, that's right.\x01",
            "I wonder there was such a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right, my bread is\x01",
            "I recommend everything ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987E")

    ChrTalk(
        0x8,
        (
            "If it says strongly,\x01",
            "I gave it to you a little while ago.\x01",
            "『Bennettワンダフル』だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Jump("loc_98C3")

    label("loc_987E")


    ChrTalk(
        0x8,
        (
            "If it says strongly, I also did it to you\x01",
            "『Bennettワンダフル』だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98C3")


    ChrTalk(
        0x102,
        "#00105FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ああ、Bennettが作ったパンでも\x01",
            "This guy is really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今の《Morges》なら、\x01",
            "Undoubtedly the best delicious ─\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Bennettの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Wait a moment, please!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_99AA():

        label("loc_99AA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99AA")

    QueueWorkItem2(0x109, 0, lambda_99AA)

    def lambda_99BC():

        label("loc_99BC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99BC")

    QueueWorkItem2(0x102, 0, lambda_99BC)

    def lambda_99CE():

        label("loc_99CE")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99CE")

    QueueWorkItem2(0x104, 0, lambda_99CE)

    def lambda_99E0():

        label("loc_99E0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99E0")

    QueueWorkItem2(0x101, 0, lambda_99E0)

    def lambda_99F2():

        label("loc_99F2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99F2")

    QueueWorkItem2(0x105, 0, lambda_99F2)

    def lambda_9A04():

        label("loc_9A04")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9A04")

    QueueWorkItem2(0x103, 0, lambda_9A04)

    def lambda_9A16():

        label("loc_9A16")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9A16")

    QueueWorkItem2(0x8, 1, lambda_9A16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AB1")
    OP_68(55480, 1510, 1690, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9A64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9A64)
    SetChrPos(0xA, 60080, 10, 4000, 135)
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 57580, 10, 2090, 3000, 0x0)
    OP_64(0xA)
    Jump("loc_9B32")

    label("loc_9AB1")

    OP_68(52700, 1510, 1930, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrPos(0xA, 52110, 1000, 10270, 315)
    ClearChrFlags(0xA, 0x4)
    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 53600, 0, 4100, 3000, 0x0)
    OP_64(0xA)

    label("loc_9B32")

    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "おう、Bennett。\x01",
            "Right now, just for your bread -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Do not do it selfishly!\x01",
            "For me that bread,\x01",
            "Because it is still an unfinished item!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oscarを超える\x01",
            "Until bread is made,\x01",
            "What a gourmet guide …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, is not it good?\x01",
            "That's because it's such delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "… ….! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And anyway … …\x01",
            "If you decide to recommend it without permission\x01",
            "I do not agree! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2D")
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 60330, 0, 3200, 3000, 0x0)

    def lambda_9CF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9CF7)
    OP_95(0xA, 60080, 10, 4000, 2000, 0x0)
    SetChrPos(0xA, 119120, 0, -660, 275)
    Jump("loc_9D9E")

    label("loc_9D2D")

    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 52110, 1000, 10270, 3000, 0x0)
    OP_95(0xA, 51750, 1000, 10270, 3000, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9D88")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    Jump("loc_9D99")

    label("loc_9D88")

    SetChrPos(0xA, 51280, 1000, 12870, 90)

    label("loc_9D99")

    ClearChrFlags(0xA, 0x4)

    label("loc_9D9E")

    OP_68(53180, 2200, 190, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "やれやれ、なんだよBennettのヤツ。\x01",
            "I am telling you that it is delicious.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EB1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9EB1)
    Sleep(50)

    def lambda_9EC1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9EC1)
    Sleep(50)

    def lambda_9ED1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9ED1)
    Sleep(50)

    def lambda_9EE1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9EE1)
    Sleep(50)

    def lambda_9EF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EF1)
    Sleep(50)

    def lambda_9F01():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F01)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10304FHuh, that's why I feel so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHoney, you can not put it on Sumi too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FAnd anyway … …\x01",
            "Bennettさんは嫌がってるみたいだし、\x01",
            "Can you introduce another recommendation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey, it can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then I'm prototyping now,\x01",
            "\"Moist Cuts Sand\"\x01",
            "Would you like me to feast?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds ate moist crisp.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10100FMunching …\x01",
            "Ha, the bread is very moist … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, the sauce sauce is also\x01",
            "Juicy and …\x01",
            "美味しいよ、Oscar。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, he is still a prototype.\x01",
            "It is selling out as a product in earnest\x01",
            "It is likely to be ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FReally……\x02\x03",
            "#00203FIf so, we\x01",
            "Not to introduce\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, once completed\x01",
            "I will give you also,\x01",
            "Please wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I am looking forward to it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A28B")
    SetScenarioFlags(0x1, 2)

    label("loc_A28B")

    SetScenarioFlags(0x172, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A2BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A2DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A2EF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A302")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A31F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A332")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A34F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A362")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A37F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A392")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A3AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3AF")

    OP_29(0x80, 0x1, 0x6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4B2")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4A9")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A4A9")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_A4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A583")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A583")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 53850, 0, 1490, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_9537 end

    def Function_29_A5B7(): pass

    label("Function_29_A5B7")

    TalkBegin(0xA)

    ChrTalk(
        0xA,
        (
            "Fuu …\x01",
            "なかなかOscarに勝てる\x01",
            "I can not make new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, do not give up\x01",
            "I have to try as many times …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(For this person, in the \"craftsman\" frame\x01",
            "You seem to be able to qualify for MISCON … …)\x02\x03",
            "#00000FExcuse me.\x01",
            "I have a little consultation … …\x02",
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
        0xA,
        "…… Ha, Miscon! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I will hold back.\x01",
            "It's not a glass … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Charity event\x01",
            "I helped with cooking.\x01",
            "Then please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so …?\x01",
            "That way it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FLet's try other things.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 6)
    SetScenarioFlags(0x1, 3)
    TalkEnd(0xA)
    Return()

    # Function_29_A5B7 end

    SaveToFile()

Try(main)
