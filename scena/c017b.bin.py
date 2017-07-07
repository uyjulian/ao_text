from ScenarioHelper import *

def main():
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
        "Receptionist Pearl",           # 1
        "Receptionist Cynthia",         # 2
        "Hanson",               # 3
        "Region",               # 4
        "Prada",                 # 5
        "Baker",               # 6
        "Southwark",               # 7
        "Neston Manager",         # 8
        "Janetta",             # 9
        "Dorothe",                 # 10
        "Ken",                   # 11
        "Honest elderly",           # 12
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
        "Function_6_64C",          # 06, 6
        "Function_7_650",          # 07, 7
        "Function_8_74B",          # 08, 8
        "Function_9_74F",          # 09, 9
        "Function_10_A23",         # 0A, 10
        "Function_11_A27",         # 0B, 11
        "Function_12_B65",         # 0C, 12
        "Function_13_B69",         # 0D, 13
        "Function_14_C9C",         # 0E, 14
        "Function_15_CA0",         # 0F, 15
        "Function_16_EBD",         # 10, 16
        "Function_17_EC1",         # 11, 17
        "Function_18_10B2",        # 12, 18
        "Function_19_1138",        # 13, 19
        "Function_20_11A4",        # 14, 20
        "Function_21_1237",        # 15, 21
        "Function_22_1296",        # 16, 22
        "Function_23_12E9",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B")

    ChrTalk(
        0x8,
        (
            "Today at the end of work,\x01",
            "シンシア先輩とJanettaちゃんの\x01",
            "I go to dinner with three people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A dinner party for the first time in a while,\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_648")

    label("loc_61B")


    ChrTalk(
        0x8,
        (
            "A dinner party for the first time in a while,\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_648")

    TalkEnd(0x8)
    Return()

    # Function_5_583 end

    def Function_6_64C(): pass

    label("Function_6_64C")

    Call(0, 7)
    Return()

    # Function_6_64C end

    def Function_7_650(): pass

    label("Function_7_650")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F9")

    ChrTalk(
        0x9,
        (
            "Janettaさん、\x01",
            "Today bashfully\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apart from going to dinner by three people\x01",
            "It is not the first time … ….\x01",
            "I wonder if you are concerned?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_747")

    label("loc_6F9")


    ChrTalk(
        0x9,
        (
            "Apart from going to dinner by three people\x01",
            "It is not the first time … ….\x01",
            "I wonder if you are concerned?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_747")

    TalkEnd(0x9)
    Return()

    # Function_7_650 end

    def Function_8_74B(): pass

    label("Function_8_74B")

    Call(0, 9)
    Return()

    # Function_8_74B end

    def Function_9_74F(): pass

    label("Function_9_74F")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D9")
    OP_AF(0x26)
    Jump("loc_7FB")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7E9")
    OP_AF(0x25)
    Jump("loc_7FB")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F9")
    OP_AF(0x24)
    Jump("loc_7FB")

    label("loc_7F9")

    OP_AF(0x23)

    label("loc_7FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1A")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_A1A")

    label("loc_81E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_957")

    ChrTalk(
        0xA,
        (
            "Choosing shoes is better if you go after the evening\x01",
            "Does everyone know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because the person's legs woke up in the morning\x01",
            "Gradually swollen and even in the evening\x01",
            "It will be as large as about 1 Reju at maximum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So, after the evening when the foot becomes the largest\x01",
            "It is said that it is better to choose the size.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A1A")

    label("loc_957")


    ChrTalk(
        0xA,
        (
            "Actually, since the person's leg got up in the morning\x01",
            "Gradually swollen and even in the evening\x01",
            "It will be as large as about 1 Reju at maximum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So, after the evening when the foot becomes the largest\x01",
            "It is said that it is better to choose the size.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1A")

    Jump("loc_75C")

    label("loc_A1F")

    TalkEnd(0xA)
    Return()

    # Function_9_74F end

    def Function_10_A23(): pass

    label("Function_10_A23")

    Call(0, 11)
    Return()

    # Function_10_A23 end

    def Function_11_A27(): pass

    label("Function_11_A27")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B61")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A92")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5C")

    label("loc_AB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC6")
    Jump("loc_B5C")

    label("loc_AC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        (
            "Good evening.\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If supper of dinner is not yet,\x01",
            "By all means use the material\x01",
            "Please buy them and go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5C")

    Jump("loc_A34")

    label("loc_B61")

    TalkEnd(0xB)
    Return()

    # Function_11_A27 end

    def Function_12_B65(): pass

    label("Function_12_B65")

    Call(0, 13)
    Return()

    # Function_12_B65 end

    def Function_13_B69(): pass

    label("Function_13_B69")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BF3")
    OP_AF(0x21)
    Jump("loc_C15")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C03")
    OP_AF(0x20)
    Jump("loc_C15")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C13")
    OP_AF(0x1F)
    Jump("loc_C15")

    label("loc_C13")

    OP_AF(0x1E)

    label("loc_C15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C93")

    label("loc_C24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C38")
    Jump("loc_C93")

    label("loc_C38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C93")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xC,
        (
            "Welcome.\x01",
            "Please have a night shopping\x01",
            "Please enjoy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    Jump("loc_B76")

    label("loc_C98")

    TalkEnd(0xC)
    Return()

    # Function_13_B69 end

    def Function_14_C9C(): pass

    label("Function_14_C9C")

    Call(0, 15)
    Return()

    # Function_14_C9C end

    def Function_15_CA0(): pass

    label("Function_15_CA0")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D2A")
    OP_AF(0x11)
    Jump("loc_D3C")

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D3A")
    OP_AF(0x10)
    Jump("loc_D3C")

    label("loc_D3A")

    OP_AF(0xF)

    label("loc_D3C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EB4")

    label("loc_D4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5F")
    Jump("loc_EB4")

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2F")

    ChrTalk(
        0xD,
        "I was completely sunny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "By the way, by the leaders\x01",
            "The theater of the alkane shell\x01",
            "It was around the end of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, enjoy\x01",
            "I hope to have you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_EB4")

    label("loc_E2F")


    ChrTalk(
        0xD,
        (
            "By the way, by the leaders\x01",
            "The theater of the alkane shell\x01",
            "It was around the end of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, enjoy\x01",
            "I hope to have you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB4")

    Jump("loc_CAD")

    label("loc_EB9")

    TalkEnd(0xD)
    Return()

    # Function_15_CA0 end

    def Function_16_EBD(): pass

    label("Function_16_EBD")

    Call(0, 17)
    Return()

    # Function_16_EBD end

    def Function_17_EC1(): pass

    label("Function_17_EC1")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4C")
    OP_AF(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A9")

    label("loc_F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F60")
    Jump("loc_10A9")

    label("loc_F60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1048")

    ChrTalk(
        0xE,
        (
            "Janettaちゃんが、\x01",
            "It seems like it will be funny this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "明日にはスーパーJanettaに\x01",
            "I was born again,\x01",
            "I was saying something I do not know well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wonder what it is, why.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_10A9")

    label("loc_1048")


    ChrTalk(
        0xE,
        (
            "Janettaちゃんが、\x01",
            "It seems like it will be funny this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wonder what it is, why.\x02",
    )

    CloseMessageWindow()

    label("loc_10A9")

    Jump("loc_ECE")

    label("loc_10AE")

    TalkEnd(0xE)
    Return()

    # Function_17_EC1 end

    def Function_18_10B2(): pass

    label("Function_18_10B2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today's sales are as usual\x01",
            "With 20:00\x01",
            "We will end it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not forget or forgotten your purchase\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_10B2 end

    def Function_19_1138(): pass

    label("Function_19_1138")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Clothes are ready, OK,\x01",
            "Nori of makeup is also perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I'm a bit different at tonight's jet\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1138 end

    def Function_20_11A4(): pass

    label("Function_20_11A4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "いい、Ken。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say something to Dad first when you return.\x01",
            "Then hug quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's okay, if you pinch it with two people\x01",
            "Because it is a scary thing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_11A4 end

    def Function_21_1237(): pass

    label("Function_21_1237")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mommy is crazy about shopping\x01",
            "Until like this ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Truly dad's also\x01",
            "I think that I am angry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1237 end

    def Function_22_1296(): pass

    label("Function_22_1296")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Well, I guess I'm about to leave home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "An old lady got angry, it was an enemy.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1296 end

    def Function_23_12E9(): pass

    label("Function_23_12E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique \"Lucca\"\x01",
            "２Ｆ　Hansonシューズ\x01",
            "２Ｆ　アクセサリ《Baker》\x01",
            "１Ｆ　《Regionフード》\x01",
            "１Ｆ　雑貨コーナー《Southwark》\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ If you have any questions\x01",
            "Front comprehensive information at\x01",
            "Please do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_23_12E9 end

    SaveToFile()

Try(main)
