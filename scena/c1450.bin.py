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
        "Function_7_1CD8",         # 07, 7
        "Function_8_1E57",         # 08, 8
        "Function_9_1FE8",         # 09, 9
        "Function_10_2119",        # 0A, 10
        "Function_11_2FA0",        # 0B, 11
        "Function_12_319A",        # 0C, 12
        "Function_13_334F",        # 0D, 13
        "Function_14_36A9",        # 0E, 14
        "Function_15_43C4",        # 0F, 15
        "Function_16_4902",        # 10, 16
        "Function_17_4A17",        # 11, 17
        "Function_18_4AEE",        # 12, 18
        "Function_19_4D9E",        # 13, 19
        "Function_20_54EE",        # 14, 20
        "Function_21_5533",        # 15, 21
        "Function_22_5646",        # 16, 22
        "Function_23_5743",        # 17, 23
        "Function_24_582B",        # 18, 24
        "Function_25_58D1",        # 19, 25
        "Function_26_5CB8",        # 1A, 26
        "Function_27_5DF2",        # 1B, 27
        "Function_28_5F8E",        # 1C, 28
        "Function_29_6A7C",        # 1D, 29
        "Function_30_6B93",        # 1E, 30
        "Function_31_8880",        # 1F, 31
        "Function_32_9137",        # 20, 32
        "Function_33_956E",        # 21, 33
        "Function_34_9D35",        # 22, 34
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BE9")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think the character who supported\x01",
            "Mr. Geval when he was a\x01",
            "congressman lives on West Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I recall, Vil, Villa...\x01",
            ""Villasomething" is the name\x01",
            "of the building where he lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He might know Mr.\x01",
            "Geval's whereabouts.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C12")
    Call(0, 32)
    Return()

    label("loc_C12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4D")

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
            "square and they were hard to approach.\x01",
            "but we can really rely on those youngsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like this is the first time\x01",
            "Downtown has become one since I came here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DFE")

    label("loc_D4D")


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
            "I feel like this is the first time\x01",
            "Downtown has become one since I came here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFE")

    Jump("loc_1CD4")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E8A")

    ChrTalk(
        0xFE,
        (
            "Just what is that\x01",
            "blue mist outside...?\x02",
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
    Jump("loc_1CD4")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

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
            "I understand his opinion, but...\x01",
            "Is there really no peaceful \x01",
            "way of solving this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F8F")

    label("loc_F27")


    ChrTalk(
        0xFE,
        "I understand the President's opinion, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is there really no peaceful\x01",
            "way of solving this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8F")

    Jump("loc_1CD4")

    label("loc_F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_1056")

    ChrTalk(
        0x8,
        (
            "Once you've thoroughly cooked\x01",
            "veggies, you start flavoring them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""Robust Acerbic Tomato Pork Miso Soup"...\x01",
            "Please wait it in anticipation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_1056")


    ChrTalk(
        0x8,
        (
            "Now then, time to get the\x01",
            "emergency feeding bowls ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm making this for everyone today.\x02",
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jump("loc_117A")

    label("loc_10C2")


    ChrTalk(
        0x8,
        (
            "As for the emergency feeding,\x01",
            "we'll be doing it in this room\x01",
            "and in Mrs. Corona's room too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The quantity is what it is. \x01",
            "I have supplies in the kitchen,\x01",
            "but it's not enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_1209")

    label("loc_117F")


    ChrTalk(
        0xFE,
        (
            "Hoh hoh! Most importantly,\x01",
            "everyone ate the pork miso soup\x01",
            "and thought it was delicious.\x02",
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

    label("loc_1209")

    Jump("loc_1CD4")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D6")

    ChrTalk(
        0xFE,
        (
            "Yesterday evening,\x01",
            "Mr. Geval had a\x01",
            "rare visitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's looked strange\x01",
            "ever since then.\x02",
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
    Jump("loc_1323")

    label("loc_12D6")


    ChrTalk(
        0xFE,
        (
            "He said he's being chased\x01",
            "by someone, but... Hmm,\x01",
            "I'm a little worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1323")

    Jump("loc_1CD4")

    label("loc_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1388")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Geval\x01",
            "too is getting used to\x01",
            "life here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hoh hoh, splendid.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CD4")

    label("loc_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(
        0xFE,
        (
            "*shock*... Mr. Geval's cooked\x01",
            "beans are a true masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh ho, I was planning to\x01",
            "save them up for dinner,\x01",
            "but I ate them all immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14F8")

    label("loc_143C")


    ChrTalk(
        0xFE,
        (
            "But most importantly, it seems\x01",
            "Mr. Geval is opening his heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Mr. Geval was prideful during\x01",
            "his time as congressman, but it seems\x01",
            "his true nature is that of a nice man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F8")

    Jump("loc_1CD4")

    label("loc_14FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_150E")
    Call(0, 7)
    Jump("loc_1CD4")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161E")

    ChrTalk(
        0xFE,
        (
            "Crossbell State, huh... \x01",
            "Our claim is legitimate, but I\x01",
            "feel our greed is excessive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two major powers won't look\x01",
            "kindly on this. I can't think\x01",
            "things will proceed peacefully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Mayor Dieter\x01",
            "has made a bold proposal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_169B")

    label("loc_161E")


    ChrTalk(
        0xFE,
        (
            "Crossbell State, huh... \x01",
            "I can't think this will go peacefully...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Mayor Dieter\x01",
            "has made a bold proposal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169B")

    Jump("loc_1CD4")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_173F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BB")
    Call(0, 8)
    Jump("loc_173A")

    label("loc_16BB")


    ChrTalk(
        0xFE,
        "Hm, hm. I see.\x02",
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

    label("loc_173A")

    Jump("loc_1CD4")

    label("loc_173F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185F")

    ChrTalk(
        0xFE,
        (
            "The unveiling ceremony, huh... \x01",
            "There's a big hullabaloo in the city about it.\x02",
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
    Jump("loc_18E4")

    label("loc_185F")


    ChrTalk(
        0xFE,
        (
            "Anyway, it seems Mr. \x01",
            "Geval is holed up as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess I'll knock on his door \x01",
            "again and listen to his grumbles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E4")

    Jump("loc_1CD4")

    label("loc_18E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19AD")

    ChrTalk(
        0xFE,
        (
            "Patrol officers are coming to\x01",
            "Downtown tomorrow on account\x01",
            "of the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not like the heads\x01",
            "of state would even visit a\x01",
            "desolate place like this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD4")

    label("loc_19AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D2")
    Call(0, 9)
    Jump("loc_1A1E")

    label("loc_19D2")


    ChrTalk(
        0xFE,
        (
            "Hmm. I'm glad you're\x01",
            "doing well, Geithner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It makes me happy too.\x02",
    )

    CloseMessageWindow()

    label("loc_1A1E")

    Jump("loc_1AA5")

    label("loc_1A23")


    ChrTalk(
        0xFE,
        (
            "Everyone, please, could\x01",
            "you leave Mr. Geval be?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of things have happened to him,\x01",
            "and it seems he can't find rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA5")

    Jump("loc_1CD4")

    label("loc_1AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1B")

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
            "us grabbed hold of success\x01",
            "after leaving this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh hoh, it's certainly true\x01",
            "that all manner of lives\x01",
            "are packed into here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CD4")

    label("loc_1C1B")


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
            "Hoh hoh, it's certainly true\x01",
            "that all manner of lives\x01",
            "are packed into here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD4")

    TalkEnd(0xFE)
    Return()

    # Function_6_AE8 end

    def Function_7_1CD8(): pass

    label("Function_7_1CD8")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCB")

    ChrTalk(
        0x8,
        (
            "*crunch, munch*...\x01",
            "Ooh, this is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Did you make these beans, Mr. Geval?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. I was a cook\x01",
            "awhile back, so I\x01",
            "tried making them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just glad\x01",
            "you like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoh hoh, thanks for\x01",
            "the trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E4E")

    label("loc_1DCB")


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
            "I'm sure everyone\x01",
            "will love them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-You think so...?\x02",
    )

    CloseMessageWindow()

    label("loc_1E4E")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_1CD8 end

    def Function_8_1E57(): pass

    label("Function_8_1E57")


    ChrTalk(
        0xA,
        "L-Listen to me, Mr. Tantos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was full of hopes too when\x01",
            "I was in my newbie days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoh hoh. I've heard that story\x01",
            "many times. I believe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You were thinking of changing this\x01",
            "city to suit your own style, right?\x02",
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
            "But one day, a certain Imperial\x01",
            "faction congressman came to me and...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_1E57 end

    def Function_9_1FE8(): pass

    label("Function_9_1FE8")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "Oh, Geithner. \x01",
            "Glad you're doing well.\x02",
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
            "everything's going smoothly.\x02",
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
            "Let's have some\x01",
            "tea right away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_9_1FE8 end

    def Function_10_2119(): pass

    label("Function_10_2119")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2465")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228A")

    ChrTalk(
        0xFE,
        (
            "Because of an arrangement with the Guild,\x01",
            "I could speak with Alm and Aerie in Liberl \x01",
            "using their international communicator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there's chaos in Liberl too, but it's\x01",
            "peaceful compared to the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chaos is Crossbell has been\x01",
            "going on for awhile... I'm glad\x01",
            "I was able to hear from them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2322")

    label("loc_228A")


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
            "going on for awhile... That's\x01",
            "why I have to do my best too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2322")

    Jump("loc_2460")

    label("loc_2327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F4")

    ChrTalk(
        0xFE,
        (
            "Just when the President was arrested,\x01",
            "that strange, huge tree appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I had just one wish, it would be\x01",
            "to get through this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O Goddess, please save me...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2460")

    label("loc_23F4")


    ChrTalk(
        0xFE,
        (
            "If I had just one wish, it would be\x01",
            "to get through this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O Goddess, please save me...\x02",
    )

    CloseMessageWindow()

    label("loc_2460")

    Jump("loc_2F9C")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_267E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252E")

    ChrTalk(
        0xFE,
        "I'm worried about this city's condition...\x02",
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
            "My son is my hope. I'd like\x01",
            "to contact him if possible...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25D8")

    label("loc_252E")


    ChrTalk(
        0xFE,
        (
            "Ever since the declaration of independence,\x01",
            "foreign communication has completely ceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alm and Aerie are my hope, so I'd\x01",
            "like to contact them somehow, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D8")

    Jump("loc_2679")

    label("loc_25DD")


    ChrTalk(
        0xFE,
        (
            "Just what are those monsters \x01",
            "that have appeared in the city...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't look like they've\x01",
            "entered Downtown, but will\x01",
            "we really be all right!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2679")

    Jump("loc_2F9C")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2ACB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_290A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2796")

    ChrTalk(
        0xFE,
        (
            "I-I heard the address on East Street,\x01",
            "but I honestly couldn't believe it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say, the\x01",
            "two major powers won't stay\x01",
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
    Jump("loc_2905")

    label("loc_2796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286A")

    ChrTalk(
        0xFE,
        "Alm and Aerie are in Liberl, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmph... What kind of convenient\x01",
            "thing am I thinking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm corrupt, I'm a Crossbellan...\x01",
            "No matter what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2905")

    label("loc_286A")


    ChrTalk(
        0xFE,
        (
            "Goodness... What kind of convenient\x01",
            "thing am I thinking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm corrupt, I'm a Crossbellan...\x01",
            "No matter what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2905")

    Jump("loc_2AC6")

    label("loc_290A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0D")

    ChrTalk(
        0xFE,
        (
            "I-I heard the address on East Street,\x01",
            "but I honestly couldn't believe it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say, the\x01",
            "two major powers won't stay\x01",
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
    Jump("loc_2AC6")

    label("loc_2A0D")


    ChrTalk(
        0xFE,
        (
            "...Hmph, what am I thinking?\x01",
            "If I discard this state now and\x01",
            "flee somewhere else, what am I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I'm corrupt, I'm a Crossbellan...\x01",
            "No matter what happens, I'll stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC6")

    Jump("loc_2F9C")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2AD9")
    Jump("loc_2F9C")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B45")

    ChrTalk(
        0xFE,
        (
            "L-Let's not joke here...\x01",
            "I've got to hurry and hide!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But, just where\x01",
            "can I go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9C")

    label("loc_2B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B56")
    Call(0, 11)
    Jump("loc_2F9C")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B67")
    Call(0, 12)
    Jump("loc_2F9C")

    label("loc_2B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B78")
    Call(0, 7)
    Jump("loc_2F9C")

    label("loc_2B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC4")

    ChrTalk(
        0xFE,
        (
            "Hmm. Mayor Dieter has\x01",
            "done a drastic thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow... With this, the positions of the\x01",
            "Imperial and Republican Faction congressmen\x01",
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
            "*sigh*. I'll have to think seriously\x01",
            "about what I want to do in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CFC")

    label("loc_2CC4")


    ChrTalk(
        0xFE,
        (
            "A second life, huh...\x01",
            "I wonder what's\x01",
            "left for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFC")

    Jump("loc_2F9C")

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1C")
    Call(0, 8)
    Jump("loc_2D9D")

    label("loc_2D1C")


    ChrTalk(
        0xFE,
        (
            "I know very well\x01",
            "I can't use this\x01",
            "as an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at that time, I was a youngster\x01",
            "who didn't know left from right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9D")

    Jump("loc_2F9C")

    label("loc_2DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E0C")

    ChrTalk(
        0xFE,
        "Tooo hell with the VIPs visit!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. Every last\x01",
            "person's in a festival mood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9C")

    label("loc_2E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC9")

    ChrTalk(
        0xFE,
        "H-Hmph... To hell with the Trade Conference.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got no interest in\x01",
            "the congress nor in\x01",
            "politics anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They should just do whatever they want.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F28")

    label("loc_2EC9")


    ChrTalk(
        0xFE,
        "H-Hmph... To hell with the Trade Conference.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They should just do whatever they want.\x02",
    )

    CloseMessageWindow()

    label("loc_2F28")

    Jump("loc_2F9C")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F93")

    ChrTalk(
        0xFE,
        "Y-You still have business with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't need anything,\x01",
            "leave already!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9C")

    label("loc_2F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F9C")

    label("loc_2F9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_2119 end

    def Function_11_2FA0(): pass

    label("Function_11_2FA0")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311E")

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
            "Ehehe. Mama's\x01",
            "homemade cookies.\x01",
            "They're so good, you know♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "T-Then, don't mind if I do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's like I'm receiving\x01",
            "them for what I did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, please don't worry\x01",
            "about the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I made extra,\x01",
            "just like you\x01",
            "did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I see, then...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_318D")

    label("loc_311E")


    ChrTalk(
        0xA,
        (
            "*crunch, crunch*...\x01",
            "Mmm, these are good!\x02",
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
        "Uh uh, I'm glad you like them.\x02",
    )

    CloseMessageWindow()

    label("loc_318D")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_2FA0 end

    def Function_12_319A(): pass

    label("Function_12_319A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C2")

    ChrTalk(
        0xC,
        (
            "Mama, these beans\x01",
            "are yummy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, Rimah's really\x01",
            "taken a liking to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mr. Geval, are you sure\x01",
            "we can have some?\x02",
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
            "There's more here\x01",
            "than I can eat.\x01",
            "Please feel free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uh uh, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thanks, mister!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3342")

    label("loc_32C2")


    ChrTalk(
        0xC,
        (
            "*glom*. Mmm,\x01",
            "they're good!\x02",
        )
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
            "Ha ha, I'm glad\x01",
            "she likes them\x01",
            "so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3342")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_319A end

    def Function_13_334F(): pass

    label("Function_13_334F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3360")
    Jump("loc_36A5")

    label("loc_3360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_336E")
    Jump("loc_36A5")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_337C")
    Jump("loc_36A5")

    label("loc_337C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_338A")
    Jump("loc_36A5")

    label("loc_338A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3398")
    Jump("loc_36A5")

    label("loc_3398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3442")

    ChrTalk(
        0xFE,
        "*sigh*, I knew this commute would be hard.\x02",
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
            "I just can't work up\x01",
            "the will to leave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_34C4")

    label("loc_3442")


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
            "I just can't work up\x01",
            "the will to leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C4")

    Jump("loc_36A5")

    label("loc_34C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34D7")
    Jump("loc_36A5")

    label("loc_34D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34E5")
    Jump("loc_36A5")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34F3")
    Jump("loc_36A5")

    label("loc_34F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3501")
    Jump("loc_36A5")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_350F")
    Jump("loc_36A5")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CD")

    ChrTalk(
        0xFE,
        (
            "Uhhm, the materials I got\x01",
            "during the orientation time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it hasn't been long since I enrolled...\x01",
            "If I forgot them, it would be hard from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_36A5")

    label("loc_35CD")


    ChrTalk(
        0xFE,
        (
            "Uh uh, but I really passed\x01",
            "the St. Ursula Medical\x01",
            "College entrance exam.\x02",
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

    label("loc_36A5")

    TalkEnd(0xFE)
    Return()

    # Function_13_334F end

    def Function_14_36A9(): pass

    label("Function_14_36A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_375E")

    ChrTalk(
        0xFE,
        (
            "When I look at that huge pale azure tree,\x01",
            "I can't help but get worried.\x02",
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
    Jump("loc_43C0")

    label("loc_375E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_37E8")

    ChrTalk(
        0xFE,
        (
            "They called it martial law, but to think\x01",
            "something like this would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...My hands are shaking when I cook.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_37E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3891")

    ChrTalk(
        0xFE,
        (
            "I asked Mr. Tantos about\x01",
            "the address, but honestly,\x01",
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
    Jump("loc_43C0")

    label("loc_3891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_396F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EC")

    ChrTalk(
        0xFE,
        (
            "It's hard to cook daikon,\x01",
            "so I'll do some light scoring...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_396A")

    label("loc_38EC")

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
        "That's right. I wonder what would be good.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_396A")

    Jump("loc_43C0")

    label("loc_396F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39FB")

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
    Jump("loc_43C0")

    label("loc_39FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A0C")
    Call(0, 11)
    Jump("loc_43C0")

    label("loc_3A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A1D")
    Call(0, 12)
    Jump("loc_43C0")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AAD")

    ChrTalk(
        0xFE,
        (
            "My husband started\x01",
            "work at a new site.\x02",
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
    Jump("loc_43C0")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD7")

    ChrTalk(
        0xFE,
        (
            "I heard this from my husband awhile back. He said\x01",
            "foreign construction companies had significant\x01",
            "involvement with the construction of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand that the floors\x01",
            "were divided up between them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among them, my husband participated\x01",
            "in construction of the VIP floor, and\x01",
            "the international conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of he international\x01",
            "conference room, it was used for\x01",
            "the Trade Conference the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. When I think that\x01",
            "it's the place where my husband\x01",
            "worked, I'm happy somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D99")

    label("loc_3CD7")


    ChrTalk(
        0xFE,
        (
            "Speaking of he international\x01",
            "conference room, it was used for\x01",
            "the Trade Conference the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. When I think that\x01",
            "it's the place where my husband\x01",
            "worked, I'm happy somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D99")

    Jump("loc_43C0")

    label("loc_3D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E1F")

    ChrTalk(
        0xFE,
        (
            "I was making some of the green\x01",
            "tea Miss Rixia gave me earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. This green tea\x01",
            "has a lovely smell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_3E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E2D")
    Jump("loc_43C0")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F16")

    ChrTalk(
        0xFE,
        (
            "Just the unveiling ceremony\x01",
            "is left for Orchis Tower.\x02",
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
            "Tomorrow, I've got to burn the image\x01",
            "of my husband's work into my memory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F99")

    label("loc_3F16")


    ChrTalk(
        0xFE,
        (
            "The Orchis Tower unveiling\x01",
            "ceremony is finally tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to burn the image of my\x01",
            "husband's work into my memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F99")

    Jump("loc_43C0")

    label("loc_3F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_418C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F2")

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
            "These past few months he's been\x01",
            "working at the site of "Orchis Tower",\x01",
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
        "Uh uh, I'm really looking forward to its completion.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4187")

    label("loc_40F2")


    ChrTalk(
        0xFE,
        (
            "Construction of "Orchis Tower"\x01",
            "is the biggest job my husband's\x01",
            "ever been involved in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I'm really looking forward to its completion.\x02",
    )

    CloseMessageWindow()

    label("loc_4187")

    Jump("loc_43C0")

    label("loc_418C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_43C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F9")

    ChrTalk(
        0xFE,
        (
            "These past few years, the state\x01",
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
            "I shouldn't be openly happy\x01",
            "they frozen it, however...\x01",
            "When I heard that, I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this place was\x01",
            "demolished, our families\x01",
            "would have nowhere to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_43C0")

    label("loc_42F9")


    ChrTalk(
        0xFE,
        (
            "I heard the congressmen at the heart\x01",
            "of the plan were arrested due to\x01",
            "involvement with the Cult incident.\x02",
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

    label("loc_43C0")

    TalkEnd(0xFE)
    Return()

    # Function_14_36A9 end

    def Function_15_43C4(): pass

    label("Function_15_43C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E2")
    Call(0, 16)
    Jump("loc_445B")

    label("loc_43E2")


    ChrTalk(
        0xFE,
        (
            "Even at a time like this,\x01",
            "papa's doing his best for\x01",
            "Rimah and mama.\x02",
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

    label("loc_445B")

    Jump("loc_48FE")

    label("loc_4460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_44BA")

    ChrTalk(
        0xFE,
        "Both papa and mama look worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if they're all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_44BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4501")

    ChrTalk(
        0xFE,
        (
            "Mama...\x01",
            "She looks sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want her to cheer up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_450F")
    Jump("loc_48FE")

    label("loc_450F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4571")

    ChrTalk(
        0xFE,
        (
            "Big sister Rixia was down\x01",
            "today, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if something happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4582")
    Call(0, 11)
    Jump("loc_48FE")

    label("loc_4582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4593")
    Call(0, 12)
    Jump("loc_48FE")

    label("loc_4593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4665")

    ChrTalk(
        0xFE,
        (
            "Mama and I saw papa\x01",
            "off this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is his first day of work at a\x01",
            "new site, so the time is flexible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rimah doesn't get it, but is\x01",
            "happy she got to see him off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_46B7")

    label("loc_4665")


    ChrTalk(
        0xFE,
        (
            "Mama and Rimah gave\x01",
            "papa a goodbye kiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Papa was embarrassed and cute.\x02",
    )

    CloseMessageWindow()

    label("loc_46B7")

    Jump("loc_48FE")

    label("loc_46BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4711")

    ChrTalk(
        0xFE,
        (
            "Wonderland was\x01",
            "really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to go again with everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4743")

    ChrTalk(
        0xFE,
        "Tea, tea♪ Tea with everyone♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4751")
    Jump("loc_48FE")

    label("loc_4751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476C")
    Call(0, 17)
    Jump("loc_47A6")

    label("loc_476C")


    ChrTalk(
        0xFE,
        (
            "Here, my darling.\x01",
            "I made food for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eat up♪\x02",
    )

    CloseMessageWindow()

    label("loc_47A6")

    Jump("loc_48FE")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4834")

    ChrTalk(
        0xFE,
        (
            "Rimah's papa works\x01",
            "at a construction\x01",
            "site every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like he's late\x01",
            "coming home today. Hmm...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_485F")

    label("loc_4834")


    ChrTalk(
        0xFE,
        (
            "Papa's late\x01",
            "coming home\x01",
            "today. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_485F")

    Jump("loc_48FE")

    label("loc_4864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48FE")

    ChrTalk(
        0xFE,
        (
            "Mama's happy those corrupt\x01",
            "government officials\x01",
            "haven't been by lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but if mama's\x01",
            "happy, Rimah's happy too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FE")

    TalkEnd(0xFE)
    Return()

    # Function_15_43C4 end

    def Function_16_4902(): pass

    label("Function_16_4902")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        "Papa, are you going to work today, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yeah. The construction site's reopened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Rimah, you must be worried, but\x01",
            "please watch the house with your mama.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, got it.\x02",
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
        "Ha ha. Off I go.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_4902 end

    def Function_17_4A17(): pass

    label("Function_17_4A17")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alllright, Rimah. \x01",
            "What shall we play today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Then,\x01",
            ""house", I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rimah will be the mama\x01",
            "so you be the papa, papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ha ha. Papa being the papa, huh?\x01",
            "I see. Roger that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_17_4A17 end

    def Function_18_4AEE(): pass

    label("Function_18_4AEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0C")
    Call(0, 16)
    Jump("loc_4BA1")

    label("loc_4B0C")


    ChrTalk(
        0xFE,
        (
            "Iyahahaha... \x01",
            "This is embarrassing,\x01",
            "bu it is uplifting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alllright! I was worried about things, but...\x01",
            "I'll work for my family again today!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA1")

    Jump("loc_4D9A")

    label("loc_4BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4C30")

    ChrTalk(
        0xFE,
        (
            "It's become like this, and I\x01",
            "don't know what to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll protect Corona and Rimah,\x01",
            "no matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C3E")
    Jump("loc_4D9A")

    label("loc_4C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C4C")
    Jump("loc_4D9A")

    label("loc_4C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4C5A")
    Jump("loc_4D9A")

    label("loc_4C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C68")
    Jump("loc_4D9A")

    label("loc_4C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C76")
    Jump("loc_4D9A")

    label("loc_4C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C84")
    Jump("loc_4D9A")

    label("loc_4C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4C92")
    Jump("loc_4D9A")

    label("loc_4C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D0A")

    ChrTalk(
        0xFE,
        (
            "*sigh*, it's been awhile since\x01",
            "I passed time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Happy families are really great things.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D18")
    Jump("loc_4D9A")

    label("loc_4D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D33")
    Call(0, 17)
    Jump("loc_4D7E")

    label("loc_4D33")


    ChrTalk(
        0xFE,
        "Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*...\x01",
            "Yeah, it tastes\x01",
            "good today too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D7E")

    Jump("loc_4D9A")

    label("loc_4D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4D91")
    Jump("loc_4D9A")

    label("loc_4D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D9A")

    label("loc_4D9A")

    TalkEnd(0xFE)
    Return()

    # Function_18_4AEE end

    def Function_19_4D9E(): pass

    label("Function_19_4D9E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E1F")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, Dietier... \x01",
            "Will independence make us happy?\x01",
            "...*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EA")

    label("loc_4E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E2D")
    Jump("loc_54EA")

    label("loc_4E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E9D")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Where's the land of dreams...\x01",
            "Vaaan, take me with youuu...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EA")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F57")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F13")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x01",
            "Who is it? Who's raining on me...\x02",
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
    Jump("loc_4F52")

    label("loc_4F13")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x01",
            "What'll I do if I wet my pants...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F52")

    Jump("loc_54EA")

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4FC5")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I don't have mira...\x01",
            "To stay overnight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I'm that kind of guy... *snore*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EA")

    label("loc_4FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50AB")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5067")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I finally got... \x01",
            "A 1,000 mira bill...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "At the casino... Before I\x01",
            "knew it... Penniless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_50A6")

    label("loc_5067")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "My mira... Give it back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A6")

    Jump("loc_54EA")

    label("loc_50AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_51C4")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515D")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Oh, Vaan! You've got no\x01",
            "problem with this, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Your breadwinner...\x01",
            "Worked... Ooh,\x01",
            "*wheeze*, *hic*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_51BF")

    label("loc_515D")


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
            "But please wait on the rent...\x01",
            "*wheeze*, *hic*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BF")

    Jump("loc_54EA")

    label("loc_51C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52DD")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5281")

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*snore*... Hah? \x01",
            "Ooh, there's some booze.\x01",
            "Nice work, Vaan.\x02",
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
            "Bleargh!? *spit spit...*!\x01",
            "The fuck is this, it's not booze!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52D8")

    label("loc_5281")


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
            "You won't get away with this... *mumble...zzz*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D8")

    Jump("loc_54EA")

    label("loc_52DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53CE")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5371")

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
            "No choice, then... \x01",
            "I'll have to get a daily job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_53C9")

    label("loc_5371")


    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "No choice, then... \x01",
            "I'll have to get a daily job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C9")

    Jump("loc_54EA")

    label("loc_53CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_542E")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Booze, booze, my best\x01",
            "friend, boooooze...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EA")

    label("loc_542E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5493")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, Vaan!\x01",
            "Aren't you here with my booze yet..!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EA")

    label("loc_5493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_54EA")
    Call(0, 20)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*zzz*...*snore*... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Booze, booze, get\x01",
            "me some boooooze...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EA")

    TalkEnd(0x14)
    Return()

    # Function_19_4D9E end

    def Function_20_54EE(): pass

    label("Function_20_54EE")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x01",
            "A voice can be heard inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_20_54EE end

    def Function_21_5533(): pass

    label("Function_21_5533")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5552")
    Call(0, 9)
    Jump("loc_55C4")

    label("loc_5552")


    ChrTalk(
        0x9,
        (
            "Most importantly, I'm glad you're \x01",
            "doing well too, Mr. Tantos.\x02",
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

    label("loc_55C4")

    Jump("loc_5642")

    label("loc_55C9")


    ChrTalk(
        0x9,
        (
            "I'll absolutely submit my notice\x01",
            "of move-out before the day is out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Sorry for putting you through all of this.\x02",
    )

    CloseMessageWindow()

    label("loc_5642")

    TalkEnd(0xFE)
    Return()

    # Function_21_5533 end

    def Function_22_5646(): pass

    label("Function_22_5646")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C1")

    ChrTalk(
        0xFE,
        "My, who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is some time until\x01",
            "the emergency feeding,\x01",
            "so please wait until then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573F")

    label("loc_56C1")

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
        "That's right. I wonder what would be good.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0x0)

    label("loc_573F")

    TalkEnd(0xFE)
    Return()

    # Function_22_5646 end

    def Function_23_5743(): pass

    label("Function_23_5743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_57D7")

    ChrTalk(
        0xFE,
        (
            "(He hasn't been able to get any booze\x01",
            "lately, so I thought he was depressed...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Disgusting...\x01",
            "This ain't my old man...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_57D7")


    ChrTalk(
        0xFE,
        (
            "Kyahaha. Old man, ain't it time for you\x01",
            "to run out both of booze and mira?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5827")

    TalkEnd(0xFE)
    Return()

    # Function_23_5743 end

    def Function_24_582B(): pass

    label("Function_24_582B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_583C")
    Jump("loc_58CD")

    label("loc_583C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5877")

    ChrTalk(
        0xFE,
        (
            "(*chuckle*... \x01",
            "He's better when drunk.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58CD")

    label("loc_5877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5885")
    Jump("loc_58CD")

    label("loc_5885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_58CD")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... \x01",
            "Then, you'll need a way\x01",
            "to make mira again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58CD")

    TalkEnd(0xFE)
    Return()

    # Function_24_582B end

    def Function_25_58D1(): pass

    label("Function_25_58D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5904")
    Call(0, 31)
    Return()

    label("loc_5904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x135, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x136, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x13B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x143, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x146, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x147, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x13A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5972")
    Call(0, 33)
    Return()

    label("loc_5972")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_5C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_END)), "loc_5C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_5A07")

    ChrTalk(
        0x13,
        (
            "Yeah, if we have so many\x01",
            "ingredients, I think I'd be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Thank you. These will\x01",
            "make everyone happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C46")

    label("loc_5A07")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                       # 0
            "Ask About Ingredients\x01",      # 1
            "Quit\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB9")

    ChrTalk(
        0x13,
        (
            "Oh, you need to check the\x01",
            "necessary ingredients?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "First, [Five-Colored Miso] x10.\x01",
            "Then, [Beast Flesh] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, [All-Curing Sake] x10\x01",
            "and [Sesame Oil] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "And, [Dark Mushroom] x30 \x01",
            "and [All-Purpose Onion] x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally, [Petit Carrot] x30\x01",
            "and [Hot Pepper] x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That's everything. Thanks in\x01",
            "advance for all your help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C46")

    label("loc_5BB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C46")

    ChrTalk(
        0x13,
        (
            "The emergency feeding menu\x01",
            "is precisely "Pork Miso Soup".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It has meat, veggies\x01",
            "and the perfect\x01",
            "nutritional balance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C46")

    Jump("loc_5CB4")

    label("loc_5C4B")


    ChrTalk(
        0x13,
        (
            "Hmm. This amount\x01",
            "too will be gone in\x01",
            "the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I wonder if I can\x01",
            "dilute it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CB4")

    TalkEnd(0xFE)
    Return()

    # Function_25_58D1 end

    def Function_26_5CB8(): pass

    label("Function_26_5CB8")

    TalkBegin(0xFE)
    OP_4B(0x15, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D80")

    ChrTalk(
        0x15,
        (
            "Listen up Vaan, and you young\x01",
            "lady as well. Stay in your rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Daddy will protect his\x01",
            "only son, and his friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "(Disgusting...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5DE6")

    label("loc_5D80")


    ChrTalk(
        0x15,
        (
            "Listen up Vaan, and you young lady\x01",
            "as well. I'll definitely protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "(Shut yer trap...)\x02",
    )

    CloseMessageWindow()

    label("loc_5DE6")

    OP_4C(0x15, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_5CB8 end

    def Function_27_5DF2(): pass

    label("Function_27_5DF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E07")
    Call(0, 28)
    Jump("loc_5F8A")

    label("loc_5E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EF2")

    ChrTalk(
        0xF,
        (
            "#01803FNow then, I've got to get\x01",
            "ready to go to City Hall...\x02\x03",
            "#01802FEveryone, thank you for the\x01",
            "warning about Miss Shirley.\x02\x03",
            "#01806FI too get a lot of "skinship"\x01",
            "due to Miss Ilya, so...\x01",
            "I'll be careful somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5F8A")

    label("loc_5EF2")


    ChrTalk(
        0xF,
        (
            "#01802FEveryone, thanks for the\x01",
            "warning about Miss Shirley.\x02\x03",
            "#01806FI too get a lot of "skinship"\x01",
            "due to Miss Ilya, so...\x01",
            "I'll be careful somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F8A")

    TalkEnd(0xFE)
    Return()

    # Function_27_5DF2 end

    def Function_28_5F8E(): pass

    label("Function_28_5F8E")

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
            "#12P#00000FHey Rixia. \x01",
            "You've returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01802FYes. I have business at\x01",
            "City Hall this afternoon,\x01",
            "so I'm resting.\x02\x03",
            "Ah... It looks like\x01",
            "Tio's finally back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, I returned to the\x01",
            "Support Section yesterday.\x02\x03",
            "#00204FI heard Arc-en-ciel gave a\x01",
            "performance for the heads of state\x01",
            "last night... That was great work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100F*giggle*, were you nervous?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FAhaha. That performance had a feeling\x01",
            "a little different from our usual ones.\x02\x03",
            "#01804FThough it was a minor role,\x01",
            "Sully had her first appearance,\x01",
            "and she was really nervous...\x02\x03",
            "#01802FMiss Ilya was the same\x01",
            "as usual, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHa ha. I can't imagine Miss\x01",
            "Ilya ever being nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01804FYes. When it comes to the stage,\x01",
            "Miss Ilya really sees only that...\x02\x03",
            "#01802FUh uh. I've felt like someone like \x01",
            "me will never be a match for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FHmm. For an artist, that's a\x01",
            "super high benchmark, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. She's a star, one of those\x01",
            "they say to be true geniuses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FBut, I feel like you will definitely\x01",
            "overtake Miss Ilya one day, Rixia.\x02\x03",
            "#00004FIt was pretty amazing how you\x01",
            "caught the kitty that fell from\x01",
            "the chandelier yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01809FAhaha... Thank you very much.\x02\x03",
            "#01802FBut really... It was because\x01",
            "my body moved on its own...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01803FBy the way, that girl yesterday...\x01",
            "Miss Shirley was her name, right?\x02\x03",
            "#01802FI heard she's Randy's cousin, but...\x01",
            "What kind of person is she?\x02",
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
            "#12P#00304F...Ha ha. If I had to say, she's a\x01",
            "tomboy who does whatever she likes.\x02\x03",
            "#00302FIt's just that she's a bit of a\x01",
            "pain, so hardly good things come\x01",
            "gettin' involved with her.\x02\x03",
            "#00309FSomehow, it looks like she's\x01",
            "quite taken with you, dear Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. If you're not careful,\x01",
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
            "#01803F(Most likely, I will deal with\x01",
            "her as "Yin" in the future...)\x02",
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
            "#01802F...Uh uh, it's nothing.\x01",
            "Thanks for the warning.\x02\x03",
            "#01806FI too get a lot of "skinship"\x01",
            "due to Miss Ilya, so...\x01",
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
        "#12P#00206FYou must have it tough too, Miss Rixia.\x02",
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

    # Function_28_5F8E end

    def Function_29_6A7C(): pass

    label("Function_29_6A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AAA")
    Call(0, 34)
    Return()

    label("loc_6AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AD3")
    Call(0, 30)
    Return()

    label("loc_6AD3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6AE4")
    Jump("loc_6B8F")

    label("loc_6AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6B1A")
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
    Jump("loc_6B8F")

    label("loc_6B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B28")
    Jump("loc_6B8F")

    label("loc_6B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6B5E")
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
    Jump("loc_6B8F")

    label("loc_6B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B8F")
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

    label("loc_6B8F")

    TalkEnd(0xFF)
    Return()

    # Function_29_6A7C end

    def Function_30_6B93(): pass

    label("Function_30_6B93")

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
            "#6P#00000FDowntown, Lotus Heights....\x01",
            "Yeah, this is the place.\x02",
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
            "#6P#00000FExcuse me, is\x01",
            "anyone there?\x02",
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
        "#6P#10103FNo answer, eh?\x02",
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
            "#00003FI feel a slight presence, but it\x01",
            "might just be my imagination...\x02",
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
            "#6P#10303FMaybe the resident is pretending not to be home.\x02\x03",
            "#10300FSo what do we do?\x01",
            "Force our way in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FWell, if we have no other options,\x01",
            "we can consider it, but...\x02",
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
        "#6P#00000FIt sounded like dishes or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FIt's looking more likely that\x01",
            "they're pretending not to be home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FLet's try calling out again.\x02\x03",
            "#00001FExcuse me! \x01",
            "Is anyone there!?\x02\x03",
            "We would like to talk a little...!\x02",
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
            "#6P#10304FHu hu, resistance to the bitter end, huh.\x02\x03",
            "#10302FMaybe they escaped\x01",
            "through the window?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHmm, that would be\x01",
            "rather troublesome.\x02",
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

    def lambda_7180():
        OP_95(0x9, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7180)
    Sleep(100)

    def lambda_719D():
        OP_95(0x8, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_719D)
    Sleep(100)
    WaitChrThread(0x9, 1)

    def lambda_71BE():
        OP_95(0x9, 3060, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_71BE)
    Sleep(100)
    WaitChrThread(0x8, 1)

    def lambda_71DF():
        OP_95(0x8, 4059, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_71DF)
    WaitChrThread(0x9, 1)

    def lambda_71FD():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_71FD)
    WaitChrThread(0x8, 1)
    Sleep(100)

    def lambda_7211():
        OP_93(0x8, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7211)
    WaitChrThread(0x8, 1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#12PI heard a bunch of yelling...\x01",
            "Is this your doing?\x02",
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

    def lambda_72D9():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72D9)
    Sleep(10)

    def lambda_72E9():
        OP_93(0x102, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72E9)
    Sleep(10)

    def lambda_72F9():
        OP_93(0x109, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72F9)
    Sleep(10)

    def lambda_7309():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7309)
    Sleep(10)

    ChrTalk(
        0x101,
        (
            "#5P#00005FOh right, excuse us.\x02\x03",
            "#00000FWe're with the Crossbell Police\x01",
            "Special Support Section.\x02\x03",
            "#00003FWe have business with the\x01",
            "resident of this apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105FDo either of you\x01",
            "know the resident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYeah, of course\x01",
            "we do. But...\x02",
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
            "Lloyd explained that they were\x01",
            "investigating suspicious housing units.\x07\x00\x02",
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
            "identify the resident\x01",
            "of this unit, do you?\x02",
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
            "resident of this unit.\x02",
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
        "#5P#00005FI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PYes. But I didn't\x01",
            "submit the residence\x01",
            "change notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PBut it's not too late, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI know, I'll be sure to submit\x01",
            "it by the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, that would\x01",
            "really help us out.\x02\x03",
            "#00103FBy the way, would you mind telling\x01",
            "us your reason for moving out?\x02",
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
            "#12PAnd so, I accepted his\x01",
            "offer and moved to the\x01",
            "Republic two weeks ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FThen, why are you here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PI wanted to thank again everyone in this apartment,\x01",
            "who supported me in that difficult time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PThey all helped\x01",
            "me so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHo ho. How thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FI see. I think I understand\x01",
            "your situation, Mr. Geithner.\x02\x03",
            "#00000FThen, I want to ask you again\x01",
            "about the current resident.\x02",
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
            "#5P#00105F...Is there some situation\x01",
            "that's difficult to explain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAh, well I think the problem lies\x01",
            "in the heart of the new resident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PLet's see...\x02",
    )

    CloseMessageWindow()

    def lambda_7AF8():
        OP_9B(0x1, 0x8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7AF8)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_7B14():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B14)
    Sleep(50)

    def lambda_7B2C():
        OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B2C)
    Sleep(50)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_7B4B():
        OP_9B(0x1, 0x109, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B4B)
    Sleep(50)

    def lambda_7B63():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B63)
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
            "#6PThis is Tantos.\x01",
            "Are you there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you can hear me,\x01",
            "could you open up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThere are police officers here.\x01",
            "They say they want to know your name.\x01",
            "They won't do anything to you.\x02",
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
        "#6POoh, looks like it's open.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PAlright, now don't cause a\x01",
            "ruckus and do what you have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FRight, thank you for your cooperation.\x02",
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

    def lambda_7E4E():
        OP_95(0x101, 51800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E4E)

    def lambda_7E68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E68)
    Sleep(500)

    def lambda_7E7C():
        OP_95(0x102, 51800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E7C)

    def lambda_7E96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E96)
    Sleep(500)

    def lambda_7EAA():
        OP_95(0x109, 50800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EAA)

    def lambda_7EC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7EC4)
    Sleep(500)

    def lambda_7ED8():
        OP_95(0x105, 50800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7ED8)

    def lambda_7EF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7EF2)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_7F0A():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F0A)
    WaitChrThread(0x102, 1)

    def lambda_7F1B():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F1B)
    WaitChrThread(0x109, 1)

    def lambda_7F2C():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7F2C)
    WaitChrThread(0x105, 1)

    def lambda_7F3D():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7F3D)

    ChrTalk(
        0x101,
        "#6P#00000F──Excuse us...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        "#11PAre you here to make fun of me?\x02",
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
            "#11PI said, "Are you here\x01",
            "to make fun of me!?"\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "???",
        (
            "#11PI'm Geval! I was once a\x01",
            "glorious congressman, but\x01",
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
        "#6P#00011FT-This person is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F...Former congressman Geval of the Imperial Faction.\x02\x03",
            "#00101FWeren't you holed up at\x01",
            "St. Ursula Hospital ever since\x01",
            "your misdeeds came to light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PH-Hmph, so you\x01",
            "do know of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell, you've found me. What're\x01",
            "you going to do with me now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI don't have any m-mira, as you can see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PEven the rent for this apartment...\x01",
            "I somehow got it through\x01",
            "an old acquaintance of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh! Or are you\x01",
            "trying to use me\x01",
            "for something?\x02",
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
            "#6P#00106FNo, nothing\x01",
            "of the sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe just came to\x01",
            "see who exactly\x01",
            "is living here.\x02\x03",
            "#00003FHmm, Mr. Geval.\x01",
            "You're definitely the new\x01",
            "resident here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PUh, yeah... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThen that's all we need to know.\x02\x03",
            "#10100FThere isn't any criminal activity,\x01",
            "so everything should be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FBut why would you write the name\x01",
            "of that fairytale author on\x01",
            "your residence change notice?\x02\x03",
            "#10300FIt's way too suspicious. I think it\x01",
            "attracts a lot of attention, contrary\x01",
            "to what you probably intended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThis address did look the most suspicious\x01",
            "out of all of them, by the look of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PH-Hmph....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI've always been a big\x01",
            "fan of Sean Alnam.\x02",
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
        (
            "#6P#10112FE-Ehm...\x01",
            "That's a bit unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FW-Well, it's true that Sean Alnam is an\x01",
            "author read by people of all ages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, I wonder if this is\x01",
            "what they call "gap moe."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FI-Is that it...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PHmph...shut up, shup up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf you've got what you\x01",
            "needed, get out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FR-Right, excuse us.\x02\x03",
            "#00100FWell then Lloyd,\x01",
            "let's get going.\x02",
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

    # Function_30_6B93 end

    def Function_31_8880(): pass

    label("Function_31_8880")

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
            "#00000FIt looks like you're getting ready\x01",
            "for emergency feeding distribution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIs there anything we can help with?\x02",
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
            "Umm... Actually,\x01",
            "we're short of\x01",
            "ingredients.\x02",
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
            "#00300FA shoppin' trip. \x01",
            "Well, that sounds easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FSo, what exactly\x01",
            "do you need?\x02",
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
            "First, [Five-Colored Miso] x10.\x01",
            "Then, [Beast Flesh] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Next, [All-Curing Sake] x10\x01",
            "and [Sesame Oil] x10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "And, [Dark Mushroom] x30 \x01",
            "and [All-Purpose Onion] x30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Finally, [Petit Carrot] x30\x01",
            "and [Hot Pepper] x30.\x02",
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
        "#10106FThat's a huge amount of stuff.\x02",
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
            "It was a bit of a problem yesterday\x01",
            "because we didn't have quite enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So today, I don't\x01",
            "want to run out.\x02",
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
            "#10300FBy the way, what\x01",
            "dish are you making?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, it's "Pork Miso Soup"― \x01",
            "It warms the body and the soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'll treat all of you to some\x01",
            "when it's done, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, I'll be looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh yeah, I\x01",
            "almost forgot.\x02",
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
            "Received 500 mira.\x07\x00\x02",
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
            "#00306FHmm, how to say this... That's not\x01",
            "enough no matter how you slice it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Sorry 'bout that. \x01",
            "The budget is really tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If you plan on helping us I beg\x01",
            "you do it with that in some way.\x02",
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
            "#00203FYes. The situation being what it is,\x01",
            "this is the least we could do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, well if that's how it's\x01",
            "going to be, then let's get to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00000FYeah. Let's go\x01",
            "shopping now.\x02",
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

    # Function_31_8880 end

    def Function_32_9137(): pass

    label("Function_32_9137")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9444")

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
            "Well, you really have my thanks.\x01",
            "We're counting on you.\x02",
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
            "somewhere, I'd like\x01",
            "you to bring it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do, I'll be able to treat\x01",
            "everyone to my special "Robust\x01",
            "Acerbic Tomato Pork Miso Soup".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FExtract, you say...\x01",
            "Are "Acerbic Tomatoes"\x01",
            "themselves no good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Preparing them for cooking\x01",
            "takes a lot of time, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that's only if you have time. \x01",
            "It's not like it's a problem if you can't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAlright, we'll remember this.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 2)
    OP_29(0x8E, 0x1, 0x3)
    Jump("loc_956A")

    label("loc_9444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_94CF")

    ChrTalk(
        0xFE,
        (
            "Oh, it looks like you've\x01",
            "brought the item I requested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm, thanks. \x01",
            "With this, I'll be able to\x01",
            "cheer everyone up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_956A")

    label("loc_94CF")


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
            "somewhere, I'd like\x01",
            "you to bring it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, only if if\x01",
            "you have time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_956A")

    TalkEnd(0x8)
    Return()

    # Function_32_9137 end

    def Function_33_956E(): pass

    label("Function_33_956E")

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
            "Hand Them Over\x01",      # 0
            "Do Not\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9738")

    ChrTalk(
        0x13,
        (
            "Oh, could it be you don't\x01",
            "have them together yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "In that case, speak with me\x01",
            "again once you're ready.\x02",
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

    label("loc_9738")


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
        "Yeah, everything's here, just like I said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Nice work guys.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x340, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AE7")
    OP_2C(0x8E, 0x1)

    ChrTalk(
        0x103,
        (
            "#00205FCome to think of it, Lloyd...\x01",
            "Should we give Azel that, too?\x02",
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
            "#10304FHu hu, Mr. Tantos asked\x01",
            "us to get it for him.\x02\x03",
            "#10302FI'm told he's making a\x01",
            "special kind of pork miso soup?\x02",
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
            "Well then, I better\x01",
            "ask Mr. Tantos\x01",
            "before using it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 4)

    label("loc_9AE7")


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
            "Yeah. Nice work you guys. This is\x01",
            "gonna be a huge help to all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'll start distributing it to\x01",
            "everyone during a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The Support Section is welcome\x01",
            "to some too, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAlright. We'll just have to take you up on that.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CAB")

    ChrTalk(
        0x101,
        (
            "#00004FWe'll leave it\x01",
            "to you, then.\x02\x03",
            "#00000FWe're done helping everyone,\x01",
            "so let's go report to Abbas.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_9CFB")

    label("loc_9CAB")


    ChrTalk(
        0x101,
        (
            "#00004FWe'll leave it\x01",
            "to you, then.\x02\x03",
            "#00000FLet's see who\x01",
            "else needs help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CFB")

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

    # Function_33_956E end

    def Function_34_9D35(): pass

    label("Function_34_9D35")

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
            "#00000FMr. Geval,\x01",
            "are you there?\x02",
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
            "#00100FThere's no mistake. This is definitely\x01",
            "Mr. Geval's apartment.\x02",
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
            "What are you\x01",
            "guys doing?\x02",
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

    def lambda_A027():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A027)
    Sleep(50)

    def lambda_A037():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A037)
    Sleep(50)

    def lambda_A047():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A047)
    Sleep(50)

    def lambda_A057():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A057)
    Sleep(50)

    def lambda_A067():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A067)
    Sleep(50)

    def lambda_A077():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A077)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Oh... You're the Special Support\x01",
            "Section from back then, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3630, 1300, 2880, 2000)
    OP_95(0x8, 3800, 0, 1500, 1500, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        (
            "#10302FHu hu,\x01",
            "good morning, Mr. Tantos.\x02\x03",
            "Do you know where\x01",
            "the former congressman\x01",
            "who lives here went?\x02",
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
        "Is there some kind of incident involving him?\x02",
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
            "Lloyd explain that they were searching\x01",
            "for Geval due to Alm's request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, so that couple came all\x01",
            "the way from Liberl, did they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ho ho, Mr. Geval\x01",
            "is one lucky fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FDo you know  \x01",
            "Mr. Alm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This past week he\x01",
            "visited this apartment.\x01",
            "We talked about many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, but Mr. Geval\x01",
            "went off somewhere\x01",
            "just before that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I didn't ask where\x01",
            "he was going...\x02",
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
        "Oh, come to think of it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There might be\x01",
            "someone who does\x01",
            "know where he went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FReally...!?\x02",
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
            "Even after Mr. Geval moved here,\x01",
            "he came to see him many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Vil, Villa... Villasomething.\x01",
            "That's the name of the\x01",
            "apartment where he lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FVillasomething...?\x01",
            "I feel like I have\x01",
            "heard that before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, let's search the\x01",
            "buildings on West Street.\x02\x03",
            "#00000FThank you very much for your\x01",
            "cooperation, Mr. Tantos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, no, don't mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please help Mr. Geval and\x01",
            "that couple find each other.\x02",
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

    # Function_34_9D35 end

    SaveToFile()

Try(main)
