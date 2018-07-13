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
        "Function_6_69F",          # 06, 6
        "Function_7_6A3",          # 07, 7
        "Function_8_7DE",          # 08, 8
        "Function_9_7E2",          # 09, 9
        "Function_10_B46",         # 0A, 10
        "Function_11_B4A",         # 0B, 11
        "Function_12_C93",         # 0C, 12
        "Function_13_C97",         # 0D, 13
        "Function_14_DAE",         # 0E, 14
        "Function_15_DB2",         # 0F, 15
        "Function_16_FCB",         # 10, 16
        "Function_17_FCF",         # 11, 17
        "Function_18_1207",        # 12, 18
        "Function_19_1295",        # 13, 19
        "Function_20_1316",        # 14, 20
        "Function_21_13E4",        # 15, 21
        "Function_22_145C",        # 16, 22
        "Function_23_14B7",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_644")

    ChrTalk(
        0x8,
        (
            "Today, after we finish work,\x01",
            "I'm going to eat with senior\x01",
            "Cynthia and Jeanetta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party in a long time... \x01",
            "Uh uh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_69B")

    label("loc_644")


    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party in a long time... \x01",
            "Uh uh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B")

    TalkEnd(0x8)
    Return()

    # Function_5_583 end

    def Function_6_69F(): pass

    label("Function_6_69F")

    Call(0, 7)
    Return()

    # Function_6_69F end

    def Function_7_6A3(): pass

    label("Function_7_6A3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(
        0x9,
        (
            "Today Miss Jeanetta is \x01",
            "really in high spirits. Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not that going to dinner us\x01",
            "three together is the first time...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7DA")

    label("loc_773")


    ChrTalk(
        0x9,
        (
            "It's not that going to dinner us\x01",
            "three together is the first time...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DA")

    TalkEnd(0x9)
    Return()

    # Function_7_6A3 end

    def Function_8_7DE(): pass

    label("Function_8_7DE")

    Call(0, 9)
    Return()

    # Function_8_7DE end

    def Function_9_7E2(): pass

    label("Function_9_7E2")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_83F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_85E")
    OP_AF(0x26)
    Jump("loc_880")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_86E")
    OP_AF(0x25)
    Jump("loc_880")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87E")
    OP_AF(0x24)
    Jump("loc_880")

    label("loc_87E")

    OP_AF(0x23)

    label("loc_880")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B3D")

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3")
    Jump("loc_B3D")

    label("loc_8A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A31")

    ChrTalk(
        0xA,
        (
            "Everyone, do you know that it would be best\x01",
            "to go choose shoes on or after evening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is because, after we wake up in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they could even be about 1 rege bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is regarded best to choose your size\x01",
            "on or after evening, when feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B3D")

    label("loc_A31")


    ChrTalk(
        0xA,
        (
            "The truth is that, after we wake up in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they could even be about 1 rege bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is regarded best to choose your size\x01",
            "on or after evening, when feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3D")

    Jump("loc_7EF")

    label("loc_B42")

    TalkEnd(0xA)
    Return()

    # Function_9_7E2 end

    def Function_10_B46(): pass

    label("Function_10_B46")

    Call(0, 11)
    Return()

    # Function_10_B46 end

    def Function_11_B4A(): pass

    label("Function_11_B4A")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC7")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8A")

    label("loc_BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDB")
    Jump("loc_C8A")

    label("loc_BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        (
            "Good evening, welcome\x01",
            "to "Region Food".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you haven't prepared dinner yet,\x01",
            "by all means please come to buy\x01",
            "your ingredients from us, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8A")

    Jump("loc_B57")

    label("loc_C8F")

    TalkEnd(0xB)
    Return()

    # Function_11_B4A end

    def Function_12_C93(): pass

    label("Function_12_C93")

    Call(0, 13)
    Return()

    # Function_12_C93 end

    def Function_13_C97(): pass

    label("Function_13_C97")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D13")
    OP_AF(0x21)
    Jump("loc_D35")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D23")
    OP_AF(0x20)
    Jump("loc_D35")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D33")
    OP_AF(0x1F)
    Jump("loc_D35")

    label("loc_D33")

    OP_AF(0x1E)

    label("loc_D35")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA5")

    label("loc_D44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D58")
    Jump("loc_DA5")

    label("loc_D58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xC,
        (
            "Welcome, please\x01",
            "enjoy shopping\x01",
            "in the evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA5")

    Jump("loc_CA4")

    label("loc_DAA")

    TalkEnd(0xC)
    Return()

    # Function_13_C97 end

    def Function_14_DAE(): pass

    label("Function_14_DAE")

    Call(0, 15)
    Return()

    # Function_14_DAE end

    def Function_15_DB2(): pass

    label("Function_15_DB2")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E2E")
    OP_AF(0x11)
    Jump("loc_E40")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E3E")
    OP_AF(0x10)
    Jump("loc_E40")

    label("loc_E3E")

    OP_AF(0xF)

    label("loc_E40")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC2")

    label("loc_E4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E63")
    Jump("loc_FC2")

    label("loc_E63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F34")

    ChrTalk(
        0xD,
        "It's already dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's right, the Arc-en-ciel's\x01",
            "performance for the heads of\x01",
            "state should ending soon.\x02",
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
    Jump("loc_FC2")

    label("loc_F34")


    ChrTalk(
        0xD,
        (
            "That's right, the Arc-en-ciel's\x01",
            "performance for the heads of\x01",
            "state should ending soon.\x02",
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

    label("loc_FC2")

    Jump("loc_DBF")

    label("loc_FC7")

    TalkEnd(0xD)
    Return()

    # Function_15_DB2 end

    def Function_16_FCB(): pass

    label("Function_16_FCB")

    Call(0, 17)
    Return()

    # Function_16_FCB end

    def Function_17_FCF(): pass

    label("Function_17_FCF")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1203")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_102C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104C")
    OP_AF(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11FE")

    label("loc_104C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1060")
    Jump("loc_11FE")

    label("loc_1060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1184")

    ChrTalk(
        0xE,
        (
            "Miss Jeanetta looks to be really\x01",
            "happy since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She was saying something I didn't\x01",
            "understand, like that tomorrow she's going\x01",
            "to make a fresh start as "super Jeanetta"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I don't know but for some reason I'm really worried.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_11FE")

    label("loc_1184")


    ChrTalk(
        0xE,
        (
            "Miss Jeanetta looks to be really\x01",
            "happy since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I don't know but for some reason I'm really worried.\x02",
    )

    CloseMessageWindow()

    label("loc_11FE")

    Jump("loc_FDC")

    label("loc_1203")

    TalkEnd(0xE)
    Return()

    # Function_17_FCF end

    def Function_18_1207(): pass

    label("Function_18_1207")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Like usual, today's\x01",
            "operating hours\x01",
            "end at 8:00.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please pay attention to not forget what\x01",
            "you bought and your own belongings.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1207 end

    def Function_19_1295(): pass

    label("Function_19_1295")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The clothes are ready and the\x01",
            "makeup condition is perfect too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm going to be a bit different tonight㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1295 end

    def Function_20_1316(): pass

    label("Function_20_1316")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Listen, Ken.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as we go back, first we tell papa we're sorry.\x01",
            "Then, let's hug him without a moment of delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine, if we both sandwich him,\x01",
            "there won't be anything to fear.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_1316 end

    def Function_21_13E4(): pass

    label("Function_21_13E4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Because mama was absorbed into\x01",
            "her shopping, it's this late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that papa is\x01",
            "going to be angry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_13E4 end

    def Function_22_145C(): pass

    label("Function_22_145C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Well then, time to go back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd be no match for my angered old lady.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_145C end

    def Function_23_14B7(): pass

    label("Function_23_14B7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique "Lucca"\x01",
            "2F Hanson Shoes\x01",
            "2F Accessory "Baker"\x01",
            "1F "Region Food"\x01",
            "1F General Corner "Southwark"\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you have any questions,\x01",
            "please enquire freely at the\x01",
            "front office information.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_23_14B7 end

    SaveToFile()

Try(main)
