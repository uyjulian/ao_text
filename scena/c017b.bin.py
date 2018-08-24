from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c017b.bin",                # FileName
        "c017b",                    # MapName
        "c017b",                    # Location
        0x0005,                     # MapIndex
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
        "c017b",                  # 0
        "Receptionist Pearl",     # 1
        "Receptionist Cynthia",   # 2
        "Hanson",                 # 3
        "Region",                 # 4
        "Prada",                  # 5
        "Baker",                  # 6
        "Southwark",              # 7
        "Manager Neston",         # 8
        "Jeanetta",               # 9
        "Dorothee",               # 10
        "Ken",                    # 11
        "Old Man Honest",         # 12
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch21600.itc",                   # 08
        "chr/ch34600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch20500.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294955767, 8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294951307, 0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294964636, 0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294960637, 8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294952847, 8000,    14420,   90,   257,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(4294966816, 8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(4294954906, 8000,    7660,    1000,    4294955766, 9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(4294951266, 0,       23800,   1000,    4294951306, 1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(920, 0)                                        # 0

    ScpFunction((
        "Function_0_398",          # 00, 0
        "Function_1_448",          # 01, 1
        "Function_2_521",          # 02, 2
        "Function_3_54F",          # 03, 3
        "Function_4_57F",          # 04, 4
        "Function_5_583",          # 05, 5
        "Function_6_697",          # 06, 6
        "Function_7_69B",          # 07, 7
        "Function_8_7CF",          # 08, 8
        "Function_9_7D3",          # 09, 9
        "Function_10_B35",         # 0A, 10
        "Function_11_B39",         # 0B, 11
        "Function_12_C85",         # 0C, 12
        "Function_13_C89",         # 0D, 13
        "Function_14_DA5",         # 0E, 14
        "Function_15_DA9",         # 0F, 15
        "Function_16_FC2",         # 10, 16
        "Function_17_FC6",         # 11, 17
        "Function_18_11F3",        # 12, 18
        "Function_19_1279",        # 13, 19
        "Function_20_12F3",        # 14, 20
        "Function_21_13C3",        # 15, 21
        "Function_22_1438",        # 16, 22
        "Function_23_1497",        # 17, 23
    ))


    def Function_0_398(): pass

    label("Function_0_398")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D0"),
        (1, "loc_3DC"),
        (2, "loc_3E8"),
        (3, "loc_3F4"),
        (4, "loc_400"),
        (5, "loc_40C"),
        (6, "loc_418"),
        (SWITCH_DEFAULT, "loc_424"),
    )


    label("loc_3D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_400")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_40C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_418")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_424")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_430")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_447")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_447")

    Return()

    # Function_0_398 end

    def Function_1_448(): pass

    label("Function_1_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_520")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_448")

    label("loc_520")

    Return()

    # Function_1_448 end

    def Function_2_521(): pass

    label("Function_2_521")

    SetChrPos(0x12, 8020, 8000, 17270, 90)
    SetChrPos(0x11, 9070, 8000, 17290, 270)
    BeginChrThread(0x11, 0, 0, 0)
    SetChrFlags(0x11, 0x10)
    Return()

    # Function_2_521 end

    def Function_3_54F(): pass

    label("Function_3_54F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_57E")

    label("loc_570")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_57E")

    Return()

    # Function_3_54F end

    def Function_4_57F(): pass

    label("Function_4_57F")

    Call(0, 5)
    Return()

    # Function_4_57F end

    def Function_5_583(): pass

    label("Function_5_583")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63E")

    ChrTalk(
        0x8,
        (
            "After we finish work today,\x01",
            "I'm going out to eat with\x01",
            "Cynthia and Jeanetta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party\x01",
            "in a long time... Haha, I'm\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_693")

    label("loc_63E")


    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party\x01",
            "in a long time... Haha, I'm\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_693")

    TalkEnd(0x8)
    Return()

    # Function_5_583 end

    def Function_6_697(): pass

    label("Function_6_697")

    Call(0, 7)
    Return()

    # Function_6_697 end

    def Function_7_69B(): pass

    label("Function_7_69B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765")

    ChrTalk(
        0x9,
        (
            "Jeanetta is in awfully\x01",
            "high spirits today. Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not the first time the three\x01",
            "of us have had dinner together...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7CB")

    label("loc_765")


    ChrTalk(
        0x9,
        (
            "It's not the first time the three\x01",
            "of us have had dinner together...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CB")

    TalkEnd(0x9)
    Return()

    # Function_7_69B end

    def Function_8_7CF(): pass

    label("Function_8_7CF")

    Call(0, 9)
    Return()

    # Function_8_7CF end

    def Function_9_7D3(): pass

    label("Function_9_7D3")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B31")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_832")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_851")
    OP_AF(0x26)
    Jump("loc_873")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_861")
    OP_AF(0x25)
    Jump("loc_873")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_871")
    OP_AF(0x24)
    Jump("loc_873")

    label("loc_871")

    OP_AF(0x23)

    label("loc_873")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2C")

    label("loc_882")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_896")
    Jump("loc_B2C")

    label("loc_896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A22")

    ChrTalk(
        0xA,
        (
            "Everyone, did you know that\x01",
            "it's best to try on shoes\x01",
            "in the evening or later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is because, after we wake in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they can be as much as 1 rige bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is thought best to choose\x01",
            "your size in the evening or later, when\x01",
            "your feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B2C")

    label("loc_A22")


    ChrTalk(
        0xA,
        (
            "The truth is, after we wake in the morning, human\x01",
            "feet swell little by little, and when evening\x01",
            "arrives, they can be as much as 1 rige bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is thought best to choose\x01",
            "your size in the evening or later, when\x01",
            "your feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2C")

    Jump("loc_7E0")

    label("loc_B31")

    TalkEnd(0xA)
    Return()

    # Function_9_7D3 end

    def Function_10_B35(): pass

    label("Function_10_B35")

    Call(0, 11)
    Return()

    # Function_10_B35 end

    def Function_11_B39(): pass

    label("Function_11_B39")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C81")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B98")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB8")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7C")

    label("loc_BB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCC")
    Jump("loc_C7C")

    label("loc_BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        (
            "Good evening, and\x01",
            "welcome to Region Foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you haven't prepared dinner\x01",
            "yet, by all means, please come buy\x01",
            "your ingredients from us, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jump("loc_B46")

    label("loc_C81")

    TalkEnd(0xB)
    Return()

    # Function_11_B39 end

    def Function_12_C85(): pass

    label("Function_12_C85")

    Call(0, 13)
    Return()

    # Function_12_C85 end

    def Function_13_C89(): pass

    label("Function_13_C89")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D07")
    OP_AF(0x21)
    Jump("loc_D29")

    label("loc_D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D17")
    OP_AF(0x20)
    Jump("loc_D29")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D27")
    OP_AF(0x1F)
    Jump("loc_D29")

    label("loc_D27")

    OP_AF(0x1E)

    label("loc_D29")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4C")
    Jump("loc_D9C")

    label("loc_D4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xC,
        (
            "Welcome, please enjoy\x01",
            "your shopping this\x01",
            "evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C")

    Jump("loc_C96")

    label("loc_DA1")

    TalkEnd(0xC)
    Return()

    # Function_13_C89 end

    def Function_14_DA5(): pass

    label("Function_14_DA5")

    Call(0, 15)
    Return()

    # Function_14_DA5 end

    def Function_15_DA9(): pass

    label("Function_15_DA9")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E08")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E27")
    OP_AF(0x11)
    Jump("loc_E39")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E37")
    OP_AF(0x10)
    Jump("loc_E39")

    label("loc_E37")

    OP_AF(0xF)

    label("loc_E39")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB9")

    label("loc_E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5C")
    Jump("loc_FB9")

    label("loc_E5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2C")

    ChrTalk(
        0xD,
        "It's already dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's right, Arc-en-Ciel's\x01",
            "performance for the heads of\x01",
            "state should be ending soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mmm, I do hope they are\x01",
            "enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_FB9")

    label("loc_F2C")


    ChrTalk(
        0xD,
        (
            "That's right, Arc-en-Ciel's\x01",
            "performance for the heads of\x01",
            "state should be ending soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mmm, I do hope they are\x01",
            "enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB9")

    Jump("loc_DB6")

    label("loc_FBE")

    TalkEnd(0xD)
    Return()

    # Function_15_DA9 end

    def Function_16_FC2(): pass

    label("Function_16_FC2")

    Call(0, 17)
    Return()

    # Function_16_FC2 end

    def Function_17_FC6(): pass

    label("Function_17_FC6")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EF")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1025")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1025")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1045")
    OP_AF(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11EA")

    label("loc_1045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1059")
    Jump("loc_11EA")

    label("loc_1059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(
        0xE,
        (
            "Jeanetta has been\x01",
            "looking really happy\x01",
            "since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She was saying something I didn't\x01",
            "understand, like she's going to make a\x01",
            "fresh start tomorrow as "super Jeanetta"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't know, but for\x01",
            "some reason I'm really\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_11EA")

    label("loc_1174")


    ChrTalk(
        0xE,
        (
            "Jeanetta has been\x01",
            "looking really happy\x01",
            "since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't know, but for\x01",
            "some reason I'm really\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EA")

    Jump("loc_FD3")

    label("loc_11EF")

    TalkEnd(0xE)
    Return()

    # Function_17_FC6 end

    def Function_18_11F3(): pass

    label("Function_18_11F3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today's business hours\x01",
            "end at 20:00, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care not to\x01",
            "forget your purchases or\x01",
            "personal belongings.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_11F3 end

    def Function_19_1279(): pass

    label("Function_19_1279")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The western clothes are\x01",
            "ready and my makeup is\x01",
            "perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I'm going to be a\x01",
            "bit different tonight㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1279 end

    def Function_20_12F3(): pass

    label("Function_20_12F3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Listen, Ken.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as we get back, first tell\x01",
            "your dad you're sorry. Then, let's\x01",
            "hug him without a moment's delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine. If we both\x01",
            "sandwich him, there won't\x01",
            "be anything to fear.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_12F3 end

    def Function_21_13C3(): pass

    label("Function_21_13C3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Because mom was absorbed\x01",
            "in her shopping, it's\x01",
            "gotten this late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think dad's going to\x01",
            "be angry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_13C3 end

    def Function_22_1438(): pass

    label("Function_22_1438")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then, time to go\x01",
            "back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would be no match for\x01",
            "my angered old lady.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1438 end

    def Function_23_1497(): pass

    label("Function_23_1497")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique "Lucca"\x01",
            "2F Hanson's Shoes\x01",
            "2F Baker's Accessories\x01",
            "1F Region Foods\x01",
            "1F Southwark's General Goods Corner\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you have any questions,\x01",
            "please feel free to ask at\x01",
            "the information desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_23_1497 end

    SaveToFile()

Try(main)
