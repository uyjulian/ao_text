from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Oscar",                  # 1
        "Morges",                 # 2
        "Bennett",                # 3
        "Katerina",               # 4
        "Chiruru",                # 5
        "Tallys",                 # 6
        "Elsa",                   # 7
        "Momo",                   # 8
        "Pete",                   # 9
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
        "Function_7_8E5",          # 07, 7
        "Function_8_2140",         # 08, 8
        "Function_9_249F",         # 09, 9
        "Function_10_256D",        # 0A, 10
        "Function_11_2635",        # 0B, 11
        "Function_12_2703",        # 0C, 12
        "Function_13_38AA",        # 0D, 13
        "Function_14_3990",        # 0E, 14
        "Function_15_3C10",        # 0F, 15
        "Function_16_4B39",        # 10, 16
        "Function_17_4D60",        # 11, 17
        "Function_18_596C",        # 12, 18
        "Function_19_5A3A",        # 13, 19
        "Function_20_5AD1",        # 14, 20
        "Function_21_5AD5",        # 15, 21
        "Function_22_6B6C",        # 16, 22
        "Function_23_735D",        # 17, 23
        "Function_24_744E",        # 18, 24
        "Function_25_7805",        # 19, 25
        "Function_26_7F28",        # 1A, 26
        "Function_27_94B9",        # 1B, 27
        "Function_28_993D",        # 1C, 28
        "Function_29_A9F6",        # 1D, 29
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
            ""The Kingdom of Sweets\x01",
            "Vol.1" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_76E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Mix Gelato"\x07\x00\x01",
            "recipe.\x02",
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_86B")
    OP_AF(0xCC)
    Jump("loc_89D")

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_87B")
    OP_AF(0xCB)
    Jump("loc_89D")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_88B")
    OP_AF(0xCA)
    Jump("loc_89D")

    label("loc_88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_89B")
    OP_AF(0xC9)
    Jump("loc_89D")

    label("loc_89B")

    OP_AF(0xC8)

    label("loc_89D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8DC")

    label("loc_8AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C0")
    Jump("loc_8DC")

    label("loc_8C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_8DC")

    Jump("loc_7FA")

    label("loc_8E1")

    TalkEnd(0x8)
    Return()

    # Function_6_78C end

    def Function_7_8E5(): pass

    label("Function_7_8E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_900")
    Call(0, 8)
    Jump("loc_213F")

    label("loc_900")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Call(0, 9)
    Jump("loc_213F")

    label("loc_91B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_936")
    Call(0, 10)
    Jump("loc_213F")

    label("loc_936")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951")
    Call(0, 11)
    Jump("loc_213F")

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(
        0x8,
        (
            "Our trial product, the\x01",
            ""Thick Cutlet Sandwich",\x01",
            "is by the window there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wanted to recommend\x01",
            "Bennett's bread but... Man,\x01",
            "I don't understand women.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213F")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE8")

    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I made my special bread,\x01",
            "just for you guys. Here,\x01",
            "take it!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x214),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x214, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00002FWow, it smells really\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FYes, it looks\x01",
            "delicious.♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know, right? It's our\x01",
            "latest product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know you guys have it really tough.\x01",
            "If you eat that, I'm sure you'll pull\x01",
            "through this tough situation somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... I hope you're\x01",
            "right. Thanks, Oscar.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 4)
    Jump("loc_D53")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC5")

    ChrTalk(
        0x8,
        (
            "I always want a lot of\x01",
            "people to eat our bread.\x01",
            "Especially now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't do anything but\x01",
            "bake delicious bread,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if I have only a\x01",
            "few customers, all I can\x01",
            "do is ease their fears.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D53")

    label("loc_CC5")


    ChrTalk(
        0x8,
        (
            "No matter the situation,\x01",
            "my job is to bake\x01",
            "delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if our bread makes\x01",
            "customers only a little\x01",
            "happier, that's enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D53")

    Jump("loc_213F")

    label("loc_D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0F")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "You're... Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOscar... Thank goodness\x01",
            "you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, you guys made it...\x01",
            "Are you guys all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wait a sec. Lloyd,\x01",
            "you're a wanted man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-Yeah... It's a long\x01",
            "story.\x02\x03",
            "#00000FAnyhow, I have to warn\x01",
            "you and the others not\x01",
            "to leave the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I don't really\x01",
            "get it, but I'll do as\x01",
            "you say for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys be careful too,\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 3)
    Jump("loc_F7F")

    label("loc_F0F")


    ChrTalk(
        0x8,
        (
            "I don't really get\x01",
            "what's going on, but at\x01",
            "least you guys are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys be careful too,\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7F")

    Jump("loc_213F")

    label("loc_F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A5")

    ChrTalk(
        0x8,
        (
            "Rail service has been halted,\x01",
            "and we're running out of\x01",
            "reserve bread ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, we have Armorica Village, so\x01",
            "we should be able to manage even\x01",
            "without imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, no matter the\x01",
            "situation, I'll keep\x01",
            "making my delicious bread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114F")

    label("loc_10A5")


    ChrTalk(
        0x8,
        (
            "Because of Armorica Village, we\x01",
            "should be able to manage even\x01",
            "without imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, no matter the\x01",
            "situation, I'll keep\x01",
            "making my delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114F")

    Jump("loc_213F")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1162")
    Jump("loc_213F")

    label("loc_1162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1259")

    ChrTalk(
        0x8,
        (
            "Our customers have been\x01",
            "agitated since early\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard the sound of gunfire has\x01",
            "been heard in the vicinity of Mainz\x01",
            "ever since yesterday evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How disturbing... I hope\x01",
            "nothing else happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A6")

    label("loc_1259")


    ChrTalk(
        0x8,
        (
            "Gunfire near Mainz...\x01",
            "How disturbing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope nothing else\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A6")

    Jump("loc_213F")

    label("loc_12AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(
        0x8,
        "Bennett is very helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When she heard I was baker,\x01",
            "she complained about it but\x01",
            "taught me just the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Despite appearances,\x01",
            "she's a nice person at\x01",
            "her core.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FA")

    label("loc_1375")


    ChrTalk(
        0x8,
        (
            "Now then, are you guys\x01",
            "buying something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it's a rainy day,\x01",
            "you should have some of my\x01",
            "freshly baked, fluffy bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_213F")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_162D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E4")

    ChrTalk(
        0x8,
        (
            "That Bennett is kneading dough\x01",
            "in the kitchen with all her\x01",
            "might. Her arms must hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since I had a compress,\x01",
            "I gave it to her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not good to overdo\x01",
            "it. I'll have to watch\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1575")

    label("loc_14E4")


    ChrTalk(
        0x8,
        (
            "Well, being a hard\x01",
            "worker is one of\x01",
            "Bennett's good points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to watch her to\x01",
            "make sure she doesn't\x01",
            "overdo it and hurt herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1628")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1628")

    Jump("loc_213F")

    label("loc_162D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(
        0x8,
        (
            "Bennett's new bread is\x01",
            "selling well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But because of that, she's\x01",
            "always shouting "I won't\x01",
            "lose to you!" and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, could it be that\x01",
            "she hates me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1780")

    label("loc_16EC")


    ChrTalk(
        0x8,
        (
            "I'll have to ask if I've\x01",
            "done something wrong and\x01",
            "apologize for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to join forces\x01",
            "with Bennett and bake\x01",
            "delicious bread together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1780")

    Jump("loc_213F")

    label("loc_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(
        0x8,
        (
            "Bennett let me sample her\x01",
            "new bread, and I thought it\x01",
            "was positively delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's Bennett for you.\x01",
            "I won't lose to her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_189C")

    label("loc_1827")


    ChrTalk(
        0x8,
        (
            "Bennett has been making\x01",
            "some tasty bread lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's my master's\x01",
            "daughter for you. I\x01",
            "won't lose to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189C")

    Jump("loc_213F")

    label("loc_18A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1996")

    ChrTalk(
        0x8,
        (
            "Reporters have crowded\x01",
            "the place since early\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see a lot of salarymen\x01",
            "and businessmen most\x01",
            "mornings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, the fact that busy people\x01",
            "can eat it while working is one\x01",
            "of bread's many charms.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A42")

    label("loc_1996")


    ChrTalk(
        0x8,
        (
            "The fact that busy people\x01",
            "can eat it while working is\x01",
            "one of bread's many charms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want those reporters that\x01",
            "ate my bread this morning\x01",
            "to do their best all day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A42")

    Jump("loc_213F")

    label("loc_1A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0x8,
        (
            "Isn't it rare to see you\x01",
            "wandering around at this\x01",
            "hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, closing time has\x01",
            "already passed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For you, it's ok. Look\x01",
            "all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks, Oscar. We'll do\x01",
            "that by all m......\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-If we're buying, we'd\x01",
            "better do it quick.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BE4")

    label("loc_1B87")


    ChrTalk(
        0x8,
        (
            "Well, closing time has\x01",
            "already passed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For you, it's ok. Look\x01",
            "all you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE4")

    Jump("loc_213F")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(
        0x8,
        (
            "The other day, I got a\x01",
            "letter says "I'm a huge\x01",
            "fan of yours."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I'm not an Arc-en-\x01",
            "Ciel artist or anything,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's possible they got the\x01",
            "address wrong. If another comes,\x01",
            "I'll have to send a reply.\x02",
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
            "#00006FI wonder if you really\x01",
            "should.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh? Really? I don't get\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E1B")

    label("loc_1D92")


    ChrTalk(
        0x8,
        (
            "Even so, Bennett looked\x01",
            "strange when I got the\x01",
            "letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She asked me about its\x01",
            "contents... Does she want\x01",
            "to read it that badly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1B")

    Jump("loc_213F")

    label("loc_1E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F31")

    ChrTalk(
        0x8,
        (
            "Bennett has been making\x01",
            "better bread than before\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Day after day, she's been locking\x01",
            "herself in the kitchen after\x01",
            "closing time, practicing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, so it's come to this,\x01",
            "has it? I'll have to practice\x01",
            "more to keep up with her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FC5")

    label("loc_1F31")


    ChrTalk(
        0x8,
        (
            "In order to not lose to\x01",
            "Bennett, I have to\x01",
            "practice more myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it's a good\x01",
            "opportunity, I'll ask her if\x01",
            "we can practice together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC5")

    Jump("loc_213F")

    label("loc_1FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_209F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2058")

    ChrTalk(
        0x8,
        (
            "Meiling is the\x01",
            "granddaughter of Mr.\x01",
            "Mors of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, but I'm counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2099")

    label("loc_2058")


    ChrTalk(
        0x8,
        "You really saved us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I knew I could count on\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2099")

    Return()

    label("loc_209A")

    Jump("loc_213F")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_213F")

    ChrTalk(
        0x8,
        (
            "Lately, I've challenged\x01",
            "myself to make more new\x01",
            "kinds of bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll give you samples from\x01",
            "time to time. Buy a whole\x01",
            "bunch if you like them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213F")

    Return()

    # Function_7_8E5 end

    def Function_8_2140(): pass

    label("Function_8_2140")


    ChrTalk(
        0x8,
        "Oh, if it isn't Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYo, Oscar. Long time no\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yo. Just making my bread\x01",
            "like usual, day after\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But there's a face I\x01",
            "haven't seen in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Were you slacking off in\x01",
            "Michelam, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FCome on, you know that's not\x01",
            "true.\x02\x03",
            "#00001FAnd I told you properly about my\x01",
            ""Temporary Separation from the\x01",
            "SSS for Training", didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh that. I totally\x01",
            "forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well anyway, take this\x01",
            "to commemorate our\x01",
            "reunion, alright?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x210),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x210, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00105FThis is... The usual new\x01",
            "bread, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWow, it smells great,\x01",
            "doesn't it.\x02",
        )
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
            "Yeah, it's fresh-baked\x01",
            "and fluffy. I'm sure\x01",
            "you'll love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, buy a lot more if\x01",
            "you like that one, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar. We'll\x01",
            "savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)
    Return()

    # Function_8_2140 end

    def Function_9_249F(): pass

    label("Function_9_249F")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm making a new bread\x01",
            "today as well. Here, try\x01",
            "some.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x211),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x211, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar. We'll\x01",
            "savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 1)
    Return()

    # Function_9_249F end

    def Function_10_256D(): pass

    label("Function_10_256D")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bennett made the new\x01",
            "bread this time. Try\x01",
            "some.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x212, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar. We'll\x01",
            "savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Return()

    # Function_10_256D end

    def Function_11_2635(): pass

    label("Function_11_2635")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm making a new bread\x01",
            "today as well. Here, try\x01",
            "some.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x213, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar. We'll\x01",
            "savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Return()

    # Function_11_2635 end

    def Function_12_2703(): pass

    label("Function_12_2703")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2828")

    ChrTalk(
        0xFE,
        (
            "With the government's\x01",
            "wheat allowance I couldn't\x01",
            "make proper bread, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, with the trade routes restored,\x01",
            "I'll get some fresh from Armorica.\x01",
            "We'll be back on our feet in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Oscar and Bennett\x01",
            "are working harder than\x01",
            "they ever have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28DB")

    label("loc_2828")


    ChrTalk(
        0xFE,
        (
            "With the trade routes restored, I'll\x01",
            "get fresh flour from Armorica. We'll\x01",
            "be back on our feet in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Oscar and Bennett\x01",
            "are working harder than\x01",
            "they ever have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DB")

    Jump("loc_38A6")

    label("loc_28E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_297C")

    ChrTalk(
        0xFE,
        (
            "Customers won't come in under this\x01",
            "martial law, so I can focus on\x01",
            "developing my new bread recipes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, what's with this\x01",
            "situation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A76")

    ChrTalk(
        0xFE,
        (
            "It'll hurt a bit, not\x01",
            "being able to get\x01",
            "imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Almost all of our breads\x01",
            "have at least one imported\x01",
            "ingredient, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll have to make do\x01",
            "with all Crossbell-native\x01",
            "ingredients for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B0F")

    label("loc_2A76")


    ChrTalk(
        0xFE,
        (
            "Hmm, but... We'll be able to\x01",
            "take pride in our "100% Local\x01",
            "Crossbell Bread", I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I know I shouldn't\x01",
            "get too carried away\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0F")

    Jump("loc_38A6")

    label("loc_2B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1A")

    ChrTalk(
        0xFE,
        (
            "We should have a\x01",
            "reconstruction\x01",
            "assistance sale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar isn't here today,\x01",
            "so I have to apologize to\x01",
            "our female customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's rare to see a parent\x01",
            "and child run the store. It's a\x01",
            "great effort in and of itself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CCD")

    label("loc_2C1A")


    ChrTalk(
        0xFE,
        (
            "Oscar isn't here today,\x01",
            "so I have to apologize to\x01",
            "our female customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's rare to see a parent\x01",
            "and child run the store. It's a\x01",
            "great effort in and of itself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCD")

    Jump("loc_38A6")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D4E")

    ChrTalk(
        0xFE,
        (
            "Hey, it seems the mining\x01",
            "town is occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who on earth might have\x01",
            "done it? I can't forgive\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5B")

    ChrTalk(
        0xFE,
        (
            "There's less traffic in\x01",
            "here on rainy days, to\x01",
            "be perfectly honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we have a lot of\x01",
            "regular customers who\x01",
            "come even in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm thankful for their\x01",
            "business. It's probably because\x01",
            "we've been in business so long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EFE")

    label("loc_2E5B")


    ChrTalk(
        0xFE,
        (
            "We have a lot of regular\x01",
            "customers who come even\x01",
            "in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm thankful for their\x01",
            "business. Next time, I'll hold\x01",
            "a sale as a thank-you to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EFE")

    Jump("loc_38A6")

    label("loc_2F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F44")

    ChrTalk(
        0xFE,
        (
            "It's noisy out there...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_2F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FCB")

    ChrTalk(
        0xFE,
        (
            "That Bennett... When I\x01",
            "praise her, she ends up\x01",
            "resenting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's shy but... That's\x01",
            "her personality, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(
        0xFE,
        (
            "A lot of time has passed\x01",
            "since Oscar became my\x01",
            "apprentice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Bennett is\x01",
            "conscious of Oscar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, at this rate,\x01",
            "Oscar is going to become\x01",
            "my son-in-law.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3124")

    label("loc_3096")


    ChrTalk(
        0xFE,
        (
            "At this rate, Oscar is\x01",
            "going to become my son-\x01",
            "in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it'll be a great\x01",
            "victory for me if he becomes\x01",
            "both my son and my heir.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3124")

    Jump("loc_38A6")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31E8")

    ChrTalk(
        0xFE,
        (
            "A throng of reporters going\x01",
            "to cover the trade conference\x01",
            "came through this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I knew we were going to\x01",
            "sell that much, I would have\x01",
            "liked to have baked more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_31E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_329B")

    ChrTalk(
        0xFE,
        (
            "Well then, it's about\x01",
            "time to tidy up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bakery's preparations start early in\x01",
            "the morning at 3, after all. I've got\x01",
            "to get to be to be ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A6")

    label("loc_329B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_340C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3374")

    ChrTalk(
        0xFE,
        (
            "Oscar gets fan letters\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been happening ever\x01",
            "since he was featured in\x01",
            "a magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, sales are\x01",
            "up, and we get to take\x01",
            "care of Oscar's fans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3407")

    label("loc_3374")


    ChrTalk(
        0xFE,
        (
            "We've got to take good care\x01",
            "of Oscar's fans, even if it's\x01",
            "just for the sake of sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Bennett's bad mood\x01",
            "is the fly in the\x01",
            "ointment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3407")

    Jump("loc_38A6")

    label("loc_340C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D2")

    ChrTalk(
        0xFE,
        (
            "Good grief, Bennett\x01",
            "drove me out of the\x01",
            "kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been baking some\x01",
            "awful bread lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, she's doing it out\x01",
            "of ambition, so I\x01",
            "suppose that's good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3562")

    label("loc_34D2")


    ChrTalk(
        0xFE,
        (
            "Being able to hear her\x01",
            "grumbling and cute monologues\x01",
            "is rather entertaining, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that gives her\x01",
            "motivation, I guess it's\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3562")

    Jump("loc_38A6")

    label("loc_3567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EE")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you all... Are\x01",
            "you here for work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please speak with Oscar\x01",
            "and the others about the\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F3")

    label("loc_35EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3682")

    ChrTalk(
        0xFE,
        (
            "If I don't hurry and\x01",
            "make the dough, it won't\x01",
            "be ready before noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, and thanks for\x01",
            "your help with this\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F3")

    label("loc_3682")


    ChrTalk(
        0xFE,
        (
            "Looks like you found the\x01",
            "umbrella. Hehe, thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll now be able to\x01",
            "resume breadmaking\x01",
            "without worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F3")

    Jump("loc_38A6")

    label("loc_36F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381B")

    ChrTalk(
        0xFE,
        (
            "Lately, I've been leaving almost\x01",
            "all our product development to\x01",
            "Oscar and Bennett.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're learning a lot through\x01",
            "competition with each other, and they're\x01",
            "making some darn good bread too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might be able to let\x01",
            "them run the whole store\x01",
            "before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38A6")

    label("loc_381B")


    ChrTalk(
        0xFE,
        (
            "I have been especially\x01",
            "happy to see my daughter's\x01",
            "growth as a baker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar has played a huge\x01",
            "role in that. Rivals are\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A6")

    TalkEnd(0xFE)
    Return()

    # Function_12_2703 end

    def Function_13_38AA(): pass

    label("Function_13_38AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38D8")
    Call(0, 29)
    Return()

    label("loc_38D8")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3937")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3957")
    OP_AF(0xCB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3987")

    label("loc_3957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_396B")
    Jump("loc_3987")

    label("loc_396B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3987")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3987")

    Jump("loc_38E5")

    label("loc_398C")

    TalkEnd(0xA)
    Return()

    # Function_13_38AA end

    def Function_14_3990(): pass

    label("Function_14_3990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3A1E")

    ChrTalk(
        0xA,
        (
            "Sorry, but I don't have\x01",
            "the figure for a\x01",
            "pageant, do I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm helping with the\x01",
            "event's food, so give me\x01",
            "a break here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0F")

    label("loc_3A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE5")

    ChrTalk(
        0xA,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm making a new bread.\x01",
            "If you like, please try\x01",
            "some.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x213, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FThanks, I'll savor it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Jump("loc_3C0F")

    label("loc_3AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B98")

    ChrTalk(
        0xA,
        (
            "Oscar went to help with\x01",
            "the charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I would have liked to go,\x01",
            "but Oscar's smile will\x01",
            "cheer everyone up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Wait, no! Forget I\x01",
            "said that!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C0F")

    label("loc_3B98")


    ChrTalk(
        0xA,
        (
            "W-Well, my task right\x01",
            "now is to tend the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll leave the charity\x01",
            "event to Oscar.\x01",
            "...That's all this is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0F")

    Return()

    # Function_14_3990 end

    def Function_15_3C10(): pass

    label("Function_15_3C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3C99")

    ChrTalk(
        0xFE,
        (
            "That Oscar... He just\x01",
            "went and recommended my\x01",
            "bread to a magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmph. I wonder what\x01",
            "he's trying to pull.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B35")

    label("loc_3C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D96")

    ChrTalk(
        0xFE,
        (
            "In order not to lose to Oscar,\x01",
            "I've got to make a lot of my new\x01",
            "bread to make everyone happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But... My bread doesn't\x01",
            "hold a candle to his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's like this, I guess\x01",
            "I'll take some advice from\x01",
            "him. This sucks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E12")

    label("loc_3D96")


    ChrTalk(
        0xFE,
        (
            "My bread doesn't hold a\x01",
            "candle to Oscar's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's like this, I guess\x01",
            "I'll take some advice from\x01",
            "him. This sucks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E12")

    Jump("loc_4B35")

    label("loc_3E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ECE")

    ChrTalk(
        0xFE,
        (
            "I'm ready to close up\x01",
            "shop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What about those monsters?\x01",
            "It's not like they're coming\x01",
            "to attack us citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're too weird\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F31")

    label("loc_3ECE")


    ChrTalk(
        0xFE,
        (
            "Those monsters outside\x01",
            "are too weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though they won't\x01",
            "attack us, I can't\x01",
            "relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F31")

    Jump("loc_4B35")

    label("loc_3F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404E")

    ChrTalk(
        0xFE,
        (
            "Both Oscar and my father\x01",
            "are oddly positive,\x01",
            "given the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Will we really be all right? Even\x01",
            "if he is Arios, the combined military\x01",
            "might of those nations is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even if I worry\x01",
            "about it, it's not like\x01",
            "anything will change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40E4")

    label("loc_404E")


    ChrTalk(
        0xFE,
        (
            "Even if he is Arios, the\x01",
            "combined military might\x01",
            "of those nations is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even if I worry\x01",
            "about it, it's not like\x01",
            "anything will change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E4")

    Jump("loc_4B35")

    label("loc_40E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40FE")
    TalkEnd(0xFE)
    Call(0, 13)
    Return()

    label("loc_40FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_420B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A8")

    ChrTalk(
        0xFE,
        (
            "Oh yeah, I'll mix that\x01",
            "herb into my next new\x01",
            "bread and...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Wah, sorry! I was just\x01",
            "thinking out loud.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_4206")

    label("loc_41A8")


    ChrTalk(
        0xFE,
        (
            "I planned out my next\x01",
            "new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think we have\x01",
            "some of that herb in\x01",
            "stock...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4206")

    Jump("loc_4B35")

    label("loc_420B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_421C")
    Call(0, 16)
    Jump("loc_4B35")

    label("loc_421C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BF")

    ChrTalk(
        0xFE,
        "...Mrr, that Oscar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's making a huge mistake if\x01",
            "he thinks a compress like this\x01",
            "is gonna put me in a good mood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4334")

    label("loc_42BF")


    ChrTalk(
        0xFE,
        "That Oscar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's making a huge mistake if\x01",
            "he thinks a compress like this\x01",
            "is gonna put me in a good mood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4334")

    Jump("loc_4B35")

    label("loc_4339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_449C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4411")

    ChrTalk(
        0xFE,
        (
            "Grrr, that Oscar... I\x01",
            "want to hit him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But when he ate it, he\x01",
            "thought it was delicious, based\x01",
            "on his facial expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No, that's not it!\x01",
            "There's no way he\x01",
            "enjoyed it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4497")

    label("loc_4411")


    ChrTalk(
        0xFE,
        (
            "Out-out-dark-thoughts!\x01",
            "(*kneading*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar... I'll get you next\x01",
            "time for sure... I'll make you\x01",
            "regret the day you were born!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4497")

    Jump("loc_4B35")

    label("loc_449C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_45B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453E")

    ChrTalk(
        0xFE,
        (
            "Just when I made better\x01",
            "bread than Oscar, he\x01",
            "looks so happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no! I want to see\x01",
            "his loser face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oooh, that Oscar!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_45AE")

    label("loc_453E")


    ChrTalk(
        0xFE,
        (
            "That Oscar... Why did he\x01",
            "have to look so happy\x01",
            "eating my bread...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Show your loser face\x01",
            "already! Geez!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45AE")

    Jump("loc_4B35")

    label("loc_45B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464D")

    ChrTalk(
        0xFE,
        (
            "When my bread and Oscar's are\x01",
            "side-by-side, the customers\x01",
            "usually go for his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oooh, what the heck am I\x01",
            "doing wrong!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_46D2")

    label("loc_464D")


    ChrTalk(
        0xFE,
        (
            "Alright. If it's like\x01",
            "this, then I'm left with\x01",
            "no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll go beyond the\x01",
            "Bennett Special and make\x01",
            "the ultimate bread!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D2")

    Jump("loc_4B35")

    label("loc_46D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4747")

    ChrTalk(
        0xFE,
        (
            "The bread I made is\x01",
            "losing in sales to\x01",
            "Oscar's...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grrr, tomorrow, for\x01",
            "sure, I'll...!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B35")

    label("loc_4747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_488D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4812")

    ChrTalk(
        0xFE,
        (
            "It seems Oscar got a\x01",
            "weird letter the other\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be a love\x01",
            "letter!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's so full of himself, and\x01",
            "just because he can make\x01",
            "bread a little better than I.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4888")

    label("loc_4812")


    ChrTalk(
        0xFE,
        (
            "A love letter? Who sent\x01",
            "it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, no, that's not it.\x01",
            "T-To think a guy like Oscar\x01",
            "could get a love letter!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4888")

    Jump("loc_4B35")

    label("loc_488D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_48F4")

    ChrTalk(
        0xFE,
        "(*knead, knead*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*mumble*... I definitely\x01",
            "won't lose to the likes\x01",
            "of Oscar!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B35")

    label("loc_48F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_49E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4962")

    ChrTalk(
        0xA,
        (
            "You guys take care of\x01",
            "the umbrella. I'll look\x01",
            "after the girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49A8")

    label("loc_4962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4977")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_49A8")

    label("loc_4977")


    ChrTalk(
        0xA,
        (
            "I mean seriously. How\x01",
            "annoying can you get?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A8")

    TalkEnd(0xFE)
    Return()

    label("loc_49AC")


    ChrTalk(
        0xA,
        "Hey, don't cry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll definitely find\x01",
            "it, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B35")

    label("loc_49E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABF")

    ChrTalk(
        0xFE,
        (
            "Welcome. Our fresh-baked\x01",
            "bread is right this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pretty angry that\x01",
            "most of them are\x01",
            "Oscar's, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Oscar... I'll\x01",
            "overtake him one of these\x01",
            "days. Mark my words!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B35")

    label("loc_4ABF")


    ChrTalk(
        0xFE,
        (
            "That Oscar is really\x01",
            "skilled. This is gonna\x01",
            "be tough, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely overtake\x01",
            "Oscar. Mark my words!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B35")

    TalkEnd(0xFE)
    Return()

    # Function_15_3C10 end

    def Function_16_4B39(): pass

    label("Function_16_4B39")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C32")

    ChrTalk(
        0xA,
        (
            "Then, please take this\x01",
            "to Tallys for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Did you forget\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You baked it fresh, but\x01",
            "it's totally cold now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "*sniff*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, enough of this. I'll\x01",
            "exchange it for you, so\x01",
            "don't cry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D57")

    label("loc_4C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D04")

    ChrTalk(
        0xA,
        (
            "Are you here on an\x01",
            "errand today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Careful not to lose your\x01",
            "umbrella again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Y-Yeah, I'm ok. My name\x01",
            "and address are written\x01",
            "on it right here....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, I see. That's a\x01",
            "relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D57")

    label("loc_4D04")


    ChrTalk(
        0xA,
        (
            "Haha, you have good\x01",
            "handwriting, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "D-Don't mention it.\x01",
            "Ehehe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D57")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_16_4B39 end

    def Function_17_4D60(): pass

    label("Function_17_4D60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E1E")

    ChrTalk(
        0xFE,
        (
            "This place's bread and I are a\x01",
            "match made in heaven. I always\x01",
            "feel energized when I eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll think I'll buy\x01",
            "enough for my family and\x01",
            "return home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EB6")

    label("loc_4E1E")


    ChrTalk(
        0xFE,
        (
            "By the way, Chiruru said\x01",
            "she was leaving on a\x01",
            "trip again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll be all\x01",
            "right. The highways have\x01",
            "gotten dangerous again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB6")

    Jump("loc_5968")

    label("loc_4EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4EC9")
    Jump("loc_5968")

    label("loc_4EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F59")

    ChrTalk(
        0xFE,
        (
            "Looks like Chiruru went\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what's going\x01",
            "to happen now, but I should\x01",
            "stay with my family...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F95")

    label("loc_4F59")


    ChrTalk(
        0xFE,
        (
            "I think I'll go home\x01",
            "today without taking any\x01",
            "detours.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F95")

    Jump("loc_5968")

    label("loc_4F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5021")

    ChrTalk(
        0xFE,
        (
            "For today's reconstruction\x01",
            "sale, some of their bread\x01",
            "is half off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sales don't happen\x01",
            "often, so I'll buy a\x01",
            "lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_5021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50A5")

    ChrTalk(
        0xFE,
        (
            "My mom told me to return\x01",
            "home early today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped,\x01",
            "given that an incident\x01",
            "like that occurred...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_50A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5156")

    ChrTalk(
        0xFE,
        (
            "Come to think of it...\x01",
            "Arc-en-Ciel's\x01",
            "performance is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I want to see it. I wonder\x01",
            "how that newcomer everyone's\x01",
            "talking about will perform...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_5156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5164")
    Jump("loc_5968")

    label("loc_5164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517F")
    Call(0, 18)
    Jump("loc_51F1")

    label("loc_517F")


    ChrTalk(
        0xFE,
        (
            "...Huh, do I hear\x01",
            "Bennett's voice in here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Her new bread is\x01",
            "popular, so she must be\x01",
            "working hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F1")

    Jump("loc_5968")

    label("loc_51F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_538B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_531B")

    ChrTalk(
        0xFE,
        (
            "Hmm, so Bennett baked\x01",
            "the new bread this time,\x01",
            "did she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stuffing strawberries and\x01",
            "cream into a fluffy bread\x01",
            "roll. How irresistible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These extravagant toppings\x01",
            "really make it stand out from\x01",
            "the last one. It's very cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I have to eat it\x01",
            "now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5386")

    label("loc_531B")


    ChrTalk(
        0xFE,
        (
            "It looks like Bennett\x01",
            "made the new bread this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's very cute... Hmm...\x01",
            "I have to have one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5386")

    Jump("loc_5968")

    label("loc_538B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53D5")

    ChrTalk(
        0xFE,
        (
            "Aww, they're all sold\x01",
            "out of the morning bread\x01",
            "I like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_53D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_53E3")
    Jump("loc_5968")

    label("loc_53E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_552E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B4")

    ChrTalk(
        0xFE,
        (
            "By the way, Chiruru got\x01",
            "back from her trip the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. I would have\x01",
            "been nice if she let me\x01",
            "know she was back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have liked to\x01",
            "have tea with her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5529")

    label("loc_54B4")


    ChrTalk(
        0xFE,
        (
            "That girl! Just when is\x01",
            "she going to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since she's back, I\x01",
            "would have liked to have\x01",
            "tea with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5529")

    Jump("loc_5968")

    label("loc_552E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5662")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5605")

    ChrTalk(
        0xFE,
        (
            "Ah, the new bread... It\x01",
            "looks delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stuffing custard cream\x01",
            "into soft melon bread...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting a little fat,\x01",
            "but... Yeah, I'll not worry\x01",
            "about that and buy it anyway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_565D")

    label("loc_5605")


    ChrTalk(
        0xFE,
        (
            "If I don't eat this new\x01",
            "bread, I'll miss out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll buy several and\x01",
            "head home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_565D")

    Jump("loc_5968")

    label("loc_5662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_57FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_579A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5727")

    ChrTalk(
        0xFE,
        (
            "Now that you mention it,\x01",
            "I think there was a\x01",
            "brother and sister here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sister was about the\x01",
            "same age as Momo... I'm\x01",
            "pretty sure on this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5796")

    label("loc_5727")


    ChrTalk(
        0xFE,
        (
            "Haha, thank goodness you\x01",
            "found Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "buy some bread and head\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5796")

    TalkEnd(0xFE)
    Return()

    label("loc_579A")


    ChrTalk(
        0xFE,
        (
            "That crying girl is the\x01",
            "daughter of that shop\x01",
            "owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what happened\x01",
            "to her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_57FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D7")

    ChrTalk(
        0xFE,
        (
            "Let's see, the new bread\x01",
            "this time is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunny-side up fried eggs\x01",
            "stuffed in a muffin...\x01",
            "Mmm, that looks delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'll buy this new\x01",
            "bread, have tea and then\x01",
            "go home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5968")

    label("loc_58D7")


    ChrTalk(
        0xFE,
        (
            "Ever since I started coming\x01",
            "here, I've been checking\x01",
            "their new breads daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'll buy this new\x01",
            "bread, have tea and then\x01",
            "go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5968")

    TalkEnd(0xFE)
    Return()

    # Function_17_4D60 end

    def Function_18_596C(): pass

    label("Function_18_596C")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "Chiruru, which one would\x01",
            "you like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you're asking me, I'd\x01",
            "go with this new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Then I'll go with\x01",
            "that one too. It's kind\x01",
            "of cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I know, right?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_18_596C end

    def Function_19_5A3A(): pass

    label("Function_19_5A3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5A4B")
    Jump("loc_5ACD")

    label("loc_5A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A66")
    Call(0, 18)
    Jump("loc_5ACD")

    label("loc_5A66")


    ChrTalk(
        0xFE,
        (
            "Whenever I leave on a\x01",
            "trip, I come here to buy\x01",
            "a lunchbox.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, this bread is\x01",
            "so cute...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ACD")

    TalkEnd(0xFE)
    Return()

    # Function_19_5A3A end

    def Function_20_5AD1(): pass

    label("Function_20_5AD1")

    Call(0, 21)
    Return()

    # Function_20_5AD1 end

    def Function_21_5AD5(): pass

    label("Function_21_5AD5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B68")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B34")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5B34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B53")
    OP_AF(0x31)
    Jump("loc_5BD5")

    label("loc_5B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5B63")
    OP_AF(0x30)
    Jump("loc_5BD5")

    label("loc_5B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B73")
    OP_AF(0x2F)
    Jump("loc_5BD5")

    label("loc_5B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B83")
    OP_AF(0x2E)
    Jump("loc_5BD5")

    label("loc_5B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B93")
    OP_AF(0x2D)
    Jump("loc_5BD5")

    label("loc_5B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5BA3")
    OP_AF(0x2C)
    Jump("loc_5BD5")

    label("loc_5BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5BB3")
    OP_AF(0x2B)
    Jump("loc_5BD5")

    label("loc_5BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BC3")
    OP_AF(0x2A)
    Jump("loc_5BD5")

    label("loc_5BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5BD3")
    OP_AF(0x29)
    Jump("loc_5BD5")

    label("loc_5BD3")

    OP_AF(0x28)

    label("loc_5BD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B63")

    label("loc_5BE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BF8")
    Jump("loc_6B63")

    label("loc_5BF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B63")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D16")

    ChrTalk(
        0xD,
        (
            "Trade's been halted for a while,\x01",
            "and I can't stock a satisfactory\x01",
            "selection of goods, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For now, I'm relieved to\x01",
            "see that Crossbell's\x01",
            "back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to work to make\x01",
            "sure all families get\x01",
            "through this ok.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DB8")

    label("loc_5D16")


    ChrTalk(
        0xD,
        (
            "It's tough not being able to\x01",
            "trade. For now, I'm just glad\x01",
            "Crossbell is back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to work to make\x01",
            "sure all families get\x01",
            "through this ok.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB8")

    Jump("loc_6B63")

    label("loc_5DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5EA1")

    ChrTalk(
        0xD,
        (
            "I-I wonder what they are...\x01",
            "Those monsters that look like\x01",
            "middle age armors, I mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A-Anyway, even though things are this\x01",
            "bad, you're still a customer. If there's\x01",
            "something you want, just let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_5EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F65")

    ChrTalk(
        0xD,
        (
            "Hearing Dieter's speech\x01",
            "made me feel independence\x01",
            "is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't know what dangers lie\x01",
            "ahead, but... I'll do whatever I\x01",
            "must to protect Momo and Elsa.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5FC8")

    label("loc_5F65")


    ChrTalk(
        0xD,
        (
            "I don't know what dangers lie\x01",
            "ahead, but... I'll do whatever I\x01",
            "must to protect Momo and Elsa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC8")

    Jump("loc_6B63")

    label("loc_5FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6052")

    ChrTalk(
        0xD,
        (
            "Hey, there. Welcome to\x01",
            "Tallys' General Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We're having a sale on\x01",
            "daily necessities.\x01",
            "Please, take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_6052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6118")

    ChrTalk(
        0xD,
        (
            "That Mainz incident...\x01",
            "There's a rumor that the\x01",
            "Empire is behind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Involving innocent\x01",
            "civilians...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If the rumor is true,\x01",
            "then I can't forgive the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6192")

    label("loc_6118")


    ChrTalk(
        0xD,
        (
            "It's possible they were\x01",
            "targeting Crossbell City\x01",
            "itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If the rumor is true,\x01",
            "then I can't forgive the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6192")

    Jump("loc_6B63")

    label("loc_6197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_625A")

    ChrTalk(
        0xD,
        (
            "I heard people were injured in\x01",
            "yesterday's derailment, but\x01",
            "service was restored somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Many places rely on the\x01",
            "railway for stocking up, so I\x01",
            "think everyone is relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_625A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_63A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6338")

    ChrTalk(
        0xD,
        (
            "Hearing the sound of an\x01",
            "ambulance, I rushed out\x01",
            "of the store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*... I was relieved\x01",
            "to see that Momo wasn't\x01",
            "hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But there were so many\x01",
            "of them. I wonder what\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_639D")

    label("loc_6338")


    ChrTalk(
        0xD,
        (
            "It seems many ambulances\x01",
            "passed by...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to warn the\x01",
            "kids not to play in the\x01",
            "street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_639D")

    Jump("loc_6B63")

    label("loc_63A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6444")

    ChrTalk(
        0xD,
        (
            "It seems Momo and the\x01",
            "others were playing in\x01",
            "the street today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's been more traffic\x01",
            "lately, so I hope they're\x01",
            "watching out for cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_6444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_65BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6529")

    ChrTalk(
        0xD,
        (
            "I think it would be good if\x01",
            "Crossbell were independent\x01",
            "from the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, if we were\x01",
            "independent, they'd\x01",
            "become our enemies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, this is a difficult\x01",
            "problem, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65B8")

    label("loc_6529")


    ChrTalk(
        0xD,
        (
            "I think Crossbell\x01",
            "independence would be a\x01",
            "good thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's scary to think the\x01",
            "Empire and Republic would\x01",
            "become our enemies...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65B8")

    Jump("loc_6B63")

    label("loc_65BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6673")

    ChrTalk(
        0xD,
        (
            "I'm sure a trade conference\x01",
            "article will be on the front page\x01",
            "of the next Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I'll sell more\x01",
            "than usual, so I need to\x01",
            "stock up on those.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_6673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66F3")

    ChrTalk(
        0xD,
        (
            "Hey, welcome! Do you\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm keeping the store\x01",
            "open for a little longer,\x01",
            "so take your time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B63")

    label("loc_66F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BD")

    ChrTalk(
        0xD,
        (
            "The Orchis Tower\x01",
            "unveiling was today,\x01",
            "wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, I think I'll close\x01",
            "up shop and go see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, big buildings and\x01",
            "cars are things men\x01",
            "eternally long for.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_683F")

    label("loc_67BD")


    ChrTalk(
        0xD,
        (
            "Big buildings like Orchis\x01",
            "tower and cars are things\x01",
            "men eternally long for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We always get so excited\x01",
            "over those things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_683F")

    Jump("loc_6B63")

    label("loc_6844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694E")

    ChrTalk(
        0xD,
        (
            "I've been seeing\x01",
            "officers in the city\x01",
            "more often lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It must in preparation for the\x01",
            "VIPs from each country that are\x01",
            "coming for the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to do my best to\x01",
            "make sure Momo doesn't\x01",
            "get into any trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69D9")

    label("loc_694E")


    ChrTalk(
        0xD,
        (
            "It seems the police have\x01",
            "stepped up security in\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to do my best to\x01",
            "make sure Momo doesn't\x01",
            "get into any trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D9")

    Jump("loc_6B63")

    label("loc_69DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8E")

    ChrTalk(
        0xD,
        (
            "I sent Momo on an errand\x01",
            "to the bakery today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But... She's taking a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I've forgotten\x01",
            "what I asked her to get\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6ADA")

    label("loc_6A8E")


    ChrTalk(
        0xD,
        (
            "Momo sure is taking a long\x01",
            "time. Could something have\x01",
            "happened to her?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADA")

    Jump("loc_6B63")

    label("loc_6ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B63")

    ChrTalk(
        0xD,
        (
            "Hey there. Welcome to\x01",
            "Tallys' General Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Leave all your daily\x01",
            "necessities to us. Please,\x01",
            "take a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B63")

    Jump("loc_5AE2")

    label("loc_6B68")

    TalkEnd(0xD)
    Return()

    # Function_21_5AD5 end

    def Function_22_6B6C(): pass

    label("Function_22_6B6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C83")

    ChrTalk(
        0xFE,
        (
            "That Momo. She rushed out of here\x01",
            "saying "I want to do something\x01",
            "for everyone in the city."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the first time I\x01",
            "ever saw her insist on\x01",
            "anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about her\x01",
            "going outside alone, but I\x01",
            "understand how she feels.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D34")

    label("loc_6C83")


    ChrTalk(
        0xFE,
        (
            "That Momo. She rushed out of here\x01",
            "saying "I want to do something\x01",
            "for everyone in the city."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about her\x01",
            "going outside alone, but I\x01",
            "understand how she feels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D34")

    Jump("loc_7359")

    label("loc_6D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6DBC")

    ChrTalk(
        0xFE,
        (
            "To think things like\x01",
            "that have appeared in\x01",
            "the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this the meaning of\x01",
            "the President's martial\x01",
            "law?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7359")

    label("loc_6DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBC")

    ChrTalk(
        0xFE,
        (
            "It looks like Crossbell\x01",
            "will only grow even more\x01",
            "unstable at this rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo might not like it,\x01",
            "but... I can't leave Momo\x01",
            "alone outside for too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but worry\x01",
            "about her whenever she's\x01",
            "out of sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F52")

    label("loc_6EBC")


    ChrTalk(
        0xFE,
        (
            "Momo might not like it,\x01",
            "but... I can't leave Momo\x01",
            "alone outside for too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but worry\x01",
            "about her whenever she's\x01",
            "out of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F52")

    Jump("loc_7359")

    label("loc_6F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6FEB")

    ChrTalk(
        0xFE,
        (
            "I get so scared whenever\x01",
            "Momo's alone outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A week has passed since\x01",
            "that incident, and I want\x01",
            "to think it's fine, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7359")

    label("loc_6FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6FF9")
    Jump("loc_7359")

    label("loc_6FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7070")

    ChrTalk(
        0xFE,
        (
            "I asked Momo to get a\x01",
            "baguette to go with\x01",
            "tonight's beef stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder when she'll be\x01",
            "back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7359")

    label("loc_7070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_707E")
    Jump("loc_7359")

    label("loc_707E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_708C")
    Jump("loc_7359")

    label("loc_708C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_709A")
    Jump("loc_7359")

    label("loc_709A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_71A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7158")

    ChrTalk(
        0xFE,
        (
            "Momo went to play with\x01",
            "Henri and Ryｹ again\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though that girl is shy,\x01",
            "she's been getting less\x01",
            "so, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I have to thank\x01",
            "Ryｹ and Henri.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_71A4")

    label("loc_7158")


    ChrTalk(
        0xFE,
        (
            "Now then, I wonder if\x01",
            "she'll be hungry when she\x01",
            "gets back again today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A4")

    Jump("loc_7359")

    label("loc_71A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C9")
    Call(0, 23)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_71FC")

    label("loc_71C9")


    ChrTalk(
        0xFE,
        (
            "Haha, that Momo. She\x01",
            "really had a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71FC")

    Jump("loc_7359")

    label("loc_7201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_720F")
    Jump("loc_7359")

    label("loc_720F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_721D")
    Jump("loc_7359")

    label("loc_721D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D0")

    ChrTalk(
        0xFE,
        (
            "That Momo. Even though\x01",
            "it's raining, she went off\x01",
            "happily on her errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It seems she wanted\x01",
            "to use the umbrella her\x01",
            "father bought her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_734B")

    label("loc_72D0")


    ChrTalk(
        0xFE,
        (
            "Momo's father bought her\x01",
            "that umbrella, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's Momo's favorite\x01",
            "color, pink, and she\x01",
            "absolutely loves it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_734B")

    Jump("loc_7359")

    label("loc_7350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7359")

    label("loc_7359")

    TalkEnd(0xFE)
    Return()

    # Function_22_6B6C end

    def Function_23_735D(): pass

    label("Function_23_735D")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "...And then, and then...\x01",
            "Ryｹ tried to enter\x01",
            "Orchis Tower on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "And when he did, even\x01",
            "Henri and Momo got\x01",
            "scolded by an officer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My my... That was\x01",
            "terrible, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But, but... It was\x01",
            "really fun!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_23_735D end

    def Function_24_744E(): pass

    label("Function_24_744E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_745F")
    Jump("loc_7801")

    label("loc_745F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_74BE")

    ChrTalk(
        0xFE,
        (
            "Oooh, it's scary\x01",
            "outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Ryｹ and\x01",
            "Henri are all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_74BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7521")

    ChrTalk(
        0xFE,
        (
            "Mama and papa look\x01",
            "really scared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo's worried too, for\x01",
            "some reason...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_759A")

    ChrTalk(
        0xFE,
        (
            "Mom has been stopping me\x01",
            "whenever I try to go\x01",
            "play outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to play with Ryｹand Henri...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_759A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_75A8")
    Jump("loc_7801")

    label("loc_75A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_75B9")
    Call(0, 16)
    Jump("loc_7801")

    label("loc_75B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_75C7")
    Jump("loc_7801")

    label("loc_75C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_75D5")
    Jump("loc_7801")

    label("loc_75D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7648")

    ChrTalk(
        0xFE,
        (
            "I'm helping with the\x01",
            "shop today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't just play all\x01",
            "time. I've got to help\x01",
            "out too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7656")
    Jump("loc_7801")

    label("loc_7656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7671")
    Call(0, 23)
    Jump("loc_770D")

    label("loc_7671")


    ChrTalk(
        0xFE,
        (
            "But Ryｹ was funny. He tried\x01",
            "to make it look like it was\x01",
            "all Henri's fault...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he was found out\x01",
            "immediately and scolded\x01",
            "even more. *chuckle*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_770D")

    Jump("loc_7801")

    label("loc_7712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7720")
    Jump("loc_7801")

    label("loc_7720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_772E")
    Jump("loc_7801")

    label("loc_772E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_77F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77A6")

    ChrTalk(
        0xF,
        (
            "That umbrella is\x01",
            "precious to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*cry, cry*... Please,\x01",
            "mister...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77DC")

    label("loc_77A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77BB")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_77DC")

    label("loc_77BB")


    ChrTalk(
        0xF,
        (
            "Ehehe, that lady is\x01",
            "nice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77DC")

    TalkEnd(0xFE)
    Return()

    label("loc_77E0")


    ChrTalk(
        0xF,
        "*cry, cry*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_77F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7801")

    label("loc_7801")

    TalkEnd(0xFE)
    Return()

    # Function_24_744E end

    def Function_25_7805(): pass

    label("Function_25_7805")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ECA")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou're Pete, Mr.\x01",
            "Grimwood's assistant, if\x01",
            "I recall.\x02\x03",
            "#00001FIt looks like you're\x01",
            "alone though. Where's\x01",
            "Mr. Grimwood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lawyer Ian saw the\x01",
            "situation and went to\x01",
            "Orchis Tower to protest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since he left me in\x01",
            "charge, I haven't been\x01",
            "able to get in touch...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D66")

    ChrTalk(
        0x102,
        (
            "#00106FMr. Grimwood... I'm\x01",
            "worried about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FIf he went to Orchis Tower,\x01",
            "then perhaps he's been\x01",
            "arrested by the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWe'd better hurry.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F...Pete.\x02\x03",
            "#00001FDid Lawyer Ian say\x01",
            "anything else?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "By the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said something\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once the situation's under\x01",
            "control, return to my office\x01",
            "and clean my desk for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FCleaning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. From the start, I\x01",
            "thought he left in a\x01",
            "hurry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I do Mr. Grimwood's\x01",
            "cleaning, he regularly tells me to keep\x01",
            "away from his desk as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said to leave it alone since there\x01",
            "are a lot of things on there a helper\x01",
            "such as myself shouldn't see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FLawyer Ian... It seems\x01",
            "like he was really\x01",
            "concerned about that...\x02\x03",
            "#00106FI don't get why he would\x01",
            "ask you to clean the\x01",
            "desk now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00000FPete, please leave\x01",
            "Lawyer Ian to us. You\x01",
            "stay safe here.\x02\x03",
            "If we learn anything,\x01",
            "we'll let you know\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9E")

    label("loc_7D66")


    ChrTalk(
        0x102,
        (
            "#00106FMr. Grimwood... I'm\x01",
            "worried about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FIf he went to Orchis Tower,\x01",
            "then perhaps he's been\x01",
            "arrested by the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWe'd better hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000FPete, please leave\x01",
            "Lawyer Ian to us. You\x01",
            "stay safe here.\x02\x03",
            "If we learn anything,\x01",
            "we'll let you know\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E9E")


    ChrTalk(
        0xFE,
        (
            "U-Understood... And\x01",
            "thank you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 5)
    Jump("loc_7F24")

    label("loc_7ECA")


    ChrTalk(
        0xFE,
        (
            "Everyone, please do\x01",
            "something for Lawyer\x01",
            "Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood... I hope\x01",
            "he's safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F24")

    TalkEnd(0xFE)
    Return()

    # Function_25_7805 end

    def Function_26_7F28(): pass

    label("Function_26_7F28")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_END)), "loc_8058")

    ChrTalk(
        0x101,
        (
            "#6P#00000FHey Oscar. We saw your\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, Lloyd! I thought\x01",
            "you'd come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's sudden but can you\x01",
            "tell us the details?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_829A")

    label("loc_8058")


    ChrTalk(
        0x101,
        (
            "#6P#00000FHey Oscar, it's been a\x01",
            "while. We saw your\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, if it isn't Lloyd! I\x01",
            "thought you'd come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut there's a face I\x01",
            "haven't seen in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWere you slacking off in\x01",
            "Michelam, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FCome on, you know that's not\x01",
            "true.\x02\x03",
            "#00001FAnd I told you properly about my\x01",
            ""Temporary Separation from the\x01",
            "SSS for Training", didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh that. I totally\x01",
            "forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...We've gotten off\x01",
            "topic. You're here about\x01",
            "my request, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell then, can you give\x01",
            "us the details?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)

    label("loc_829A")


    ChrTalk(
        0x8,
        (
            "#11PYeah. The one with the\x01",
            "request is actually\x01",
            "little Momo over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PShe is Tallys' little girl,\x01",
            "and she brought her umbrella\x01",
            "today since it's raining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHowever...\x02",
    )

    CloseMessageWindow()
    OP_68(53460, 1500, 2390, 2000)

    def lambda_836C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_836C)
    Sleep(10)

    def lambda_837C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_837C)
    Sleep(10)

    def lambda_838C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_838C)
    Sleep(10)

    def lambda_839C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_839C)
    Sleep(10)

    def lambda_83AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_83AC)
    Sleep(10)

    def lambda_83BC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_83BC)
    WaitChrThread(0x105, 2)
    OP_6F(0x1)

    ChrTalk(
        0xF,
        "...*sob, sob*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "M-my... Where did my\x01",
            "favorite pink umbrella\x01",
            "go...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...And there you have\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see...\x02\x03",
            "#00001FDid you look around the\x01",
            "store and outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, Oscar and I looked\x01",
            "everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And... We came across\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennett took out a pink umbrella.\x02",
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
            "#12P#10105FW-Wait, this pink\x01",
            "umbrella is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10305FThis isn't her umbrella?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I thought so too, but\x01",
            "look here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennett showed the handle to the team.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00100FIt says "Meiling".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see...\x02\x03",
            "#00000FIt sounds like someone\x01",
            "grabbed the wrong\x01",
            "umbrella by mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah, that's what I\x01",
            "think as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThere haven't been many\x01",
            "customers today, and besides,\x01",
            "I remember all my customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut this "Meiling" name\x01",
            "doesn't ring a bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI want you to find the one who\x01",
            "took Momo's umbrella by mistake\x01",
            "and collect it for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo, can you help?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, leave it to us.\x02\x03",
            "We'll find the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PGreat! I'm counting on\x01",
            "you, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut I wish we had more\x01",
            "clues about this\x01",
            ""Meiling" name.\x02\x03",
            "#00100FLloyd, any ideas?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88B3)
    Sleep(50)

    def lambda_88C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_88C3)
    Sleep(50)

    def lambda_88D3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_88D3)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FHmm. Actually, I think\x01",
            "I've heard the name\x01",
            "before.\x02\x03",
            "#10106FI wish I could remember\x01",
            "where I heard it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FHmm, now where was it...\x01",
            "(I feel like I've heard\x01",
            "it before as well...)\x02\x03",
            "#00000FIf I remember correctly,\x01",
            ""Meiling" is a resident\x01",
            "of...\x02",
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
            "Central Square\x01",              # 0
            "West Street\x01",                 # 1
            "Residential Street\x01",          # 2
            "East Street\x01",                 # 3
            "Waterfront Area\x01",             # 4
            "Governmental District\x01",       # 5
            "Entertainment District\x01",      # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CC7")
    OP_2C(0x6B, 0x1)

    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a girl\x01",
            "who lives on East Street?\x02\x03",
            "I feel like she's the granddaughter\x01",
            "of Mr. Mors, the Crossbell trade\x01",
            "association president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#12P#00105FOh, now that you mention\x01",
            "it...! I've spoken with\x01",
            "her several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FShe has an older brother\x01",
            "named Roy.\x02\x03",
            "#10300FThey might have come\x01",
            "shopping here together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Oh yeah, that's right!\x01",
            "I remember a brother and\x01",
            "sister stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut the granddaughter of\x01",
            "Mr. Mors. I guess I've\x01",
            "seen her before then, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91A0")

    label("loc_8CC7")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8CF5"),
        (1, "loc_8D44"),
        (2, "loc_8D90"),
        (4, "loc_8DE3"),
        (5, "loc_8E33"),
        (6, "loc_8E89"),
        (SWITCH_DEFAULT, "loc_8EE0"),
    )


    label("loc_8CF5")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives in\x01",
            "Central Square?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8D44")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives on West\x01",
            "Street?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8D90")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives on\x01",
            "Residential Street?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8DE3")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives in\x01",
            "Waterfront Area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8E33")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives in\x01",
            "Governmental District?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8E89")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...the name of a little\x01",
            "girl who lives in\x01",
            "Entertainment District?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE0")

    label("loc_8EE0")


    ChrTalk(
        0x105,
        "#6P#10304FNo, wrong answer.\x02",
    )

    CloseMessageWindow()

    def lambda_8F06():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F06)
    Sleep(50)

    def lambda_8F16():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8F16)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FMeiling is the granddaughter of Mr.\x01",
            "Mors, the Merchants Association\x01",
            "President who lives on East Street.\x02\x03",
            "#10304FShe has an older brother named Roy.\x01",
            "They probably came here together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Oh yeah, that's right!\x01",
            "I remember a brother and\x01",
            "sister stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FI see... So she's Mr.\x01",
            "Mors' granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWe've been over that\x01",
            "many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FBut Wazy, why do you\x01",
            "know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, I've collected\x01",
            "various information\x01",
            "through my hosting jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI-I see... Not that I\x01",
            "can respect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FSettle down, now. And\x01",
            "thanks, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91A0")


    ChrTalk(
        0x8,
        (
            "#11PGreat, then I'll give\x01",
            "you Meiling's umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Here.\x02",
    )

    CloseMessageWindow()

    def lambda_91E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_91E7)
    Sleep(50)

    def lambda_91F7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_91F7)
    Sleep(50)

    def lambda_9207():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9207)
    Sleep(50)

    def lambda_9217():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9217)
    Sleep(50)

    def lambda_9227():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9227)
    WaitChrThread(0xA, 2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x325),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x325, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0xA, 0xB4, 0x3E8, 0x5DC, 0x0)

    ChrTalk(
        0x8,
        (
            "#11PReturn that to Meiling\x01",
            "and get Momo's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'm counting on you,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sob, sob*... Thanks\x01",
            "mister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell then let's go visit\x01",
            "Mr. Mors and see if we\x01",
            "can find her.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9384():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9384)
    Sleep(50)

    def lambda_9394():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9394)
    Sleep(50)

    def lambda_93A4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93A4)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHis house is at the end\x01",
            "of East Street, if I\x01",
            "remember correctly.\x02\x03",
            "Let's head there for\x01",
            "now.\x02",
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
            "Quest [The Vanished\x01",
            "Umbrella]\x07\x00",
            " Started!\x02",
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

    # Function_26_7F28 end

    def Function_27_94B9(): pass

    label("Function_27_94B9")

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
        "#11POh Lloyd! How did it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, we got it back.\x02",
    )

    CloseMessageWindow()

    def lambda_95B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_95B0)
    Sleep(10)

    def lambda_95C0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_95C0)
    Sleep(10)

    def lambda_95D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_95D0)
    Sleep(10)

    def lambda_95E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_95E0)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#00000FHere you go Momo.\x02",
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
            "#16IReturned Momo's umbrella.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x325, 1)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)

    ChrTalk(
        0xF,
        (
            "Sniff.... This is...\x01",
            "Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This is the one daddy\x01",
            "bought me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Thank you! Thank you so\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSure, no problem.\x02\x03",
            "#10100FI'm glad we could get it\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yeah!\x02",
    )

    CloseMessageWindow()

    def lambda_975E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_975E)
    Sleep(50)

    def lambda_976E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_976E)
    Sleep(50)

    def lambda_977E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_977E)
    Sleep(50)

    def lambda_978E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_978E)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10304FCase closed, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYou really saved us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI knew I could count on\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll be sure to call if\x01",
            "we ever need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FPlease do. We'll be\x01",
            "waiting for your\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FLater, Oscar!\x02",
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
            "Quest [The Vanished\x01",
            "Umbrella]\x07\x00",
            " completed!\x02",
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

    # Function_27_94B9 end

    def Function_28_993D(): pass

    label("Function_28_993D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B02")

    ChrTalk(
        0x8,
        (
            "Oh, thanks for coming,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bennett made the new\x01",
            "bread this time. Try\x01",
            "some.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x212, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar. I'll eat\x01",
            "it a bit later.\x02\x03",
            "We're here for work\x01",
            "today, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B67")

    label("loc_9B02")


    ChrTalk(
        0x8,
        (
            "Oh, thanks for coming,\x01",
            "Lloyd. Want some of our\x01",
            "bread?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, I'm here for work\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B67")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, that reminds me. I\x01",
            "did hear about something\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right. Although I'm\x01",
            "pleased to recommend all\x01",
            "our bread...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C92")

    ChrTalk(
        0x8,
        (
            "If I had to pick one, it'd\x01",
            "be the "Bennett Wonderful"\x01",
            "I just gave you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Jump("loc_9CE1")

    label("loc_9C92")


    ChrTalk(
        0x8,
        (
            "If I had to pick one, it'd\x01",
            "be the "Bennett Wonderful"\x01",
            "I gave you earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CE1")


    ChrTalk(
        0x102,
        "#00105FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Even though Bennett\x01",
            "came up with it, it's\x01",
            "really very well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want Morges'\x01",
            "best, it has to be this\x01",
            "one─\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Bennett's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "H-Hey, wait a second!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_9DC5():

        label("loc_9DC5")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9DC5")

    QueueWorkItem2(0x109, 0, lambda_9DC5)

    def lambda_9DD7():

        label("loc_9DD7")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9DD7")

    QueueWorkItem2(0x102, 0, lambda_9DD7)

    def lambda_9DE9():

        label("loc_9DE9")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9DE9")

    QueueWorkItem2(0x104, 0, lambda_9DE9)

    def lambda_9DFB():

        label("loc_9DFB")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9DFB")

    QueueWorkItem2(0x101, 0, lambda_9DFB)

    def lambda_9E0D():

        label("loc_9E0D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9E0D")

    QueueWorkItem2(0x105, 0, lambda_9E0D)

    def lambda_9E1F():

        label("loc_9E1F")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9E1F")

    QueueWorkItem2(0x103, 0, lambda_9E1F)

    def lambda_9E31():

        label("loc_9E31")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9E31")

    QueueWorkItem2(0x8, 1, lambda_9E31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ECC")
    OP_68(55480, 1510, 1690, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9E7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9E7F)
    SetChrPos(0xA, 60080, 10, 4000, 135)
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 57580, 10, 2090, 3000, 0x0)
    OP_64(0xA)
    Jump("loc_9F4D")

    label("loc_9ECC")

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

    label("loc_9F4D")

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
            "Oh, Bennett. I was just\x01",
            "recommending your─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-What do you think you're\x01",
            "doing!? I'm not finished\x01",
            "developing that yet!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Putting my bread in the\x01",
            "Gourmet Guide before I've\x01",
            "surpassed you is...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, don't worry about\x01",
            "it. It's this delicious\x01",
            "already, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A-Anyway... If you're going to\x01",
            "go and recommend it anyway, I'll\x01",
            "never consent to it, you hear!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A15A")
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 60330, 0, 3200, 3000, 0x0)

    def lambda_A124():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_A124)
    OP_95(0xA, 60080, 10, 4000, 2000, 0x0)
    SetChrPos(0xA, 119120, 0, -660, 275)
    Jump("loc_A1CB")

    label("loc_A15A")

    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 52110, 1000, 10270, 3000, 0x0)
    OP_95(0xA, 51750, 1000, 10270, 3000, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A1B5")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    Jump("loc_A1C6")

    label("loc_A1B5")

    SetChrPos(0xA, 51280, 1000, 12870, 90)

    label("loc_A1C6")

    ClearChrFlags(0xA, 0x4)

    label("loc_A1CB")

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
            "Man, she's always like\x01",
            "this. And just because I\x01",
            "said it was delicious, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2E2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A2E2)
    Sleep(50)

    def lambda_A2F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A2F2)
    Sleep(50)

    def lambda_A302():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A302)
    Sleep(50)

    def lambda_A312():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A312)
    Sleep(50)

    def lambda_A322():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A322)
    Sleep(50)

    def lambda_A332():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A332)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304FHaha, that's probably\x01",
            "why she's this\x01",
            "concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, you need to settle\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FA-Anyway... If Bennett is\x01",
            "that against it, could you\x01",
            "recommend something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then I'll have you try\x01",
            "my latest creation, the\x01",
            ""Thick Cutlet Sandwich".\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate\x01",
            "the Thick Cutlet\x01",
            "Sandwich.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10100F*chewing*... Ahh, the\x01",
            "bread is very soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and the sauce is\x01",
            "juicy. This is good,\x01",
            "Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm still working on it\x01",
            "though. It'll be a while\x01",
            "before it's for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FI see...\x02\x03",
            "#00203FIn that case, maybe you\x01",
            "should have picked something\x01",
            "else for us to try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, when it's finished I'll\x01",
            "give you more on the house,\x01",
            "so please wait until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, we'll be looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6A5")
    SetScenarioFlags(0x1, 2)

    label("loc_A6A5")

    SetScenarioFlags(0x172, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A6D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A6F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A709")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A71C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A739")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A74C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A769")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A77C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A799")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A7AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A7C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7C9")

    OP_29(0x80, 0x1, 0x6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8D4")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A8CB")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A8CB")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_A8D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9C2")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A9C2")

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

    # Function_28_993D end

    def Function_29_A9F6(): pass

    label("Function_29_A9F6")

    TalkBegin(0xA)

    ChrTalk(
        0xA,
        (
            "*sigh*... My new bread\x01",
            "to surpass Oscar's still\x01",
            "isn't done yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, I won't give up.\x01",
            "I'll try as many times\x01",
            "as I have to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She might make a good\x01",
            "worker for the\x01",
            "pageant...)\x02\x03",
            "#00000FUmm, excuse me. I've a\x01",
            "little something to ask\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Bennett to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "...What, a pageant!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-I'll pass. I don't\x01",
            "have the figure for\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm helping cook for the\x01",
            "charity event. Give me a\x01",
            "break here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI-Is that so... We'll\x01",
            "have to look somewhere\x01",
            "else, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FLet's find someone else.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 6)
    SetScenarioFlags(0x1, 3)
    TalkEnd(0xA)
    Return()

    # Function_29_A9F6 end

    SaveToFile()

Try(main)
