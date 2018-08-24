from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Old Man Tantos",         # 1
        "Geithner",               # 2
        "Geval",                  # 3
        "Corona",                 # 4
        "Rimah",                  # 5
        "Melson",                 # 6
        "Medical Intern Micheau", # 7
        "Rixia",                  # 8
        "Grandma Paola",          # 9
        "Vaan",                   # 10
        "Roser",                  # 11
        "Azel",                   # 12
        "Man's Voice",            # 13
        "Bacchus",                # 14
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
        "Function_7_1C61",         # 07, 7
        "Function_8_1DD6",         # 08, 8
        "Function_9_1F47",         # 09, 9
        "Function_10_207E",        # 0A, 10
        "Function_11_2EAD",        # 0B, 11
        "Function_12_3086",        # 0C, 12
        "Function_13_3228",        # 0D, 13
        "Function_14_3577",        # 0E, 14
        "Function_15_4266",        # 0F, 15
        "Function_16_47A9",        # 10, 16
        "Function_17_48C0",        # 11, 17
        "Function_18_4990",        # 12, 18
        "Function_19_4C44",        # 13, 19
        "Function_20_5358",        # 14, 20
        "Function_21_539D",        # 15, 21
        "Function_22_54B0",        # 16, 22
        "Function_23_55AD",        # 17, 23
        "Function_24_5692",        # 18, 24
        "Function_25_573B",        # 19, 25
        "Function_26_5B21",        # 1A, 26
        "Function_27_5C5E",        # 1B, 27
        "Function_28_5DDF",        # 1C, 28
        "Function_29_6886",        # 1D, 29
        "Function_30_699D",        # 1E, 30
        "Function_31_85EB",        # 1F, 31
        "Function_32_8E77",        # 20, 32
        "Function_33_929B",        # 21, 33
        "Function_34_9A47",        # 22, 34
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BE2")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think the character who\x01",
            "supported Geval when he was a\x01",
            "congressman lives on West Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I recall, Vil, Villa...\x01",
            ""Villa Something" is the name\x01",
            "of the building where he lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He might know Geval's\x01",
            "whereabouts.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B")
    Call(0, 32)
    Return()

    label("loc_C0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D46")

    ChrTalk(
        0xFE,
        (
            "The kids of the delinquent\x01",
            "groups are cooperating to\x01",
            "protect Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before, they fought many times in the\x01",
            "square and they were hard to approach. But\x01",
            "we can really rely on those youngsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like this is the first\x01",
            "time Downtown has become one\x01",
            "since I came here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DF7")

    label("loc_D46")


    ChrTalk(
        0xFE,
        (
            "Those delinquent kids are\x01",
            "protecting Downtown. I knew we\x01",
            "could rely on those youngsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like this is the first\x01",
            "time Downtown has become one\x01",
            "since I came here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF7")

    Jump("loc_1C5D")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E83")

    ChrTalk(
        0xFE,
        (
            "Just what is that blue\x01",
            "mist outside...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I must warn the\x01",
            "residents of this apartment\x01",
            "not to go outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(
        0xFE,
        (
            "I heard the President's\x01",
            "address too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand his opinion,\x01",
            "but... Is there really no\x01",
            "peaceful way of solving this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F87")

    label("loc_F1F")


    ChrTalk(
        0xFE,
        (
            "I understand the\x01",
            "president's opinion,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is there really no\x01",
            "peaceful way of solving\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F87")

    Jump("loc_1C5D")

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_10A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_103F")

    ChrTalk(
        0x8,
        (
            "Once you've thoroughly\x01",
            "cooked veggies you can\x01",
            "flavor them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""Robust Tomato Pork\x01",
            "Miso"... I'm looking\x01",
            "forward to it, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A4")

    label("loc_103F")


    ChrTalk(
        0x8,
        (
            "Now then, time to get my\x01",
            "emergency feeding bowl\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm making this for\x01",
            "everyone today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A4")

    Jump("loc_1150")

    label("loc_10A9")


    ChrTalk(
        0x8,
        (
            "We'll be doing the emergency\x01",
            "feeding in this room and in\x01",
            "Corona's room too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The quantity is what it is. I\x01",
            "have supplies in the kitchen,\x01",
            "but it's not enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1150")

    Jump("loc_11D6")

    label("loc_1155")


    ChrTalk(
        0xFE,
        (
            "Hoho! Most importantly,\x01",
            "everyone at the pork miso and\x01",
            "thought it was delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am obliged to thank\x01",
            "you all as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D6")

    Jump("loc_1C5D")

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129F")

    ChrTalk(
        0xFE,
        (
            "Yesterday evening, Geval\x01",
            "had a rare visitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's looked strange ever\x01",
            "since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he's being chased\x01",
            "by someone, but... Hmm,\x01",
            "I'm a little worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12EC")

    label("loc_129F")


    ChrTalk(
        0xFE,
        (
            "He said he's being chased\x01",
            "by someone, but... Hmm,\x01",
            "I'm a little worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC")

    Jump("loc_1C5D")

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1345")

    ChrTalk(
        0xFE,
        (
            "It seems Geval's getting\x01",
            "used to life here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hoho, splendid.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D8")

    ChrTalk(
        0xFE,
        (
            "*shock*... Geval's beans\x01",
            "are a true masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho! I planned to make\x01",
            "him dinner, but it seems\x01",
            "I won't be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148C")

    label("loc_13D8")


    ChrTalk(
        0xFE,
        (
            "But most importantly, it\x01",
            "seems Geval is opening\x01",
            "his heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Geval was prideful during his\x01",
            "time as congressman, but it seems his\x01",
            "true nature is that of a nice man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148C")

    Jump("loc_1C5D")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14A2")
    Call(0, 7)
    Jump("loc_1C5D")

    label("loc_14A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_163A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AD")

    ChrTalk(
        0xFE,
        (
            "Crossbell State, huh... Our\x01",
            "claim is legitimate, but I\x01",
            "feel our greed is excessive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The major powers won't look\x01",
            "kindly on this. I can't think\x01",
            "things will proceed peacefully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Mayor Dieter\x01",
            "has made a bold\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1635")

    label("loc_15AD")


    ChrTalk(
        0xFE,
        (
            "Crossbell will become a\x01",
            "state, huh. I can't think\x01",
            "this will go peacefully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Mayor Dieter\x01",
            "has made a bold\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1635")

    Jump("loc_1C5D")

    label("loc_163A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1655")
    Call(0, 8)
    Jump("loc_16D6")

    label("loc_1655")


    ChrTalk(
        0xFE,
        "Yes, yes. I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly, if something like that\x01",
            "happened, succumbing to temptation\x01",
            "wouldn't be out of the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D6")

    Jump("loc_1C5D")

    label("loc_16DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1875")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(
        0xFE,
        (
            "The unveiling ceremony, huh...\x01",
            "There's a big hullabaloo in\x01",
            "the city about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That new City Hall building or\x01",
            "whatever is like a symbol of\x01",
            "Crossbell's prosperity, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they wouldn't forget\x01",
            "the humble folks that live\x01",
            "here in its shadows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1870")

    label("loc_17FA")


    ChrTalk(
        0xFE,
        (
            "But, it seems Geval is\x01",
            "holed up as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I knocked on his\x01",
            "door again and he\x01",
            "listened with a grumble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1870")

    Jump("loc_1C5D")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1939")

    ChrTalk(
        0xFE,
        (
            "Patrol officers are coming to\x01",
            "Downtown tomorrow on account\x01",
            "of the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not like the heads\x01",
            "of state would even visit a\x01",
            "desolate block like this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195E")
    Call(0, 9)
    Jump("loc_19B4")

    label("loc_195E")


    ChrTalk(
        0xFE,
        (
            "Hmm. Most importantly,\x01",
            "I'm glad you're doing\x01",
            "well, Geithner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm happy too.\x02",
    )

    CloseMessageWindow()

    label("loc_19B4")

    Jump("loc_1A2D")

    label("loc_19B9")


    ChrTalk(
        0xFE,
        (
            "Everyone, please deal\x01",
            "gently with Geval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of things have\x01",
            "happened to him, and his\x01",
            "spirit needs rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2D")

    Jump("loc_1C5D")

    label("loc_1A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA1")

    ChrTalk(
        0xFE,
        (
            "As you can see, Downtown\x01",
            "was left behind by the\x01",
            "city planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Public order is bad, but rent is\x01",
            "cheap, and people with all sorts of\x01",
            "circumstances have gathered here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, some of\x01",
            "us grab hold of success\x01",
            "after leaving the nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho! It's certainly true\x01",
            "that all manner of lives\x01",
            "are packed into this place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C5D")

    label("loc_1BA1")


    ChrTalk(
        0xFE,
        (
            "Though people with all manner of\x01",
            "circumstances gather here in\x01",
            "Downtown, some of us leave the nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho! It's certainly true\x01",
            "that all manner of lives\x01",
            "are packed into this place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    TalkEnd(0xFE)
    Return()

    # Function_6_AE8 end

    def Function_7_1C61(): pass

    label("Function_7_1C61")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(
        0x8,
        (
            "*crunch, munch*... Ho,\x01",
            "this is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you make these\x01",
            "beans, Geval?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. I was a cook a\x01",
            "while back, so I tried\x01",
            "making them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just glad you like\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho, thanks for the\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DCD")

    label("loc_1D4D")


    ChrTalk(
        0x8,
        (
            "Hmm, how about bringing\x01",
            "some to others if there\x01",
            "are leftovers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure everyone will\x01",
            "love them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-You think so?\x02",
    )

    CloseMessageWindow()

    label("loc_1DCD")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_1C61 end

    def Function_8_1DD6(): pass

    label("Function_8_1DD6")


    ChrTalk(
        0xA,
        "L-Listen to me, Tantos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was full of hopes too\x01",
            "when I was a new\x01",
            "resident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho. I've heard that\x01",
            "story many times. I\x01",
            "believe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You were thinking of\x01",
            "changing this city to suit\x01",
            "your own style, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, exactly. Back then, I\x01",
            "was elected as a motivated,\x01",
            "independent congressman....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But one day, a certain\x01",
            "Imperial faction came...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_1DD6 end

    def Function_9_1F47(): pass

    label("Function_9_1F47")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "Oh, Geithner. Glad\x01",
            "you're doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, how's business?\x01",
            "Going well, I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. Thankfully,\x01",
            "everything's going\x01",
            "smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's right. I brought\x01",
            "you a box cake as a\x01",
            "souvenir. Please, take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, thanks for this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I'll make some\x01",
            "tea right away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_9_1F47 end

    def Function_10_207E(): pass

    label("Function_10_207E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_239E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(
        0xFE,
        (
            "Because of an arrangement\x01",
            "with the guild, I can speak\x01",
            "with Alm and Aerie in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there's chaos in Liberl\x01",
            "too, but it's peaceful compared\x01",
            "to the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chaos is Crossbell has been\x01",
            "going on for a while... I'm glad\x01",
            "I was able to hear from them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_225F")

    label("loc_21C6")


    ChrTalk(
        0xFE,
        (
            "I was able to speak with\x01",
            "Alm and Aerie in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chaos is Crossbell has been\x01",
            "going on for a while... That's\x01",
            "why I have to do my best too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225F")

    Jump("loc_2399")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232F")

    ChrTalk(
        0xFE,
        (
            "Just when the president was\x01",
            "arrested, that strange,\x01",
            "huge tree appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I had just one wish,\x01",
            "it would be to get\x01",
            "through this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess, please save\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2399")

    label("loc_232F")


    ChrTalk(
        0xFE,
        (
            "If I had just one wish,\x01",
            "it would be to get\x01",
            "through this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess, please save\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2399")

    Jump("loc_2EA9")

    label("loc_239E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2467")

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "state of the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Alm's family\x01",
            "in Liberl is safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son is my hope. I'd\x01",
            "like to contact him if\x01",
            "possible...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2511")

    label("loc_2467")


    ChrTalk(
        0xFE,
        (
            "Ever since the declaration of\x01",
            "independence, foreign communication\x01",
            "has completely ceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alm and Aerie are my hope,\x01",
            "so I'd like to contact\x01",
            "them somehow, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2511")

    Jump("loc_25AF")

    label("loc_2516")


    ChrTalk(
        0xFE,
        (
            "Just what are those\x01",
            "monsters that have\x01",
            "appeared in town...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't look like they've\x01",
            "entered Downtown, but will\x01",
            "they really be all right!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AF")

    Jump("loc_2EA9")

    label("loc_25B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C8")

    ChrTalk(
        0xFE,
        (
            "I-I heard the address on\x01",
            "East Street, but I honestly\x01",
            "couldn't believe it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say, the\x01",
            "major powers won't stay\x01",
            "silent with those remarks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given that, it might be\x01",
            "wise to relocate outside\x01",
            "the state, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2833")

    label("loc_26C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279A")

    ChrTalk(
        0xFE,
        (
            "Alm and Aerie are in\x01",
            "Liberl, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmph... What kind of\x01",
            "convenient thing am I\x01",
            "thinking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm rotten, I'm\x01",
            "Crossbellian... No matter\x01",
            "what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2833")

    label("loc_279A")


    ChrTalk(
        0xFE,
        (
            "Goodness... What kind of\x01",
            "convenient thing am I\x01",
            "thinking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm rotten, I'm\x01",
            "Crossbellian... No matter\x01",
            "what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2833")

    Jump("loc_29EE")

    label("loc_2838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")

    ChrTalk(
        0xFE,
        (
            "I-I heard the address on\x01",
            "East Street, but I honestly\x01",
            "couldn't believe it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say, the\x01",
            "major powers won't stay\x01",
            "silent with those remarks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given that, it might be\x01",
            "wise to relocate outside\x01",
            "the state, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29EE")

    label("loc_2937")


    ChrTalk(
        0xFE,
        (
            "...Hmph, what am I thinking? If\x01",
            "I discard this state now and\x01",
            "flee somewhere else, what am I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm rotten, I'm\x01",
            "Crossbellian... No matter\x01",
            "what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EE")

    Jump("loc_2EA9")

    label("loc_29F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A01")
    Jump("loc_2EA9")

    label("loc_2A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A67")

    ChrTalk(
        0xFE,
        (
            "T-That was a joke! I've\x01",
            "got to hurry and hide!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But, just where can I\x01",
            "go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA9")

    label("loc_2A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A78")
    Call(0, 11)
    Jump("loc_2EA9")

    label("loc_2A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A89")
    Call(0, 12)
    Jump("loc_2EA9")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A9A")
    Call(0, 7)
    Jump("loc_2EA9")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEF")

    ChrTalk(
        0xFE,
        (
            "Hmm. Mayor Dieter has\x01",
            "resorted to drastic\x01",
            "measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow... With this, the positions of the\x01",
            "Imperial and Republic faction congresspeople\x01",
            "will grow even more precarious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hey, why the heck am\x01",
            "I discussing politics?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I'll have to think\x01",
            "seriously about what I\x01",
            "want to do in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C27")

    label("loc_2BEF")


    ChrTalk(
        0xFE,
        (
            "A second life, huh... I\x01",
            "wonder what's left for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C27")

    Jump("loc_2EA9")

    label("loc_2C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C47")
    Call(0, 8)
    Jump("loc_2CB3")

    label("loc_2C47")


    ChrTalk(
        0xFE,
        (
            "I know it's not an\x01",
            "excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at that time, I was\x01",
            "a youngster who didn't\x01",
            "know left from right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB3")

    Jump("loc_2EA9")

    label("loc_2CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D20")

    ChrTalk(
        0xFE,
        (
            "To hell with the VIPs'\x01",
            "visit!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Every last\x01",
            "person's in a festive\x01",
            "mood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA9")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDB")

    ChrTalk(
        0xFE,
        (
            "H-Hmph... What's with\x01",
            "this trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've already lost\x01",
            "interest in both\x01",
            "congress and government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should just do\x01",
            "whatever they want.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E3A")

    label("loc_2DDB")


    ChrTalk(
        0xFE,
        (
            "H-Hmph... What's with\x01",
            "this trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should just do\x01",
            "whatever they want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3A")

    Jump("loc_2EA9")

    label("loc_2E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2EA0")

    ChrTalk(
        0xFE,
        (
            "Y-You still have\x01",
            "business with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you've no business,\x01",
            "leave already!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA9")

    label("loc_2EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2EA9")

    label("loc_2EA9")

    TalkEnd(0xFE)
    Return()

    # Function_10_207E end

    def Function_11_2EAD(): pass

    label("Function_11_2EAD")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    ChrTalk(
        0xB,
        (
            "Umm, I've baked cookies\x01",
            "you see. If you like,\x01",
            "please take one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ehehe. Mom's homemade\x01",
            "cookies. So good♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "T-Then, don't mind if I\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's like I'm receiving\x01",
            "a favor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, please don't worry\x01",
            "about the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I made extra, just like\x01",
            "you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I see, then...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3079")

    label("loc_300B")


    ChrTalk(
        0xA,
        (
            "*crunch, crunch*... Mmm,\x01",
            "these are good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ehehe, I know, right?♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, I'm glad you like\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3079")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_2EAD end

    def Function_12_3086(): pass

    label("Function_12_3086")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A1")

    ChrTalk(
        0xC,
        (
            "Mom, these beans are\x01",
            "yummy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, Rimah's really\x01",
            "taken a liking to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Geval, are you sure we\x01",
            "can have some?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's more here than I\x01",
            "can eat. Please feel\x01",
            "free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thanks, mister!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_321B")

    label("loc_31A1")


    ChrTalk(
        0xC,
        "*glom*. Mmm, it's good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, Rimah. You mustn't\x01",
            "eat with your fingers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, I'm glad she likes\x01",
            "it so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321B")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_3086 end

    def Function_13_3228(): pass

    label("Function_13_3228")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3239")
    Jump("loc_3573")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3247")
    Jump("loc_3573")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3255")
    Jump("loc_3573")

    label("loc_3255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3263")
    Jump("loc_3573")

    label("loc_3263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3271")
    Jump("loc_3573")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331B")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I knew this\x01",
            "commute would be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And there are a lot of\x01",
            "people I know here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just can't work up the\x01",
            "will to leave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_339D")

    label("loc_331B")


    ChrTalk(
        0xFE,
        (
            "This commute is hard, but\x01",
            "there are a lot of people I\x01",
            "know in this apartment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just can't work up the\x01",
            "will to leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339D")

    Jump("loc_3573")

    label("loc_33A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33B0")
    Jump("loc_3573")

    label("loc_33B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33BE")
    Jump("loc_3573")

    label("loc_33BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33CC")
    Jump("loc_3573")

    label("loc_33CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33DA")
    Jump("loc_3573")

    label("loc_33DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33E8")
    Jump("loc_3573")

    label("loc_33E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349D")

    ChrTalk(
        0xFE,
        (
            "Uhhm, the materials I\x01",
            "got during\x01",
            "orientation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it hasn't been long since\x01",
            "I enrolled... If I forgot them,\x01",
            "that'd make things difficult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3573")

    label("loc_349D")


    ChrTalk(
        0xFE,
        (
            "Haha, but I really passed\x01",
            "the St. Ursula Medical\x01",
            "School entrance exam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it'll be even tougher going forward\x01",
            "than the exam was, but... it might be good\x01",
            "to bask in the glow of success a bit longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3573")

    TalkEnd(0xFE)
    Return()

    # Function_13_3228 end

    def Function_14_3577(): pass

    label("Function_14_3577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_362A")

    ChrTalk(
        0xFE,
        (
            "When I look at that huge\x01",
            "pale blue tree, I can't\x01",
            "help but be worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband, who works outdoors,\x01",
            "must feel the same... I want to\x01",
            "help him somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_362A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_36B0")

    ChrTalk(
        0xFE,
        (
            "They called it martial law,\x01",
            "but to think something like\x01",
            "this would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...My cooking hands are\x01",
            "shaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_36B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3755")

    ChrTalk(
        0xFE,
        (
            "I asked Tantos about the\x01",
            "address, but honestly,\x01",
            "I'm full of uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband left for work\x01",
            "normally today... I hope\x01",
            "he gets home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_3755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_382B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A8")

    ChrTalk(
        0xFE,
        (
            "It's hard to cook\x01",
            "daikon, so some light\x01",
            "scoring...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3826")

    label("loc_37A8")

    OP_4B(0x10, 0x0)

    ChrTalk(
        0xB,
        (
            "Now then. Next is to\x01",
            "decide on tonight's\x01",
            "emergency feeding menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That's right. I wonder\x01",
            "what would be good.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_3826")

    Jump("loc_4262")

    label("loc_382B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_38B7")

    ChrTalk(
        0xFE,
        (
            "I heard a scary incident\x01",
            "occurred at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF are fighting even\x01",
            "now, but... I hope they\x01",
            "resolve this quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_38B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38C8")
    Call(0, 11)
    Jump("loc_4262")

    label("loc_38C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_38D9")
    Call(0, 12)
    Jump("loc_4262")

    label("loc_38D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3969")

    ChrTalk(
        0xFE,
        (
            "My husband started work\x01",
            "at a new site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Day after day he works hard\x01",
            "for his family... Words are\x01",
            "not enough to thank him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_3969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B92")

    ChrTalk(
        0xFE,
        (
            "I heard this from my husband a while back. He said\x01",
            "foreign construction companies had significant\x01",
            "involvement with the construction of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand that the\x01",
            "floors were divided up\x01",
            "between them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among them, my husband participated\x01",
            "in construction of the VIP floor and\x01",
            "the international conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They call it the international\x01",
            "conference room, but it was used for\x01",
            "the trade conference the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. When I think that\x01",
            "it's the place my husband\x01",
            "worked, I'm happy somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C53")

    label("loc_3B92")


    ChrTalk(
        0xFE,
        (
            "They call it the international\x01",
            "conference room, but it was used for\x01",
            "the trade conference the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. When I think that\x01",
            "it's the place my husband\x01",
            "worked, I'm happy somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C53")

    Jump("loc_4262")

    label("loc_3C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CD3")

    ChrTalk(
        0xFE,
        (
            "I was making some of the\x01",
            "green tea Rixia gave me\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. This green tea has\x01",
            "a lovely smell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_3CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CE1")
    Jump("loc_4262")

    label("loc_3CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DCA")

    ChrTalk(
        0xFE,
        (
            "Just the unveiling\x01",
            "ceremony is left for\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, my\x01",
            "husband's workload has\x01",
            "finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow, I've got to burn\x01",
            "the image of my husband's\x01",
            "work into my memory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3E4D")

    label("loc_3DCA")


    ChrTalk(
        0xFE,
        (
            "The Orchis Tower\x01",
            "unveiling ceremony is\x01",
            "finally tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to burn the\x01",
            "image of my husband's\x01",
            "work into my memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4D")

    Jump("loc_4262")

    label("loc_3E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_403E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA3")

    ChrTalk(
        0xFE,
        (
            "My husband works at\x01",
            "construction sites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These past few months, he's been\x01",
            "working at the site of Orchis Tower\x01",
            "that everyone's been talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The interior's already complete.\x01",
            "All that's left are some finishing\x01",
            "touches on the exterior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm really looking\x01",
            "forward to its\x01",
            "completion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4039")

    label("loc_3FA3")


    ChrTalk(
        0xFE,
        (
            "The construction of Orchis Tower\x01",
            "is the biggest job my husband's\x01",
            "ever been involved in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm really looking\x01",
            "forward to its\x01",
            "completion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4039")

    Jump("loc_4262")

    label("loc_403E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4198")

    ChrTalk(
        0xFE,
        (
            "These past few years, state\x01",
            "congress considered a Downtown\x01",
            "redevelopment plan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the new congress\x01",
            "considered it, the plan\x01",
            "was officially frozen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't be happy when\x01",
            "I heard about the freeze,\x01",
            "but... I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this place was\x01",
            "demolished, our families\x01",
            "would have no place to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4262")

    label("loc_4198")


    ChrTalk(
        0xFE,
        (
            "I heard the congresspeople at the\x01",
            "heart of the plan were arrested due to\x01",
            "involvement with the cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, the plan\x01",
            "itself had many deficiencies,\x01",
            "which hindered discussions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4262")

    TalkEnd(0xFE)
    Return()

    # Function_14_3577 end

    def Function_15_4266(): pass

    label("Function_15_4266")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4284")
    Call(0, 16)
    Jump("loc_42FF")

    label("loc_4284")


    ChrTalk(
        0xFE,
        (
            "Even at a time like this,\x01",
            "papa's doing his best for\x01",
            "Rimah and Corona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, Rimah's got\x01",
            "to do her best too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42FF")

    Jump("loc_47A5")

    label("loc_4304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_435C")

    ChrTalk(
        0xFE,
        (
            "Both dad and mom look\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they're all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A5")

    label("loc_435C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_43A2")

    ChrTalk(
        0xFE,
        "Mom... She looks sad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want her to cheer up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47A5")

    label("loc_43A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_43B0")
    Jump("loc_47A5")

    label("loc_43B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4407")

    ChrTalk(
        0xFE,
        (
            "Rixia was down today,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A5")

    label("loc_4407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4418")
    Call(0, 11)
    Jump("loc_47A5")

    label("loc_4418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4429")
    Call(0, 12)
    Jump("loc_47A5")

    label("loc_4429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44FB")

    ChrTalk(
        0xFE,
        (
            "Mama and I saw papa off\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is his first day\x01",
            "of work at a new site,\x01",
            "so the time is flexible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rimah doesn't get it,\x01",
            "but is happy she got to\x01",
            "see him off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_454D")

    label("loc_44FB")


    ChrTalk(
        0xFE,
        (
            "Mama and Rimah gave papa\x01",
            "a goodbye kiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Papa was embarrassed and\x01",
            "cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_454D")

    Jump("loc_47A5")

    label("loc_4552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_45A7")

    ChrTalk(
        0xFE,
        (
            "Wonderland was really\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to go again with\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A5")

    label("loc_45A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45D9")

    ChrTalk(
        0xFE,
        (
            "Tea, tea♪ Tea with\x01",
            "everyone♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A5")

    label("loc_45D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_45E7")
    Jump("loc_47A5")

    label("loc_45E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_463C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4602")
    Call(0, 17)
    Jump("loc_4637")

    label("loc_4602")


    ChrTalk(
        0xFE,
        (
            "Here you go. I made food\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eat up♪\x02",
    )

    CloseMessageWindow()

    label("loc_4637")

    Jump("loc_47A5")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_470D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CB")

    ChrTalk(
        0xFE,
        (
            "Rimah's dad works at a\x01",
            "construction site every\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he'll be late\x01",
            "coming home again today.\x01",
            "Hmm...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4708")

    label("loc_46CB")


    ChrTalk(
        0xFE,
        (
            "I think papa'll be late\x01",
            "coming home again today.\x01",
            "Hmm...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4708")

    Jump("loc_47A5")

    label("loc_470D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_47A5")

    ChrTalk(
        0xFE,
        (
            "Mom's happy those corrupt\x01",
            "government officials\x01",
            "haven't been by lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but if mom's happy,\x01",
            "Rimah's happy too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A5")

    TalkEnd(0xFE)
    Return()

    # Function_15_4266 end

    def Function_16_47A9(): pass

    label("Function_16_47A9")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Papa, are you going to\x01",
            "work today, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah. The construction\x01",
            "site's reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Rimah, you must be\x01",
            "worried, but please watch\x01",
            "the house with your mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Papa, have a good day!\x01",
            "...*kiss*㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Haha. Off I go.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_47A9 end

    def Function_17_48C0(): pass

    label("Function_17_48C0")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alllright, Rimah. What\x01",
            "shall we play today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Then, "house", I\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rimah will be the mom so\x01",
            "you be the dad, dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha. Dad being the dad,\x01",
            "huh? I see. Roger that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_17_48C0 end

    def Function_18_4990(): pass

    label("Function_18_4990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AE")
    Call(0, 16)
    Jump("loc_4A43")

    label("loc_49AE")


    ChrTalk(
        0xFE,
        (
            "Iyahahaha... This is\x01",
            "embarrassing, but it is\x01",
            "uplifting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alllright! I was worried about\x01",
            "things, but... I'll work for\x01",
            "my family again today!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A43")

    Jump("loc_4C40")

    label("loc_4A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4AD2")

    ChrTalk(
        0xFE,
        (
            "It's become like this,\x01",
            "and I don't know what to\x01",
            "do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll protect Corona and\x01",
            "Rimah, no matter what\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C40")

    label("loc_4AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4AE0")
    Jump("loc_4C40")

    label("loc_4AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AEE")
    Jump("loc_4C40")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4AFC")
    Jump("loc_4C40")

    label("loc_4AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B0A")
    Jump("loc_4C40")

    label("loc_4B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B18")
    Jump("loc_4C40")

    label("loc_4B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4B26")
    Jump("loc_4C40")

    label("loc_4B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B34")
    Jump("loc_4C40")

    label("loc_4B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4BAD")

    ChrTalk(
        0xFE,
        (
            "*sigh*, it's been a\x01",
            "while since I passed\x01",
            "time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Happy families are\x01",
            "really great things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C40")

    label("loc_4BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4BBB")
    Jump("loc_4C40")

    label("loc_4BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")
    Call(0, 17)
    Jump("loc_4C24")

    label("loc_4BD6")


    ChrTalk(
        0xFE,
        "Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*... Yeah,\x01",
            "it's reall good again\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C24")

    Jump("loc_4C40")

    label("loc_4C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C37")
    Jump("loc_4C40")

    label("loc_4C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C40")

    label("loc_4C40")

    TalkEnd(0xFE)
    Return()

    # Function_18_4990 end

    def Function_19_4C44(): pass

    label("Function_19_4C44")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CC4")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, Dieter... Will\x01",
            "independence make you happy?\x01",
            "...*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5354")

    label("loc_4CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4CD2")
    Jump("loc_5354")

    label("loc_4CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D45")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Where is the nation of\x01",
            "dreams... Vaaan, take me\x01",
            "with youuu...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5354")

    label("loc_4D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DFF")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DBB")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*... Who\x01",
            "is it? Who's raining on\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Gotta pee soon...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4DFA")

    label("loc_4DBB")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x01",
            "What'll I do if I wet my\x01",
            "pants...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFA")

    Jump("loc_5354")

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E6A")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I don't have mira... to\x01",
            "stay overnight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I'm that kind of guy...\x01",
            "Ngoo...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5354")

    label("loc_4E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F4F")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F0B")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I finally got... a 1,000\x01",
            "mira bill...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "At the casino... Before\x01",
            "I knew it...\x01",
            "Penniless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4F4A")

    label("loc_4F0B")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "My mira... Give it\x01",
            "back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4A")

    Jump("loc_5354")

    label("loc_4F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5055")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF3")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Oh, Vaan! You've no\x01",
            "problem with this,\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Your breadwinner...\x01",
            "Worked... Ooh, *hic*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5050")

    label("loc_4FF3")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Your breadwinner...\x01",
            "Worked...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "But please wait on the\x01",
            "rent... Ooh, *hic*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5050")

    Jump("loc_5354")

    label("loc_5055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_516D")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5115")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*snore*... Hah? Oh, I've\x01",
            "got some alcohol. Nice\x01",
            "work, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug, glug*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Bleargh!? *spit\x01",
            "spit...*! The fuck is\x01",
            "this, this isn't booze!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5168")

    label("loc_5115")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Just who did this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "You won't get away with\x01",
            "this... *munyanya*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5168")

    Jump("loc_5354")

    label("loc_516D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5250")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FA")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Huh? No mira, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "No choice, then... I'll\x01",
            "have to get a job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_524B")

    label("loc_51FA")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "No choice, then... I'll\x01",
            "have to get a job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_524B")

    Jump("loc_5354")

    label("loc_5250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52AA")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Drink, drink, my best\x01",
            "friend, drink!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5354")

    label("loc_52AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_52FC")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, Vaan! Where's my\x01",
            "drink!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5354")

    label("loc_52FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5354")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*... *snore*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Drink, drink... ...Bring\x01",
            "me some drink!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5354")

    TalkEnd(0x14)
    Return()

    # Function_19_4C44 end

    def Function_20_5358(): pass

    label("Function_20_5358")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x01",
            "A voice can be heard\x01",
            "inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_20_5358 end

    def Function_21_539D(): pass

    label("Function_21_539D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53BC")
    Call(0, 9)
    Jump("loc_542E")

    label("loc_53BC")


    ChrTalk(
        0x9,
        (
            "Most importantly, I'm\x01",
            "glad you're doing well\x01",
            "yourself, Tantos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly, I'm thankful\x01",
            "to everyone here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542E")

    Jump("loc_54AC")

    label("loc_5433")


    ChrTalk(
        0x9,
        (
            "I'll absolutely submit\x01",
            "my notice of move-out\x01",
            "before the day is out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sorry for putting you\x01",
            "through all of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AC")

    TalkEnd(0xFE)
    Return()

    # Function_21_539D end

    def Function_22_54B0(): pass

    label("Function_22_54B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552B")

    ChrTalk(
        0xFE,
        "Huh? Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's some time until\x01",
            "the emergency feeding, so\x01",
            "please wait until then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_552B")

    OP_4B(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "Now then. Next is to\x01",
            "decide on tonight's\x01",
            "emergency feeding menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That's right. I wonder\x01",
            "what would be good.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0x0)

    label("loc_55A9")

    TalkEnd(0xFE)
    Return()

    # Function_22_54B0 end

    def Function_23_55AD(): pass

    label("Function_23_55AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_563E")

    ChrTalk(
        0xFE,
        (
            "(When I think he's depressed\x01",
            "because he hasn't gotten any\x01",
            "alcohol lately...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Disgusting... This\x01",
            "ain't my old man...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_568E")

    label("loc_563E")


    ChrTalk(
        0xFE,
        (
            "Kyahaha. Old man, you'll run\x01",
            "out of money for drinking\x01",
            "before long, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_568E")

    TalkEnd(0xFE)
    Return()

    # Function_23_55AD end

    def Function_24_5692(): pass

    label("Function_24_5692")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56A3")
    Jump("loc_5737")

    label("loc_56A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_56E2")

    ChrTalk(
        0xFE,
        (
            "(*chuckle*... He's\x01",
            "better when he's drunk.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5737")

    label("loc_56E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_56F0")
    Jump("loc_5737")

    label("loc_56F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5737")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Then you'll\x01",
            "need a way to make money\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5737")

    TalkEnd(0xFE)
    Return()

    # Function_24_5692 end

    def Function_25_573B(): pass

    label("Function_25_573B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576E")
    Call(0, 31)
    Return()

    label("loc_576E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x135, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x136, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x13B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x143, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x146, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x147, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x13A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57DC")
    Call(0, 33)
    Return()

    label("loc_57DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_5AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_END)), "loc_5AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_5870")

    ChrTalk(
        0x13,
        (
            "Yeah. If I just had\x01",
            "these ingredients, I\x01",
            "think I'd have enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Thanks. These 'll make\x01",
            "everyone happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB2")

    label("loc_5870")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                       # 0
            "Ask About Ingredients\x01",      # 1
            "Cancel\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A25")

    ChrTalk(
        0x13,
        (
            "Oh, you need to check\x01",
            "the necessary\x01",
            "ingredients?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "First, [Five-Colored\x01",
            "Miso] x10. Then, [Beast\x01",
            "Flesh] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, [All-Curing Sake]\x01",
            "x10, then [Sesame Oil]\x01",
            "x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "And, [Dark Mushroom] x30\x01",
            "and [All-Purpose Onion]\x01",
            "x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally, [Petit Carrot]\x01",
            "x30 and [Hot Pepper]\x01",
            "x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That's everything.\x01",
            "Thanks in advance for\x01",
            "all your help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB2")

    label("loc_5A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB2")

    ChrTalk(
        0x13,
        (
            "The emergency feeding\x01",
            "menu is precisely "Pork\x01",
            "Miso Soup".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It has meat, veggies and\x01",
            "the perfect nutritional\x01",
            "balance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB2")

    Jump("loc_5B1D")

    label("loc_5AB7")


    ChrTalk(
        0x13,
        (
            "Hmm. Even this amount\x01",
            "was gone in the blink of\x01",
            "an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I wonder if I can dilute\x01",
            "it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B1D")

    TalkEnd(0xFE)
    Return()

    # Function_25_573B end

    def Function_26_5B21(): pass

    label("Function_26_5B21")

    TalkBegin(0xFE)
    OP_4B(0x15, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BED")

    ChrTalk(
        0x15,
        (
            "Listen up Vaan, and you\x01",
            "young lady as well. Stay\x01",
            "in your rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Daddy will protect his\x01",
            "only son, and his\x01",
            "friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "(He looks happy...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5C52")

    label("loc_5BED")


    ChrTalk(
        0x15,
        (
            "Listen up Vaan, and you\x01",
            "young lady as well. I'll\x01",
            "definitely protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "(How annoying...)\x02",
    )

    CloseMessageWindow()

    label("loc_5C52")

    OP_4C(0x15, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_5B21 end

    def Function_27_5C5E(): pass

    label("Function_27_5C5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C73")
    Call(0, 28)
    Jump("loc_5DDB")

    label("loc_5C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4F")

    ChrTalk(
        0xF,
        (
            "#01803FNow then, I've got to\x01",
            "get ready to go to City\x01",
            "Hall...\x02\x03",
            "#01802FEveryone, thanks for the\x01",
            "warning about Shirley.\x02\x03",
            "#01806FI have a lot of skinship\x01",
            "with Ilya too, but...\x01",
            "I'll be careful somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5DDB")

    label("loc_5D4F")


    ChrTalk(
        0xF,
        (
            "#01802FEveryone, thanks for the\x01",
            "warning about Shirley.\x02\x03",
            "#01806FI have a lot of skinship\x01",
            "with Ilya too, but...\x01",
            "I'll be careful somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDB")

    TalkEnd(0xFE)
    Return()

    # Function_27_5C5E end

    def Function_28_5DDF(): pass

    label("Function_28_5DDF")

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
        "#01802FAh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FHey Rixia. You've\x01",
            "returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802FYes. I have business at\x01",
            "City Hall this afternoon,\x01",
            "so I'm resting.\x02\x03",
            "Ah... It looks like Tio's\x01",
            "finally back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, I returned to the Support\x01",
            "Section yesterday.\x02\x03",
            "#00204FI heard Arc-en-Ciel gave a\x01",
            "performance for the heads of state\x01",
            "last night... That was great work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHaha, were you nervous?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FAhaha. That performance had a\x01",
            "feeling a little different from\x01",
            "our usual ones.\x02\x03",
            "#01804FThough it was a minor role,\x01",
            "Sully made her first appearance,\x01",
            "and she was really nervous...\x02\x03",
            "#01802FIlya was the same as usual,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHaha. I can't imagine\x01",
            "Ilya ever being nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01804FYes. When it comes to the\x01",
            "stage, Ilya is\x01",
            "straightforward...\x02\x03",
            "#01802FHaha. I've felt like\x01",
            "someone like me is no match\x01",
            "for her this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FHmm. For an artist,\x01",
            "that's a super high\x01",
            "benchmark, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. The so-called true\x01",
            "genius of a star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FBut, I feel like you will\x01",
            "definitely overtake Ilya one\x01",
            "day, Rixia.\x02\x03",
            "#00004FIt was pretty amazing how you\x01",
            "caught the kitten that fell\x01",
            "from the chandelier yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FAhaha... Thank you very\x01",
            "much.\x02\x03",
            "#01802FBut really... It was\x01",
            "because my body moved on\x01",
            "its own...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01803FBy the way, that girl\x01",
            "yesterday... Shirley was\x01",
            "her name, right?\x02\x03",
            "#01802FI heard she was Randy's\x01",
            "cousin, but... What kind\x01",
            "of person is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FU-Umm...\x02\x03",
            "#00003F(I can't say something\x01",
            "careless and involve\x01",
            "Rixia, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F...Haha. If I had to say, she a\x01",
            "tomboy who does whatever she\x01",
            "likes.\x02\x03",
            "#00302FIt's just, a while back, she got\x01",
            "something good because she tangled\x01",
            "with a troublesome fellow.\x02\x03",
            "#00309FSomehow, it looks like you're\x01",
            "quite taken with her, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. If you're not careful,\x01",
            "she might put you through the\x01",
            "same thing she did to Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00113FE-Enough... Please,\x01",
            "forget that already.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01808F(Bloody Shirley...)\x02\x03",
            "#01803F(Most likely, I will\x01",
            "deal with her as Yin in\x01",
            "the future...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F...Umm, Rixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802F...Haha, it's nothing.\x01",
            "Thanks for the warning.\x02\x03",
            "#01806FI have a lot of skinship\x01",
            "with Ilya too, but...\x01",
            "I'll be careful somehow.\x02",
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
        "#12P#10112FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FYou must have it tough,\x01",
            "Rixia.\x02",
        )
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

    # Function_28_5DDF end

    def Function_29_6886(): pass

    label("Function_29_6886")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68B4")
    Call(0, 34)
    Return()

    label("loc_68B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68DD")
    Call(0, 30)
    Return()

    label("loc_68DD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_68EE")
    Jump("loc_6999")

    label("loc_68EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6924")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6999")

    label("loc_6924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6932")
    Jump("loc_6999")

    label("loc_6932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6968")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6999")

    label("loc_6968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6999")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6999")

    TalkEnd(0xFF)
    Return()

    # Function_29_6886 end

    def Function_30_699D(): pass

    label("Function_30_699D")

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
            "#6P#00000FDowntown, Lotus\x01",
            "Heights.... Yeah, this\x01",
            "is the place.\x02",
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
            "#6P#00000FExcuse me, is anyone\x01",
            "there?\x02",
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
        "#6P#10103FNo answer, huh?\x02",
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
            "#11P#00001FYeah, it's bolted tight.\x02\x03",
            "#00003FI feel a slight\x01",
            "presence, but it might\x01",
            "just be my imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FMaybe the resident is\x01",
            "pretending not to be\x01",
            "home.\x02\x03",
            "#10300FSo what do we do? Force\x01",
            "our way in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FWell, if we have no\x01",
            "other options, we can\x01",
            "consider it, but...\x02",
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
        "#6P#10105FWhat was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FIt sounded like dishes\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FIt's looking more likely\x01",
            "that they're pretending\x01",
            "not to be home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FLet's try calling out\x01",
            "again.\x02\x03",
            "#00001FExcuse me! Is anyone\x01",
            "there!?\x02\x03",
            "Can you please say\x01",
            "something!?\x02",
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
            "#6P#10304FHaha, to the bitter end,\x01",
            "huh.\x02\x03",
            "#10302FMaybe they escaped\x01",
            "through the window?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHmm, that would be a\x01",
            "rather dangerous.\x02",
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

    def lambda_6F78():
        OP_95(0x9, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F78)
    Sleep(100)

    def lambda_6F95():
        OP_95(0x8, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6F95)
    Sleep(100)
    WaitChrThread(0x9, 1)

    def lambda_6FB6():
        OP_95(0x9, 3060, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FB6)
    Sleep(100)
    WaitChrThread(0x8, 1)

    def lambda_6FD7():
        OP_95(0x8, 4059, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6FD7)
    WaitChrThread(0x9, 1)

    def lambda_6FF5():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FF5)
    WaitChrThread(0x8, 1)
    Sleep(100)

    def lambda_7009():
        OP_93(0x8, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7009)
    WaitChrThread(0x8, 1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#12PI heard a bunch of\x01",
            "yelling... Is this your\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PWhat's going on here?\x02",
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

    def lambda_70D0():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70D0)
    Sleep(10)

    def lambda_70E0():
        OP_93(0x102, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70E0)
    Sleep(10)

    def lambda_70F0():
        OP_93(0x109, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_70F0)
    Sleep(10)

    def lambda_7100():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7100)
    Sleep(10)

    ChrTalk(
        0x101,
        (
            "#5P#00005FOh right, excuse us.\x02\x03",
            "#00000FWe're with the Crossbell\x01",
            "Police Special Support\x01",
            "Section.\x02\x03",
            "#00003FWe have business with\x01",
            "the resident of this\x01",
            "apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105FDo either of you know\x01",
            "the resident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYeah, of course we do.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x0)

    ChrTalk(
        0x9,
        (
            "#12PCare to tell us the\x01",
            "situation, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that\x01",
            "they were investigating\x01",
            "suspicious addresses.\x02",
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
            "#12PI see. So you need to\x01",
            "identify the resident of\x01",
            "this unit, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PHmm. I'm not sure how to\x01",
            "say it, but I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FHuh? What do you mean?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x0)

    ChrTalk(
        0x9,
        (
            "#12PWell, to tell you the truth,\x01",
            "I'm Geithner, the previous\x01",
            "resident of this room.\x02",
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
        "#5P#00005FI-Is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PYes. But I didn't submit\x01",
            "the residence change\x01",
            "notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PAnd now it's late, I'm\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI know, ok? I'll be sure\x01",
            "to submit it by the end\x01",
            "of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, that would really\x01",
            "help us out.\x02\x03",
            "#00103FBy the way, would you\x01",
            "mind telling us your\x01",
            "reason for moving out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PRight... This must be\x01",
            "what they call "fate".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI wound up here in the first place\x01",
            "because, as a trader, I made a\x01",
            "huge blunder about a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PAfter learning about my situation,\x01",
            "one of my fellow traders asked me\x01",
            "to come help with his business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PAnd so, I accepted their\x01",
            "offer and moved to the\x01",
            "Republic two weeks ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FThen, why are you here\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI wanted to thank again everyone\x01",
            "in this apartment, who supported\x01",
            "me in that difficult time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PYou all helped me so\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHoho. How thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FI see. I think I\x01",
            "understand your\x01",
            "situation, Mr. Geithner.\x02\x03",
            "#00000FThen, I want to ask you\x01",
            "again about the current\x01",
            "resident.\x02",
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
            "#5P#00105F...Is there some\x01",
            "situation that's\x01",
            "difficult to explain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAh, well I think the\x01",
            "problem lies in the heart\x01",
            "of the new resident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_78E9():
        OP_9B(0x1, 0x8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_78E9)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_7905():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7905)
    Sleep(50)

    def lambda_791D():
        OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_791D)
    Sleep(50)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_793C():
        OP_9B(0x1, 0x109, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_793C)
    Sleep(50)

    def lambda_7954():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7954)
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
            "#6PThis is Tantos. Are you\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you can hear me, open\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThere are police here.\x01",
            "We won't do anything.\x02",
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
        (
            "#6POh, looks like it's\x01",
            "open.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PAlright, now don't cause\x01",
            "a ruckus and just\x01",
            "cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FRight, thank you for\x01",
            "your cooperation.\x02",
        )
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

    def lambda_7BF7():
        OP_95(0x101, 51800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BF7)

    def lambda_7C11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C11)
    Sleep(500)

    def lambda_7C25():
        OP_95(0x102, 51800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C25)

    def lambda_7C3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C3F)
    Sleep(500)

    def lambda_7C53():
        OP_95(0x109, 50800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C53)

    def lambda_7C6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C6D)
    Sleep(500)

    def lambda_7C81():
        OP_95(0x105, 50800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C81)

    def lambda_7C9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C9B)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_7CB3():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CB3)
    WaitChrThread(0x102, 1)

    def lambda_7CC4():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CC4)
    WaitChrThread(0x109, 1)

    def lambda_7CD5():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7CD5)
    WaitChrThread(0x105, 1)

    def lambda_7CE6():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7CE6)

    ChrTalk(
        0x101,
        "#6P#00000F─Excuse us...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        (
            "#11PAre you here to make fun\x01",
            "of me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    NpcTalk(
        0xA,
        "???",
        (
            "#11PI said, "Are you here to\x01",
            "make fun of me!?"\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        (
            "#11PI'm Geval! I was once a\x01",
            "glorious congressperson, but\x01",
            "now I've lost everything!\x02",
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
        "#6P#00011FT-This guy is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F...Representative Geval of\x01",
            "the Imperial faction.\x02\x03",
            "#00101FWeren't you holed up at St.\x01",
            "Ursula Hospital ever since\x01",
            "your misdeeds came to light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PS-So you do know of me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell you've found me.\x01",
            "What are you going to do\x01",
            "with me now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI don't have any money,\x01",
            "as you can see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PEven the rent for this apartment...\x01",
            "I somehow managed to get it through\x01",
            "an old acquaintance of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POr are you trying to use\x01",
            "me for something?\x02",
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
            "#6P#00106FN-No, nothing of the\x01",
            "sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe just came to see who\x01",
            "exactly is living here.\x02\x03",
            "#00003FSo you're definitely the\x01",
            "new resident, Geval?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PUh, yeah... That's\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThen that's all we need\x01",
            "to know.\x02\x03",
            "#10100FThere isn't any criminal\x01",
            "activity so everything\x01",
            "should be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FBut why would you write the name of\x01",
            "that fairy tale author on your\x01",
            "residence change notice?\x02\x03",
            "#10300FIt's way too suspicious. I think it\x01",
            "attracts a lot of attention, contrary\x01",
            "to what you probably intended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThis address did look the\x01",
            "most suspicious out of all\x01",
            "of them, by the look of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHmm....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI've always been a big\x01",
            "fan of Sean Alnam's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PSo when I had to pick a\x01",
            "name, I came up with his\x01",
            "on the spur of the moment!\x02",
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
        "#6P#10112F...How unexpected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FW-Well, it's true that\x01",
            "Sean Alnam is read by\x01",
            "people of all ages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, I wonder if this\x01",
            "is what they call "gap\x01",
            "moe".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FR-Really?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PHey! Shut up already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf you got what you\x01",
            "needed, get out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FR-Right, excuse us.\x02\x03",
            "#00100FWell then Lloyd, let's\x01",
            "get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRight.\x02\x03",
            "Excuse us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1400", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_699D end

    def Function_31_85EB(): pass

    label("Function_31_85EB")

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
        "#10300FYo, Azel.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x13,
        "Ah, Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Could it be that you're\x01",
            "here to help out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like you're getting\x01",
            "ready for the emergency food\x01",
            "distribution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIs there anything we can\x01",
            "help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Yeah, hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Umm... Actually, we're\x01",
            "short of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If possible, I'd like\x01",
            "you to buy them for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FA shopping trip. Well\x01",
            "that sounds easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FSo, what exactly do you\x01",
            "need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Alright, be sure to\x01",
            "write this down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "First, [Five-Colored\x01",
            "Miso] x10. Then, [Beast\x01",
            "Flesh] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, [All-Curing Sake]\x01",
            "x10, then [Sesame Oil]\x01",
            "x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "And, [Dark Mushroom] x30\x01",
            "and [All-Purpose Onion]\x01",
            "x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally, [Petit Carrot]\x01",
            "x30 and [Hot Pepper]\x01",
            "x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "―That's everything.\x02",
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
        (
            "#10106FThat's a huge amount of\x01",
            "stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yeah, it's enough for\x01",
            "everyone to eat well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It was a bit of a problem\x01",
            "yesterday because we\x01",
            "didn't have quite enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So today, I don't want\x01",
            "to run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBy the way, what dish\x01",
            "are you making?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            ""Pork Miso Soup"― It\x01",
            "warms the body and soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'll treat all of you to\x01",
            "some when it's done, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, I'll be looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh yeah, I almost\x01",
            "forgot.\x02",
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
            "500 mira\x07\x00",
            " received.\x02",
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
            "#00306FHmm, how to say this...\x01",
            "That's not enough not\x01",
            "matter how you slice it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Sorry 'bout that. The\x01",
            "budget is really tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "You guys want to help,\x01",
            "but this is all we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, we'll donate the\x01",
            "rest of the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes. The situation being\x01",
            "what it is, it's the\x01",
            "least we could do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10300FHaha, well if that's how\x01",
            "it's going to be, then\x01",
            "let's get to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00000FYeah. Let's go shopping.\x02",
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

    # Function_31_85EB end

    def Function_32_8E77(): pass

    label("Function_32_8E77")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9172")

    ChrTalk(
        0x8,
        (
            "Hmm, it's you guys. You're helping\x01",
            "us by supplying ingredients for\x01",
            "the emergency feeding, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, thanks. Sorry, but\x01",
            "we're counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, yes― If it's all\x01",
            "right with you, I have a\x01",
            "request related to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The concentrated extract\x01",
            "of acerbic tomato...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you can get that\x01",
            "somewhere, I'd like you\x01",
            "to bring it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do, I'll be able to treat\x01",
            "everyone to my special "Robust\x01",
            "Acerbic Tomato Pork Miso".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExtract, you say... Are\x01",
            "Acerbic Tomatoes\x01",
            "themselves no good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Preparing them for\x01",
            "cooking takes a lot of\x01",
            "time, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that's only if you have\x01",
            "time. It's not like it's a\x01",
            "problem if you can't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAlright, we'll remember\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 2)
    OP_29(0x8E, 0x1, 0x3)
    Jump("loc_9297")

    label("loc_9172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_91FC")

    ChrTalk(
        0xFE,
        (
            "Oh, it looks like you've\x01",
            "brought the item I\x01",
            "requested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm, thanks. With this,\x01",
            "I'll be able to cheer\x01",
            "everyone up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9297")

    label("loc_91FC")


    ChrTalk(
        0x8,
        (
            "The concentrated extract\x01",
            "of acerbic tomato...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you can get that\x01",
            "somewhere, I'd like you\x01",
            "to bring it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, only if if you\x01",
            "have time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9297")

    TalkEnd(0x8)
    Return()

    # Function_32_8E77 end

    def Function_33_929B(): pass

    label("Function_33_929B")

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
            "Ah, you got all of our\x01",
            "ingredients, right?\x02",
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
            "Hand them over\x01",      # 0
            "Refuse\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946A")

    ChrTalk(
        0x13,
        (
            "Oh, could it be that you\x01",
            "don't have them together\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "In that case, speak with\x01",
            "me again once you're\x01",
            "ready.\x02",
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

    label("loc_946A")


    ChrTalk(
        0x101,
        "#00000FYeah, here you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#20I[Five-Colored Miso] x10\x01\x07\x02",
            "#20I[Beast Flesh] x10\x01\x07\x02",
            "#20I[All-Curing Sake] x10\x01\x07\x02",
            "#20I[Sesame Oil] x10\x01\x07\x02",
            "#20I[Dark Mushroom] x30\x01\x07\x02",
            "#20I[All-Purpose Onion] x30\x01\x07\x02",
            "#20I[Petit Carrot] x30\x01\x07\x02",
            "#20I[Hot Pepper] x30 handed over.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    SubItemNumber(0x135, 10)
    SubItemNumber(0x12C, 10)
    SubItemNumber(0x136, 10)
    SubItemNumber(0x13B, 10)
    SubItemNumber(0x143, 30)
    SubItemNumber(0x146, 30)
    SubItemNumber(0x147, 30)
    SubItemNumber(0x13A, 30)

    ChrTalk(
        0x13,
        (
            "Yeah, everything's here,\x01",
            "just like I said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Nice work guys. And\x01",
            "thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x340, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9806")
    OP_2C(0x8E, 0x1)

    ChrTalk(
        0x103,
        (
            "#00205FCome to think of it,\x01",
            "Lloyd... Should we give\x01",
            "Azel that, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FOh, that's right.\x02\x03",
            "#00000FPlease take this, too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x340),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x340, 1)

    ChrTalk(
        0x13,
        "This is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, Tantos asked us to\x01",
            "get it for him.\x02\x03",
            "#10302FWe're told you're making\x01",
            "a special kind of pork\x01",
            "miso?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yeah, I guess. He did\x01",
            "say something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Well then, I better ask\x01",
            "Tantos before using it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 4)

    label("loc_9806")


    ChrTalk(
        0x104,
        (
            "#00300FThen, is that about it\x01",
            "for your help request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yeah. Nice work you\x01",
            "guys. This is gonna be a\x01",
            "huge help to all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'll start distributing\x01",
            "it to everyone during a\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The Support Section is\x01",
            "welcome to some too, if\x01",
            "you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAlright. We'll take you\x01",
            "up on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99BD")

    ChrTalk(
        0x101,
        (
            "#00004FWe'll leave it to you,\x01",
            "then.\x02\x03",
            "#00000FWe're done helping\x01",
            "everyone, so let's go\x01",
            "report to Abbas.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_9A0D")

    label("loc_99BD")


    ChrTalk(
        0x101,
        (
            "#00004FWe'll leave it to you,\x01",
            "then.\x02\x03",
            "#00000FLet's see who else needs\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A0D")

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

    # Function_33_929B end

    def Function_34_9A47(): pass

    label("Function_34_9A47")

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
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Geval, are you\x01",
            "there?\x02",
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
        "#00003F...Looks like he's out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThere's no mistake. This\x01",
            "is definitely Geval's\x01",
            "apartment.\x02",
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
        "What are you guys doing?\x02",
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

    def lambda_9D35():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D35)
    Sleep(50)

    def lambda_9D45():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D45)
    Sleep(50)

    def lambda_9D55():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D55)
    Sleep(50)

    def lambda_9D65():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D65)
    Sleep(50)

    def lambda_9D75():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9D75)
    Sleep(50)

    def lambda_9D85():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D85)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Oh... You're the Special\x01",
            "Support Section from\x01",
            "back then, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3630, 1300, 2880, 2000)
    OP_95(0x8, 3800, 0, 1500, 1500, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        (
            "#10302FHaha... Hello, Tantos.\x02\x03",
            "Do you know where the\x01",
            "representative who lives\x01",
            "here went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I think he left\x01",
            "about a week ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is there some kind of\x01",
            "incident involving him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they\x01",
            "were searching for Geval\x01",
            "due to Alm's request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, so that couple came\x01",
            "all the way from Liberl,\x01",
            "did they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho, that Geval is one\x01",
            "lucky fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FDo you know Alm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He visited my apartment\x01",
            "this past week. We\x01",
            "talked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, but it seems Geval\x01",
            "went off somewhere after\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I didn't ask where he\x01",
            "was going...\x02",
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
        "#10106FThat's a problem...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, come to think of\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There might be someone\x01",
            "who does know where he\x01",
            "went.\x02",
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
            "Yes. There's a certain character\x01",
            "from West Street who helped him\x01",
            "when he was a congressman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even after Geval moved\x01",
            "here, he went to see him\x01",
            "many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Vil, Villa... Villa-\x01",
            "something, that's the name of\x01",
            "the apartment where he lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FVilla something, huh...\x01",
            "I feel like I've heard\x01",
            "that before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, let's search the\x01",
            "buildings on West\x01",
            "Street.\x02\x03",
            "#00000FThanks for your\x01",
            "cooperation, Tantos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, don't mention\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please help Geval and\x01",
            "that couple find each\x01",
            "other.\x02",
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

    # Function_34_9A47 end

    SaveToFile()

Try(main)
