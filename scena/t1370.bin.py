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
        "MWL Staff",              # 14
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
        "Function_4_7D2",          # 04, 4
        "Function_5_9B7",          # 05, 5
        "Function_6_B0B",          # 06, 6
        "Function_7_D6B",          # 07, 7
        "Function_8_E1C",          # 08, 8
        "Function_9_F25",          # 09, 9
        "Function_10_11D2",        # 0A, 10
        "Function_11_13A1",        # 0B, 11
        "Function_12_1461",        # 0C, 12
        "Function_13_1519",        # 0D, 13
        "Function_14_151D",        # 0E, 14
        "Function_15_1521",        # 0F, 15
        "Function_16_15B7",        # 10, 16
        "Function_17_164D",        # 11, 17
        "Function_18_16E8",        # 12, 18
        "Function_19_16EC",        # 13, 19
        "Function_20_1861",        # 14, 20
        "Function_21_18F1",        # 15, 21
        "Function_22_196E",        # 16, 22
        "Function_23_19E8",        # 17, 23
        "Function_24_1ACA",        # 18, 24
        "Function_25_1B71",        # 19, 25
        "Function_26_1C3F",        # 1A, 26
        "Function_27_1CD8",        # 1B, 27
        "Function_28_1D92",        # 1C, 28
        "Function_29_2011",        # 1D, 29
        "Function_30_2685",        # 1E, 30
        "Function_31_27D3",        # 1F, 31
        "Function_32_29B7",        # 20, 32
        "Function_33_37A8",        # 21, 33
        "Function_34_3EA3",        # 22, 34
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
            ""The Kingdom of Sweets\x01",
            "Vol.3" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_7CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Rainbow\x01",
            "Cotton Candy"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7CE")

    TalkEnd(0xFF)
    Return()

    # Function_3_715 end

    def Function_4_7D2(): pass

    label("Function_4_7D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EB")
    Jump("loc_9B3")

    label("loc_7EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    Jump("loc_9B3")

    label("loc_801")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906")

    ChrTalk(
        0x8,
        (
            "#00306FNngh... I came here thinkin'\x01",
            "I'd enjoy havin' a tea or\x01",
            "somethin' with Cecil.\x02\x03",
            "#00309FWell, I guess I'll have to\x01",
            "make do with Noｱl...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#10106FW-What an extreme way to\x01",
            "say it, Randy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_987")

    label("loc_906")


    ChrTalk(
        0x8,
        (
            "#00306FI came here thinkin' I'd\x01",
            "enjoy havin' a tea or\x01",
            "something with Cecil.\x02\x03",
            "#00309FWell, I guess I'll keep\x01",
            "Noｱl company...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_987")

    Jump("loc_9B3")

    label("loc_98C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_9B3")

    label("loc_9A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B3")

    label("loc_9B3")

    TalkEnd(0xFE)
    Return()

    # Function_4_7D2 end

    def Function_5_9B7(): pass

    label("Function_5_9B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D0")
    Jump("loc_B07")

    label("loc_9D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E6")
    Jump("loc_B07")

    label("loc_9E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(
        0x9,
        (
            "#10100FCecil went out to have\x01",
            "fun.\x02\x03",
            "#10109FHaha, Randy's has such\x01",
            "awful timing, huh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ADB")

    label("loc_A63")


    ChrTalk(
        0x9,
        (
            "#10105FBy the way... Does Zeit\x01",
            "intend nap there all\x01",
            "day?\x02\x03",
            "#10104FHmm, maybe I'll buy him\x01",
            "something at the\x01",
            "stand...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADB")

    Jump("loc_B07")

    label("loc_AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF6")
    Jump("loc_B07")

    label("loc_AF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")

    label("loc_B07")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B7 end

    def Function_6_B0B(): pass

    label("Function_6_B0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B24")
    Jump("loc_D67")

    label("loc_B24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    Jump("loc_D67")

    label("loc_B3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B50")
    Jump("loc_D67")

    label("loc_B50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B66")
    Jump("loc_D67")

    label("loc_B66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(
        0x101,
        (
            "#00005FWazy, what are you\x01",
            "doing?\x02\x03",
            "#00003FDon't tell me you're\x01",
            "making a pass on my\x01",
            "sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10306FHehe, oh man. How about a little\x01",
            "trust?.\x02\x03",
            "#10302FYoung ladies like her come to the\x01",
            "club I work at, but... I'm off\x01",
            "today, so I won't do anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThat's exactly why I\x01",
            "can't trust you...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D67")

    label("loc_CD6")


    ChrTalk(
        0xA,
        (
            "#10305FYoung ladies like Cecil\x01",
            "come to the establishment\x01",
            "where I work, but...\x02\x03",
            "#10300FHehe, I won't lay a hand\x01",
            "on your lovely older\x01",
            "sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D67")

    TalkEnd(0xFE)
    Return()

    # Function_6_B0B end

    def Function_7_D6B(): pass

    label("Function_7_D6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D84")
    Jump("loc_E18")

    label("loc_D84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA7")
    Call(0, 27)
    Jump("loc_DD6")

    label("loc_DA7")


    ChrTalk(
        0xB,
        (
            "#01105FEeeh, but isn't he just\x01",
            "so cuuute?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD6")

    Jump("loc_E18")

    label("loc_DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF1")
    Jump("loc_E18")

    label("loc_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")
    Jump("loc_E18")

    label("loc_E07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E18")

    label("loc_E18")

    TalkEnd(0xFE)
    Return()

    # Function_7_D6B end

    def Function_8_E1C(): pass

    label("Function_8_E1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E52")

    ChrTalk(
        0xC,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F21")

    label("loc_E52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E75")
    Call(0, 27)
    Jump("loc_E8A")

    label("loc_E75")


    ChrTalk(
        0xC,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_E8A")

    Jump("loc_F21")

    label("loc_E8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBE")

    ChrTalk(
        0xC,
        "#01200F...Grrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F21")

    label("loc_EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF3")

    ChrTalk(
        0xC,
        "#01200F...Grrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F21")

    label("loc_EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F21")

    ChrTalk(
        0xC,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_F21")

    TalkEnd(0xFE)
    Return()

    # Function_8_E1C end

    def Function_9_F25(): pass

    label("Function_9_F25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC4")

    ChrTalk(
        0xD,
        (
            "#05900FI'll try to stay here as\x01",
            "much as I can.\x02\x03",
            "#05909FHaha. You and the others\x01",
            "should feel free to go\x01",
            "to have fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_104A")

    label("loc_FC4")


    ChrTalk(
        0xD,
        (
            "#05904FI think I'll take it\x01",
            "easy here with Zeit for\x01",
            "a while.\x02\x03",
            "#05909FHaha. However, if you\x01",
            "invite me, I will of\x01",
            "course join you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_11CE")

    label("loc_104F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1065")
    Jump("loc_11CE")

    label("loc_1065")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107B")
    Jump("loc_11CE")

    label("loc_107B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1091")
    Jump("loc_11CE")

    label("loc_1091")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114B")

    ChrTalk(
        0xD,
        (
            "#05900FHaha. It seems the day\x01",
            "is almost over, so I'll\x01",
            "wait here for everyone.\x02\x03",
            "#05904FLloyd, when you're\x01",
            "finished having fun,\x01",
            "please return here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_11CE")

    label("loc_114B")


    ChrTalk(
        0xD,
        (
            "#05900FLloyd, when you're\x01",
            "finished having fun,\x01",
            "please return here.\x02\x03",
            "#05909FHaha. If you invite me,\x01",
            "I will of course join\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CE")

    TalkEnd(0xFE)
    Return()

    # Function_9_F25 end

    def Function_10_11D2(): pass

    label("Function_10_11D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    Jump("loc_139D")

    label("loc_11EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1201")
    Jump("loc_139D")

    label("loc_1201")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    Jump("loc_139D")

    label("loc_1217")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1318")

    ChrTalk(
        0xE,
        (
            "#01700FIs he Zeit? He's always calm...\x01",
            "He looks pretty smart.\x02\x03",
            "#01704FHe was featured in Crossbell\x01",
            "Times before too... I feel like\x01",
            "he's quite the budding star.\x02\x03",
            "#01709FHehe. Should I scout him for\x01",
            "Arc-en-Ciel, maybe?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1387")

    label("loc_1318")


    ChrTalk(
        0xE,
        (
            "#01704FI feel Zeit has quite\x01",
            "the star potential.\x02\x03",
            "#01709FHehe. Should I scout him\x01",
            "for Arc-en-Ciel, maybe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1387")

    Jump("loc_139D")

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139D")

    label("loc_139D")

    TalkEnd(0xFE)
    Return()

    # Function_10_11D2 end

    def Function_11_13A1(): pass

    label("Function_11_13A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BA")
    Jump("loc_145D")

    label("loc_13BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D0")
    Jump("loc_145D")

    label("loc_13D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E6")
    Jump("loc_145D")

    label("loc_13E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144C")

    ChrTalk(
        0xF,
        (
            "#01803FThat stand's cotton\x01",
            "candy was delicious.\x02\x03",
            "#01809FHave you tried it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145D")

    label("loc_144C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145D")

    label("loc_145D")

    TalkEnd(0xFE)
    Return()

    # Function_11_13A1 end

    def Function_12_1461(): pass

    label("Function_12_1461")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147A")
    Jump("loc_1515")

    label("loc_147A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149D")
    Call(0, 27)
    Jump("loc_14D3")

    label("loc_149D")


    ChrTalk(
        0x10,
        (
            "#14006FBe it cute or cool, bad\x01",
            "things are bad...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D3")

    Jump("loc_1515")

    label("loc_14D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EE")
    Jump("loc_1515")

    label("loc_14EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1504")
    Jump("loc_1515")

    label("loc_1504")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")

    label("loc_1515")

    TalkEnd(0xFE)
    Return()

    # Function_12_1461 end

    def Function_13_1519(): pass

    label("Function_13_1519")

    Call(0, 29)
    Return()

    # Function_13_1519 end

    def Function_14_151D(): pass

    label("Function_14_151D")

    Call(0, 30)
    Return()

    # Function_14_151D end

    def Function_15_1521(): pass

    label("Function_15_1521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(
        0x12,
        (
            "C'mon, what should we\x01",
            "ride next?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B3")

    label("loc_1560")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1576")
    Jump("loc_15B3")

    label("loc_1576")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158C")
    Jump("loc_15B3")

    label("loc_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A2")
    Jump("loc_15B3")

    label("loc_15A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")

    label("loc_15B3")

    TalkEnd(0xFE)
    Return()

    # Function_15_1521 end

    def Function_16_15B7(): pass

    label("Function_16_15B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(
        0x13,
        (
            "Haha, fine. Let's relax\x01",
            "up high.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1649")

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160C")
    Jump("loc_1649")

    label("loc_160C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1622")
    Jump("loc_1649")

    label("loc_1622")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1638")
    Jump("loc_1649")

    label("loc_1638")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1649")

    label("loc_1649")

    TalkEnd(0xFE)
    Return()

    # Function_16_15B7 end

    def Function_17_164D(): pass

    label("Function_17_164D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1691")

    ChrTalk(
        0x14,
        (
            "Rimah wants to ride the\x01",
            "Ferris wheel!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E4")

    label("loc_1691")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A7")
    Jump("loc_16E4")

    label("loc_16A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BD")
    Jump("loc_16E4")

    label("loc_16BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D3")
    Jump("loc_16E4")

    label("loc_16D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E4")

    label("loc_16E4")

    TalkEnd(0xFE)
    Return()

    # Function_17_164D end

    def Function_18_16E8(): pass

    label("Function_18_16E8")

    Call(0, 19)
    Return()

    # Function_18_16E8 end

    def Function_19_16EC(): pass

    label("Function_19_16EC")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_174B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")
    OP_AF(0x6B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1858")

    label("loc_176B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177F")
    Jump("loc_1858")

    label("loc_177F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1797")
    TalkEnd(0x15)
    Return()

    label("loc_1797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1858")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(
        0x15,
        "Welcooome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Do you want some\x01",
            "delicious cotton candy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1858")

    label("loc_1804")


    ChrTalk(
        0x15,
        (
            "Aren't you feeling\x01",
            "hungry around now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "How about some sweeet\x01",
            "cotton candy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1858")

    Jump("loc_16F9")

    label("loc_185D")

    TalkEnd(0x15)
    Return()

    # Function_19_16EC end

    def Function_20_1861(): pass

    label("Function_20_1861")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C1")

    ChrTalk(
        0x16,
        (
            "Ah, jeez, coming to a\x01",
            "place like this and\x01",
            "fighting, just stop it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18ED")

    label("loc_18C1")


    ChrTalk(
        0x16,
        (
            "Ah, jeez! Deal with it\x01",
            "just this once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18ED")

    TalkEnd(0xFE)
    Return()

    # Function_20_1861 end

    def Function_21_18F1(): pass

    label("Function_21_18F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_193B")

    ChrTalk(
        0x17,
        (
            "Hehe, but isn't it fine?\x01",
            "I only had a bite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196A")

    label("loc_193B")


    ChrTalk(
        0x17,
        (
            "Going home already...\x01",
            "It's way too early!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196A")

    TalkEnd(0xFE)
    Return()

    # Function_21_18F1 end

    def Function_22_196E(): pass

    label("Function_22_196E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(
        0x18,
        (
            "Aahn, brother ate my\x01",
            "cotton candyyy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E4")

    label("loc_19B1")


    ChrTalk(
        0x18,
        (
            "Aahn, no, no! I want to\x01",
            "see the night parade!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E4")

    TalkEnd(0xFE)
    Return()

    # Function_22_196E end

    def Function_23_19E8(): pass

    label("Function_23_19E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A77")

    ChrTalk(
        0x19,
        (
            "Sorry to keep you\x01",
            "waiting, honey. I went\x01",
            "to buy a juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Let's drink it together\x01",
            "with this love-love\x01",
            "straw!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1A77")


    ChrTalk(
        0x19,
        (
            "The setting sun is\x01",
            "beautiful, honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "However, you're more\x01",
            "beautiful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC6")

    TalkEnd(0xFE)
    Return()

    # Function_23_19E8 end

    def Function_24_1ACA(): pass

    label("Function_24_1ACA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B22")

    ChrTalk(
        0x1A,
        (
            "Well, stuff like that is\x01",
            "okay, so please buy two\x01",
            "of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6D")

    label("loc_1B22")


    ChrTalk(
        0x1A,
        (
            "Well, stuff like that is\x01",
            "okay, but it's time for\x01",
            "us to be going home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6D")

    TalkEnd(0xFE)
    Return()

    # Function_24_1ACA end

    def Function_25_1B71(): pass

    label("Function_25_1B71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3B")

    ChrTalk(
        0x1B,
        (
            "Although the health resort was\x01",
            "quiet and pretty, Michelam is\x01",
            "a strange place too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "It's totally geared towards\x01",
            "young people. I wish they'd\x01",
            "think about the elderly too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C3B")

    label("loc_1C3B")

    TalkEnd(0xFE)
    Return()

    # Function_25_1B71 end

    def Function_26_1C3F(): pass

    label("Function_26_1C3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD4")

    ChrTalk(
        0x1C,
        (
            "Haha. You say that, but\x01",
            "inside, you really\x01",
            "enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "After all, you rode the\x01",
            "horror coaster four\x01",
            "times today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD4")

    label("loc_1CD4")

    TalkEnd(0xFE)
    Return()

    # Function_26_1C3F end

    def Function_27_1CD8(): pass

    label("Function_27_1CD8")

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
            "#14006FNo, no... that's\x01",
            "impossible. Use some\x01",
            "common sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_27_1CD8 end

    def Function_28_1D92(): pass

    label("Function_28_1D92")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA3")
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
    Jump("loc_2010")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECD")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_2010")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0F")
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
    Jump("loc_2010")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FBB")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_END)), "loc_1F6B")
    SetChrPos(0x11, 14920, 0, -450, 270)

    label("loc_1F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_END)), "loc_1F79")
    SetChrFlags(0x11, 0x80)

    label("loc_1F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_1FA8")
    SetChrFlags(0xE, 0x80)
    Jump("loc_1FB6")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_1FB6")
    SetChrFlags(0xF, 0x80)

    label("loc_1FB6")

    Jump("loc_2010")

    label("loc_1FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2010")
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

    label("loc_2010")

    Return()

    # Function_28_1D92 end

    def Function_29_2011(): pass

    label("Function_29_2011")

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
            "#00005FHuh, there's something\x01",
            "pink hiding...?\x02",
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
            "Nice to meet you,\x01",
            "mister㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I'm "Mishette", you\x01",
            "know?♪ Mishishi, it's a\x01",
            "pleasure!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FAh, could you be Mishy's\x01",
            "little sister?\x02\x03",
            "#00004FTio said I'd meet you if\x01",
            "I was lucky... Haha,\x01",
            "guess I was lucky, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Ah, so you knew about\x01",
            "me! Mishishi, I'm so\x01",
            "happy~☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005FBy the way... Why are\x01",
            "you hiding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, I just looove\x01",
            "hide and seek, you\x01",
            "know~.\x07\x00\x02",
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
            "#00012FHaha. Then this time,\x01",
            "I'm your prince on a\x01",
            "white horse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, that's right~.\x01",
            "I'm really happy you\x01",
            "found me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You're a hundred times cooler than my\x01",
            "brother with that stupid face of his... You\x01",
            "fit the prince's requirements perfectly☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(T-That's a pretty harsh\x01",
            "way to put it, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "A-And so... Won't you\x01",
            "play hide and seek with\x01",
            "me, mister?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "It's a special game only\x01",
            "princes who find me can\x01",
            "play~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You'll have to find me hiding\x01",
            "in Wonderland five times with\x01",
            "one of your friends!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There's a wonderful\x01",
            "prize too☆. So, want to\x01",
            "give it a try?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_29_2011 end

    def Function_30_2685(): pass

    label("Function_30_2685")

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
            "Ah, mister! Will you\x01",
            "play hide and seek with\x01",
            "me, then?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You'll have to find me hiding\x01",
            "in Wonderland five times with\x01",
            "one of your friends!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There's a wonderful\x01",
            "prize too☆. So, want to\x01",
            "give it a try?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_30_2685 end

    def Function_31_27D3(): pass

    label("Function_31_27D3")


    ChrTalk(
        0x101,
        (
            "#00003F(Once I begin, it looks like I\x01",
            "won't have time to enjoy the other\x01",
            "attractions until it's over...)\x02",
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
            "[Accept Mishette's Challenge]\x01",      # 0
            "[Cancel]\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B9")
    Call(0, 32)
    Jump("loc_297F")

    label("loc_28B9")


    ChrTalk(
        0x101,
        (
            "#00000FUmm, sorry. I'm currently\x01",
            "in the middle of seeing\x01",
            "attractions, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Aww, really～?\x01",
            "*dejected*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "But, tell me if you\x01",
            "change your mind, ok?\x01",
            "I'll be waiting here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 6)

    label("loc_297F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x11, 14920, 0, -450, 270)
    OP_4C(0x11, 0xFF)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_27D3 end

    def Function_32_29B7(): pass

    label("Function_32_29B7")


    ChrTalk(
        0x101,
        (
            "#00000FThen... I guess I'll\x01",
            "give it a try.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, now that's the\x01",
            "spirit☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Then, I'll go hide at\x01",
            "once. Go look for a\x01",
            "partner, ok mister?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "When you want to give up,\x01",
            "you can tell my big brother\x01",
            "Mishy at the plaza.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, see you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(12510, 0, 1310, 3000)

    def lambda_2AF3():

        label("loc_2AF3")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_2AF3")

    QueueWorkItem2(0x101, 1, lambda_2AF3)
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
            "#00003FA-Anyway... Looks like I\x01",
            "need a partner to look\x01",
            "for Mishette with.\x02\x03",
            "#00000FWho should I invite?\x02",
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
        (0, "loc_2C8D"),
        (1, "loc_2CCF"),
        (2, "loc_2D10"),
        (3, "loc_2D53"),
        (4, "loc_2D95"),
        (5, "loc_2DD7"),
        (6, "loc_2E18"),
        (7, "loc_2E5A"),
        (8, "loc_2E9D"),
        (9, "loc_2EDF"),
        (10, "loc_2F22"),
        (SWITCH_DEFAULT, "loc_2F65"),
    )


    label("loc_2C8D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C7, 7)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Elie.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x0)
    Jump("loc_2F65")

    label("loc_2CCF")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 0)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Tio.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x1)
    Jump("loc_2F65")

    label("loc_2D10")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 1)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x2)
    Jump("loc_2F65")

    label("loc_2D53")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 2)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Noｱl.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x3)
    Jump("loc_2F65")

    label("loc_2D95")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x4)
    Jump("loc_2F65")

    label("loc_2DD7")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 4)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "KeA.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x5)
    Jump("loc_2F65")

    label("loc_2E18")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 5)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Fran.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x6)
    Jump("loc_2F65")

    label("loc_2E5A")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 6)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x7)
    Jump("loc_2F65")

    label("loc_2E9D")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 7)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x8)
    Jump("loc_2F65")

    label("loc_2EDF")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 0)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Rixia.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x9)
    Jump("loc_2F65")

    label("loc_2F22")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 1)

    ChrTalk(
        0x101,
        (
            "#00000F(Alright... I'll invite\x01",
            "Sully.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0xA)
    Jump("loc_2F65")

    label("loc_2F65")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_2F82")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_2F94")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_2FA6")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2FB8")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_2FCA")
    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2FDC")
    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_2FEE")
    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_2FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3000")
    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3032")

    label("loc_3000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3017")
    AddParty(0x33, 0xEF, 0xFF)
    SetChrFlags(0xE, 0x80)
    Jump("loc_3032")

    label("loc_3017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_302E")
    AddParty(0x34, 0xEF, 0xFF)
    SetChrFlags(0xF, 0x80)
    Jump("loc_3032")

    label("loc_302E")

    AddParty(0x65, 0xEF, 0xFF)

    label("loc_3032")

    OP_68(14480, 0, 520, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0xEF, 13000, 0, 200, 180)
    SetChrPos(0x101, 13000, 0, -1690, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3114")

    ChrTalk(
        0x102,
        (
            "#00100FYes, I understand the\x01",
            "situation.\x02\x03",
            "#00109F*giggle*, it seems quite\x01",
            "fun, so let's do our\x01",
            "best and look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_31B0")

    ChrTalk(
        0x103,
        (
            "#00200FI see... I understand the\x01",
            "situation.\x02\x03",
            "#00204FHide and seek with that\x01",
            "Mishette... We must get fired\x01",
            "up and deal with this head-on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_3218")

    ChrTalk(
        0x104,
        (
            "#00300FI see, got it.\x02\x03",
            "#00304FWell, it could be fun as\x01",
            "a filler between\x01",
            "attractions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_3299")

    ChrTalk(
        0x109,
        (
            "#10105F*sigh*, something like\x01",
            "that, huh...\x02\x03",
            "#10109FBut it sounds fun. Since\x01",
            "we're doing it, let's go\x01",
            "all out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_3320")

    ChrTalk(
        0x105,
        (
            "#10300FHm, I see. Seems it'll\x01",
            "be quite fun.\x02\x03",
            "#10309FHehe. It's a rare\x01",
            "opportunity, so let's\x01",
            "get fired up, shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_338A")

    ChrTalk(
        0x153,
        (
            "#01100FHide and seek? Sounds\x01",
            "fun!!\x02\x03",
            "#01109FLloyd, let's do our best\x01",
            "and look for her!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_338A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_3411")

    ChrTalk(
        0x156,
        (
            "#06405FWow, hide and seek with\x01",
            "that Mishette, you say?\x02\x03",
            "#06409FHaha, Lloyd! This being\x01",
            "the case, let's do our\x01",
            "best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3488")

    ChrTalk(
        0x14C,
        (
            "#05905FMy, something like that\x01",
            "happened?\x02\x03",
            "#05909FHaha. Then let's look\x01",
            "for that Mishette, shall\x01",
            "we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3533")

    ChrTalk(
        0x134,
        (
            "#01700FHm, hm, I understand. Seems\x01",
            "interesting.\x02\x03",
            "#01709FIt's just hide and seek, but it\x01",
            "seems we must do it all out, eh?\x01",
            "Let's do our best, little bro!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_35C8")

    ChrTalk(
        0x135,
        (
            "#01802FI see... I understand the\x01",
            "situation.\x02\x03",
            "#01809FHaha. Hide and seek is my\x01",
            "forte as well, so please\x01",
            "allow me to accompany you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_35C8")


    ChrTalk(
        0x166,
        (
            "#14000FHmm, hide and seek, eh?\x01",
            "It's pretty weird, though.\x02\x03",
            "#14004FWell, I'm free so I'll tag\x01",
            "along. ...C'mon, let's get\x01",
            "looking already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_36C6")

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FThen, let's start\x01",
            "looking for her in the\x01",
            "theme park right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3728")

    label("loc_36C6")


    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks.\x02\x03",
            "#00000FThen, let's start\x01",
            "looking for her in the\x01",
            "theme park right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3728")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Mishette's\x01",
            "Challenge]\x07\x00",
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

    # Function_32_29B7 end

    def Function_33_37A8(): pass

    label("Function_33_37A8")

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
            "#05200FPhew, we got through\x01",
            "that somehow...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F...Good job.\x02\x03",
            "#05526FDancing in a mascot\x01",
            "character costume was\x01",
            "quite tough...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FYou're right... It was\x01",
            "insanely hot.\x02\x03",
            "#05209FThe real actor does this\x01",
            "every day... He's really\x01",
            "something.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FHaha... right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 6440, 0, 1530, 45)

    NpcTalk(
        0x1D,
        "Man's Voice",
        "Heeey! Mishy, Mishette!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(11850, 0, 8160, 3000)
    SetCameraDistance(20690, 3000)

    def lambda_3A16():

        label("loc_3A16")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3A16")

    QueueWorkItem2(0x101, 1, lambda_3A16)

    def lambda_3A28():

        label("loc_3A28")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3A28")

    QueueWorkItem2(0x103, 1, lambda_3A28)
    OP_95(0x1D, 10760, 0, 5250, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FAh... Good work out\x01",
            "there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yeah, same to you. That\x01",
            "was great work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hey, listen to this. It seems\x01",
            ""Mishette" is quite the topic of\x01",
            "conversation in the park today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FTopic... you say?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yeah, they say they can't get\x01",
            "enough of the cool behavior she\x01",
            "displays when accompanying Mishy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hmm, maybe we should think about\x01",
            "taking "Mishette"'s character in\x01",
            "a different direction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FR-Really?\x07\x00\x02",
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
            "#05524F...*ahem*... Well, I'm\x01",
            "just happy I could help.\x02\x03",
            "#05520FBy the way... Is the\x01",
            "real actor still...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...Ah, right, how could\x01",
            "I forget!? He arrived\x01",
            "just moments ago.\x02",
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
            "Thank you, really. If\x01",
            "you like, please accept\x01",
            "this as compensation.\x02",
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
            "#05200FThen, Tio... Shall we\x01",
            "head inside?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYes, let's.\x07\x00\x02",
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

    # Function_33_37A8 end

    def Function_34_3EA3(): pass

    label("Function_34_3EA3")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sketch map of the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_34_3EA3 end

    SaveToFile()

Try(main)
