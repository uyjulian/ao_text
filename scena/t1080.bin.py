from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1080.bin",                # FileName
        "t1080",                    # MapName
        "t1080",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1080",                  # 0
        "Citrus",               # 1
        "Zolk",                 # 2
        "Keya",                 # 3
        "Franc",                 # 4
        "Cecil",                 # 5
        "Ilia",                 # 6
        "Lisha",               # 7
        "Shuri",                 # 8
        "Erie",                 # 9
        "Tio",                 # 10
        "Noel",                 # 11
        "Zeit",               # 12
        "Marybele",             # 13
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10000.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
        "chr/ch05202.itc",                   # 0C
        "chr/ch10002.itc",                   # 0D
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

    DeclNpc(106129,  0,       11579,   0,    385,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(4294952456, 0,       6570,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(569,     0,       1809,    135,  389,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294954046, 0,       6540,    1500,    4294952456, 1500,    6570,    0x007E, 0,  17, 0x0000)

    ChipFrameInfo(804, 0)                                        # 0

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_62A",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_899",          # 05, 5
        "Function_6_D2B",          # 06, 6
        "Function_7_129C",         # 07, 7
        "Function_8_151F",         # 08, 8
        "Function_9_16F6",         # 09, 9
        "Function_10_19D7",        # 0A, 10
        "Function_11_1AC7",        # 0B, 11
        "Function_12_1E50",        # 0C, 12
        "Function_13_2025",        # 0D, 13
        "Function_14_21EC",        # 0E, 14
        "Function_15_2319",        # 0F, 15
        "Function_16_24D7",        # 10, 16
        "Function_17_2658",        # 11, 17
        "Function_18_265C",        # 12, 18
        "Function_19_2833",        # 13, 19
        "Function_20_3A24",        # 14, 20
        "Function_21_3A34",        # 15, 21
        "Function_22_3A44",        # 16, 22
        "Function_23_3A54",        # 17, 23
        "Function_24_3A64",        # 18, 24
        "Function_25_3A92",        # 19, 25
        "Function_26_3ACF",        # 1A, 26
        "Function_27_3B0C",        # 1B, 27
        "Function_28_3B49",        # 1C, 28
        "Function_29_3B86",        # 1D, 29
        "Function_30_3BC3",        # 1E, 30
        "Function_31_3C0F",        # 1F, 31
        "Function_32_3C5B",        # 20, 32
        "Function_33_3CA7",        # 21, 33
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_1_3DC")

    label("loc_43C")

    Return()

    # Function_1_3DC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_5F1")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_45E")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4F8")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 5850, 0, 4400, 45)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6560, 0, 5100, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    SetChrFlags(0x11, 0x10)

    label("loc_4A7")

    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 97700, 150, 124100, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4800, 0, 6050, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_506")
    Jump("loc_5F1")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5F1")
    SetChrChipByIndex(0xF, 0xD)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 104060, 500, 118180, 0)
    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 104060, 500, 119880, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 99230, 0, -80380, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100220, 0, -80390, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_59D")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -100940, 0, 121230, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -99810, 0, 121220, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_5DD")

    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_605")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_617")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_617")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 33)

    label("loc_617")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_66(0x0, 0x1)

    label("loc_629")

    Return()

    # Function_2_43D end

    def Function_3_62A(): pass

    label("Function_3_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_63F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_63F")

    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_62A end

    def Function_4_661(): pass

    label("Function_4_661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_672")
    Jump("loc_895")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_680")
    Jump("loc_895")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_895")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_895")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    Call(0, 15)
    Jump("loc_701")

    label("loc_6B7")


    ChrTalk(
        0xF,
        (
            "#04205FWhat, suddenly ……\x02\x03",
            "#04206FI said something bad, did not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701")

    Jump("loc_895")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_714")
    Jump("loc_895")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72F")
    Call(0, 6)
    Jump("loc_895")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845")

    ChrTalk(
        0xF,
        (
            "#04206FHa, I can not swim\x01",
            "It is the first time I was born.\x02\x03",
            "#04208FLisha姉が教えてくれるけど、\x01",
            "What should I do if I get drowned …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FI do not want to worry about such things\x01",
            "It is cute and there is this,\x01",
            "Shuriぞう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04201FOh, already!\x01",
            "Shuriぞうでいいから\x01",
            "Oh no!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_895")

    label("loc_845")


    ChrTalk(
        0xF,
        (
            "#04206F泳ぐなんてIt is the first time I was born.\x02\x03",
            "#04208FWhat should I do if I get drowned …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_895")

    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_899(): pass

    label("Function_5_899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8AA")
    Jump("loc_D27")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8B8")
    Jump("loc_D27")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8C6")
    Jump("loc_D27")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_8DE")

    label("loc_8DE")

    Jump("loc_D27")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F")

    ChrTalk(
        0xE,
        "#01802FAh …… Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fあれ、Lisha。\x01",
            "Have you been in the room yet?\x02\x03",
            "#00000FErieたちと一緒に\x01",
            "When I went to a boutique\x01",
            "I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01809FHaha, somehow on the beach\x01",
            "It looks like I'm tired from playing.\x02\x03",
            "#01802FAfter a while resting\x01",
            "I am going to go also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FReally……\x02\x03",
            "#00002FWell, at the theme park\x01",
            "I have time to wait,\x01",
            "Do not push yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01809FYes, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B12")

    label("loc_A9F")


    ChrTalk(
        0xE,
        (
            "#01800FKeyaちゃんなら、\x01",
            "I have not come here.\x02\x03",
            "Maybe from the hotel\x01",
            "It may have come out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12")

    Jump("loc_D27")

    label("loc_B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B25")
    Jump("loc_D27")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    Call(0, 6)
    Jump("loc_D27")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(
        0xE,
        (
            "#01803FIn truth, I'm an inexperienced person like me\x01",
            "I do not have time for playing ….\x02\x03",
            "#01802FIt is important to rest for artists,\x01",
            "Iliaさんに説得されてしまって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIliaさんの言うことももっともだよ。\x02\x03",
            "#00000Fせっかくの機会だし、Lishaも\x01",
            "I wish I could change my mood full of eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01800FHehe … …. Yes, I will do so.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D27")

    label("loc_C9A")


    ChrTalk(
        0xE,
        (
            "#01804FFirst from the basic swimming method\x01",
            "You had better tell me in turn.\x02\x03",
            "#01803FEven if I remember it, afterwards\x01",
            "Shuriちゃんのセンスで\x01",
            "I think that it will manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")

    TalkEnd(0xFE)
    Return()

    # Function_5_899 end

    def Function_6_D2B(): pass

    label("Function_6_D2B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBC")
    Jump("loc_E06")

    label("loc_DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DDC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DFC")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBC")
    Jump("loc_F06")

    label("loc_EBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EDC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F06")

    label("loc_EDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F06")

    label("loc_EFC")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F06")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xE,
        "#01802FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHere is unpacking\x01",
            "It looks like it ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802FYes, I see. ….\x02\x03",
            "#01809FShuriちゃんが今日、\x01",
            "It seems to be playing for the first time in the water\x01",
            "It seems a bit nervous.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#04211Fちょ、ちょっとLisha姉っ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, because I hid it\x01",
            "It does not matter what happens,\x01",
            "Shuriぞう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04205Fシュ、Shuriぞうって……\x01",
            "I do not have to call HEN suddenly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, is not it nice?\x01",
            "Tioすけ、ヨナ公、キー坊ときたら\x01",
            "次はやっぱりShuriぞうだろ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04206FThen, you know!\x01",
            "Right? Well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, if you can not swim\x01",
            "She takes a takeaway\x01",
            "You can tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802Fうん、それにShuriちゃんなら\x01",
            "I think it will be too early to remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04203FFufun, I know that.\x02\x03",
            "#04208FHowever, that is, preparation of various hearts … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, well if I am ready\x01",
            "Lishaと一緒に来るといいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x15A, 4)
    Return()

    # Function_6_D2B end

    def Function_7_129C(): pass

    label("Function_7_129C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_12AD")
    Jump("loc_151B")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12BB")
    Jump("loc_151B")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_12C9")
    Jump("loc_151B")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_12D7")
    Jump("loc_151B")

    label("loc_12D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12E5")
    Jump("loc_151B")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_12F3")
    Jump("loc_151B")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130E")
    Call(0, 9)
    Jump("loc_151B")

    label("loc_130E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")

    ChrTalk(
        0xD,
        (
            "#01704FEarlier, since I saw it in a foreign magazine\x01",
            "Playing on the beach plainly\x01",
            "It was a dream, was not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F個人的には、Iliaさんたちの\x01",
            "Looking at swimsuits is fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FOh, at the reception of a lake bath\x01",
            "You are renting a bathing suit.\x02\x03",
            "#01709FWell, after that\x01",
            "Super cool doing loud and sexy\x01",
            "I will pick you!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909Fふふ、Iliaったら。\x01",
            "Do it in moderation?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_151B")

    label("loc_1480")


    ChrTalk(
        0xD,
        (
            "#01709FPlease look forward to it.\x01",
            "Super cool doing loud and sexy swimwear\x01",
            "I will choose!\x02\x03",
            "#01702FThen, please prepare quickly\x01",
            "Let's go to the beach wish go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151B")

    TalkEnd(0xFE)
    Return()

    # Function_7_129C end

    def Function_8_151F(): pass

    label("Function_8_151F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1530")
    Jump("loc_16F2")

    label("loc_1530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_153E")
    Jump("loc_16F2")

    label("loc_153E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_154C")
    Jump("loc_16F2")

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_155A")
    Jump("loc_16F2")

    label("loc_155A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1568")
    Jump("loc_16F2")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1576")
    Jump("loc_16F2")

    label("loc_1576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1591")
    Call(0, 9)
    Jump("loc_16F2")

    label("loc_1591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167A")

    ChrTalk(
        0xC,
        (
            "#05900FOh, Lloyd.\x01",
            "Have you finished preparing soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, in a word.\x02\x03",
            "#00004F先に行ってるから、Cecil姉たちは\x01",
            "You may come slowly later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05902FHehu, I understand.\x01",
            "I'm going to be as late as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_16F2")

    label("loc_167A")


    ChrTalk(
        0xC,
        (
            "#05904FIliaったら本当に\x01",
            "It is as usual.\x02\x03",
            "#05902FHuhu, people of alkane shell\x01",
            "I guess you have a hard time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F2")

    TalkEnd(0xFE)
    Return()

    # Function_8_151F end

    def Function_9_16F6(): pass

    label("Function_9_16F6")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909FEven so,\x01",
            "Iliaとお泊りなんて\x01",
            "Ever since I was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FOh, that's right.\x02\x03",
            "#01704FSince I became busy with practice too\x01",
            "I could hardly go and see them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01709FYes, today is a long time\x01",
            "Can you even enter a bath together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05905FYeah, I do not mind … …\x02\x03",
            "#05903FWith the bus in the room\x01",
            "Two adults are not narrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FWell, that's not good.\x02\x03",
            "#01709FGrowth for several years, firmly with this hand\x01",
            "We have to make sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05909Fふふ、Iliaったら\x01",
            "It is as usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x101)

    ChrTalk(
        0x104,
        (
            "#00306F(Muu ……\x01",
            "  Iliaさんのポジションが\x01",
            "I am envious to enormous. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, hmm … ….\x01",
            "  Cecil姉は無防備だしなあ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_16F6 end

    def Function_10_19D7(): pass

    label("Function_10_19D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_19E8")
    Jump("loc_1AC3")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19F6")
    Jump("loc_1AC3")

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A04")
    Jump("loc_1AC3")

    label("loc_1A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1A14")
    Jump("loc_1AC3")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1A22")
    Jump("loc_1AC3")

    label("loc_1A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A30")
    Jump("loc_1AC3")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1A3E")
    Jump("loc_1AC3")

    label("loc_1A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A59")
    Call(0, 12)
    Jump("loc_1AC3")

    label("loc_1A59")


    ChrTalk(
        0xB,
        (
            "#06401FIf you are older sister,\x01",
            "It is a terrible complaint, is not it ~.\x02\x03",
            "#06406FEven this, too\x01",
            "I wish I were a policeman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    TalkEnd(0xFE)
    Return()

    # Function_10_19D7 end

    def Function_11_1AC7(): pass

    label("Function_11_1AC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1AD8")
    Jump("loc_1E4C")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1AE6")
    Jump("loc_1E4C")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1AF4")
    Jump("loc_1E4C")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1B04")
    Jump("loc_1E4C")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1B12")
    Jump("loc_1E4C")

    label("loc_1B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D06")

    ChrTalk(
        0x12,
        (
            "#10103FWell, I\x01",
            "Let's meet until the meeting time.\x02\x03",
            "#10108FFrancと一緒にブティックに行っても\x01",
            "It was good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs that also a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10111FWell, actually, that … …\x02\x03",
            "#10109Fビーチで見たCecilさんたちの\x01",
            "To a proportion, a bit\x01",
            "I felt a sense of defeat.\x02\x03",
            "#10106FChoose clothes in front of them\x01",
            "To try on and on,\x01",
            "I do not feel like going … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No,\x01",
            "I think that I think too much ….\x01",
            "Is it possible that there are females? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1DAD")

    label("loc_1D06")


    ChrTalk(
        0x12,
        (
            "#10106FCecilさんたちの前で\x01",
            "服を選んだりTo try on and on,\x01",
            "I do not feel like going on ……\x02\x03",
            "#10100FI will have Randy senior later\x01",
            "I will go even to a jewelry store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAD")

    Jump("loc_1E4C")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1DC0")
    Jump("loc_1E4C")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDB")
    Call(0, 12)
    Jump("loc_1E3E")

    label("loc_1DDB")


    ChrTalk(
        0x12,
        (
            "#10106FHaa, it feels like I've been eaten.\x02\x03",
            "#10101FこのあたしがFrancなんかに\x01",
            "I will be deceived …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3E")

    Jump("loc_1E4C")

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1E4C")

    label("loc_1E4C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1AC7 end

    def Function_12_1E50(): pass

    label("Function_12_1E50")

    OP_4B(0x12, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x12,
        (
            "#10101Fもう、Francったら……\x01",
            "I do not feel like coming yesterday\x01",
            "You did not show it at all.\x02\x03",
            "#10106F\"I will go if there is no work\"\x01",
            "\"My sister is envious\" ~\x01",
            "Say it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#06402FEr, sorry ~.\x01",
            "The invitation itself is with her older sister\x01",
            "I received it around the same time ….\x02\x03",
            "#06409FMarybeleさんから\x01",
            "As it is silent till the day\x01",
            "I was being held out of my mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10106FHa, this is me\x01",
            "Francなんかに騙されるなんて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#06405FOh, you terrible ~ Iio!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_12_1E50 end

    def Function_13_2025(): pass

    label("Function_13_2025")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2036")
    Jump("loc_21E8")

    label("loc_2036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2044")
    Jump("loc_21E8")

    label("loc_2044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_21E8")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2060")
    Jump("loc_21E8")

    label("loc_2060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_208F")

    ChrTalk(
        0x13,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E8")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_21E8")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_21DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B9")

    ChrTalk(
        0x13,
        "#01200F… …. Gurrule …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FZeit、ここにいたのか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHahahaha, a journey by water bus\x01",
            "A bit tired?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01203F……won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FIt seems not to be so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fまあ、Zeitも後で\x01",
            "I will come to the beach\x01",
            "Leave it alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21DA")

    label("loc_21B9")


    ChrTalk(
        0x13,
        "#01200F… …. Gurrule …………\x02",
    )

    CloseMessageWindow()

    label("loc_21DA")

    Jump("loc_21E8")

    label("loc_21DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_21E8")

    label("loc_21E8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2025 end

    def Function_14_21EC(): pass

    label("Function_14_21EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_21FD")
    Jump("loc_2315")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_220B")
    Jump("loc_2315")

    label("loc_220B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2219")
    Jump("loc_2315")

    label("loc_2219")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2229")
    Jump("loc_2315")

    label("loc_2229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2237")
    Jump("loc_2315")

    label("loc_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2252")
    Call(0, 15)
    Jump("loc_22EB")

    label("loc_2252")


    ChrTalk(
        0x11,
        (
            "#00203FWithout knowing Michishi\x01",
            "Let's go to a theme park,\x01",
            "It is a good place to blame.\x02\x03",
            "#00201FどうやらShuriさんには\x01",
            "It seems necessary to have a thorough education …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_2315")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_22FE")
    Jump("loc_2315")

    label("loc_22FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_230C")
    Jump("loc_2315")

    label("loc_230C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2315")

    label("loc_2315")

    TalkEnd(0xFE)
    Return()

    # Function_14_21EC end

    def Function_15_2319(): pass

    label("Function_15_2319")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        "#04205FWhy do you have that machine …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#00204FYeah, it's a Mitsushi strap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FOh, I heard this in a story\x01",
            "\"Missi\" is a guy.\x02\x03",
            "#04204FBy the way it may have been the first time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#00205F……The first time I saw?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FOh, I've often heard of your name\x01",
            "I did not know that it was such a monkey.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00203F……どうやらShuriさんには\x01",
            "I think it is necessary to have a thorough education.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_15_2319 end

    def Function_16_24D7(): pass

    label("Function_16_24D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_24E8")
    Jump("loc_2654")

    label("loc_24E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_24F6")
    Jump("loc_2654")

    label("loc_24F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D1")

    ChrTalk(
        0xFE,
        (
            "Today, the VIP floor is\x01",
            "It is private for all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition, various room services\x01",
            "Marybele様のご厚意で\x01",
            "It is provided free of charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do not hesitate to ask\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2654")

    label("loc_25D1")


    ChrTalk(
        0xFE,
        (
            "Various room service\x01",
            "Marybele様のご厚意で\x01",
            "It is provided free of charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do not hesitate to ask\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2654")

    TalkEnd(0xFE)
    Return()

    # Function_16_24D7 end

    def Function_17_2658(): pass

    label("Function_17_2658")

    Call(0, 18)
    Return()

    # Function_17_2658 end

    def Function_18_265C(): pass

    label("Function_18_265C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_266D")
    Jump("loc_282F")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(
        0x9,
        (
            "Everyone, at the beach\x01",
            "How was everything going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On the day I was off,\x01",
            "Sunbathing on the beach etc\x01",
            "I am enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, in the near future\x01",
            "I will not go back again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2793")

    label("loc_2726")


    ChrTalk(
        0x9,
        (
            "On the day I was off,\x01",
            "Sunbathing on the beach etc\x01",
            "I am enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, in the near future\x01",
            "I will not go back again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2793")

    Jump("loc_282F")

    label("loc_2798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_282F")

    ChrTalk(
        0x9,
        (
            "This is for the VIP floor only\x01",
            "It is a bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Various cocktails, soft drinks etc.\x01",
            "We are preparing, so please feel free to contact us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282F")

    TalkEnd(0x9)
    Return()

    # Function_18_265C end

    def Function_19_2833(): pass

    label("Function_19_2833")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    SoundLoad(3801)
    SoundLoad(3771)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0xD, 9970, 0, 11960, 90)
    SetChrPos(0xC, 8910, 0, 12550, 90)
    SetChrPos(0xE, 8960, 0, 11180, 90)
    SetChrPos(0xF, 7880, 0, 11840, 90)
    SetChrPos(0x14, 1690, 0, 5920, 270)
    SetChrPos(0x109, 2590, 0, 7310, 225)
    SetChrPos(0xB, 3500, 0, 5840, 225)
    SetChrPos(0x102, 4019, 0, 7340, 225)
    SetChrPos(0x103, 4150, 0, 8660, 225)
    SetChrPos(0xA, 5460, 0, 7210, 225)
    SetChrPos(0x101, 5510, 0, 8830, 180)
    SetChrPos(0x104, 6640, 0, 9950, 180)
    SetChrPos(0x105, 5200, 0, 10210, 180)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    OP_68(7450, 1700, 8400, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(27000, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0xD, 3, 0, 20)
    BeginChrThread(0xC, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 22)
    BeginChrThread(0xF, 3, 0, 23)
    BeginChrThread(0x14, 3, 0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    BeginChrThread(0xB, 3, 0, 26)
    BeginChrThread(0x102, 3, 0, 27)
    BeginChrThread(0x103, 3, 0, 28)
    BeginChrThread(0xA, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 30)
    BeginChrThread(0x105, 3, 0, 31)
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(200)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(4000)
    OP_0D()
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0x104, 0x3)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    Sound(121, 0, 100, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2B2D")
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x14,
        "#02902F#3801V#30WThis is your room.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xED9)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Jump("loc_2B6B")

    label("loc_2B2D")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x14,
        "#02902FThis is your room.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2B6B")

    OP_68(-100000, 1000, -81500, 0)
    MoveCamera(318, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x14, -100000, 0, -78000, 180)
    SetChrPos(0x101, -100000, 0, -80300, 180)
    SetChrPos(0x104, -99000, 0, -80000, 180)
    SetChrPos(0x105, -101000, 0, -80100, 180)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x5)
    FadeToBright(1000, 0)
    OP_68(-100000, 1000, -79000, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#11PThis is amazing …\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        "#00309F#5PYou are too loud, are not you?\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10302F#11PWe also have the number of beds according to us\x01",
            "It seems they adjusted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PUfufu, if it is a luxury hotel\x01",
            "It's a natural service.\x02\x03",
            "#02901FWell, regarding this room\x01",
            "Like a key from outside\x01",
            "I wanted to do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2D76():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D76)
    Sleep(50)

    def lambda_2D86():
        TurnDirection(0x104, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D86)
    Sleep(50)

    def lambda_2D96():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D96)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00012F#6PWell, that is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#6PI do not believe such a trust.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PHuh, I'm outgoing.\x02\x03",
            "#10302FEveryone except us,\x01",
            "Because it is beautiful women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02906F#11PWell, as for Wasan\x01",
            "It seems to be somehow trustworthy though.\x02\x03",
            "#02913FLloyd and Randy\x01",
            "To be honest, I can not trust him.\x02\x03",
            "#02901F…… especially Lloyd's\x01",
            "It is a dangerous person with caution needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#6PHuh, because it's all about you\x01",
            "Suddenly I went out to the lounge at midnight\x01",
            "There is a girl who can not sleep … ….\x02\x03",
            "#10302FWhile talking with that\x01",
            "It is likely to be a good atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6POh, it seems to be quite likely.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#02909F#11P…… Lloyd.\x01",
            "About a sleeping room for employees\x01",
            "Will you stay overnight?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    ChrTalk(
        0x101,
        "#00012F#6PNo, not from there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02906F#11PHuh, absolutely.\x02\x03",
            "#02904FBy the way, I\x01",
            "After this, we have a board of directors\x01",
            "Once I get back to the city … …\x02\x03",
            "くれぐれも、水着姿のErieたちに\x01",
            "Please be careful not to be inferior.\x02\x03",
            "#02901F…… If you do evil, call the security department\x01",
            "I will pound you in the middle of the lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's why I will not ……\x02\x03",
            "#00001F……でも、Marybeleさん、\x01",
            "You are quite busy after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PHuh, your father like that\x01",
            "Because I have said it.\x02\x03",
            "#02902FIndeed the IBC business\x01",
            "It seems to be difficult to parallel\x01",
            "All of them were taken over by the Board of Directors.\x02\x03",
            "Of course I\x01",
            "It is a translation that wrinkle pulls are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PIs that so……\x01",
            "I'm really thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PWell, appropriately\x01",
            "Please also take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#6PRest and relieve stress\x01",
            "It is also good for beauty and health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PThank you for your consideration.\x02\x03",
            "#02900FAs I reported, the reception of the lake bath\x01",
            "It is on the right side of the 1F arcade.\x02\x03",
            "You can rent a swimsuit there\x01",
            "Please change clothes in the changing room.\x02\x03",
            "#02901F…… Of course the boys are right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PNo, I do not care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PAnyway, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PLake bath area for you\x01",
            "I will rent it until noon.\x02\x03",
            "From the afternoon at the theme park\x01",
            "It would be nice to have fun.\x02\x03",
            "#02902FPeople who have been there also\x01",
            "I will leave it because it will be many.\x02\x03",
            "#02909FAnd at night, at the guest house\x01",
            "We have seats for dinner.\x02\x03",
            "There is no necessity of dressing up\x01",
            "Please come by time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PIn full glory\x01",
            "I am sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#02904F#11PHuh, how are you?\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_36F2")
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x14,
        (
            "#02911F#3771V#5P#40W── Stay a good stay#10R噵 噵 噵 噵 噵#.\x01",
            "Please extend your wing to its full capacity.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEBB)
    OP_C9(0x1, 0x80000000)
    Jump("loc_372F")

    label("loc_36F2")


    ChrTalk(
        0x14,
        (
            "#02902F#5P── Stay a good stay.\x01",
            "Please extend your wing to its full capacity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372F")

    OP_57(0x0)
    OP_5A()

    def lambda_3737():

        label("loc_3737")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3737")

    QueueWorkItem2(0x101, 2, lambda_3737)

    def lambda_3749():

        label("loc_3749")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3749")

    QueueWorkItem2(0x104, 2, lambda_3749)

    def lambda_375B():

        label("loc_375B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_375B")

    QueueWorkItem2(0x105, 2, lambda_375B)

    def lambda_376D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_376D)
    Sleep(1000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x14, 1)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_68(-100000, 1000, -80000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#6P… … what are you saying?\x01",
            "He is a very kind person.\x02\x03",
            "#00006FIt is strangely hostile to me\x01",
            "I want you to forgive … ….\x02",
        )
    )

    CloseMessageWindow()

    def lambda_384C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_384C)
    Sleep(50)

    def lambda_385C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_385C)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00304F#12PWait, give up as you think destiny.\x02\x03",
            "#00302FWell then,\x01",
            "Would you go to the beach ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHuh, that's right.\x02\x03",
            "#10300FThe female team absolutely preparations\x01",
            "It will take time …\x02\x03",
            "You can go ahead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PThat's right.\x02\x03",
            "#00000FWell then,\x01",
            "I wish to call out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_49()
    OP_D7(0x24)
    SetMapObjFlags(0x0, 0x10)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    SetScenarioFlags(0x144, 5)
    OP_29(0xA5, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_19_2833 end

    def Function_20_3A24(): pass

    label("Function_20_3A24")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_20_3A24 end

    def Function_21_3A34(): pass

    label("Function_21_3A34")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_21_3A34 end

    def Function_22_3A44(): pass

    label("Function_22_3A44")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_3A44 end

    def Function_23_3A54(): pass

    label("Function_23_3A54")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_3A54 end

    def Function_24_3A64(): pass

    label("Function_24_3A64")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_3A64 end

    def Function_25_3A92(): pass

    label("Function_25_3A92")

    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_3A92 end

    def Function_26_3ACF(): pass

    label("Function_26_3ACF")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_3ACF end

    def Function_27_3B0C(): pass

    label("Function_27_3B0C")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xED8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_27_3B0C end

    def Function_28_3B49(): pass

    label("Function_28_3B49")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_28_3B49 end

    def Function_29_3B86(): pass

    label("Function_29_3B86")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_29_3B86 end

    def Function_30_3BC3(): pass

    label("Function_30_3BC3")

    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x14B4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_30_3BC3 end

    def Function_31_3C0F(): pass

    label("Function_31_3C0F")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_31_3C0F end

    def Function_32_3C5B(): pass

    label("Function_32_3C5B")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_32_3C5B end

    def Function_33_3CA7(): pass

    label("Function_33_3CA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3396)
    SetChrPos(0x101, -100500, 0, -80500, 90)
    SetChrPos(0x104, -99000, 0, -81000, 270)
    SetChrPos(0x105, -101000, 0, -85000, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -100000, 0, -74900, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Erieの声")

    AnonymousTalk(
        0xFF,
        "#3396V#30WI am sorry, a little nice?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD44)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7565", "ed7111")
    OP_68(-100000, 1000, -78300, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 1500)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)

    def lambda_3E15():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E15)
    Sleep(50)

    def lambda_3E25():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E25)
    OP_79(0x7)
    OP_68(-100000, 1000, -79300, 2000)

    def lambda_3E46():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E46)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#6Pああ、Erieか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#6PAre you already here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00102F#11Pええ、Iliaさんたちに誘われて\x01",
            "From looking into the shop to the theme park\x01",
            "I'm going to go …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#00105F#11Pその、Keyaちゃん、\x01",
            "Did not you visit here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PKeyaが？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#6PWhat, what happened to the keebou?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11PThat is it, just a minute ago\x01",
            "\"Going to Lloyd's place\"\x01",
            "I went out of the room ….\x02\x03",
            "#00108FWell, I wonder where I went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PIs it so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PTioすけかZeitと\x01",
            "Is not he with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F#11PWell, maybe.\x02\x03",
            "#00102FI'm sorry.\x01",
            "I will search a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, I waited for a moment.\x02\x03",
            "#00000FIliaさんたちを\x01",
            "I guess he's waiting?\x02\x03",
            "Keyaは俺が探しておくから\x01",
            "Erieはそっちに行ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00105F#11PErr, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PずっとErieたちに\x01",
            "It is bad that you are left behind.\x02\x03",
            "#00002FI found it properly\x01",
            "I will take you to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11PWell.\x01",
            "Then you gotta ask me.\x02\x03",
            "#00108F…… Huh.\x01",
            "Keyaちゃんにも新しい服を\x01",
            "I wanted to see you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)

    def lambda_4299():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4299)
    Sleep(1000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x80)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_68(-100000, 1000, -80000, 1500)
    OP_6F(0x79)
    OP_93(0x104, 0x10E, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00309F#12PHahaha, key people also\x01",
            "It's as usual as ever.\x02\x03",
            "#00300FSoon, why do not you look for it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, I alone is enough.\x02\x03",
            "Randy also has a shop\x01",
            "You said you wanted to peep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12PReally?\x02\x03",
            "#00304FThen, I am in the lower jewelry store\x01",
            "Please call out if there is something.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_END)), "loc_443B")

    ChrTalk(
        0x101,
        "#00002F#5POh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_443B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_455D")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWhat is a jewelry store …?\x01",
            "Today only for members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12POh, whatever.\x01",
            "Marybeleお嬢さんの口利きで\x01",
            "She seems to put in even us?\x02\x03",
            "#00304FThe clerk is subtlely unlucky\x01",
            "I'm curious about the assortment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, I understand.\x01",
            "(Shall we take a look?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_455D")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWhat is a jewelry store …?\x01",
            "Is it in the lower arcade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12POh, whatever.\x01",
            "Marybeleお嬢さんの口利きで\x01",
            "She seems to put in even us?\x02\x03",
            "#00304FIt has stopped as high as possible\x01",
            "I'm curious about the assortment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, I understand.\x01",
            "(Shall we take a look?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4675")

    OP_68(-100000, 1000, -78500, 5000)

    def lambda_468B():

        label("loc_468B")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_468B")

    QueueWorkItem2(0x101, 2, lambda_468B)
    OP_93(0x104, 0x0, 0x1F4)

    def lambda_46A4():
        OP_95(0xFE, -100000, 0, -76900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46A4)
    WaitChrThread(0x104, 1)
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_93(0x104, 0x0, 0x0)

    def lambda_46E2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46E2)
    Sleep(500)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6Pさてと、Keyaを探すか。\x02\x03",
            "#00008FProbably, from the hotel\x01",
            "I think that it has not come out ….\x02\x03",
            "#00001FIf not found,\x01",
            "I need to look for other places as well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    ClearChrFlags(0x105, 0x8)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetScenarioFlags(0x145, 1)
    OP_29(0xA5, 0x1, 0x4)
    SubItemNumber('纯白之石', 10)
    SubItemNumber('纯白之石', 10)
    SubItemNumber('纯白之石', 10)
    EventEnd(0x5)
    Return()

    # Function_33_3CA7 end

    SaveToFile()

Try(main)
