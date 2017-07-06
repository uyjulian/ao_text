﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1450.bin",                # FileName
        "c1450",                    # MapName
        "c1450",                    # Location
        0x0033,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 51, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1450",                  # 0
        "タントス老人",           # 1
        "ガイトナー",             # 2
        "ゲバル",                 # 3
        "コロナ",                 # 4
        "リマ",                   # 5
        "メルスン",               # 6
        "研修医ミショー",         # 7
        "リーシャ",               # 8
        "パオラ婆さん",           # 9
        "ヴァン",                 # 10
        "ルゼ",                   # 11
        "アゼル",                 # 12
        "男の声",                 # 13
        "バッカス",               # 14
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch21000.itc",                   # 01
        "chr/ch47700.itc",                   # 02
        "apl/ch50375.itc",                   # 03
        "chr/ch21002.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch05200.itc",                   # 09
        "chr/ch47702.itc",                   # 0A
        "chr/ch23300.itc",                   # 0B
        "chr/ch20702.itc",                   # 0C
        "chr/ch26202.itc",                   # 0D
        "chr/ch24002.itc",                   # 0E
        "chr/ch23000.itc",                   # 0F
        "chr/ch24700.itc",                   # 10
        "chr/ch23400.itc",                   # 11
    ))

    DeclNpc(4269,    0,       4294915137, 90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(52340,   29,      959,     180,  389,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(51130,   0,       3210,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(51200,   0,       54049,   0,    261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  261,  0x0, 0,   7,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294921436, 0,       3589,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294965657, 29,      56029,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(51200,   0,       54049,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(16379,   3500,    3470,    180,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(16379,   3500,    2069,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(17899,   3500,    4294967257, 0,    126,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(32799,   4294960796, 4294930346, 315,  389,  0x0, 0,   17,  0,   0,   0,   0,   26,  255,  0)

    DeclActor(5800,    0,       4000,    2000,    5800,    1200,    4000,    0x007C, 0,  29, 0x0000)
    DeclActor(17900,   3500,    4294967256, 1500,    17900,   4800,    4294967256, 0x007C, 0,  19, 0x0000)

    ChipFrameInfo(824, 0)                                        # 0

    ScpFunction((
        "Function_0_338",          # 00, 0
        "Function_1_3E8",          # 01, 1
        "Function_2_413",          # 02, 2
        "Function_3_43E",          # 03, 3
        "Function_4_469",          # 04, 4
        "Function_5_937",          # 05, 5
        "Function_6_AE8",          # 06, 6
        "Function_7_1B64",         # 07, 7
        "Function_8_1D2B",         # 08, 8
        "Function_9_1E84",         # 09, 9
        "Function_10_1FDD",        # 0A, 10
        "Function_11_2CC7",        # 0B, 11
        "Function_12_2EC9",        # 0C, 12
        "Function_13_30D9",        # 0D, 13
        "Function_14_33D4",        # 0E, 14
        "Function_15_3F5D",        # 0F, 15
        "Function_16_44B4",        # 10, 16
        "Function_17_45B8",        # 11, 17
        "Function_18_468C",        # 12, 18
        "Function_19_4932",        # 13, 19
        "Function_20_50B6",        # 14, 20
        "Function_21_50F3",        # 15, 21
        "Function_22_51E2",        # 16, 22
        "Function_23_52D1",        # 17, 23
        "Function_24_53A7",        # 18, 24
        "Function_25_544E",        # 19, 25
        "Function_26_584C",        # 1A, 26
        "Function_27_5985",        # 1B, 27
        "Function_28_5B46",        # 1C, 28
        "Function_29_65DF",        # 1D, 29
        "Function_30_6705",        # 1E, 30
        "Function_31_82FA",        # 1F, 31
        "Function_32_8B84",        # 20, 32
        "Function_33_8F5B",        # 21, 33
        "Function_34_96E8",        # 22, 34
    ))


    def Function_0_338(): pass

    label("Function_0_338")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_370"),
        (1, "loc_37C"),
        (2, "loc_388"),
        (3, "loc_394"),
        (4, "loc_3A0"),
        (5, "loc_3AC"),
        (6, "loc_3B8"),
        (SWITCH_DEFAULT, "loc_3C4"),
    )


    label("loc_370")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_37C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_388")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_394")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3E7")

    Return()

    # Function_0_338 end

    def Function_1_3E8(): pass

    label("Function_1_3E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_412")
    OP_94(0xFE, 0xC602, 0xFFFFF538, 0xCFDA, 0xF50, 0x3E8)
    Sleep(300)
    Jump("Function_1_3E8")

    label("loc_412")

    Return()

    # Function_1_3E8 end

    def Function_2_413(): pass

    label("Function_2_413")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43D")
    OP_94(0xFE, 0x1CFC, 0x208A, 0x2FBC, 0x337C, 0x3E8)
    Sleep(300)
    Jump("Function_2_413")

    label("loc_43D")

    Return()

    # Function_2_413 end

    def Function_3_43E(): pass

    label("Function_3_43E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_468")
    OP_94(0xFE, 0xCC74, 0xBCCA, 0xD8C2, 0xC4C2, 0x3E8)
    Sleep(300)
    Jump("Function_3_43E")

    label("loc_468")

    Return()

    # Function_3_43E end

    def Function_4_469(): pass

    label("Function_4_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrPos(0xC, 8650, 3500, 10630, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, 8650, 3500, 11630, 180)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_4B3")

    Jump("loc_936")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_550")
    SetChrPos(0xC, 54580, 30, 48540, 135)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 55550, 200, 52190, 270)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x15, 52830, 20, -50640, 0)
    SetChrPos(0x11, 52800, 20, -48960, 180)
    SetChrPos(0x12, 51720, 0, -48250, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_936")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_59D")
    SetChrPos(0xA, 52340, 30, 960, 180)
    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0xC, 11610, 3500, 10750, 180)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xB, 11700, 3500, 9390, 0)
    Jump("loc_936")

    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5C0")
    SetChrPos(0x8, 3800, 0, 1500, 270)

    label("loc_5C0")

    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")
    SetChrPos(0x10, 52570, 30, 53820, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")
    SetChrFlags(0x13, 0x10)

    label("loc_5F2")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 4100, 30, -56450, 90)
    Jump("loc_634")

    label("loc_60D")

    SetChrPos(0x10, 52660, 30, 50020, 135)
    SetChrPos(0xB, 53860, 30, 48820, 315)
    SetChrFlags(0x10, 0x10)

    label("loc_634")

    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_936")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0xA, 51130, 0, 3210, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_936")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C2")
    SetChrPos(0xA, 3400, 0, 3610, 270)
    SetChrPos(0xB, 1320, 0, 3550, 90)
    SetChrPos(0xC, 2020, 0, 2420, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_936")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_73A")
    SetChrPos(0x8, 1590, 200, -55120, 270)
    SetChrChipByIndex(0x8, 0xE)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 10560, 3500, 10830, 135)
    SetChrPos(0xB, 11700, 3500, 9390, 315)
    SetChrPos(0xC, 12540, 3500, 11160, 225)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_936")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_779")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, 3400, 30, -54370, 315)
    SetChrPos(0xA, 2200, 30, -53180, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_936")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_936")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_831")
    SetChrPos(0xA, -1400, 150, -54970, 90)
    SetChrPos(0x8, 1590, 150, -55120, 270)
    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0x8, 0xE)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 55550, 200, 52190, 270)
    SetChrChipByIndex(0xC, 0xC)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52380, 200, 52200, 90)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_936")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_86E")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xA, 51130, 0, 3210, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_936")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 8650, 3500, 10630, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, 8650, 3500, 11630, 180)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_936")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_923")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FC")
    SetChrPos(0x9, 2200, 30, -53180, 135)
    SetChrPos(0x8, 3400, 30, -54370, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_91E")

    label("loc_8FC")

    SetChrPos(0x9, 2200, 30, -53180, 135)
    SetChrPos(0x8, 3400, 30, -54370, 315)

    label("loc_91E")

    Jump("loc_936")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_936")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_936")

    Return()

    # Function_4_469 end

    def Function_5_937(): pass

    label("Function_5_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_952")
    OP_65(0x1, 0x1)
    Jump("loc_95C")

    label("loc_952")

    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_974")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_991")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_9A9")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C4")
    OP_66(0x0, 0x1)
    Jump("loc_9F2")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0")
    OP_66(0x0, 0x1)
    Jump("loc_9F2")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F2")
    OP_66(0x0, 0x1)

    label("loc_9F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0B")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_A11")

    label("loc_A0B")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5A")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A99")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")
    Sound(1020, 1, 60, 0)
    Jump("loc_ACB")

    label("loc_AC8")

    OP_24(0x3FC)

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE7")
    ClearMapObjFlags(0x6, 0x4)

    label("loc_AE7")

    Return()

    # Function_5_937 end

    def Function_6_AE8(): pass

    label("Function_6_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BDC")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "ゲバル殿が議員時代に\x01",
            "世話になっておった人物が、\x01",
            "西通りの方におるらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "確か、ヴィ、ヴィラ……\x01",
            "『ヴィラなんとか』という名前の\x01",
            "建物に住んでおるらしい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "その人ならゲバル殿の行方を\x01",
            "知っておるかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    Call(0, 32)
    Return()

    label("loc_C05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D08")

    ChrTalk(
        0xFE,
        (
            "不良グループの子たちが、\x01",
            "協力して旧市街を\x01",
            "守ってくれておるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前は広場でのケンカも多くて\x01",
            "近寄りがたい存在じゃったが、\x01",
            "やはり若いもんは頼れるのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ここにきて、ようやく旧市街が\x01",
            "一つになり始めた気がするわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D9F")

    label("loc_D08")


    ChrTalk(
        0xFE,
        (
            "不良グループの子たちが、\x01",
            "旧市街を守ってくれておる。\x01",
            "やはり若いもんは頼れるのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ここにきて、ようやく旧市街が\x01",
            "一つになり始めた気がするわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9F")

    Jump("loc_1B60")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E2D")

    ChrTalk(
        0xFE,
        (
            "外に出ておる青いモヤは\x01",
            "一体何なんじゃろうAh…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とにかくアパートの住人が\x01",
            "外に出ないように、\x01",
            "注意しておかんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECD")

    ChrTalk(
        0xFE,
        (
            "大統領演説は\x01",
            "わしも聞かせてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "確かに主張は分かるのじゃが……\x01",
            "平和的な解決方法は\x01",
            "本当になかったのじゃろうか.......?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F32")

    label("loc_ECD")


    ChrTalk(
        0xFE,
        "確かに大統領の主張は分かるのじゃが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平和的な解決方法は\x01",
            "本当になかったのじゃろうか.......?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F32")

    Jump("loc_1B60")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1143")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_1036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_FCC")

    ChrTalk(
        0x8,
        (
            "野菜に十分火が通れば\x01",
            "調味の開始じゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "『強壮にがトマ豚汁』……\x01",
            "どうか楽しみに待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1031")

    label("loc_FCC")


    ChrTalk(
        0x8,
        (
            "さてと、そろそろ炊き出し用の\x01",
            "器を用意しておかんとな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "今日は皆に行き渡るとよいのじゃが……\x02",
    )

    CloseMessageWindow()

    label("loc_1031")

    Jump("loc_10BC")

    label("loc_1036")


    ChrTalk(
        0x8,
        (
            "炊き出しの準備は、\x01",
            "この部屋とコロナさんの部屋で\x01",
            "行っておるぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "何しろ量が量じゃからな。\x01",
            "調理場がいくつあっても\x01",
            "足りんわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BC")

    Jump("loc_113E")

    label("loc_10C1")


    ChrTalk(
        0xFE,
        (
            "ほっほっ、みんな豚汁を\x01",
            "おいしそうに食べてくれて\x01",
            "何よりじゃったわい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "お前さんたちには\x01",
            "礼を言わせてもらわねばのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113E")

    Jump("loc_1B60")

    label("loc_1143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_126A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121D")

    ChrTalk(
        0xFE,
        (
            "昨日の夕方頃、\x01",
            "珍しくゲバル殿の所に\x01",
            "来客があったんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "それからというものの、\x01",
            "ゲバル殿の様子が変でな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "誰かに追われているとか\x01",
            "言っておったが……\x01",
            "ふむ、少し心配じゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1265")

    label("loc_121D")


    ChrTalk(
        0xFE,
        (
            "誰かに追われているとか\x01",
            "言っておったが……\x01",
            "ふむ、少し心配じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1265")

    Jump("loc_1B60")

    label("loc_126A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12DA")

    ChrTalk(
        0xFE,
        (
            "どうやらゲバル殿も\x01",
            "ここでの生活に\x01",
            "馴染みつつあるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ほっほっ、結構なことじゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1413")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1384")

    ChrTalk(
        0xFE,
        (
            "パクパク……\x01",
            "ゲバル殿の煮豆、本当に絶品じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、夕食まで\x01",
            "取っておくつもりじゃったが、\x01",
            "すぐになくなってしまいそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_140E")

    label("loc_1384")


    ChrTalk(
        0xFE,
        (
            "しかし、ゲバル殿も徐々に\x01",
            "心を開いてくれてるようで何よりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "議員時代は高慢だったと聞くが、\x01",
            "どうやら心根は優しいようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140E")

    Jump("loc_1B60")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1424")
    Call(0, 7)
    Jump("loc_1B60")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152A")

    ChrTalk(
        0xFE,
        (
            "クロスベルを国家に、か……\x01",
            "極めて正当な主張ではあるが、\x01",
            "欲張り過ぎな気もするのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "２大国もあまり良い顔は\x01",
            "しておらんそうじゃし、\x01",
            "平和的に事が進むとも思えんが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いやはや、ディーター市長も\x01",
            "大胆なことを提案するもんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15A8")

    label("loc_152A")


    ChrTalk(
        0xFE,
        (
            "クロスベルを国家に、か。\x01",
            "平和的に事が進むとも思えんが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "いやはや、ディーター市長も\x01",
            "大胆なことを提案するもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A8")

    Jump("loc_1B60")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_163B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C8")
    Call(0, 8)
    Jump("loc_1636")

    label("loc_15C8")


    ChrTalk(
        0xFE,
        "ふむふむ、なるほどのう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "確かにそんな事があっては\x01",
            "誘惑に負けてしまっても\x01",
            "不思議ではないと思うぞい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1636")

    Jump("loc_1B60")

    label("loc_163B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1741")

    ChrTalk(
        0xFE,
        (
            "除幕式か……街の方では\x01",
            "大した騒ぎのようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あの新市庁ビルとやらは、\x01",
            "まさにこのクロスベルの繁栄を\x01",
            "示しているかのようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "その影で、わしらのように\x01",
            "つつましく暮らす者たちがおることも\x01",
            "忘れんで欲しいものじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17BF")

    label("loc_1741")


    ChrTalk(
        0xFE,
        (
            "しかし、ゲバル殿は相変わらず\x01",
            "塞ぎこんでおるようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "どれ、また部屋にでも呼んで\x01",
            "愚痴でも聞いてやるとするかの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BF")

    Jump("loc_1B60")

    label("loc_17C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1876")

    ChrTalk(
        0xFE,
        (
            "明日から通商会議とあって\x01",
            "この旧市街にも巡回の警官が\x01",
            "来ているようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "まあ、こんな寂れた区画は\x01",
            "間違っても首脳たちの訪れるような\x01",
            "場所ではないんじゃが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_1876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_197B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189B")
    Call(0, 9)
    Jump("loc_18E8")

    label("loc_189B")


    ChrTalk(
        0xFE,
        (
            "ふむ、ガイトナー君が\x01",
            "元気そうで何よりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "わしも本当に嬉しいぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_18E8")

    Jump("loc_1976")

    label("loc_18ED")


    ChrTalk(
        0xFE,
        (
            "お前さんたち、\x01",
            "どうかゲバル殿のことは\x01",
            "そっとしておいてやってくれるかの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "彼も色々あって、なかなか\x01",
            "気が休まらんみたいなのでな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1976")

    Jump("loc_1B60")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABC")

    ChrTalk(
        0xFE,
        (
            "この旧市街は見ての通り、\x01",
            "都市計画から\x01",
            "取り残された場所でのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "治安は悪いが家賃が安く、\x01",
            "あらゆる事情を抱えた者たちが\x01",
            "集まって来るのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そしてその一方で、\x01",
            "中にはここを巣立った後に\x01",
            "成功を掴む者もおる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、この場所には\x01",
            "本当に様々な人生模様が\x01",
            "詰まっておるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B60")

    label("loc_1ABC")


    ChrTalk(
        0xFE,
        (
            "この旧市街にはあらゆる事情を\x01",
            "抱えた者が集まって来るが、\x01",
            "中には巣立って行く者もおる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほっほっ、この場所には\x01",
            "本当に様々な人生模様が\x01",
            "詰まっておるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B60")

    TalkEnd(0xFE)
    Return()

    # Function_6_AE8 end

    def Function_7_1B64(): pass

    label("Function_7_1B64")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7F")

    ChrTalk(
        0x8,
        (
            "モグモグ……\x01",
            "ほう、これは旨いのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "この煮豆はゲバル殿が.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "ええ、久しぶりに\x01",
            "料理なんぞをしてみたら\x01",
            "つい作りすぎましてね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "とりあえず、お口に\x01",
            "合ったみたいで安心しました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ほっほっ、わざわざすまんのう。\x01",
            "本当にありがたいことじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D22")

    label("loc_1C7F")


    ChrTalk(
        0x8,
        (
            "ふむ、もしまだ余っとるのなら\x01",
            "他の人たちの所にも持って行って\x01",
            "あげてはどうかのう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "これなら、きっと\x01",
            "みんな喜んでくれるはずじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "そ、そうですか.......?\x02",
    )

    CloseMessageWindow()

    label("loc_1D22")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_1B64 end

    def Function_8_1D2B(): pass

    label("Function_8_1D2B")


    ChrTalk(
        0xA,
        "聞いてくだされ、タントス殿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "この私にも希望に満ちた\x01",
            "新人時代というものがあってですな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ほっほっ、何度も聞かされたから\x01",
            "知っておるよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "お前さんなりに、この街を\x01",
            "変えてやろうと思ってたんじゃろう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "そう、その通りなのです。\x01",
            "当時の私は志に満ち、\x01",
            "無所属で議員に選出され……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "ですがある日、\x01",
            "とある帝国派議員が私に……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_1D2B end

    def Function_9_1E84(): pass

    label("Function_9_1E84")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "おうおう、ガイトナー君。\x01",
            "元気そうで何よりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "で、商売の方はどうじゃ。\x01",
            "うまく行っておるのかの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ええ、おかげ様で順調に\x01",
            "やらせてもらっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "そうだ、今日はお土産に\x01",
            "菓子折りをお持ちしたんです。\x01",
            "よかったらどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "おお、これはありがたい。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "さっそく、茶でも入れて\x01",
            "いただくとしようかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_9_1E84 end

    def Function_10_1FDD(): pass

    label("Function_10_1FDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_219A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2100")

    ChrTalk(
        0xFE,
        (
            "ギルドに取り計らってもらってな、\x01",
            "リベールに居るアルムたちに、\x01",
            "国際通信で話すことが出来たのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "リベールも混乱はあるそうだが、\x01",
            "帝国と共和国に比べれば平和らしい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "クロスベルの混乱は\x01",
            "しばらく続きそうだが……\x01",
            "声が聞けて本当によかったぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2195")

    label("loc_2100")


    ChrTalk(
        0xFE,
        (
            "リベールに居るアルムたちに、\x01",
            "国際通信で話すことが出来たのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "クロスベルの混乱は\x01",
            "しばらく続きそうだが……\x01",
            "これでわしも頑張っていけそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2195")

    Jump("loc_22D9")

    label("loc_219A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2268")

    ChrTalk(
        0xFE,
        (
            "大統領が拘束されたと思ったら、\x01",
            "あんな得体のしれない大樹まで現れて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "せめてわしにも、何か希望があれば\x01",
            "こんな事態も乗り越えていけるのに……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女神よ、どうか救いをくだされ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22D9")

    label("loc_2268")


    ChrTalk(
        0xFE,
        (
            "せめてわしにも、何か希望があれば\x01",
            "こんな事態も乗り越えていけるのに……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女神よ、どうか救いをくだされ……\x02",
    )

    CloseMessageWindow()

    label("loc_22D9")

    Jump("loc_2CC3")

    label("loc_22DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2493")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_241C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2399")

    ChrTalk(
        0xFE,
        "この街の有様も心配だが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "リベールにいるアルムの家族は\x01",
            "無事だろうか……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "息子たちはわしの希望なのだ、\x01",
            "何とか連絡がとれないものか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2417")

    label("loc_2399")


    ChrTalk(
        0xFE,
        (
            "独立宣言以降、国外への連絡は\x01",
            "とんと途絶えてしまった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "アルムたちはわしの希望なのだ、\x01",
            "何とか連絡がとれないものか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2417")

    Jump("loc_248E")

    label("loc_241C")


    ChrTalk(
        0xFE,
        "街に出たという化物は一体……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "この旧市街にまでは\x01",
            "入ってきていないようだが、\x01",
            "本当に大丈夫なのだろうな!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248E")

    Jump("loc_2CC3")

    label("loc_2493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2861")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258B")

    ChrTalk(
        0xFE,
        (
            "ひ、東通りで演説を聞いてきたが、\x01",
            "正直耳を疑ったぞ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "発言の是非はどうあれ、\x01",
            "これでは２大国が黙っている\x01",
            "はずがないではないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "こうなると、\x01",
            "何としてでも自治州外に\x01",
            "出ることが賢明かもしれんが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26CD")

    label("loc_258B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2649")

    ChrTalk(
        0xFE,
        "リベールにはアルムたちがいるが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "フ、Ughわしは何を\x01",
            "都合の良いことを考えているのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしは腐ってもクロスベル人だ……\x01",
            "何があっても、この地に留まるぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_26CD")

    label("loc_2649")


    ChrTalk(
        0xFE,
        (
            "まSeriously…わしは何を\x01",
            "都合の良いことを考えているのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしは腐ってもクロスベル人だ……\x01",
            "何があっても、この地に留まるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26CD")

    Jump("loc_285C")

    label("loc_26D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B5")

    ChrTalk(
        0xFE,
        (
            "ひ、東通りで演説を聞いてきたが、\x01",
            "正直耳を疑ったぞ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "発言の是非はどうあれ、\x01",
            "これでは２大国が黙っている\x01",
            "はずがないではないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "こうなると、\x01",
            "何としてでも自治州外に\x01",
            "出ることが賢明かもしれんが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_285C")

    label("loc_27B5")


    ChrTalk(
        0xFE,
        (
            "……フン、わしは何をバカなことを。\x01",
            "今さら自治州を捨てて\x01",
            "他へ逃げた所で何になるというのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしは腐ってもクロスベル人だ……\x01",
            "何があっても、この地に留まるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_285C")

    Jump("loc_2CC3")

    label("loc_2861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_286F")
    Jump("loc_2CC3")

    label("loc_286F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28D3")

    ChrTalk(
        0xFE,
        (
            "じょ、冗談じゃない……\x01",
            "早く身を隠さねば!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "し、しかし、\x01",
            "一体どこに行けば……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_28D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28E4")
    Call(0, 11)
    Jump("loc_2CC3")

    label("loc_28E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28F5")
    Call(0, 12)
    Jump("loc_2CC3")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2906")
    Call(0, 7)
    Jump("loc_2CC3")

    label("loc_2906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A24")

    ChrTalk(
        0xFE,
        (
            "ふむ、ディーター市長も\x01",
            "思い切ったことをしたものだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "とにもかくにも……\x01",
            "これで一層、帝国・共和国派議員の\x01",
            "立場は悪くなるというものRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……と、わしは一体\x01",
            "何の目線で政治を語っておるのだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふう、そろそろ真剣に\x01",
            "今後の身の振り方を考えんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A66")

    label("loc_2A24")


    ChrTalk(
        0xFE,
        (
            "第２の人生か……\x01",
            "わしには一体、\x01",
            "何が残されておるのだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A66")

    Jump("loc_2CC3")

    label("loc_2A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A86")
    Call(0, 8)
    Jump("loc_2B07")

    label("loc_2A86")


    ChrTalk(
        0xFE,
        (
            "私もそんなことが\x01",
            "言い訳にならんことは\x01",
            "重々判ってはおるのです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ですが、当時はとにかく\x01",
            "右も左も判らない若造でしてね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B07")

    Jump("loc_2CC3")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B77")

    ChrTalk(
        0xFE,
        "ぬわ〜にが、ＶＩＰの来訪だ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "まったく、どいつもこいつも\x01",
            "お祭り気分で浮かれおって!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_2B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C16")

    ChrTalk(
        0xFE,
        "フ、Ugh何が通商会議だ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしはもう、\x01",
            "議会に興味がなければ\x01",
            "政治にすらも興味はない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "何でも勝手にすればいいのだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C5A")

    label("loc_2C16")


    ChrTalk(
        0xFE,
        "フ、Ugh何が通商会議だ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "何でも勝手にすればいいのだ。\x02",
    )

    CloseMessageWindow()

    label("loc_2C5A")

    Jump("loc_2CC3")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CBA")

    ChrTalk(
        0xFE,
        "ま、まだ何か用があるのか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用がなければ、\x01",
            "さっさと出て行くがいい!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_2CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CC3")

    label("loc_2CC3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1FDD end

    def Function_11_2CC7(): pass

    label("Function_11_2CC7")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E51")

    ChrTalk(
        0xB,
        (
            "あのこれ、クッキーを\x01",
            "焼いたんですけど、\x01",
            "よかったらと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "えへへ。\x01",
            "ママの手作りクッキー、\x01",
            "おいしいよー♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "そ、そんな、申し訳ない。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "これではまるで、\x01",
            "お礼をもらうために……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ふふ、細かい事は\x01",
            "気になさらないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "こちらも同じように\x01",
            "余分に作ってしまっただけの\x01",
            "ことですので。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "そ、そうですか、では……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBC")

    label("loc_2E51")


    ChrTalk(
        0xA,
        (
            "サクサク……\x01",
            "うむ、これはうまい!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "えへへ、でしょでしょ〜♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "ふふ、喜んで頂けて良かったです。\x02",
    )

    CloseMessageWindow()

    label("loc_2EBC")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_2CC7 end

    def Function_12_2EC9(): pass

    label("Function_12_2EC9")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3026")

    ChrTalk(
        0xC,
        (
            "ママ、このお豆さん、\x01",
            "とってもおいしーねー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ふふ、リマったら\x01",
            "すっかり気に入っちゃって。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ゲバルさん、本当に\x01",
            "頂いてもよろしいんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "え、ええ、勿論ですとも。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "どうせ１人では\x01",
            "食べ切れなかったので、\x01",
            "遠慮せずにもらってやって下さい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ehe, thank you so much\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "ありがとね、おじちゃん!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30CC")

    label("loc_3026")


    ChrTalk(
        0xC,
        (
            "ひょいパクッ。\x01",
            "う〜ん、おいしー!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "もうリマったら。\x01",
            "ツマミ食いはいけないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "はは、お子さんに\x01",
            "こんなに喜んでもらえるなんて\x01",
            "ありがたいことですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30CC")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_2EC9 end

    def Function_13_30D9(): pass

    label("Function_13_30D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30EA")
    Jump("loc_33D0")

    label("loc_30EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_30F8")
    Jump("loc_33D0")

    label("loc_30F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3106")
    Jump("loc_33D0")

    label("loc_3106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3114")
    Jump("loc_33D0")

    label("loc_3114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3122")
    Jump("loc_33D0")

    label("loc_3122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3251")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CD")

    ChrTalk(
        0xFE,
        "ふう、やっぱり通いはつらいよな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でも、ここには仲良くさせて\x01",
            "もらっている人も多いし……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "なかなか、\x01",
            "出て行く気になれないんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_324C")

    label("loc_31CD")


    ChrTalk(
        0xFE,
        (
            "通いはつらいけど、\x01",
            "このアパートには仲良くさせて\x01",
            "もらっている人も多いし……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "なかなか、\x01",
            "出て行く気になれないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324C")

    Jump("loc_33D0")

    label("loc_3251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_325F")
    Jump("loc_33D0")

    label("loc_325F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_326D")
    Jump("loc_33D0")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_327B")
    Jump("loc_33D0")

    label("loc_327B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3289")
    Jump("loc_33D0")

    label("loc_3289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3297")
    Jump("loc_33D0")

    label("loc_3297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3334")

    ChrTalk(
        0xFE,
        (
            "えっと、オリエンテーションの\x01",
            "時にもらった資料は、と……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "はぁ、まだ入学して日も浅いのに\x01",
            "忘れ物なんて先が思いやられるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33D0")

    label("loc_3334")


    ChrTalk(
        0xFE,
        (
            "ふふ、でも僕\x01",
            "あのウルスラ医科大学に\x01",
            "本当に受かったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "受験なんかよりこれからが\x01",
            "大変って話But…もう少し\x01",
            "合格の余韻に浸ってもいいよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D0")

    TalkEnd(0xFE)
    Return()

    # Function_13_30D9 end

    def Function_14_33D4(): pass

    label("Function_14_33D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(
        0xFE,
        (
            "あの大きな青白い樹を見ると、\x01",
            "どうしても不安な気持ちになります。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外で仕事をする夫も\x01",
            "同じ気持ちでしょうけど……\x01",
            "なんとか応援してあげたいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_34FB")

    ChrTalk(
        0xFE,
        (
            "戒厳令とは言われていましたけど、\x01",
            "まさかここまでのことが起きるなんて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……料理をする手も震えますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_34FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35AB")

    ChrTalk(
        0xFE,
        (
            "演説の話をタントスさんから\x01",
            "伺ったのですが……\x01",
            "正直不安な気持ちで一杯です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主人は今日も普通に\x01",
            "仕事に出かけましたけど……\x01",
            "早く家に帰ってきてほしいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_35AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3670")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FF")

    ChrTalk(
        0xFE,
        (
            "お大根は火が通りにくいから\x01",
            "隠し包丁を入れて、と……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_366B")

    label("loc_35FF")

    OP_4B(0x10, 0x0)

    ChrTalk(
        0xB,
        (
            "さてと、次は\x01",
            "夕方の炊き出しメニューを\x01",
            "決めないとTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "そうですねぇ、なにがいいかしら。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_366B")

    Jump("loc_3F59")

    label("loc_3670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_370F")

    ChrTalk(
        0xFE,
        (
            "マインツの方で恐ろしい事件が\x01",
            "起こっているそうTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今も警備隊の人たちが\x01",
            "戦っているらしいですけど……\x01",
            "一刻も早く解決して欲しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_370F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3720")
    Call(0, 11)
    Jump("loc_3F59")

    label("loc_3720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3731")
    Call(0, 12)
    Jump("loc_3F59")

    label("loc_3731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37BE")

    ChrTalk(
        0xFE,
        (
            "主人はまた新しい現場で\x01",
            "仕事を始めたんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毎日毎日家族のために\x01",
            "頑張って働いてくれて……\x01",
            "感謝の言葉もありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_37BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_39F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395C")

    ChrTalk(
        0xFE,
        (
            "この前、主人から聞いたんですが……\x01",
            "オルキスタワーの建設には\x01",
            "外国の建設会社も多く関わったとか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "何でもフロアによって\x01",
            "完全に分担が決まっていて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主人はその中でも\x01",
            "上階のＶＩＰフロアと国際会議場の\x01",
            "施工に携わったそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "国際会議場といえば、\x01",
            "先日の通商会議が\x01",
            "まさに行われた場所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、ウチの主人が\x01",
            "仕事をした場所だと思うと、\x01",
            "何だか私まで嬉しくなりますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_39F0")

    label("loc_395C")


    ChrTalk(
        0xFE,
        (
            "国際会議場といえば、\x01",
            "先日の通商会議が\x01",
            "まさに行われた場所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、ウチの主人が\x01",
            "仕事をした場所だと思うと、\x01",
            "何だか私まで嬉しくなりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F0")

    Jump("loc_3F59")

    label("loc_39F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A6F")

    ChrTalk(
        0xFE,
        (
            "以前リーシャさんから頂いた\x01",
            "緑茶を淹れている所なんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、この茶葉、\x01",
            "とてもいい香りがします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_3A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A7D")
    Jump("loc_3F59")

    label("loc_3A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B42")

    ChrTalk(
        0xFE,
        (
            "オルキスタワーも\x01",
            "後は除幕式を残すだけ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "おかげさまでようやく、\x01",
            "主人の仕事も\x01",
            "落ち着いてくれました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明日は、主人の仕事を\x01",
            "目に焼き付けないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BA4")

    label("loc_3B42")


    ChrTalk(
        0xFE,
        (
            "いよいよ明日が\x01",
            "オルキスタワーの除幕式……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主人の仕事を\x01",
            "目に焼き付けないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA4")

    Jump("loc_3F59")

    label("loc_3BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBD")

    ChrTalk(
        0xFE,
        (
            "ウチの主人は建設現場で\x01",
            "働いているのですが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "この数ヶ月間は、話題の新市庁ビル\x01",
            "《オルキスタワー》の現場で\x01",
            "汗を流しているんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "もう内部は完成していて、\x01",
            "後は外装の仕上げを\x01",
            "残すのみだそうですが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ふふ、本当に完成が楽しみです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D3B")

    label("loc_3CBD")


    ChrTalk(
        0xFE,
        (
            "《オルキスタワー》の建設は\x01",
            "これまで主人が関わってきた中でも\x01",
            "一番大きい仕事なんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ふふ、本当に完成が楽しみです。\x02",
    )

    CloseMessageWindow()

    label("loc_3D3B")

    Jump("loc_3F59")

    label("loc_3D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB5")

    ChrTalk(
        0xFE,
        (
            "ここ数年、自治州議会の方で\x01",
            "旧市街の再開発計画が\x01",
            "検討されていたそうなんですが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "新議会で改めて審議した結果、\x01",
            "計画は正式に凍結されることが\x01",
            "決まったそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あくまで凍結という話なので\x01",
            "手放しでは喜べませんが……\x01",
            "それを聞いた時は安心しました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "もしここが取り壊されでもしたら、\x01",
            "私たち家族は行き場を\x01",
            "失ってしまいますからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F59")

    label("loc_3EB5")


    ChrTalk(
        0xFE,
        (
            "何でも計画の中心にいた\x01",
            "議員さんが、例の教団事件絡みで\x01",
            "逮捕されたらしくって……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "おまけに計画そのものにも\x01",
            "不備が多かったために、\x01",
            "話が頓挫したらしいTrue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F59")

    TalkEnd(0xFE)
    Return()

    # Function_14_33D4 end

    def Function_15_3F5D(): pass

    label("Function_15_3F5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7B")
    Call(0, 16)
    Jump("loc_3FE2")

    label("loc_3F7B")


    ChrTalk(
        0xFE,
        (
            "パパはこんな時でも\x01",
            "リマたちのために\x01",
            "がんばってるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "よーし、\x01",
            "リマもがんばらなくちゃ!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE2")

    Jump("loc_44B0")

    label("loc_3FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_402D")

    ChrTalk(
        0xFE,
        "パパもママも、不安そうなの。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "大丈夫かなAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4080")

    ChrTalk(
        0xFE,
        (
            "ママ……\x01",
            "悲しそうなお顔をしているの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "元気出して欲しいの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_4080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_408E")
    Jump("loc_44B0")

    label("loc_408E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_40F3")

    ChrTalk(
        0xFE,
        (
            "リーシャお姉ちゃん、\x01",
            "今日はなんだか元気がなかったの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "なにかあったのかなー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4104")
    Call(0, 11)
    Jump("loc_44B0")

    label("loc_4104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4115")
    Call(0, 12)
    Jump("loc_44B0")

    label("loc_4115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_425B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F5")

    ChrTalk(
        0xFE,
        (
            "今朝は、ママといっしょに\x01",
            "パパのことをお見送りしたの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今日は新しいゲンバのしょにちだから\x01",
            "いり時間にゆとりがあったらしいの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "リマはよく分からないけど、\x01",
            "お見送りできてうれしかったの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4256")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "ママとリマで、パパに\x01",
            "行ってらっしゃいのチューをしたの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "パパ、照れててかわいかったの。\x02",
    )

    CloseMessageWindow()

    label("loc_4256")

    Jump("loc_44B0")

    label("loc_425B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42B8")

    ChrTalk(
        0xFE,
        (
            "わんだーらんど、\x01",
            "ほんとに楽しかったのー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "またみんなで行きたいなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_42B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42EA")

    ChrTalk(
        0xFE,
        "お茶、お茶♪　みんなでお茶〜♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_42EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42F8")
    Jump("loc_44B0")

    label("loc_42F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4313")
    Call(0, 17)
    Jump("loc_4360")

    label("loc_4313")


    ChrTalk(
        0xFE,
        (
            "はい、あなた。\x01",
            "ゴハンのよういができたわよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "た〜んと、めしあがれ♪\x02",
    )

    CloseMessageWindow()

    label("loc_4360")

    Jump("loc_44B0")

    label("loc_4365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E9")

    ChrTalk(
        0xFE,
        (
            "リマのパパは、\x01",
            "毎日けんせつげんばで\x01",
            "働いているの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今日も帰るのおそくなるらしいの。\x01",
            "Ugh…\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_441F")

    label("loc_43E9")


    ChrTalk(
        0xFE,
        (
            "パパは今日も\x01",
            "帰るの遅くなるらしいの。\x01",
            "Ugh…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441F")

    Jump("loc_44B0")

    label("loc_4424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44B0")

    ChrTalk(
        0xFE,
        (
            "最近、いじわるな\x01",
            "おやくにんさんが来なくなったって\x01",
            "ママが喜んでるの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "よく分からないけど、\x01",
            "ママが喜ぶとリマもうれしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B0")

    TalkEnd(0xFE)
    Return()

    # Function_15_3F5D end

    def Function_16_44B4(): pass

    label("Function_16_44B4")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        "パパ、今日もお仕事に行くの？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "ああ、今の建築現場が再開したからね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "リマ、色々と不安だろうけど\x01",
            "ママと一緒にお留守番を頼むな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "うOh, got it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "パパ、いってらっしゃい!\x01",
            "……ちゅっ噴\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "はは、いってきます。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_44B4 end

    def Function_17_45B8(): pass

    label("Function_17_45B8")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "よ〜し、リマ。\x01",
            "今日は何をして遊ぼうか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "う〜んとね。\x01",
            "じゃあ、おままごとがいい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "リマがママの役をやるから\x01",
            "パパはパパの役ね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "はは、パパはパパの役か。\x01",
            "なるほど、分かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_17_45B8 end

    def Function_18_468C(): pass

    label("Function_18_468C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_473C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AA")
    Call(0, 16)
    Jump("loc_4737")

    label("loc_46AA")


    ChrTalk(
        0xFE,
        (
            "いやはHaha…\x01",
            "こういうのは照れてしまうけど、\x01",
            "やっぱり元気が出るね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "よーし、色々と不安はあるけど……、\x01",
            "家族の為に今日も働くぞー!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4737")

    Jump("loc_492E")

    label("loc_473C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_47C4")

    ChrTalk(
        0xFE,
        (
            "こんな事になってしまって、\x01",
            "どうしていいか分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "何があってもコロナとリマだけは\x01",
            "守ってやらないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492E")

    label("loc_47C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_47D2")
    Jump("loc_492E")

    label("loc_47D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47E0")
    Jump("loc_492E")

    label("loc_47E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_47EE")
    Jump("loc_492E")

    label("loc_47EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_47FC")
    Jump("loc_492E")

    label("loc_47FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_480A")
    Jump("loc_492E")

    label("loc_480A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4818")
    Jump("loc_492E")

    label("loc_4818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4826")
    Jump("loc_492E")

    label("loc_4826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_489D")

    ChrTalk(
        0xFE,
        (
            "ふう、こんなにゆったりした\x01",
            "時間を過ごすのは久しぶりだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "家族団らんって、本当にいいものだね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_492E")

    label("loc_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48AB")
    Jump("loc_492E")

    label("loc_48AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4917")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C6")
    Call(0, 17)
    Jump("loc_4912")

    label("loc_48C6")


    ChrTalk(
        0xFE,
        "ああ、ありがとう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "モグモグ……\x01",
            "うん、今日もとっても\x01",
            "おいしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4912")

    Jump("loc_492E")

    label("loc_4917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4925")
    Jump("loc_492E")

    label("loc_4925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_492E")

    label("loc_492E")

    TalkEnd(0xFE)
    Return()

    # Function_18_468C end

    def Function_19_4932(): pass

    label("Function_19_4932")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_49BC")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごご。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "おい、ディーター……\x01",
            "独立すりゃあ幸せになれんのかぁ.......?\x01",
            "……んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_49BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49CA")
    Jump("loc_50B2")

    label("loc_49CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4A38")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "夢の国はどこだぁ……\x01",
            "ヴァ〜ン、連れてってくれぇ〜い……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_4A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B05")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC1")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x01",
            "誰だぁ、雨降らせやがったのはぁ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ションベンが近くなるだろうがぁ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4B00")

    label("loc_4AC1")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x01",
            "漏らしたらどうするつもりだぁ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B00")

    Jump("loc_50B2")

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B6B")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "オレは宵越しのぉ……\x01",
            "ミラは持たねぇ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "そういう男だぁ……んごUh\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_4B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C5A")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C15")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "せっかくぅ……手にしたぁ……\x01",
            "１０００ミラ札〜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "カジノでぇ……気付けばぁ……\x01",
            "すかんぴん〜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4C55")

    label("loc_4C15")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "オレのミラぁ……返せぇ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C55")

    Jump("loc_50B2")

    label("loc_4C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D7C")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D0B")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごご。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "おらぁ、ヴァ〜ン!\x01",
            "これで文句ねえだろぉ…!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "大黒柱がぁ……\x01",
            "稼いできてやったぞぉ……\x01",
            "うぃ〜、ヒック……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D77")

    label("loc_4D0B")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "大黒柱がぁ……\x01",
            "稼いできてやったぞぉ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "でも家賃は待ってくだしゃ〜い……\x01",
            "うぃ〜、ヒック……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D77")

    Jump("loc_50B2")

    label("loc_4D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA6")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E49")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んごー……んあ.......?\x01",
            "おお、ちゃんと酒あるじゃねえか。\x01",
            "でかしたぞ、ヴァン。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ぐびぐび…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "ぐえあ!？　ぺっぺっ…!\x01",
            "なんじゃこりゃ、酢じゃねえか!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4EA1")

    label("loc_4E49")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "誰だぁこんなことしやがったのはぁ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "タダじゃおかね………むにゃにゃ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA1")

    Jump("loc_50B2")

    label("loc_4EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F93")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3B")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "あァ？　ミラがねぇだとぉ〜？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "仕方ねUh…だったら\x01",
            "ちょいと日雇いのぉ〜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4F8E")

    label("loc_4F3B")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "仕方ねUh…だったら\x01",
            "ちょいと日雇いのぉ〜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8E")

    Jump("loc_50B2")

    label("loc_4F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FF9")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒ぇ、酒ぇ……\x01",
            "マイベストフレ〜ンド、酒ぇ…!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_4FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5055")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "おい、ヴァ〜ン!\x01",
            "酒はまだかぁ〜…!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_5055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50B2")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "んぐー……んごー……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒ぇ〜、酒ぇ〜。\x01",
            "……酒もってこいぃ〜…!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B2")

    TalkEnd(0x14)
    Return()

    # Function_19_4932 end

    def Function_20_50B6(): pass

    label("Function_20_50B6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされており、\x01",
            "中から声が聞こえる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_20_50B6 end

    def Function_21_50F3(): pass

    label("Function_21_50F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5112")
    Call(0, 9)
    Jump("loc_517E")

    label("loc_5112")


    ChrTalk(
        0x9,
        (
            "タントスさんの方こそ\x01",
            "お元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "本当に、ここの皆さんには\x01",
            "感謝してもしきれませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517E")

    Jump("loc_51DE")

    label("loc_5183")


    ChrTalk(
        0x9,
        (
            "私の転出届けの方は必ず\x01",
            "今日の内に提出しておくよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "手間をかけて申し訳なかったね。\x02",
    )

    CloseMessageWindow()

    label("loc_51DE")

    TalkEnd(0xFE)
    Return()

    # Function_21_50F3 end

    def Function_22_51E2(): pass

    label("Function_22_51E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5261")

    ChrTalk(
        0xFE,
        "あら、どちら様ですかねぇ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "炊き出しの方はもう少し\x01",
            "時間がかかるから、\x01",
            "待っていてくださるかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52CD")

    label("loc_5261")

    OP_4B(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "さてと、次は\x01",
            "夕方の炊き出しメニューを\x01",
            "決めないとTrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "そうですねぇ、なにがいいかしら。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0x0)

    label("loc_52CD")

    TalkEnd(0xFE)
    Return()

    # Function_22_51E2 end

    def Function_23_52D1(): pass

    label("Function_23_52D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_535E")

    ChrTalk(
        0xFE,
        (
            "（最近は酒が手に入らなかったから\x01",
            "  ヘコんでると思ったら……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（きしょくわり〜……\x01",
            "  こんなのオヤジじゃね〜……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A3")

    label("loc_535E")


    ChrTalk(
        0xFE,
        (
            "キャハハ、オヤジのやろー、\x01",
            "そろそろ酒もミラも尽きる頃じゃねHuh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A3")

    TalkEnd(0xFE)
    Return()

    # Function_23_52D1 end

    def Function_24_53A7(): pass

    label("Function_24_53A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53B8")
    Jump("loc_544A")

    label("loc_53B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_53F9")

    ChrTalk(
        0xFE,
        (
            "（Hehe\x01",
            "  酔っ払ってる方がマシだね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544A")

    label("loc_53F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5407")
    Jump("loc_544A")

    label("loc_5407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_544A")

    ChrTalk(
        0xFE,
        (
            "Hehe\x01",
            "じゃあまた適当に\x01",
            "稼いでもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544A")

    TalkEnd(0xFE)
    Return()

    # Function_24_53A7 end

    def Function_25_544E(): pass

    label("Function_25_544E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5481")
    Call(0, 31)
    Return()

    label("loc_5481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('五谷味噌', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('魔兽兽肉', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('百药精酒', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('香油', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑暗菇', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('万能青葱', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你胡萝卜', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('热辣椒', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54EF")
    Call(0, 33)
    Return()

    label("loc_54EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_57DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_END)), "loc_57DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_5586")

    ChrTalk(
        0x13,
        (
            "うん、これだけ材料があれば\x01",
            "足らなくなることはなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ほんとありがとう、\x01",
            "これでみんな喜んでくれるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DA")

    label("loc_5586")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                    # 0
            "必要な食材について聞く\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574E")

    ChrTalk(
        0x13,
        (
            "ああ、必要な食材を\x01",
            "改めて確認したいんだね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "まず『五穀味噌』を１０個。\x01",
            "それから『魔獣の獣肉』を１０個――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "次に『百薬清酒』を１０本に\x01",
            "さらに『セサミオイル』を１０本――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "で、『暗闇茸』を３０本に\x01",
            "『万能ネギ』を３０本――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "最後に『プチキャロット』を３０本。\x01",
            "『ホットペッパー』を３０個。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That should do it\x01",
            "どうかよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DA")

    label("loc_574E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57DA")

    ChrTalk(
        0x13,
        (
            "炊き出しのメニューは\x01",
            "ずばり『豚汁』ってヤツさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "肉も野菜も一緒に摂れるし、\x01",
            "栄養を付けるには\x01",
            "もってこいなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DA")

    Jump("loc_5848")

    label("loc_57DF")


    ChrTalk(
        0x13,
        (
            "う〜ん、この量じゃ\x01",
            "またあっという間に\x01",
            "なくなっちゃうよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "どうにかして\x01",
            "水増しできないかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5848")

    TalkEnd(0xFE)
    Return()

    # Function_25_544E end

    def Function_26_584C(): pass

    label("Function_26_584C")

    TalkBegin(0xFE)
    OP_4B(0x15, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5926")

    ChrTalk(
        0x15,
        (
            "いいかヴァン、それに嬢ちゃん。\x01",
            "しっかり部屋の中にいるんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "大事な一人息子とその友達だ、\x01",
            "父ちゃんが絶対守ってやるからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "（きしょくわりー……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5979")

    label("loc_5926")


    ChrTalk(
        0x15,
        (
            "いいかヴァン、それに嬢ちゃん。\x01",
            "俺が絶対守ってやるからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "（うぜー……）\x02",
    )

    CloseMessageWindow()

    label("loc_5979")

    OP_4C(0x15, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_584C end

    def Function_27_5985(): pass

    label("Function_27_5985")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599A")
    Call(0, 28)
    Jump("loc_5B42")

    label("loc_599A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A93")

    ChrTalk(
        0xF,
        (
            "#01803Fさてと、そろそろ市役所に行く\x01",
            "準備をしないと……\x02\x03",
            "#01802F皆さん、シャーリィさんについては\x01",
            "ご忠告ありがとうございました。\x02\x03",
            "#01806F私もイリアさんのスキンシップで\x01",
            "いっぱいいっぱいですけど……\x01",
            "なんとか気を付けておきますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5B42")

    label("loc_5A93")


    ChrTalk(
        0xF,
        (
            "#01802F皆さん、シャーリィさんについては\x01",
            "ご忠告ありがとうございました。\x02\x03",
            "#01806F私もイリアさんのスキンシップで\x01",
            "いっぱいいっぱいですけど……\x01",
            "なんとか気を付けておきますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B42")

    TalkEnd(0xFE)
    Return()

    # Function_27_5985 end

    def Function_28_5B46(): pass

    label("Function_28_5B46")

    EventBegin(0x0)
    Fade(500)
    OP_93(0xF, 0xB4, 0x0)
    OP_4B(0xF, 0xFF)
    OP_68(-1970, 1230, 54740, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17780, 0)
    SetChrPos(0x101, -1680, 30, 54360, 0)
    SetChrPos(0x102, -2670, 30, 54080, 0)
    SetChrPos(0x103, -620, 30, 54080, 0)
    SetChrPos(0x104, -1660, 30, 52940, 0)
    SetChrPos(0x109, -2910, 30, 52790, 0)
    SetChrPos(0x105, -330, 30, 52680, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0xF,
        "#01802Fあ、みなさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000Fやあ、リーシャ。\x01",
            "自宅に戻ってたんRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802Fはい、今日は午後から\x01",
            "市役所の方に用事があったので、\x01",
            "休みをもらってたんです。\x02\x03",
            "あUhティオちゃんも\x01",
            "ようやく戻ってきたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202Fはい、昨日付けで\x01",
            "支援課に復帰したところです。\x02\x03",
            "#00204Fアルカンシェルは昨夜、\x01",
            "各国首脳を招いたステージだったとか……\x01",
            "本当にお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100Fふふ、やっぱり緊張しましたか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809Fあはは、いつものステージとは\x01",
            "確かにちょっと違う感じでした。\x02\x03",
            "#01804F端役とはいえ、シュリちゃんも\x01",
            "初めて舞台に立つことになって\x01",
            "物凄い緊張感でしたし……\x02\x03",
            "#01802Fもっとも、イリアさんなんかは\x01",
            "いつも通りでしたけどね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309Fハハ、イリアさんは\x01",
            "緊張なんかとは無縁だろうしなあ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01804Fええ、本当に舞台のことになると\x01",
            "イリアさんはまっすぐで……\x02\x03",
            "#01802Fふふ、私なんかこれからずっと\x01",
            "敵わない気がしちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103Fうーん、アーティストの方にとっては\x01",
            "ものすごく高い目標ですよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、なんたって\x01",
            "真の天才と言われてるスターだからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000Fでも、リーシャなら絶対にいつか\x01",
            "イリアさんに追いつける気がするよ。\x02\x03",
            "#00004F昨日もシャンデリアから\x01",
            "落下した子猫をキャッチしたのは\x01",
            "かなりすごかったしな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FあHaha…That's fine, thank you\x02\x03",
            "#01802Fでも、本当にあれはとっさに\x01",
            "体が動いただけですから……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01803Fそういえば、昨日の女の子……\x01",
            "シャーリィさんでしたか。\x02\x03",
            "#01802Fランディさんの従妹だそうですけど……\x01",
            "どういった方なんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005Fえ、Uhm...\x02\x03",
            "#00003F（余計なことを言って\x01",
            "  リーシャを巻き込むワケには\x01",
            "  いかないけど……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F……ハハ、どうっつっても\x01",
            "あのまんまのお転婆娘でな。\x02\x03",
            "#00302Fただ、ちっとばかり面倒なヤツだから\x01",
            "絡まれたら上手いことかわしてくれ。\x02\x03",
            "#00309Fなんだかアイツ、リーシャちゃんを\x01",
            "気に入っちまったみたいだしな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、油断すると\x01",
            "エリィみたいな目に\x01",
            "遭っちゃうかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113Fも、もう……\x01",
            "いい加減忘れてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01808F（血染めの#9R ブラッディ#シャーリィ……）\x02\x03",
            "#01803F（もしかしたらこの先、\x01",
            "  《銀》としての私とも……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F……えっと、リーシャ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802F……ふふ、いHuh\x01",
            "ご忠告That's fine, thank you\x02\x03",
            "#01806F私もイリアさんのスキンシップで\x01",
            "いっぱいいっぱいですけど……\x01",
            "なんとか気を付けておきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10112Fあ、あHaha…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00206Fリーシャさんも苦労しますね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 4)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1680, 30, 54360, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_5B46 end

    def Function_29_65DF(): pass

    label("Function_29_65DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_660D")
    Call(0, 34)
    Return()

    label("loc_660D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6636")
    Call(0, 30)
    Return()

    label("loc_6636")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6647")
    Jump("loc_6701")

    label("loc_6647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6682")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6701")

    label("loc_6682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6690")
    Jump("loc_6701")

    label("loc_6690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_66CB")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6701")

    label("loc_66CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6701")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6701")

    TalkEnd(0xFF)
    Return()

    # Function_29_65DF end

    def Function_30_6705(): pass

    label("Function_30_6705")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3530, 1300, 3570, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 3800, 0, 3500, 90)
    SetChrPos(0x102, 3500, 0, 4800, 90)
    SetChrPos(0x109, 2800, 0, 3200, 90)
    SetChrPos(0x105, 2300, 0, 4500, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000F旧市街・ロータスハイツ……\x01",
            "うん、ここで合ってるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000Fすみません、\x01",
            "誰かいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x109,
        "#6P#10103FNo answer huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FIs it locked?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00001FIyeah it's bolted tight\x02\x03",
            "#00003F少し気配を感じた気がするんだけど、\x01",
            "気のせいだったかAh…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FR-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FMaybe it's for protection\x02\x03",
            "#10300Fそういう場合はどうする。\x01",
            "無理にでも開けて踏み込むかい？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003Fああ、他に手がなかったら\x01",
            "最悪それも考えられるけど……\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 50, 0)
    Sound(857, 0, 80, 0)
    Sleep(200)
    Sound(856, 0, 30, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x5DC)

    ChrTalk(
        0x109,
        "#6P#10105F今のは.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FSounded like the sound of a plate breaking…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103Fどうやら、居留守の\x01",
            "可能性はかなり高Yeah I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FLet's call out again\x02\x03",
            "#00001Fすみません!\x01",
            "いらっしゃいますよね!?\x02\x03",
            "Can you please say something!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x105,
        (
            "#6P#10304FThis is really something else\x02\x03",
            "#10302Fもしくは、窓から\x01",
            "逃げてたりなんかして。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006Fう〜ん、そうなると\x01",
            "ちょっと厄介Right.\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(1000)
    OP_68(3720, 1000, 2530, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16200, 3000)
    SetChrPos(0x8, 8000, 0, -3500, 0)
    SetChrPos(0x9, 8000, 0, -2500, 0)

    def lambda_6CC8():
        OP_95(0x9, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6CC8)
    Sleep(100)

    def lambda_6CE5():
        OP_95(0x8, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6CE5)
    Sleep(100)
    WaitChrThread(0x9, 1)

    def lambda_6D06():
        OP_95(0x9, 3060, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D06)
    Sleep(100)
    WaitChrThread(0x8, 1)

    def lambda_6D27():
        OP_95(0x8, 4059, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6D27)
    WaitChrThread(0x9, 1)

    def lambda_6D45():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D45)
    WaitChrThread(0x8, 1)
    Sleep(100)

    def lambda_6D59():
        OP_93(0x8, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6D59)
    WaitChrThread(0x8, 1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#12Pさっきから何やら騒がしいが……\x01",
            "あんたらの仕業かね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PWhat's going on there?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6E25():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E25)
    Sleep(10)

    def lambda_6E35():
        OP_93(0x102, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E35)
    Sleep(10)

    def lambda_6E45():
        OP_93(0x109, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E45)
    Sleep(10)

    def lambda_6E55():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E55)
    Sleep(10)

    ChrTalk(
        0x101,
        (
            "#5P#00005FOh right, excuse us\x02\x03",
            "#00000F自分たちはクロスベル警察の\x01",
            "特務支援課なんですが……\x02\x03",
            "#00003Fちょっと、この部屋の\x01",
            "住民の方に用事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105Fその、お２人は、\x01",
            "この部屋の方をご存知ですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12Pああ、もちろん\x01",
            "知ってはおるんじゃが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x0)

    ChrTalk(
        0x9,
        (
            "#12Pふむ、事情を\x01",
            "聞かせてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FActually\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは不審住戸の\x01",
            "調査について説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#12Pなるほどのう……\x01",
            "それで居住者を確認する\x01",
            "必要があるわけか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pう〜ん、何というか\x01",
            "申し訳ないことをしたね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105Fえ、それはどういう.......?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x0)

    ChrTalk(
        0x9,
        (
            "#12Pああ、というのも何を隠そう\x01",
            "私が以前この部屋に住んでいた\x01",
            "ガイトナーなんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FI-is that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pああ、そういうわけで\x01",
            "私が転出届けを出さなきゃ\x01",
            "いけなかったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PAnd now it's late I'm sure\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P分かった、届書の方は\x01",
            "今日の内に必ず出させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100Fええ、そうして頂けると\x01",
            "こちらも助かります。\x02\x03",
            "#00103Fちなみに転出の事情について\x01",
            "お聞きしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pああ、一言で言うと、\x01",
            "これも“縁”というヤツでね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pそもそも私は、１年ほど前に\x01",
            "商人として大きな失敗をして\x01",
            "このアパートにやって来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P私の事情を知った昔の商売仲間が\x01",
            "一緒に商売をやろうって\x01",
            "声を掛けてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pそれで、つい２週間ほど前に\x01",
            "その仲間がいる共和国に\x01",
            "移り住んだ所だったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FSo you're still here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12Pああ、このアパートでお世話になった\x01",
            "皆さんに改めてお礼を言いに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P皆さんには\x01",
            "本当に良くしてもらったからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12POf course, it wasn't a big deal\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004Fなるほど、ガイトナーさんの\x01",
            "事情は概ね分かりました。\x02\x03",
            "#00000Fでは改めて今の居住者について\x01",
            "お聞きしたいんですが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PYes that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105F……何か、仰りにくい\x01",
            "事情でもあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12Pいや、まあ本人の\x01",
            "心の問題だとは思うんじゃが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHmm…\x02",
    )

    CloseMessageWindow()

    def lambda_75ED():
        OP_9B(0x1, 0x8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_75ED)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_7609():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7609)
    Sleep(50)

    def lambda_7621():
        OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7621)
    Sleep(50)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_7640():
        OP_9B(0x1, 0x109, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7640)
    Sleep(50)

    def lambda_7658():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7658)
    Sleep(50)
    OP_93(0x9, 0x2D, 0x0)
    WaitChrThread(0x8, 1)
    OP_9B(0x0, 0x8, 0x5A, 0x3E8, 0x3E8, 0x0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#6Pタントスじゃが……\x01",
            "お前さん、いるんじゃろう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P話を聞いていたなら\x01",
            "ここを開けてくれんかの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6Pここにいるのは警察の方じゃ。\x01",
            "名前が知れたからと言って、\x01",
            "何も起こったりしやせんわい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    Sound(806, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6POk we're opening up\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5Pでは、あまり騒ぎにならん内に\x01",
            "確認してもらえますかのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, please cooperate\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(52110, 1430, -1830, 0)
    MoveCamera(73, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    SetChrPos(0xA, 55000, 30, -2100, 90)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x101, 48300, 30, 100, 90)
    SetChrPos(0x102, 48300, 30, 100, 90)
    SetChrPos(0x109, 48300, 30, 100, 90)
    SetChrPos(0x105, 48300, 30, 100, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_7937():
        OP_95(0x101, 51800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7937)

    def lambda_7951():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7951)
    Sleep(500)

    def lambda_7965():
        OP_95(0x102, 51800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7965)

    def lambda_797F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_797F)
    Sleep(500)

    def lambda_7993():
        OP_95(0x109, 50800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7993)

    def lambda_79AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_79AD)
    Sleep(500)

    def lambda_79C1():
        OP_95(0x105, 50800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79C1)

    def lambda_79DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_79DB)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_79F3():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79F3)
    WaitChrThread(0x102, 1)

    def lambda_7A04():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A04)
    WaitChrThread(0x109, 1)

    def lambda_7A15():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A15)
    WaitChrThread(0x105, 1)

    def lambda_7A26():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A26)

    ChrTalk(
        0x101,
        "#6P#00000FExcuse me…\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        "#11PAre you here to laugh at me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FUh…？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    NpcTalk(
        0xA,
        "???",
        (
            "#11Pわしを笑いに来たのかと\x01",
            "言っとるんだ!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        (
            "#11P議員時代の栄光に囚われながら\x01",
            "今やすっかり落ちぶれてしまった\x01",
            "このゲバルを!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FT-this guy is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FRepresentative Guevara of the Sentate…\x02\x03",
            "#00101F過去に不正が発覚して以来、\x01",
            "ずっとウルスラ病院に\x01",
            "入院していたんじゃなかったかしら……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pふ、ふん、やはり\x01",
            "わしを知っておったか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pわしの居場所を突き止めて\x01",
            "一体何のつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI don't have any money, as you can see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pこのアパートの家賃にしても、\x01",
            "古い知人のつてを辿りに辿って\x01",
            "何とか工面した所だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pはっ、まさか、\x01",
            "そんなわしのか細い人脈すらも\x01",
            "利用しようという腹なのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#00106Fいえ、そんなつもりは\x01",
            "毛頭ありませんから。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F自分たちは、\x01",
            "あなたのことをこの目で\x01",
            "確認したかっただけです。\x02\x03",
            "#00003Fえっと、ゲバルさん。\x01",
            "貴方がここの新たな居住者で\x01",
            "間違いありませんね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11Pあ、あAh...その通りだ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThen that's all we need to know\x02\x03",
            "#10100F犯罪に利用されていた\x01",
            "わけではなくて一安心True.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303Fでもどうして届書に\x01",
            "童話の作者の名前なんか\x01",
            "書いたんだろうねぇ。\x02\x03",
            "#10300F不審すぎて、逆に\x01",
            "足がついちゃうと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F確かに、この住戸が一番\x01",
            "見るからに怪しかったからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pわしは昔からショーン・\x01",
            "アルナムの大ファンなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pとっさに思いついた\x01",
            "名前がそれだったんだから\x01",
            "仕方ないだろう!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10112Fえ、Uhm...\x01",
            "ちょっと意外True.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103Fま、まあ色んな世代に\x01",
            "読まれている作家ではあるし……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、これもいわゆる\x01",
            "ギャップ萌えってヤツかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005Fそ、そうなのか.......?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11POh shut up shut up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P貴様ら用事は済んだのだろう!\x01",
            "だったら、さっさと出て行くがいい!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FR-right, excuse us\x02\x03",
            "#00100Fそれじゃロイド、\x01",
            "そろそろ行きましょうか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes.\x02\x03",
            "Well then excuse me\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1400", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_6705 end

    def Function_31_82FA(): pass

    label("Function_31_82FA")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1320, -56500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2600, 20, -55850, 90)
    SetChrPos(0x105, 2600, 20, -57050, 90)
    SetChrPos(0x104, 1400, 20, -56100, 90)
    SetChrPos(0x103, 1100, 20, -57150, 90)
    SetChrPos(0x102, 2790, 20, -54460, 135)
    SetChrPos(0x109, -90, 20, -56800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FYo, Azel\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x13,
        "Oh Wazy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "もしかして、\x01",
            "手伝いに来てくれたのかい？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FYeah, that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fここでは、炊き出しの\x01",
            "準備をしているんRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIs there anything we can do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "ああ、Yeah…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Uhm...\x01",
            "実は炊き出しの材料が\x01",
            "かなり不足していてね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "できれば、買い出しを\x01",
            "お願いしたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F買い出しねぇ。\x01",
            "ま、お安い御用ってとこか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205Fちなみに、何がどれだけ\x01",
            "必要なんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ああ、今から言うから\x01",
            "覚えていてくれるかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "まず『五穀味噌』を１０個。\x01",
            "それから『魔獣の獣肉』を１０個――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "次に『百薬清酒』を１０本に\x01",
            "さらに『セサミオイル』を１０本――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "で、『暗闇茸』を３０本に\x01",
            "『万能ネギ』を３０本――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "最後に『プチキャロット』を３０本。\x01",
            "『ホットペッパー』を３０個。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "That should do it\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x109,
        "#10106FI know it's a rediculous amount of stuff\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ああ、それだけみんな\x01",
            "よく食べるからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "実は昨日は、十分に行き届かなくて\x01",
            "ちょっとした騒ぎになったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "だから今日は、そんなことが\x01",
            "ないようにしたくってさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI-I see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300Fちなみに、\x01",
            "一体何の料理なんだい？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ああ、身も心も温まる――\x01",
            "『豚汁』ってヤツさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "完成したら当然みんなにも\x01",
            "振舞わさせてもらうからね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FEheh, I'll look forward to that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "そうそう、それと買い出しの\x01",
            "代金を渡しておかないと。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００ミラ\x07\x00",
            "Got FORCE from Dudley\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    AddMira(500)

    ChrTalk(
        0x104,
        (
            "#00306Fいや、なんつうか……\x01",
            "どう考えても足りねえだろ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "う〜ん、ごめん。\x01",
            "何しろ予算がカツカツでさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "僕たちを助けるつもりで\x01",
            "何とかそれでお願いしたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100Fまあ、足りない分は\x01",
            "あたしたちの寄付ってことで。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203Fええ、状況も状況ですし、\x01",
            "このくらいは協力すべきかと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10300Fフフ、そうと決まれば\x01",
            "善は急げだね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00000Fああ、さっそく\x01",
            "買い出しに向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 1)
    OP_29(0x8E, 0x1, 0x2)
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2600, 20, -56450, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_82FA end

    def Function_32_8B84(): pass

    label("Function_32_8B84")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E2A")

    ChrTalk(
        0x8,
        (
            "ふむ、お前さんたち。\x01",
            "炊き出しの材料調達を\x01",
            "手伝ってくれるそうじゃの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いやありがたい。\x01",
            "すまぬがよろしく頼むぞい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "おおそうじゃ――\x01",
            "よければそのことで１つ\x01",
            "頼みたいことがあっての。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "にがトマトの成分が\x01",
            "凝縮されたエキス……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "それをどこかで\x01",
            "手に入れることができれば\x01",
            "持ってきて欲しいんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "そうすれば、わし特製の\x01",
            "『強壮にがトマ豚汁』を\x01",
            "振舞うことが出来るんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fエキスって……\x01",
            "『にがトマト』そのものじゃ\x01",
            "ダメなんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ああ、それだと調理に恐ろしく\x01",
            "時間がかかってしまうんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "まあ、余裕があればでいいんじゃ。\x01",
            "なくても困るものではないからの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fええ、覚えておきますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 2)
    OP_29(0x8E, 0x1, 0x3)
    Jump("loc_8F57")

    label("loc_8E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_8EB9")

    ChrTalk(
        0xFE,
        (
            "お、どうやらわしの注文の品を\x01",
            "持ってきてくれたようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh that's wonderful\x01",
            "これでみんなに\x01",
            "元気を注入してやれるぞい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F57")

    label("loc_8EB9")


    ChrTalk(
        0x8,
        (
            "にがトマトの成分が\x01",
            "凝縮されたエキス……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "それをどこかで\x01",
            "手に入れることができれば\x01",
            "持ってきて欲しいんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "まあ、余裕が\x01",
            "あればでいいんじゃがの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F57")

    TalkEnd(0x8)
    Return()

    # Function_32_8B84 end

    def Function_33_8F5B(): pass

    label("Function_33_8F5B")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1320, -56500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2600, 20, -55850, 90)
    SetChrPos(0x105, 2600, 20, -57050, 90)
    SetChrPos(0x104, 1400, 20, -56100, 90)
    SetChrPos(0x103, 1100, 20, -57150, 90)
    SetChrPos(0x102, 2790, 20, -54460, 135)
    SetChrPos(0x109, -90, 20, -56800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    TurnDirection(0x13, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "あ、食材を\x01",
            "調達してきてくれたんだね？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Choice 1: Hand everything over\x01",      # 0
            "やめておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_910F")

    ChrTalk(
        0x13,
        (
            "ああ、もしかして\x01",
            "まだ揃っていなかった？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "それじゃ、準備ができたら\x01",
            "また声を掛けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    label("loc_910F")


    ChrTalk(
        0x101,
        "#00000FYes, here you go\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#20I五穀味噌　　　\x07\x00",
            "×１０\x01\x07\x02",
            "#20I魔獣の獣肉　　\x07\x00",
            "×１０\x01\x07\x02",
            "#20I百薬清酒　　　\x07\x00",
            "×１０\x01\x07\x02",
            "#20Iセサミオイル　\x07\x00",
            "×１０\x01\x07\x02",
            "#20I暗闇茸　　　　\x07\x00",
            "×３０\x01\x07\x02",
            "#20I万能ネギ　　　\x07\x00",
            "×３０\x01\x07\x02",
            "#20Iプチキャロット\x07\x00",
            "×３０\x01\x07\x02",
            "#20Iホットペッパー\x07\x00",
            "×３０　Handed over Bitter Tomato Paste\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    SubItemNumber('五谷味噌', 10)
    SubItemNumber('魔兽兽肉', 10)
    SubItemNumber('百药精酒', 10)
    SubItemNumber('香油', 10)
    SubItemNumber('黑暗菇', 30)
    SubItemNumber('万能青葱', 30)
    SubItemNumber('迷你胡萝卜', 30)
    SubItemNumber('热辣椒', 30)

    ChrTalk(
        0x13,
        "Yep this is everything\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "よく調達して来てくれたね。\x01",
            "どうもありがとう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦西红柿酱', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94D6")
    OP_2C(0x8E, 0x1)

    ChrTalk(
        0x103,
        (
            "#00205FそういえばLloyd…\x01",
            "あれも渡した方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FOh right Lloyd, can you pass that over too?\x02\x03",
            "#00000FWe went to get this too\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿酱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over Bitter Tomato Paste\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('苦西红柿酱', 1)

    ChrTalk(
        0x13,
        "This is..？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304Fフフ、タントスさんから\x01",
            "調達を頼まれた品でね。\x02\x03",
            "#10302F何でもスペシャルな豚汁が\x01",
            "出来るって聞いたけど？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ああ、その話か。\x01",
            "確かに本人も言ってたな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "うん、じゃあこれは\x01",
            "タントスさんに聞いて\x01",
            "ぜひ使ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 4)

    label("loc_94D6")


    ChrTalk(
        0x104,
        (
            "#00300Fそんじゃま、これで\x01",
            "手伝い終了ってことで構わねえか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "ああ、お疲れ様。\x01",
            "おかげで助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "作業が一区切り付いたら\x01",
            "炊き出しを開始するからさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "支援課のみんなも\x01",
            "ぜひ参加していってくれ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWe're looking forward to it\x02",
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9656")

    ChrTalk(
        0x101,
        (
            "#00004Fま、あとは任せて\x01",
            "大丈夫Yeah we should\x02\x03",
            "#00000F一通り手伝いもすんだし、\x01",
            "アッバスに報告にいくか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_96AE")

    label("loc_9656")


    ChrTalk(
        0x101,
        (
            "#00004Fま、あとは任せて\x01",
            "大丈夫Yeah we should\x02\x03",
            "#00000F俺たちは他の場所を\x01",
            "回るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96AE")

    SetScenarioFlags(0x196, 3)
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2600, 20, -56450, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_8F5B end

    def Function_34_96E8(): pass

    label("Function_34_96E8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4030, 1300, 3430, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 4790, 0, 4019, 90)
    SetChrPos(0x102, 3300, 0, 4710, 90)
    SetChrPos(0x103, 2990, 0, 3570, 90)
    SetChrPos(0x104, 1690, 0, 5630, 90)
    SetChrPos(0x109, 1230, 0, 4280, 90)
    SetChrPos(0x105, 1640, 0, 3020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000Fすみません、ゲバルさん。\x01",
            "いらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        "#00003F……留守にしてるみたいRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fここがゲバルさんの部屋に\x01",
            "間違いないはずBut…\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3910, 1300, 1040, 3000)
    SetChrPos(0x8, 8000, 0, -3500, 0)
    OP_4B(0x8, 0xFF)
    OP_95(0x8, 8000, 0, 0, 2000, 0x0)
    OP_95(0x8, 4059, 0, 0, 2000, 0x0)
    OP_93(0x8, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        (
            "お前さんたち、\x01",
            "何をしとるのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_99F5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99F5)
    Sleep(50)

    def lambda_9A05():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A05)
    Sleep(50)

    def lambda_9A15():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A15)
    Sleep(50)

    def lambda_9A25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A25)
    Sleep(50)

    def lambda_9A35():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A35)
    Sleep(50)

    def lambda_9A45():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A45)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "おや、いつぞやの……\x01",
            "確か特務支援課だったか。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3630, 1300, 2880, 2000)
    OP_95(0x8, 3800, 0, 1500, 1500, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        (
            "#10302FHah\x01",
            "こんにちは、タントスさん。\x02\x03",
            "こちらに住んでいた\x01",
            "元議員のおじさんは\x01",
            "どこに行っているのかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ふむ、彼なら先週あたりから\x01",
            "どこぞに出かけとるようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is there some kind of case?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell actually\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはアルムの依頼で\x01",
            "ゲバルを捜索している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "おお、はるばるリベールから来た\x01",
            "例の息子夫婦か……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ほほ、ゲバル殿も\x01",
            "なかなかに果報者じゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205Fお爺さんもアルムさんの事を\x01",
            "ご存知なんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "つい先週、アパートを\x01",
            "訪ねてきたのでな。\x01",
            "色々と話させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ふむ、しかしその直前あたりから、\x01",
            "ゲバル殿はどこかに\x01",
            "出かけてしまったようでな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "行き先も聞いておらんし\x01",
            "どこに行ったやら……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FUgh! Not a single clue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FThat's a problem\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hmm, but that reminds me\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "もしかすると、ゲバル殿の\x01",
            "行方を知っている者が\x01",
            "いるかもしれんぞい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F本当ですか……!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "うむ、確か西通りの方に\x01",
            "彼が議員時代に世話になっておった\x01",
            "人物がおるらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "こちらに引っ越してくる時も、\x01",
            "色々と面倒を見てもらったそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "確か、ヴィ、ヴィラ……\x01",
            "ヴィラなんとか、などという名前の\x01",
            "建物に住んでおるらしいぞい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203Fヴィラなんとか……\x01",
            "なんだか聞き覚えのあるような\x01",
            "語感True.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003Fとにかく、西通りの建物を\x01",
            "探してみるとしようか。\x02\x03",
            "#00000Fおじいさん、\x01",
            "Thanks for your help\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No no not at all\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ゲバル殿と息子夫婦たちを、\x01",
            "なんとか引き合わせてやっておくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x90, 0x1, 0x1)
    SetScenarioFlags(0x19A, 7)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1030, 0, 1180, 225)
    SetChrPos(0x8, 3800, 0, 1500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_34_96E8 end

    SaveToFile()

Try(main)
