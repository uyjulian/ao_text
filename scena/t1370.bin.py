from ScenarioHelper import *

def main():
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
        "Randy",               # 1
        "Noel",                 # 2
        "Waji",                   # 3
        "Keya",                 # 4
        "Zeit",               # 5
        "Cecil",                 # 6
        "Ilia",                 # 7
        "Lisha",               # 8
        "Shuri",                 # 9
        "Misee",               # 10
        "Marsun",               # 11
        "corona",                 # 12
        "Lima",                   # 13
        "MWL staff",         # 14
        "tourist",                 # 15
        "tourist",                 # 16
        "tourist",                 # 17
        "tourist",                 # 18
        "tourist",                 # 19
        "tourist",                 # 20
        "tourist",                 # 21
        "Staff Hanks",           # 22
        "Directions to Wonderland entrance square",# 23
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

    PlaceName(10.0, 0.0, -45.0, 0x0000, 0x0000, "Directions to Wonderland entrance square")
    PlaceName(17.68000030517578, 0.0, 4.739999771118164, 0x0000, 0x0053, "")

    ChipFrameInfo(1208, 0)                                       # 0

    ScpFunction((
        "Function_0_4B8",          # 00, 0
        "Function_1_570",          # 01, 1
        "Function_2_5FC",          # 02, 2
        "Function_3_715",          # 03, 3
        "Function_4_7C2",          # 04, 4
        "Function_5_97E",          # 05, 5
        "Function_6_AEF",          # 06, 6
        "Function_7_D42",          # 07, 7
        "Function_8_DF8",          # 08, 8
        "Function_9_F17",          # 09, 9
        "Function_10_1193",        # 0A, 10
        "Function_11_1373",        # 0B, 11
        "Function_12_1440",        # 0C, 12
        "Function_13_1507",        # 0D, 13
        "Function_14_150B",        # 0E, 14
        "Function_15_150F",        # 0F, 15
        "Function_16_159D",        # 10, 16
        "Function_17_1640",        # 11, 17
        "Function_18_16D0",        # 12, 18
        "Function_19_16D4",        # 13, 19
        "Function_20_1860",        # 14, 20
        "Function_21_18DE",        # 15, 21
        "Function_22_1950",        # 16, 22
        "Function_23_19D5",        # 17, 23
        "Function_24_1A98",        # 18, 24
        "Function_25_1B27",        # 19, 25
        "Function_26_1BD2",        # 1A, 26
        "Function_27_1C7A",        # 1B, 27
        "Function_28_1D30",        # 1C, 28
        "Function_29_1FAF",        # 1D, 29
        "Function_30_262C",        # 1E, 30
        "Function_31_276D",        # 1F, 31
        "Function_32_2934",        # 20, 32
        "Function_33_3742",        # 21, 33
        "Function_34_3DFC",        # 22, 34
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
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
            "\"The third volume of sweets' kingdom\" is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_7BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Nanako Wotamaime\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7BE")

    TalkEnd(0xFF)
    Return()

    # Function_3_715 end

    def Function_4_7C2(): pass

    label("Function_4_7C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    Jump("loc_97A")

    label("loc_7DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    Jump("loc_97A")

    label("loc_7F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7")

    ChrTalk(
        0x8,
        (
            "#00306Fぬう……Cecilさんと\x01",
            "Trying to have fun and tea\x01",
            "I thought that.\x02\x03",
            "#00309Fまあ、ここはNoelで\x01",
            "Are you going to endure it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#10106FSuddenly, something extensive … senpai ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_94E")

    label("loc_8D7")


    ChrTalk(
        0x8,
        (
            "#00306FCecilさんと\x01",
            "Trying to have fun and tea\x01",
            "I thought that.\x02\x03",
            "#00309Fまあ、Noelに\x01",
            "I suppose you are going out with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94E")

    Jump("loc_97A")

    label("loc_953")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    Jump("loc_97A")

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")

    label("loc_97A")

    TalkEnd(0xFE)
    Return()

    # Function_4_7C2 end

    def Function_5_97E(): pass

    label("Function_5_97E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_997")
    Jump("loc_AEB")

    label("loc_997")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD")
    Jump("loc_AEB")

    label("loc_9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3A")

    ChrTalk(
        0x9,
        (
            "#10100FCecilさんは遊びに\x01",
            "It seems to be out.\x02\x03",
            "#10109Fふふ、Randy先輩も\x01",
            "The timing is bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ABF")

    label("loc_A3A")


    ChrTalk(
        0x9,
        (
            "#10105Fby the way……\x01",
            "Zeit君はずっとここで\x01",
            "I am planning to take a nap.\x02\x03",
            "#10104FWell, something in a shop\x01",
            "I wonder if I should buy it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABF")

    Jump("loc_AEB")

    label("loc_AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADA")
    Jump("loc_AEB")

    label("loc_ADA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEB")

    label("loc_AEB")

    TalkEnd(0xFE)
    Return()

    # Function_5_97E end

    def Function_6_AEF(): pass

    label("Function_6_AEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B08")
    Jump("loc_D3E")

    label("loc_B08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1E")
    Jump("loc_D3E")

    label("loc_B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B34")
    Jump("loc_D3E")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4A")
    Jump("loc_D3E")

    label("loc_B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(
        0x101,
        (
            "#00005FWaji、なにしてるんだ？\x02\x03",
            "#00003Fまさか、Cecil姉に\x01",
            "You are spending a lot of money ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10306FHuh, good grief.\x01",
            "I want you to trust a little.\x02\x03",
            "#10302FTo the club where I am going\x01",
            "A woman of her kind also comes around … …\x01",
            "I am off today and I will not go out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FBecause it is such a thing\x01",
            "I do not believe it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D3E")

    label("loc_CB2")


    ChrTalk(
        0xA,
        (
            "#10305Fうちの店にはCecilさんくらいの\x01",
            "A woman of a marriage may come but … …\x02\x03",
            "#10300FHuh, for your lovely older sister\x01",
            "I will not put out my hands or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3E")

    TalkEnd(0xFE)
    Return()

    # Function_6_AEF end

    def Function_7_D42(): pass

    label("Function_7_D42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B")
    Jump("loc_DF4")

    label("loc_D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    Call(0, 27)
    Jump("loc_DB2")

    label("loc_D7E")


    ChrTalk(
        0xB,
        (
            "#01105FEh, because\x01",
            "It's cute, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB2")

    Jump("loc_DF4")

    label("loc_DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    Jump("loc_DF4")

    label("loc_DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE3")
    Jump("loc_DF4")

    label("loc_DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF4")

    label("loc_DF4")

    TalkEnd(0xFE)
    Return()

    # Function_7_D42 end

    def Function_8_DF8(): pass

    label("Function_8_DF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E32")

    ChrTalk(
        0xC,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E55")
    Call(0, 27)
    Jump("loc_E6E")

    label("loc_E55")


    ChrTalk(
        0xC,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()

    label("loc_E6E")

    Jump("loc_F13")

    label("loc_E73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA6")

    ChrTalk(
        0xC,
        "#01200F… …. Gurururu ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(
        0xC,
        "#01200F… …. Gurulu …… won.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(
        0xC,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_F13")

    TalkEnd(0xFE)
    Return()

    # Function_8_DF8 end

    def Function_9_F17(): pass

    label("Function_9_F17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAB")

    ChrTalk(
        0xD,
        (
            "#05900FAs much as possible I\x01",
            "I'm going to stay here.\x02\x03",
            "#05909FHuhu, Lloyd's are\x01",
            "Please help yourself without hesitation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1023")

    label("loc_FAB")


    ChrTalk(
        0xD,
        (
            "#05904FしばらくはZeitくんと\x01",
            "Maybe I should relax.\x02\x03",
            "#05909FHehuu, but if you invite me\x01",
            "You will be with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    Jump("loc_118F")

    label("loc_1028")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103E")
    Jump("loc_118F")

    label("loc_103E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1054")
    Jump("loc_118F")

    label("loc_1054")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106A")
    Jump("loc_118F")

    label("loc_106A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")

    ChrTalk(
        0xD,
        (
            "#05900FHuhu, it is about time.\x01",
            "Because the part of the day seems to end\x01",
            "I'm waiting for everyone here.\x02\x03",
            "#05904FWhen Lloyd also finished playing,\x01",
            "Please come back here once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_118F")

    label("loc_1112")


    ChrTalk(
        0xD,
        (
            "#05900FWhen Lloyd also finished playing,\x01",
            "Please come back here once.\x02\x03",
            "#05909FHuhu, of course\x01",
            "If you invite me\x01",
            "I will be with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    TalkEnd(0xFE)
    Return()

    # Function_9_F17 end

    def Function_10_1193(): pass

    label("Function_10_1193")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AC")
    Jump("loc_136F")

    label("loc_11AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C2")
    Jump("loc_136F")

    label("loc_11C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D8")
    Jump("loc_136F")

    label("loc_11D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    ChrTalk(
        0xE,
        (
            "#01700Fこの子、Zeit君だっけ？\x01",
            "It is usually quiet,\x01",
            "He looks pretty smart.\x02\x03",
            "#01704FEven in Crossbell Times before\x01",
            "It seems I was introduced … …\x01",
            "I feel quite a star.\x02\x03",
            "#01709FHuff, to the alkane shell\x01",
            "I will scout you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1359")

    label("loc_12E5")


    ChrTalk(
        0xE,
        (
            "#01704FZeit君には\x01",
            "I feel quite a star.\x02\x03",
            "#01709FHuff, to the alkane shell\x01",
            "I will scout you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1359")

    Jump("loc_136F")

    label("loc_135E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136F")

    label("loc_136F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1193 end

    def Function_11_1373(): pass

    label("Function_11_1373")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138C")
    Jump("loc_143C")

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A2")
    Jump("loc_143C")

    label("loc_13A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B8")
    Jump("loc_143C")

    label("loc_13B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142B")

    ChrTalk(
        0xF,
        (
            "#01803FThe straw soup of the shop there\x01",
            "It was quite delicious.\x02\x03",
            "#01809FHave you tried eating yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143C")

    label("loc_142B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143C")

    label("loc_143C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1373 end

    def Function_12_1440(): pass

    label("Function_12_1440")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1459")
    Jump("loc_1503")

    label("loc_1459")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147C")
    Call(0, 27)
    Jump("loc_14C1")

    label("loc_147C")


    ChrTalk(
        0x10,
        (
            "#14006FIt is cute\x01",
            "It might be cool\x01",
            "Do not you wish you ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C1")

    Jump("loc_1503")

    label("loc_14C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DC")
    Jump("loc_1503")

    label("loc_14DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F2")
    Jump("loc_1503")

    label("loc_14F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1503")

    label("loc_1503")

    TalkEnd(0xFE)
    Return()

    # Function_12_1440 end

    def Function_13_1507(): pass

    label("Function_13_1507")

    Call(0, 29)
    Return()

    # Function_13_1507 end

    def Function_14_150B(): pass

    label("Function_14_150B")

    Call(0, 30)
    Return()

    # Function_14_150B end

    def Function_15_150F(): pass

    label("Function_15_150F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1546")

    ChrTalk(
        0x12,
        "Now, what shall we take next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155C")
    Jump("loc_1599")

    label("loc_155C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1572")
    Jump("loc_1599")

    label("loc_1572")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    Jump("loc_1599")

    label("loc_1588")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1599")

    label("loc_1599")

    TalkEnd(0xFE)
    Return()

    # Function_15_150F end

    def Function_16_159D(): pass

    label("Function_16_159D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E9")

    ChrTalk(
        0x13,
        (
            "Huh, you know.\x01",
            "Let's take it easy at a high place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163C")

    label("loc_15E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FF")
    Jump("loc_163C")

    label("loc_15FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1615")
    Jump("loc_163C")

    label("loc_1615")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162B")
    Jump("loc_163C")

    label("loc_162B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163C")

    label("loc_163C")

    TalkEnd(0xFE)
    Return()

    # Function_16_159D end

    def Function_17_1640(): pass

    label("Function_17_1640")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1679")

    ChrTalk(
        0x14,
        "Lima、観覧車に乗りたーい！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_1679")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168F")
    Jump("loc_16CC")

    label("loc_168F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A5")
    Jump("loc_16CC")

    label("loc_16A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BB")
    Jump("loc_16CC")

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CC")

    label("loc_16CC")

    TalkEnd(0xFE)
    Return()

    # Function_17_1640 end

    def Function_18_16D0(): pass

    label("Function_18_16D0")

    Call(0, 19)
    Return()

    # Function_18_16D0 end

    def Function_19_16D4(): pass

    label("Function_19_16D4")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",              # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_173B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175B")
    OP_AF(0x6B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1857")

    label("loc_175B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176F")
    Jump("loc_1857")

    label("loc_176F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1787")
    TalkEnd(0x15)
    Return()

    label("loc_1787")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1857")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F8")

    ChrTalk(
        0x15,
        "Welcome~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "How about a delicious Japanese cotton candy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_17F8")


    ChrTalk(
        0x15,
        (
            "It is about time that my stomach is empty\x01",
            "Is there~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "How about sweet ~ Iwakita?\x02",
    )

    CloseMessageWindow()

    label("loc_1857")

    Jump("loc_16E1")

    label("loc_185C")

    TalkEnd(0x15)
    Return()

    # Function_19_16D4 end

    def Function_20_1860(): pass

    label("Function_20_1860")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B4")

    ChrTalk(
        0x16,
        (
            "Oh, already here\x01",
            "Stop fighting!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DA")

    label("loc_18B4")


    ChrTalk(
        0x16,
        "Oh, now, please gaman!\x02",
    )

    CloseMessageWindow()

    label("loc_18DA")

    TalkEnd(0xFE)
    Return()

    # Function_20_1860 end

    def Function_21_18DE(): pass

    label("Function_21_18DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(
        0x17,
        (
            "Hello, just about a mouthful\x01",
            "Is not it good?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_194C")

    label("loc_1926")


    ChrTalk(
        0x17,
        "It is absolutely premature to go home again!\x02",
    )

    CloseMessageWindow()

    label("loc_194C")

    TalkEnd(0xFE)
    Return()

    # Function_21_18DE end

    def Function_22_1950(): pass

    label("Function_22_1950")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199E")

    ChrTalk(
        0x18,
        (
            "Ahh, onii-chan\x01",
            "I ate a cotton candy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D1")

    label("loc_199E")


    ChrTalk(
        0x18,
        (
            "Ahh, it's temperate ~!\x01",
            "I also see the night parade ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D1")

    TalkEnd(0xFE)
    Return()

    # Function_22_1950 end

    def Function_23_19D5(): pass

    label("Function_23_19D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A54")

    ChrTalk(
        0x19,
        (
            "Let me wait, honey.\x01",
            "I bought juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "With this love love straw\x01",
            "Let's drink it together!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A94")

    label("loc_1A54")


    ChrTalk(
        0x19,
        "The sunset is beautiful, honey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "But you are more beautiful.\x02",
    )

    CloseMessageWindow()

    label("loc_1A94")

    TalkEnd(0xFE)
    Return()

    # Function_23_19D5 end

    def Function_24_1A98(): pass

    label("Function_24_1A98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(
        0x1A,
        (
            "No, I do not care like that\x01",
            "Please buy two.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B23")

    label("loc_1AEC")


    ChrTalk(
        0x1A,
        (
            "No, I do not care like that\x01",
            "Let's go home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B23")

    TalkEnd(0xFE)
    Return()

    # Function_24_1A98 end

    def Function_25_1B27(): pass

    label("Function_25_1B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCE")

    ChrTalk(
        0x1B,
        (
            "Although it was a quiet and beautiful resort,\x01",
            "Michelam changed, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Hold on to everything for young people.\x01",
            "I want you to think about the elderly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCE")

    label("loc_1BCE")

    TalkEnd(0xFE)
    Return()

    # Function_25_1B27 end

    def Function_26_1BD2(): pass

    label("Function_26_1BD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(
        0x1C,
        (
            "Huhu, old man\x01",
            "I'm talking about that,\x01",
            "I am enjoying the inner circumstances considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Today, even on a horror coaster\x01",
            "I already have it four times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C76")

    label("loc_1C76")

    TalkEnd(0xFE)
    Return()

    # Function_26_1BD2 end

    def Function_27_1C7A(): pass

    label("Function_27_1C7A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xB,
        (
            "#01109FWell then, then\x01",
            "The next attraction is\x01",
            "Zeitも一緒に乗ろー！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01200F……won?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#14006FNo … No, it is impossible,\x01",
            "Think common sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_27_1C7A end

    def Function_28_1D30(): pass

    label("Function_28_1D30")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E41")
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
    Jump("loc_1FAE")

    label("loc_1E41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6B")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_1FAE")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAD")
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
    Jump("loc_1FAE")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F59")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_END)), "loc_1F09")
    SetChrPos(0x11, 14920, 0, -450, 270)

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_END)), "loc_1F17")
    SetChrFlags(0x11, 0x80)

    label("loc_1F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_1F46")
    SetChrFlags(0xE, 0x80)
    Jump("loc_1F54")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_1F54")
    SetChrFlags(0xF, 0x80)

    label("loc_1F54")

    Jump("loc_1FAE")

    label("loc_1F59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAE")
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

    label("loc_1FAE")

    Return()

    # Function_28_1D30 end

    def Function_29_1FAF(): pass

    label("Function_29_1FAF")

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
            "#00005FThat, something pink is there\x01",
            "You are hiding … ….?\x02",
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
            "Kyat, I found it ☆\x07\x00\x02",
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
            "Nice to meet you, my older broom\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あたしは『Misee』だヨっ♪\x01",
            "Misashi, thanks!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FOh, maybe\x01",
            "Mi sister sister?\x02\x03",
            "#00004FTio, if you are lucky\x01",
            "Saying I can meet you ….\x01",
            "I was lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Oh, I knew ~!\x01",
            "Misashi, glad to see you ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005Fby the way……\x01",
            "Why in such a place\x01",
            "You were hiding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, I me.\x01",
            "I love hide and seek.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Always wonderland\x01",
            "Hiding somewhere, the Prince of Hakuba\x01",
            "I'm waiting for you to find a spray\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(You have to be lucky.\x01",
            "I can not see you … …)\x02\x03",
            "#00012FHaha … that this time\x01",
            "I wonder if I am the Prince of Hakuba?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, it's like that ~.\x01",
            "Did you find it?\x01",
            "I'm so happy!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Shibuya's Onii-chan's\x01",
            "Hundred-fold is a handsome man,\x01",
            "The prince's qualification is perfect as well ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Mi, Michishi delicately\x01",
            "It seems that it is terrible … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "so……\x01",
            "Older with me\x01",
            "Do you play hide-and - seek?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005Feh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "He found me.\x01",
            "Only the prince can participate,\x01",
            "It is a special game.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "The older brother, together with his friends,\x01",
            "I'm hiding in Wonderland\x01",
            "Find me five times!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There are gorgeous prizes too ☆\x01",
            "How do you not try?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_29_1FAF end

    def Function_30_262C(): pass

    label("Function_30_262C")

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
            "Oh, my older brother!\x01",
            "After all I and hide and see ~?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "The older brother, together with his friends,\x01",
            "I'm hiding in Wonderland\x01",
            "Find me five times!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "There are gorgeous prizes too ☆\x01",
            "How do you not try?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_30_262C end

    def Function_31_276D(): pass

    label("Function_31_276D")


    ChrTalk(
        0x101,
        (
            "#00003F(Once you start,\x01",
            "By the other attractions till the end\x01",
            "I do not think I have time to play … …)\x02",
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
            "【Accept】\x01",      # 0
            "【I will stop it】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283D")
    Call(0, 32)
    Jump("loc_28FC")

    label("loc_283D")


    ChrTalk(
        0x101,
        (
            "#00000FWell, sorry.\x01",
            "Now I've got attractions\x01",
            "I'm in the middle of spinning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Well, is that so ~?\x01",
            "Frustrated ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "But when I want to do it\x01",
            "Say it anytime you'd like!\x01",
            "I'm waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 6)

    label("loc_28FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x11, 14920, 0, -450, 270)
    OP_4C(0x11, 0xFF)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_276D end

    def Function_32_2934(): pass

    label("Function_32_2934")


    ChrTalk(
        0x101,
        (
            "#00000FWell then……\x01",
            "Let's try it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, there you are!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Well then, I will hide from there.\x01",
            "The older partner\x01",
            "Searching for it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "When you give up\x01",
            "To Michio ioio in the square\x01",
            "Because you only have to tell me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, that's it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(12510, 0, 1310, 3000)

    def lambda_2A79():

        label("loc_2A79")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_2A79")

    QueueWorkItem2(0x101, 1, lambda_2A79)
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
            "#00003FAnd anyway … …\x01",
            "一緒にMiseeを探す\x01",
            "I need a partner.\x02\x03",
            "#00000FWho should I invite …?\x02",
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
            "【Erie】\x01",        # 0
            "[Tio]\x01",        # 1
            "【Randy】\x01",      # 2
            "【Noel】\x01",        # 3
            "【Waji】\x01",          # 4
            "【Keya】\x01",        # 5
            "[Franc]\x01",        # 6
            "【Cecil】\x01",        # 7
            "【Ilia】\x01",        # 8
            "【Lisha】\x01",      # 9
            "【Shuri】\x01",        # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C3D"),
        (1, "loc_2C83"),
        (2, "loc_2CC9"),
        (3, "loc_2D11"),
        (4, "loc_2D57"),
        (5, "loc_2D9B"),
        (6, "loc_2DE1"),
        (7, "loc_2E27"),
        (8, "loc_2E6F"),
        (9, "loc_2EB9"),
        (10, "loc_2F01"),
        (SWITCH_DEFAULT, "loc_2F47"),
    )


    label("loc_2C3D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C7, 7)

    ChrTalk(
        0x101,
        "#00000F(Okay … let's invite Ellie.\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x0)
    Jump("loc_2F47")

    label("loc_2C83")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 0)

    ChrTalk(
        0x101,
        "#00000F(Alright … let's invite Tio.\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x1)
    Jump("loc_2F47")

    label("loc_2CC9")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 1)

    ChrTalk(
        0x101,
        "#00000F（よし……Randyを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x2)
    Jump("loc_2F47")

    label("loc_2D11")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 2)

    ChrTalk(
        0x101,
        "#00000F（よし……Noelを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x3)
    Jump("loc_2F47")

    label("loc_2D57")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 3)

    ChrTalk(
        0x101,
        "#00000F（よし……Wajiを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x4)
    Jump("loc_2F47")

    label("loc_2D9B")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 4)

    ChrTalk(
        0x101,
        "#00000F（よし……Keyaを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x5)
    Jump("loc_2F47")

    label("loc_2DE1")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 5)

    ChrTalk(
        0x101,
        "#00000F(Alright … let's invite the franc.\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x6)
    Jump("loc_2F47")

    label("loc_2E27")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 6)

    ChrTalk(
        0x101,
        "#00000F（よし……Cecil姉を誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x7)
    Jump("loc_2F47")

    label("loc_2E6F")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 7)

    ChrTalk(
        0x101,
        "#00000F（よし……Iliaさんを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x8)
    Jump("loc_2F47")

    label("loc_2EB9")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 0)

    ChrTalk(
        0x101,
        "#00000F（よし……Lishaを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x9)
    Jump("loc_2F47")

    label("loc_2F01")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 1)

    ChrTalk(
        0x101,
        "#00000F（よし……Shuriを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0xA)
    Jump("loc_2F47")

    label("loc_2F47")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_2F64")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_2F76")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_2F88")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2F9A")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_2FAC")
    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2FBE")
    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_2FD0")
    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_2FE2")
    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_2FF9")
    AddParty(0x33, 0xEF, 0xFF)
    SetChrFlags(0xE, 0x80)
    Jump("loc_3014")

    label("loc_2FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_3010")
    AddParty(0x34, 0xEF, 0xFF)
    SetChrFlags(0xF, 0x80)
    Jump("loc_3014")

    label("loc_3010")

    AddParty(0x65, 0xEF, 0xFF)

    label("loc_3014")

    OP_68(14480, 0, 520, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0xEF, 13000, 0, 200, 180)
    SetChrPos(0x101, 13000, 0, -1690, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_30DF")

    ChrTalk(
        0x102,
        (
            "#00100FYeah, I know the circumstances.\x02\x03",
            "#00109FHehe he seems quite enjoyable,\x01",
            "Let's do our best and look for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_30DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3168")

    ChrTalk(
        0x103,
        (
            "#00200FI see……\x01",
            "I understood the circumstances.\x02\x03",
            "#00204FあのMiseeとかくれんぼ……\x01",
            "I have to go in with the spirit\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_31DD")

    ChrTalk(
        0x104,
        (
            "#00300FI see, I understand the circumstances.\x02\x03",
            "#00304FWell, to the attraction of the attraction\x01",
            "Why do not you try playing for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_31DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_324E")

    ChrTalk(
        0x109,
        (
            "#10105FHa, such a thing ……\x02\x03",
            "#10109FBut it looks interesting, is not it?\x01",
            "Let's search seriously because I will do it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_324E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_32D6")

    ChrTalk(
        0x105,
        (
            "#10300FHmm, I see.\x01",
            "It seemed pretty fun.\x02\x03",
            "#10309FBecause it's cheap\x01",
            "Let's spirit and look for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_32D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_333A")

    ChrTalk(
        0x153,
        (
            "#01100FHide and seek, it's fun! It is!\x02\x03",
            "#01109FLloyd, do your best! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_33BA")

    ChrTalk(
        0x156,
        (
            "#06405Fへえ、あのMiseeと\x01",
            "Hide and seek ~ ~.\x02\x03",
            "#06409FHuh, Lloyd!\x01",
            "Let's do it this way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_33BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3433")

    ChrTalk(
        0x14C,
        (
            "#05905FWell, there was such a thing.\x02\x03",
            "#05909FHuhu, then that\x01",
            "Miseeって子を探してみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_34DA")

    ChrTalk(
        0x134,
        (
            "#01700FHmm, I know the circumstances.\x01",
            "It sounds like funny somehow.\x02\x03",
            "#01709FTakaka is a hide and seek,\x01",
            "It seems necessary to seriously!\x01",
            "Let's do our best, my brother!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_34DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_355D")

    ChrTalk(
        0x135,
        (
            "#01802Fなるほど……I understood the circumstances.\x02\x03",
            "#01809FHuhu, I am also good at hide and seek,\x01",
            "I will be with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_355D")


    ChrTalk(
        0x166,
        (
            "#14000FHmm, hide and seek.\x01",
            "I'm supposed to be talking about something.\x02\x03",
            "#14004FWell, I do not have time, I will go out with you.\x01",
            "Let's go looking around quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3662")

    ChrTalk(
        0x101,
        (
            "#00009FHello, thank you.\x02\x03",
            "#00000FWell then\x01",
            "Let's search inside the theme park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C1")

    label("loc_3662")


    ChrTalk(
        0x101,
        (
            "#00009FHello, I beg you.\x02\x03",
            "#00000FWell then\x01",
            "Why do not you try looking inside the theme park.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【Miseeの挑戦】\x07\x00",
            "I started!\x02",
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

    # Function_32_2934 end

    def Function_33_3742(): pass

    label("Function_33_3742")

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
            "#05200FWell, I managed to do it … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F… … Good work.\x02\x03",
            "#05526FDance as a costume\x01",
            "It was quite a hard time …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FThat's right.\x01",
            "It is very hot.\x02\x03",
            "#05209FI will do this everyday\x01",
            "A real actor is\x01",
            "It is a big deal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FHehe … … That's right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 6440, 0, 1530, 45)

    NpcTalk(
        0x1D,
        "Male voice",
        (
            "Hey!\x01",
            "みっしぃ、Misee！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(11850, 0, 8160, 3000)
    SetCameraDistance(20690, 3000)

    def lambda_39AE():

        label("loc_39AE")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_39AE")

    QueueWorkItem2(0x101, 1, lambda_39AE)

    def lambda_39C0():

        label("loc_39C0")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_39C0")

    QueueWorkItem2(0x103, 1, lambda_39C0)
    OP_95(0x1D, 10760, 0, 5250, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FAh……\x01",
            "Is cheers for good work.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh Good job.\x01",
            "It was a real cheek!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Come on, listen.\x01",
            "今日の『Misee』がなんだか\x01",
            "It seems pretty hot topic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FTopic ……?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh, accompanied Misoshi\x01",
            "The coolest idea that I was occasionally showing\x01",
            "I am dying!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Well, this is\x01",
            "『Misee』のキャラの方向性を\x01",
            "I wonder if it is better to rethink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212FIs that so …?\x07\x00\x02",
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
            "#05524F…… Konin …\x01",
            "Well, I hope it helped.\x02\x03",
            "#05520Fby the way……\x01",
            "A real actor, yet … …?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "…… Oh, I forgot that!\x01",
            "I arrived just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Because he seems to head back later,\x01",
            "Go to the locker room ahead\x01",
            "Wait for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Really appreciate your work.\x01",
            "If it's okay, at my bite cost\x01",
            "Please accept this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '咪雪玩偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('咪雪玩偶', 1)
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
            "#05200FWell then, Tio …\x01",
            "Would you like to go up?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522FYeah, you are right.\x07\x00\x02",
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

    # Function_33_3742 end

    def Function_34_3DFC(): pass

    label("Function_34_3DFC")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of the theme park\x01",
            "A sketch is drawn.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_34_3DFC end

    SaveToFile()

Try(main)
