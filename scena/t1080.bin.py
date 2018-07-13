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
        "Function_5_8C7",          # 05, 5
        "Function_6_DAF",          # 06, 6
        "Function_7_1366",         # 07, 7
        "Function_8_1645",         # 08, 8
        "Function_9_185B",         # 09, 9
        "Function_10_1B60",        # 0A, 10
        "Function_11_1C56",        # 0B, 11
        "Function_12_2020",        # 0C, 12
        "Function_13_2236",        # 0D, 13
        "Function_14_23F9",        # 0E, 14
        "Function_15_2528",        # 0F, 15
        "Function_16_26FF",        # 10, 16
        "Function_17_28AF",        # 11, 17
        "Function_18_28B3",        # 12, 18
        "Function_19_2A60",        # 13, 19
        "Function_20_3E27",        # 14, 20
        "Function_21_3E37",        # 15, 21
        "Function_22_3E47",        # 16, 22
        "Function_23_3E57",        # 17, 23
        "Function_24_3E67",        # 18, 24
        "Function_25_3E95",        # 19, 25
        "Function_26_3ED2",        # 1A, 26
        "Function_27_3F0F",        # 1B, 27
        "Function_28_3F4C",        # 1C, 28
        "Function_29_3F89",        # 1D, 29
        "Function_30_3FC6",        # 1E, 30
        "Function_31_4012",        # 1F, 31
        "Function_32_405E",        # 20, 32
        "Function_33_40AA",        # 21, 33
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
    Jump("loc_8C3")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_680")
    Jump("loc_8C3")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_8C3")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_8C3")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_70F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    Call(0, 15)
    Jump("loc_70A")

    label("loc_6B7")


    ChrTalk(
        0xF,
        (
            "#04205FW-What do you want all of a sudden...\x02\x03",
            "#04206FDid I say something bad?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A")

    Jump("loc_8C3")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_71D")
    Jump("loc_8C3")

    label("loc_71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738")
    Call(0, 6)
    Jump("loc_8C3")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_870")

    ChrTalk(
        0xF,
        (
            "#04206F*haah*, it's the first time since\x01",
            "I was born that I'm swimming.\x02\x03",
            "#04208FBig sis Rixia is teaching me,\x01",
            "but what will I do if I drown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, you're worrying about that...\x01",
            "So you have some cute sides too,\x01",
            "Sullboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04201FAh, jeez!\x01",
            "Enough with the Sullboy,\x01",
            "go away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8C3")

    label("loc_870")


    ChrTalk(
        0xF,
        (
            "#04206FIt's the first time I'm swimming.\x02\x03",
            "#04208FWhat will I do if I drown...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C3")

    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_8C7(): pass

    label("Function_5_8C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8D8")
    Jump("loc_DAB")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8E6")
    Jump("loc_DAB")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8F4")
    Jump("loc_DAB")

    label("loc_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C")
    Jump("loc_90C")

    label("loc_90C")

    Jump("loc_DAB")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4")

    ChrTalk(
        0xE,
        "#01802FAh...Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, Rixia.\x01",
            "Are you still in your room?\x02\x03",
            "#00000FI thought you had gone\x01",
            "to the boutique with Elie \x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01809FAhaha, somehow it seems I have\x01",
            "got tired by playing at the beach.\x02\x03",
            "#01802FAfter I have had some rest,\x01",
            "I intend to go too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see...\x02\x03",
            "#00002FWell, there's still time until the\x01",
            "appointment at the theme park,\x01",
            "so don't overdo it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01809FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B50")

    label("loc_AE4")


    ChrTalk(
        0xE,
        (
            "#01800FIf you're looking for KeA,\x01",
            "she hasn't come here.\x02\x03",
            "Maybe, she could have\x01",
            "gone outside the hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B50")

    Jump("loc_DAB")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B63")
    Jump("loc_DAB")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7E")
    Call(0, 6)
    Jump("loc_DAB")

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF3")

    ChrTalk(
        0xE,
        (
            "#01803FActually, a novice like me shouldn't\x01",
            "have the time to play at the beach, but...\x02\x03",
            "#01802FI was convinced by Miss Ilya that \x01",
            "rest is important for an artist too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWhat Miss Ilya said is quite right.\x02\x03",
            "#00000FIt's a rare chance, so it would be nice if\x01",
            "you had a great change of pace too, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01800FUh uh...yes, I will do that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_DAB")

    label("loc_CF3")


    ChrTalk(
        0xE,
        (
            "#01804FFirst of all, I will teach her in order\x01",
            "from the swimming styles basics.\x02\x03",
            "#01803FIf she memorizes those,\x01",
            "I think that with Sully's sense\x01",
            "she'll manage in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")

    TalkEnd(0xFE)
    Return()

    # Function_5_8C7 end

    def Function_6_DAF(): pass

    label("Function_6_DAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E40")
    Jump("loc_E8A")

    label("loc_E40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E60")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E8A")

    label("loc_E60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E80")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E8A")

    label("loc_E80")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E8A")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F40")
    Jump("loc_F8A")

    label("loc_F40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F60")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8A")

    label("loc_F60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F80")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8A")

    label("loc_F80")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F8A")

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
            "#00000FIt looks like you have\x01",
            "finished unpacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802FYes, you're right, but...\x02\x03",
            "#01809FToday, it seems it's the first\x01",
            "time for Sully to play in water\x01",
            "and she looks a little tense...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#04211FH-Hey, big sis Rixia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, even if you hide it,\x01",
            "it won't make much difference,\x01",
            "you know, Sullboy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04205FS-Sullboy...\x01",
            "Don't call me by a weird name all of a sudden!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, oh come'on.\x01",
            "PeTiote, the great Jona, Keddo...\x01",
            "Might as well be Sullboy, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04206FW-Who cares!\x01",
            "Right? I mean, no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, well, if you don't know how to swim,\x01",
            "it would be all right if you teach her\x01",
            "very attentively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01802FYes, also, I think that Sully\x01",
            "will be able to learn quick too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04203FH-Hmph, I know.\x02\x03",
            "#04208FIt's just that, I have to mentally prepare and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, well, when you have prepared,\x01",
            "you can come with Rixia.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x15A, 4)
    Return()

    # Function_6_DAF end

    def Function_7_1366(): pass

    label("Function_7_1366")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1377")
    Jump("loc_1641")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1385")
    Jump("loc_1641")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1393")
    Jump("loc_1641")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_13A1")
    Jump("loc_1641")

    label("loc_13A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13AF")
    Jump("loc_1641")

    label("loc_13AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_13BD")
    Jump("loc_1641")

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D8")
    Call(0, 9)
    Jump("loc_1641")

    label("loc_13D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(
        0xD,
        (
            "#01704FAfter I previously saw it in a foreign magazine,\x01",
            "my dream has been to party hard at the beach.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FPersonally, I'm lookin' forward to see\x01",
            "Miss Ilya and the others in swimsuits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FYeah, they lend swimsuit\x01",
            "at the Lake Beach reception.\x02\x03",
            "#01709FAlright, now that we've come to this,\x01",
            "I guess I'll pick a super flashy and\x01",
            "sexy swimsuit!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909FUh uh, oh, Ilya.\x01",
            "Don't go too much overboard, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_1641")

    label("loc_159A")


    ChrTalk(
        0xD,
        (
            "#01709FHu hu, look forward to it.\x01",
            "I'll pick a super flashy\x01",
            "and sexy swimsuit!\x02\x03",
            "#01702FAlright, let's finish preparing at once\x01",
            "and go to the long-cherished beach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1641")

    TalkEnd(0xFE)
    Return()

    # Function_7_1366 end

    def Function_8_1645(): pass

    label("Function_8_1645")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1656")
    Jump("loc_1857")

    label("loc_1656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1664")
    Jump("loc_1857")

    label("loc_1664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1672")
    Jump("loc_1857")

    label("loc_1672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1680")
    Jump("loc_1857")

    label("loc_1680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_168E")
    Jump("loc_1857")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_169C")
    Jump("loc_1857")

    label("loc_169C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B7")
    Call(0, 9)
    Jump("loc_1857")

    label("loc_16B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CA")

    ChrTalk(
        0xC,
        (
            "#05900FOh, Lloyd.\x01",
            "Have you finished preparing already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, more or less.\x02\x03",
            "#00004FWe'll go on ahead, so you and Miss Ilya\x01",
            "can take your time and come later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05902FUh uh, all right. We will try as much\x01",
            "as possible to not be too late.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1857")

    label("loc_17CA")


    ChrTalk(
        0xC,
        (
            "#05904FOh Ilya, you are\x01",
            "always the same.\x02\x03",
            "#05902FUh uh, I am sure you are causing a lot of\x01",
            "trouble for the Arc-en-ciel members too, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1857")

    TalkEnd(0xFE)
    Return()

    # Function_8_1645 end

    def Function_9_185B(): pass

    label("Function_9_185B")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "#05909FBy the way, we haven't\x01",
            "spent the night together\x01",
            "since we were kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01705FAh, now that you mention it, yes.\x02\x03",
            "#01704FAfter I became busy with practice,\x01",
            "we couldn't meet much anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01709FRight, why don't we bath together today?\x01",
            "We haven't done it in a long time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05905FYes, I don't mind, but...\x02\x03",
            "#05903FWon't the bath in the room\x01",
            "be narrow for two adults?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FEeh, and isn't that fine?\x02\x03",
            "#01709FI must carefully ascertain with these\x01",
            "hands many years of growing up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#05909FUh uh, oh Ilya, you are\x01",
            "always the same.\x02",
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
            "#00306F(Mrr...\x01",
            "I envy Miss Ilya's\x01",
            "position sooo much.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(U-Uhhm...\x01",
            "Sister Cecil is defenseless.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_185B end

    def Function_10_1B60(): pass

    label("Function_10_1B60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1B71")
    Jump("loc_1C52")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1B7F")
    Jump("loc_1C52")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1B8D")
    Jump("loc_1C52")

    label("loc_1B8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1B9D")
    Jump("loc_1C52")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1BAB")
    Jump("loc_1C52")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1BB9")
    Jump("loc_1C52")

    label("loc_1BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1BC7")
    Jump("loc_1C52")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE2")
    Call(0, 12)
    Jump("loc_1C52")

    label("loc_1BE2")


    ChrTalk(
        0xB,
        (
            "#06401FOh big sis, that's a \x01",
            "rude remark, you know?\x02\x03",
            "#06406FDespite appearances,\x01",
            "I'm a police officer too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B60 end

    def Function_11_1C56(): pass

    label("Function_11_1C56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1C67")
    Jump("loc_201C")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1C75")
    Jump("loc_201C")

    label("loc_1C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1C83")
    Jump("loc_201C")

    label("loc_1C83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1C93")
    Jump("loc_201C")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1CA1")
    Jump("loc_201C")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB9")

    ChrTalk(
        0x12,
        (
            "#10103FUhhm, what will I do until\x01",
            "the appointment hour?\x02\x03",
            "#10108FIt would be nice to go to the\x01",
            "boutique with Fran, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHm, is there any problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10111FE-Ehm, actually, it's that...\x02\x03",
            "#10109FAfter having seen Miss Cecil and the\x01",
            "others' proportions at the beach, I\x01",
            "started feeling a sense of defeat...\x02\x03",
            "#10106FI'm very hesitating to\x01",
            "choose and try clothes\x01",
            "in front of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(U-Uuhm...\x01",
            "I believe she's thinking too much, but...\x01",
            "Maybe it's possible since she's a woman too?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1F58")

    label("loc_1EB9")


    ChrTalk(
        0x12,
        (
            "#10106FI'm very hesitating to choose\x01",
            "and try clothes in front of\x01",
            "Miss Cecil and the others...\x02\x03",
            "#10100FI'll go to the jewelry where\x01",
            "senior Randy is later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F58")

    Jump("loc_201C")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1F6B")
    Jump("loc_201C")

    label("loc_1F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F86")
    Call(0, 12)
    Jump("loc_200E")

    label("loc_1F86")


    ChrTalk(
        0x12,
        (
            "#10106F*haah*, I feel like I was played a trick.\x02\x03",
            "#10101FTo think that I, of all people, have\x01",
            "been tricked by someone like Fran...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200E")

    Jump("loc_201C")

    label("loc_2013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_201C")

    label("loc_201C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1C56 end

    def Function_12_2020(): pass

    label("Function_12_2020")

    OP_4B(0x12, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x12,
        (
            "#10101FEnough, Fran...\x01",
            "Yesterday you didn't show any\x01",
            "intention of coming at all.\x02\x03",
            "#10106FYou were saying things like\x01",
            ""I'd come if I hadn't work to do"\x01",
            "and "How I envy you, big siiis"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#06402FEh eh, sorry.\x01",
            "I received the invitation at\x01",
            "the same time of yours, but...\x02\x03",
            "#06409FI have been forbidden to say\x01",
            "anything by Miss Mariabell\x01",
            "and stayed silent until today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10106F*haah*, to think that I, of all people,\x01",
            "have been tricked by someone like Fran...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#06405FAh, that's rude, big sis!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_12_2020 end

    def Function_13_2236(): pass

    label("Function_13_2236")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2247")
    Jump("loc_23F5")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2255")
    Jump("loc_23F5")

    label("loc_2255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2263")
    Jump("loc_23F5")

    label("loc_2263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2271")
    Jump("loc_23F5")

    label("loc_2271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_229B")

    ChrTalk(
        0x13,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23F5")

    label("loc_229B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_22A9")
    Jump("loc_23F5")

    label("loc_22A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_23EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CD")

    ChrTalk(
        0x13,
        "#01200F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSo you were here, Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, have the trip by\x01",
            "water bus tired you out a bit?\x02",
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
        "#10304FIt doesn't look so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, Zeit too will come\x01",
            "to the beach later, so\x01",
            "let's leave him alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23E7")

    label("loc_23CD")


    ChrTalk(
        0x13,
        "#01200F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_23E7")

    Jump("loc_23F5")

    label("loc_23EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_23F5")

    label("loc_23F5")

    TalkEnd(0xFE)
    Return()

    # Function_13_2236 end

    def Function_14_23F9(): pass

    label("Function_14_23F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_240A")
    Jump("loc_2524")

    label("loc_240A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2418")
    Jump("loc_2524")

    label("loc_2418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2426")
    Jump("loc_2524")

    label("loc_2426")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2436")
    Jump("loc_2524")

    label("loc_2436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2444")
    Jump("loc_2524")

    label("loc_2444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_24FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245F")
    Call(0, 15)
    Jump("loc_24FA")

    label("loc_245F")


    ChrTalk(
        0x11,
        (
            "#00203FGoing to the theme park\x01",
            "without knowing Michey...\x01",
            "What recklessness.\x02\x03",
            "#00201FIt appears that you need to be\x01",
            "thoroughly educated, Miss Sully...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FA")

    Jump("loc_2524")

    label("loc_24FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_250D")
    Jump("loc_2524")

    label("loc_250D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_251B")
    Jump("loc_2524")

    label("loc_251B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2524")

    label("loc_2524")

    TalkEnd(0xFE)
    Return()

    # Function_14_23F9 end

    def Function_15_2528(): pass

    label("Function_15_2528")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        "#04205FHm, what's that machine attached there...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#00204FWell, it's a Michey's strap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FEeh, so this is that "Michey"\x01",
            "I heard about, huh?\x02\x03",
            "#04204FI guess it's the first time I'm seeing it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#00205F...First time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04202FYeah, I've heard the name often\x01",
            "but I didn't know it was like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00203F...It appears that you need to be\x01",
            "thoroughly educated, Miss Sully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_15_2528 end

    def Function_16_26FF(): pass

    label("Function_16_26FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2710")
    Jump("loc_28AB")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_271E")
    Jump("loc_28AB")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_28AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281B")

    ChrTalk(
        0xFE,
        (
            "Today, the VIP floor is reserved for you,\x01",
            "ladies and gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, you are offered every\x01",
            "kind of room service free of charge,\x01",
            "by courtesy of lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to ask\x01",
            "whatever you want.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28AB")

    label("loc_281B")


    ChrTalk(
        0xFE,
        (
            "You are offered every kind\x01",
            "of room service free of charge,\x01",
            "by courtesy of lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to ask\x01",
            "whatever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AB")

    TalkEnd(0xFE)
    Return()

    # Function_16_26FF end

    def Function_17_28AF(): pass

    label("Function_17_28AF")

    Call(0, 18)
    Return()

    # Function_17_28AF end

    def Function_18_28B3(): pass

    label("Function_18_28B3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_28C4")
    Jump("loc_2A5C")

    label("loc_28C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_29D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296A")

    ChrTalk(
        0x9,
        (
            "How is your time \x01",
            "at the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On days off, I too\x01",
            "enjoy sunbathing\x01",
            "at the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, I'll have to\x01",
            "go again before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29D0")

    label("loc_296A")


    ChrTalk(
        0x9,
        (
            "On days off, I too\x01",
            "enjoy sunbathing\x01",
            "at the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, I'll have to\x01",
            "go again before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D0")

    Jump("loc_2A5C")

    label("loc_29D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2A5C")

    ChrTalk(
        0x9,
        (
            "This is the bar counter\x01",
            "for the VIP floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please, feel free to order any cocktails\x01",
            "soft drinks and so on you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5C")

    TalkEnd(0x9)
    Return()

    # Function_18_28B3 end

    def Function_19_2A60(): pass

    label("Function_19_2A60")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2D50")
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
    Jump("loc_2D84")

    label("loc_2D50")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x14,
        "#02902FThis is your room.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2D84")

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
        "#00309F#5P*phew*, isn't it too luxurious?\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10302F#11PIt looks like you have arranged\x01",
            "the number of beds to match us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PUhuhu, a given service\x01",
            "in a top class hotel.\x02\x03",
            "#02901FWell, regarding this room,\x01",
            "I would have liked it with the possibility\x01",
            "to be locked from the outside too, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2FC5():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FC5)
    Sleep(50)

    def lambda_2FD5():
        TurnDirection(0x104, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2FD5)
    Sleep(50)

    def lambda_2FE5():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FE5)
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
            "#10304F#6PHu hu, not unexpected.\x02\x03",
            "#10302FAside from us, the others are\x01",
            "all pretty ladies, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02906F#11PWell, I think I can somehow\x01",
            "trust Mr. Wazy, though.\x02\x03",
            "#02913FIt's Mr. Lloyd and Mr. Randy\x01",
            "I honestly can't fully trust.\x02\x03",
            "#02901F...Especially Mr. Lloyd, you're a dangerous \x01",
            "person requiring special surveillance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PEeh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#6PHu hu, we're talking about you here.\x01",
            "If you suddenly went out to the lounge in the\x01",
            "dead of night, you'd find a sleepless girl...\x02\x03",
            "#10302FAnd while talking, a nice\x01",
            "mood would be forming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PYeah, I can see that happenin'.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#02909F#11P...Mr. Lloyd.\x01",
            "I wonder if can I have you staying the\x01",
            "night in the employees nap room?\x02",
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
            "#02904FIncidentally, after this I will have to\x01",
            "return to the city temporarily because\x01",
            "I have a board of directors' meeting, but...\x02\x03",
            "Be extremely careful to not lust after\x01",
            "Elie and the others in their swimsuits.\x02\x03",
            "#02901F...If you do something bad, I will call the \x01",
            "security department and have you dropped\x01",
            "in the middle of the lake, understood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI won't do it already...\x02\x03",
            "#00001F...However, Miss Mariabell,\x01",
            "you really seem to be busy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PUh uh, it's because my father\x01",
            "declared such a thing.\x02\x03",
            "#02902FAs you can imagine, since the IBC work has\x01",
            "become more complex at the same time, it was\x01",
            "all took over by the board of directors.\x02\x03",
            "Of course the strain is\x01",
            "affecting me too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see...\x01",
            "Really, thank you for all your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PWell, please take\x01",
            "proper breathers too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#6PRest and stress relieving are\x01",
            "good for beauty and health too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02904F#11PUh uh, thank you for your concern.\x02\x03",
            "#02900FLike I told you, the Lake Beach reception\x01",
            "is on 1F of the arcade right wing area.\x02\x03",
            "You can rent swimsuits too there,\x01",
            "so please change in the locker room.\x02\x03",
            "#02901F...In the men's one, naturally?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PWell, you don't have to emphasize that.\x02",
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
            "#02904F#11PThe Lake Beach is reserved\x01",
            "for you all until noon.\x02\x03",
            "From the afternoon, you can have all\x01",
            "the fun you want at the theme park.\x02\x03",
            "#02902FMany persons will probably be there,\x01",
            "so please take your time.\x02\x03",
            "#02909FAt night, you're going to have your seats\x01",
            "for dinner readied at the guest house.\x02\x03",
            "There is no need for a full dress,\x01",
            "so please come in time.\x02",
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
            "#10304F#6PThank you, it is\x01",
            "very polite of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#02904F#11PUh uh, you are welcome.\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_3AA4")
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x14,
        (
            "#02911F#3771V#5P#40W──Have a good stay.\x01",
            "Please relax to your heart's content.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEBB)
    OP_C9(0x1, 0x80000000)
    Jump("loc_3AEF")

    label("loc_3AA4")


    ChrTalk(
        0x14,
        (
            "#02902F#5P──Have a good stay.\x01",
            "Please relax to your heart's content.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEF")

    OP_57(0x0)
    OP_5A()

    def lambda_3AF7():

        label("loc_3AF7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3AF7")

    QueueWorkItem2(0x101, 2, lambda_3AF7)

    def lambda_3B09():

        label("loc_3B09")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3B09")

    QueueWorkItem2(0x104, 2, lambda_3B09)

    def lambda_3B1B():

        label("loc_3B1B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3B1B")

    QueueWorkItem2(0x105, 2, lambda_3B1B)

    def lambda_3B2D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B2D)
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
            "#00002F#6P...No matter what one can say,\x01",
            "she's a very kind person.\x02\x03",
            "#00006FAlthough I wished she stopped\x01",
            "strangely considering me as hostile...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C2E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C2E)
    Sleep(50)

    def lambda_3C3E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C3E)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00304F#12PWell, resign to your fate.\x02\x03",
            "#00302FThen, let's go to\x01",
            "the beach at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PHu hu, right.\x02\x03",
            "#10300FIt seems it'll take time for the womenfolk\x01",
            "to get prepared no matter what, so...\x02\x03",
            "It would be all right going ahead, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYou're right...\x02\x03",
            "#00000FWell then, let's speak\x01",
            "to them and go.\x02",
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

    # Function_19_2A60 end

    def Function_20_3E27(): pass

    label("Function_20_3E27")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_20_3E27 end

    def Function_21_3E37(): pass

    label("Function_21_3E37")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_21_3E37 end

    def Function_22_3E47(): pass

    label("Function_22_3E47")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_3E47 end

    def Function_23_3E57(): pass

    label("Function_23_3E57")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_3E57 end

    def Function_24_3E67(): pass

    label("Function_24_3E67")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_3E67 end

    def Function_25_3E95(): pass

    label("Function_25_3E95")

    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_3E95 end

    def Function_26_3ED2(): pass

    label("Function_26_3ED2")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_3ED2 end

    def Function_27_3F0F(): pass

    label("Function_27_3F0F")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xED8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_27_3F0F end

    def Function_28_3F4C(): pass

    label("Function_28_3F4C")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_28_3F4C end

    def Function_29_3F89(): pass

    label("Function_29_3F89")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_29_3F89 end

    def Function_30_3FC6(): pass

    label("Function_30_3FC6")

    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x14B4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_30_3FC6 end

    def Function_31_4012(): pass

    label("Function_31_4012")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_31_4012 end

    def Function_32_405E(): pass

    label("Function_32_405E")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_32_405E end

    def Function_33_40AA(): pass

    label("Function_33_40AA")

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
        "#3396V#30WExcuse me, do you have a moment?\x02",
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

    def lambda_421E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_421E)
    Sleep(50)

    def lambda_422E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_422E)
    OP_79(0x7)
    OP_68(-100000, 1000, -79300, 2000)

    def lambda_424F():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_424F)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#6POh, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#6PAre you goin' already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00102F#11PYes. I was invited by Miss Ilya and the others,\x01",
            "so after looking at the shops, we intend to go\x01",
            "to the theme park, but...\x02",
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
            "#00105F#11PUhmm, hasn't KeA come here, \x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PKeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#6PWhat, something's wrong with Keddo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11PWell, some time ago she left\x01",
            "the room saying that she was \x01",
            "coming to your room, Lloyd...\x02\x03",
            "#00108FUhhm, I wonder where she's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PIsn't she with peTiote\x01",
            "or maybe Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F#11PYes, that could be.\x02\x03",
            "#00102FI'm sorry.\x01",
            "I'll look for her a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PAh, wait a moment.\x02\x03",
            "#00000FMiss Ilya and the others are\x01",
            "waiting for you, right?\x02\x03",
            "I'll look for KeA, you go\x01",
            "to the others, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00105F#11PEh, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PIt's not good always leaving\x01",
            "everything to you all.\x02\x03",
            "#00002FI'll properly find her and\x01",
            "bring her to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F#11PUhhm.\x01",
            "Then, please.\x02\x03",
            "#00108F...*sigh*\x01",
            "I wanted to look for\x01",
            "a new dress for her...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)

    def lambda_46AE():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46AE)
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
            "#00309F#12PHa ha, Keddo's super\x01",
            "popular as always, huh.\x02\x03",
            "#00300FThen, should we look for her now?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00000F#5PAh, I alone will be enough.\x02\x03",
            "You said you wanted to look\x01",
            "at the shops too, right, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12PYou sure?\x02\x03",
            "#00304FThen, I'll be down at the jewelry.\x01",
            "Call me if something happens.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_END)), "loc_486F")

    ChrTalk(
        0x101,
        "#00002F#5PYeah, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B18")

    label("loc_486F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_49C7")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PThe jewelry...\x01",
            "The one for members only?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PYeah, it seems that thanks to\x01",
            "Milady Mariabell's mediation\x01",
            "we can go in too, you know?\x02\x03",
            "#00304FThat clerk pisses me off a little, but\x01",
            "I'm interested in what they have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, got it.\x01",
            "(Should I go take a brief look?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B18")

    label("loc_49C7")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PThe jewelry...\x01",
            "The one in the arcade downstair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PYeah, it seems that thanks to\x01",
            "Milady Mariabell's mediation\x01",
            "we can go in too, you know?\x02\x03",
            "#00304FThat clerk pisses me off a little, but\x01",
            "I'm interested in what they have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see, got it.\x01",
            "(Should I go take a brief look?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B18")

    OP_68(-100000, 1000, -78500, 5000)

    def lambda_4B2E():

        label("loc_4B2E")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_4B2E")

    QueueWorkItem2(0x101, 2, lambda_4B2E)
    OP_93(0x104, 0x0, 0x1F4)

    def lambda_4B47():
        OP_95(0xFE, -100000, 0, -76900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4B47)
    WaitChrThread(0x104, 1)
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_93(0x104, 0x0, 0x0)

    def lambda_4B85():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4B85)
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
            "#00004F#6PAlright, let's look for KeA.\x02\x03",
            "#00008FI think that she hasn't\x01",
            "left the hotel, but...\x02\x03",
            "#00001FIf I don't find her, I'll need\x01",
            "to look into other places too.\x02",
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

    # Function_33_40AA end

    SaveToFile()

Try(main)
