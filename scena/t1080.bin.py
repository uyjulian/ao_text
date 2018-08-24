from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Citrus",                 # 1
        "Zork",                   # 2
        "KeA",                    # 3
        "Fran",                   # 4
        "Cecil",                  # 5
        "Ilya",                   # 6
        "Rixia",                  # 7
        "Sully",                  # 8
        "Elie",                   # 9
        "Tio",                    # 10
        "Noｱl",                  # 11
        "Zeit",                   # 12
        "Mariabell",              # 13
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
        "Function_5_8B2",          # 05, 5
        "Function_6_D38",          # 06, 6
        "Function_7_12C8",         # 07, 7
        "Function_8_1592",         # 08, 8
        "Function_9_1773",         # 09, 9
        "Function_10_1A6E",        # 0A, 10
        "Function_11_1B54",        # 0B, 11
        "Function_12_1EE0",        # 0C, 12
        "Function_13_2089",        # 0D, 13
        "Function_14_2258",        # 0E, 14
        "Function_15_2381",        # 0F, 15
        "Function_16_2552",        # 10, 16
        "Function_17_2716",        # 11, 17
        "Function_18_271A",        # 12, 18
        "Function_19_28CF",        # 13, 19
        "Function_20_3C5E",        # 14, 20
        "Function_21_3C6E",        # 15, 21
        "Function_22_3C7E",        # 16, 22
        "Function_23_3C8E",        # 17, 23
        "Function_24_3C9E",        # 18, 24
        "Function_25_3CCC",        # 19, 25
        "Function_26_3D09",        # 1A, 26
        "Function_27_3D46",        # 1B, 27
        "Function_28_3D83",        # 1C, 28
        "Function_29_3DC0",        # 1D, 29
        "Function_30_3DFD",        # 1E, 30
        "Function_31_3E49",        # 1F, 31
        "Function_32_3E95",        # 20, 32
        "Function_33_3EE1",        # 21, 33
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
    Jump("loc_8AE")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_680")
    Jump("loc_8AE")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_8AE")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_8AE")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    Call(0, 15)
    Jump("loc_70C")

    label("loc_6B7")


    ChrTalk(
        0xF,
        (
            "#04205FW-What do you want all\x01",
            "of a sudden...\x02\x03",
            "#04206FDid I say something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C")

    Jump("loc_8AE")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_71F")
    Jump("loc_8AE")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A")
    Call(0, 6)
    Jump("loc_8AE")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85E")

    ChrTalk(
        0xF,
        (
            "#04206F*sigh*, I'll be swimming\x01",
            "for the first time in my\x01",
            "life.\x02\x03",
            "#04208FRixia is teaching me,\x01",
            "but what if I drown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, you're worrying about\x01",
            "that... You have a cute\x01",
            "side, don't you Sullboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04201FAh, jeez! Enough with\x01",
            "the Sullboy already, go\x01",
            "away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8AE")

    label("loc_85E")


    ChrTalk(
        0xF,
        (
            "#04206FIt'll be my first time\x01",
            "swimming.\x02\x03",
            "#04208FWhat'll I do if I\x01",
            "drown...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE")

    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_8B2(): pass

    label("Function_5_8B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8C3")
    Jump("loc_D34")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8D1")
    Jump("loc_D34")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8DF")
    Jump("loc_D34")

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F7")
    Jump("loc_8F7")

    label("loc_8F7")

    Jump("loc_D34")

    label("loc_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAB")

    ChrTalk(
        0xE,
        "#01802FAh, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, Rixia. You're still\x01",
            "in your room?\x02\x03",
            "#00000FI thought you went to\x01",
            "the boutique with Elie\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01809FAhaha. It seems playing\x01",
            "at the beach tired me\x01",
            "out.\x02\x03",
            "#01802FI'll go after I've had\x01",
            "some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see...\x02\x03",
            "#00002FWell, there's still time until\x01",
            "our appointment at the theme\x01",
            "park, so don't push yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01809FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B05")

    label("loc_AAB")


    ChrTalk(
        0xE,
        (
            "#01800FIf you're looking for\x01",
            "KeA, she hasn't been\x01",
            "here.\x02\x03",
            "Perhaps she left the\x01",
            "hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B05")

    Jump("loc_D34")

    label("loc_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B18")
    Jump("loc_D34")

    label("loc_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B33")
    Call(0, 6)
    Jump("loc_D34")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83")

    ChrTalk(
        0xE,
        (
            "#01803FActually, a novice like\x01",
            "me shouldn't have time to\x01",
            "play at the beach, but...\x02\x03",
            "#01802FIlya convinced me that\x01",
            "rest is important for\x01",
            "artists as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIlya's right.\x02\x03",
            "#00000FIt's a rare chance, so I\x01",
            "think a change of pace would\x01",
            "be good for you too, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01800FHaha... Yes, I'll do\x01",
            "just that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D34")

    label("loc_C83")


    ChrTalk(
        0xE,
        (
            "#01804FFirst, I'll teach her the\x01",
            "basics of each swimming style\x01",
            "in order.\x02\x03",
            "#01803FOnce she learns them, with her\x01",
            "intuition for these things,\x01",
            "she'll manage somehow or other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D34")

    TalkEnd(0xFE)
    Return()

    # Function_5_8B2 end

    def Function_6_D38(): pass

    label("Function_6_D38")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC9")
    Jump("loc_E13")

    label("loc_DC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DE9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E13")

    label("loc_DE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E09")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E13")

    label("loc_E09")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E13")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EC9")
    Jump("loc_F13")

    label("loc_EC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EE9")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F13")

    label("loc_EE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F09")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F13")

    label("loc_F09")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F13")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xE,
        "#01802FAh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLooks like you've\x01",
            "finished unpacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802FYes, that's right, but...\x02\x03",
            "#01809FIt seems like today will be Sully's\x01",
            "first day playing in the water and\x01",
            "she looks a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#04211FH-Hey, Rixia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha. Just hiding won't\x01",
            "do anything. You know\x01",
            "that, right Sullboy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04205FS-Sullboy he said... Don't\x01",
            "call me such a weird name\x01",
            "all of a sudden!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha. It's fine, isn't it? With\x01",
            "PeTiote, Jona buddy and Keddo,\x01",
            "the next has to be Sullboy right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04206FW-Who cares! Right? I\x01",
            "mean, no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Well if you can't\x01",
            "swim, Rixia'll teach you\x01",
            "patiently, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802FYes. And I'm sure you'll\x01",
            "pick it up quickly,\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04203FH-Hmph. I know that\x01",
            "already.\x02\x03",
            "#04208FIt's just... I'm not\x01",
            "quite ready, see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. Well once you're\x01",
            "ready, come to the beach\x01",
            "with Rixia.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x15A, 4)
    Return()

    # Function_6_D38 end

    def Function_7_12C8(): pass

    label("Function_7_12C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_12D9")
    Jump("loc_158E")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12E7")
    Jump("loc_158E")

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_12F5")
    Jump("loc_158E")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1303")
    Jump("loc_158E")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1311")
    Jump("loc_158E")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_131F")
    Jump("loc_158E")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_158E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133A")
    Call(0, 9)
    Jump("loc_158E")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EA")

    ChrTalk(
        0xD,
        (
            "#01704FAfter I saw it in a foreign\x01",
            "magazine, my dream has been\x01",
            "to party hard at the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FPersonally, I'm lookin'\x01",
            "forward to see Ilya and\x01",
            "the others in swimsuits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FYeah, they lend swimsuits at the\x01",
            "Lake Beach reception area.\x02\x03",
            "#01709FAlright, if that's how it's\x01",
            "going to be, I guess I'll pick a\x01",
            "super flashy and sexy swimsuit!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909FHaha, oh, Ilya. Don't go\x01",
            "too crazy, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_158E")

    label("loc_14EA")


    ChrTalk(
        0xD,
        (
            "#01709FHehe, look forward to it.\x01",
            "I'll pick a super flashy\x01",
            "and sexy swimsuit!\x02\x03",
            "#01702FAlright, let's finish\x01",
            "preparing at once and go\x01",
            "to the long-awaited beach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158E")

    TalkEnd(0xFE)
    Return()

    # Function_7_12C8 end

    def Function_8_1592(): pass

    label("Function_8_1592")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_15A3")
    Jump("loc_176F")

    label("loc_15A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15B1")
    Jump("loc_176F")

    label("loc_15B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_15BF")
    Jump("loc_176F")

    label("loc_15BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_15CD")
    Jump("loc_176F")

    label("loc_15CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15DB")
    Jump("loc_176F")

    label("loc_15DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_15E9")
    Jump("loc_176F")

    label("loc_15E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_176F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")
    Call(0, 9)
    Jump("loc_176F")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16ED")

    ChrTalk(
        0xC,
        (
            "#05900FOh, Lloyd. Are you ready\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, more or less.\x02\x03",
            "#00004FWe'll go on ahead, so you\x01",
            "and Ilya can take your\x01",
            "time and come later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05902FHaha, all right. We'll\x01",
            "try not to be too late.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_176F")

    label("loc_16ED")


    ChrTalk(
        0xC,
        (
            "#05904FOh Ilya, you never change.\x02\x03",
            "#05902FHaha. I'm sure she's causing\x01",
            "a lot of trouble for the\x01",
            "Arc-en-Ciel members as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176F")

    TalkEnd(0xFE)
    Return()

    # Function_8_1592 end

    def Function_9_1773(): pass

    label("Function_9_1773")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909FCome to think of it, we\x01",
            "haven't had a sleepover\x01",
            "since we were kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FOh, that's right.\x02\x03",
            "#01704FAfter I got busy with\x01",
            "practice, I haven't had many\x01",
            "chances to come see you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01709FThat's right. Want to take a\x01",
            "bath together today? We haven't\x01",
            "done that in a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05905FYes, I don't mind,\x01",
            "but...\x02\x03",
            "#05903FIsn't the bath in our\x01",
            "room a little small for\x01",
            "two adults?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FIsn't that just fine?\x02\x03",
            "#01709FWith these hands, I've got\x01",
            "to see how you've grown\x01",
            "these past few years!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05909FHaha. Ilya, you never\x01",
            "change.\x02",
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
            "#00306F(Mrr... I am sooo\x01",
            "jealous of Ilya right\x01",
            "now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Y-Yeah... Cecil is\x01",
            "defenseless, huh.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_1773 end

    def Function_10_1A6E(): pass

    label("Function_10_1A6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1A7F")
    Jump("loc_1B50")

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1A8D")
    Jump("loc_1B50")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A9B")
    Jump("loc_1B50")

    label("loc_1A9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1AAB")
    Jump("loc_1B50")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1AB9")
    Jump("loc_1B50")

    label("loc_1AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1AC7")
    Jump("loc_1B50")

    label("loc_1AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1AD5")
    Jump("loc_1B50")

    label("loc_1AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF0")
    Call(0, 12)
    Jump("loc_1B50")

    label("loc_1AF0")


    ChrTalk(
        0xB,
        (
            "#06401FNoｱl! That's rude, you\x01",
            "know?\x02\x03",
            "#06406FDespite appearances, I'm\x01",
            "a police officer too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B50")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A6E end

    def Function_11_1B54(): pass

    label("Function_11_1B54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1B65")
    Jump("loc_1EDC")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1B73")
    Jump("loc_1EDC")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1B81")
    Jump("loc_1EDC")

    label("loc_1B81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1B91")
    Jump("loc_1EDC")

    label("loc_1B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1B9F")
    Jump("loc_1EDC")

    label("loc_1B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D93")

    ChrTalk(
        0x12,
        (
            "#10103FHmm, what will I do\x01",
            "until our appointment?\x02\x03",
            "#10108FIt would be nice to go\x01",
            "to the boutique with\x01",
            "Fran, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHmm, is there a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10111FUmm, actually, it's that...\x02\x03",
            "#10109FAfter seeing Cecil and the\x01",
            "others' proportions at the beach,\x01",
            "I started feeling defeated...\x02\x03",
            "#10106FI'm very hesitant to choose and\x01",
            "try on clothes in front of\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm... I'm certain she's\x01",
            "overthinking it, but... Maybe\x01",
            "it's also because she's a woman?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1E27")

    label("loc_1D93")


    ChrTalk(
        0x12,
        (
            "#10106FI'm very hesitant to choose\x01",
            "and try on clothes in front\x01",
            "of Cecil and the others...\x02\x03",
            "#10100FI'll go to the jewelry\x01",
            "where Randy is later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E27")

    Jump("loc_1EDC")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1E3A")
    Jump("loc_1EDC")

    label("loc_1E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E55")
    Call(0, 12)
    Jump("loc_1ECE")

    label("loc_1E55")


    ChrTalk(
        0x12,
        (
            "#10106F*sigh*, I feel like I\x01",
            "was duped.\x02\x03",
            "#10101FTo think that I, of all\x01",
            "people, was tricked by\x01",
            "someone like Fran...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECE")

    Jump("loc_1EDC")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1EDC")

    label("loc_1EDC")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B54 end

    def Function_12_1EE0(): pass

    label("Function_12_1EE0")

    OP_4B(0x12, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x12,
        (
            "#10101FOh, Fran... You didn't show\x01",
            "any intention of coming at all\x01",
            "yesterday.\x02\x03",
            "#10106FYou even said things like "I'd\x01",
            "go if I didn't have work" and\x01",
            ""I envy you, Noｱl"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#06402FEhe, sorry~. I got my\x01",
            "invitation when you did,\x01",
            "but...\x02\x03",
            "#06409FMariabell forbade me to\x01",
            "say anything until\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10106F*sigh*. To think I was\x01",
            "tricked by someone like\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#06405FAw! That's so mean!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_12_1EE0 end

    def Function_13_2089(): pass

    label("Function_13_2089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_209A")
    Jump("loc_2254")

    label("loc_209A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_20A8")
    Jump("loc_2254")

    label("loc_20A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_20B6")
    Jump("loc_2254")

    label("loc_20B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_20C4")
    Jump("loc_2254")

    label("loc_20C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_20EF")

    ChrTalk(
        0x13,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2254")

    label("loc_20EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_20FD")
    Jump("loc_2254")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_224B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222C")

    ChrTalk(
        0x13,
        "#01200F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FZeit, so this is where\x01",
            "you were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, did the water bus\x01",
            "trip tire you out a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01203F...Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FIt doesn't look like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, Zeit will join us\x01",
            "at beach later, so let's\x01",
            "leave him alone for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2246")

    label("loc_222C")


    ChrTalk(
        0x13,
        "#01200F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_2246")

    Jump("loc_2254")

    label("loc_224B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2254")

    label("loc_2254")

    TalkEnd(0xFE)
    Return()

    # Function_13_2089 end

    def Function_14_2258(): pass

    label("Function_14_2258")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2269")
    Jump("loc_237D")

    label("loc_2269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2277")
    Jump("loc_237D")

    label("loc_2277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2285")
    Jump("loc_237D")

    label("loc_2285")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2295")
    Jump("loc_237D")

    label("loc_2295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_22A3")
    Jump("loc_237D")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BE")
    Call(0, 15)
    Jump("loc_2353")

    label("loc_22BE")


    ChrTalk(
        0x11,
        (
            "#00203FGoing to the theme park\x01",
            "without knowing Mishy...\x01",
            "What recklessness.\x02\x03",
            "#00201FIt appears that you need\x01",
            "to be thoroughly\x01",
            "educated, Sully...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2353")

    Jump("loc_237D")

    label("loc_2358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2366")
    Jump("loc_237D")

    label("loc_2366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2374")
    Jump("loc_237D")

    label("loc_2374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_237D")

    label("loc_237D")

    TalkEnd(0xFE)
    Return()

    # Function_14_2258 end

    def Function_15_2381(): pass

    label("Function_15_2381")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "#04205FHmm? What's that\x01",
            "attached to your device?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00204FIt's called a Mishy\x01",
            "strap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FWow. So this is the\x01",
            ""Mishy" I've heard so\x01",
            "much about.\x02\x03",
            "#04204FI guess it's my first\x01",
            "time seeing him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#00205F...Your first time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FYeah. I've heard the\x01",
            "name often but I had no\x01",
            "idea this is who he was.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00203F...It appears you need\x01",
            "to be thoroughly\x01",
            "educated, Sully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_15_2381 end

    def Function_16_2552(): pass

    label("Function_16_2552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2563")
    Jump("loc_2712")

    label("loc_2563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2571")
    Jump("loc_2712")

    label("loc_2571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2678")

    ChrTalk(
        0xFE,
        (
            "Today, the VIP floor is\x01",
            "reserved for you, ladies\x01",
            "and gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, we are pleased to\x01",
            "offer you all room service free of\x01",
            "charge, courtesy of Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to ask\x01",
            "me for anything you may\x01",
            "need.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2712")

    label("loc_2678")


    ChrTalk(
        0xFE,
        (
            "We are pleased to offer you all\x01",
            "room service free of charge,\x01",
            "courtesy of lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to ask\x01",
            "me for anything you may\x01",
            "need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2712")

    TalkEnd(0xFE)
    Return()

    # Function_16_2552 end

    def Function_17_2716(): pass

    label("Function_17_2716")

    Call(0, 18)
    Return()

    # Function_17_2716 end

    def Function_18_271A(): pass

    label("Function_18_271A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_272B")
    Jump("loc_28CB")

    label("loc_272B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D3")

    ChrTalk(
        0x9,
        (
            "How was your time at the\x01",
            "beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On days off, I enjoy\x01",
            "sunbathing at the beach\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I'll have to go\x01",
            "again before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_283B")

    label("loc_27D3")


    ChrTalk(
        0x9,
        (
            "On days off, I enjoy\x01",
            "sunbathing at the beach\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I'll have to go\x01",
            "again before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_283B")

    Jump("loc_28CB")

    label("loc_2840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_28CB")

    ChrTalk(
        0x9,
        (
            "This is the bar for the\x01",
            "VIP floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please, feel free to order all\x01",
            "the cocktails, soft drinks or\x01",
            "the like that you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CB")

    TalkEnd(0x9)
    Return()

    # Function_18_271A end

    def Function_19_28CF(): pass

    label("Function_19_28CF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2BC2")
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x14,
        "#02902F#3801V#30WThese are your rooms.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xED9)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Jump("loc_2BF9")

    label("loc_2BC2")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x14,
        "#02902FThese are your rooms.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2BF9")

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
        "#00011F#11PThis is amazing...\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        "#00309F#5PAh, too fancy!\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10302F#11PIt looks like you changed\x01",
            "the number of beds to\x01",
            "match our number, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PUhuhu. This service is a matter of\x01",
            "course for a top-class hotel.\x02\x03",
            "#02901FWell, regarding this room specifically,\x01",
            "I would have liked to be able to lock\x01",
            "it from the outside, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2E3A():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E3A)
    Sleep(50)

    def lambda_2E4A():
        TurnDirection(0x104, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E4A)
    Sleep(50)

    def lambda_2E5A():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2E5A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00012F#6PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#6PNo trust at all, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PHehe, not entirely\x01",
            "unexpected.\x02\x03",
            "#10302FAfter all, aside from\x01",
            "us, all your guests are\x01",
            "pretty ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02906F#11PI think I can trust you\x01",
            "though, Wazy.\x02\x03",
            "#02913FHonestly, it's Lloyd and\x01",
            "Randy that I don't fully\x01",
            "trust.\x02\x03",
            "#02901FEspecially Lloyd. He is a\x01",
            "dangerous character requiring\x01",
            "special surveillance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PWhaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#6PHehe. It's you we're talking about here.\x01",
            "You'd casually wander into the lounge in\x01",
            "the middle of the night, there'd be a\x01",
            "girl who can't sleep there...\x02\x03",
            "#10302FThen, while you were talking a nice\x01",
            "atmosphere would be building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PYeah, I can see that\x01",
            "happenin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#02909F#11P...Lloyd. I wonder if\x01",
            "can I have you stay in\x01",
            "the employee nap room?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    ChrTalk(
        0x101,
        "#00012F#6PNo, I won't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02906F#11PHmph, honestly.\x02\x03",
            "#02904FBy the way, I have a board meeting so\x01",
            "I'll return to the city after this,\x01",
            "but...\x02\x03",
            "Be extremely careful to not lust after\x01",
            "Elie and the others in their swimsuits.\x02\x03",
            "#02901F...If you do anything bad, I'll call the\x01",
            "Security Department and have you thrown\x01",
            "in the middle of the lake, understood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI'm telling you, I\x01",
            "won't...\x02\x03",
            "#00001F...But Mariabell, you\x01",
            "seem quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PHuhu. It's because my father declared such a\x01",
            "thing.\x02\x03",
            "#02902FAs you can imagine, IBC's business has grown\x01",
            "more complicated due to that, and everything\x01",
            "has been taken over by the board of directors.\x02\x03",
            "Naturally, that burden falls on me as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see... Really, thank\x01",
            "you for all your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PWell, at least remember\x01",
            "to take proper breaks\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#6PRest and stress are\x01",
            "important for beauty and\x01",
            "health, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PHuhu. Thank you for your concern.\x02\x03",
            "#02900FLike I told you, the Lake Beach\x01",
            "reception area is on 1F in the\x01",
            "right wing of the shopping arcade.\x02\x03",
            "You can rent swimsuits there too,\x01",
            "so please change in the locker\x01",
            "room.\x02\x03",
            "#02901F...Of course in the men's one, you\x01",
            "hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, you don't have to\x01",
            "emphasize that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PIn any case, gotcha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PLake Beach is reserved for\x01",
            "you all until noon.\x02\x03",
            "You should enjoy the theme\x01",
            "park all you like this\x01",
            "afternoon.\x02\x03",
            "#02902FMany people in your group\x01",
            "have been there before, so\x01",
            "I'll leave that to you.\x02\x03",
            "#02909FThis evening, I'll have\x01",
            "dinner prepared for you at\x01",
            "the guest house.\x02\x03",
            "Formal dress is not\x01",
            "required, so please go there\x01",
            "at the appointed time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PYou're nothing if not\x01",
            "thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#02904F#11PHuhu. It is my pleasure.\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_38FB")
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x14,
        (
            "#02911F#3771V#5P#40W─Have a good stay. And\x01",
            "please enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEBB)
    OP_C9(0x1, 0x80000000)
    Jump("loc_393B")

    label("loc_38FB")


    ChrTalk(
        0x14,
        (
            "#02902F#5P─Have a good stay. And\x01",
            "please enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393B")

    OP_57(0x0)
    OP_5A()

    def lambda_3943():

        label("loc_3943")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3943")

    QueueWorkItem2(0x101, 2, lambda_3943)

    def lambda_3955():

        label("loc_3955")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3955")

    QueueWorkItem2(0x104, 2, lambda_3955)

    def lambda_3967():

        label("loc_3967")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3967")

    QueueWorkItem2(0x105, 2, lambda_3967)

    def lambda_3979():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3979)
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
            "#00002F#6P...She's a very kind\x01",
            "person, no matter what\x01",
            "anyone says.\x02\x03",
            "#00006FAlthough I wish she'd\x01",
            "stop seeing me as some\x01",
            "strange threat...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A74():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A74)
    Sleep(50)

    def lambda_3A84():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A84)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00304F#12PWell, think of it as\x01",
            "fate and give up.\x02\x03",
            "#00302FAlll righty then, let's\x01",
            "head to the beach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHehe, right.\x02\x03",
            "#10300FI bet it'll take the\x01",
            "girls some time to get\x01",
            "ready...\x02\x03",
            "Shall we head there\x01",
            "ahead of them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah...\x02\x03",
            "#00000FAlright then, let's\x01",
            "speak to them and then\x01",
            "go.\x02",
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

    # Function_19_28CF end

    def Function_20_3C5E(): pass

    label("Function_20_3C5E")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_20_3C5E end

    def Function_21_3C6E(): pass

    label("Function_21_3C6E")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_21_3C6E end

    def Function_22_3C7E(): pass

    label("Function_22_3C7E")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_3C7E end

    def Function_23_3C8E(): pass

    label("Function_23_3C8E")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_3C8E end

    def Function_24_3C9E(): pass

    label("Function_24_3C9E")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_3C9E end

    def Function_25_3CCC(): pass

    label("Function_25_3CCC")

    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_3CCC end

    def Function_26_3D09(): pass

    label("Function_26_3D09")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_3D09 end

    def Function_27_3D46(): pass

    label("Function_27_3D46")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xED8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_27_3D46 end

    def Function_28_3D83(): pass

    label("Function_28_3D83")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_28_3D83 end

    def Function_29_3DC0(): pass

    label("Function_29_3DC0")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_29_3DC0 end

    def Function_30_3DFD(): pass

    label("Function_30_3DFD")

    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x14B4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_30_3DFD end

    def Function_31_3E49(): pass

    label("Function_31_3E49")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_31_3E49 end

    def Function_32_3E95(): pass

    label("Function_32_3E95")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_32_3E95 end

    def Function_33_3EE1(): pass

    label("Function_33_3EE1")

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
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3396V#30WExcuse me, can I come\x01",
            "in?\x02",
        )
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

    def lambda_404E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_404E)
    Sleep(50)

    def lambda_405E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_405E)
    OP_79(0x7)
    OP_68(-100000, 1000, -79300, 2000)

    def lambda_407F():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_407F)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#6POh, Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#6PLeaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00102F#11PYes. The Arc-en-Ciel girls invited me to\x01",
            "go shopping with them. I was going to go\x01",
            "to the theme park after that, but...\x02",
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
        "#00105F#11PUmm, did KeA stop by?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PKeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6PWhat, something wrong\x01",
            "with Keddo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11PShe said "I'm going to\x01",
            "Lloyd's room" just now,\x01",
            "but...\x02\x03",
            "#00108FHmm, I wonder where\x01",
            "she's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PAren't Tio and Zeit with\x01",
            "her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F#11PYes, they could be.\x02\x03",
            "#00102FSorry. I'll keep looking\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PAh, wait a moment.\x02\x03",
            "#00000FIlya and the others are\x01",
            "waiting for you, right?\x02\x03",
            "Go to them. I'll look\x01",
            "for KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00105F#11PHuh, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI shouldn't rely on you\x01",
            "guys for everything all\x01",
            "the time.\x02\x03",
            "#00002FI'll find KeA and bring\x01",
            "her to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11POkay. I'll leave it to\x01",
            "you, then.\x02\x03",
            "#00108F...*sigh*. I wanted to\x01",
            "look for new clothes for\x01",
            "KeA, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)

    def lambda_447F():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_447F)
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
            "#00309F#12PHaha, Keddo's super\x01",
            "popular as always, huh.\x02\x03",
            "#00300FThen, should we start\x01",
            "looking?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00000F#5PAh, I alone will be\x01",
            "enough.\x02\x03",
            "You said you wanted to\x01",
            "look in the shops, right\x01",
            "Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12PYou sure?\x02\x03",
            "#00304FIn that case, I'll be in the\x01",
            "jewelry store downstairs. Let\x01",
            "me know if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_END)), "loc_4650")

    ChrTalk(
        0x101,
        "#00002F#5PYeah, sure thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48C9")

    label("loc_4650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_4791")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWait, a jewelry store...\x01",
            "Isn't it members only?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PYeah. I heard we can shop\x01",
            "there today thanks to\x01",
            "Mariabell.\x02\x03",
            "#00304FThat clerk pisses me off a\x01",
            "little, but I'm interested\x01",
            "in what they have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, got it. (Should I\x01",
            "take a look inside?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48C9")

    label("loc_4791")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PA jewelry store... The\x01",
            "one in the arcade\x01",
            "downstairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PYeah. I heard we can shop\x01",
            "there today thanks to\x01",
            "Mariabell.\x02\x03",
            "#00304FThat clerk pisses me off a\x01",
            "little, but I'm interested\x01",
            "in what they have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, got it. (Should I\x01",
            "take a look inside?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48C9")

    OP_68(-100000, 1000, -78500, 5000)

    def lambda_48DF():

        label("loc_48DF")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_48DF")

    QueueWorkItem2(0x101, 2, lambda_48DF)
    OP_93(0x104, 0x0, 0x1F4)

    def lambda_48F8():
        OP_95(0xFE, -100000, 0, -76900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_48F8)
    WaitChrThread(0x104, 1)
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_93(0x104, 0x0, 0x0)

    def lambda_4936():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4936)
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
            "#00004F#6PThen, I think I'll look\x01",
            "for KeA.\x02\x03",
            "#00008FShe probably hasn't left\x01",
            "the hotel, but...\x02\x03",
            "#00001FIf I don't find her\x01",
            "here, I'll need to\x01",
            "search elsewhere.\x02",
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
    SubItemNumber(0x329, 10)
    SubItemNumber(0x32B, 10)
    SubItemNumber(0x32C, 10)
    EventEnd(0x5)
    Return()

    # Function_33_3EE1 end

    SaveToFile()

Try(main)
