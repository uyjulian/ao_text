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
        "Function_5_774",          # 05, 5
        "Function_6_78E",          # 06, 6
        "Function_7_8E5",          # 07, 7
        "Function_8_2178",         # 08, 8
        "Function_9_24F4",         # 09, 9
        "Function_10_25BE",        # 0A, 10
        "Function_11_2686",        # 0B, 11
        "Function_12_2750",        # 0C, 12
        "Function_13_3955",        # 0D, 13
        "Function_14_3A39",        # 0E, 14
        "Function_15_3CB4",        # 0F, 15
        "Function_16_4C57",        # 10, 16
        "Function_17_4E82",        # 11, 17
        "Function_18_5AB3",        # 12, 18
        "Function_19_5B81",        # 13, 19
        "Function_20_5C18",        # 14, 20
        "Function_21_5C1C",        # 15, 21
        "Function_22_6CFF",        # 16, 22
        "Function_23_74F2",        # 17, 23
        "Function_24_75F0",        # 18, 24
        "Function_25_79AC",        # 19, 25
        "Function_26_80F1",        # 1A, 26
        "Function_27_96D3",        # 1B, 27
        "Function_28_9B73",        # 1C, 28
        "Function_29_AC52",        # 1D, 29
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
            ""The Kingdom of Sweets Vol.1" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_770")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_770")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Mix Gelato"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_770")

    TalkEnd(0xFF)
    Return()

    # Function_4_6BF end

    def Function_5_774(): pass

    label("Function_5_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78A")
    Call(0, 13)
    Jump("loc_78D")

    label("loc_78A")

    Call(0, 6)

    label("loc_78D")

    Return()

    # Function_5_774 end

    def Function_6_78E(): pass

    label("Function_6_78E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C5")
    Call(0, 28)
    Return()

    label("loc_7C5")

    Jump("loc_7EF")

    label("loc_7CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EF")
    Call(0, 26)
    Return()

    label("loc_7EF")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
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

    Jump("loc_7FC")

    label("loc_8E1")

    TalkEnd(0x8)
    Return()

    # Function_6_78E end

    def Function_7_8E5(): pass

    label("Function_7_8E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_900")
    Call(0, 8)
    Jump("loc_2177")

    label("loc_900")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Call(0, 9)
    Jump("loc_2177")

    label("loc_91B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_936")
    Call(0, 10)
    Jump("loc_2177")

    label("loc_936")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951")
    Call(0, 11)
    Jump("loc_2177")

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A02")

    ChrTalk(
        0x8,
        (
            "I didn't want to put that "Thick Cutlet\x01",
            "Sandwich" trial product up for sale.\x02",
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
    Jump("loc_2177")

    label("loc_A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC")

    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I made my special\x01",
            "bread, just for you\x01",
            "guys. Here, take it!\x02",
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
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x214, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002FWow, it smells really good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FYes, it looks delicious♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know, right? It's\x01",
            "our latest product.\x02",
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
    Jump("loc_D57")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC9")

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
            "I can't do anything but bake\x01",
            "delicious bread, but...\x02",
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
    Jump("loc_D57")

    label("loc_CC9")


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

    label("loc_D57")

    Jump("loc_2177")

    label("loc_D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F16")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "It's you... Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOscar... Thank\x01",
            "goodness you're safe.\x02",
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
            "#00006FY-Yeah... \x01",
            "It's a long story.\x02\x03",
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
            "get it, but I'll do\x01",
            "as you say for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys be careful\x01",
            "too, alright?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 3)
    Jump("loc_F80")

    label("loc_F16")


    ChrTalk(
        0x8,
        (
            "I don't really get what's going on,\x01",
            "but at least you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys be careful\x01",
            "too, alright?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    Jump("loc_2177")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A3")

    ChrTalk(
        0x8,
        (
            "Rail service has halted,\x01",
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
            "Well, no matter the situation, I'll\x01",
            "just keep making delicious bread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114F")

    label("loc_10A3")


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
            "Well, no matter the situation, I'll\x01",
            "just keep making delicious bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114F")

    Jump("loc_2177")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1162")
    Jump("loc_2177")

    label("loc_1162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125A")

    ChrTalk(
        0x8,
        (
            "Our customers have been panicking\x01",
            "since early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard the sound of gunfire has been heard in the\x01",
            "vicinity of Mainz ever since yesterday evening.\x02",
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
    Jump("loc_12AA")

    label("loc_125A")


    ChrTalk(
        0x8,
        (
            "Gunfire near Mainz...\x01",
            "How disturbing... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I hope nothing else happens.\x02",
    )

    CloseMessageWindow()

    label("loc_12AA")

    Jump("loc_2177")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")

    ChrTalk(
        0x8,
        (
            "Bennett is\x01",
            "very helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When she heard I wanted to make \x01",
            "bread,, she complained about it \x01",
            "but taught me just the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Despite appearances, she's\x01",
            "a nice person at her core.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_140C")

    label("loc_1387")


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
            "you should have some of\x01",
            "my freshly baked, fluffy bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140C")

    Jump("loc_2177")

    label("loc_1411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FA")

    ChrTalk(
        0x8,
        (
            "That Bennett kneaded dough\x01",
            "in the kitchen with all her\x01",
            "might that her arms hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since I just had a compress,\x01",
            "I pasted it to her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not good to overdo it.\x01",
            "I'll have to monitor her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_158B")

    label("loc_14FA")


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
            "I'll have to watch her to make sure she\x01",
            "doesn't overdo it and hurt herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_163E")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get coverage for\x01",
            "the gourmet guide here, but...)\x02\x03",
            "#00003F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163E")

    Jump("loc_2177")

    label("loc_1643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_179B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")

    ChrTalk(
        0x8,
        (
            "Bennett's new bread\x01",
            "is selling well.\x02",
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
            "Hmm, could it be\x01",
            "that she hates me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1796")

    label("loc_1702")


    ChrTalk(
        0x8,
        (
            "I'll have to ask if I've done\x01",
            "something wrong and apologize for it.\x02",
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

    label("loc_1796")

    Jump("loc_2177")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183D")

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
    Jump("loc_18AF")

    label("loc_183D")


    ChrTalk(
        0x8,
        (
            "Bennett has been\x01",
            "making some tasty\x01",
            "bread lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's Master's daughter\x01",
            "for you. I won't lose to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AF")

    Jump("loc_2177")

    label("loc_18B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AA")

    ChrTalk(
        0x8,
        (
            "Reporters have crowded the\x01",
            "place since early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see a lot of\x01",
            "salarymen and business\x01",
            "men most mornings.\x02",
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
    Jump("loc_1A56")

    label("loc_19AA")


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

    label("loc_1A56")

    Jump("loc_2177")

    label("loc_1A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB7")

    ChrTalk(
        0x8,
        (
            "Isn't it rare to see\x01",
            "you loitering around\x01",
            "at such an hour?\x02",
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
            "For you, it's ok.\x01",
            "Look all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks, Oscar. \x01",
            "We'll do that by all m......\x02",
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
            "#00006F(I-If we're going to buy, it seems\x01",
            "it would be better doing it fast.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C14")

    label("loc_1BB7")


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
            "For you, it's ok.\x01",
            "Look all you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C14")

    Jump("loc_2177")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCA")

    ChrTalk(
        0x8,
        (
            "The other day, I got\x01",
            "a letter that says \x01",
            ""I'm a fan of yours."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I'm not an\x01",
            "Arc-en-ciel artist\x01",
            "or anything, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's possible they got the\x01",
            "addressee wrong. If another\x01",
            "comes, I'll have to return it.\x02",
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
            "#00006FI-I wonder if you\x01",
            "really should.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh? Really?\x01",
            "I don't really get it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E52")

    label("loc_1DCA")


    ChrTalk(
        0x8,
        (
            "Even so, Bennett\x01",
            "looked strange when\x01",
            "I got the letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She asked me about its\x01",
            "content... Does she want\x01",
            "to read it that badly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E52")

    Jump("loc_2177")

    label("loc_1E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F68")

    ChrTalk(
        0x8,
        (
            "Bennett has been making better\x01",
            "bread than before lately.\x02",
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
    Jump("loc_1FFD")

    label("loc_1F68")


    ChrTalk(
        0x8,
        (
            "In order to not lose to Bennett,\x01",
            "I'll have to practice more, too.\x02",
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

    label("loc_1FFD")

    Jump("loc_2177")

    label("loc_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_20D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2090")

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
            "Thank you, I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D1")

    label("loc_2090")


    ChrTalk(
        0x8,
        "Thanks for all your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I knew I could\x01",
            "count on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D1")

    Return()

    label("loc_20D2")

    Jump("loc_2177")

    label("loc_20D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2177")

    ChrTalk(
        0x8,
        (
            "Lately, I've challenged myself\x01",
            "to make more new kinds of bread.\x02",
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

    label("loc_2177")

    Return()

    # Function_7_8E5 end

    def Function_8_2178(): pass

    label("Function_8_2178")


    ChrTalk(
        0x8,
        "Ooh, if it isn't Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHi, Oscar. Long time no see.\x01",
            "How is work going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, just making my bread\x01",
            "like usual, day after day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, I haven't\x01",
            "seen your face\x01",
            "in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Were you slacking off\x01",
            "in Michelam, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FCome on, you know\x01",
            "that's not true.\x02\x03",
            "#00001FAnd I told you properly about my\x01",
            ""Temporary separation from the\x01",
            "SSS for training", didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, is that so?\x01",
            "I totally forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well anyway, take\x01",
            "this to commemorate\x01",
            "our meeting, alright?\x02",
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
            " received.\x02",
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
            "#00105FThis is... The usual\x01",
            "new bread, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FWow, it smells great, doesn't it.\x02",
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
            "Yeah, it's fresh-baked and fluffy.\x01",
            "I'm sure you'll love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He he, buy a lot more if\x01",
            "you like that one, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks Oscar.\x01",
            "We'll savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)
    Return()

    # Function_8_2178 end

    def Function_9_24F4(): pass

    label("Function_9_24F4")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm making a new bread\x01",
            "today too. Here, try some.\x02",
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
            " received.\x02",
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
            "#00000FThanks Oscar.\x01",
            "We'll savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 1)
    Return()

    # Function_9_24F4 end

    def Function_10_25BE(): pass

    label("Function_10_25BE")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bennett made the\x01",
            "new bread this time.\x01",
            "Try some.\x02",
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
            " received.\x02",
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
            "#00000FThanks Oscar.\x01",
            "We'll savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Return()

    # Function_10_25BE end

    def Function_11_2686(): pass

    label("Function_11_2686")


    ChrTalk(
        0x8,
        "Oh, thanks for coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm making a new bread\x01",
            "today too. Here, try some.\x02",
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
            " received.\x02",
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
            "#00000FThanks Oscar.\x01",
            "We'll savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Return()

    # Function_11_2686 end

    def Function_12_2750(): pass

    label("Function_12_2750")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_292F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2875")

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
            "Both Oscar and Bennett are working\x01",
            "harder than they ever have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_292A")

    label("loc_2875")


    ChrTalk(
        0xFE,
        (
            "With the trade routes restored, \x01",
            "I'll get fresh flour from Armorica. \x01",
            "We'll be back on our feet in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Oscar and Bennett are working\x01",
            "harder than they ever have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292A")

    Jump("loc_3951")

    label("loc_292F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_29D2")

    ChrTalk(
        0xFE,
        (
            "With martial law declared like this,\x01",
            "customers don't come, so I can focus\x01",
            "on developing my new bread recipes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, what's going on?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_29D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")

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
            "We'll have to make do with all Crossbell\x01",
            "native ingredients for awhile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B5F")

    label("loc_2ACB")


    ChrTalk(
        0xFE,
        (
            "Hmm, but... We'll be able to\x01",
            "take pride in our [100% Local\x01",
            "Crossbell Bread], I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, I know\x01",
            "I shouldn't talk\x01",
            "that recklessly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5F")

    Jump("loc_3951")

    label("loc_2B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C64")

    ChrTalk(
        0xFE,
        (
            "It's nice to have a reconstruction\x01",
            "assistance sale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar isn't here today, so I'm\x01",
            "sorry for our female customers...\x02",
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
    Jump("loc_2D0E")

    label("loc_2C64")


    ChrTalk(
        0xFE,
        (
            "Oscar isn't here today, so I'm\x01",
            "sorry for our female customers...\x02",
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

    label("loc_2D0E")

    Jump("loc_3951")

    label("loc_2D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D95")

    ChrTalk(
        0xFE,
        (
            "Hey, it seems the mining\x01",
            "town has been occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who on earth might have done it?\x01",
            "I can't forgive them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_2D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA8")

    ChrTalk(
        0xFE,
        (
            "There's less traffic in\x01",
            "here on rainy days,\x01",
            "to be perfectly honest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we have a lot of regular customers\x01",
            "who come even in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, that's something to be thankful for. It's\x01",
            "probably because we've been in business so long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5C")

    label("loc_2EA8")


    ChrTalk(
        0xFE,
        (
            "We have a lot of regular customers\x01",
            "who come even in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, that's something to be thankful for.\x01",
            "Next time, I'll hold a sale or\x01",
            "something as a thank-you to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5C")

    Jump("loc_3951")

    label("loc_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FA2")

    ChrTalk(
        0xFE,
        (
            "It's noisy out there...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_2FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_303E")

    ChrTalk(
        0xFE,
        (
            "That Bennett...\x01",
            "When I praise her,\x01",
            "she ends up resenting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's 'cause she's shy I guess...\x01",
            "Oh man, what a personality she has.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_303E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3117")

    ChrTalk(
        0xFE,
        (
            "A lot of time has\x01",
            "passed since Oscar\x01",
            "became my apprentice.\x02",
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
            "Hehe, at this rate, I guess\x01",
            "I'll allow Oscar to become\x01",
            "my son-in-law, eh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31B6")

    label("loc_3117")


    ChrTalk(
        0xFE,
        (
            "As things stand, I guess\x01",
            "I'll allow Oscar to become\x01",
            "my son-in-law, eh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it will be a great\x01",
            "victory to me if he becomes\x01",
            "both my son and my heir.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B6")

    Jump("loc_3951")

    label("loc_31BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_327A")

    ChrTalk(
        0xFE,
        (
            "A throng of reporters going to cover the\x01",
            "Trade Conference came through this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I knew we were going to sell\x01",
            "that much, I would have\x01",
            "liked to have baked more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_327A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_333D")

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
            "A bakery preparations start early \x01",
            "in the morning at 3:00, after all.\x01",
            "In preparation for tomorrow,\x01",
            "I'll have to go to rest quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3951")

    label("loc_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3416")

    ChrTalk(
        0xFE,
        (
            "Oscar gets fan\x01",
            "letters from\x01",
            "time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been happening ever since\x01",
            "he was featured in a magazine.\x02",
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
    Jump("loc_34A9")

    label("loc_3416")


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
            "But Bennett's bad\x01",
            "mood is the fly\x01",
            "in the ointment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A9")

    Jump("loc_3951")

    label("loc_34AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357E")

    ChrTalk(
        0xFE,
        (
            "Good grief, Bennett drove\x01",
            "me out of the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately she's been baking\x01",
            "bread like she's possessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, she's doing it out of ambition,\x01",
            "so I suppose that's good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_360E")

    label("loc_357E")


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
            "If that gives her motivation,\x01",
            "I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360E")

    Jump("loc_3951")

    label("loc_3613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3695")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you all...\x01",
            "Are you here for work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please speak with Oscar\x01",
            "and Bennett for the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_379E")

    label("loc_3695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_372D")

    ChrTalk(
        0xFE,
        (
            "If I don't hurry and\x01",
            "make dough, it won't be\x01",
            "ready for the afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, and thanks for your\x01",
            "help with this job matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_379E")

    label("loc_372D")


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
            "I'll now be able to resume\x01",
            "breadmaking without worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379E")

    Jump("loc_3951")

    label("loc_37A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C6")

    ChrTalk(
        0xFE,
        (
            "Lately, I've been leaving almost all our\x01",
            "product development to Oscar and Bennett.\x02",
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
            "I might be able to let them run\x01",
            "the whole store before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3951")

    label("loc_38C6")


    ChrTalk(
        0xFE,
        (
            "I have been especially happy to\x01",
            "see my daughter's growth as a baker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar has played a\x01",
            "huge role in that.\x01",
            "Rivals are important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3951")

    TalkEnd(0xFE)
    Return()

    # Function_12_2750 end

    def Function_13_3955(): pass

    label("Function_13_3955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3983")
    Call(0, 29)
    Return()

    label("loc_3983")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3990")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A35")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_39E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A00")
    OP_AF(0xCB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A30")

    label("loc_3A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A14")
    Jump("loc_3A30")

    label("loc_3A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3A30")

    Jump("loc_3990")

    label("loc_3A35")

    TalkEnd(0xA)
    Return()

    # Function_13_3955 end

    def Function_14_3A39(): pass

    label("Function_14_3A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3AC7")

    ChrTalk(
        0xA,
        (
            "Sorry, but I don't have the\x01",
            "figure for a pageant, do I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm helping with the\x01",
            "event's food, so give\x01",
            "me a break here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB3")

    label("loc_3AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8E")

    ChrTalk(
        0xA,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm making a new bread.\x01",
            "If you like, please try some.\x02",
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
            " received.\x02",
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
            "#00000FThanks,\x01",
            "I'll savor it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Jump("loc_3CB3")

    label("loc_3B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3C")

    ChrTalk(
        0xA,
        (
            "Oscar went to\x01",
            "help with the\x01",
            "charity event.\x02",
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
            "...Wait, n-no!\x01",
            "Forget that!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CB3")

    label("loc_3C3C")


    ChrTalk(
        0xA,
        (
            "W-Well, my task\x01",
            "right now is to\x01",
            "tend the shop.\x02",
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

    label("loc_3CB3")

    Return()

    # Function_14_3A39 end

    def Function_15_3CB4(): pass

    label("Function_15_3CB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3D3D")

    ChrTalk(
        0xFE,
        (
            "That Oscar... He just\x01",
            "went and recommended\x01",
            "my bread to a magazine.\x02",
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
    Jump("loc_4C53")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4D")

    ChrTalk(
        0xFE,
        (
            "In order not to lose to Oscar,\x01",
            "I've got to make lots of new breads\x01",
            "that can make everyone happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But... My bread\x01",
            "doesn't yet hold a\x01",
            "candle to Oscar's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's like this, I guess\x01",
            "I'll take some advice from\x01",
            "Oscar. This sucks a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3ED5")

    label("loc_3E4D")


    ChrTalk(
        0xFE,
        (
            "My bread doesn't hold\x01",
            "a candle to Oscar's yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's like this, I guess\x01",
            "I'll take some advice from\x01",
            "Oscar. This sucks a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED5")

    Jump("loc_4C53")

    label("loc_3EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F91")

    ChrTalk(
        0xFE,
        "I'm ready to close up shop...\x02",
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
        "They're too weird somehow...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FFD")

    label("loc_3F91")


    ChrTalk(
        0xFE,
        "Those monsters outside are too weird...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though they won't attack\x01",
            "us citizens, I can't relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFD")

    Jump("loc_4C53")

    label("loc_4002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4116")

    ChrTalk(
        0xFE,
        (
            "Both Oscar and my father are oddly\x01",
            "positive, given the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Will we really be all right?\x01",
            "Even if he is Mr. Arios, the enemies\x01",
            "are the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, even if I worry about it,\x01",
            "it's not like anything will change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41A8")

    label("loc_4116")


    ChrTalk(
        0xFE,
        (
            "Even if he is Mr. Arios, the enemies\x01",
            "are the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, even if I worry about it,\x01",
            "it's not like anything will change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A8")

    Jump("loc_4C53")

    label("loc_41AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41C2")
    TalkEnd(0xFE)
    Call(0, 13)
    Return()

    label("loc_41C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_42D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426C")

    ChrTalk(
        0xFE,
        (
            "Oh yeah, I'll mix that herb\x01",
            "into my next new bread and...\x02",
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
    Jump("loc_42CF")

    label("loc_426C")


    ChrTalk(
        0xFE,
        (
            "I was planning out\x01",
            "my next new bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think we have some\x01",
            "of that herb in stock...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CF")

    Jump("loc_4C53")

    label("loc_42D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42E5")
    Call(0, 16)
    Jump("loc_4C53")

    label("loc_42E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_43F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4385")

    ChrTalk(
        0xFE,
        "...Mrr, that Oscar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's making a huge mistake if\x01",
            "he thinks he can butter me up\x01",
            "with a compress like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Hmph.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43F4")

    label("loc_4385")


    ChrTalk(
        0xFE,
        "That Oscar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's making a huge mistake if\x01",
            "he thinks he can butter me up\x01",
            "with a compress like this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F4")

    Jump("loc_4C53")

    label("loc_43F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_458A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F0")

    ChrTalk(
        0xFE,
        (
            "Grrr, that Oscar...\x01",
            "What's with being so blunt, jeez...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But when he ate it, he really thought it was\x01",
            "delicious, based on his facial expression...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...N-No, that's not it! \x01",
            "There's no way he enjoyed it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4585")

    label("loc_44F0")


    ChrTalk(
        0xFE,
        (
            "Out-out-dark-thoughts!\x01",
            "(*kneading, kneading*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar... I'll get you next time\x01",
            "foooooor sure... I'll make you\x01",
            "regret the day you were born!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4585")

    Jump("loc_4C53")

    label("loc_458A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_46C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4647")

    ChrTalk(
        0xFE,
        (
            "Just when I made better\x01",
            "bread than his, Oscar\x01",
            "looked so happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no! \x01",
            "What I want to see it's\x01",
            "Oscar's mortified face...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oooh, that Oscar...!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_46BB")

    label("loc_4647")


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
        "Show your mortified face already! Jeez!\x02",
    )

    CloseMessageWindow()

    label("loc_46BB")

    Jump("loc_4C53")

    label("loc_46C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475D")

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
        "Oooh, what the heck am I doing wrong...!?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47E5")

    label("loc_475D")


    ChrTalk(
        0xFE,
        (
            "Alright. If it's like this,\x01",
            "then I'm left with no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll surpass the "Bennett Special"\x01",
            "and make the ultimate bread...!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E5")

    Jump("loc_4C53")

    label("loc_47EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_485A")

    ChrTalk(
        0xFE,
        (
            "The bread I made\x01",
            "is losing in sales\x01",
            "to Oscar's...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grrr, tomorrow, for sure, I'll...!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C53")

    label("loc_485A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4928")

    ChrTalk(
        0xFE,
        (
            "It seems Oscar got a weird\x01",
            "letter the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be a\x01",
            "love letter...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's so full of himself, and\x01",
            "just because he can make\x01",
            "bread a little better than I!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49AF")

    label("loc_4928")


    ChrTalk(
        0xFE,
        (
            "Who...who sent\x01",
            "a love letter\x01",
            "to Oscar...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, no, that's not it.\x01",
            "T-To think a guy like Oscar\x01",
            "could get a love letter...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49AF")

    Jump("loc_4C53")

    label("loc_49B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A1E")

    ChrTalk(
        0xFE,
        "(*knead, knead*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*mumble*...\x01",
            "I definitely won't lose\x01",
            "to the likes of Oscar...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C53")

    label("loc_4A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4B09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8C")

    ChrTalk(
        0xA,
        (
            "You guys take care of the umbrella.\x01",
            "I'll look after the girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC8")

    label("loc_4A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA1")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_4AC8")

    label("loc_4AA1")


    ChrTalk(
        0xA,
        "I mean seriously. How annoying...\x02",
    )

    CloseMessageWindow()

    label("loc_4AC8")

    TalkEnd(0xFE)
    Return()

    label("loc_4ACC")


    ChrTalk(
        0xA,
        "Hey, don't cry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "We'll definitely find it, ok?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C53")

    label("loc_4B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BDF")

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
            "I'm pretty angry that most\x01",
            "of them are Oscar's, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Oscar... I'll overtake him\x01",
            "one of these days. Mark my words!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C53")

    label("loc_4BDF")


    ChrTalk(
        0xFE,
        (
            "That Oscar is really skilled.\x01",
            "This is gonna be tough, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely overtake him.\x01",
            "Mark my words!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C53")

    TalkEnd(0xFE)
    Return()

    # Function_15_3CB4 end

    def Function_16_4C57(): pass

    label("Function_16_4C57")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D55")

    ChrTalk(
        0xA,
        (
            "Then, please\x01",
            "take this to Mr.\x01",
            "Tallys for me.\x02",
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
        "...*sniff*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, enough of this. I'll exchange\x01",
            "it for you, so don't cry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E79")

    label("loc_4D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E2B")

    ChrTalk(
        0xA,
        "Are you here on an errand today too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Careful not to lose\x01",
            "your umbrella again.\x02",
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
            "Hmm, I see.\x01",
            "That's a relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E79")

    label("loc_4E2B")


    ChrTalk(
        0xA,
        (
            "Uh uh, you have good\x01",
            "handwriting, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I-Is that so?\x01",
            "Ehehe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E79")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_16_4C57 end

    def Function_17_4E82(): pass

    label("Function_17_4E82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3D")

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
            "I think I'll buy enough for\x01",
            "my family and return home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FD5")

    label("loc_4F3D")


    ChrTalk(
        0xFE,
        (
            "By the way, Chiruru said she was\x01",
            "leaving on a trip again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll be all right. The\x01",
            "highways have gotten dangerous again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD5")

    Jump("loc_5AAF")

    label("loc_4FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4FE8")
    Jump("loc_5AAF")

    label("loc_4FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_50BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507C")

    ChrTalk(
        0xFE,
        (
            "Looks like Chiruru\x01",
            "returned home.\x02",
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
    Jump("loc_50B8")

    label("loc_507C")


    ChrTalk(
        0xFE,
        (
            "I think I'll go home today\x01",
            "without taking any detours.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B8")

    Jump("loc_5AAF")

    label("loc_50BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5142")

    ChrTalk(
        0xFE,
        (
            "For today's reconstruction sale,\x01",
            "some of the bread is half off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sales don't happen often,\x01",
            "so I'll buy a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAF")

    label("loc_5142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_51C6")

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
            "It can't be helped, given that an\x01",
            "incident like that occurred...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAF")

    label("loc_51C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_527E")

    ChrTalk(
        0xFE,
        (
            "Come to think of it...\x01",
            "Arc-en-ciel's public\x01",
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
    Jump("loc_5AAF")

    label("loc_527E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_528C")
    Jump("loc_5AAF")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A7")
    Call(0, 18)
    Jump("loc_5322")

    label("loc_52A7")


    ChrTalk(
        0xFE,
        (
            "...Huh, do I hear Miss\x01",
            "Bennett's voice from there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, her new bread is popular,\x01",
            "so she must be working hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5322")

    Jump("loc_5AAF")

    label("loc_5327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5452")

    ChrTalk(
        0xFE,
        (
            "Hmm, so Miss Bennett baked \x01",
            "the new bread this time, did she?\x02",
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
        "Hmm, I have to eat it now!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54CB")

    label("loc_5452")


    ChrTalk(
        0xFE,
        (
            "It looks like Miss Bennett made\x01",
            "the new bread this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a very cute bread... \x01",
            "Hmm, I have to eat it now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54CB")

    Jump("loc_5AAF")

    label("loc_54D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551A")

    ChrTalk(
        0xFE,
        (
            "Aww, they're all sold\x01",
            "out of the morning\x01",
            "bread I like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAF")

    label("loc_551A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5528")
    Jump("loc_5AAF")

    label("loc_5528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FA")

    ChrTalk(
        0xFE,
        (
            "By the way, Chiruru got back\x01",
            "from her trip the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. It would have been nice\x01",
            "if she let me know she was back.\x02",
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
    Jump("loc_5660")

    label("loc_55FA")


    ChrTalk(
        0xFE,
        (
            "That girl! She's really\x01",
            "never at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While she's back, I would\x01",
            "like to have tea with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5660")

    Jump("loc_5AAF")

    label("loc_5665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5742")

    ChrTalk(
        0xFE,
        (
            "Ah, the new bread...\x01",
            "It looks delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stuffing custard\x01",
            "cream into soft\x01",
            "melon bread...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems it'll get me a little fat, but... Yeah,\x01",
            "I won't worry about that and buy it anyway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57A8")

    label("loc_5742")


    ChrTalk(
        0xFE,
        (
            "It'll be a waste not eating\x01",
            "such a delicious-looking bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll buy several and head home.\x02",
    )

    CloseMessageWindow()

    label("loc_57A8")

    Jump("loc_5AAF")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5950")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586D")

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
            "They were about the same\x01",
            "age as Momo... I'm\x01",
            "pretty sure on this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58DD")

    label("loc_586D")


    ChrTalk(
        0xFE,
        (
            "Uh uh, thank goodness you\x01",
            "found Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll buy\x01",
            "some bread and head home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58DD")

    TalkEnd(0xFE)
    Return()

    label("loc_58E1")


    ChrTalk(
        0xFE,
        (
            "That crying little girl is the\x01",
            "daughter of that store's owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened to her...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AAF")

    label("loc_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A23")

    ChrTalk(
        0xFE,
        "Let's see, the new bread this time is...\x02",
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
            "Uh uh, I'll buy the new bread,\x01",
            "have tea and go home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5AAF")

    label("loc_5A23")


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
            "Uh uh, I'll buy the new bread,\x01",
            "have tea and go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AAF")

    TalkEnd(0xFE)
    Return()

    # Function_17_4E82 end

    def Function_18_5AB3(): pass

    label("Function_18_5AB3")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Chiruru, which one would you like?\x02",
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
            "...Then I'll go\x01",
            "with that one too.\x01",
            "It's kind of cute.\x02",
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

    # Function_18_5AB3 end

    def Function_19_5B81(): pass

    label("Function_19_5B81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5B92")
    Jump("loc_5C14")

    label("loc_5B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BAD")
    Call(0, 18)
    Jump("loc_5C14")

    label("loc_5BAD")


    ChrTalk(
        0xFE,
        (
            "Whenever I leave on a trip,\x01",
            "I come here to buy a lunchbox.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even so, this bread is so cute...\x02",
    )

    CloseMessageWindow()

    label("loc_5C14")

    TalkEnd(0xFE)
    Return()

    # Function_19_5B81 end

    def Function_20_5C18(): pass

    label("Function_20_5C18")

    Call(0, 21)
    Return()

    # Function_20_5C18 end

    def Function_21_5C1C(): pass

    label("Function_21_5C1C")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CFB")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C79")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5C79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C98")
    OP_AF(0x31)
    Jump("loc_5D1A")

    label("loc_5C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5CA8")
    OP_AF(0x30)
    Jump("loc_5D1A")

    label("loc_5CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5CB8")
    OP_AF(0x2F)
    Jump("loc_5D1A")

    label("loc_5CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5CC8")
    OP_AF(0x2E)
    Jump("loc_5D1A")

    label("loc_5CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5CD8")
    OP_AF(0x2D)
    Jump("loc_5D1A")

    label("loc_5CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5CE8")
    OP_AF(0x2C)
    Jump("loc_5D1A")

    label("loc_5CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5CF8")
    OP_AF(0x2B)
    Jump("loc_5D1A")

    label("loc_5CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D08")
    OP_AF(0x2A)
    Jump("loc_5D1A")

    label("loc_5D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D18")
    OP_AF(0x29)
    Jump("loc_5D1A")

    label("loc_5D18")

    OP_AF(0x28)

    label("loc_5D1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CF6")

    label("loc_5D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3D")
    Jump("loc_6CF6")

    label("loc_5D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E5A")

    ChrTalk(
        0xD,
        (
            "Trade's been halted for awhile,\x01",
            "and I can't stock a satisfactory\x01",
            "selection of goods, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For now, I'm relieved to see\x01",
            "that Crossbell's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to work to make sure all\x01",
            "families get through this ok.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EFC")

    label("loc_5E5A")


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
            "I've got to work to make sure all\x01",
            "families get through this ok.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EFC")

    Jump("loc_6CF6")

    label("loc_5F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5FE3")

    ChrTalk(
        0xD,
        (
            "I-I wonder what are...those monsters\x01",
            "that looks like Middle Ages armors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A-Anyway, even though things are this bad,\x01",
            "you came all the way to the store. If there's\x01",
            "something you want, just let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_5FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60AB")

    ChrTalk(
        0xD,
        (
            "Hearing Mr. Dieter's speech made\x01",
            "me feel independence is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't know what dangers\x01",
            "lie ahead, but... I'll do\x01",
            "whatever I must to\x01",
            "protect Momo and Elsa.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_610E")

    label("loc_60AB")


    ChrTalk(
        0xD,
        (
            "I don't know what dangers\x01",
            "lie ahead, but... I'll do\x01",
            "whatever I must to\x01",
            "protect Momo and Elsa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_610E")

    Jump("loc_6CF6")

    label("loc_6113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6198")

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
            "We're having a sale\x01",
            "on daily necessities.\x01",
            "Please, take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_6198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627B")

    ChrTalk(
        0xD,
        (
            "That Mainz incident... There's a\x01",
            "rumor that the Empire was pulling\x01",
            "the strings behind the scenes.\x02",
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
            "If the rumor is true, then\x01",
            "I can't forgive the Empire.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_62FA")

    label("loc_627B")


    ChrTalk(
        0xD,
        (
            "It's possible that\x01",
            "they were targeting\x01",
            "Crossbell City itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If the rumor is true, then\x01",
            "I can't forgive the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FA")

    Jump("loc_6CF6")

    label("loc_62FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_63BE")

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
            "Many places rely on\x01",
            "railway for stocking up,\x01",
            "so I guess everyone is relieved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_63BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_650E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A4")

    ChrTalk(
        0xD,
        (
            "Hearing the sound of ambulances,\x01",
            "I rushed out of the store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*... I was a little\x01",
            "relieved to see that\x01",
            "Momo wasn't hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, there were so many of them.\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6509")

    label("loc_64A4")


    ChrTalk(
        0xD,
        (
            "It seems many\x01",
            "ambulances passed by...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've got to warn the kids\x01",
            "not to play in the street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6509")

    Jump("loc_6CF6")

    label("loc_650E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65B2")

    ChrTalk(
        0xD,
        (
            "It seems Momo and the others were\x01",
            "playing in the street today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There has been more traffic lately, so\x01",
            "I hope they're watching out for cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_65B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_672F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669B")

    ChrTalk(
        0xD,
        (
            "It would be good if Crossbell\x01",
            "was independent from the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, if we were independent,\x01",
            "they would probably\x01",
            "become our enemies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm, this is a difficult problem, isn't it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_672A")

    label("loc_669B")


    ChrTalk(
        0xD,
        (
            "I think Crossbell independence\x01",
            "would be a good thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's scary to think the Empire and\x01",
            "Republic would become our enemies...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672A")

    Jump("loc_6CF6")

    label("loc_672F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67E6")

    ChrTalk(
        0xD,
        (
            "I'm sure a Trade Conference article will be on\x01",
            "the front page of the next Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think it'll sell more than usual,\x01",
            "so I need to stock up on those.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_67E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_686A")

    ChrTalk(
        0xD,
        (
            "Hey, welcome! \x01",
            "Do you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I intend to keep the\x01",
            "store open for a little\x01",
            "more, so take your time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF6")

    label("loc_686A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_69DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6954")

    ChrTalk(
        0xD,
        (
            "The Orchis Tower inauguration\x01",
            "ceremony was today, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, I wanted to see it but it\x01",
            "would've meant to close the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Uh uh, big buildings and cars are\x01",
            "things boys eternally long for.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69D9")

    label("loc_6954")


    ChrTalk(
        0xD,
        (
            "Big buildings like Orchis\x01",
            "Tower and cars are things\x01",
            "boys eternally long for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "They always get so excited\x01",
            "over those things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D9")

    Jump("loc_6CF6")

    label("loc_69DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AC9")

    ChrTalk(
        0xD,
        (
            "I've been seeing officers\x01",
            "in the city often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It must be for the VIPs\x01",
            "from each country who're\x01",
            "going to come to Crossbell.\x02",
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
    Jump("loc_6B54")

    label("loc_6AC9")


    ChrTalk(
        0xD,
        (
            "It seems the police have stepped\x01",
            "up security in the city.\x02",
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

    label("loc_6B54")

    Jump("loc_6CF6")

    label("loc_6B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1F")

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
            "But... She's taking\x01",
            "a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Maybe she didn't understand\x01",
            "the new bread or something\x01",
            "I asked her to buy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C6B")

    label("loc_6C1F")


    ChrTalk(
        0xD,
        (
            "Momo sure is taking a long time.\x01",
            "Could something have happened to her?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6B")

    Jump("loc_6CF6")

    label("loc_6C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6CF6")

    ChrTalk(
        0xD,
        (
            "Hey there. Welcome to\x01",
            ""Tallys' General Store".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Leave all your daily necessities\x01",
            "to us. Please, take a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF6")

    Jump("loc_5C29")

    label("loc_6CFB")

    TalkEnd(0xD)
    Return()

    # Function_21_5C1C end

    def Function_22_6CFF(): pass

    label("Function_22_6CFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E16")

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
            "That's the first time I ever saw\x01",
            "her insist on anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about her going outside\x01",
            "alone, but I understand how she feels.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6EC7")

    label("loc_6E16")


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
            "I'm worried about her going outside\x01",
            "alone, but I understand how she feels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EC7")

    Jump("loc_74EE")

    label("loc_6ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F4F")

    ChrTalk(
        0xFE,
        (
            "To think things like that\x01",
            "have appeared in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this the meaning of the\x01",
            "President's martial law?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74EE")

    label("loc_6F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_70E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_704E")

    ChrTalk(
        0xFE,
        (
            "It looks like Crossbell will only grow\x01",
            "even more unstable at this rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo might not like it,\x01",
            "but... I can't leave her\x01",
            "alone outside for too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but worry about her\x01",
            "whenever she's out of sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_70E3")

    label("loc_704E")


    ChrTalk(
        0xFE,
        (
            "Momo might not like it,\x01",
            "but... I can't leave her\x01",
            "alone outside for too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but worry about her\x01",
            "whenever she's out of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70E3")

    Jump("loc_74EE")

    label("loc_70E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_717C")

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
            "A week has passed since that incident,\x01",
            "and I want to think it's fine, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74EE")

    label("loc_717C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_718A")
    Jump("loc_74EE")

    label("loc_718A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7201")

    ChrTalk(
        0xFE,
        (
            "I asked Momo to get a baguette\x01",
            "to go with tonight's beef stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder when she'll be back...\x02",
    )

    CloseMessageWindow()
    Jump("loc_74EE")

    label("loc_7201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_720F")
    Jump("loc_74EE")

    label("loc_720F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_721D")
    Jump("loc_74EE")

    label("loc_721D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_722B")
    Jump("loc_74EE")

    label("loc_722B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72EA")

    ChrTalk(
        0xFE,
        (
            "Momo went to play with\x01",
            "Henri and Ryｹ again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though that girl is shy, she's\x01",
            "been getting less so, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I have to thank\x01",
            "Ryｹ and Henri.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7330")

    label("loc_72EA")


    ChrTalk(
        0xFE,
        (
            "Now then, I wonder if\x01",
            "she'll be hungry when\x01",
            "she gets back today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7330")

    Jump("loc_74EE")

    label("loc_7335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_738C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7355")
    Call(0, 23)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_7387")

    label("loc_7355")


    ChrTalk(
        0xFE,
        (
            "Uh uh, oh Momo, she\x01",
            "really had a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7387")

    Jump("loc_74EE")

    label("loc_738C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_739A")
    Jump("loc_74EE")

    label("loc_739A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_73A8")
    Jump("loc_74EE")

    label("loc_73A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_745C")

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
            "Uh uh, it seems she wanted\x01",
            "to use the umbrella her\x01",
            "father bought her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_74E0")

    label("loc_745C")


    ChrTalk(
        0xFE,
        (
            "That umbrella was bought\x01",
            "by her father, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's Momo's favorite color, pink,\x01",
            "and it looks like she loves it a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E0")

    Jump("loc_74EE")

    label("loc_74E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_74EE")

    label("loc_74EE")

    TalkEnd(0xFE)
    Return()

    # Function_22_6CFF end

    def Function_23_74F2(): pass

    label("Function_23_74F2")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "......And then, and then... \x01",
            "Ryｹ tried to enter\x01",
            "Orchis Tower on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "And when he did it, even Henri and\x01",
            "Momo were scolded by an officer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My my... \x01",
            "That was terrible, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But, but... \x01",
            "It was really fun...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_23_74F2 end

    def Function_24_75F0(): pass

    label("Function_24_75F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7601")
    Jump("loc_79A8")

    label("loc_7601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_765F")

    ChrTalk(
        0xFE,
        "Ooh, it's scary outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if Ryｹ and Henri are all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_79A8")

    label("loc_765F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_76C1")

    ChrTalk(
        0xFE,
        (
            "Mama and papa look\x01",
            "really uneasy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo's getting uneasy\x01",
            "too, somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A8")

    label("loc_76C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_773B")

    ChrTalk(
        0xFE,
        (
            "Mama has been stopping\x01",
            "me whenever I try to\x01",
            "go play outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to play with\x01",
            "Ryｹ and Henri...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A8")

    label("loc_773B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7749")
    Jump("loc_79A8")

    label("loc_7749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_775A")
    Call(0, 16)
    Jump("loc_79A8")

    label("loc_775A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7768")
    Jump("loc_79A8")

    label("loc_7768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7776")
    Jump("loc_79A8")

    label("loc_7776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77EE")

    ChrTalk(
        0xFE,
        "I'm helping with the shop today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't just play all time. \x01",
            "You've got to help out too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79A8")

    label("loc_77EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77FC")
    Jump("loc_79A8")

    label("loc_77FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_78B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7817")
    Call(0, 23)
    Jump("loc_78B1")

    label("loc_7817")


    ChrTalk(
        0xFE,
        (
            "Ryｹ was fun.\x01",
            "He tried to make it seem like\x01",
            "it was all Henri's fault...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he was found out at\x01",
            "once and scolded even\x01",
            "more. *chuckle chuckle*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B1")

    Jump("loc_79A8")

    label("loc_78B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78C4")
    Jump("loc_79A8")

    label("loc_78C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_78D2")
    Jump("loc_79A8")

    label("loc_78D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_799F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7987")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_794A")

    ChrTalk(
        0xF,
        "That umbrella is precious to me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*cry, cry*...\x01",
            "Please, mister...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7983")

    label("loc_794A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795F")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_7983")

    label("loc_795F")


    ChrTalk(
        0xF,
        (
            "Ehehe, you're\x01",
            "nice, big sis...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7983")

    TalkEnd(0xFE)
    Return()

    label("loc_7987")


    ChrTalk(
        0xF,
        "*cry, cry*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_79A8")

    label("loc_799F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_79A8")

    label("loc_79A8")

    TalkEnd(0xFE)
    Return()

    # Function_24_75F0 end

    def Function_25_79AC(): pass

    label("Function_25_79AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8093")

    ChrTalk(
        0xFE,
        "Ah, the Special Support Section!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou're Pete, Lawyer Ian's\x01",
            "assistant, if I recall.\x02\x03",
            "#00001FIt looks like you're alone though. \x01",
            "Where's Mr. Grimwood?\x02",
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
            "Ever since he left me in charge,\x01",
            "I haven't been able to get in touch...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7F2D")

    ChrTalk(
        0x102,
        "#00106FMr. Grimwood... I'm worried about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FIf he went to Orchis Tower,\x01",
            "then perhaps he has been\x01",
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
        "Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said something\x01",
            "that's been worrying me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Once the situation is under\x01",
            "control, return to my office\x01",
            "and clean my desk for me."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FCleaning...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. From the start, I thought\x01",
            "he left in a hurry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I do Mr. Grimwood's cleaning,\x01",
            "he regularly tells me to keep away from\x01",
            "his desk as much as possible.\x02",
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
            "#00108FLawyer Ian... It seems like he was\x01",
            "really concerned about that...\x02\x03",
            "#00106FI don't get why he\x01",
            "would ask you to clean\x01",
            "the desk now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00000FPete, please leave\x01",
            "Lawyer Ian to us.\x01",
            "You stay safe here.\x02\x03",
            "If we learn anything, we'll\x01",
            "let you know immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8067")

    label("loc_7F2D")


    ChrTalk(
        0x102,
        "#00106FMr. Grimwood... I'm worried about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208FIf he went to Orchis Tower,\x01",
            "then perhaps he has been\x01",
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
            "Lawyer Ian to us.\x01",
            "You stay safe here.\x02\x03",
            "If we learn anything, we'll\x01",
            "let you know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8067")


    ChrTalk(
        0xFE,
        (
            "U-Understood...\x01",
            "And thank you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 5)
    Jump("loc_80ED")

    label("loc_8093")


    ChrTalk(
        0xFE,
        (
            "Everyone, please do\x01",
            "something for Lawyer Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mr. Grimwood... I hope he's safe.\x02",
    )

    CloseMessageWindow()

    label("loc_80ED")

    TalkEnd(0xFE)
    Return()

    # Function_25_79AC end

    def Function_26_80F1(): pass

    label("Function_26_80F1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_END)), "loc_8222")

    ChrTalk(
        0x101,
        (
            "#6P#00000FHey Oscar. \x01",
            "We saw your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, Lloyd!\x01",
            "I thought you'd come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's sudden but\x01",
            "can you tell us\x01",
            "the details?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8461")

    label("loc_8222")


    ChrTalk(
        0x101,
        (
            "#6P#00000FHey Oscar, it's been awhile.\x01",
            "We saw your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, if it isn't Lloyd!\x01",
            "I thought you'd come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven so, I haven't\x01",
            "seen your face\x01",
            "in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWere you slacking off\x01",
            "in Michelam, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FCome on, you know\x01",
            "that's not true.\x02\x03",
            "#00001FAnd I told you properly about my\x01",
            ""Temporary separation from the\x01",
            "SSS for training", didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, is that so?\x01",
            "I totally forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...We've gotten off topic.\x01",
            "We have to talk about my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell then, can you\x01",
            "give us the details?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)

    label("loc_8461")


    ChrTalk(
        0x8,
        (
            "#11PYeah. The one with the request is\x01",
            "actually little Momo over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PShe is Mr. Tallys' little girl,\x01",
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

    def lambda_8537():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8537)
    Sleep(10)

    def lambda_8547():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_8547)
    Sleep(10)

    def lambda_8557():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8557)
    Sleep(10)

    def lambda_8567():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8567)
    Sleep(10)

    def lambda_8577():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8577)
    Sleep(10)

    def lambda_8587():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8587)
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
            "W-Where did Momo's\x01",
            "favorite pink\x01",
            "umbrella go...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...There lies the problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see...\x02\x03",
            "#00001FDid you look around the store and outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, Oscar and I\x01",
            "looked everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And...we came\x01",
            "across this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennett took out a pink umbrella.\x07\x00\x02",
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
        (
            "#12P#10305FThis isn't that\x01",
            "little girl's umbrella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I thought so too,\x01",
            "but look here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bennett showed the handle\x01",
            "to Lloyd and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt says\x01",
            ""Meiling".\x02",
        )
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
        "#11PYeah, that's what I think as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThere hasn't been many\x01",
            "customers today, and besides,\x01",
            "I remember all my customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut this "Meiling"\x01",
            "name doesn't ring\x01",
            "a bell.\x02",
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
            "#6P#00000FYeah, leave\x01",
            "it to us.\x02\x03",
            "We'll find the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGreat! I'm counting on you, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut I wish we had\x01",
            "more clues about\x01",
            "this "Meiling" name.\x02\x03",
            "#00100FLloyd, any ideas?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A9A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A9A)
    Sleep(50)

    def lambda_8AAA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8AAA)
    Sleep(50)

    def lambda_8ABA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8ABA)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FHmm. I think I have\x01",
            "actually heard the\x01",
            "name before.\x02\x03",
            "#10106FI wish I could remember\x01",
            "where I heard it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FHmm, now where was it...\x01",
            "(I think I've heard it\x01",
            "somewhere before, too...)\x02\x03",
            "#00000FWasn't "Meiling" living in...\x02",
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
            "Residential District\x01",        # 2
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA8")
    OP_2C(0x6B, 0x1)

    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "girl who lives on East Street?\x02\x03",
            "I feel like she's the granddaughter of Mr. Mors,\x01",
            "the Crossbell Merchants Association President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#12P#00105FOh, now that you mention it...!\x01",
            "I've spoken with her several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FShe has an older\x01",
            "brother named Roy.\x02\x03",
            "#10300FThey might have come\x01",
            "shopping here together...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Oh yeah that's right! I remember\x01",
            "a brother and sister stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut the granddaughter of Mr. Mors.\x01",
            "I guess I've seen her before then, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93AB")

    label("loc_8EA8")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8ED6"),
        (1, "loc_8F2C"),
        (2, "loc_8F7F"),
        (4, "loc_8FD2"),
        (5, "loc_9029"),
        (6, "loc_9082"),
        (SWITCH_DEFAULT, "loc_90DC"),
    )


    label("loc_8ED6")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "who lives in Central Square?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_8F2C")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "who lives on West Street?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_8F7F")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "who lives on East Street?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_8FD2")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "who lives in Waterfront Area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_9029")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "lives in Governmental District?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_9082")


    ChrTalk(
        0x101,
        (
            "#11P#00000F...Wasn't that the name of a little\x01",
            "lives in Entertainment District?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DC")

    label("loc_90DC")


    ChrTalk(
        0x105,
        "#6P#10304FNo, you're wrong.\x02",
    )

    CloseMessageWindow()

    def lambda_9102():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9102)
    Sleep(50)

    def lambda_9112():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9112)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F"Meiling" is the granddaughter of\x01",
            "Mr. Mors, the Merchants Association\x01",
            "President who lives on East Street.\x02\x03",
            "#10304FShe has an older brother\x01",
            "named Roy. They probably\x01",
            "came here together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Oh yeah that's right! I remember\x01",
            "a brother and sister stopping by.\x02",
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
            "#12P#00100FWe've been over\x01",
            "there many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FBut Wazy, why do you know that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, I've collected various\x01",
            "information through my hosting jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI-I see... \x01",
            "Not that I can approve of it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FSettle down, now.\x01",
            "And thanks, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93AB")


    ChrTalk(
        0x8,
        (
            "#11PGreat, then we'll\x01",
            "give you Meiling's\x01",
            "umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    def lambda_93FA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_93FA)
    Sleep(50)

    def lambda_940A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_940A)
    Sleep(50)

    def lambda_941A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_941A)
    Sleep(50)

    def lambda_942A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_942A)
    Sleep(50)

    def lambda_943A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_943A)
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
            "#11PReturn that one\x01",
            "to Meiling and\x01",
            "get Momo's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'm counting on you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sob, sob...*\x01",
            "Please, mister...\x02",
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
            "#12P#00100FWell then, let's go visit \x01",
            "Mr. Mors and see if\x01",
            "we can find her.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_959E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_959E)
    Sleep(50)

    def lambda_95AE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_95AE)
    Sleep(50)

    def lambda_95BE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_95BE)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHis house is at the end of East\x01",
            "Street, if I remember correctly.\x02\x03",
            "Let's head\x01",
            "there for now.\x02",
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
            "Quest [The Vanished Umbrella]\x07\x00",
            " started!\x02",
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

    # Function_26_80F1 end

    def Function_27_96D3(): pass

    label("Function_27_96D3")

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
            "#11POh Lloyd! \x01",
            "How did it go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, we got it back.\x02",
    )

    CloseMessageWindow()

    def lambda_97CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97CB)
    Sleep(10)

    def lambda_97DB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97DB)
    Sleep(10)

    def lambda_97EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97EB)
    Sleep(10)

    def lambda_97FB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97FB)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FHere you\x01",
            "go, Momo.\x02",
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
            "#16IYou returned Momo's Umbrella\x07\x00",
            ".\x02",
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
            "*sniff*... This is...\x01",
            "Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This is the one\x01",
            "father bought me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "T-Thank you! \x01",
            "Thank you so much...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FYep, no problem.\x02\x03",
            "#10100FUh uh, glad we could\x01",
            "get it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yeah...!\x02",
    )

    CloseMessageWindow()

    def lambda_998D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_998D)
    Sleep(50)

    def lambda_999D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_999D)
    Sleep(50)

    def lambda_99AD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_99AD)
    Sleep(50)

    def lambda_99BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_99BD)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10304FCase closed, then.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PThanks for all your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI knew I could\x01",
            "count on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll be sure to call again\x01",
            "if we ever need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FPlease do. We'll be\x01",
            "waiting for your request.\x02",
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
            "Quest [The Vanished Umbrella]\x07\x00",
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

    # Function_27_96D3 end

    def Function_28_9B73(): pass

    label("Function_28_9B73")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D35")

    ChrTalk(
        0x8,
        "Oh, thanks for coming, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bennett made the\x01",
            "new bread this time.\x01",
            "Try some.\x02",
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
            "#00000FThanks Oscar. \x01",
            "I'll savor it later.\x02\x03",
            "We're here for work today, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D9C")

    label("loc_9D35")


    ChrTalk(
        0x8,
        (
            "Oh, thanks for coming, Lloyd.\x01",
            "Want some of our bread?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUmm, I'm here for work today...\x02",
    )

    CloseMessageWindow()

    label("loc_9D9C")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, so that's what\x01",
            "you're talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right. Although I'm pleased\x01",
            "to recommend all our bread...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC2")

    ChrTalk(
        0x8,
        (
            "If I had to pick one, it'd\x01",
            "be the "Bennett's Wonderful"\x01",
            "I just gave you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Jump("loc_9F13")

    label("loc_9EC2")


    ChrTalk(
        0x8,
        (
            "If I had to pick one, it'd be the\x01",
            ""Bennett's Wonderful" I gave you earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F13")


    ChrTalk(
        0x102,
        "#00105FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Even though Bennett came up\x01",
            "with it, it's really very well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want "Morges"' best,\x01",
            "it has to be this one──\x02",
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

    def lambda_9FFB():

        label("loc_9FFB")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9FFB")

    QueueWorkItem2(0x109, 0, lambda_9FFB)

    def lambda_A00D():

        label("loc_A00D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A00D")

    QueueWorkItem2(0x102, 0, lambda_A00D)

    def lambda_A01F():

        label("loc_A01F")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A01F")

    QueueWorkItem2(0x104, 0, lambda_A01F)

    def lambda_A031():

        label("loc_A031")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A031")

    QueueWorkItem2(0x101, 0, lambda_A031)

    def lambda_A043():

        label("loc_A043")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A043")

    QueueWorkItem2(0x105, 0, lambda_A043)

    def lambda_A055():

        label("loc_A055")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A055")

    QueueWorkItem2(0x103, 0, lambda_A055)

    def lambda_A067():

        label("loc_A067")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_A067")

    QueueWorkItem2(0x8, 1, lambda_A067)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A102")
    OP_68(55480, 1510, 1690, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_A0B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_A0B5)
    SetChrPos(0xA, 60080, 10, 4000, 135)
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 57580, 10, 2090, 3000, 0x0)
    OP_64(0xA)
    Jump("loc_A183")

    label("loc_A102")

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

    label("loc_A183")

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
            "Gourmet Guide before \x01",
            "I've surpassed you is...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, don't worry about it. \x01",
            "It's this delicious already, see?\x02",
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
            "go and recommend it anyway, \x01",
            "I won't hear any complaints, ok!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A391")
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 60330, 0, 3200, 3000, 0x0)

    def lambda_A35B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_A35B)
    OP_95(0xA, 60080, 10, 4000, 2000, 0x0)
    SetChrPos(0xA, 119120, 0, -660, 275)
    Jump("loc_A402")

    label("loc_A391")

    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 52110, 1000, 10270, 3000, 0x0)
    OP_95(0xA, 51750, 1000, 10270, 3000, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A3EC")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    Jump("loc_A3FD")

    label("loc_A3EC")

    SetChrPos(0xA, 51280, 1000, 12870, 90)

    label("loc_A3FD")

    ClearChrFlags(0xA, 0x4)

    label("loc_A402")

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
            "Man, she's always like this. And just\x01",
            "because I said it was delicious, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A519():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A519)
    Sleep(50)

    def lambda_A529():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A529)
    Sleep(50)

    def lambda_A539():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A539)
    Sleep(50)

    def lambda_A549():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A549)
    Sleep(50)

    def lambda_A559():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A559)
    Sleep(50)

    def lambda_A569():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A569)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10304FHu hu, that's probably why she's this concerned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHa ha, you're a smart knowin' fellow too, huh?\x02",
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
            "Lloyd and the others ate the Thick Cutlet Sandwich.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10100F*chewing*... \x01",
            "Ahh, the bread is very tender.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and the sauce\x01",
            "is juicy. This is\x01",
            "good, Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha ha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm still working on it\x01",
            "though. It'll be awhile\x01",
            "before it's for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FI see...\x02\x03",
            "#00203FIn that case, maybe we \x01",
            "shouldn't feature it in \x01",
            "one of our articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, when it is finished I'll\x01",
            "give you more on the house,\x01",
            "so please wait until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, we'll be looking forward to it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8EE")
    SetScenarioFlags(0x1, 2)

    label("loc_A8EE")

    SetScenarioFlags(0x172, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A922")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A93F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A952")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A965")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A982")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A995")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A9B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A9C5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A9E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A9F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_AA12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AA12")

    OP_29(0x80, 0x1, 0x6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB3A")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AB31")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_AB31")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_AB3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC1E")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "We have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_AC1E")

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

    # Function_28_9B73 end

    def Function_29_AC52(): pass

    label("Function_29_AC52")

    TalkBegin(0xA)

    ChrTalk(
        0xA,
        (
            "*sigh*... \x01",
            "I can't quite make a new bread\x01",
            "that can surpass Oscar's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, I won't give up. I'll try\x01",
            "as many times as I have to...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She might make a good\x01",
            ""craftman" for the pageant...)\x02\x03",
            "#00000FUmm, excuse me. I've a little\x01",
            "something to ask you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
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
            "I-I'll pass. I don't have\x01",
            "the figure for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm helping cook for\x01",
            "the charity event.\x01",
            "Give me a break here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI-Is that so... We'll have to\x01",
            "look somewhere else, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FLet's ask someone else.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 6)
    SetScenarioFlags(0x1, 3)
    TalkEnd(0xA)
    Return()

    # Function_29_AC52 end

    SaveToFile()

Try(main)
