from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1370.bin",                # FileName
        "t1370",                    # MapName
        "t1370",                    # Location
        0x00B9,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 185, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1370",                  # 0
        "Randy",                  # 1
        "Noｱl",                  # 2
        "Wazy",                   # 3
        "KeA",                    # 4
        "Zeit",                   # 5
        "Cecil",                  # 6
        "Ilya",                   # 7
        "Rixia",                  # 8
        "Sully",                  # 9
        "Miichie",                # 10
        "Melson",                 # 11
        "Corona",                 # 12
        "Rimah",                  # 13
        "M. W. L. Staff",         # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Staffer Hanks",          # 22
        "To Wonderland Entrance", # 23
    ))

    AddCharChip((
        "chr/ch00302.itc",                   # 00
        "chr/ch02902.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch07502.itc",                   # 05
        "chr/ch05102.itc",                   # 06
        "chr/ch05202.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch45400.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch22702.itc",                   # 0B
        "chr/ch20702.itc",                   # 0C
        "chr/ch44600.itc",                   # 0D
        "chr/ch23500.itc",                   # 0E
        "chr/ch23800.itc",                   # 0F
        "chr/ch23900.itc",                   # 10
        "chr/ch33102.itc",                   # 11
        "chr/ch34302.itc",                   # 12
        "chr/ch21602.itc",                   # 13
        "chr/ch21702.itc",                   # 14
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

    DeclNpc(4294964546, 200,     13850,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294964546, 200,     10949,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294963046, 200,     12250,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(769,     0,       8899,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(270,     0,       10720,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294966046, 200,     12250,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294966046, 200,     12250,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294963046, 200,     12250,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294967066, 0,       8899,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18000,   0,       4294966827, 90,   389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294958696, 200,     2400,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294957196, 200,     3900,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294955696, 200,     2400,    90,   389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(17700,   0,       4750,    270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(10250,   0,       7349,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(10750,   0,       6250,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9750,    0,       6250,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294967046, 200,     899,     0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294967046, 200,     3900,    180,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294950196, 200,     2400,    270,  389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294947196, 200,     2400,    90,   389,  0x0, 0,   20,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16700,   0,       4750,    1000,    17700,   1500,    4750,    0x007E, 0,  18, 0x0000)
    DeclActor(4294945296, 500,     9250,    1200,    4294945296, 750,     9250,    0x007C, 0,  3,  0x0000)
    DeclActor(15870,   0,       4294966666, 1200,    18000,   1500,    4294966826, 0x007C, 0,  13, 0x0000)
    DeclActor(8450,    0,       9280,    1200,    8450,    2000,    9280,    0x007C, 0,  34, 0x0000)

    PlaceName(10.0, 0.0, -45.0, 0x0000, 0x0000, "To Wonderland Entrance")
    PlaceName(17.68000030517578, 0.0, 4.739999771118164, 0x0000, 0x0053, "")

    ChipFrameInfo(1208, 0)                                       # 0

    ScpFunction((
        "Function_0_4B8",          # 00, 0
        "Function_1_570",          # 01, 1
        "Function_2_5FC",          # 02, 2
        "Function_3_715",          # 03, 3
        "Function_4_7D4",          # 04, 4
        "Function_5_9C0",          # 05, 5
        "Function_6_B2C",          # 06, 6
        "Function_7_DAD",          # 07, 7
        "Function_8_E58",          # 08, 8
        "Function_9_F60",          # 09, 9
        "Function_10_1225",        # 0A, 10
        "Function_11_141D",        # 0B, 11
        "Function_12_14EA",        # 0C, 12
        "Function_13_15AA",        # 0D, 13
        "Function_14_15AE",        # 0E, 14
        "Function_15_15B2",        # 0F, 15
        "Function_16_164A",        # 10, 16
        "Function_17_16E9",        # 11, 17
        "Function_18_1784",        # 12, 18
        "Function_19_1788",        # 13, 19
        "Function_20_1908",        # 14, 20
        "Function_21_198E",        # 15, 21
        "Function_22_1A0E",        # 16, 22
        "Function_23_1A88",        # 17, 23
        "Function_24_1B6F",        # 18, 24
        "Function_25_1BD7",        # 19, 25
        "Function_26_1CAE",        # 1A, 26
        "Function_27_1D55",        # 1B, 27
        "Function_28_1E15",        # 1C, 28
        "Function_29_2094",        # 1D, 29
        "Function_30_2751",        # 1E, 30
        "Function_31_28AD",        # 1F, 31
        "Function_32_2A82",        # 20, 32
        "Function_33_38D6",        # 21, 33
        "Function_34_3FE4",        # 22, 34
    ))


    def Function_0_4B8(): pass

    label("Function_0_4B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4F8"),
        (1, "loc_504"),
        (2, "loc_510"),
        (3, "loc_51C"),
        (4, "loc_528"),
        (5, "loc_534"),
        (6, "loc_540"),
        (SWITCH_DEFAULT, "loc_54C"),
    )


    label("loc_4F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_504")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_510")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_51C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_528")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_534")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_540")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_56F")

    Return()

    # Function_0_4B8 end

    def Function_1_570(): pass

    label("Function_1_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57E")
    Jump("loc_5EC")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_58C")
    Jump("loc_5EC")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_59A")
    Jump("loc_5EC")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5AB")
    Call(0, 28)
    Jump("loc_5EC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B9")
    Jump("loc_5EC")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C7")
    Jump("loc_5EC")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D5")
    Jump("loc_5EC")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5EC")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5FB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 33)

    label("loc_5FB")

    Return()

    # Function_1_570 end

    def Function_2_5FC(): pass

    label("Function_2_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)

    label("loc_62F")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_6B0")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_64F")
    Jump("loc_6B0")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_65D")
    Jump("loc_6B0")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_66F")
    OP_66(0x0, 0x1)
    Jump("loc_6B0")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_67D")
    Jump("loc_6B0")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6B0")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_699")
    Jump("loc_6B0")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6A7")
    Jump("loc_6B0")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_6B0")

    label("loc_6B0")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
    OP_66(0x2, 0x1)

    label("loc_6D6")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_708")
    OP_24(0x335)
    Jump("loc_70E")

    label("loc_708")

    Sound(821, 1, 50, 0)

    label("loc_70E")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_5FC end

    def Function_3_715(): pass

    label("Function_3_715")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""The Kingdom of Sweets Vol.3" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_7D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Rainbow Cotton Candy"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7D0")

    TalkEnd(0xFF)
    Return()

    # Function_3_715 end

    def Function_4_7D4(): pass

    label("Function_4_7D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ED")
    Jump("loc_9BC")

    label("loc_7ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_803")
    Jump("loc_9BC")

    label("loc_803")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A")

    ChrTalk(
        0x8,
        (
            "#00306FNngh...I came here thinkin'\x01",
            "I'd enjoy havin' a tea or\x01",
            "something with Miss Cecil.\x02\x03",
            "#00309FWell, I guess I'll have to\x01",
            "bear with Noｱl...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#10106FW-What an extreme way to say it, senior...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_990")

    label("loc_90A")


    ChrTalk(
        0x8,
        (
            "#00306FI came here thinkin'\x01",
            "I'd enjoy havin' a tea or\x01",
            "something with Miss Cecil.\x02\x03",
            "#00309FWell, I guess I'll keep\x01",
            "Noｱl company...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    Jump("loc_9BC")

    label("loc_995")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AB")
    Jump("loc_9BC")

    label("loc_9AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BC")

    label("loc_9BC")

    TalkEnd(0xFE)
    Return()

    # Function_4_7D4 end

    def Function_5_9C0(): pass

    label("Function_5_9C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D9")
    Jump("loc_B28")

    label("loc_9D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EF")
    Jump("loc_B28")

    label("loc_9EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(
        0x9,
        (
            "#10100FIt seems that Miss Cecil\x01",
            "went out to have fun.\x02\x03",
            "#10109FUh uh, senior Randy's\x01",
            "timing was bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AFC")

    label("loc_A7B")


    ChrTalk(
        0x9,
        (
            "#10105FBy the way...\x01",
            "Does Zeit intend to be\x01",
            "napping there all day?\x02\x03",
            "#10104FUhhm, maybe I'll buy him\x01",
            "something at a stall...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC")

    Jump("loc_B28")

    label("loc_B01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    Jump("loc_B28")

    label("loc_B17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")

    label("loc_B28")

    TalkEnd(0xFE)
    Return()

    # Function_5_9C0 end

    def Function_6_B2C(): pass

    label("Function_6_B2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B45")
    Jump("loc_DA9")

    label("loc_B45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5B")
    Jump("loc_DA9")

    label("loc_B5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    Jump("loc_DA9")

    label("loc_B71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B87")
    Jump("loc_DA9")

    label("loc_B87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(
        0x101,
        (
            "#00005FWazy, what're you doing?\x02\x03",
            "#00003FDon't tell me you're making\x01",
            "a pass on sister Cecil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10306FHu hu, oh boy.\x01",
            "I'd like you trusted me a little.\x02\x03",
            "#10302FEven young ladies like her\x01",
            "come at the club I work to, but...\x01",
            "Today I'm off, so I won't do anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThat's exactly why\x01",
            "I can't trust you...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_DA9")

    label("loc_D06")


    ChrTalk(
        0xA,
        (
            "#10305FEven young ladies like Miss Cecil happen to\x01",
            "come at the establishment I work at, but...\x02\x03",
            "#10300FHu hu, I won't lay a hand on\x01",
            "your lovely older sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA9")

    TalkEnd(0xFE)
    Return()

    # Function_6_B2C end

    def Function_7_DAD(): pass

    label("Function_7_DAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC6")
    Jump("loc_E54")

    label("loc_DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE9")
    Call(0, 27)
    Jump("loc_E12")

    label("loc_DE9")


    ChrTalk(
        0xB,
        (
            "#01105FEeeh, but isn't\x01",
            "this cuuute?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E12")

    Jump("loc_E54")

    label("loc_E17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2D")
    Jump("loc_E54")

    label("loc_E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E43")
    Jump("loc_E54")

    label("loc_E43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E54")

    label("loc_E54")

    TalkEnd(0xFE)
    Return()

    # Function_7_DAD end

    def Function_8_E58(): pass

    label("Function_8_E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8D")

    ChrTalk(
        0xC,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB0")
    Call(0, 27)
    Jump("loc_EC5")

    label("loc_EB0")


    ChrTalk(
        0xC,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_EC5")

    Jump("loc_F5C")

    label("loc_ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFA")

    ChrTalk(
        0xC,
        "#01200F...Grrrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_EFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2F")

    ChrTalk(
        0xC,
        "#01200F...Grrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5C")

    ChrTalk(
        0xC,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_F5C")

    TalkEnd(0xFE)
    Return()

    # Function_8_E58 end

    def Function_9_F60(): pass

    label("Function_9_F60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1005")

    ChrTalk(
        0xD,
        (
            "#05900FI will try to stay here\x01",
            "as much as possible.\x02\x03",
            "#05909FUh uh, you and the others\x01",
            "should feel free to go to have fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1083")

    label("loc_1005")


    ChrTalk(
        0xD,
        (
            "#05904FI believe I will take it slowly\x01",
            "with Zeit for a while.\x02\x03",
            "#05909FUh uh, however, if you invite me,\x01",
            "I will join you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1083")

    Jump("loc_1221")

    label("loc_1088")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109E")
    Jump("loc_1221")

    label("loc_109E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B4")
    Jump("loc_1221")

    label("loc_10B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CA")
    Jump("loc_1221")

    label("loc_10CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1197")

    ChrTalk(
        0xD,
        (
            "#05900FUh uh, it seems that the\x01",
            "day part is about to end,\x01",
            "so I will wait here for everyone.\x02\x03",
            "#05904FLloyd, when you have finished having fun,\x01",
            "please come back here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1221")

    label("loc_1197")


    ChrTalk(
        0xD,
        (
            "#05900FLloyd, when you have finished having fun,\x01",
            "please come back here.\x02\x03",
            "#05909FUh uh, naturally,\x01",
            "if you invite me,\x01",
            "I will join you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1221")

    TalkEnd(0xFE)
    Return()

    # Function_9_F60 end

    def Function_10_1225(): pass

    label("Function_10_1225")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123E")
    Jump("loc_1419")

    label("loc_123E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1254")
    Jump("loc_1419")

    label("loc_1254")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126A")
    Jump("loc_1419")

    label("loc_126A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(
        0xE,
        (
            "#01700FIs he...Zeit, I guess?\x01",
            "He's always calm...\x01",
            "He looks pretty smart.\x02\x03",
            "#01704FIt seems he was featured in\x01",
            "Crossbell Times before too...\x01",
            "I feel quite the nature of a star in him.\x02\x03",
            "#01709FUh uh, should I scout him\x01",
            "for the Arc-en-ciel, maybe?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1403")

    label("loc_1385")


    ChrTalk(
        0xE,
        (
            "#01704FI feel quite the nature of a star\x01",
            "coming from Zeit.\x02\x03",
            "#01709FUh uh, should I scout him\x01",
            "for the Arc-en-ciel, maybe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1403")

    Jump("loc_1419")

    label("loc_1408")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1419")

    label("loc_1419")

    TalkEnd(0xFE)
    Return()

    # Function_10_1225 end

    def Function_11_141D(): pass

    label("Function_11_141D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1436")
    Jump("loc_14E6")

    label("loc_1436")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144C")
    Jump("loc_14E6")

    label("loc_144C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1462")
    Jump("loc_14E6")

    label("loc_1462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D5")

    ChrTalk(
        0xF,
        (
            "#01803FThat stall's cotton candy\x01",
            "was quite delicious.\x02\x03",
            "#01809FHave you tried eating it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E6")

    label("loc_14D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E6")

    label("loc_14E6")

    TalkEnd(0xFE)
    Return()

    # Function_11_141D end

    def Function_12_14EA(): pass

    label("Function_12_14EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1503")
    Jump("loc_15A6")

    label("loc_1503")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1526")
    Call(0, 27)
    Jump("loc_1564")

    label("loc_1526")


    ChrTalk(
        0x10,
        (
            "#14006FBe it cute or be\x01",
            "it cool, something\x01",
            "bad is bad...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1564")

    Jump("loc_15A6")

    label("loc_1569")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157F")
    Jump("loc_15A6")

    label("loc_157F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1595")
    Jump("loc_15A6")

    label("loc_1595")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")

    label("loc_15A6")

    TalkEnd(0xFE)
    Return()

    # Function_12_14EA end

    def Function_13_15AA(): pass

    label("Function_13_15AA")

    Call(0, 29)
    Return()

    # Function_13_15AA end

    def Function_14_15AE(): pass

    label("Function_14_15AE")

    Call(0, 30)
    Return()

    # Function_14_15AE end

    def Function_15_15B2(): pass

    label("Function_15_15B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(
        0x12,
        "Come on, what should we ride next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1646")

    label("loc_15F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1609")
    Jump("loc_1646")

    label("loc_1609")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161F")
    Jump("loc_1646")

    label("loc_161F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1635")
    Jump("loc_1646")

    label("loc_1635")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1646")

    label("loc_1646")

    TalkEnd(0xFE)
    Return()

    # Function_15_15B2 end

    def Function_16_164A(): pass

    label("Function_16_164A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(
        0x13,
        (
            "Uh uh, fine.\x01",
            "Let's relax on a high place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E5")

    label("loc_1692")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A8")
    Jump("loc_16E5")

    label("loc_16A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BE")
    Jump("loc_16E5")

    label("loc_16BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D4")
    Jump("loc_16E5")

    label("loc_16D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E5")

    label("loc_16E5")

    TalkEnd(0xFE)
    Return()

    # Function_16_164A end

    def Function_17_16E9(): pass

    label("Function_17_16E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(
        0x14,
        "Rimah wants to ride the ferris wheel!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1780")

    label("loc_172D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1743")
    Jump("loc_1780")

    label("loc_1743")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1759")
    Jump("loc_1780")

    label("loc_1759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176F")
    Jump("loc_1780")

    label("loc_176F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1780")

    label("loc_1780")

    TalkEnd(0xFE)
    Return()

    # Function_17_16E9 end

    def Function_18_1784(): pass

    label("Function_18_1784")

    Call(0, 19)
    Return()

    # Function_18_1784 end

    def Function_19_1788(): pass

    label("Function_19_1788")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1795")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1904")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_17E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1805")
    OP_AF(0x6B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18FF")

    label("loc_1805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1819")
    Jump("loc_18FF")

    label("loc_1819")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1831")
    TalkEnd(0x15)
    Return()

    label("loc_1831")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189E")

    ChrTalk(
        0x15,
        "Welcooome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Do you want some delicious cotton candy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FF")

    label("loc_189E")


    ChrTalk(
        0x15,
        (
            "Shouldn't you be feeling\x01",
            "hungry around this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What about some sweeet cotton candy?\x02",
    )

    CloseMessageWindow()

    label("loc_18FF")

    Jump("loc_1795")

    label("loc_1904")

    TalkEnd(0x15)
    Return()

    # Function_19_1788 end

    def Function_20_1908(): pass

    label("Function_20_1908")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1969")

    ChrTalk(
        0x16,
        (
            "Ah, jeez, coming to such a place\x01",
            "and having a fight, just stop it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198A")

    label("loc_1969")


    ChrTalk(
        0x16,
        "Ah, jeez, endure this time!\x02",
    )

    CloseMessageWindow()

    label("loc_198A")

    TalkEnd(0xFE)
    Return()

    # Function_20_1908 end

    def Function_21_198E(): pass

    label("Function_21_198E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D7")

    ChrTalk(
        0x17,
        (
            "Eh eh, isn't it fine?\x01",
            "I only had one bite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_19D7")


    ChrTalk(
        0x17,
        "Getting home already...it's really too early!\x02",
    )

    CloseMessageWindow()

    label("loc_1A0A")

    TalkEnd(0xFE)
    Return()

    # Function_21_198E end

    def Function_22_1A0E(): pass

    label("Function_22_1A0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A51")

    ChrTalk(
        0x18,
        (
            "Aahn, brother ate\x01",
            "my cotton candyyy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_1A51")


    ChrTalk(
        0x18,
        (
            "Aahn, no, no!\x01",
            "I want to see the night parade!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A84")

    TalkEnd(0xFE)
    Return()

    # Function_22_1A0E end

    def Function_23_1A88(): pass

    label("Function_23_1A88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1C")

    ChrTalk(
        0x19,
        (
            "Sorry to have kept you waiting, honey.\x01",
            "I went to buy a juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Let's drink it together\x01",
            "with this love love straw!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6B")

    label("loc_1B1C")


    ChrTalk(
        0x19,
        "The setting sun is beautiful, honey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "However, you're more beautiful.\x02",
    )

    CloseMessageWindow()

    label("loc_1B6B")

    TalkEnd(0xFE)
    Return()

    # Function_23_1A88 end

    def Function_24_1B6F(): pass

    label("Function_24_1B6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAE")

    ChrTalk(
        0x1A,
        (
            "No, stop it.\x01",
            "Go buy two of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_1BAE")


    ChrTalk(
        0x1A,
        (
            "No, stop it.\x01",
            "Let's go back now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD3")

    TalkEnd(0xFE)
    Return()

    # Function_24_1B6F end

    def Function_25_1BD7(): pass

    label("Function_25_1BD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(
        0x1B,
        (
            "Although the health resort was calm and pretty,\x01",
            "Michelam is a strange place too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "It is, by all means, geared towards the young ones.\x01",
            "I wish they'd think about the elderly too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAA")

    label("loc_1CAA")

    TalkEnd(0xFE)
    Return()

    # Function_25_1BD7 end

    def Function_26_1CAE(): pass

    label("Function_26_1CAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D51")

    ChrTalk(
        0x1C,
        (
            "Uh uh, you're saying\x01",
            "those things, but inside,\x01",
            "you quite enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "After all, today you rode the\x01",
            "Horror Coaster four times...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1D51")

    TalkEnd(0xFE)
    Return()

    # Function_26_1CAE end

    def Function_27_1D55(): pass

    label("Function_27_1D55")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xB,
        (
            "#01109FAlright, then, let's\x01",
            "ride the next attraction\x01",
            "with Zeit too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01200F...Woof?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#14006FNo, no...that's impossible.\x01",
            "Think with some common sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_27_1D55 end

    def Function_28_1E15(): pass

    label("Function_28_1E15")

    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x11)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x12)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x13)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x14)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F26")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    Jump("loc_2093")

    label("loc_1F26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F50")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_2093")

    label("loc_1F50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F92")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_2093")

    label("loc_1F92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203E")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_END)), "loc_1FEE")
    SetChrPos(0x11, 14920, 0, -450, 270)

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_END)), "loc_1FFC")
    SetChrFlags(0x11, 0x80)

    label("loc_1FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_202B")
    SetChrFlags(0xE, 0x80)
    Jump("loc_2039")

    label("loc_202B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_2039")
    SetChrFlags(0xF, 0x80)

    label("loc_2039")

    Jump("loc_2093")

    label("loc_203E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2093")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    TurnDirection(0x17, 0x16, 0)
    TurnDirection(0x18, 0x16, 0)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_2093")

    Return()

    # Function_28_1E15 end

    def Function_29_2094(): pass

    label("Function_29_2094")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17030, 400, 460, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 13520, 0, -380, 90)
    OP_65(0x2, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FOh, there's something\x01",
            "pink hidden there...?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x11, 0xFF)
    OP_9C(0x11, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x11, 0x101, 500)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Nice to meet you, mister㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I'm "Miichie", you know?♪\x01",
            "Mishishi, it's a pleasure!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FAh, could you be\x01",
            "Michey's little sister?\x02\x03",
            "#00004FTio said that if you're lucky\x01",
            "you can meet you...\x01",
            "Ha ha, I was lucky then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Ah, so you knew about me!\x01",
            "Mishishi, I'm happy☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005FBy the way...\x01",
            "Why are you hiding\x01",
            "in such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you know, I really\x01",
            "love hide and seek.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I always hide somewhere in\x01",
            "Wonderland, waiting to be found\x01",
            "by a prince on a white horse㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(But if he isn't lucky,\x01",
            "he won't find you...)\x02\x03",
            "#00012FHa ha, so it means that this time,\x01",
            "I'm your prince on a white horse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, right.\x01",
            "I'm really happy\x01",
            "you found me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You're a hundred times cooler than that\x01",
            "brother of mine with the dejected face...\x01",
            "You perfectly fit the prince's requirements☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(M-Miichie speaks in\x01",
            "a slightly cruel way...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Being that the case...\x01",
            "Mister, won't you play\x01",
            "hide and seek with me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "It's a special game that\x01",
            "only the prince who finds\x01",
            "me can participate to.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Together with one of your friends,\x01",
            "you'll have to find me five times\x01",
            "while I hide in Wonderland.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There's a wonderful prize too☆\x01",
            "So, do you want to do it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_29_2094 end

    def Function_30_2751(): pass

    label("Function_30_2751")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x11, 0xFF)
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Ah, mister!\x01",
            "Will you play hide and seek with me, then?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Together with one of your friends,\x01",
            "you'll have to find me five times\x01",
            "while I hide in Wonderland.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There's a wonderful prize too☆\x01",
            "So, do you want to do it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_30_2751 end

    def Function_31_28AD(): pass

    label("Function_31_28AD")


    ChrTalk(
        0x101,
        (
            "#00003F(It seems that once I begin,\x01",
            "I won't have any time to enjoy the \x01",
            "other attractions until it's over...)\x02",
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
            "[Accept]\x01",      # 0
            "[Quit]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2981")
    Call(0, 32)
    Jump("loc_2A4A")

    label("loc_2981")


    ChrTalk(
        0x101,
        (
            "#00000FEhhm, sorry.\x01",
            "I'm currently touring\x01",
            "the attractions, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eeh, is that so?\x01",
            "*dejected*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "But, if you want to do it,\x01",
            "you can aways tell me, ok?\x01",
            "I'll be waiting here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 6)

    label("loc_2A4A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x11, 14920, 0, -450, 270)
    OP_4C(0x11, 0xFF)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_28AD end

    def Function_32_2A82(): pass

    label("Function_32_2A82")


    ChrTalk(
        0x101,
        (
            "#00000FThen...\x01",
            "I guess I'll give it a try.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, that's the spirit☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Then, I'll go hide at once.\x01",
            "Mister, go look for a partner.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "When you want to give up,\x01",
            "you can tell big brother\x01",
            "Michey at the plaza.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, see you then!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(12510, 0, 1310, 3000)

    def lambda_2BBB():

        label("loc_2BBB")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_2BBB")

    QueueWorkItem2(0x101, 1, lambda_2BBB)
    SetChrFlags(0x11, 0x1000)
    OP_95(0x11, 13790, 0, 1620, 5000, 0x0)
    OP_95(0x11, 2640, 0, 1210, 5000, 0x0)
    EndChrThread(0x101, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FA-At any rate...\x01",
            "It seems I need a partner with\x01",
            "whom to look for Miichie.\x02\x03",
            "#00000FWho should I invite...?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Elie]\x01",       # 0
            "[Tio]\x01",        # 1
            "[Randy]\x01",      # 2
            "[Noｱl]\x01",      # 3
            "[Wazy]\x01",       # 4
            "[KeA]\x01",        # 5
            "[Fran]\x01",       # 6
            "[Cecil]\x01",      # 7
            "[Ilya]\x01",       # 8
            "[Rixia]\x01",      # 9
            "[Sully]\x01",      # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D5F"),
        (1, "loc_2DA7"),
        (2, "loc_2DEE"),
        (3, "loc_2E37"),
        (4, "loc_2E7F"),
        (5, "loc_2EC7"),
        (6, "loc_2F0E"),
        (7, "loc_2F56"),
        (8, "loc_2FA6"),
        (9, "loc_2FF3"),
        (10, "loc_303C"),
        (SWITCH_DEFAULT, "loc_3085"),
    )


    label("loc_2D5F")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C7, 7)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Elie.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x0)
    Jump("loc_3085")

    label("loc_2DA7")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 0)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Tio.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x1)
    Jump("loc_3085")

    label("loc_2DEE")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 1)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Randy.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x2)
    Jump("loc_3085")

    label("loc_2E37")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 2)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Noｱl.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x3)
    Jump("loc_3085")

    label("loc_2E7F")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 3)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Wazy.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x4)
    Jump("loc_3085")

    label("loc_2EC7")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 4)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite KeA.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x5)
    Jump("loc_3085")

    label("loc_2F0E")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 5)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Fran.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x6)
    Jump("loc_3085")

    label("loc_2F56")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 6)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite sister Cecil.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x7)
    Jump("loc_3085")

    label("loc_2FA6")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 7)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Miss Ilya.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x8)
    Jump("loc_3085")

    label("loc_2FF3")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 0)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Rixia.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x9)
    Jump("loc_3085")

    label("loc_303C")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 1)

    ChrTalk(
        0x101,
        "#00000F(Alright...I'll try to invite Sully.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0xA)
    Jump("loc_3085")

    label("loc_3085")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_30A2")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_30B4")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_30C6")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_30D8")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_30EA")
    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_30FC")
    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_30FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_310E")
    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_310E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3120")
    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3152")

    label("loc_3120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3137")
    AddParty(0x33, 0xEF, 0xFF)
    SetChrFlags(0xE, 0x80)
    Jump("loc_3152")

    label("loc_3137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_314E")
    AddParty(0x34, 0xEF, 0xFF)
    SetChrFlags(0xF, 0x80)
    Jump("loc_3152")

    label("loc_314E")

    AddParty(0x65, 0xEF, 0xFF)

    label("loc_3152")

    OP_68(14480, 0, 520, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0xEF, 13000, 0, 200, 180)
    SetChrPos(0x101, 13000, 0, -1690, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3234")

    ChrTalk(
        0x102,
        (
            "#00100FYes, I understand the situation.\x02\x03",
            "#00109F*giggle*, it seems quite fun,\x01",
            "so let's do our best and look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_3234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_32D1")

    ChrTalk(
        0x103,
        (
            "#00200FI see...\x01",
            "I understand the situation.\x02\x03",
            "#00204FHide and seek with that Miichie...\x01",
            "We must do our very best\x01",
            "and deal with the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_333C")

    ChrTalk(
        0x104,
        (
            "#00300FI see, got it.\x02\x03",
            "#00304FWell, I guess I'll play a little\x01",
            "as an attraction filler.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_333C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_33C2")

    ChrTalk(
        0x109,
        (
            "#10105F*haah*, such a thing has...\x02\x03",
            "#10109FBut it sounds fun. Since we're doing it,\x01",
            "let's look for her in earnest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_33C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_345B")

    ChrTalk(
        0x105,
        (
            "#10300FHm, I understand.\x01",
            "Seems it's quite fun.\x02\x03",
            "#10309FHu hu, since it's a rare opportunity,\x01",
            "let's do our very best and look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_34C5")

    ChrTalk(
        0x153,
        (
            "#01100FHide and seek? Sounds fun!!\x02\x03",
            "#01109FLloyd, let's do our best and look for her!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_34C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_3547")

    ChrTalk(
        0x156,
        (
            "#06405FEeh, hide and seek\x01",
            "with that Miichie?\x02\x03",
            "#06409FUh uh, Mr. Lloyd!\x01",
            "Being this the case, let's do our best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_3547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0x14C,
        (
            "#05905FMy, something like that happened?\x02\x03",
            "#05909FUh uh, then, let's look\x01",
            "for that Miichie, hm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_35B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3675")

    ChrTalk(
        0x134,
        (
            "#01700FHm, hm, I understand.\x01",
            "Somehow it seems fun.\x02\x03",
            "#01709FAlthough it's just hide and seek,\x01",
            "it seems we must do this seriously, eh?\x01",
            "Let's do our best, younger brother!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_3675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_370C")

    ChrTalk(
        0x135,
        (
            "#01802FI see... I understand the circumstances.\x02\x03",
            "#01809FUh uh, hide and seek is also my forte,\x01",
            "so please allow me to come with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3798")

    label("loc_370C")


    ChrTalk(
        0x166,
        (
            "#14000FHmm, hide and seek, eh?\x01",
            "What a weird story though.\x02\x03",
            "#14004FWell, I'm free so I'll tag along.\x01",
            "...Hey, let's go look for her now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3800")

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thank you.\x02\x03",
            "#00000FThen, let's look for her\x01",
            "inside the theme park now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3857")

    label("loc_3800")


    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks.\x02\x03",
            "#00000FThen, let's look for her\x01",
            "inside the theme park now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3857")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Miichie's Challenge]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C9, 2)
    OP_29(0x7F, 0x4, 0x2)
    SetChrFlags(0x11, 0x80)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_2A82 end

    def Function_33_38D6(): pass

    label("Function_33_38D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrFlags(0x1D, 0x8000)
    OP_68(12380, 0, 8690, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 10510, 0, 7810, 90)
    SetChrPos(0x103, 11970, 0, 7490, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F*phew*, we got through that somehow...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F...Good job.\x02\x03",
            "#05526FDancing in a mascot character\x01",
            "costume was quite tough...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FYou're right...\x01",
            "It was crazily hot.\x02\x03",
            "#05209FThe real actor does\x01",
            "this every day...\x01",
            "He's really something.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FUh uh...right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 6440, 0, 1530, 45)

    NpcTalk(
        0x1D,
        "Man's Voice",
        (
            "Heeey!\x01",
            "Michey, Miichie!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(11850, 0, 8160, 3000)
    SetCameraDistance(20690, 3000)

    def lambda_3B45():

        label("loc_3B45")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3B45")

    QueueWorkItem2(0x101, 1, lambda_3B45)

    def lambda_3B57():

        label("loc_3B57")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3B57")

    QueueWorkItem2(0x103, 1, lambda_3B57)
    OP_95(0x1D, 10760, 0, 5250, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FAh...\x01",
            "Thank you for your hard work.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yeah, thank you for yours too.\x01",
            "You did really well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hey, listen to this.\x01",
            "It seems that "Miichie" is becoming\x01",
            "quite the topic of the day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FThe...topic?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yeah, they say that her cool behavior\x01",
            "that she displays sometimes when\x01",
            "accompanying Michey is irresistible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hmmm, maybe we should rethink\x01",
            ""Miichie"'s character...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FI-Is that so...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F......*cough*......\x01",
            "Well, I am happy if I could be of help...\x02\x03",
            "#05520FBy the way...\x01",
            "Is the real actor still...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...Ah, right, I was forgetting!\x01",
            "He arrived just moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It seems he'll meet you later\x01",
            "so he went ahead to the locker\x01",
            "room and said he'll wait there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Thank you, really.\x01",
            "Please accept this as pay for\x01",
            "the side job, if you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x1D, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x34D, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202FThank you very much.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FThen, Tio...\x01",
            "Should we end it here?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, you are right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 4000, 50)
    StopSound(126, 4000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_38D6 end

    def Function_34_3FE4(): pass

    label("Function_34_3FE4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sketch map\x01",
            "of the theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_34_3FE4 end

    SaveToFile()

Try(main)
