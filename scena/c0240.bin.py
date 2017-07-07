from ScenarioHelper import *

def main():
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
        "Sammy",                 # 1
        "Kindoor",             # 2
        "Brigitta",             # 3
        "Louvic's old man",       # 4
        "Mrs Olga",             # 5
        "Ilia",                 # 6
        "Shuri",                 # 7
        "Almu",                 # 8
        "Airy",               # 9
        "Ponce",                 # 10
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
        "Function_6_1C12",         # 06, 6
        "Function_7_2D43",         # 07, 7
        "Function_8_39FF",         # 08, 8
        "Function_9_4383",         # 09, 9
        "Function_10_44A1",        # 0A, 10
        "Function_11_4E4C",        # 0B, 11
        "Function_12_4E9A",        # 0C, 12
        "Function_13_4EE8",        # 0D, 13
        "Function_14_50E2",        # 0E, 14
        "Function_15_5168",        # 0F, 15
        "Function_16_52D9",        # 10, 16
        "Function_17_54BD",        # 11, 17
        "Function_18_5F63",        # 12, 18
        "Function_19_62CE",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E7")

    ChrTalk(
        0xFE,
        (
            "Such things appeared in the wetland … …\x01",
            "I am worried, but my job is properly\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shuriちゃんだって、\x01",
            "Always in the alkane shell\x01",
            "It looks like I'm doing my best for practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilia様が戻ってきた時のためにも\x01",
            "I must clean the apartment firmly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_980")

    label("loc_8E7")


    ChrTalk(
        0xFE,
        (
            "Shuriちゃんだって、\x01",
            "Always in the alkane shell\x01",
            "It looks like I'm doing my best for practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilia様が戻ってきた時のためにも\x01",
            "I have to clean up the apartment firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_980")

    Jump("loc_1C0E")

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(
        0xFE,
        (
            "Oh, what shall I do ……\x01",
            "It is such a thing happens in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, to everyone in the room\x01",
            "I have to call out not to go outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A7F")

    ChrTalk(
        0xFE,
        (
            "That raid incident ……\x01",
            "The black curtain seems to be an empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will not forgive you.\x01",
            "あの事件でIlia様は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B68")

    ChrTalk(
        0xFE,
        (
            "This apartment's\x01",
            "I lived on the third floor,\x01",
            "Ilia様だったのね……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've come to pick up my luggage.\x01",
            "Shuriちゃんを見て、\x01",
            "Finally I realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… If it is true I'm happy,\x01",
            "Ilia様があんなことに\x01",
            "I guess … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE3")

    label("loc_B68")


    ChrTalk(
        0xFE,
        (
            "Shuriちゃん、\x01",
            "I have a face without animation forever.\x01",
            "Poor thing……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, how are you?\x01",
            "I hope you will regain it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE3")

    Jump("loc_1C0E")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(
        0xFE,
        (
            "\"Gold Sun, the Moon of Silver\"\x01",
            "Renewal performance ……\x01",
            "It's time tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately the tickets\x01",
            "I could not buy it … ….\x01",
            "I'll support you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "はあ、Shuriちゃんの勇姿、\x01",
            "I wish I could see … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D3B")

    label("loc_CC2")


    ChrTalk(
        0xFE,
        (
            "\"Gold Sun, the Moon of Silver\"\x01",
            "Renewal performance ……\x01",
            "It's time tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "はあ、Shuriちゃんの勇姿、\x01",
            "I wish I could see … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3B")

    Jump("loc_1C0E")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_104F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E18")

    ChrTalk(
        0xFE,
        (
            "今朝早くShuriちゃんが\x01",
            "He went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently what?\x01",
            "It seems like I feel good.\x01",
            "I am a bit worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all renewal performance\x01",
            "I wonder if it's pressure …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E8D")

    label("loc_E18")


    ChrTalk(
        0xFE,
        (
            "Shuriちゃん、\x01",
            "After all renewal performance\x01",
            "I wonder if it's pressure …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I firmly\x01",
            "I have to support you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8D")

    Jump("loc_104A")

    label("loc_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(
        0xFE,
        (
            "Saki, now ……\x01",
            "３階のShuriちゃんの部屋から\x01",
            "Ilia様が出て行ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I was greeted … …\x01",
            "I am too happy to cry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilia様、Shuriちゃんの部屋に\x01",
            "I wonder if she came to see me.\x01",
            "Happy envy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F（いや、本当はIliaさんの\x01",
            "I am in a room ….)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104A")

    label("loc_FBF")


    ChrTalk(
        0xFE,
        (
            "はあ、Ilia様が遊びにくるなんて、\x01",
            "Shuriちゃんうらやましい……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well somewhere ……\x01",
            "Ilia様を間近で見られて\x01",
            "It was awesome lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_1C0E")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10C7")

    ChrTalk(
        0xFE,
        (
            "Mr. Louvic and this is\x01",
            "When cleaning is over ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I wonder if the next floor is the third floor.\x01",
            "It will be messy again …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_10C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118C")

    ChrTalk(
        0xFE,
        (
            "Lou Vic,\x01",
            "Drive with your wife\x01",
            "It looks like I'm going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until border gate\x01",
            "I told you to run a car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is precocious old age right.\x01",
            "I'm jealous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121A")

    label("loc_118C")


    ChrTalk(
        0xFE,
        (
            "Well, that's … …\x01",
            "Mr. Lou Vic and his wife\x01",
            "I thought that the couple was fighting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well someday.\x01",
            "Anyway, I was annoyed\x01",
            "I have to clean it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_1C0E")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_136D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(
        0xFE,
        (
            "This time the alkane shell\x01",
            "Renewal performance ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "３階に住んでるShuriちゃんが\x01",
            "It was selected as one of the semi-protagonists\x01",
            "It looks like!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "CAR, it is amazing!\x01",
            "I really want to see it! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1368")

    label("loc_12EC")


    ChrTalk(
        0xFE,
        (
            "Ahh ……\x01",
            "Shuriちゃんの晴れ舞台、\x01",
            "I want to see it … ___ ___ 0\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But … the tickets are\x01",
            "I missed buying it.\x01",
            "Oh no ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1368")

    Jump("loc_1C0E")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0xFE,
        (
            "Lou Vic's house,\x01",
            "It looks like a couple fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you go to collection\x01",
            "The air is heavy and heavy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, not even a party\x01",
            "I strangely used my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148F")

    label("loc_141D")


    ChrTalk(
        0xFE,
        (
            "Lou Vic and Mr. Olga,\x01",
            "It looks like a couple fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I want you to forgive me.\x01",
            "I will use my mind ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148F")

    Jump("loc_1C0E")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_15A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1544")

    ChrTalk(
        0xFE,
        (
            "Today the leaders of each country\x01",
            "I am watching the alkane shell\x01",
            "It seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, sir, in a good seat\x01",
            "I guess you are enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kuu ~, I'm so jealous!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_159B")

    label("loc_1544")


    ChrTalk(
        0xFE,
        (
            "After all, this time the renewal performance\x01",
            "I missed buying tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa …\x02",
    )

    CloseMessageWindow()

    label("loc_159B")

    Jump("loc_1C0E")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164C")

    ChrTalk(
        0xFE,
        (
            "Hey, did you hear that? Well,\x01",
            "That \"gold sun, silver moon\"\x01",
            "It seems to be renewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm looking forward to it.\x01",
            "I have to go get some tickets!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D7")

    label("loc_164C")


    ChrTalk(
        0xFE,
        (
            "Of alkane shell\x01",
            "\"Gold Sun, Month of Silver\"\x01",
            "It seems to be renewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not miss this absolutely …\x01",
            "I have to go get some tickets!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D7")

    Jump("loc_1C0E")

    label("loc_16DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    ChrTalk(
        0xFE,
        (
            "Mr. Lou Vic on the first floor,\x01",
            "Renovation of condominiums\x01",
            "It was handed out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I have Mira all\x01",
            "I was told,\x01",
            "In the end my wife came to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, I was surprised.\x01",
            "Originally hired and managed\x01",
            "Even if I told you … hey?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1862")

    label("loc_17D7")


    ChrTalk(
        0xFE,
        (
            "Lou Vic says,\x01",
            "He is a former legislator and he is very wealthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "Would you like to reconstruct an apartment?\x01",
            "I do not think I can easily think of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1862")

    Jump("loc_1C0E")

    label("loc_1867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(
        0xFE,
        (
            "With the person on the third floor,\x01",
            "The timing is always bad\x01",
            "I could not see you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Morning cold this morning\x01",
            "Finally I could say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shuriっていう女の子で、\x01",
            "What an apprentice of alkane shell\x01",
            "You are doing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe he seems to be notorious yet,\x01",
            "I have to check it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F（確かShuriって、\x01",
            "  Iliaさんの部屋の\x01",
            "I'm terrible … ….? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F（３階がIliaさんの\x01",
            "To my room,\x01",
            "You do not seem to notice it. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE6")

    label("loc_1A30")


    ChrTalk(
        0xFE,
        (
            "But what is alkane shell?\x01",
            "After all I have a good salary ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even a child of an apprentice, so big\x01",
            "Because I can live in an apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F（本当はIliaさんの\x01",
            "Because it is a room ……)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE6")

    Jump("loc_1C0E")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBB")

    ChrTalk(
        0xFE,
        (
            "I am in this apartment\x01",
            "Employed managers\x01",
            "I'm doing it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is true,\x01",
            "It is wide and beautiful.\x01",
            "I also want to live in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Too wide,\x01",
            "Cleaning a little is difficult though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C0E")

    label("loc_1BBB")


    ChrTalk(
        0xFE,
        (
            "Well, the rest of the courtyard\x01",
            "I have to clean it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The hired, the manager is also serious.\x02",
    )

    CloseMessageWindow()

    label("loc_1C0E")

    TalkEnd(0xFE)
    Return()

    # Function_5_7DC end

    def Function_6_1C12(): pass

    label("Function_6_1C12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1E")

    ChrTalk(
        0xFE,
        (
            "The president inside the Orchis Tower\x01",
            "It seems she was constructing a dubious facility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I worked on the exterior design\x01",
            "Add dubious hands to Orkis Tower,\x01",
            "I was abusing it … etc ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were all deceived.\x01",
            "Whew you can not forgive us at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DAE")

    label("loc_1D1E")


    ChrTalk(
        0xFE,
        (
            "The president inside the Orchis Tower\x01",
            "It seems she was constructing a dubious facility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were all deceived.\x01",
            "Whew you can not forgive us at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAE")

    Jump("loc_2D3F")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(
        0xFE,
        (
            "However, Presidential …\x01",
            "No way to do things so far!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Exterior design of the Orchis Tower\x01",
            "To what I leave you\x01",
            "Though I was thankful … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can no longer trust you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EAE")

    label("loc_1E7D")


    ChrTalk(
        0xFE,
        (
            "President … …\x01",
            "Can no longer trust you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAE")

    Jump("loc_2D3F")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F50")

    ChrTalk(
        0xFE,
        (
            "In this way,\x01",
            "Work in the Empire and the Republic\x01",
            "Can not receive … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cut, at least the work I'm working on at the moment is\x01",
            "I wanted to finish … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_1F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower\x01",
            "Thanks to Arios\x01",
            "I heard that it was protected ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC building was disappointing.\x01",
            "That is also crossbell\x01",
            "Even though it should be called a symbol …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Raiders are crossbells\x01",
            "It is equal to insulting history itself.\x01",
            "They are utterly unforgivable … …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20B4")

    label("loc_2057")


    ChrTalk(
        0xFE,
        (
            "IBC Building Cross Bell\x01",
            "It was a symbolic building … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Raid crime, totally unforgivable … …!\x02",
    )

    CloseMessageWindow()

    label("loc_20B4")

    Jump("loc_2D3F")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226D")

    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "………………………… Ha ha.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2196")
    Jump("loc_21E0")

    label("loc_2196")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E0")

    label("loc_21B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E0")

    label("loc_21D6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21E0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "…… For something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am concentrating on drawing drawings,\x01",
            "Is it bad but will not disturb you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C5")

    label("loc_226D")


    ChrTalk(
        0xFE,
        (
            "Recently, good for work\x01",
            "You can concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not see much around you\x01",
            "It is a disadvantage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C5")

    Jump("loc_2D3F")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2345")

    ChrTalk(
        0xFE,
        (
            "Rain sound means,\x01",
            "How come\x01",
            "I guess it's comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow drawing drawings\x01",
            "I feel like I'm back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_2345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23B5")

    ChrTalk(
        0xFE,
        (
            "Muu\x01",
            "The street is bustling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that siren … …\x01",
            "Was there also an accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243B")

    ChrTalk(
        0xFE,
        (
            "I am a great architect grandfather\x01",
            "I wonder if it is a little closer … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Well, now it's work anyway.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_248B")

    label("loc_243B")


    ChrTalk(
        0xFE,
        (
            "Certainly, from the empire\x01",
            "The drawing request should have come …\x01",
            "Do you want to get there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248B")

    Jump("loc_2D3F")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_251E")

    ChrTalk(
        0xFE,
        (
            "The Orchest Tower's announcement\x01",
            "The load of the shoulder went down after it was over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "I'd like to do a variety of jobs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2619")

    ChrTalk(
        0xFE,
        (
            "I am the Orkis Tower\x01",
            "Although I was designing the appearance design,\x01",
            "I do not really understand the relationship of the power net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The internal drawing is recommended by the mayor\x01",
            "I left it to other architects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, the importance of cooperating with others\x01",
            "I felt like I was taught to be taught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26A4")

    label("loc_2619")


    ChrTalk(
        0xFE,
        (
            "The drawing inside the tower is\x01",
            "Mayor recommends\x01",
            "I left it to other architects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The importance of cooperating with others\x01",
            "I felt like I was taught to be taught.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A4")

    Jump("loc_2D3F")

    label("loc_26A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_287B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D0")

    ChrTalk(
        0xFE,
        (
            "A building as large as the Orkis Tower\x01",
            "To the background which was completed at the speed so far,\x01",
            "It was the achievement of the power net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among construction-related persons,\x01",
            "Information exchange such as drawings\x01",
            "It was done with a power net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To make it more efficient\x01",
            "Because it is connected … ….\x01",
            "Advancement of technology is a wonderful thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2876")

    label("loc_27D0")


    ChrTalk(
        0xFE,
        (
            "In the construction of the Orchis Tower\x01",
            "With the power net\x01",
            "Information exchange was taking place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until mayor develops law\x01",
            "The reason for trying to spread\x01",
            "Somehow I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2876")

    Jump("loc_2D3F")

    label("loc_287B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2889")
    Jump("loc_2D3F")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292E")

    ChrTalk(
        0xFE,
        (
            "Finally tomorrow,\x01",
            "I have designed the appearance\x01",
            "\"Orkis Tower\" will be announced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu …\x01",
            "It is somewhat unprepared\x01",
            "I was nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A1")

    label("loc_292E")


    ChrTalk(
        0xFE,
        (
            "Finally \"Orchis Tower\"\x01",
            "Are you announcing tomorrow …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the unveiling ceremony,\x01",
            "Greeting to architects\x01",
            "Let's go around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A1")

    Jump("loc_2D3F")

    label("loc_29A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    ChrTalk(
        0xFE,
        (
            "City Hall ……\x01",
            "No, was it a citizen hall now?\x01",
            "That building was designed by my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandfather is a great architect.\x01",
            "Crossbell's old public facilities, etc.,\x01",
            "Almost my grandfather worked on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking at the back of such grandfather,\x01",
            "I also aimed for an architect … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, as my grandson I\x01",
            "Designed the appearance of the new city hall … …\x01",
            "No, life is funny.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BAC")

    label("loc_2B04")


    ChrTalk(
        0xFE,
        (
            "My grandfather was a great architect.\x01",
            "The current city hall,\x01",
            "My grandfather worked on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, as my grandson I\x01",
            "Designed the appearance of the new city hall … …\x01",
            "No, life is funny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAC")

    Jump("loc_2D3F")

    label("loc_2BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCB")

    ChrTalk(
        0xFE,
        (
            "Cross Bell City's new city hall building\x01",
            "Finally completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new Mayor plans construction plan\x01",
            "Thanks to you,\x01",
            "It finally reached that point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At one point, as the budget is frozen\x01",
            "Although completion was risked … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also worked on designing the exterior\x01",
            "It seems that I can settle down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D3F")

    label("loc_2CCB")


    ChrTalk(
        0xFE,
        (
            "I am the architect of the new city hall\x01",
            "He was involved in the design of the appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be completed soon …\x01",
            "There is a deep emotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1C12 end

    def Function_7_2D43(): pass

    label("Function_7_2D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E51")

    ChrTalk(
        0xFE,
        (
            "While my husband was angry with the president,\x01",
            "It seems that he began to undertake the next job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because there was such a thing in town,\x01",
            "Request for renovation in crime prevention and security\x01",
            "I was flooded with various companies ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case I will not drag the tower,\x01",
            "I just want you to do your job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EE1")

    label("loc_2E51")


    ChrTalk(
        0xFE,
        (
            "Request for renovation in crime prevention and security\x01",
            "I was flooded with various companies ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case I will not drag the tower,\x01",
            "I just want you to do your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE1")

    Jump("loc_39FB")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F5D")

    ChrTalk(
        0xFE,
        (
            "Outside of the building is in the building\x01",
            "There is no sign of coming in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am afraid of scary things …\x02",
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_2F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FDC")

    ChrTalk(
        0xFE,
        (
            "IBC funds\x01",
            "To the declaration to freeze,\x01",
            "I was surprised by fluff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for doing this\x01",
            "Is it OK?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A5")

    ChrTalk(
        0xFE,
        (
            "To the city being attacked by a pirate,\x01",
            "It was a terrible incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is also a great deal of damage around here\x01",
            "I did not have it,\x01",
            "I am worried about it from now on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is not to happen again\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_310D")

    label("loc_30A5")


    ChrTalk(
        0xFE,
        (
            "To the city being attacked by a pirate,\x01",
            "It was a terrible incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is not to happen again\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310D")

    Jump("loc_39FB")

    label("loc_3112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_319C")

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "There are various incidents occurring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before a little while ago\x01",
            "Even though it has hardly happened ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3228")

    ChrTalk(
        0xFE,
        (
            "I do not want it …\x01",
            "Today I go shopping in department stores\x01",
            "I thought I was going to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is inevitable,\x01",
            "I have to put an umbrella ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_329E")

    label("loc_3228")


    ChrTalk(
        0xFE,
        (
            "To the imported grocery store\x01",
            "There are good coffee beans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it will impair the flavor when moistened,\x01",
            "I will be in trouble if it is rainy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329E")

    Jump("loc_39FB")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32E8")

    ChrTalk(
        0xFE,
        (
            "Well, my favorite\x01",
            "Libert coffee …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_32E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_346D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D8")

    ChrTalk(
        0xFE,
        (
            "From the past,\x01",
            "To the complex to the grandson\x01",
            "I was breathing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, in the Orkis Tower\x01",
            "By being involved in the appearance design\x01",
            "I think that it has become considerably positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was confident even by myself\x01",
            "I guess it was a job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3468")

    label("loc_33D8")


    ChrTalk(
        0xFE,
        (
            "My husband to the grandfather\x01",
            "Complex\x01",
            "It seems I got faded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having made the appearance design of the tower\x01",
            "Make your master confident\x01",
            "You guessed it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3468")

    Jump("loc_39FB")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34FD")

    ChrTalk(
        0xFE,
        (
            "As my husband's work got better,\x01",
            "Let's have a cup of coffee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's bean is Libertan bean\x01",
            "You surely smell nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_34FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3599")

    ChrTalk(
        0xFE,
        (
            "Actually, around this morning\x01",
            "Various new work\x01",
            "I have come down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband also tower's work\x01",
            "Just because it's over,\x01",
            "There is not much time to rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3630")

    ChrTalk(
        0xFE,
        (
            "I do not even listen if my husband\x01",
            "About the Orkis Tower\x01",
            "It tells us various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, the unveiling of the daytime\x01",
            "It seems that the excitement is not overwhelming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C3")

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower\x01",
            "Masters involved in design, too,\x01",
            "I was present at the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By this time, the completion of completion\x01",
            "It may be around the time of immersion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_36C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3749")

    ChrTalk(
        0xFE,
        (
            "It was a particularly big job this time\x01",
            "My husband seems to be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even coffee is brewed\x01",
            "Shall I calm down?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FB")

    label("loc_3749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3826")

    ChrTalk(
        0xFE,
        (
            "About the master's grandfather\x01",
            "I often hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that he was a very good architect,\x01",
            "It is an eternal goal of my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little, to the complex\x01",
            "Maybe there is a feeling part\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38BD")

    label("loc_3826")


    ChrTalk(
        0xFE,
        (
            "My husband was an excellent architect\x01",
            "Complex to your grandfather\x01",
            "I feel it feels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband is doing my best to be his husband,\x01",
            "I think that is fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BD")

    Jump("loc_39FB")

    label("loc_38C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3995")

    ChrTalk(
        0xFE,
        (
            "My husband is designing a new city hall building\x01",
            "It became involved again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a big job,\x01",
            "Stuff root for the past month\x01",
            "I was working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it seems that it has gone one way too\x01",
            "relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39FB")

    label("loc_3995")


    ChrTalk(
        0xFE,
        (
            "My house is at the design office\x01",
            "It is getting on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently in the design of the new city hall\x01",
            "I was busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FB")

    TalkEnd(0xFE)
    Return()

    # Function_7_2D43 end

    def Function_8_39FF(): pass

    label("Function_8_39FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A92")

    ChrTalk(
        0xFE,
        (
            "After all, noisy\x01",
            "It is something that has become a world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make some shelter in the basement\x01",
            "I am hiding with my grandmother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B0E")

    ChrTalk(
        0xFE,
        (
            "Muu is outside\x01",
            "Is my car safe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do hurt\x01",
            "I will demand compensation for damages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B1C")
    Jump("loc_437F")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CEC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B58")
    Call(0, 19)
    Return()

    label("loc_3B58")


    ChrTalk(
        0xFE,
        (
            "Geval is now in Almorika village\x01",
            "You should be staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I will find it if I search it,\x01",
            "Ask circumstances to himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE7")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")

    ChrTalk(
        0xFE,
        (
            "Milla who sold old furniture,\x01",
            "At the charity event venue\x01",
            "Donated it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Than I use it\x01",
            "It is used much more meaningfully\x01",
            "Let's do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When everyone is in trouble.\x01",
            "To help each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CE7")

    label("loc_3CB4")


    ChrTalk(
        0xFE,
        (
            "When everyone is in trouble.\x01",
            "To help each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE7")

    Jump("loc_437F")

    label("loc_3CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")

    ChrTalk(
        0xFE,
        (
            "The town is occupied by armed groups,\x01",
            "It is unheard of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If in Mainz direction\x01",
            "If you go to the drive,\x01",
            "The possibility of being caught ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, terrible.\x01",
            "trembling……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E28")

    label("loc_3DB3")


    ChrTalk(
        0xFE,
        (
            "If in Mainz direction\x01",
            "If you go to the drive,\x01",
            "The possibility of being caught ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, terrible.\x01",
            "trembling……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E28")

    Jump("loc_437F")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E48")
    Call(0, 13)
    Jump("loc_3EB1")

    label("loc_3E48")


    ChrTalk(
        0xFE,
        (
            "（ふむ……あのAlmu君が\x01",
            "It is getting bigger so far … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(Yet, that idiot Mon … …)\x02",
    )

    CloseMessageWindow()

    label("loc_3EB1")

    Jump("loc_437F")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EC4")
    Jump("loc_437F")

    label("loc_3EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ED2")
    Jump("loc_437F")

    label("loc_3ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F59")

    ChrTalk(
        0xFE,
        (
            "I thought of going tomorrow.\x01",
            "Drive an old lady\x01",
            "You tried inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, even a little mood\x01",
            "I hope you fix it, but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_437F")

    label("loc_3F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(
        0xFE,
        (
            "From yesterday with my grandmother\x01",
            "Do you have a fight? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, living by two people\x01",
            "This cold war state\x01",
            "There are thawing pots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, how can I be with my grandmother?\x01",
            "Would you be able to reconcile …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_408E")

    label("loc_401E")


    ChrTalk(
        0xFE,
        (
            "How to do with an old lady\x01",
            "Would you be able to reconcile …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luxury wine after all ……\x01",
            "No, is not it like that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408E")

    Jump("loc_437F")

    label("loc_4093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AE")
    Call(0, 9)
    Jump("loc_4124")

    label("loc_40AE")


    ChrTalk(
        0xFE,
        (
            "I thought about drinking with me all the time\x01",
            "I bought a good wine ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it is already good.\x01",
            "Because I will drink alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4124")

    Jump("loc_437F")

    label("loc_4129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4137")
    Jump("loc_437F")

    label("loc_4137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D9")

    ChrTalk(
        0xFE,
        (
            "To protect the driving vehicle from rain and wind,\x01",
            "The garage\x01",
            "Did you want it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it gets angry over there,\x01",
            "I have no choice but to give up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4212")

    label("loc_41D9")


    ChrTalk(
        0xFE,
        (
            "Well, but until that time\x01",
            "It will not make me angry …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4212")

    Jump("loc_437F")

    label("loc_4217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E3")

    ChrTalk(
        0xFE,
        (
            "Mu, the driving force car on the table\x01",
            "I am getting wet by the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, something like a garage\x01",
            "Where do you want it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if it is tomorrow\x01",
            "I will carefully wash the car.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4371")

    label("loc_42E3")


    ChrTalk(
        0xFE,
        (
            "However, as it is,\x01",
            "It is also a thing to keep it in the field\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you live in a condominium\x01",
            "I can not install a garage\x01",
            "It is a painful place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4371")

    Jump("loc_437F")

    label("loc_4376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_437F")

    label("loc_437F")

    TalkEnd(0xFE)
    Return()

    # Function_8_39FF end

    def Function_9_4383(): pass

    label("Function_9_4383")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "Oh, after all\x01",
            "This wine is delicious.\x01",
            "I'm glad I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The old lady seems to need it,\x01",
            "I guess I should drink alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… Yes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For that, pay a high Mira\x01",
            "I guess I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Huh!\x01",
            "Give me a chance.\x02",
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

    # Function_9_4383 end

    def Function_10_44A1(): pass

    label("Function_10_44A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4542")

    ChrTalk(
        0xFE,
        (
            "My husband said that the underground shelter\x01",
            "There will be no mirrors to buy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do whatever you buy high\x01",
            "I can not get rid of the habit trying to solve it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4589")

    ChrTalk(
        0xFE,
        (
            "Completely, if the master\x01",
            "Until such a time of worrying about cars ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4630")

    ChrTalk(
        0xFE,
        (
            "I heard a speech ….\x01",
            "The Empire and the Republic have been crossbells so far\x01",
            "暗闘を繰り広げてたIt seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a crossbell resident,\x01",
            "It's not something I can forgive … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46BD")

    ChrTalk(
        0xFE,
        (
            "For the reconstruction of the city\x01",
            "My husband made a donation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Use Mira only for myself\x01",
            "I thought it was a waste,\x01",
            "I reviewed it slightly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_46BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_472F")

    ChrTalk(
        0xFE,
        (
            "No way, such a big incident\x01",
            "I wake up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard managed to\x01",
            "I hope you solve it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4797")

    ChrTalk(
        0xFE,
        (
            "Almu君が家庭を持って\x01",
            "I'm into a crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, anyhow\x01",
            "It seems to be happy and what is more than anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_47A5")
    Jump("loc_4E48")

    label("loc_47A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47B3")
    Jump("loc_4E48")

    label("loc_47B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4853")

    ChrTalk(
        0xFE,
        (
            "How does the wind blow\x01",
            "I do not know but ….\x01",
            "My husband invited me to drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Absolutely …\x01",
            "To that extent my mood can be taken\x01",
            "I wonder if I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_4853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48CA")

    ChrTalk(
        0xFE,
        (
            "For a while with my husband\x01",
            "I do not give my mouth\x01",
            "I decided to decide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until I apologize\x01",
            "Do you forgive me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E48")

    label("loc_48CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_491B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E5")
    Call(0, 9)
    Jump("loc_4916")

    label("loc_48E5")


    ChrTalk(
        0xFE,
        (
            "…… Hmm, what about my husband?\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4916")

    Jump("loc_4E48")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D2")

    ChrTalk(
        0xFE,
        (
            "My husband silent me\x01",
            "High class vintage wine\x01",
            "I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in the case of the garage during this time,\x01",
            "Even though I got angry that much …\x01",
            "I do not reflect on it at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A16")

    label("loc_49D2")


    ChrTalk(
        0xFE,
        (
            "My husband ……\x01",
            "Even if I am delighted with my own waste habit\x01",
            "I wonder why.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A16")

    Jump("loc_4E48")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B14")

    ChrTalk(
        0xFE,
        (
            "My husband, inside the apartment\x01",
            "I was trying to build a garage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to persuade my husband,\x01",
            "相談されていたSammyさんが\x01",
            "I was taken aback.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, when the waste habit comes to this point\x01",
            "I can not say things by truth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BA0")

    label("loc_4B14")


    ChrTalk(
        0xFE,
        (
            "My husband, inside the apartment\x01",
            "I was trying to build a garage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, when the waste habit comes to this point\x01",
            "I can not say things by truth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA0")

    Jump("loc_4E48")

    label("loc_4BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7E")

    ChrTalk(
        0xFE,
        (
            "On such a rainy day,\x01",
            "I am limited to my hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, my hobby is handicraft.\x01",
            "Recently, patchwork something\x01",
            "I am particularly enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chubu ..\x01",
            "It's quite deep and fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D12")

    label("loc_4C7E")


    ChrTalk(
        0xFE,
        (
            "My hobby is handicraft.\x01",
            "Recently, patchwork something\x01",
            "I am particularly enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband, like me,\x01",
            "A hobby that does not cost Mira\x01",
            "You should have chosen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D12")

    Jump("loc_4E48")

    label("loc_4D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE4")

    ChrTalk(
        0xFE,
        "My husband is having trouble with wasting expenses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it is not necessary from a long time ago\x01",
            "I changed my furniture\x01",
            "I was there … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the meantime,\x01",
            "I bought a guided vehicle.\x01",
            "Altogether ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E48")

    label("loc_4DE4")


    ChrTalk(
        0xFE,
        (
            "Without any consultation\x01",
            "I bought a guided vehicle ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a wasteful habit of that person\x01",
            "It is really troubling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E48")

    TalkEnd(0xFE)
    Return()

    # Function_10_44A1 end

    def Function_11_4E4C(): pass

    label("Function_11_4E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E61")
    Call(0, 13)
    Jump("loc_4E96")

    label("loc_4E61")


    ChrTalk(
        0xFE,
        (
            "Okay, today, this way\x01",
            "I wonder if I will go to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    TalkEnd(0xFE)
    Return()

    # Function_11_4E4C end

    def Function_12_4E9A(): pass

    label("Function_12_4E9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAF")
    Call(0, 13)
    Jump("loc_4EE4")

    label("loc_4EAF")


    ChrTalk(
        0xFE,
        (
            "Hehe, it's a little by little\x01",
            "It is steadily approaching me\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE4")

    TalkEnd(0xFE)
    Return()

    # Function_12_4E9A end

    def Function_13_4EE8(): pass

    label("Function_13_4EE8")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "I see, then\x01",
            "A few months ago from Ursula hospital ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, after that too\x01",
            "Do not you know it in detail …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although I came all the way to come,\x01",
            "I can only tell you about this degree\x01",
            "I'm really sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No, such a thing.\x01",
            "It was helpful enough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        "New, your eyes\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xF,
        (
            "ああ、Airy。\x01",
            "Large Venus grabbed by three family members!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "baby",
        "Ca cake ♪\x02",
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
            "Haha, your wild,\x01",
            "It really matches well.\x02",
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

    # Function_13_4EE8 end

    def Function_14_50E2(): pass

    label("Function_14_50E2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder how this happens\x01",
            "I did not imagine it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And anyway … …\x01",
            "More than one situation now\x01",
            "I have to put it in a picture.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_50E2 end

    def Function_15_5168(): pass

    label("Function_15_5168")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517D")
    Call(0, 17)
    Jump("loc_52D5")

    label("loc_517D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529C")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "#04206FHa Ha ha ……\x02\x03",
            "#04201Fなあ、Iliaさん。\x01",
            "Is not it enough already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01703FBecause I can still see the color of tension\x01",
            "I guess it will be a little more loose.\x02\x03",
            "#01702FAnyway, for now\x01",
            "You leave yourself silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04206FUU……\x01",
            "How long is it going on forever?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    Jump("loc_52D5")

    label("loc_529C")


    ChrTalk(
        0xE,
        (
            "#04206FUU……\x01",
            "Anything's fine\x01",
            "Please end it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D5")

    TalkEnd(0xFE)
    Return()

    # Function_15_5168 end

    def Function_16_52D9(): pass

    label("Function_16_52D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EE")
    Call(0, 17)
    Jump("loc_54B9")

    label("loc_52EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5400")

    ChrTalk(
        0xD,
        (
            "#01700FHuh, what's your brother guys as well\x01",
            "Shall I massage you?\x02\x03",
            "#01709FPersonally, female team priority\x01",
            "I want to go, but the spout\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FOh, haha ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, I will hold back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04206F(Ha, it's a chiraf this way\x01",
            "I will come over … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54B9")

    label("loc_5400")


    ChrTalk(
        0xD,
        (
            "#01700FToward the performance of the night, firmly\x01",
            "Shuriの身体をほぐしておかないとね。\x02\x03",
            "#01709FThere is no worry if it is prepared … …\x01",
            "I have a massage for girls Ne\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04206F(Yes, you do not understand the meaning … …)\x02",
    )

    CloseMessageWindow()

    label("loc_54B9")

    TalkEnd(0xFE)
    Return()

    # Function_16_52D9 end

    def Function_17_54BD(): pass

    label("Function_17_54BD")

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
        "#11P#01709FOh, ya brother you ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04205F#5PYo\x02\x03",
            "#04206F…… cassette ride! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWhat are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01704FHuff, tonight to the alkane shell\x01",
            "The leaders of the countries\x01",
            "I'm coming to the theater ….\x02\x03",
            "#01702FShuriにも端役として\x01",
            "I am supposed to be helped.\x02\x03",
            "#01709FFor softening the body\x01",
            "It's massage time … … Yop!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(50)
    SetChrSubChip(0xE, 0x0)

    def lambda_56E5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_56E5)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#04212F#11P#4SAh ah ah! It is!\x02",
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
        "#6P#00102FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FWell, that, is that okay?\x02\x03",
            "#10106FWhen an amateur touches muscles, it is counterproductive\x01",
            "I will also listen to the story, but ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#11P#01704FHuh, you do not need to worry.\x02\x03",
            "#01702FBefore a professional massage master\x01",
            "Tell me exactly,\x01",
            "I mastered it perfectly.\x02\x03",
            "In stretching between practice and etc.,\x01",
            "It is doing well to Lisha, is not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FIndeed, for the stage\x01",
            "Absorb any field\x01",
            "Is it okay to use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309Fいや〜、さすがIliaさんッス！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "#04206F#5PNo no no …\x01",
            "Because painful things hurt! It is!\x02\x03",
            "#04201Fイ、Iliaさん、本当の本当に\x01",
            "I wonder if it is OK! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01706FSo, like dijob\x01",
            "You said that from a while ago.\x02\x03",
            "#01700FWhat I hurt any more, on tonight's stage\x01",
            "Because my body is getting nervous and hard.\x02\x03",
            "#01709FDo not worry, while you continue\x01",
            "As it gradually becomes comfortable\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04207F#5PThere is no objectionable way of saying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01701FOh no, it is noisy.\x01",
            "If you do not stay still …… like this!\x02",
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
        "#5P#04212F#5SHyeah ah! Is it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xE,
        "#5P#04207FHow, where and where are you touching! It is! Is it? Is it?\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    SetChrSubChip(0xE, 0x1)

    ChrTalk(
        0xD,
        (
            "#11P#01709FMuhufu, be relieved.\x01",
            "Because this is also a solid massage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04207F#5PLie, you lie! It is!\x02\x03",
            "#04209FHahahaha, ticklish ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01709FYes, yeah, I'm growing Up growing eyes\x01",
            "You are promising in the future unexpected, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04212F#5PThen, you know! It is!\x02",
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
            "#6P#00113FWell, as expected\x01",
            "I feel like this is something … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FHuh, this has a taste in this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHahaha, whatever you say\x01",
            "Shuriもアルカンシェルに\x01",
            "I feel like familiar.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5P#04207FWell, do not put it in a summary\x01",
            "Please help me! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#01709FHey Hey, I will not let it escape.\x02",
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

    # Function_17_54BD end

    def Function_18_5F63(): pass

    label("Function_18_5F63")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_629F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6141")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the other side of the door,\x01",
            "IliaとShuriの賑やかな声が\x01",
            "I can hear it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Shuriの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, hahahahah ….\x01",
            "So, Soko is different!\x02\x03",
            "Ha Ha……\x01",
            "Iliaさん、さっきから\x01",
            "Have you done that on purpose?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Iliaの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, I'm in the mood!\x02",
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
        "#00012FIliaさん、凄く楽しそうだな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FShuriちゃん……かわいそうに。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetScenarioFlags(0x0, 7)
    Jump("loc_629A")

    label("loc_6141")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the other side of the door,\x01",
            "IliaとShuriの賑やかな声が\x01",
            "I can hear it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Shuriの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はあHa Ha……\x01",
            "How long is it going on forever?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 20, -1, -1)
    SetChrName("Iliaの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, you are\x01",
            "If you are growing quiet a bit more\x01",
            "I think that it will be done quickly\x02",
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

    label("loc_629A")

    Jump("loc_62CA")

    label("loc_629F")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_62CA")

    TalkEnd(0xFF)
    Return()

    # Function_18_5F63 end

    def Function_19_62CE(): pass

    label("Function_19_62CE")

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
            "#2POh, you guys ……\x01",
            "Is there something for this tin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FSorry, I suddenly visited\x01",
            "I am sorry but …\x02\x03",
            "#00000FIn the name of Mr. Geval, says\x01",
            "Does it make sense?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#2PHmm, are you acquainted with Gevall?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PCertainly he was in parliamentary era\x01",
            "It's a man I was looking after … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FIt looks like he was a bingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FUm, actually …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Loids, Gebal's son and couple\x01",
            "I explained what he was looking for.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#2PHmm, I see.\x01",
            "You guys are asked by them … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PActually during this time, Mr. Gebal\x01",
            "\"I want to hide from crossbells\"\x01",
            "You consulted with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PWhew, that idiot mon …\x01",
            "Blessed with such kind son couple,\x01",
            "I wonder what will escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FAfter all, Mr. Gebal's whereabouts\x01",
            "Did you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHowever, \"hide yourself\"\x01",
            "What does that mean?\x02\x03",
            "#00303FI do not understand why it is not long … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FThat's right!\x01",
            "せっかくAlmuさんたちが\x01",
            "You said you wanted to see him ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PWell, looking at others\x01",
            "Is not it a tricky thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2P… … no, about that\x01",
            "I will not say it from my mouth.\x02",
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
            "#2P…… Ayatsu is now in Almorika village\x01",
            "You should be staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2PSince I will find it if I search it,\x01",
            "Ask circumstances to himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI understand……\x01",
            "Thank you very much.\x02\x03",
            "#00000FIn the village of Almorika\x01",
            "Let's face it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's do that.\x02",
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

    # Function_19_62CE end

    SaveToFile()

Try(main)
