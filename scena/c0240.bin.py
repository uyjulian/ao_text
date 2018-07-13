from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0240.bin",                # FileName
        "c0240",                    # MapName
        "c0240",                    # Location
        0x000F,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 15, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0240",                  # 0
        "Sammy",                  # 1
        "Kindoll",                # 2
        "Brigitta",               # 3
        "Old Man Ryｹvic",        # 4
        "Mrs. Origa",             # 5
        "Ilya",                   # 6
        "Sully",                  # 7
        "Alm",                    # 8
        "Aerie",                  # 9
        "Ponce",                  # 10
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21602.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20102.itc",                   # 07
        "chr/ch05100.itc",                   # 08
        "chr/ch10002.itc",                   # 09
        "chr/ch46300.itc",                   # 0A
        "chr/ch46200.itc",                   # 0B
        "chr/ch20200.itc",                   # 0C
    ))

    DeclNpc(9060,    10000,   18000,   45,   261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294965287, 1149,    60479,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(8470,    1019,    62380,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294921646, 1019,    60169,   180,  261,  0x0, 0,   4,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(7030,    150,     6969,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(54020,   1019,    60490,   270,  261,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(52540,   1149,    60540,   270,  261,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294921936, 1029,    61159,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294920337, 1049,    60360,   180,  389,  0x0, 0,   11,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294952177, 0,       5829,    270,  389,  0x0, 0,   12,  0,   0,   0,   0,   14,  255,  0)

    DeclActor(4294966956, 10000,   20320,   1200,    4294966956, 11500,   20320,   0x007C, 0,  18, 0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_35A",          # 03, 3
        "Function_4_731",          # 04, 4
        "Function_5_7DC",          # 05, 5
        "Function_6_1DD2",         # 06, 6
        "Function_7_315A",         # 07, 7
        "Function_8_3FEC",         # 08, 8
        "Function_9_497A",         # 09, 9
        "Function_10_4A8E",        # 0A, 10
        "Function_11_5565",        # 0B, 11
        "Function_12_55B5",        # 0C, 12
        "Function_13_561E",        # 0D, 13
        "Function_14_582C",        # 0E, 14
        "Function_15_58BC",        # 0F, 15
        "Function_16_5A4D",        # 10, 16
        "Function_17_5C13",        # 11, 17
        "Function_18_669F",        # 12, 18
        "Function_19_6A27",        # 13, 19
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32E")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_304")

    label("loc_32E")

    Return()

    # Function_1_304 end

    def Function_2_32F(): pass

    label("Function_2_32F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_2_32F")

    label("loc_359")

    Return()

    # Function_2_32F end

    def Function_3_35A(): pass

    label("Function_3_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38A")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E1")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0x8, 2310, 0, 1000, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1570, 0, 1740, 225)
    Jump("loc_730")

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_416")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -39810, 1030, 62640, 0)
    Jump("loc_730")

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E")
    SetChrFlags(0x9, 0x10)

    label("loc_45E")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, -44550, 1020, 59150, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_4EA")

    Jump("loc_730")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52E")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 5740, 1000, 62320, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_730")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_568")
    SetChrPos(0x8, -52720, 1000, 63170, 0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_730")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_598")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C8")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_635")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, -48700, 1200, 60400, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    Jump("loc_730")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    Jump("loc_730")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_730")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_730")
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -51460, 1200, 60400, 90)

    label("loc_730")

    Return()

    # Function_3_35A end

    def Function_4_731(): pass

    label("Function_4_731")

    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_753")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x2, 0x10)

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79C")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_7DB")

    Return()

    # Function_4_731 end

    def Function_5_7DC(): pass

    label("Function_5_7DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C")

    ChrTalk(
        0xFE,
        (
            "Something like that appeared in the\x01",
            "Marshlands... Though I'm worried\x01",
            "about it, I have to do my duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for Sully,\x01",
            "it seems she's been practicing\x01",
            "at Arc-en-ciel this whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to clean Lady Ilya's\x01",
            "apartment for when she gets back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9B2")

    label("loc_90C")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Sully,\x01",
            "it seems she's been practicing\x01",
            "at Arc-en-ciel this whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to clean Lady Ilya's\x01",
            "apartment for when she gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B2")

    Jump("loc_1DCE")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(
        0xFE,
        (
            "Aaah, what to do... To think something\x01",
            "like this happened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, I'll warn everyone\x01",
            "here not to go outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCE")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(
        0xFE,
        (
            "That attack... It seems\x01",
            "the Empire was behind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll never forgive them. In\x01",
            "that accident, Lady Ilya was...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCE")

    label("loc_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya lived on\x01",
            "the third floor of\x01",
            "this condo...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I saw Sully who\x01",
            "came to get luggages,\x01",
            "I finally realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Normally I'd be happy,\x01",
            "but to think that\x01",
            "happened to Lady Ilya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C40")

    label("loc_BB3")


    ChrTalk(
        0xFE,
        (
            "Sully hasn't had that\x01",
            "mischevious look on her face\x01",
            "this whole time. Poor Sully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I've got to get\x01",
            "her to cheer up somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40")

    Jump("loc_1DCE")

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(
        0xFE,
        (
            "The "Golden Sun, Silver Moon"\x01",
            "renewal performance...\x01",
            "It's finally opening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad I couldn't\x01",
            "get tickets...\x01",
            "I'll cheer them on from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh, I really wanted to see\x01",
            "Sully in action, though...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD2")

    label("loc_D3E")


    ChrTalk(
        0xFE,
        (
            "The "Golden Sun, Silver Moon"\x01",
            "renewal performance...\x01",
            "It's finally opening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh, I really wanted to see\x01",
            "Sully in action, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD2")

    Jump("loc_1DCE")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAB")

    ChrTalk(
        0xFE,
        (
            "Sully left early\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She looks nervous\x01",
            "lately... I'm a little\x01",
            "worried about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's probably feeling the pressure\x01",
            "of the renewal performance...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F13")

    label("loc_EAB")


    ChrTalk(
        0xFE,
        (
            "Sully's probably feeling\x01",
            "the pressure of the\x01",
            "renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to\x01",
            "cheer her on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13")

    Jump("loc_10B6")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1018")

    ChrTalk(
        0xFE,
        (
            "J-Just now... Lady \x01",
            "Ilya came out of \x01",
            "Sully's room on 3F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I greeted her... \x01",
            "I was so happy I cried!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Lady Ilya\x01",
            "visited Sully's room.\x01",
            "Aah, I'm so jealous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, it's actually\x01",
            "Miss Ilya's room...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B6")

    label("loc_1018")


    ChrTalk(
        0xFE,
        (
            "Aah, to think Lady Ilya visited\x01",
            "Sully's room. I'm so jealous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it's fine... \x01",
            "I'm lucky to have gotten to see\x01",
            "Lady Ilya up close like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_1DCE")

    label("loc_10BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(
        0xFE,
        (
            "I've finished cleaning\x01",
            "Mr. Ryｹvic's place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll tackle 3F next.\x01",
            "It's still a mess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCE")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1207")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Ryｹvic\x01",
            "and his wife went\x01",
            "for a drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they were going\x01",
            "as far as the state border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the quintessential leisurely\x01",
            "elderly life. I'm so jealooous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B0")

    label("loc_1207")


    ChrTalk(
        0xFE,
        (
            "Huh, come to think of it...\x01",
            "I feel like Mr. Ryｹvic and his\x01",
            "wife have been fighting, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess it's fine.\x01",
            "Anyway, they did ask me\x01",
            "to clean for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B0")

    Jump("loc_1DCE")

    label("loc_12B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138E")

    ChrTalk(
        0xFE,
        (
            "The next Arc-en-ciel\x01",
            "renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sully, who lives on 3F, is\x01",
            "one of the co-stars, and it'll\x01",
            "be a huge promotion for her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eek, how amazing!\x01",
            "I really want to see it!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FF")

    label("loc_138E")


    ChrTalk(
        0xFE,
        (
            "Aah... I really want\x01",
            "to see Sully's big\x01",
            "moment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, I missed\x01",
            "my chance to buy\x01",
            "tickets. *siiigh*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FF")

    Jump("loc_1DCE")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F1")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Ryｹvic and\x01",
            "his wife are fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a heavy atmosphere when\x01",
            "I went to collect my payment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm not even a person concerned,\x01",
            "but I ended up being concerned for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157B")

    label("loc_14F1")


    ChrTalk(
        0xFE,
        (
            "It seems Mr. Ryｹvic and\x01",
            "Mrs. Origa are fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wish they'd give me a break.\x01",
            "I'll end up being concerned for them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157B")

    Jump("loc_1DCE")

    label("loc_1580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_16C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")

    ChrTalk(
        0xFE,
        (
            "It seems that today each nations'\x01",
            "VIPs are going to come to the\x01",
            "theatre to see the Arc-en-ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uuhm, they're going to enjoy it\x01",
            "from some nice seats for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grrr, I'm so envious!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16C4")

    label("loc_165F")


    ChrTalk(
        0xFE,
        (
            "In the end, I failed to buy the tickets\x01",
            "for the next renewal public performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*...\x02",
    )

    CloseMessageWindow()

    label("loc_16C4")

    Jump("loc_1DCE")

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_183F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1799")

    ChrTalk(
        0xFE,
        (
            "Did you hear? There's a rumor that\x01",
            "they'll be doing a renewal performance\x01",
            "of "Golden Sun, Silver Moon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm looking forward to it.\x01",
            "I've got to hurry and buy tickets!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_183A")

    label("loc_1799")


    ChrTalk(
        0xFE,
        (
            "It seems Arc-en-ciel is doing\x01",
            "a renewal performance of\x01",
            ""Golden Sun, Silver Moon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is something I can't miss...\x01",
            "I've got to hurry and buy tickets!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183A")

    Jump("loc_1DCE")

    label("loc_183F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(
        0xFE,
        (
            "Mr. Ryｹvic on 1F was\x01",
            "considering remodeling\x01",
            "the mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he had all the\x01",
            "required mira, but in the\x01",
            "end his wife stopped him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I was surprised.\x01",
            "First of all, even he says that to me,\x01",
            "I'm just a hired caretaker...right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F8")

    label("loc_194E")


    ChrTalk(
        0xFE,
        (
            "Mr. Ryｹvic is a former\x01",
            "congressman and very wealthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But just because of that, I can't\x01",
            "believe he could come up with the\x01",
            "idea of trying to remodel the mansion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_1DCE")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC7")

    ChrTalk(
        0xFE,
        (
            "My timing is always\x01",
            "poor, so I never see\x01",
            "the 3F resident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ran into her this\x01",
            "morning and greeted her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She said her name is\x01",
            "Sully and she's an\x01",
            "Arc-en-ciel trainee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it seems she's still unknown.\x01",
            "I'll have to check up on her from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Sully is freeloading\x01",
            "in Miss Ilya's room, if I'm\x01",
            "remembering it right...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(It seems she hasn't\x01",
            "noticed that Miss Ilya's\x01",
            "room is on 3F.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C7C")

    label("loc_1BC7")


    ChrTalk(
        0xFE,
        (
            "But, Arc-en-ciel pays\x01",
            "very well, don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because, even though she's a trainee,\x01",
            "she lives in that huge apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(It's really Miss Ilya's\x01",
            "room, though...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7C")

    Jump("loc_1DCE")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6E")

    ChrTalk(
        0xFE,
        (
            "I am this\x01",
            "apartment's hired\x01",
            "caretaker, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place is spacious and\x01",
            "beautiful. I'd like to live\x01",
            "in a place like this, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But it's too spacious, and a\x01",
            "little difficult to clean, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DCE")

    label("loc_1D6E")


    ChrTalk(
        0xFE,
        (
            "Hmm, I have to clean\x01",
            "the garden later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, being a caretaker sure is hard work.\x02",
    )

    CloseMessageWindow()

    label("loc_1DCE")

    TalkEnd(0xFE)
    Return()

    # Function_5_7DC end

    def Function_6_1DD2(): pass

    label("Function_6_1DD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(
        0xFE,
        (
            "It seems the President constructed\x01",
            "suspicious facilities inside Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I worked on the exterior design of Orchis\x01",
            "Tower and he made questionable revisions...\x01",
            "It was misusing the building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've all been deceived. Good grief.\x01",
            "I can't possibly forgive him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FA1")

    label("loc_1F06")


    ChrTalk(
        0xFE,
        (
            "It seems the President constructed\x01",
            "suspicious facilities inside Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've all been deceived. Good grief.\x01",
            "I can't possibly forgive him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA1")

    Jump("loc_3156")

    label("loc_1FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2076")

    ChrTalk(
        0xFE,
        (
            "T-That President... Who would\x01",
            "have thought he'd go this far!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was thankful he entrusted\x01",
            "me with Orchis Tower's\x01",
            "exterior design, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He can no longer be trusted.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20AB")

    label("loc_2076")


    ChrTalk(
        0xFE,
        (
            "That President... \x01",
            "He can no longer be trusted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    Jump("loc_3156")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2159")

    ChrTalk(
        0xFE,
        (
            "Thanks to this, I'm no\x01",
            "longer employable in the\x01",
            "Empire or Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guh, I would have wanted them to at\x01",
            "least let me finish my current work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2265")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower was\x01",
            "protected thanks\x01",
            "to Mr. Arios, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad about the IBC\x01",
            "building, though. It was also\x01",
            "a symbol of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like the criminals are\x01",
            "poking fun at the history of\x01",
            "Crossbell itself. Unforgivable!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C5")

    label("loc_2265")


    ChrTalk(
        0xFE,
        (
            "The IBC building was also\x01",
            "a symbol of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Those criminals can't be forgiven!\x02",
    )

    CloseMessageWindow()

    label("loc_22C5")

    Jump("loc_3156")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_251D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248E")

    ChrTalk(
        0xFE,
        (
            "............\x01",
            ".........Huh!\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_238E")
    Jump("loc_23D8")

    label("loc_238E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23D8")

    label("loc_23AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23D8")

    label("loc_23CE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23D8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "...Do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to concentrate on drawing up these\x01",
            "blueprints. Sorry, but please don't interrupt me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2518")

    label("loc_248E")


    ChrTalk(
        0xFE,
        (
            "Lately, I've been able\x01",
            "to focus on work better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But not being able to see the surroundings\x01",
            "at all it's its drawback, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2518")

    Jump("loc_3156")

    label("loc_251D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25B3")

    ChrTalk(
        0xFE,
        (
            "Why does the sound\x01",
            "of the rain make\x01",
            "me feel this good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'm making good progress\x01",
            "on these blueprints too, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_25B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2625")

    ChrTalk(
        0xFE,
        (
            "Hmm... It's awfully\x01",
            "noisy outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, those sirens... \x01",
            "Was there some kind of accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_2625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B6")

    ChrTalk(
        0xFE,
        (
            "I wonder if I'm getting any closer to\x01",
            "my grandfather, a great architect...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Hmm. Anyway, I'm working now.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2711")

    label("loc_26B6")


    ChrTalk(
        0xFE,
        (
            "A request for plans should've\x01",
            "come in from the Empire...\x01",
            "I think I'll start on those.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2711")

    Jump("loc_3156")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27C7")

    ChrTalk(
        0xFE,
        (
            "I feel relieved now that the Orchis\x01",
            "Tower inauguration ceremony is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I want to work on different\x01",
            "kind of jobs for a change of attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3156")

    label("loc_27C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_298A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EA")

    ChrTalk(
        0xFE,
        (
            "I handled Orchis Tower's exterior\x01",
            "design, but I don't understand its\x01",
            "connection with the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The interior design was handled by\x01",
            "another architect the mayor recommended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think I learned in person the\x01",
            "importance of working with others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2985")

    label("loc_28EA")


    ChrTalk(
        0xFE,
        (
            "Planning for Orchis Tower's\x01",
            "interior design was handled\x01",
            "by another architect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I learned in person the\x01",
            "importance of working with others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2985")

    Jump("loc_3156")

    label("loc_298A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABD")

    ChrTalk(
        0xFE,
        (
            "The orbal network had its merit\x01",
            "in the circumstance of the Orchis\x01",
            "Tower speedy completion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among the construction staff,\x01",
            "plans and such were exchanged\x01",
            "over the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That connected to the\x01",
            "efficiency of their work...\x01",
            "Technological progress sure is amazing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B6F")

    label("loc_2ABD")


    ChrTalk(
        0xFE,
        (
            "Information was exchanged over\x01",
            "the orbal network during the\x01",
            "construction of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I understand why\x01",
            "the mayor passed legislation\x01",
            "to promote its use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6F")

    Jump("loc_3156")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B82")
    Jump("loc_3156")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C29")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, the exterior of\x01",
            ""Orchis Tower" that I designed\x01",
            "will finally be revealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "Despite my age, I'm\x01",
            "nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CCA")

    label("loc_2C29")


    ChrTalk(
        0xFE,
        (
            "Tomorrow, "Orchis Tower" is\x01",
            "finally going to be unveiled, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the inauguration ceremony,\x01",
            "I think I'll go say hello to\x01",
            "the construction staff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCA")

    Jump("loc_3156")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E90")

    ChrTalk(
        0xFE,
        (
            "City Hall... No, I guess it's the\x01",
            "City Meeting Hall now. That building\x01",
            "was designed by my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandfather was a great architect. He\x01",
            "had a hand in the design of almost all\x01",
            "of Crossbell's oldest public buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an architect, my aim is to be\x01",
            "as great as my grandfather was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I, his grandson, designed the\x01",
            "exterior of the new City Hall building...\x01",
            "Life sure is interesting, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5B")

    label("loc_2E90")


    ChrTalk(
        0xFE,
        (
            "My grandfather was a great\x01",
            "architect. He designed the\x01",
            "current City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I, his grandson, designed the\x01",
            "exterior of the new City Hall building...\x01",
            "Life sure is interesting, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5B")

    Jump("loc_3156")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CD")

    ChrTalk(
        0xFE,
        (
            "Crossbell's new City Hall\x01",
            "building is finally complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only because the new mayor\x01",
            "took over the construction planning\x01",
            "that it was able to come this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of a temporary budget freeze,\x01",
            "the project was in danger, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that I, who participated in the\x01",
            "external design, will be able to settle down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3156")

    label("loc_30CD")


    ChrTalk(
        0xFE,
        (
            "I participated in the new City Hall\x01",
            "building external design as an architect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be completed soon...\x01",
            "That's deeply moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3156")

    TalkEnd(0xFE)
    Return()

    # Function_6_1DD2 end

    def Function_7_315A(): pass

    label("Function_7_315A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3377")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B6")

    ChrTalk(
        0xFE,
        (
            "Despite his anger towards the President, \x01",
            "my husband started work on his next project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of what happened to the city, reconstruction\x01",
            "requests for crime prevention and security have come\x01",
            "in from all sorts of companies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I earnestly want him to deal with works\x01",
            "without being stucked on the Tower.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3372")

    label("loc_32B6")


    ChrTalk(
        0xFE,
        (
            "Reconstruction requests for crime prevention and\x01",
            "security have come in from all sorts of companies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I earnestly want him to deal with works\x01",
            "without being stucked on the Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3372")

    Jump("loc_3FE8")

    label("loc_3377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33EA")

    ChrTalk(
        0xFE,
        (
            "There's no sign of those monsters\x01",
            "outside in any buildings, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Scary things are scary.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_33EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3472")

    ChrTalk(
        0xFE,
        (
            "I was surprised at\x01",
            "the asset freeze\x01",
            "IBC declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I wonder if something like\x01",
            "this will really be all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3564")

    ChrTalk(
        0xFE,
        (
            "To think enemies attacked the city. \x01",
            "What a terrifying incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was hardly any damage\x01",
            "around here, but I'm worried\x01",
            "about what will happen next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope nothing like this\x01",
            "happens again, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35DE")

    label("loc_3564")


    ChrTalk(
        0xFE,
        (
            "To think enemies attacked the city. \x01",
            "What a terrifying incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope nothing like this\x01",
            "happens again, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35DE")

    Jump("loc_3FE8")

    label("loc_35E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3677")

    ChrTalk(
        0xFE,
        (
            "Somehow,, various incidents have\x01",
            "been occurring recently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until a little while ago,\x01",
            "hardly any incidents occurred...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_37C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3726")

    ChrTalk(
        0xFE,
        (
            "This isn't good... I was\x01",
            "thinking of going shopping at\x01",
            "the department store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll just have to\x01",
            "bring my umbrella with me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37BF")

    label("loc_3726")


    ChrTalk(
        0xFE,
        (
            "They have some good coffee beans\x01",
            "at the imported goods general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they get wet their flavor will be\x01",
            "ruined, so I wish it hadn't rained.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BF")

    Jump("loc_3FE8")

    label("loc_37C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3809")

    ChrTalk(
        0xFE,
        (
            "Let's see, my husband's\x01",
            "favorite Liberl coffee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391E")

    ChrTalk(
        0xFE,
        (
            "My husband has struggled\x01",
            "with a grandfather complex\x01",
            "for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, because of his involvement in the\x01",
            "Orchis Tower exterior design, I think\x01",
            "he's gotten a lot more positive lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It became a work he\x01",
            "himself is confident of.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39C1")

    label("loc_391E")


    ChrTalk(
        0xFE,
        (
            "It seems my husband's\x01",
            "grandfather complex\x01",
            "has faded a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe his confidence has improved\x01",
            "due to his involvement in the\x01",
            "Orchis Tower exterior design.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C1")

    Jump("loc_3FE8")

    label("loc_39C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A69")

    ChrTalk(
        0xFE,
        (
            "To help my husband with his work,\x01",
            "I'll make some coffee for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I'm using Liberl beans today,\x01",
            "I'm sure it will have a nice aroma.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B01")

    ChrTalk(
        0xFE,
        (
            "Actually, some\x01",
            "new work came\x01",
            "in this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because my husband\x01",
            "work on the tower has ended,\x01",
            "it doesn't mean he can rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3BC7")

    ChrTalk(
        0xFE,
        (
            "That husband of mine, I didn't\x01",
            "even ask and he's teaching me many\x01",
            "things about the Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it seems his excitement for the\x01",
            "unveiling at noon is not wearing off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C86")

    ChrTalk(
        0xFE,
        (
            "My husband, who was involved in\x01",
            "the design of Orchis Tower,\x01",
            "attended its inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Around now, he should be basking\x01",
            "in the celebration of its completion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D05")

    ChrTalk(
        0xFE,
        (
            "It was a really big job this time,\x01",
            "and my husband seems nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe some coffee\x01",
            "will calm him down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE8")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD6")

    ChrTalk(
        0xFE,
        (
            "I often hear about my\x01",
            "husband's grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he was an excellent architect,\x01",
            "and my husband uses him as a benchmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he might\x01",
            "have a bit of a\x01",
            "complex.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E78")

    label("loc_3DD6")


    ChrTalk(
        0xFE,
        (
            "It seems my husband has a bit of\x01",
            "a complex toward his grandfather,\x01",
            "an excellent architect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband is doing his best,\x01",
            "and that's good enough for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E78")

    Jump("loc_3FE8")

    label("loc_3E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F75")

    ChrTalk(
        0xFE,
        (
            "My husband had formal involvement with\x01",
            "the new City Hall building's design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a big job\x01",
            "and kept him busy\x01",
            "for the last whole month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he seems relieved now that\x01",
            "it's been settled for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FE8")

    label("loc_3F75")


    ChrTalk(
        0xFE,
        (
            "Our home serves as\x01",
            "a design office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, we were very busy with designing\x01",
            "the new City Hall building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE8")

    TalkEnd(0xFE)
    Return()

    # Function_7_315A end

    def Function_8_3FEC(): pass

    label("Function_8_3FEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4086")

    ChrTalk(
        0xFE,
        (
            "As I thought, the world is\x01",
            "getting more dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll build an underground shelter\x01",
            "somewhere and hide in with my wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4976")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_40F1")

    ChrTalk(
        0xFE,
        (
            "Hmmm, I wonder if my\x01",
            "car's safe outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's damaged, I'll\x01",
            "demand restitution.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4976")

    label("loc_40F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40FF")
    Jump("loc_4976")

    label("loc_40FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4313")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413B")
    Call(0, 19)
    Return()

    label("loc_413B")


    ChrTalk(
        0xFE,
        (
            "Geval should be staying\x01",
            "in Armorica Village now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure you'll find him if you look around.\x01",
            "You should ask him about his situation directly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_430E")

    label("loc_41D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C9")

    ChrTalk(
        0xFE,
        (
            "I went to the charity event\x01",
            "hall to donate the mira I got\x01",
            "from selling old furniture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be put to\x01",
            "better use than if\x01",
            "I were to spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone has it hard right now.\x01",
            "We need to help each other out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_430E")

    label("loc_42C9")


    ChrTalk(
        0xFE,
        (
            "Everyone has it hard right now.\x01",
            "We need to help each other out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_430E")

    Jump("loc_4976")

    label("loc_4313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4450")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D9")

    ChrTalk(
        0xFE,
        (
            "An armed group occupying\x01",
            "a town? That's unheard of!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were to drive in that\x01",
            "direction, I might become\x01",
            "involved as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, how dreadful.\x01",
            "*shivers*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_444B")

    label("loc_43D9")


    ChrTalk(
        0xFE,
        (
            "If I were to drive in that\x01",
            "direction, I might become\x01",
            "involved as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, how dreadful.\x01",
            "*shivers*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444B")

    Jump("loc_4976")

    label("loc_4450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_44B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446B")
    Call(0, 13)
    Jump("loc_44B4")

    label("loc_446B")


    ChrTalk(
        0xFE,
        (
            "(Hmm... How that\x01",
            "Alm has grown...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(Even so, that idiot is...)\x02",
    )

    CloseMessageWindow()

    label("loc_44B4")

    Jump("loc_4976")

    label("loc_44B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_44C7")
    Jump("loc_4976")

    label("loc_44C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44D5")
    Jump("loc_4976")

    label("loc_44D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4565")

    ChrTalk(
        0xFE,
        (
            "I tried to invite my wife\x01",
            "to a drive I had planned\x01",
            "to do tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope I'll be able to cheer\x01",
            "her up a little, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4976")

    label("loc_4565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463C")

    ChrTalk(
        0xFE,
        (
            "I've been quarrelling with my\x01",
            "wife since yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. It's painful having\x01",
            "a cold war when we live\x01",
            "together like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'll have to make up\x01",
            "with my wife somehow...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46AF")

    label("loc_463C")


    ChrTalk(
        0xFE,
        (
            "Just how can I make up\x01",
            "with my wife, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps some expensive wine...\x01",
            "No, no, that won't work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46AF")

    Jump("loc_4976")

    label("loc_46B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_475A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CF")
    Call(0, 9)
    Jump("loc_4755")

    label("loc_46CF")


    ChrTalk(
        0xFE,
        (
            "I thought we would've drunk it together\x01",
            "and so I went to buy a good wine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, enough already.\x01",
            "I'll drink it alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4755")

    Jump("loc_4976")

    label("loc_475A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4768")
    Jump("loc_4976")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47FB")

    ChrTalk(
        0xFE,
        (
            "I wanted a garage to\x01",
            "protect my car from\x01",
            "the rain, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She got so mad at me, so I\x01",
            "had to abandon the idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4832")

    label("loc_47FB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, but I wish she\x01",
            "didn't get so mad at me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4832")

    Jump("loc_4976")

    label("loc_4837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_496D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48DB")

    ChrTalk(
        0xFE,
        (
            "Hmm. My car outside\x01",
            "will get wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have wanted\x01",
            "a garage, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose it's fine. I'll\x01",
            "have it washed tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4968")

    label("loc_48DB")


    ChrTalk(
        0xFE,
        (
            "But at this rate, the\x01",
            "weather will wear out\x01",
            "my orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's hard living in an\x01",
            "apartment and not being\x01",
            "able to install a garage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4968")

    Jump("loc_4976")

    label("loc_496D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4976")

    label("loc_4976")

    TalkEnd(0xFE)
    Return()

    # Function_8_3FEC end

    def Function_9_497A(): pass

    label("Function_9_497A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "Aah, as I thought, this\x01",
            "wine is delicious. I'm\x01",
            "glad I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems you don't want any,\x01",
            "my dear, so I'll drink it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Yes, do as you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You paid a lot of mira\x01",
            "for it, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Hmph!\x01",
            "*gluglugluglug*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_9_497A end

    def Function_10_4A8E(): pass

    label("Function_10_4A8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B50")

    ChrTalk(
        0xFE,
        (
            "That husband of mine. It's not like we have\x01",
            "the mira to buy an underground shelter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he can't get out his bad habit of\x01",
            "buying all manners of expensive things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4BCA")

    ChrTalk(
        0xFE,
        (
            "Good grief. Of all things, for that husband of mine\x01",
            "to be worried about his car at a time like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C9D")

    ChrTalk(
        0xFE,
        (
            "I heard the address and... It seems\x01",
            "the Empire and Republic have been\x01",
            "fighting in secret over Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To those of us who live here, it's something\x01",
            "that absolutely can't be forgiven...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D43")

    ChrTalk(
        0xFE,
        (
            "My husband gave a donation\x01",
            "for city reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought he only spent mira\x01",
            "on himself. It seems I'll need\x01",
            "to rethink my opinion of him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4DA7")

    ChrTalk(
        0xFE,
        (
            "To think such a major\x01",
            "incident occurred...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the CGF\x01",
            "resolves it soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E09")

    ChrTalk(
        0xFE,
        (
            "Alm brought his\x01",
            "family to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Anyway, \x01",
            "I'm glad he's happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E17")
    Jump("loc_5561")

    label("loc_4E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E25")
    Jump("loc_5561")

    label("loc_4E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ED9")

    ChrTalk(
        0xFE,
        (
            "I don't know what caused it,\x01",
            "but my husband invited me to\x01",
            "come with him on a drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. Does he really\x01",
            "think something like that\x01",
            "will butter me up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F51")

    ChrTalk(
        0xFE,
        (
            "I've decided not to\x01",
            "speak to my husband\x01",
            "for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As if I'd forgive him\x01",
            "before he apologizes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_4F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6C")
    Call(0, 9)
    Jump("loc_4F9E")

    label("loc_4F6C")


    ChrTalk(
        0xFE,
        (
            "...Hmph, who cares about\x01",
            "what my husband do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F9E")

    Jump("loc_5561")

    label("loc_4FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_50C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507A")

    ChrTalk(
        0xFE,
        (
            "My husband bought an\x01",
            "expensive vintage wine\x01",
            "without saying a word to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And after I got so mad after the\x01",
            "garage incident the other day... \x01",
            "Good grief. He's totally unrepentant.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50C3")

    label("loc_507A")


    ChrTalk(
        0xFE,
        (
            "That husband of mine...\x01",
            "As if I'd approve of\x01",
            "his wasteful spending.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C3")

    Jump("loc_5561")

    label("loc_50C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D3")

    ChrTalk(
        0xFE,
        (
            "That husband of mine... He tried\x01",
            "to add a garage to our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to talk him out of it \x01",
            "somehow, but Miss Sammy, who he\x01",
            "consulted with, was dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. I'm in shock at his\x01",
            "level of wasteful spending.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_525C")

    label("loc_51D3")


    ChrTalk(
        0xFE,
        (
            "That husband of mine... He tried\x01",
            "to add a garage to our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. I'm in shock at his\x01",
            "level of wasteful spending.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525C")

    Jump("loc_5561")

    label("loc_5261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5330")

    ChrTalk(
        0xFE,
        (
            "On rainy days like this,\x01",
            "I focus on my hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, my hobby is\x01",
            "handicrafts. Lately, I've\x01",
            "been making a quilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*stitching*... \x01",
            "This is rather complex and fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53D6")

    label("loc_5330")


    ChrTalk(
        0xFE,
        (
            "My hobby is handicrafts.\x01",
            "Lately, I've been\x01",
            "enjoying making a quilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would have been nice if my\x01",
            "husband picked a hobby that\x01",
            "doesn't cost much, like mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D6")

    Jump("loc_5561")

    label("loc_53DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DF")

    ChrTalk(
        0xFE,
        "My husband's wasteful spending is troublesome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a long time, he's done\x01",
            "things like replace furniture\x01",
            "we didn't need to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just the other day, he went\x01",
            "and bought an orbal car. \x01",
            "Goodness gracious, I can't even...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5561")

    label("loc_54DF")


    ChrTalk(
        0xFE,
        (
            "Without discussing anything with me,\x01",
            "he went and bought an orbal car...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That man's wasteful\x01",
            "spending is a real problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5561")

    TalkEnd(0xFE)
    Return()

    # Function_10_4A8E end

    def Function_11_5565(): pass

    label("Function_11_5565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557A")
    Call(0, 13)
    Jump("loc_55B1")

    label("loc_557A")


    ChrTalk(
        0xFE,
        (
            "Alright, today we'll go to\x01",
            "the hospital, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55B1")

    TalkEnd(0xFE)
    Return()

    # Function_11_5565 end

    def Function_12_55B5(): pass

    label("Function_12_55B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CA")
    Call(0, 13)
    Jump("loc_561A")

    label("loc_55CA")


    ChrTalk(
        0xFE,
        (
            "Uh uh, it was just a tiny bit, but\x01",
            "we are steadily getting closer to him㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561A")

    TalkEnd(0xFE)
    Return()

    # Function_12_55B5 end

    def Function_13_561E(): pass

    label("Function_13_561E")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "I see, then he was discharged a\x01",
            "few months ago from St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes. I don't know what\x01",
            "happened after that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You've come all this\x01",
            "way. I'm sorry I could\x01",
            "only tell you this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No, don't worry about it.\x01",
            "You've helped us a lot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        "Right, dear㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xF,
        (
            "Yes, Aerie. It's a spectacular\x01",
            "victory for the three of us!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Baby",
        "Gaa, gaa♪\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xB,
        (
            "Ha ha. You all are\x01",
            "really very close.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xF, 0x87, 0x0)
    OP_93(0x10, 0xB4, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_13_561E end

    def Function_14_582C(): pass

    label("Function_14_582C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I-I couldn't even imagine\x01",
            "something like this happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway... I have to\x01",
            "save this moment in as\x01",
            "many photos as possible.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_582C end

    def Function_15_58BC(): pass

    label("Function_15_58BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D1")
    Call(0, 17)
    Jump("loc_5A49")

    label("loc_58D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A02")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "#04206F*pant, pant, pant*...\x02\x03",
            "#04201FSay, Miss Ilya. Is\x01",
            "this good enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FHmm, you're still a little tense.\x01",
            "You should loose up a little more.\x02\x03",
            "#01702FAnyway, just listen to me,\x01",
            "keep quiet and do what I say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04206FOoh... How long is\x01",
            "this going to go on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    Jump("loc_5A49")

    label("loc_5A02")


    ChrTalk(
        0xE,
        (
            "#04206FOoh... I'll do\x01",
            "whatever you want,\x01",
            "just make it stop quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A49")

    TalkEnd(0xFE)
    Return()

    # Function_15_58BC end

    def Function_16_5A4D(): pass

    label("Function_16_5A4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A62")
    Call(0, 17)
    Jump("loc_5C0F")

    label("loc_5A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B57")

    ChrTalk(
        0xD,
        (
            "#01700FUh uh. If you like, I'll\x01",
            "massage you guys too.\x02\x03",
            "#01709FI personally prefer\x01",
            "females, though㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI-I think I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04206F(*sigh*, if she's like this\x01",
            "when sober, I give up...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C0F")

    label("loc_5B57")


    ChrTalk(
        0xD,
        (
            "#01700FI've got to loosen Sully up\x01",
            "for tonight's performance.\x02\x03",
            "#01709FWe've got to make sure we have no\x01",
            "regrets... I'll massage the ladies, ok㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04206F(I-I don't get it...)\x02",
    )

    CloseMessageWindow()

    label("loc_5C0F")

    TalkEnd(0xFE)
    Return()

    # Function_16_5A4D end

    def Function_17_5C13(): pass

    label("Function_17_5C13")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51814.itc", 0x1E)
    OP_68(51500, 2300, 59170, 0)
    MoveCamera(58, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 51430, 1050, 58470, 45)
    SetChrPos(0x102, 50280, 1050, 58640, 45)
    SetChrPos(0x104, 51460, 1000, 57280, 45)
    SetChrPos(0x109, 49800, 1050, 57410, 45)
    SetChrPos(0x105, 50350, 1000, 56530, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    SetChrSubChip(0xE, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#11P#01709FOh, hey there younger brother☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04205F#5PH-Hey...\x02\x03",
            "#04206F...Owowowowow!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FW-What're you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01704FUh uh, those heads of\x01",
            "state are coming to our\x01",
            "theatre tonight, but...\x02\x03",
            "#01702FSully is helping out\x01",
            "in a minor role too.\x02\x03",
            "#01709FI've got to limber her up.\x01",
            "It's massage time! Here we go!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(50)
    SetChrSubChip(0xE, 0x0)

    def lambda_5E2E():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5E2E)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#04212F#11P#4SOoooooooww!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00102FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FU-Umm, are you all right?\x02\x03",
            "#10106FI've heard it has the opposite\x01",
            "effect if done by amateurs, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#11P#01704FUh uh, no need to worry.\x02\x03",
            "#01702FI had a pro masseuse\x01",
            "instruct me, so I'm a\x01",
            "total master now, I guess.\x02\x03",
            "I do this a lot to Rixia too during\x01",
            "our stretching in practices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FI see. So you'll turn\x01",
            "to any field if it's to\x01",
            "help your plays, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FAh, that's Miss Ilya for you!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "#04206F#5PNononono... Painful\x01",
            "things are painful!!\x02\x03",
            "#04201FM-Miss Ilya, is this really,\x01",
            "really all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01706FI already told\x01",
            "you it's fine...\x02\x03",
            "#01700FYou're in pain because you're nervous about\x01",
            "tonight's play and your body's gotten stiff.\x02\x03",
            "#01709FDon't worry. If I keep it up,\x01",
            "you'll get used to it eventually㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04207F#5PH-How suspicious can you get!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01701FQuiet, you. To shut you up... \x01",
            "How about this!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x2)
    SetChrPos(0xD, 53710, 1200, 60530, 270)
    OP_A6(0xD, 0x0, 0x14, 0x190, 0x1388)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x2)
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0xE,
        "#5P#04212F#5SWhaaaa!?\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xE,
        "#5P#04207FW-W-W-Where're you touching!?!?\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    SetChrSubChip(0xE, 0x1)

    ChrTalk(
        0xD,
        (
            "#11P#01709FMwuhuhu, don't worry. \x01",
            "This massage is particularly effective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04207F#5PS-Stop lying!!\x02\x03",
            "#04209FAhaha, t-that tickles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01709FHmmhmm, growing up, aren't you?㈱ \x01",
            "Unexpectedly there could be\x01",
            "hope for you in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04212F#5PW-Who cares!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#00113FAs you might expect, I'm a little\x01",
            "worried about this scene, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FHu hu, I'm sure all of this has its own meaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha. Somehow, it seems\x01",
            "that Sully is getting\x01",
            "used to Arc-en-ciel.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5P#04207FD-Don't summarize!\x01",
            "Help me out here!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#01709FNow, now. I'm not letting you gooo.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrPos(0xD, 54020, 1020, 60490, 270)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_4C(0xD, 0xFF)
    OP_93(0xD, 0x10E, 0x0)
    SetChrPos(0x0, 50040, 1050, 57020, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x14C, 5)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_17_5C13 end

    def Function_18_669F(): pass

    label("Function_18_669F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6898")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya and Sully's voices\x01",
            "can be heard from\x01",
            "beyond the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Sully's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Aha, ah ha ha ha...\x01",
            "I told you, not there!\x02\x03",
            "*pant, pant*... Miss Ilya,\x01",
            "have you been doing that on\x01",
            "purpose this whole time?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Ilya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, no, it's just your imagination㈱\x02",
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
        "#00012FIt seems Miss Ilya is enjoying herself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FPoor Sully...\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetScenarioFlags(0x0, 7)
    Jump("loc_69F8")

    label("loc_6898")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya and Sully's voices\x01",
            "can be heard from\x01",
            "beyond the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Sully's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "*pant, pant, pant*... \x01",
            "How long is this going to go on?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Ilya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You know, it'd be over\x01",
            "sooner if you just\x01",
            "went along with it㈱\x02",
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

    label("loc_69F8")

    Jump("loc_6A23")

    label("loc_69FD")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6A23")

    TalkEnd(0xFF)
    Return()

    # Function_18_669F end

    def Function_19_6A27(): pass

    label("Function_19_6A27")

    EventBegin(0x0)
    Fade(500)
    OP_68(-42750, 2270, 60900, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23950, 0)
    SetChrPos(0xB, -40610, 1030, 60630, 270)
    SetChrPos(0x101, -42710, 1020, 61350, 90)
    SetChrPos(0x102, -42900, 1020, 60110, 90)
    SetChrPos(0x103, -44070, 1020, 61440, 90)
    SetChrPos(0x104, -44470, 1020, 60240, 90)
    SetChrPos(0x109, -45710, 1020, 61170, 90)
    SetChrPos(0x105, -45790, 1020, 59690, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#2POh, it's all of you...\x01",
            "Do you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FPardon the sudden\x01",
            "visit, but...\x02\x03",
            "#00000FDo you know the\x01",
            "name "Geval"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#2PHmm, you know him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PI did indeed look after him\x01",
            "when he was a congressman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, bingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FUmm, you see...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they were looking for Geval\x01",
            "to reunite him with his son and his wife.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#2PHmm, I see. So you received a\x01",
            "request from them, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PActually, Geval came to me the\x01",
            "other day asking me the best\x01",
            "way to "hide from Crossbell."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PMy goodness. That idiot...\x01",
            "His son and wife make such a nice\x01",
            "couple. What is he running from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FIt seems you know\x01",
            "where Mr. Geval went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FBut why is\x01",
            "he hiding?\x02\x03",
            "#00303FI don't really get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI-I know! Even though\x01",
            "Alm and Aerie said\x01",
            "they want to see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PHmm, this probably seems\x01",
            "trivial to an outsider, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2P...No,\x01",
            "I won't say it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2P...He should be staying in\x01",
            "Armorica Village right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PI'm sure you'll find him if you look around.\x01",
            "You should ask him about his situation directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUnderstood...\x01",
            "And thank you very much.\x02\x03",
            "#00000FLet's head for Armorica\x01",
            "Village immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x90, 0x1, 0x2)
    SetScenarioFlags(0x19B, 0)
    OP_4C(0xB, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -49950, 1000, 56930, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_19_6A27 end

    SaveToFile()

Try(main)
