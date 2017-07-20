from ScenarioHelper import *

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
        "Tantos old man",           # 1
        "Geitner",             # 2
        "Gabal",                 # 3
        "corona",                 # 4
        "Lima",                   # 5
        "Marsun",               # 6
        "Trainee Misho",         # 7
        "Lisha",               # 8
        "Paola Lady",           # 9
        "Van",                 # 10
        "Ruze",                   # 11
        "Azel",                 # 12
        "Voice of a man",                 # 13
        "Bacchus",               # 14
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
            "When Gevar is a member of the Diet\x01",
            "The person who was taken care of,\x01",
            "It seems to be in the direction of Nishi-dori.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, Vi, Villa ……\x01",
            "Named as \"Villa somehow\"\x01",
            "She seems to live in a building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that person gets the whereabouts of Guerbal\x01",
            "Maybe you know.\x02",
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
            "The bad groups'\x01",
            "Cooperate with the old city\x01",
            "You guarded me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Previously there were lots of fighting in the plaza\x01",
            "It was a hard-to-access existence,\x01",
            "Again young people can depend on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come here and finally the old town\x01",
            "I feel like I'm starting to become one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D9F")

    label("loc_D08")


    ChrTalk(
        0xFE,
        (
            "The bad groups'\x01",
            "It protects the old city.\x01",
            "Again young people can depend on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come here and finally the old town\x01",
            "I feel like I'm starting to become one.\x02",
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
            "The blue moya that is out\x01",
            "What on earth are you ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway the inhabitants of the apartment\x01",
            "In order not to go outside,\x01",
            "Please be careful.\x02",
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
            "Presidential speech is\x01",
            "I also had you hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly you understand the claim … …\x01",
            "Peaceful solution\x01",
            "Was not it really there …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F32")

    label("loc_ECD")


    ChrTalk(
        0xFE,
        "Certainly you know the president's claim … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Peaceful solution\x01",
            "Was not it really there …?\x02",
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
            "If the vegetables are sufficiently heated\x01",
            "Start of seasoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"Tomatoba juice is tonic\" … …\x01",
            "Please wait looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1031")

    label("loc_FCC")


    ChrTalk(
        0x8,
        (
            "Well, it's time for cooking\x01",
            "Carefully prepared vessels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You ought to go over to everyone today … …\x02",
    )

    CloseMessageWindow()

    label("loc_1031")

    Jump("loc_10BC")

    label("loc_1036")


    ChrTalk(
        0x8,
        (
            "To prepare for cooking,\x01",
            "In this room and Corona's room\x01",
            "I'm going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everything is in terms of quantity.\x01",
            "No matter how many kitchens you have\x01",
            "I am lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BC")

    Jump("loc_113E")

    label("loc_10C1")


    ChrTalk(
        0xFE,
        (
            "Ho ho everyone, pork soup\x01",
            "I like to eat deliciously\x01",
            "More than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To you guys\x01",
            "I have to thank you.\x02",
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
            "Yesterday evening,\x01",
            "Unusually at the place of Guerbal\x01",
            "There was a visitor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And then,\x01",
            "The state of Gabaru is strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone is being chased by\x01",
            "I told him … …\x01",
            "Hmm, I am a bit worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1265")

    label("loc_121D")


    ChrTalk(
        0xFE,
        (
            "Someone is being chased by\x01",
            "I told him … …\x01",
            "Hmm, I am a bit worried.\x02",
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
            "Apparently Gabal also\x01",
            "To live here\x01",
            "It seems to be familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, that's fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1413")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1384")

    ChrTalk(
        0xFE,
        (
            "Paku Paku ……\x01",
            "Gabal's cooked beans, it is really superb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho, until dinner\x01",
            "I intended to take it,\x01",
            "It seems that it will be gone soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_140E")

    label("loc_1384")


    ChrTalk(
        0xFE,
        (
            "However, Gabal also gradually\x01",
            "It seems like I am opening my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that it was proud that the legislature era,\x01",
            "Apparently the heart is gentle.\x02",
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
            "Crossbell to the state, … ….\x01",
            "Although it is a very legitimate claim,\x01",
            "I feel I am too greedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "2 great countries also have a good face\x01",
            "It seems to be doing it,\x01",
            "I do not think that things go peacefully … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, Mayor Dieter also\x01",
            "I will propose bold things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15A8")

    label("loc_152A")


    ChrTalk(
        0xFE,
        (
            "Crossbell to the nation,?\x01",
            "I do not think that things go peacefully … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, Mayor Dieter also\x01",
            "I will propose bold things.\x02",
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
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly there is such a thing\x01",
            "Even if I lose the temptation\x01",
            "I do not think it is strange.\x02",
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
            "In the unveiling ceremony …… in the town\x01",
            "It seems to be a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that new city hall building,\x01",
            "Probably the prosperity of this crossbell\x01",
            "It seems as if it shows … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that shadow, like ours\x01",
            "There are people who live in a modest way\x01",
            "I do not want you to forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17BF")

    label("loc_1741")


    ChrTalk(
        0xFE,
        (
            "However, Gabaru remains as usual\x01",
            "It seems to be occupying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which, even calling it in the room\x01",
            "Do you mean to ask even bitches?\x02",
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
            "From tomorrow I have a trade meeting\x01",
            "A patrol officer also in this old city\x01",
            "You seem to be coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, these sad memories are\x01",
            "Even if you make a mistake, the leaders will come\x01",
            "It's not a place.\x02",
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
            "Hmm, Geithner you\x01",
            "Looks fine and more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am also really happy.\x02",
    )

    CloseMessageWindow()

    label("loc_18E8")

    Jump("loc_1976")

    label("loc_18ED")


    ChrTalk(
        0xFE,
        (
            "You guys,\x01",
            "Please remember that\x01",
            "Do you leave me alone and doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He also has various things, quite\x01",
            "I do not feel like taking a rest.\x02",
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
            "As you can see this old city,\x01",
            "From city planning\x01",
            "The place left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The security is bad but the rent is cheap,\x01",
            "Those who had any circumstances\x01",
            "They come together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand,\x01",
            "After having nested here\x01",
            "Some also have success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry, in this place\x01",
            "There are truly various life patterns\x01",
            "It's packed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B60")

    label("loc_1ABC")


    ChrTalk(
        0xFE,
        (
            "All circumstances in this old city\x01",
            "Those who came gathered,\x01",
            "Some also go nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry, in this place\x01",
            "There are truly various life patterns\x01",
            "It's packed.\x02",
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
            "Mogmog …\x01",
            "This is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This boiled bean is Gabaru … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, after a long time\x01",
            "When you try cooking\x01",
            "You made too much luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tentatively, in your mouth\x01",
            "I felt relieved like it was fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not mind bothering you.\x01",
            "It is truly appreciated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D22")

    label("loc_1C7F")


    ChrTalk(
        0x8,
        (
            "Hmm, if I still have it\x01",
            "Take it to other people\x01",
            "How about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is this, surely\x01",
            "Everyone will be pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Is that right, is not it?\x02",
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
        "Listen, Tantos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am full of hope for this\x01",
            "There is something called a new era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Holds up, I heard it many times\x01",
            "I know that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You, this town to you\x01",
            "You thought you'd change it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, that's right.\x01",
            "I was filled with ambition at that time,\x01",
            "He was elected as a parliament independent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, one day,\x01",
            "A certain imperialist member to me ……\x02",
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
            "Ou, Geithner.\x01",
            "Looks fine and more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So how about business people?\x01",
            "Are you going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, thanks in advance\x01",
            "I am letting you do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, today as a souvenir\x01",
            "I had a confectionery fold.\x01",
            "Please feel free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, this is appreciated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just put some tea\x01",
            "I suppose I should get it.\x02",
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
            "Have you guided by the guild,\x01",
            "To Alm, who is in Ribeel,\x01",
            "I was able to talk in international communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Libert is also confused,\x01",
            "It seems to be peaceful compared to the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell confusion\x01",
            "It seems that it will continue for a while … …\x01",
            "It was really nice to hear your voice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2195")

    label("loc_2100")


    ChrTalk(
        0xFE,
        (
            "To Alm, who is in Ribeel,\x01",
            "I was able to talk in international communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell confusion\x01",
            "It seems that it will continue for a while … …\x01",
            "This seems to be going to work hard.\x02",
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
            "If you think that the president was detained,\x01",
            "It appeared to such a big tree that such body might be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At least for a moment, if there is any hope\x01",
            "Even though we can overcome this situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O goddess, please rescue me ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22D9")

    label("loc_2268")


    ChrTalk(
        0xFE,
        (
            "At least for a moment, if there is any hope\x01",
            "Even though we can overcome this situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O goddess, please rescue me ……\x02",
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
        "I am worried about the existence of this town, though ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alm's family in Libert\x01",
            "Is not it okay …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sons are my hopes,\x01",
            "I can not get in touch … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2417")

    label("loc_2399")


    ChrTalk(
        0xFE,
        (
            "Since the Declaration of Independence, contact with foreign countries\x01",
            "It ceased to exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The alms are my hope,\x01",
            "I can not get in touch … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2417")

    Jump("loc_248E")

    label("loc_241C")


    ChrTalk(
        0xFE,
        "A monster that came out to the city is one piece ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To this old town\x01",
            "I do not seem to be entering,\x01",
            "I wonder if it is really okay! Is it?\x02",
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
            "Hi, I have heard a speech on east street,\x01",
            "I doubt the honest ears ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of whether or not you speak,\x01",
            "Now the two major powers are silent\x01",
            "Is not it supposed to be possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way,\x01",
            "Anything outside the autonomous province\x01",
            "It might be prudent to get out … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26CD")

    label("loc_258B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2649")

    ChrTalk(
        0xFE,
        "There are Alm in Libert … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Funfu …… Wagashi\x01",
            "We are thinking about what is convenient for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I rot, I am a crossbell … …\x01",
            "No matter what happens, I will stay here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_26CD")

    label("loc_2649")


    ChrTalk(
        0xFE,
        (
            "Absolutely … what do I do\x01",
            "We are thinking about what is convenient for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I rot, I am a crossbell … …\x01",
            "No matter what happens, I will stay here.\x02",
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
            "Hi, I have heard a speech on east street,\x01",
            "I doubt the honest ears ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of whether or not you speak,\x01",
            "Now the two major powers are silent\x01",
            "Is not it supposed to be possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way,\x01",
            "Anything outside the autonomous province\x01",
            "It might be prudent to get out … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_285C")

    label("loc_27B5")


    ChrTalk(
        0xFE,
        (
            "…… Hun, what stupid thing is that for me.\x01",
            "Abandon autonomous state nowadays\x01",
            "That's what it got when you ran away to others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I rot, I am a crossbell … …\x01",
            "No matter what happens, I will stay here.\x02",
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
            "It is not a joke …\x01",
            "You must hide yourself soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "Where shall we go ……\x02",
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
            "Hmm, Mayor Dieter also\x01",
            "It was what I did daringly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway ….\x01",
            "With this, even more empire and republican\x01",
            "The position is to get worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……, I am united\x01",
            "From what point of view is talking about politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is almost time for serious\x01",
            "Think about how to shake your future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A66")

    label("loc_2A24")


    ChrTalk(
        0xFE,
        (
            "Second life ……\x01",
            "For me,\x01",
            "I wonder what is left behind.\x02",
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
            "I do not know that\x01",
            "Things that make excuses\x01",
            "We know it seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at that time anyway\x01",
            "It's a young man who knows neither right nor left … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B07")

    Jump("loc_2CC3")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B77")

    ChrTalk(
        0xFE,
        "Nuwa ~, it's a VIP visit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, this guy as well\x01",
            "Float in a festive mood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_2B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C16")

    ChrTalk(
        0xFE,
        "Huh … … what is a trade meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well,\x01",
            "If you are not interested in Congress\x01",
            "Even politics is not interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You should do whatever you want.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C5A")

    label("loc_2C16")


    ChrTalk(
        0xFE,
        "Huh … … what is a trade meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You should do whatever you want.\x02",
    )

    CloseMessageWindow()

    label("loc_2C5A")

    Jump("loc_2CC3")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CBA")

    ChrTalk(
        0xFE,
        "Well, there is still something for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without use,\x01",
            "Go out quickly!\x02",
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
            "Um, this is cookie\x01",
            "I baked it,\x01",
            "I thought it would be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe.\x01",
            "Mama's handmade cookie,\x01",
            "It's delicious!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "Sorry, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As if by that,\x01",
            "To get a reward … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, what is fine\x01",
            "Please do not mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the same way\x01",
            "I just made extra\x01",
            "Because it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Is that so, but … ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBC")

    label("loc_2E51")


    ChrTalk(
        0xA,
        (
            "Crispy …\x01",
            "Well, this is good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hey, is not it? ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hehe, I was glad that you could have it.\x02",
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
            "Mama, this bean,\x01",
            "Very tasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, if you remember\x01",
            "I really liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mr. Gebal, really\x01",
            "May I please you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For any one alone\x01",
            "Because I could not eat it,\x01",
            "Please do not hesitate to ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thanks, my uncle!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30CC")

    label("loc_3026")


    ChrTalk(
        0xC,
        (
            "It's awful.\x01",
            "Well, good taste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Alright if it's already over.\x01",
            "You should not eat the knob.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, to your child\x01",
            "I can not help being so pleased\x01",
            "Thankfully.\x02",
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
        "Well, after all it is hard to get through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, let's get along here\x01",
            "There are also many people who receive it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Quite\x01",
            "I do not feel like going out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_324C")

    label("loc_31CD")


    ChrTalk(
        0xFE,
        (
            "It is hard to get through,\x01",
            "Let me get along with this apartment\x01",
            "There are also many people who receive it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Quite\x01",
            "I do not feel like going out.\x02",
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
            "Um, Orientation\x01",
            "The material that I got sometimes … and …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, I have not entered the school yet\x01",
            "You can think of something behind forgetful things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33D0")

    label("loc_3334")


    ChrTalk(
        0xFE,
        (
            "Huhu, but I\x01",
            "To Ursula Medical College\x01",
            "It really came true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on than taking an exam\x01",
            "It's hard to tell you … but a little more\x01",
            "You can immerse yourself in the reverberation of passing.\x02",
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
            "Looking at that big pale tree,\x01",
            "It makes me feel uneasy by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband who works outside\x01",
            "It will be the same feeling … ….\x01",
            "I want to support you somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_34FB")

    ChrTalk(
        0xFE,
        (
            "It was said to be martial law,\x01",
            "No way it will happen so far …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… The hands of cooking also tremble.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F59")

    label("loc_34FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35AB")

    ChrTalk(
        0xFE,
        (
            "From Tantos to talk about the speech\x01",
            "Did you ask ……\x01",
            "Honestly I am full of anxious feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband also ordinary today\x01",
            "I went to work, but ……\x01",
            "I want him to come home as soon as possible.\x02",
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
            "Because the fire is hard to pass through your radish\x01",
            "Put a hidden kitchen knife, … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_366B")

    label("loc_35FF")

    OP_4B(0x10, 0x0)

    ChrTalk(
        0xB,
        (
            "Well, next\x01",
            "Evening cooked menu\x01",
            "You have to decide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "That's right, what should I do?\x02",
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
            "A horrible incident on Mainz\x01",
            "That seems to be happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even now the guards people\x01",
            "It seems to be fighting … ….\x01",
            "I want you to solve it as soon as possible.\x02",
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
            "My husband also at the new site\x01",
            "I started work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyday for families every day\x01",
            "Work hard and work ……\x01",
            "I do not have any words of gratitude.\x02",
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
            "I heard from my husband before this … …\x01",
            "Construction of the Orkis Tower\x01",
            "Many foreign construction companies were also involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By whatever floor\x01",
            "The share is completely decided … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband\x01",
            "On the upper floor of the VIP floor and the international conference hall\x01",
            "I heard he was engaged in construction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of the International Conference Hall,\x01",
            "The other day commerce meeting\x01",
            "Where exactly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, my husband\x01",
            "When I think that it is the place where I worked,\x01",
            "Somehow I will be pleased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_39F0")

    label("loc_395C")


    ChrTalk(
        0xFE,
        (
            "Speaking of the International Conference Hall,\x01",
            "The other day commerce meeting\x01",
            "Where exactly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, my husband\x01",
            "When I think that it is the place where I worked,\x01",
            "Somehow I will be pleased.\x02",
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
            "I got it from Mr. Lisha before.\x01",
            "It is the place where green tea is brewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, this tea leaf,\x01",
            "It smells very nice.\x02",
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
            "Orkis Tower also\x01",
            "Only to leave the unveiling ceremony … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, thanks,\x01",
            "My master's job also\x01",
            "It calms down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow, my master's job\x01",
            "You have to burn your eyes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BA4")

    label("loc_3B42")


    ChrTalk(
        0xFE,
        (
            "As it is tomorrow\x01",
            "The unveiling ceremony of the Orkis Tower …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Master's job\x01",
            "You have to burn your eyes.\x02",
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
            "My husband at the construction site\x01",
            "I am working but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the past several months, the topic of the new city hall building\x01",
            "At the site of \"Orkis Tower\"\x01",
            "I am sweating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The interior is already completed,\x01",
            "After finishing the exterior finish\x01",
            "It seems to be only to leave … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I am really looking forward to completion.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D3B")

    label("loc_3CBD")


    ChrTalk(
        0xFE,
        (
            "Construction of the \"Orkis Tower\"\x01",
            "Even though my husband has been involved\x01",
            "It is the biggest job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I am really looking forward to completion.\x02",
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
            "In recent years, the autonomous state legislature\x01",
            "The redevelopment plan of the Old Town\x01",
            "I heard that they were being considered … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a result of new deliberations by the new parliament,\x01",
            "The plan is officially frozen\x01",
            "I heard that he decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a story of freezing to the last\x01",
            "Although I am not happy with letting go ……\x01",
            "I was relieved when I heard that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this place is torn down,\x01",
            "Our family wants to visit\x01",
            "I will lose it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F59")

    label("loc_3EB5")


    ChrTalk(
        0xFE,
        (
            "Everything was at the center of the plan\x01",
            "Congressman, with an example of the cult incident\x01",
            "He seems to have been arrested …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition to the plan itself\x01",
            "Because there were many defects,\x01",
            "It seems that the story was torn down.\x02",
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
            "Dad is like this\x01",
            "For the Lima's\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well,\x01",
            "Lima must also do its best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE2")

    Jump("loc_44B0")

    label("loc_3FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_402D")

    ChrTalk(
        0xFE,
        "Both Dad and Mama seem uneasy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you alright?\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4080")

    ChrTalk(
        0xFE,
        (
            "Mama …\x01",
            "I have a sad look on your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want you to get well.\x02",
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
            "Lisa's older sister,\x01",
            "I did not feel well today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened?\x02",
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
            "This morning, with mum\x01",
            "I sent off to see you about my dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is the new genba hobby\x01",
            "It seems that there was room for the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not really understand Lima,\x01",
            "I was happy to see you off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4256")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "With Mama and Lima, to Dad\x01",
            "I went and tasted it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Dad, I was cute and cute.\x02",
    )

    CloseMessageWindow()

    label("loc_4256")

    Jump("loc_44B0")

    label("loc_425B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42B8")

    ChrTalk(
        0xFE,
        (
            "Wonder Land,\x01",
            "It was truly fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to go there again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B0")

    label("loc_42B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42EA")

    ChrTalk(
        0xFE,
        "Tea, tea ♪ everyone with tea ~ ♪\x02",
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
            "Yes, you.\x01",
            "It was like Gohan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not forget it ♪\x02",
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
            "Lima's dad,\x01",
            "Every single day at Kakegobo\x01",
            "I am working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it will be late to go home today.\x01",
            "Shun\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_441F")

    label("loc_43E9")


    ChrTalk(
        0xFE,
        (
            "Dad also today\x01",
            "It seems that you will be late when you go home.\x01",
            "Shun\x02",
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
            "Recently, mean\x01",
            "I heard that Mr. Okaunun has stopped coming.\x01",
            "Mom is pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not really understand it,\x01",
            "I am glad if Mama is pleased.\x02",
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
        "Dad, are you going to work today too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Oh, the current construction site has resumed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Lima, I'm worried about various things\x01",
            "Do not ask for an answering machine with your mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Papa, go ahead!\x01",
            "…… Chu spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I am going.\x02",
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
            "Good night, Lima.\x01",
            "What shall we do today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well …\x01",
            "Well, I'd like to have a good job with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because Lima plays the role of Mama\x01",
            "Dad is playing daddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, is your dad acting as a dad?\x01",
            "Indeed, I understand.\x02",
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
            "No, no …\x01",
            "I'm embarrassed like this,\x01",
            "After all I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, I have various uneasiness … ….,\x01",
            "I will work today for my family too!\x02",
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
            "It has become such a thing,\x01",
            "I do not know what to do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what happens, only Corona and Lima\x01",
            "I have to protect you.\x02",
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
            "Well, it made me so relaxed\x01",
            "It's been a long time since I have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Family members are really nice things.\x02",
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
        "Oh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mogmog …\x01",
            "Yes, even today\x01",
            "delicious.\x02",
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
            "I ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, Dieter ……\x01",
            "Independently, I can not be happy … ….?\x01",
            "…… … … ….\x07\x00\x02",
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
            "Gee ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Where is the country of your dreams ……\x01",
            "Van, please take me there … …\x07\x00\x02",
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
            "Gee ……\x01",
            "Whoa, it was raining again ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Shoben will be close, but …\x07\x00\x02",
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
            "Gee ……\x01",
            "What are you planning to do if you leak it ……\x07\x00\x02",
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
            "I am overnight …\x01",
            "Mira does not have it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Such a guy … ….\x07\x00\x02",
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
            "Shockwave …… I got it … …\x01",
            "1000 Mirror bill ~ …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "At the casino … … If you notice … …\x01",
            "Sukinpin … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gee ……\x07\x00\x02",
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
            "Mira of me … return it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gee ……\x07\x00\x02",
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
            "I ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Oh, Van!\x01",
            "I do not complain with this … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "The main pillar …\x01",
            "I've already earned money …\x01",
            "Wow ~, Hick ……\x07\x00\x02",
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
            "The main pillar …\x01",
            "I've already earned money …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "But wait for the rent … …\x01",
            "Wow ~, Hick ……\x07\x00\x02",
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
            "Hmm … oh ……?\x01",
            "Oh, you have alcohol properly.\x01",
            "Well done, Van.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Glacier …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gluttonous! Is it? Pepe ……!\x01",
            "What is this, is not it vinegar!\x07\x00\x02",
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
            "Who is it that I did this kind of thing …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Oh, okay ……… Mumma … …\x07\x00\x02",
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
            "What? Mira is not hey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "No way … … If it's the case\x01",
            "Just a day and a day ~ …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gee ……\x07\x00\x02",
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
            "No way … … If it's the case\x01",
            "Just a day and a day ~ …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gee ……\x07\x00\x02",
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
            "Gee ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Sake, liquor ……\x01",
            "My Best Friend, Sake! …!\x07\x00\x02",
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
            "Hey, Van!\x01",
            "The liquor is still ~ …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gee ……\x07\x00\x02",
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
            "Gee ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Sake ~, liquor ~.\x01",
            "… … Have a drink … ___ ___ 0\x07\x00\x02",
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
            "The door is tightly closed,\x01",
            "A voice is heard from inside.\x07\x00\x02",
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
            "Those people are Mr. Tantos\x01",
            "I'm glad that you are fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Really, to everyone here\x01",
            "I can not thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517E")

    Jump("loc_51DE")

    label("loc_5183")


    ChrTalk(
        0x9,
        (
            "Those who move me out\x01",
            "I will submit it within today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I am sorry to have trouble.\x02",
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
        "Oh, how are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One who cooks a little more\x01",
            "Because it takes time,\x01",
            "I wonder if I will be waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52CD")

    label("loc_5261")

    OP_4B(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "Well, next\x01",
            "Evening cooked menu\x01",
            "You have to decide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "That's right, what should I do?\x02",
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
            "(Because alcohol was not available recently\x01",
            "If you think that it is sticky … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Kishikuri ~ ……\x01",
            "This is my oie … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A3")

    label("loc_535E")


    ChrTalk(
        0xFE,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "It is not about time that sake and Mira run out.\x02",
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
            "(Couscous……\x01",
            "You are better off drunk. )\x02",
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
            "Couscous……\x01",
            "Well then again\x01",
            "I have to make money.\x02",
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
            "Yeah, if there is only this material\x01",
            "It seems that it will not run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Thank you so much,\x01",
            "Everyone will be pleased with this.\x02",
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
            "talk\x01",                    # 0
            "Listen to the necessary ingredients\x01",      # 1
            "quit\x01",                      # 2
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
            "Oh, I need the ingredients\x01",
            "Do you want to check it again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "First of all, there are ten \"five-grain miso\".\x01",
            "Then 10 \"devil of beasts\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, \"100 sake\" to 10\x01",
            "In addition, 10 \"sesame oil\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So, \"dark mushrooms\" to 30\x01",
            "30 \"All-purpose onega\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally \"Petit Carrot\" 30 pieces.\x01",
            "30 \"Hot Pepper\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That should do it\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DA")

    label("loc_574E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57DA")

    ChrTalk(
        0x13,
        (
            "The cooked menu is\x01",
            "It is impolite \"pork soup\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Both meat and vegetables are taken together,\x01",
            "To nourish\x01",
            "It is perfect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DA")

    Jump("loc_5848")

    label("loc_57DF")


    ChrTalk(
        0x13,
        (
            "Well, this amount\x01",
            "Also quickly\x01",
            "I'm gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "By any means\x01",
            "I wonder if I can pad them up.\x02",
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
            "Wonder what is Van, and lady.\x01",
            "I am firmly in the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's an important son and her friends,\x01",
            "Dad will definitely protect you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "(Kishoguri ー ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5979")

    label("loc_5926")


    ChrTalk(
        0x15,
        (
            "Wonder what is Van, and lady.\x01",
            "I will definitely protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "(Well ……)\x02",
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
            "#01803FWell, I will go to the city hall soon.\x01",
            "I have to prepare ……\x02\x03",
            "#01802FEveryone, about Charlie\x01",
            "Thank you very much for your advice.\x02\x03",
            "#01806FI also went to Ilia 's skinship\x01",
            "There are lots of things … ….\x01",
            "I'll be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5B42")

    label("loc_5A93")


    ChrTalk(
        0xF,
        (
            "#01802FEveryone, about Charlie\x01",
            "Thank you very much for your advice.\x02\x03",
            "#01806FI also went to Ilia 's skinship\x01",
            "There are lots of things … ….\x01",
            "I'll be careful.\x02",
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
        "#01802FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FHi, Lisa.\x01",
            "I was returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802FYes, today this afternoon\x01",
            "Because there was business in the city hall,\x01",
            "I was on holiday.\x02\x03",
            "Ah … … Tio too\x01",
            "It seems that it finally came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, attaching yesterday\x01",
            "I have just returned to the support department.\x02\x03",
            "#00204FAlcan Shell last night,\x01",
            "It was a stage that invited leaders from different countries … …\x01",
            "I really appreciate your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHuhu, were you nervous after all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FHaha, the usual stage is\x01",
            "It certainly was a bit different.\x02\x03",
            "#01804FAlthough it is a branch, SRIRI also\x01",
            "It is supposed to be on the stage for the first time\x01",
            "It was a terrible tension feeling … ….\x02\x03",
            "#01802FHowever, Iria something\x01",
            "It was as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha, Iria\x01",
            "I wonder if it is nothing to be tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01804FYeah, it's really about the stage\x01",
            "Iria is straight … …\x02\x03",
            "#01802FHuhuu, I will always be someday\x01",
            "I do not feel like enemies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FWell, for artists\x01",
            "It is a very high goal, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuff, what did you say?\x01",
            "It is said to be a true genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FBut if Lisher, absolutely someday\x01",
            "I feel like catching up with Iria.\x02\x03",
            "#00004FAlso from chandeliers yesterday\x01",
            "I caught a falling kittens\x01",
            "It was quite amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FHaha … … Thank you.\x02\x03",
            "#01802FBut, truly that one\x01",
            "Because the body just moved …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01803FBy the way, yesterday 's girl ……\x01",
            "Was it Shirley?\x02\x03",
            "#01802FIt seems to be Randy's cousin … …\x01",
            "Who is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FLet me see……\x02\x03",
            "#00003F(Say unnecessary things\x01",
            "Wake to involve Lisha\x01",
            "I do not wish (…))\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F…… Haha, whatever you are\x01",
            "You're such a girlfriend's girlfriend.\x02\x03",
            "#00302FJust because it's a painful one\x01",
            "Dodge well when entangled.\x02\x03",
            "#00309FSomehow, Atsu, Lisha-chan\x01",
            "You seem to like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuff, if you give up\x01",
            "In an eye like Ellie\x01",
            "It may be encountered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FEven ….\x01",
            "Please do not forget it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01808FBlooded#9RBloody#Charlie ……)\x02\x03",
            "#01803F(Maybe this time,\x01",
            "With me as \"silver\" ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWell, Lisha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802F… … Hehe, no.\x01",
            "Thank you for your advice.\x02\x03",
            "#01806FI also went to Ilia 's skinship\x01",
            "There are lots of things … ….\x01",
            "I will manage somehow.\x02",
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
        "#12P#10112FOh, haha ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00206FLesha is having trouble too.\x02",
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
            "There is a lock on the door.\x07\x00\x02",
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
            "There is a lock on the door.\x07\x00\x02",
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
            "There is a lock on the door.\x07\x00\x02",
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
            "#6P#00000FOld Town · Lotus Heights … ….\x01",
            "Yeah, it should match here.\x02",
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
            "#6P#00000FExcuse me,\x01",
            "Is anyone coming?\x02",
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
        "#6P#10103FThere is no response, is not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FHow is the key?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00001FOh, it's sticky.\x02\x03",
            "#00003FI feel I felt a little sign,\x01",
            "I wonder if it was due to mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FIt might be a residence, or?\x02\x03",
            "#10300FWhat do you do in that case?\x01",
            "Can you open it even if you forcibly open it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FOh, if there is no other hand\x01",
            "The worst thought possible though … …\x02",
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
        "#6P#10105FWhat is it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, it sounds like dishes or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FApparently, I am immune\x01",
            "The possibility seems to be quite high …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FWill you call out again, again?\x02\x03",
            "#00001FExcuse me!\x01",
            "You are welcome! Is it?\x02\x03",
            "I'd like to ask you a few stories!\x02",
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
            "#6P#10304FHuh, it is a thorough anti-war place.\x02\x03",
            "#10302FOr from the window\x01",
            "Run away or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWell, then\x01",
            "It's kind of awkward.\x02",
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
            "#12PIt's noisy somewhere from a little while ago ….\x01",
            "Is it your work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PWhat on earth was it?\x02",
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
            "#5P#00005FOh, I'm sorry.\x02\x03",
            "#00000FThey are cross-police\x01",
            "I am a Special Support Section, but …\x02\x03",
            "#00003FHey, in this room\x01",
            "There was an errand for the residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105FThat two,\x01",
            "Do you know the direction of this room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12POh, of course\x01",
            "Do not you know that … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x0)

    ChrTalk(
        0x9,
        (
            "#12PHmm, I will tell you the circumstances\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes, in fact …\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is a suspicious house\x01",
            "I explained the survey.\x07\x00\x02",
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
            "#12PI see.\x01",
            "Confirm residents with that\x01",
            "Is it necessary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PWell, what are you saying?\x01",
            "I did sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FWell, what is that …?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x0)

    ChrTalk(
        0x9,
        (
            "#12POh, for what I hide\x01",
            "I used to live in this room before\x01",
            "He's a Geithner.\x02",
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
        "#5P#00005FWell, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12POh, that's why\x01",
            "I have to hand out the transfer\x01",
            "You did not go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PBut well, is it not too late now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI understand, who is the order form\x01",
            "I will surely let you out within today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, if you do that\x01",
            "This is also helpful.\x02\x03",
            "#00103FBy the way, about the circumstances of moving out\x01",
            "May I ask you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12POh, in a nutshell,\x01",
            "This is also called \"Edge\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PIn the first place, I was a year ago\x01",
            "Make a big mistake as a merchant\x01",
            "I came to this apartment … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PAn old business association who knew my circumstances\x01",
            "Let's do business together\x01",
            "He gave me a voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PSo, about two weeks ago\x01",
            "To a republic with that group\x01",
            "It was a place I moved to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FSo, what are you here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12POh, thank you for taking care of me in this apartment\x01",
            "I came again to thank you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PTo everyone\x01",
            "I was really well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PCheerfully, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FIndeed, Mr. Geithner's\x01",
            "I understand the situation in general.\x02\x03",
            "#00000FAgain about the now residents\x01",
            "I'd like to ask …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHmm, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105F…… something, hard to tell\x01",
            "Is it also circumstances?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PNo, well of the principal\x01",
            "I think that it is a matter of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12Pwhich one……\x02",
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
            "#6PTantos is …\x01",
            "You guys, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you were listening\x01",
            "Can you open here and be a part of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIt is the police who is here.\x01",
            "Because you know the name,\x01",
            "Nothing happens, it's not funny.\x02",
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
        "#6P#00105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6POh, it looks like it was opened.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PSo, do not get too much trouble inside\x01",
            "Can you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWell, thank you for your cooperation.\x02",
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
        "#6P#00000F--Excuse me.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Is it? Is it? Is it?",
        "#11PDid you come to laugh at me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh……?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    NpcTalk(
        0xA,
        "Is it? Is it? Is it?",
        (
            "#11PI wonder if you came to laugh at me\x01",
            "I tell you!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Is it? Is it? Is it?",
        (
            "#11PWhile being caught in the glory of the parliamentary era\x01",
            "It has fallen completely now\x01",
            "This guerball!\x02",
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
        "#6P#00011FHere, this person …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F…… It is a former imperialist member Gebal.\x02\x03",
            "#00101FSince fraud has been discovered in the past,\x01",
            "I always stayed at Ursula hospital\x01",
            "I wonder if I was in the hospital … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHuh, huh, again\x01",
            "Did you know me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PLocate my whereabouts\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PMi, Mira will not do as you see it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PEven if you rent this apartment,\x01",
            "Follow the old acquaintance\x01",
            "It was a place I managed to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHa ha, it does not matter,\x01",
            "Even such a thin line of personal connections\x01",
            "Is not it hungry to use it?\x02",
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
            "#6P#00106FNo, that's what I intended to do.\x01",
            "I do not have hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe,\x01",
            "With this eyes you\x01",
            "I only wanted to confirm.\x02\x03",
            "#00003FEr, Mr. Gebal.\x01",
            "You are the new resident here\x01",
            "There is no mistake, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PAh, oh … that is right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FConfirmation is completed with this.\x02\x03",
            "#10100FIt was used for crime\x01",
            "It is not a point of concern, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FBut why did I submit it?\x01",
            "Name of fairy tale author\x01",
            "I guess I wrote it.\x02\x03",
            "#10300FIt's too suspicious, on the contrary\x01",
            "I think that my legs will stick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FCertainly, this house is the best\x01",
            "It was doubtful to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHuh, huh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PFrom a long time ago Shawn ·\x01",
            "It is a big fan of Al Nam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI came up with an idea\x01",
            "Because the name was that\x01",
            "It can not be helped!\x02",
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
            "#6P#10112FLet me see……\x01",
            "It is a bit surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FWell, to various generations\x01",
            "I am a writer who is being read … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, this is also called\x01",
            "Is it a gap moe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWell, maybe … ….?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PEee … …. It's noisy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI wonder what you have done errands!\x01",
            "Then, please go out quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FEh, yeah, I'm sorry.\x02\x03",
            "#00100FThen Lloyd,\x01",
            "Shall we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh.\x02\x03",
            "Then, I will excuse you.\x02",
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
            "Perhaps,\x01",
            "Did you come and help me?\x02",
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
            "#00000FHere, we cooked\x01",
            "You are preparing.\x02",
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
        "OH right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Er …\x01",
            "Actually the ingredients for cooking\x01",
            "It was pretty lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If possible, please buy\x01",
            "I'd like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FI will not buy it.\x01",
            "Well, I guess it's cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FBy the way, what is just how much\x01",
            "Is it necessary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, since I say from now\x01",
            "I wonder if you remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "First of all, there are ten \"five-grain miso\".\x01",
            "Then 10 \"devil of beasts\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, \"100 sake\" to 10\x01",
            "In addition, 10 \"sesame oil\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So, \"dark mushrooms\" to 30\x01",
            "30 \"All-purpose onega\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally \"Petit Carrot\" 30 pieces.\x01",
            "30 \"Hot Pepper\".\x02",
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
            "Oh, that's all\x01",
            "I often eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Actually yesterday, I did not get enough\x01",
            "It was a bit of a fuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So today, that is\x01",
            "Do not make it so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI - I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBy the way,\x01",
            "What on earth are you cooking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, my body and mind also warm up -\x01",
            "\"Pork soup\" is a fool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Naturally everyone will\x01",
            "I will let you act.\x02",
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
            "Oh yeah, I bought it\x01",
            "I have to hand you the price.\x02",
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
            "500 Mira\x07\x00",
            "Received.\x02",
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
            "#00306FNo, what kind of … ….\x01",
            "It is not enough to think about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Well, sorry.\x01",
            "After all the budget is awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "In the intention of helping us\x01",
            "I'd like to ask you somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, the missing part\x01",
            "By saying that we donate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYeah, the situation is also the situation,\x01",
            "I wonder if this should be cooperated.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10300FHuh, if you decide so\x01",
            "Good is a hurry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00000FOh, at once\x01",
            "Let's say you head for buying.\x02",
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
            "Hmm, you guys.\x01",
            "Material procurement for cooking\x01",
            "Are you going to help me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, thank you.\x01",
            "Sorry to keep you well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh yea -\x01",
            "If it's okay it's one thing\x01",
            "There was something I wanted to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The ingredients of tomatoes are\x01",
            "Condensed extract ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somewhere with it\x01",
            "If you can get it\x01",
            "I want you to bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do so, you will find a special cake\x01",
            "\"Tomba pork soup in tonic\"\x01",
            "You can behave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExtract ……\x01",
            "\"Nagara Tomato\" by itself\x01",
            "Is it useless?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, it's frightening to cook\x01",
            "It will take time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you can afford it, you do not mind.\x01",
            "It is not troublesome even if it is not necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, I will remember.\x02",
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
            "Oh, apparently the item of my order\x01",
            "You seem to have brought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I appreciate it.\x01",
            "With everyone in this\x01",
            "I will be able to inject energy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F57")

    label("loc_8EB9")


    ChrTalk(
        0x8,
        (
            "The ingredients of tomatoes are\x01",
            "Condensed extract ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somewhere with it\x01",
            "If you can get it\x01",
            "I want you to bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you can afford\x01",
            "I do not mind having it.\x02",
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
            "Oh, Foodstuff\x01",
            "Did you procure it?\x02",
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
            "Give ingredients\x01",      # 0
            "To give up\x01",      # 1
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
            "Oh, maybe\x01",
            "Have not you got it yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Then, if you are ready\x01",
            "Please give me a voice again.\x02",
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
            "#20IFive grain miso\x07\x00",
            "× 10\x01\x07\x02",
            "#20IDemonic beast of meat\x07\x00",
            "× 10\x01\x07\x02",
            "#20IHundred-percent sake\x07\x00",
            "× 10\x01\x07\x02",
            "#20ISesame Oil\x07\x00",
            "× 10\x01\x07\x02",
            "#20IDark mushroom\x07\x00",
            "× 30\x01\x07\x02",
            "#20IAll-purpose green onion\x07\x00",
            "× 30\x01\x07\x02",
            "#20IPetit carrot\x07\x00",
            "× 30\x01\x07\x02",
            "#20IHot Pepper\x07\x00",
            "× 30 passed.\x07\x00\x02",
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
            "You brought me well.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦西红柿酱', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94D6")
    OP_2C(0x8E, 0x1)

    ChrTalk(
        0x103,
        (
            "#00205FBy the way, Mr. Lloyd … …\x01",
            "Would you rather give that one back?\x02",
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
        "This is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FMr. Huff, Mr. Tantos\x01",
            "I asked for procurement.\x02\x03",
            "#10302FAnything special pig soup\x01",
            "I heard that I can do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, that story?\x01",
            "Surely the person himself said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yeah, then this\x01",
            "Listen to Mr. Tantos\x01",
            "Let's use it by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 4)

    label("loc_94D6")


    ChrTalk(
        0x104,
        (
            "#00300FSoba, this is it\x01",
            "Do you mind if I end the help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh Good job.\x01",
            "Thanks, I was saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "When the work breaks\x01",
            "I will start cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Everyone in the support department\x01",
            "Please participate by all means.\x02",
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
            "#00004FWell, leave it to me.\x01",
            "It looks okay.\x02\x03",
            "#00000FI helped out all the way,\x01",
            "Would you like to report to Abbas?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_96AE")

    label("loc_9656")


    ChrTalk(
        0x101,
        (
            "#00004FWell, leave it to me.\x01",
            "It looks okay.\x02\x03",
            "#00000FWe have other places\x01",
            "Let's go around.\x02",
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
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FI'm sorry, Mr. Gebal.\x01",
            "Do you Come?\x02",
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
        "#00003FLooks like he's out\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThis is here in Mr. Gebal's room\x01",
            "There is no doubt … ….\x02",
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
            "You guys,\x01",
            "What do you do?\x02",
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
            "Oh, it's an anniversary …\x01",
            "Was he surely a special support section?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3630, 1300, 2880, 2000)
    OP_95(0x8, 3800, 0, 1500, 1500, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        (
            "#10302FGiggle\x01",
            "Hello, Mr. Tantos.\x02\x03",
            "I lived here.\x01",
            "Former lawmaker's uncle\x01",
            "Where are you going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, if he is from last week\x01",
            "Where are you going out? …\x02",
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
            "Lloyd at the request of Almu\x01",
            "I explained the circumstances of searching for Gebal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, I came all the way from Libert\x01",
            "An example son or couple ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Coca-Cola\x01",
            "It is quite a fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FMy grandfather also told me about Al Mr.\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just last week, the apartment\x01",
            "I have come to visit.\x01",
            "I had you talk a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, but from just before that,\x01",
            "Gabal is somewhere\x01",
            "It seems like I went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have you heard about the destination\x01",
            "I wonder where I went ……\x02",
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
            "Perhaps it is Genbal's\x01",
            "A person who knows where to go\x01",
            "Maybe there is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, certainly towards Nishi-dori\x01",
            "He was taken care of in the Congressman days\x01",
            "You seem to have a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even when you move here,\x01",
            "She seems to have taken care of various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure, Vi, Villa ……\x01",
            "Villa somehow, such as the name\x01",
            "She seems to live in a building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FVilla somehow ……\x01",
            "It seems like somehow heard\x01",
            "It's a word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, the building on Nishi-dori\x01",
            "Let's look for it.\x02\x03",
            "#00000Fold man,\x01",
            "Thank you for your cooperation.\x02",
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
            "Gabal and his son couple,\x01",
            "Let me catch up somehow.\x02",
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
