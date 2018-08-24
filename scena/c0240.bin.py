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
        "Function_6_1D55",         # 06, 6
        "Function_7_3070",         # 07, 7
        "Function_8_3EAC",         # 08, 8
        "Function_9_4831",         # 09, 9
        "Function_10_4947",        # 0A, 10
        "Function_11_5415",        # 0B, 11
        "Function_12_5464",        # 0C, 12
        "Function_13_54BB",        # 0D, 13
        "Function_14_56C4",        # 0E, 14
        "Function_15_5754",        # 0F, 15
        "Function_16_58D1",        # 10, 16
        "Function_17_5A8C",        # 11, 17
        "Function_18_6501",        # 12, 18
        "Function_19_6883",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")

    ChrTalk(
        0xFE,
        (
            "Something like that appearing in the\x01",
            "Marshlands... Though I'm worried about\x01",
            "it, I have my duties to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for Sully, it\x01",
            "seems she's been practicing at\x01",
            "Arc-en-Ciel this whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to clean Ilya's\x01",
            "apartment for when she\x01",
            "gets back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9B0")

    label("loc_90F")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Sully, it\x01",
            "seems she's been practicing at\x01",
            "Arc-en-Ciel this whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to clean Ilya's\x01",
            "apartment for when she\x01",
            "gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B0")

    Jump("loc_1D51")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A47")

    ChrTalk(
        0xFE,
        (
            "Ah, what to do... To\x01",
            "think something like this\x01",
            "happened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, I'll warn\x01",
            "everyone here not to go\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ACD")

    ChrTalk(
        0xFE,
        (
            "That attack... It seems\x01",
            "the Empire was behind\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll never forgive them.\x01",
            "In that accident, Lady\x01",
            "Ilya was...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA8")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya lived on the\x01",
            "third floor of this\x01",
            "condo...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I saw Sully\x01",
            "bringing packages here,\x01",
            "I finally realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Normally I'd be\x01",
            "happy, but to think that\x01",
            "happened to Ilya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C35")

    label("loc_BA8")


    ChrTalk(
        0xFE,
        (
            "Sully hasn't had that\x01",
            "mischievous look on her face\x01",
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

    label("loc_C35")

    Jump("loc_1D51")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D31")

    ChrTalk(
        0xFE,
        (
            "The Golden Sun, Silver Moon\x01",
            "renewal performance... It's\x01",
            "finally opening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad I couldn't\x01",
            "get tickets... I'll\x01",
            "cheer them on from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh, I really wanted to\x01",
            "see Sully in action,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC3")

    label("loc_D31")


    ChrTalk(
        0xFE,
        (
            "The Golden Sun, Silver Moon\x01",
            "renewal performance... It's\x01",
            "finally opening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh, I really wanted to\x01",
            "see Sully in action,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC3")

    Jump("loc_1D51")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA5")

    ChrTalk(
        0xFE,
        (
            "Sully left early this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been looking\x01",
            "nervous lately... I'm a\x01",
            "little worried about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's probably feeling\x01",
            "the pressure of the\x01",
            "renewal performance...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F0D")

    label("loc_EA5")


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
            "I've got to cheer her\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0D")

    Jump("loc_10AC")

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100F")

    ChrTalk(
        0xFE,
        (
            "J-Just now... Sully came\x01",
            "out of Lady Ilya's room\x01",
            "on 3F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I greeted her... I was\x01",
            "so happy I cried!\x02",
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
            "Ilya's room, but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10AC")

    label("loc_100F")


    ChrTalk(
        0xFE,
        (
            "Aah, to think Lady Ilya\x01",
            "visited Sully's room.\x01",
            "I'm so jealous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it's fine... I'm\x01",
            "lucky to have gotten to see\x01",
            "Lady Ilya up close like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AC")

    Jump("loc_1D51")

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1128")

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
            "I think I'll tackle 3F\x01",
            "next. It's still a\x01",
            "mess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FC")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Ryｹvic and\x01",
            "his wife went for a\x01",
            "drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they were\x01",
            "going as far as the\x01",
            "state border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the quintessential\x01",
            "leisurely elderly life.\x01",
            "I'm so jealous~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A5")

    label("loc_11FC")


    ChrTalk(
        0xFE,
        (
            "Huh, come to think of it... I\x01",
            "feel like Mr. Ryｹvic and his\x01",
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

    label("loc_12A5")

    Jump("loc_1D51")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1384")

    ChrTalk(
        0xFE,
        (
            "The next Arc-en-Ciel\x01",
            "renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sully, who lives on 3F, is one\x01",
            "of the co-stars, and it'll be\x01",
            "a huge promotion for her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyah, how amazing! I\x01",
            "really want to see it!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F1")

    label("loc_1384")


    ChrTalk(
        0xFE,
        (
            "Aah... I really want to\x01",
            "see Sully's big moment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, I missed my\x01",
            "chance to buy ticket.\x01",
            "Aaah~...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F1")

    Jump("loc_1D51")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DE")

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
            "There was a heavy\x01",
            "atmosphere when I went\x01",
            "to collect my payment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wish they'd think\x01",
            "about the needs of people\x01",
            "other than themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1563")

    label("loc_14DE")


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
            "*sigh*, I wish they'd give\x01",
            "me a break. They don't\x01",
            "consider others at all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1563")

    Jump("loc_1D51")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_16A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(
        0xFE,
        (
            "I heard each nation's VIPs\x01",
            "are going to the theatre to\x01",
            "see Arc-en-Ciel tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, they're going to\x01",
            "enjoy it from some nice\x01",
            "seats for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grrr, I'm so envious!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_169B")

    label("loc_1636")


    ChrTalk(
        0xFE,
        (
            "In the end, I failed to buy\x01",
            "the tickets for the next\x01",
            "renewal public performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*...\x02",
    )

    CloseMessageWindow()

    label("loc_169B")

    Jump("loc_1D51")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176E")

    ChrTalk(
        0xFE,
        (
            "Did you hear? There's a rumor that\x01",
            "they'll be doing a renewal performance\x01",
            "of Golden Sun, Silver Moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm looking forward\x01",
            "to it. I've got to hurry\x01",
            "and buy tickets!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_180D")

    label("loc_176E")


    ChrTalk(
        0xFE,
        (
            "It seems Arc-en-Ciel is\x01",
            "doing a renewal performance\x01",
            "of Golden Sun, Silver Moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is something I can't\x01",
            "miss... I've got to hurry\x01",
            "and buy tickets!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180D")

    Jump("loc_1D51")

    label("loc_1812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_199E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1920")

    ChrTalk(
        0xFE,
        (
            "Mr. Ryｹvic on 1F is\x01",
            "considering remodeling\x01",
            "his apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it would have cost all\x01",
            "the mira they have, and in\x01",
            "the end his wife stopped him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was surprised. He's the\x01",
            "one employing me as manager\x01",
            "in the first place... right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1999")

    label("loc_1920")


    ChrTalk(
        0xFE,
        (
            "Mr. Ryｹvic is a former\x01",
            "congressman and very\x01",
            "wealthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, he's\x01",
            "think of remodeling this\x01",
            "apartment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1999")

    Jump("loc_1D51")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(
        0xFE,
        (
            "My timing is always\x01",
            "poor, so I never see the\x01",
            "3F resident, but...\x02",
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
            "Sully and she's an Arc-\x01",
            "en-Ciel trainee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems she's still\x01",
            "unknown. I'll have check\x01",
            "up on her from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Sully is freeloading in\x01",
            "Ilya's room, if I'm\x01",
            "remembering it right.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(It seems she hasn't\x01",
            "noticed that Ilya's room\x01",
            "is on 3F.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C09")

    label("loc_1B59")


    ChrTalk(
        0xFE,
        (
            "But, Arc-en-Ciel pays\x01",
            "very well, don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because, even though she's\x01",
            "a trainee, she lives in\x01",
            "that huge apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(It's really Ilya's\x01",
            "room, though...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C09")

    Jump("loc_1D51")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF3")

    ChrTalk(
        0xFE,
        (
            "I am this apartment's\x01",
            "manager, but...\x02",
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
            "...But it's too spacious,\x01",
            "and a little difficult to\x01",
            "clean, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D51")

    label("loc_1CF3")


    ChrTalk(
        0xFE,
        (
            "Hmm, I have to clean the\x01",
            "garden later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, being a manager\x01",
            "sure is hard work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D51")

    TalkEnd(0xFE)
    Return()

    # Function_5_7DC end

    def Function_6_1D55(): pass

    label("Function_6_1D55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6D")

    ChrTalk(
        0xFE,
        (
            "It seems the President\x01",
            "constructed suspicious\x01",
            "facilities inside Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He made questionable revisions\x01",
            "to my exterior design. For\x01",
            "nefarious purposes, it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've all been deceived.\x01",
            "Good grief. I can't\x01",
            "possibly forgive him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F08")

    label("loc_1E6D")


    ChrTalk(
        0xFE,
        (
            "It seems the President\x01",
            "constructed suspicious\x01",
            "facilities inside Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've all been deceived.\x01",
            "Good grief. I can't\x01",
            "possibly forgive him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F08")

    Jump("loc_306C")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDF")

    ChrTalk(
        0xFE,
        (
            "T-That President... Who\x01",
            "would have thought he'd\x01",
            "go this far!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I'm thankful he\x01",
            "entrusted me with Orchis\x01",
            "Tower's exterior design...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can no longer be\x01",
            "trusted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2013")

    label("loc_1FDF")


    ChrTalk(
        0xFE,
        (
            "That President... He can\x01",
            "no longer be trusted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2013")

    Jump("loc_306C")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20C1")

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
            "Guh, I would have wanted\x01",
            "them to at least let me\x01",
            "finish my current work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_222D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C9")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower was\x01",
            "protected thanks to\x01",
            "Arios, but...\x02",
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
    Jump("loc_2228")

    label("loc_21C9")


    ChrTalk(
        0xFE,
        (
            "The IBC building was\x01",
            "also a symbol of\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those criminal can't be\x01",
            "forgiven!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2228")

    Jump("loc_306C")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_245A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D8")

    ChrTalk(
        0xFE,
        "......*sigh*.\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22E4")
    Jump("loc_232E")

    label("loc_22E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2304")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_232E")

    label("loc_2304")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2324")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_232E")

    label("loc_2324")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_232E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "...Need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to concentrate on\x01",
            "drawing up these plans. Sorry,\x01",
            "but please don't interrupt me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2455")

    label("loc_23D8")


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
            "Not being able to see\x01",
            "one's surroundings is a\x01",
            "drawback, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2455")

    Jump("loc_306C")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24EB")

    ChrTalk(
        0xFE,
        (
            "Why does the sound of\x01",
            "the rain make me feel\x01",
            "this good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'm making\x01",
            "good progress on these\x01",
            "plans too, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_24EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_255C")

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
            "But, those sirens... Was\x01",
            "there some kind of\x01",
            "accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_264D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25ED")

    ChrTalk(
        0xFE,
        (
            "I wonder if I'm getting any\x01",
            "closer to my grandfather, a\x01",
            "great architect...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmm. Anyway, I'm\x01",
            "working now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2648")

    label("loc_25ED")


    ChrTalk(
        0xFE,
        (
            "A request for plans should've\x01",
            "come in from the Empire... I\x01",
            "think I'll start on those.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2648")

    Jump("loc_306C")

    label("loc_264D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26CF")

    ChrTalk(
        0xFE,
        (
            "I feel relieved now that\x01",
            "the Orchis Tower unveiling\x01",
            "ceremony is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have other work to\x01",
            "deal with now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_26CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(
        0xFE,
        (
            "I handled Orchis Tower's exterior\x01",
            "design, but I don't understand its\x01",
            "connection with the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The interior design was\x01",
            "handled by another architect\x01",
            "the mayor recommended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know from experience\x01",
            "the importance of\x01",
            "working with others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2881")

    label("loc_27EB")


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
            "I know from experience\x01",
            "the importance of\x01",
            "working with others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2881")

    Jump("loc_306C")

    label("loc_2886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D2")

    ChrTalk(
        0xFE,
        (
            "In the background of the speedy\x01",
            "Orchis Tower construction, the orbal\x01",
            "network achieved several milestones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between the construction staff,\x01",
            "plans and such were exchanged\x01",
            "over the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That must be connected to the\x01",
            "efficiency of their work...\x01",
            "Technological progress sure is amazing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A84")

    label("loc_29D2")


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

    label("loc_2A84")

    Jump("loc_306C")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A97")
    Jump("loc_306C")

    label("loc_2A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B49")

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
            "*sigh*... I know it's\x01",
            "childish, but I'm\x01",
            "worried about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BE0")

    label("loc_2B49")


    ChrTalk(
        0xFE,
        (
            "Tomorrow, "Orchis Tower"\x01",
            "will finally be\x01",
            "unveiled, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the unveiling ceremony,\x01",
            "I think I'll go say hello to\x01",
            "the construction staff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE0")

    Jump("loc_306C")

    label("loc_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA6")

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
            "As an architect, my aim\x01",
            "is to be as great as my\x01",
            "grandfather was...\x02",
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
    Jump("loc_2E71")

    label("loc_2DA6")


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

    label("loc_2E71")

    Jump("loc_306C")

    label("loc_2E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_306C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE3")

    ChrTalk(
        0xFE,
        (
            "Crossbell's new City\x01",
            "Hall building is finally\x01",
            "complete.\x02",
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
            "Because of a temporary\x01",
            "budget freeze, the project\x01",
            "was in danger, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that I, who participated\x01",
            "in the external design, will be\x01",
            "able to settle down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_306C")

    label("loc_2FE3")


    ChrTalk(
        0xFE,
        (
            "I participated in the new\x01",
            "City Hall building external\x01",
            "design as an architect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be completed\x01",
            "soon... That's deeply\x01",
            "moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    TalkEnd(0xFE)
    Return()

    # Function_6_1D55 end

    def Function_7_3070(): pass

    label("Function_7_3070")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(
        0xFE,
        (
            "Despite his anger towards the\x01",
            "President, my husband started\x01",
            "work on his next project.\x02",
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
            "I want him to focus on\x01",
            "his work without\x01",
            "fixating on the Tower.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_326D")

    label("loc_31BE")


    ChrTalk(
        0xFE,
        (
            "Reconstruction requests for crime\x01",
            "prevention and security have come\x01",
            "in from all sorts of companies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to focus on\x01",
            "his work without\x01",
            "fixating on the Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326D")

    Jump("loc_3EA8")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_32E5")

    ChrTalk(
        0xFE,
        (
            "There's no sign of those\x01",
            "monsters outside in any\x01",
            "buildings, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Scary things are scary.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_32E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_336D")

    ChrTalk(
        0xFE,
        (
            "I was surprised at the\x01",
            "asset freeze IBC\x01",
            "declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I wonder if something\x01",
            "like this will really be\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_336D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345E")

    ChrTalk(
        0xFE,
        (
            "To think enemies\x01",
            "attacked the city. What\x01",
            "a terrifying incident.\x02",
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
    Jump("loc_34D7")

    label("loc_345E")


    ChrTalk(
        0xFE,
        (
            "To think enemies\x01",
            "attacked the city. What\x01",
            "a terrifying incident.\x02",
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

    label("loc_34D7")

    Jump("loc_3EA8")

    label("loc_34DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_357D")

    ChrTalk(
        0xFE,
        (
            "Various incidents have been\x01",
            "occurring for a while now\x01",
            "for some reason, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until a little while\x01",
            "ago, hardly any\x01",
            "incidents occurred...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362C")

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
            "I guess I'll just have\x01",
            "to bring my umbrella\x01",
            "with me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36C5")

    label("loc_362C")


    ChrTalk(
        0xFE,
        (
            "They have some good coffee\x01",
            "beans at the imported\x01",
            "goods general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they get wet their\x01",
            "flavor will be ruined, so\x01",
            "I wish it hadn't rained.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C5")

    Jump("loc_3EA8")

    label("loc_36CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_370F")

    ChrTalk(
        0xFE,
        (
            "Let's see, my husband's\x01",
            "favorite Liberl\x01",
            "coffee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_370F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3814")

    ChrTalk(
        0xFE,
        (
            "My husband has struggled\x01",
            "with a father complex\x01",
            "for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, because of his involvement in\x01",
            "Orchis Tower's exterior design, I think\x01",
            "he's gotten a lot more positive lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I have confidence\x01",
            "in his work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38B0")

    label("loc_3814")


    ChrTalk(
        0xFE,
        (
            "It seems my husband's\x01",
            "father complex has faded\x01",
            "a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe his confidence has improved\x01",
            "due to his involvement in Orchis\x01",
            "Tower's exterior design.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B0")

    Jump("loc_3EA8")

    label("loc_38B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3958")

    ChrTalk(
        0xFE,
        (
            "To help my husband with\x01",
            "his work, I'll make some\x01",
            "coffee for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I'm using Liberl\x01",
            "beans today, I'm sure it\x01",
            "will have a nice aroma.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39F1")

    ChrTalk(
        0xFE,
        (
            "Actually, some new work\x01",
            "came in this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because my husbands\x01",
            "work on the tower has ended,\x01",
            "it doesn't mean he can rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_39F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3AB0")

    ChrTalk(
        0xFE,
        (
            "That husband of mine, I didn't\x01",
            "even ask and he's teaching me\x01",
            "many things about Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems his excitement\x01",
            "from the unveiling at noon\x01",
            "hasn't worn off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B6B")

    ChrTalk(
        0xFE,
        (
            "My husband, who was involved in\x01",
            "the design of Orchis Tower,\x01",
            "attended its unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He should be basking in\x01",
            "the celebration of its\x01",
            "completion around now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BEA")

    ChrTalk(
        0xFE,
        (
            "It was a really big job\x01",
            "this time, and my\x01",
            "husband seems nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe some coffee will\x01",
            "calm him down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBB")

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
            "It seems he was an excellent\x01",
            "architect, and my husband\x01",
            "uses him as a benchmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he might have a\x01",
            "bit of a complex.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D5D")

    label("loc_3CBB")


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
            "My husband is doing his\x01",
            "best, and that's good\x01",
            "enough for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5D")

    Jump("loc_3EA8")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3C")

    ChrTalk(
        0xFE,
        (
            "My husband had formal\x01",
            "involvement with the new\x01",
            "City Hall building's design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a big job and\x01",
            "kept him busy for a\x01",
            "whole month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he seems relieved\x01",
            "now that it's complete.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EA8")

    label("loc_3E3C")


    ChrTalk(
        0xFE,
        (
            "Our home serves as a\x01",
            "design office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, we're been busy\x01",
            "designing the new City\x01",
            "Hall building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA8")

    TalkEnd(0xFE)
    Return()

    # Function_7_3070 end

    def Function_8_3EAC(): pass

    label("Function_8_3EAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3F3B")

    ChrTalk(
        0xFE,
        (
            "As I thought, the world\x01",
            "is getting more\x01",
            "dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to hide in an\x01",
            "underground shelter\x01",
            "somewhere with my wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_482D")

    label("loc_3F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3FA6")

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
    Jump("loc_482D")

    label("loc_3FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FB4")
    Jump("loc_482D")

    label("loc_3FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF0")
    Call(0, 19)
    Return()

    label("loc_3FF0")


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
            "I'm sure you'll find him if you\x01",
            "look around a bit. You can ask\x01",
            "the man himself for the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_4090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4186")

    ChrTalk(
        0xFE,
        (
            "I'm going to the charity event\x01",
            "hall to donate the mira I got\x01",
            "from selling my old furniture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be put to better\x01",
            "use than if I were to\x01",
            "spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone has it hard\x01",
            "right now. We need to\x01",
            "help each other out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41CB")

    label("loc_4186")


    ChrTalk(
        0xFE,
        (
            "Everyone has it hard\x01",
            "right now. We need to\x01",
            "help each other out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CB")

    Jump("loc_482D")

    label("loc_41D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_430D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4297")

    ChrTalk(
        0xFE,
        (
            "An armed group occupying\x01",
            "the town? That's unheard\x01",
            "of!\x02",
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
            "*shiver*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4308")

    label("loc_4297")


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
            "*shiver*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4308")

    Jump("loc_482D")

    label("loc_430D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4328")
    Call(0, 13)
    Jump("loc_4371")

    label("loc_4328")


    ChrTalk(
        0xFE,
        (
            "(Hmm... How that Alm has\x01",
            "grown...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Even so, that idiot\x01",
            "is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4371")

    Jump("loc_482D")

    label("loc_4376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4384")
    Jump("loc_482D")

    label("loc_4384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4392")
    Jump("loc_482D")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_441F")

    ChrTalk(
        0xFE,
        (
            "I tried inviting my wife\x01",
            "on a drive I had planned\x01",
            "for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope I'll be able to\x01",
            "cheer her up a little,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_482D")

    label("loc_441F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_456B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F3")

    ChrTalk(
        0xFE,
        (
            "I've been fighting with\x01",
            "my wife since\x01",
            "yesterday...\x02",
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
            "Hmm. I'll have to make\x01",
            "up with my wife\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4566")

    label("loc_44F3")


    ChrTalk(
        0xFE,
        (
            "Just how can I make up\x01",
            "with my wife, I\x01",
            "wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps some expensive\x01",
            "wine... No, no, that\x01",
            "won't work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4566")

    Jump("loc_482D")

    label("loc_456B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4586")
    Call(0, 9)
    Jump("loc_460C")

    label("loc_4586")


    ChrTalk(
        0xFE,
        (
            "I thought we would've drunk\x01",
            "it together and so I went\x01",
            "to buy a good wine, but...\x02",
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

    label("loc_460C")

    Jump("loc_482D")

    label("loc_4611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_461F")
    Jump("loc_482D")

    label("loc_461F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_46EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B3")

    ChrTalk(
        0xFE,
        (
            "I wanted a garage to\x01",
            "protect my car from the\x01",
            "rain, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She got so mad at me\x01",
            "that I had to abandon\x01",
            "the idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46E9")

    label("loc_46B3")


    ChrTalk(
        0xFE,
        (
            "*sigh*, but I wish she\x01",
            "hadn't gotten so\x01",
            "angry...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E9")

    Jump("loc_482D")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4792")

    ChrTalk(
        0xFE,
        (
            "Hmm. My car outside will\x01",
            "get wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have wanted a\x01",
            "garage, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose it's fine.\x01",
            "I'll have it washed\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_481F")

    label("loc_4792")


    ChrTalk(
        0xFE,
        (
            "But at this rate, the\x01",
            "weather will wear out my\x01",
            "orbal car.\x02",
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

    label("loc_481F")

    Jump("loc_482D")

    label("loc_4824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_482D")

    label("loc_482D")

    TalkEnd(0xFE)
    Return()

    # Function_8_3EAC end

    def Function_9_4831(): pass

    label("Function_9_4831")

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
            "It seems you don't want\x01",
            "any, old lady, so I'll\x01",
            "drink it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Fine, do as you like.\x02",
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
        "...Hmph! *gluglugluglug*\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_9_4831 end

    def Function_10_4947(): pass

    label("Function_10_4947")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_49FE")

    ChrTalk(
        0xFE,
        (
            "That husband of mine. It's\x01",
            "not like we have the mira to\x01",
            "buy an underground shelter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deciding to buy all manner\x01",
            "of high-priced things is a\x01",
            "bad habit of his.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_49FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A78")

    ChrTalk(
        0xFE,
        (
            "Good grief. Of all things, for that\x01",
            "husband of mine to be worried about\x01",
            "his car at a time like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B4D")

    ChrTalk(
        0xFE,
        (
            "I heard the address, but... It seems\x01",
            "the Empire and Republic have been\x01",
            "fighting in secret over Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To those of use who live here,\x01",
            "it's something that absolutely\x01",
            "can't be forgiven...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4BE6")

    ChrTalk(
        0xFE,
        (
            "My husband gave a\x01",
            "donation for city\x01",
            "reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought he only spent\x01",
            "mira on himself. It seems\x01",
            "I'll need to rethink that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4C4A")

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
            "I hope the CGF resolves\x01",
            "it soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4CAA")

    ChrTalk(
        0xFE,
        (
            "Alm brought his family\x01",
            "to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Anyway, I'm glad\x01",
            "he's happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CB8")
    Jump("loc_5411")

    label("loc_4CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CC6")
    Jump("loc_5411")

    label("loc_4CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D7D")

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
            "will lighten my mood?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5411")

    label("loc_4D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4DF6")

    ChrTalk(
        0xFE,
        (
            "I've decided not to\x01",
            "speak to my husband for\x01",
            "a while.\x02",
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
    Jump("loc_5411")

    label("loc_4DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E11")
    Call(0, 9)
    Jump("loc_4E3B")

    label("loc_4E11")


    ChrTalk(
        0xFE,
        (
            "...Hmph, who cares about\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3B")

    Jump("loc_5411")

    label("loc_4E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F16")

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
            "garage incident the other day... Good\x01",
            "grief. He's totally unrepentant.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F5F")

    label("loc_4F16")


    ChrTalk(
        0xFE,
        (
            "That husband of mine...\x01",
            "As if I'd approve of his\x01",
            "wasteful spending.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5F")

    Jump("loc_5411")

    label("loc_4F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_510D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5074")

    ChrTalk(
        0xFE,
        (
            "That husband of mine...\x01",
            "He tried to add a garage\x01",
            "to our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to talk him out of it\x01",
            "somehow, but Sammy, who he\x01",
            "consulted with, was dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. As if I'd be\x01",
            "surprised by this level\x01",
            "of wasteful spending.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5108")

    label("loc_5074")


    ChrTalk(
        0xFE,
        (
            "That husband of mine...\x01",
            "He tried to add a garage\x01",
            "to our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. As if I'd be\x01",
            "surprised by this level\x01",
            "of wasteful spending.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5108")

    Jump("loc_5411")

    label("loc_510D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51DC")

    ChrTalk(
        0xFE,
        (
            "On rainy days like this,\x01",
            "I focus on my hobbies.\x02",
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
            "*stiching*... This is\x01",
            "rather complex and fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5282")

    label("loc_51DC")


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

    label("loc_5282")

    Jump("loc_5411")

    label("loc_5287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538F")

    ChrTalk(
        0xFE,
        (
            "My husband's wasteful\x01",
            "spending is troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a long time, he's done\x01",
            "things like replace furniture\x01",
            "we didn't need to, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just the other day, he went\x01",
            "and bought an orbal car. Goodness\x01",
            "gracious, I can't even...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5411")

    label("loc_538F")


    ChrTalk(
        0xFE,
        (
            "Without discussing\x01",
            "anything with me, he went\x01",
            "and bought an orbal car...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That man's wasteful\x01",
            "spending is a real\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5411")

    TalkEnd(0xFE)
    Return()

    # Function_10_4947 end

    def Function_11_5415(): pass

    label("Function_11_5415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542A")
    Call(0, 13)
    Jump("loc_5460")

    label("loc_542A")


    ChrTalk(
        0xFE,
        (
            "Alright, today I'll go\x01",
            "to the hospital, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5460")

    TalkEnd(0xFE)
    Return()

    # Function_11_5415 end

    def Function_12_5464(): pass

    label("Function_12_5464")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5479")
    Call(0, 13)
    Jump("loc_54B7")

    label("loc_5479")


    ChrTalk(
        0xFE,
        (
            "Haha, it's been slow,\x01",
            "but you're getting more\x01",
            "reliable㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B7")

    TalkEnd(0xFE)
    Return()

    # Function_12_5464 end

    def Function_13_54BB(): pass

    label("Function_13_54BB")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "I see, then he was\x01",
            "discharged a few months\x01",
            "ago from St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes. I don't know what\x01",
            "happened after that,\x01",
            "but...\x02",
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
            "No, don't worry about\x01",
            "it. You've done enough.\x02",
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
            "Yes, Aerie. It's a\x01",
            "spectacular victory for\x01",
            "the three of us!\x02",
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
            "Haha. You all are really\x01",
            "very close.\x02",
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

    # Function_13_54BB end

    def Function_14_56C4(): pass

    label("Function_14_56C4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I-I couldn't even\x01",
            "imagine something like\x01",
            "this happening.\x02",
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

    # Function_14_56C4 end

    def Function_15_5754(): pass

    label("Function_15_5754")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5769")
    Call(0, 17)
    Jump("loc_58CD")

    label("loc_5769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_588C")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "#04206F*ha, ha, haah*...\x02\x03",
            "#04201FSay, Ilya. Is this good\x01",
            "enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FHmm~, you're still a\x01",
            "little tense. I think I'll\x01",
            "loosen you up a bit more.\x02\x03",
            "#01702FYou're fine, just shut up\x01",
            "and give in to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04206FOoh... How long is this\x01",
            "going to go on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    Jump("loc_58CD")

    label("loc_588C")


    ChrTalk(
        0xE,
        (
            "#04206FOoh... I'll do whatever\x01",
            "you want, just make it\x01",
            "stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58CD")

    TalkEnd(0xFE)
    Return()

    # Function_15_5754 end

    def Function_16_58D1(): pass

    label("Function_16_58D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E6")
    Call(0, 17)
    Jump("loc_5A88")

    label("loc_58E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D0")

    ChrTalk(
        0xD,
        (
            "#01700FHaha. Would you all like\x01",
            "a massage?\x02\x03",
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
            "#04206F(*sigh*, if she's like\x01",
            "this when sober, I give\x01",
            "up...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A88")

    label("loc_59D0")


    ChrTalk(
        0xD,
        (
            "#01700FI've got to loosen up\x01",
            "Sully for tonight's\x01",
            "performance.\x02\x03",
            "#01709FWe've got to make sure we\x01",
            "have no regrets... I'll\x01",
            "massage the ladies, ok㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04206F(I-I don't get it...)\x02",
    )

    CloseMessageWindow()

    label("loc_5A88")

    TalkEnd(0xFE)
    Return()

    # Function_16_58D1 end

    def Function_17_5A8C(): pass

    label("Function_17_5A8C")

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
        (
            "#11P#01709FOh, hey there little\x01",
            "bro☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04205F#5PH-Hey...\x02\x03",
            "#04206F...Whaaaaat!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01704FHaha, those heads of\x01",
            "state are coming to our\x01",
            "theater tonight, but...\x02\x03",
            "#01702FSully is helping us out\x01",
            "in a minor role.\x02\x03",
            "#01709FWe've got to limber you\x01",
            "up. It's massage time!\x01",
            "Here we go!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(50)
    SetChrSubChip(0xE, 0x0)

    def lambda_5C9A():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5C9A)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#04212F#11P#4SAaaaaah!!\x02",
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
            "#6P#10105FU-Umm, are you all\x01",
            "right?\x02\x03",
            "#10106FI've heard it has the\x01",
            "opposite effect if done\x01",
            "by amateurs, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#11P#01704FHaha, no need to worry.\x02\x03",
            "#01702FI had a pro masseuse\x01",
            "instruct me, so I'm a\x01",
            "total master now, I guess.\x02\x03",
            "I do this to Rixia during\x01",
            "our stretches in practice\x01",
            "too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FI see. So you'll turn to\x01",
            "any field if it's to\x01",
            "help your dancing, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FAh, that's our Ilya for\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "#04206F#5PNononono... Painful\x01",
            "things are painful!!\x02\x03",
            "#04201FI-Ilya, are you really,\x01",
            "really sure this is all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01706FI already told you, it's\x01",
            "fine.\x02\x03",
            "#01700FYou're in pain because you're\x01",
            "nervous about tonight's dance\x01",
            "and your body's gotten stiff.\x02\x03",
            "#01709FDon't worry. If I keep it up,\x01",
            "you'll get used to it\x01",
            "eventually㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04207F#5PH-How suspicious can you\x01",
            "get!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01701FQuiet, you. To shut you\x01",
            "up... How about this!\x02",
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
        (
            "#5P#04207FWh-Wh-Wh-Where are you\x01",
            "touching!?!?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xE)
    SetChrSubChip(0xE, 0x1)

    ChrTalk(
        0xD,
        (
            "#11P#01709FMuhuhu, don't worry.\x01",
            "This massage is\x01",
            "particularly effective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04207F#5PS-Stop lying!!\x02\x03",
            "#04209FAhaha, that tickles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01709FHmmhmm, that's the way㈱\x01",
            "You've got a bright\x01",
            "future ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04212F#5PH-How can you know\x01",
            "that!?\x02",
        )
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
            "#6P#00113FAs you might expect, I'm\x01",
            "a little worried about\x01",
            "this scene, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHaha, I'm sure all of\x01",
            "this has its own\x01",
            "meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha. Somehow, it seems\x01",
            "that Sully is getting\x01",
            "used to Arc-en-Ciel.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5P#04207FD-Don't summarize! Help\x01",
            "me out here!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01709FNow, now. I'm not\x01",
            "letting you go~.\x02",
        )
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

    # Function_17_5A8C end

    def Function_18_6501(): pass

    label("Function_18_6501")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya and Sully's voices\x01",
            "can be heard from beyond\x01",
            "the door.\x07\x00\x02",
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
            "Aha, ahahaha... I told\x01",
            "you, not there!\x02\x03",
            "*pant, pant*... Ilya, have\x01",
            "you been doing that on\x01",
            "purpose this whole time?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Ilya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, no, it's just your\x01",
            "imagination㈱\x02",
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
        (
            "#00012FYou look like you're\x01",
            "enjoying yourself, Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FPoor Sully.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetScenarioFlags(0x0, 7)
    Jump("loc_6854")

    label("loc_66F5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya and Sully's voices\x01",
            "can be heard from beyond\x01",
            "the door.\x07\x00\x02",
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
            "*pant, pant, pant*...\x01",
            "How long is this going\x01",
            "to go on?\x02",
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
            "sooner if you just went\x01",
            "along with it㈱\x02",
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

    label("loc_6854")

    Jump("loc_687F")

    label("loc_6859")

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

    label("loc_687F")

    TalkEnd(0xFF)
    Return()

    # Function_18_6501 end

    def Function_19_6883(): pass

    label("Function_19_6883")

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
            "#00004FPardon the sudden visit,\x01",
            "but...\x02\x03",
            "#00000FDo you know the name\x01",
            ""Geval"?\x02",
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
            "#2PI did indeed look after\x01",
            "him when he was a\x01",
            "congressman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha, bingo.\x02",
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
            "Lloyd explained that they were\x01",
            "looking for Geval to reunite\x01",
            "him with his son and his wife.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#2PHmm, I see. So you\x01",
            "received a request from\x01",
            "them, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PActually, Geval came to me the\x01",
            "other day asking me the best\x01",
            "way to "hide from Crossbell".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PMy goodness. That idiot... His\x01",
            "son and wife make such a nice\x01",
            "couple. What is he running from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FIt seems you know where\x01",
            "Geval went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FBut why is he hiding?\x02\x03",
            "#00303FI don't really get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI know! Even though Alm\x01",
            "and Aerie said they want\x01",
            "to see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PHmm, this probably seems\x01",
            "trivial to an outsider,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2P...No, I won't say it.\x02",
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
            "#2P...He should be staying\x01",
            "in Armorica Village\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PI'm sure you'll find him if you\x01",
            "look around a bit. You can ask\x01",
            "the man himself for the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUnderstood... And thank\x01",
            "you.\x02\x03",
            "#00000FLet's head for Armorica\x01",
            "immediately.\x02",
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

    # Function_19_6883 end

    SaveToFile()

Try(main)
