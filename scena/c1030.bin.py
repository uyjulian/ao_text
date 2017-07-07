from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1030.bin",                # FileName
        "c1030",                    # MapName
        "c1030",                    # Location
        0x0012,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1030",                  # 0
        "Zhang Hui",             # 1
        "Fen",                 # 2
        "Sunsan",               # 3
        "pack",                 # 4
        "Ruth",                 # 5
        "grid",               # 6
        "bond",                 # 7
        "Craig",               # 8
        "Sanita",               # 9
        "Mary",                 # 10
        "tourist",                 # 11
        "tourist",                 # 12
        "tourist",                 # 13
        "tourist",                 # 14
        "Reporter Noticia",         # 15
        "Grace",               # 16
        "Raines",               # 17
        "Mrs.",                   # 18
        "boy",                 # 19
        "Citizen",                   # 20
        "Lisha",               # 21
        "Sister · Lease",       # 22
        "Almu",                 # 23
        "Airy",               # 24
        "Alexei members",         # 25
        "Cronk",               # 26
        "Dins",               # 27
        "Lily",                 # 28
        "Marte",                 # 29
        "Tsao",                 # 30
        "Row",                   # 31
        "Nielsen",             # 32
        "Rector",               # 33
        "Dishes",                   # 34
        "Dishes",                   # 35
        "Dishes",                   # 36
        "Dishes",                   # 37
        "Dishes",                   # 38
        "Dishes",                   # 39
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch27602.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch34402.itc",                   # 08
        "chr/ch39000.itc",                   # 09
        "chr/ch20002.itc",                   # 0A
        "chr/ch20102.itc",                   # 0B
        "chr/ch20202.itc",                   # 0C
        "chr/ch20302.itc",                   # 0D
        "chr/ch47900.itc",                   # 0E
        "chr/ch32300.itc",                   # 0F
        "chr/ch20302.itc",                   # 10
        "chr/ch23002.itc",                   # 11
        "chr/ch22802.itc",                   # 12
        "chr/ch14002.itc",                   # 13
        "chr/ch46300.itc",                   # 14
        "chr/ch46200.itc",                   # 15
        "chr/ch31302.itc",                   # 16
        "chr/ch06002.itc",                   # 17
        "chr/ch28102.itc",                   # 18
        "chr/ch47902.itc",                   # 19
        "chr/ch45100.itc",                   # 1A
        "chr/ch23500.itc",                   # 1B
        "chr/ch20400.itc",                   # 1C
        "chr/ch24800.itc",                   # 1D
        "chr/ch24900.itc",                   # 1E
        "chr/ch06302.itc",                   # 1F
        "chr/ch31402.itc",                   # 20
        "chr/ch32502.itc",                   # 21
        "chr/ch45102.itc",                   # 22
        "chr/ch47902.itc",                   # 23
        "chr/ch05202.itc",                   # 24
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(12329,   0,       15989,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(12310,   0,       4294965306, 225,  261,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(17909,   0,       8399,    90,   261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(7130,    150,     4294965816, 180,  325,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(10550,   100,     3140,    270,  453,  0x0, 0,   6,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(8850,    0,       4840,    180,  453,  0x0, 0,   7,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(7150,    100,     3140,    90,   453,  0x0, 0,   8,   0,   255, 255, 0,   27,  255,  0)
    DeclNpc(7329,    29,      4590,    165,  389,  0x0, 0,   9,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   10,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(7159,    29,      3200,    90,   453,  0x0, 0,   11,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(4940,    150,     7130,    270,  453,  0x0, 0,   12,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(1620,    150,     7320,    90,   453,  0x0, 0,   13,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(14090,   0,       4294967177, 90,   453,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  389,  0x0, 0,   23,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(7159,    100,     3200,    90,   389,  0x0, 0,   24,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   16,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(7159,    150,     3200,    90,   453,  0x0, 0,   17,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  453,  0x0, 0,   18,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(14000,   50,      0,       90,   453,  0x0, 0,   36,  0,   255, 255, 0,   47,  255,  0)
    DeclNpc(14090,   0,       4294967177, 90,   453,  0x0, 0,   19,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(4294866496, 29,      4294911806, 90,   389,  0x0, 0,   20,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4294867697, 29,      4294911806, 270,  389,  0x0, 0,   21,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   453,  0x0, 0,   22,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(8819,    0,       8770,    225,  389,  0x0, 0,   28,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(8930,    0,       6710,    90,   389,  0x0, 0,   29,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(9939,    0,       6710,    270,  389,  0x0, 0,   30,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(7599,    0,       8909,    225,  389,  0x0, 0,   27,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(10689,   150,     3200,    270,  389,  0x0, 0,   31,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(9029,    150,     5059,    180,  389,  0x0, 0,   32,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294920776, 200,     4294915046, 180,  453,  0x0, 0,   34,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ChipFrameInfo(1652, 0)                                       # 0

    ScpFunction((
        "Function_0_674",          # 00, 0
        "Function_1_72C",          # 01, 1
        "Function_2_880",          # 02, 2
        "Function_3_A2C",          # 03, 3
        "Function_4_12D0",         # 04, 4
        "Function_5_1442",         # 05, 5
        "Function_6_1556",         # 06, 6
        "Function_7_36E9",         # 07, 7
        "Function_8_45EC",         # 08, 8
        "Function_9_4706",         # 09, 9
        "Function_10_5B58",        # 0A, 10
        "Function_11_5BFF",        # 0B, 11
        "Function_12_5E5C",        # 0C, 12
        "Function_13_5F76",        # 0D, 13
        "Function_14_6C18",        # 0E, 14
        "Function_15_6D32",        # 0F, 15
        "Function_16_7C4E",        # 10, 16
        "Function_17_89E7",        # 11, 17
        "Function_18_8A45",        # 12, 18
        "Function_19_8A7F",        # 13, 19
        "Function_20_8AA0",        # 14, 20
        "Function_21_8B19",        # 15, 21
        "Function_22_8D18",        # 16, 22
        "Function_23_95D4",        # 17, 23
        "Function_24_9964",        # 18, 24
        "Function_25_9ACC",        # 19, 25
        "Function_26_9B2E",        # 1A, 26
        "Function_27_9C70",        # 1B, 27
        "Function_28_9CE8",        # 1C, 28
        "Function_29_9D09",        # 1D, 29
        "Function_30_A2C0",        # 1E, 30
        "Function_31_A376",        # 1F, 31
        "Function_32_A410",        # 20, 32
        "Function_33_A5C7",        # 21, 33
        "Function_34_A6F5",        # 22, 34
        "Function_35_ACFB",        # 23, 35
        "Function_36_ADB3",        # 24, 36
        "Function_37_AE5D",        # 25, 37
        "Function_38_BA8D",        # 26, 38
        "Function_39_BD93",        # 27, 39
        "Function_40_BF2E",        # 28, 40
        "Function_41_C1F7",        # 29, 41
        "Function_42_C2D5",        # 2A, 42
        "Function_43_C3EC",        # 2B, 43
        "Function_44_C527",        # 2C, 44
        "Function_45_C543",        # 2D, 45
        "Function_46_C6F7",        # 2E, 46
        "Function_47_C7EE",        # 2F, 47
        "Function_48_C8C7",        # 30, 48
        "Function_49_D1BA",        # 31, 49
        "Function_50_E209",        # 32, 50
        "Function_51_EE8E",        # 33, 51
        "Function_52_EEBF",        # 34, 52
        "Function_53_FE7D",        # 35, 53
        "Function_54_105E0",       # 36, 54
        "Function_55_10E6B",       # 37, 55
        "Function_56_110A9",       # 38, 56
    ))


    def Function_0_674(): pass

    label("Function_0_674")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6B4"),
        (1, "loc_6C0"),
        (2, "loc_6CC"),
        (3, "loc_6D8"),
        (4, "loc_6E4"),
        (5, "loc_6F0"),
        (6, "loc_6FC"),
        (SWITCH_DEFAULT, "loc_708"),
    )


    label("loc_6B4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6C0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6CC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6D8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6E4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6F0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_6FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_708")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_714")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_714")

    label("loc_72B")

    Return()

    # Function_0_674 end

    def Function_1_72C(): pass

    label("Function_1_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87F")
    OP_95(0xFE, 7200, 0, 370, 1000, 0x0)
    OP_95(0xFE, 7280, 30, 1390, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_95(0xFE, 5850, 0, 1930, 1000, 0x0)
    OP_95(0xFE, 4730, 0, 3700, 1000, 0x0)
    OP_95(0xFE, 4840, 0, 5570, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 5660, 0, 5540, 1000, 0x0)
    OP_95(0xFE, 10470, 0, 10350, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1200)
    OP_95(0xFE, 12980, 0, 7230, 1000, 0x0)
    OP_95(0xFE, 12730, 0, 2100, 1000, 0x0)
    OP_95(0xFE, 13200, 0, 1420, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1600)
    OP_95(0xFE, 12280, 0, 680, 1000, 0x0)
    OP_95(0xFE, 11230, 0, 110, 1000, 0x0)
    OP_95(0xFE, 8930, 30, -1570, 1000, 0x0)
    Sleep(1400)
    OP_95(0xFE, 8720, 0, -510, 1000, 0x0)
    Jump("Function_1_72C")

    label("loc_87F")

    Return()

    # Function_1_72C end

    def Function_2_880(): pass

    label("Function_2_880")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2B")
    OP_95(0xFE, -62990, 0, 1230, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -60190, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -57400, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -50960, 0, 1190, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -57400, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -60190, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x190)
    OP_95(0xFE, -62990, 0, 1230, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    OP_95(0xFE, -65030, 0, 1190, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Sleep(100)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(300)
    Jump("Function_2_880")

    label("loc_A2B")

    Return()

    # Function_2_880 end

    def Function_3_A2C(): pass

    label("Function_3_A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5E")
    SetMapFlags(0x10000000)
    Event(0, 50)
    Jump("loc_A8B")

    label("loc_A5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B")
    SetMapFlags(0x10000000)
    Event(0, 49)

    label("loc_A8B")

    SetChrChipByIndex(0xD, 0x3)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B04")
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    EndChrThread(0x25, 0x0)
    SetChrBattleFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    Jump("loc_12CF")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B9C")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x23, 0x10)
    SetChrPos(0x8, 5670, 0, 11670, 225)
    SetChrPos(0x9, 6460, 0, 10550, 225)
    SetChrPos(0xA, 10860, 0, -1600, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xD, 0x80)
    Jump("loc_12CF")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BEE")
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -103850, 0, -53460, 180)
    Jump("loc_12CF")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CD1")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C17")
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    label("loc_C17")

    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    SetChrPos(0xA, 13000, 400, -5170, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    EndChrThread(0xA, 0x0)
    Jump("loc_C88")

    label("loc_C77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C88")
    SetChrFlags(0xA, 0x80)

    label("loc_C88")

    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x12)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrPos(0xB, 12330, 0, 15990, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_12CF")

    label("loc_CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D39")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E13")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x27, 0x10)
    SetChrPos(0x16, -46690, 200, -56110, 0)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0E")
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0xA, 16120, 0, -40, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)

    label("loc_E0E")

    Jump("loc_12CF")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E7B")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F36")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0x11)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrPos(0xA, 16030, 0, 6050, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xB, 12310, 0, -1990, 225)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 16000, 0, 15990, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x8, 17080, 0, 15430, 315)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    Jump("loc_12CF")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FF6")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x13)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -96120, 150, -52330, 180)
    SetChrChipByIndex(0x16, 0x19)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_12CF")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1063")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_12CF")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10FC")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x17, 0x17)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrChipByIndex(0x18, 0x18)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_12CF")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11DF")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrPos(0x14, 10690, 150, 3200, 270)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, 7160, 100, 3200, 90)
    SetChrFlags(0x15, 0x10)
    SetChrChipByIndex(0x16, 0x19)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, 14090, 150, -120, 90)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0x8, 0x10)

    label("loc_11DA")

    Jump("loc_12CF")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_126C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrPos(0xB, -65030, 0, 1190, 90)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrPos(0xC, 16030, 0, 6050, 270)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x16)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")
    SetChrFlags(0x20, 0x10)

    label("loc_1267")

    Jump("loc_12CF")

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12CF")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrPos(0xB, 16030, 0, 6050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -65030, 0, 1190, 90)
    BeginChrThread(0xC, 0, 0, 2)

    label("loc_12CF")

    Return()

    # Function_3_A2C end

    def Function_4_12D0(): pass

    label("Function_4_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1319")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1358")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1369")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_137A")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_138B")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_139C")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13AD")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13BE")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_13CF")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_13CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13E0")
    SetScenarioFlags(0x1, 5)
    Jump("loc_1441")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13F1")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1402")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1413")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1424")
    SetScenarioFlags(0x1, 6)
    Jump("loc_1441")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1435")
    SetScenarioFlags(0x1, 7)
    Jump("loc_1441")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1441")
    SetScenarioFlags(0x1, 6)

    label("loc_1441")

    Return()

    # Function_4_12D0 end

    def Function_5_1442(): pass

    label("Function_5_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1456")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_1456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_146A")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_146A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_147E")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_147E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1492")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_14A6")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14BA")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14CE")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14E2")
    SetScenarioFlags(0x1, 5)
    Call(0, 8)
    Jump("loc_1555")

    label("loc_14E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14F6")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_150A")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_151E")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1532")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)
    Jump("loc_1555")

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1546")
    SetScenarioFlags(0x1, 7)
    Call(0, 14)
    Jump("loc_1555")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1555")
    SetScenarioFlags(0x1, 6)
    Call(0, 12)

    label("loc_1555")

    Return()

    # Function_5_1442 end

    def Function_6_1556(): pass

    label("Function_6_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_158D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158D")
    Call(0, 52)
    Return()

    label("loc_158D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1627")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "If you like those things\x01",
            "It was worthwhile to make me too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will also cook for you\x01",
            "If you want to eat, you can come anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2221")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20CA")

    ChrTalk(
        0xFE,
        (
            "…… I'm totally okay.\x01",
            "When thinking that the riot on the table is over\x01",
            "From the next one, only funny things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, you are all together\x01",
            "You seem to go somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well this situation, to a police officer\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEr, what happened …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A20")

    ChrTalk(
        0xFE,
        (
            "Fu …… It can not be helped, even the chef's training\x01",
            "It seems that I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is my earning head,\x01",
            "Recipes of hidden secrets that pass over generations\x01",
            "I will tell you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zhang Huiは強引に料理手帳を奪って\x01",
            "I wrote something.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Medicinal Selena Tofu\"\x07\x00",
            "I got a recipe for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_B2(0x2)

    ChrTalk(
        0xFE,
        "… … Yes, I'd like to bring it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(This is … the last page of the notebook\x01",
            "It seems I got buried. )\x02\x03",
            "#00000FWell, is that okay?\x01",
            "Such an important recipe\x01",
            "Please let me know …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, I do not need to thank you.\x01",
            "Because I wanted to teach you\x01",
            "I just taught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From such a thing\x01",
            "The way of a chef is very steep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, more and more\x01",
            "You have to practice yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8C")

    label("loc_1A20")


    ChrTalk(
        0xFE,
        (
            "Fu …… It can not be helped, even the chef's training\x01",
            "It seems that I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The ultimate dish containing the soul of mine,\x01",
            "You ought to take this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '神仙麻婆『麒麟』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神仙麻婆『麒麟』', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FWell, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hun, I do not need to thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From such a thing\x01",
            "The way of a chef is very steep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, more and more\x01",
            "You have to practice yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8C")


    ChrTalk(
        0x101,
        "#00011F……Huh? Ha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is a chance, I will come again.\x01",
            "I will train a full-fledged Chinese training.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x101,
        (
            "#00012FAA no……\x01",
            "Although I had a feeling of strangeness from before.\x02\x03",
            "Perhaps they themselves,\x01",
            "People who came to practice cooking here yet\x01",
            "I feel misunderstood … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What? A few months ago\x01",
            "A misunderstanding story! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is different from another.\x01",
            "Look at the Hora food pocketbook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell Cooking Association affiliation affiliation,\x01",
            "Lloyd Bannings.\x01",
            "That's written on your notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the human who brought this\x01",
            "As a member store, you are responsible for training.\x01",
            "I see!\x02",
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
        0x103,
        (
            "#00200FThat dish notebook ……\x01",
            "That was so serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, absolutely\x01",
            "I did not notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FLet's say ha ha\x01",
            "We are respectable\x01",
            "Is it the cook's egg?\x02\x03",
            "At this time, trying to seriously aim\x01",
            "It might be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, indeed\x01",
            "It is called reckless or what ….\x02\x03",
            "#00000F……Uh,\x01",
            "But thank you.\x02\x03",
            "I mean,\x01",
            "Have it done so much ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, I do not need a bow.\x01",
            "Just to be a prospective young man\x01",
            "Until I did what I should do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, the food of ours is attentive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eat a little, and then quickly\x01",
            "I want you to regain everyday life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… even this, I,\x01",
            "Because I trust my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DE, 4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C5")

    label("loc_20C5")

    Jump("loc_221C")

    label("loc_20CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2181")

    ChrTalk(
        0xFE,
        (
            "It is quite funny at all.\x01",
            "Hun, in a hurry I will not be doing anything\x01",
            "The shop will continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That pale shining tree is creepy.\x01",
            "I want you to come back to peace at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_221C")

    label("loc_2181")


    ChrTalk(
        0xFE,
        (
            "The Longyuan restaurant is open normally.\x01",
            "You can get a seat if you order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… all of you gathered somewhere\x01",
            "I am going to go.\x01",
            "Hopefully you will finish your lunch quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221C")

    Jump("loc_36E5")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22D1")

    ChrTalk(
        0xFE,
        (
            "I do not know how long it will last\x01",
            "If I am irritated by martial law ……\x01",
            "What does this turmoil mean? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A compound that is going outside\x01",
            "If you hurt the shop even a little,\x01",
            "It is not free!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_235E")

    ChrTalk(
        0xFE,
        (
            "Independently of the crossbell,\x01",
            "Citizenたちが興奮しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything is fine,\x01",
            "Only to make a noise at a store\x01",
            "I want you to withhold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2416")

    ChrTalk(
        0xFE,
        (
            "Lishaがいなくなって、\x01",
            "Sunsanも相当こたえてるね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I made it fantastically\x01",
            "Presence that can be called a best friend …\x01",
            "Is it unreasonable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Manage energetically\x01",
            "I hope that it will become effective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2416")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2477")

    ChrTalk(
        0xFE,
        (
            "心なしか、Sunsanが\x01",
            "Looks like you are excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have you recovered?\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B3")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262C")

    ChrTalk(
        0xFE,
        (
            "Sunsan……\x01",
            "Silently to myself to miscon\x01",
            "What does it mean to participate in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the invitation from the Chairman of the Chamber of Commerce\x01",
            "You should have told me to refuse … !.!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Whom is it doing! Is it?\x01",
            "As soon as we find it, this kitchen knife\x01",
            "I'm going to break it! It is!\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        "#00306F(Why, let's keep it silent … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Huh, even seeing the reaction by rose\x01",
            "It looks fun. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26B3")

    label("loc_262C")


    ChrTalk(
        0xFE,
        (
            "まあ、Sunsanが\x01",
            "It was nice to have regained a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… As it is,\x01",
            "Sunsanを出場させた輩は\x01",
            "I will make it into eight pieces.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B3")

    Jump("loc_36E5")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2759")

    ChrTalk(
        0xFE,
        (
            "I … did you do something?\x01",
            "It seems somehow cluttered … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not fight if my belly decreases.\x01",
            "It is universal in common.\x01",
            "You should eat plenty of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_2759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27CF")

    ChrTalk(
        0xFE,
        (
            "After all, on rainy days,\x01",
            "I am comfortable with few customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until tomorrow's preparation\x01",
            "I will keep it at a stretch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E5")

    label("loc_27CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2915")

    ChrTalk(
        0xFE,
        (
            "Whew, byte to try\x01",
            "I tried simple cooking … …\x01",
            "It did not become useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After a while,\x01",
            "You have no choice but to do chores.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2910")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2910")

    Jump("loc_36E5")

    label("loc_2915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2AB8")
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A33")

    ChrTalk(
        0xFE,
        (
            "The trick to making fried rice well\x01",
            "Anyhow stir fry with high heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then do not burn the pan\x01",
            "It will be a refreshing texture.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        "Hey, I see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Korat!\x01",
            "Do not look at you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1200)
    OP_64(0xC)
    OP_93(0xC, 0x0, 0x1F4)

    ChrTalk(
        0xC,
        "Well, sorry!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    Jump("loc_2AAF")

    label("loc_2A33")


    ChrTalk(
        0xFE,
        (
            "Oh, already …\x01",
            "It is koga from my side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Failure is properly made\x01",
            "You must eat it yourself! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ui Ui …!\x02",
    )

    CloseMessageWindow()

    label("loc_2AAF")

    OP_4C(0xC, 0xFF)
    Jump("loc_36E5")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB4")

    ChrTalk(
        0xFE,
        (
            "If Crosbell wants independence\x01",
            "I think that I should like it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Empire from the Republic\x01",
            "Safety will not be guaranteed\x01",
            "That's a little problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunsanに１リジュたりとも\x01",
            "There must not be danger.\x01",
            "That's why I'm against you independently.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C3D")

    label("loc_2BB4")


    ChrTalk(
        0xFE,
        (
            "If security is not to be done,\x01",
            "I'm against the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunsanに１リジュたりとも\x01",
            "It is dangerous\x01",
            "It must not exist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3D")

    Jump("loc_36E5")

    label("loc_2C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(
        0xFE,
        (
            "That new bite,\x01",
            "I can not leave my work forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunsanに色目を使うのも\x01",
            "There is no sign of stopping in all directions ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, this time tight ~ a moxibustion\x01",
            "Would you like me to keep it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D82")

    label("loc_2D08")


    ChrTalk(
        0xFE,
        (
            "そもそも、Sunsanに\x01",
            "There are too many people who use eyelids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there were any fellows who could give out ……\x01",
            "…… Hun, I will not say it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D82")

    Jump("loc_36E5")

    label("loc_2D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E44")

    ChrTalk(
        0xFE,
        (
            "The table is noisy this morning\x01",
            "Was not it right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President of the Republic\x01",
            "She said she entered the crossbell\x01",
            "It was a story, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who will disturb the peace of I\x01",
            "I can not forgive him no matter what.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E97")

    label("loc_2E44")


    ChrTalk(
        0xFE,
        "I like calm shops.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who will disturb that peace\x01",
            "I can not forgive him no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E97")

    Jump("loc_36E5")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3102")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Oh, I was at the table earlier.\x01",
            "A small customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How was your meal?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        "The smaller is superfluous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "However, the direction of cooking is satisfactory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "However, that price is too cheap for that quality.\x01",
            "Shopkeeper also worth more value -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, the customer.\x01",
            "Although he is still young, Tyjean's clever son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, thank you for remembering,\x01",
            "Here is the Ryuushu restaurant of \"common people\".\x01",
            "I do not want to be a store with a high threshold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Therefore,\x01",
            "I do not intend to change the price now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I see, I see … ….\x01",
            "I misread it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F(Huh, what mind is obedient.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1DC, 5)
    Jump("loc_317D")

    label("loc_3102")


    ChrTalk(
        0x8,
        (
            "But small customers.\x01",
            "It is quite yet young\x01",
            "You know the difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ほんと、packとRuthにも\x01",
            "I want to emulate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317D")

    Jump("loc_330E")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3275")

    ChrTalk(
        0xFE,
        (
            "Towards the commerce meeting from tomorrow,\x01",
            "A fair number of reporters also enter the crossbell\x01",
            "I'm talking about doing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "フン、中にはSunsanの写真を\x01",
            "I try to take photos on my own\x01",
            "There may be reporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there was such a person,\x01",
            "I will not tolerate you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_330E")

    label("loc_3275")


    ChrTalk(
        0xFE,
        (
            "記者の中にはSunsanの写真を\x01",
            "There seems to be some people trying to photograph themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is a woman's reporter,\x01",
            "If a male reporter would do such a thing\x01",
            "I will not tolerate you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330E")

    Jump("loc_36E5")

    label("loc_3313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_343F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C8")

    ChrTalk(
        0xFE,
        (
            "By the way, in the old city\x01",
            "Red jersey villains,\x01",
            "You rarely show your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They are not\x01",
            "I wanted to drink it with Tsuke\x01",
            "Is not it going to step down?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_343A")

    label("loc_33C8")


    ChrTalk(
        0xFE,
        (
            "Sunsanに手を出しそうな輩が\x01",
            "I do not mind being willing to reduce it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After returning Takehito\x01",
            "I want you, absolutely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343A")

    Jump("loc_36E5")

    label("loc_343F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_END)), "loc_359C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3511")

    ChrTalk(
        0xFE,
        (
            "I also want to thank you\x01",
            "When I can make a new disciple\x01",
            "I thought ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, if you are wrong, you can not help it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The handbook I handed\x01",
            "You can use it as you like,\x01",
            "You should at least step forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3597")

    label("loc_3511")


    ChrTalk(
        0xFE,
        (
            "The handbook I handed\x01",
            "You can use it as you like,\x01",
            "You should at least step forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The tips of growth,\x01",
            "To cook anyway.\x01",
            "… You got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3597")

    Jump("loc_36E5")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3656")

    ChrTalk(
        0xFE,
        (
            "The customer went unnoticed\x01",
            "You must not enter the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway,\x01",
            "This is for chefs\x01",
            "Because it is a sanctuary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'd like to join my disciple.\x01",
            "If it says, the story is different.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36E5")

    label("loc_3656")


    ChrTalk(
        0xFE,
        (
            "If you would like to learn toasty cuisine,\x01",
            "It is not bothersome to teach me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If not,\x01",
            "In this kitchen sanctuary\x01",
            "Do not get in uncanny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E5")

    TalkEnd(0xFE)
    Return()

    # Function_6_1556 end

    def Function_7_36E9(): pass

    label("Function_7_36E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380E")

    ChrTalk(
        0xFE,
        (
            "Hehe, it's a strange sight\x01",
            "I do not care how I cook\x01",
            "Well, it seems like a master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried about the republic's bag,\x01",
            "The more the empire the civil war is going on\x01",
            "It might be a dangerous situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not care about the castle which I am distracting.\x01",
            "I am afraid I got a solid master.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38B9")

    label("loc_380E")


    ChrTalk(
        0xFE,
        (
            "I am worried about the republic's bag,\x01",
            "The more the empire the civil war is going on\x01",
            "It might be a dangerous situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not care about the castle which I am distracting.\x01",
            "I am afraid I got a solid master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B9")

    Jump("loc_45E8")

    label("loc_38BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3943")

    ChrTalk(
        0xFE,
        (
            "To be something tons of tons\x01",
            "It was getting messed up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's a shop\x01",
            "If you are doing it\x01",
            "Hey maybe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E9")

    ChrTalk(
        0xFE,
        (
            "If I miss today,\x01",
            "For a while to the Republic\x01",
            "I guess it is hard to get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Mother of the Republic, are you worried?\x01",
            "I wonder if I should go home ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A63")

    label("loc_39E9")


    ChrTalk(
        0xFE,
        (
            "しっかし、Lishaちゃんも\x01",
            "I wonder where he really went ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunsanも心配してるし、\x01",
            "I wish I could hear from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A63")

    Jump("loc_45E8")

    label("loc_3A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A76")
    Jump("loc_45E8")

    label("loc_3A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3AD7")

    ChrTalk(
        0xFE,
        "It is somehow recently noisy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright\x01",
            "I do not care what you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDE")

    ChrTalk(
        0xFE,
        (
            "Bytes,\x01",
            "Apparently more chores than before\x01",
            "It seems that he decided to try hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, until now\x01",
            "『うだつの上がらないpackとRuth』\x01",
            "How I was calling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally,\x01",
            "『そこそこ見所のあるpackとRuth』\x01",
            "Was it because it became it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C67")

    label("loc_3BDE")


    ChrTalk(
        0xFE,
        (
            "packとRuthも、ようやく\x01",
            "A spirited way of thinking\x01",
            "It seems that he could throw it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as there are a few places\x01",
            "I guess it is getting started.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C67")

    Jump("loc_45E8")

    label("loc_3C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D04")

    ChrTalk(
        0xFE,
        (
            "packもRuthも、\x01",
            "Their immaturity\x01",
            "Thinking it is awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to recover here.\x01",
            "Even if you start business\x01",
            "I do not think it will continue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEF")

    ChrTalk(
        0xFE,
        (
            "packとRuthの野郎、\x01",
            "I do not want you to do a better job\x01",
            "I was sipping a cheeky mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also used to say something similar\x01",
            "I got angry at the master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a wonderful work for chores,\x01",
            "Do not understand properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E60")

    label("loc_3DEF")


    ChrTalk(
        0xFE,
        (
            "Any work,\x01",
            "More than given\x01",
            "I must take pride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ok, well of the master\x01",
            "It is a selling out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_45E8")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F11")

    ChrTalk(
        0xFE,
        (
            "So, also in the Republic\x01",
            "Have not returned home for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's fun to work here\x01",
            "I do not mind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes to bag\x01",
            "I wish to contact you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F51")

    label("loc_3F11")


    ChrTalk(
        0xFE,
        (
            "Sometimes to bag\x01",
            "I wish to contact you.\x01",
            "You have returned so much …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F51")

    Jump("loc_45E8")

    label("loc_3F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407A")

    ChrTalk(
        0xFE,
        (
            "Somehow I still, to the master\x01",
            "“Sunsanに手を出しそうな輩”に\x01",
            "It looks like it is listed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was also pressed by a byte caretaker,\x01",
            "Sunsanに手を出させないように\x01",
            "That is why … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "うーん、俺にとっちゃSunsanは\x01",
            "It is like my sister.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_410E")

    label("loc_407A")


    ChrTalk(
        0xFE,
        (
            "I keep company with Master for a long time,\x01",
            "俺にとっちゃSunsanは\x01",
            "It is like a little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Watching over,\x01",
            "I do not plan to put out my hands\x01",
            "I do not have it at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410E")

    Jump("loc_45E8")

    label("loc_4113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41CF")

    ChrTalk(
        0xFE,
        (
            "In rumors Master,\x01",
            "Especially in a place where security is poor in the eastern people street\x01",
            "I wish I could open a store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I met the Master\x01",
            "It's a crossbell, but the old story\x01",
            "You do not do almost it ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_41CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C3")

    ChrTalk(
        0xFE,
        (
            "Master of the Oriental martial arts\x01",
            "Preference#2RTaste#She seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was in the East Street Town,\x01",
            "Rough comers to the store\x01",
            "It's a story that I dismissed myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunsanに近づく男を睨みつける\x01",
            "To the sharpness of that eye,\x01",
            "It is because I am convinced.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_432F")

    label("loc_42C3")


    ChrTalk(
        0xFE,
        (
            "Master of the Oriental martial arts\x01",
            "Preference#2RTaste#She seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, if you really get angry\x01",
            "You may regret it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432F")

    Jump("loc_45E8")

    label("loc_4334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4420")

    ChrTalk(
        0xFE,
        (
            "実はこの間、Lishaちゃんに\x01",
            "I tried to apply motion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was no appearance at all,\x01",
            "After a fresh greeting\x01",
            "I went to practice and went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than love,\x01",
            "Alcane shell is fun\x01",
            "Looks like it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44B6")

    label("loc_4420")


    ChrTalk(
        0xFE,
        (
            "Lishaちゃん、\x01",
            "Now the alkane shell\x01",
            "I guess it's fun and unavoidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess\x01",
            "I am spending time with Peppermint\x01",
            "I am ashamed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B6")

    Jump("loc_45E8")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_45E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_455D")

    ChrTalk(
        0xFE,
        (
            "新入りのpackとRuthに、\x01",
            "Accounting, cleaning, dish-washing etc\x01",
            "I decided to give up chores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally I also in the kitchen\x01",
            "I can concentrate on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_45E8")

    label("loc_455D")


    ChrTalk(
        0xFE,
        (
            "新入りのpackとRuthに、\x01",
            "I decided to delegate miscellaneous in general.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even on the back of the counter\x01",
            "From the time I could not get it in\x01",
            "I guess he has made progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E8")

    TalkEnd(0xFE)
    Return()

    # Function_7_36E9 end

    def Function_8_45EC(): pass

    label("Function_8_45EC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_46FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4602")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "To take a break\x01",        # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4675")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4675")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4694")
    OP_AF(0x34)
    Jump("loc_4696")

    label("loc_4694")

    OP_AF(0x33)

    label("loc_4696")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46F5")

    label("loc_46A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C5")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46F5")

    label("loc_46C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D9")
    Jump("loc_46F5")

    label("loc_46D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_46F5")

    Jump("loc_4602")

    label("loc_46FA")

    Jump("loc_4702")

    label("loc_46FF")

    Call(0, 9)

    label("loc_4702")

    TalkEnd(0xA)
    Return()

    # Function_8_45EC end

    def Function_9_4706(): pass

    label("Function_9_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A08")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4731")
    Call(0, 11)
    Jump("loc_48A4")

    label("loc_4731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482F")

    ChrTalk(
        0xA,
        (
            "Lishaたち、\x01",
            "From now on to dangerous places\x01",
            "I guess it will get on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually I want to stop it … ….\x01",
            "Lishaが行くって言うなら\x01",
            "I can not stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be waiting … ….\x01",
            "Please come home safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10704FYeah … … I will definitely come back.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_48A4")

    label("loc_482F")


    ChrTalk(
        0xA,
        (
            "Lishaたち、\x01",
            "From now on to dangerous places\x01",
            "I guess it will get on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be waiting … ….\x01",
            "Please come home safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A4")

    Jump("loc_4A03")

    label("loc_48A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48BB")
    Call(0, 10)
    Jump("loc_4A03")

    label("loc_48BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498E")

    ChrTalk(
        0xA,
        (
            "Lishaたち、\x01",
            "From now on to dangerous places\x01",
            "I guess it will get on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually I want to stop it … ….\x01",
            "Lishaが行くって言うなら\x01",
            "I can not stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be waiting … ….\x01",
            "Please come home safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A03")

    label("loc_498E")


    ChrTalk(
        0xA,
        (
            "Lishaたち、\x01",
            "From now on to dangerous places\x01",
            "I guess it will get on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be waiting … ….\x01",
            "Please come home safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A03")

    Jump("loc_5B57")

    label("loc_4A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4B79")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A33")
    Call(0, 11)
    Jump("loc_4AE4")

    label("loc_4A33")


    ChrTalk(
        0xA,
        (
            "Gusu …\x01",
            "Lishaにまた会えて\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Next time, if I go out silently\x01",
            "I will never forgive you! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah … I promise.\x01",
            "ありがとう、Sunsan。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE4")

    Jump("loc_4B74")

    label("loc_4AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AFB")
    Call(0, 10)
    Jump("loc_4B74")

    label("loc_4AFB")


    ChrTalk(
        0xA,
        (
            "Gusu …\x01",
            "Lishaにまた会えて\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Next time, if I go out silently\x01",
            "I will never forgive you! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B74")

    Jump("loc_5B57")

    label("loc_4B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3F")

    ChrTalk(
        0xA,
        (
            "Crossbell to this\x01",
            "I guess … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If it comes to war,\x01",
            "本当にもうLishaに\x01",
            "I feel like I will not be able to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Lisha、今どこにいるの……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4CB7")

    label("loc_4C3F")


    ChrTalk(
        0xA,
        (
            "If it comes to war,\x01",
            "本当にもうLishaに\x01",
            "I feel like I will not be able to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Lisha、今どこにいるの……？\x02",
    )

    CloseMessageWindow()

    label("loc_4CB7")

    Jump("loc_5B57")

    label("loc_4CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CEE")
    Call(0, 53)
    Return()

    label("loc_4CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E24")

    ChrTalk(
        0xA,
        (
            "……Lisha、いなくなる直前に\x01",
            "You left me a deposit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "\"Cross Bell with circumstances\x01",
            "I decided to leave. \"\x01",
            "I was wondering why … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Leave the alkane shell\x01",
            "Absolutely not going to disappear\x01",
            "Lishaらしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "… … Did something happen?\x01",
            "I wish I had consulted … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EA1")

    label("loc_4E24")


    ChrTalk(
        0xA,
        (
            "Leave the alkane shell\x01",
            "I can not lose it.\x01",
            "Lishaらしくないよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can not talk to my best friend\x01",
            "I wonder if there were circumstances ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA1")

    Jump("loc_4F23")

    label("loc_4EA6")


    ChrTalk(
        0xA,
        (
            "Good Luck and MISCON\x01",
            "I will make you excitement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At the start of the program\x01",
            "Because I go to make it in time,\x01",
            "Please contact me later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F23")

    Jump("loc_5B57")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506C")

    ChrTalk(
        0xA,
        (
            "Today, early in the morning\x01",
            "Going to alkane shell\x01",
            "Lishaを見かけたね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I greeted you ….\x01",
            "I mean\x01",
            "I did not feel at ease.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_END)), "loc_5009")

    ChrTalk(
        0x101,
        (
            "#00008F(… for now\x01",
            "There is no other choice but to keep it … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5064")

    label("loc_5009")


    ChrTalk(
        0x101,
        (
            "#00003F（……Lisha……\x01",
            "To the alkane shell\x01",
            "Let's go see the state … ….? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5064")

    SetScenarioFlags(0x0, 2)
    Jump("loc_50E9")

    label("loc_506C")


    ChrTalk(
        0xA,
        (
            "朝、見かけたLisha……\x01",
            "I did not feel at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……What happened.\x01",
            "If you can ride consultation\x01",
            "I'd like to ride.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E9")

    Jump("loc_5B57")

    label("loc_50EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_51ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517C")

    ChrTalk(
        0xA,
        (
            "Lisha、用事があるからって\x01",
            "I went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Let's talk a little bit more\x01",
            "I wanted to do it … but it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E8")

    label("loc_517C")


    ChrTalk(
        0xA,
        (
            "もう少しLishaと\x01",
            "I wanted to talk but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If it's a business you can not help it.\x01",
            "…… I have to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E8")

    Jump("loc_5B57")

    label("loc_51ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_526E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5208")
    Call(0, 48)
    Jump("loc_5269")

    label("loc_5208")


    ChrTalk(
        0xA,
        (
            "えへへ……Lishaに\x01",
            "I'm ashamed of being told so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "一生の友達でいようね、Lisha！\x02",
    )

    CloseMessageWindow()

    label("loc_5269")

    Jump("loc_5B57")

    label("loc_526E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52E6")

    ChrTalk(
        0xA,
        (
            "packとRuth、\x01",
            "After all my work has not clung up\x01",
            "I got back to the original shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "People and papa are also bad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B57")

    label("loc_52E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_549F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5387")

    ChrTalk(
        0xA,
        (
            "…… Gourmet guide coverage?\x01",
            "Oh, I've heard the story ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Daddy is in the kitchen,\x01",
            "Can you ask me that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_5387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5430")

    ChrTalk(
        0xA,
        (
            "Dad and Fay,\x01",
            "Today I just need your bill\x01",
            "I was pushed into here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……packとRuthがすっごく\x01",
            "I heard that I am busy, is it okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_549A")

    label("loc_5430")


    ChrTalk(
        0xA,
        (
            "今日はpackが\x01",
            "She seems to do all the waiters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… I am very busy.\x01",
            "I wonder if I do not really need to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_549A")

    Jump("loc_5B57")

    label("loc_549F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5546")

    ChrTalk(
        0xA,
        (
            "welcome.\x01",
            "Would you like to order something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone who comes somehow,\x01",
            "It seems like a topic of a trade meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What the mayor said,\x01",
            "Was it such a serious thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B57")

    label("loc_5546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F9")

    ChrTalk(
        0xA,
        (
            "幼馴染のpackとRuthを\x01",
            "It is my recommendation to Byte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah yeah, for two people\x01",
            "I am impressed and feeling like I'm doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My nose is high as I asked for daddy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5661")

    label("loc_55F9")


    ChrTalk(
        0xA,
        (
            "packとRuth、\x01",
            "I work part-time properly\x01",
            "Looks like I'm doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My nose is high as I asked for daddy.\x02",
    )

    CloseMessageWindow()

    label("loc_5661")

    Jump("loc_5B57")

    label("loc_5666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_57B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5744")

    ChrTalk(
        0xA,
        (
            "Papa says, the Republic\x01",
            "More than crossbell\x01",
            "They are a country with many Toho people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I was a child, here\x01",
            "Because I have migrated.\x01",
            "I hardly remember it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It looks like a very lively place.\x01",
            "Sounds fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_57B4")

    label("loc_5744")


    ChrTalk(
        0xA,
        (
            "Republic from Crossbell\x01",
            "There seems to be many Toho people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's lively and fun ~.\x01",
            "I would like to go if there is opportunity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B4")

    Jump("loc_5B57")

    label("loc_57B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584C")
    TurnDirection(0xA, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        "Oh, a pretty customer just before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please come back again, I will always be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Oh, ah ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_58D8")

    label("loc_584C")


    ChrTalk(
        0xA,
        (
            "A woman sitting at that counter seat,\x01",
            "He was a reporter of Libert ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huh, because it's painful\x01",
            "I wonder if you can take a cute picture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D8")

    Jump("loc_5B57")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CB")

    ChrTalk(
        0xA,
        (
            "まったくFenさんったら、\x01",
            "Lishaをナンパするなんて\x01",
            "A troubled person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Lishaだったら、\x01",
            "In the future, too - human beings\x01",
            "You should find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fenさんには失礼かもだけど、\x01",
            "As a close friend I can not hand it over.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A3E")

    label("loc_59CB")


    ChrTalk(
        0xA,
        (
            "Lishaだったら、\x01",
            "In the future, too - human beings\x01",
            "It should be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, my best friend, I\x01",
            "I will guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A3E")

    Jump("loc_5B57")

    label("loc_5A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC4")

    ChrTalk(
        0xA,
        (
            "welcome.\x01",
            "About your favorite seats ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Dad is a bit scary,\x01",
            "The taste of cooking is the best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B57")

    label("loc_5AC4")


    ChrTalk(
        0xA,
        (
            "Started to help the store\x01",
            "Although it's not more than a year ago,\x01",
            "I've gotten used to work as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "People are good people,\x01",
            "In this way it will be able to continue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B57")

    Return()

    # Function_9_4706 end

    def Function_10_5B58(): pass

    label("Function_10_5B58")


    ChrTalk(
        0xA,
        (
            "Lisha……\x01",
            "I wonder what they are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell to this\x01",
            "Becoming … … I worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(… … It would be better to bring him back later\x01",
            "It might be nice … …)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_10_5B58 end

    def Function_11_5BFF(): pass

    label("Function_11_5BFF")

    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    ChrTalk(
        0xA,
        (
            "リ、Lisha……\x01",
            "Lishaだよね！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Where are you until now? Is it?\x01",
            "I was so worried … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703Fごめんなさい、Sunsan……\x01",
            "Please worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uu … … It is true!\x01",
            "Lishaのばかばか！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But ….\x01",
            "I am glad to see you again … ….\x01",
            "Yeah yeah yeah ~ ~ ~ … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x106)

    ChrTalk(
        0x106,
        "#10705Fな、泣かないでSunsan……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gusu … … Because,\x01",
            "I was really worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Next time, if I go out silently\x01",
            "I will never forgive you! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYes, I'm really sorry.\x01",
            "…… Thank you for waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F（Lisha……良かったな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 0)
    Return()

    # Function_11_5BFF end

    def Function_12_5E5C(): pass

    label("Function_12_5E5C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5F6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "To take a break\x01",        # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EE5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5EE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F04")
    OP_AF(0x34)
    Jump("loc_5F06")

    label("loc_5F04")

    OP_AF(0x33)

    label("loc_5F06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F65")

    label("loc_5F15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F35")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F65")

    label("loc_5F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F49")
    Jump("loc_5F65")

    label("loc_5F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F65")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_5F65")

    Jump("loc_5E72")

    label("loc_5F6A")

    Jump("loc_5F72")

    label("loc_5F6F")

    Call(0, 13)

    label("loc_5F72")

    TalkEnd(0xB)
    Return()

    # Function_12_5E5C end

    def Function_13_5F76(): pass

    label("Function_13_5F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_60A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6032")

    ChrTalk(
        0xB,
        (
            "Everyone is happy if they are full.\x01",
            "That's the master motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "将来Ruthと店をやるときには\x01",
            "Thinking of customers like that,\x01",
            "I want to work hard on my job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60A0")

    label("loc_6032")


    ChrTalk(
        0xB,
        (
            "That's why today's free of charge,\x01",
            "It's free for meals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Eating hard,\x01",
            "Please give me the spirit!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A0")

    Jump("loc_6C17")

    label("loc_60A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_612D")

    ChrTalk(
        0xB,
        (
            "I wonder if I have time to clean up.\x01",
            "…… However, where\x01",
            "I can not escape … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ha ha … only a sigh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_612D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_61A9")

    ChrTalk(
        0xB,
        (
            "I wonder what will become of it,\x01",
            "I have no idea at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is the time\x01",
            "I have to survive with the spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_61A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626C")

    ChrTalk(
        0xB,
        (
            "Mr. Fei\x01",
            "Charity event\x01",
            "Go to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I entered the kitchen instead\x01",
            "I am assisting the Master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As much as I can\x01",
            "I should do what I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62DE")

    label("loc_626C")


    ChrTalk(
        0xB,
        (
            "I can not do it\x01",
            "It's a chore at a time but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There is not Fei,\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62DE")

    Jump("loc_6C17")

    label("loc_62E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6389")

    ChrTalk(
        0xB,
        "100, 200, 300 Mirat …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To, from Oita before\x01",
            "The counter industry got better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Only I did it,\x01",
            "You are growing properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_645D")

    ChrTalk(
        0xB,
        (
            "Job only\x01",
            "I thought it would be anything but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all somewhere\x01",
            "Perhaps my idea was sweet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, I will do what I can do now!\x01",
            "I knew it was important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_64C3")

    label("loc_645D")


    ChrTalk(
        0xB,
        (
            "昨日はRuthの奴と一緒に、\x01",
            "Although it was dented quite a lot ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, what I can do now\x01",
            "I do not have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C3")

    Jump("loc_6C17")

    label("loc_64C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6548")

    ChrTalk(
        0xB,
        "Ha, I'm tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sunsanの仕事を見てたら\x01",
            "I thought that it was just fun,\x01",
            "I did not do that at all …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65BE")

    ChrTalk(
        0xB,
        (
            "Wiping the table,\x01",
            "Take orders and carry cooking ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ooo, I'm too busy.\x01",
            "Eyes will spin … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_65BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B6")

    ChrTalk(
        0xB,
        (
            "Ruthがバイト代を増やすために、\x01",
            "Making a job more important post\x01",
            "I ask you to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Indeed for the future\x01",
            "I do not have to earn money here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "ま、オレとRuthなら\x01",
            "In any fighting spirit\x01",
            "You can get over it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_670C")

    label("loc_66B6")


    ChrTalk(
        0xB,
        (
            "To the unexpected, I am a clerk\x01",
            "I may have talent … …\x01",
            "I wonder if I will ask the master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670C")

    Jump("loc_6C17")

    label("loc_6711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6814")

    ChrTalk(
        0xB,
        (
            "オレとRuthとSunsanは\x01",
            "Sunday school days\x01",
            "I am a classmate, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From that time on, Master,\x01",
            "Sunsanに関わるだけで\x01",
            "I have a scary face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "さっきも、Sunsanに\x01",
            "Just a greeting\x01",
            "I was scared of being scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha, I want you to forgive me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_688F")

    label("loc_6814")


    ChrTalk(
        0xB,
        (
            "SunsanにJust a greeting\x01",
            "I was scolded by the master … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since Sunday school days\x01",
            "It is like this … …\x01",
            "I want you to forgive me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_688F")

    Jump("loc_6C17")

    label("loc_6894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6933")

    ChrTalk(
        0xB,
        (
            "Ruthはなんでもかんでも\x01",
            "I'm trying to put it in a mold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why did you decide to place a shop\x01",
            "Even if you go to a restaurant\x01",
            "I do not mind at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_6933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69D8")

    ChrTalk(
        0xB,
        (
            "Ruthの奴、なんだか色々と\x01",
            "I guess it is too much thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm doing my best this time,\x01",
            "We are surely becoming big!\x01",
            "There is nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C17")

    label("loc_69D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A66")

    ChrTalk(
        0xB,
        (
            "Please count on me.\x01",
            "Sliding exactly a while ago\x01",
            "I got a rice cake touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ooo, this kind of pain,\x01",
            "I'll blow it away with the spirit!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6ADB")

    label("loc_6A66")


    ChrTalk(
        0xB,
        (
            "Please give it to me.\x01",
            "Well Whether you are going to sing a fight or not\x01",
            "Does pain hurts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because it will ride on a rainy day\x01",
            "You also should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADB")

    Jump("loc_6C17")

    label("loc_6AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB7")

    ChrTalk(
        0xB,
        (
            "少し前から、相棒のRuthと一緒に\x01",
            "I have been bite-bye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, the counter industry is\x01",
            "I'm not very good at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's fun,\x01",
            "Do not count the mirrors\x01",
            "All I can do is get angry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C17")

    label("loc_6BB7")


    ChrTalk(
        0xB,
        (
            "Well,\x01",
            "Even restaurant staff\x01",
            "It fits quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm having fun doing it.\x02",
    )

    CloseMessageWindow()

    label("loc_6C17")

    Return()

    # Function_13_5F76 end

    def Function_14_6C18(): pass

    label("Function_14_6C18")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_6D2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D26")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "To take a break\x01",        # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6CA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6CC0")
    OP_AF(0x34)
    Jump("loc_6CC2")

    label("loc_6CC0")

    OP_AF(0x33)

    label("loc_6CC2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D21")

    label("loc_6CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF1")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D21")

    label("loc_6CF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D05")
    Jump("loc_6D21")

    label("loc_6D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D21")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 15)

    label("loc_6D21")

    Jump("loc_6C2E")

    label("loc_6D26")

    Jump("loc_6D2E")

    label("loc_6D2B")

    Call(0, 15)

    label("loc_6D2E")

    TalkEnd(0xC)
    Return()

    # Function_14_6C18 end

    def Function_15_6D32(): pass

    label("Function_15_6D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E15")

    ChrTalk(
        0xC,
        (
            "Experience of hard work in times of difficulty\x01",
            "It will be absolutely useful in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "将来、相棒のpackと\x01",
            "I am planning to open a big shop ….\x01",
            "I have to work hard in front of my eyes now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Well then, if we decide so\x01",
            "I'm sweeping off by myself! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6E9E")

    label("loc_6E15")


    ChrTalk(
        0xC,
        (
            "Experience of hard work in times of difficulty\x01",
            "将来、packと商店を開いた時にも\x01",
            "It will be absolutely useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Well then, if we decide so\x01",
            "I'm sweeping off by myself! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9E")

    Jump("loc_7C4D")

    label("loc_6EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F03")

    ChrTalk(
        0xC,
        "I guess that's going outside like this …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What are we going to do …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F77")

    ChrTalk(
        0xC,
        (
            "Hyakko, crossbell\x01",
            "What is to become an independent country!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wow, that is awful.\x01",
            "Heat will get in for cleaning too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6FE7")

    ChrTalk(
        0xC,
        (
            "The old town is somewhere near,\x01",
            "Eastern Street as well\x01",
            "It might have been like a similar thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "… ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_6FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7088")

    ChrTalk(
        0xC,
        (
            "Hmm, because it's troublesome until now\x01",
            "I also swept the square floor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is better to do it properly from the edge\x01",
            "It's rather quick.\x01",
            "The cleaning is also deep inside … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_7088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_729A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_714A")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage … …?\x01",
            "Oh, that's right Master\x01",
            "It looks like he was saying such a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because the master is in the kitchen,\x01",
            "Try to talk over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_714A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722B")

    ChrTalk(
        0xC,
        (
            "Yesterday, experiencing the kitchen\x01",
            "Although it seemed to be apt to get weathered ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "packと話し合って、\x01",
            "I can do what I can do right now\x01",
            "I decided to do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Someone who can not even do simple work\x01",
            "It is not easy to get a tough task\x01",
            "I did not have it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7295")

    label("loc_722B")


    ChrTalk(
        0xC,
        (
            "将来、相棒のpackと\x01",
            "To open a big store ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now choreographed perfectly\x01",
            "I hope to be able to do this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7295")

    Jump("loc_7C4D")

    label("loc_729A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7306")

    ChrTalk(
        0xC,
        (
            "… … From kitchen hell\x01",
            "Finally it was released ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We are not at all\x01",
            "I was wrong ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4D")

    label("loc_7306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7395")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Oh, fever …!\x01",
            "Also,\x01",
            "O, heavy … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Look, I'm going to hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, sorry!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_7410")

    label("loc_7395")


    ChrTalk(
        0xC,
        (
            "Hi, hoes ……\x01",
            "When I helped before\x01",
            "I thought it was an easy victory … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I will make one fried rice\x01",
            "It was such a hard time ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7410")

    Jump("loc_7C4D")

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_764B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D7")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage … …?\x01",
            "Oh, that's right Master\x01",
            "It looks like he was saying such a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because the master is in the kitchen,\x01",
            "Try to talk over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7646")

    label("loc_74D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B9")

    ChrTalk(
        0xC,
        (
            "Indeed, with Tamanakamata\x01",
            "It's a mere chore\x01",
            "I can not afford funds ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Together, to the master\x01",
            "Step up work\x01",
            "Do you consult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "なーに、オレとRuthなら\x01",
            "Any job\x01",
            "Just a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7646")

    label("loc_75B9")


    ChrTalk(
        0xC,
        (
            "Sooner or later, I will escape from chores\x01",
            "I have to step up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it was a kitchen,\x01",
            "I just helped a little before … …\x01",
            "I will consult the master this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7646")

    Jump("loc_7C4D")

    label("loc_764B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7724")

    ChrTalk(
        0xC,
        (
            "Successively clean the part to be cleaned\x01",
            "It has been doubled as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "もしかしてpackのやつ、\x01",
            "マスターの前でSunsanに\x01",
            "Did you talk to me …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If so, is this a joint liability?\x01",
            "Sea urchin\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7784")

    label("loc_7724")


    ChrTalk(
        0xC,
        (
            "Oh, later\x01",
            "I have to clean the back of the store ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "packがうっかりしてたせいで\x01",
            "It's a soldering cleaning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7784")

    Jump("loc_7C4D")

    label("loc_7789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_784C")

    ChrTalk(
        0xC,
        (
            "packが、将来の俺たちの商店に\x01",
            "I wonder if you can make it in the cafeteria,\x01",
            "What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well …\x01",
            "Even though minimum funds are not accumulated\x01",
            "I guess the story is getting chaotic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_78C4")

    label("loc_784C")


    ChrTalk(
        0xC,
        (
            "将来、packとデカい商店を\x01",
            "I'm planning to open ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Whether to put a dining room,\x01",
            "I guess the story is getting chaotic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78C4")

    Jump("loc_7C4D")

    label("loc_78C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_79E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7974")

    ChrTalk(
        0xC,
        (
            "packの奴、なんだか結構\x01",
            "I am enjoying this byte\x01",
            "It looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Two people shop a store\x01",
            "You forget the original purpose\x01",
            "I do not think so …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_79E3")

    label("loc_7974")


    ChrTalk(
        0xC,
        (
            "To the end the byte\x01",
            "Mira for putting out a store\x01",
            "It's a means to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "packの奴、なんだか\x01",
            "Have fun ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E3")

    Jump("loc_7C4D")

    label("loc_79E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ABE")

    ChrTalk(
        0xC,
        (
            "Ha\x01",
            "When listening to rain sounds\x01",
            "It's getting depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mira gotten little by little,\x01",
            "It is far from putting out the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Really like this\x01",
            "If I keep byte,\x01",
            "Will you bring it closer to your dream?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7B2D")

    label("loc_7ABE")


    ChrTalk(
        0xC,
        (
            "Really like this\x01",
            "If I keep byte,\x01",
            "Will you bring it closer to your dream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "後でpackの奴にも\x01",
            "Why do not you ask your opinion ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B2D")

    Jump("loc_7C4D")

    label("loc_7B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC6")

    ChrTalk(
        0xC,
        (
            "相棒のpackと、\x01",
            "To earn money for shopping\x01",
            "I started a byte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Someday to open up our shop\x01",
            "That's why I accumulate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7C4D")

    label("loc_7BC6")


    ChrTalk(
        0xC,
        (
            "But the master is tough\x01",
            "Hourly wages are low … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sunsanに幼馴染のよしみで\x01",
            "I was hired but ….\x01",
            "I regret somehow recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C4D")

    Return()

    # Function_15_6D32 end

    def Function_16_7C4E(): pass

    label("Function_16_7C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D46")

    ChrTalk(
        0xFE,
        (
            "Munching …\x01",
            "Our transport company has also resumed business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until now, transportation routes with the Republic\x01",
            "I was mainly responsible, but for the time being\x01",
            "It is likely to be in the autonomous state only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what you do is not changed so much\x01",
            "I have to keep going.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7DD3")

    label("loc_7D46")


    ChrTalk(
        0xFE,
        (
            "Well, work only within autonomous state\x01",
            "Because it became it,\x01",
            "That's nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's do it properly,\x01",
            "I have to keep going as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD3")

    Jump("loc_89E3")

    label("loc_7DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7DE6")
    Jump("loc_89E3")

    label("loc_7DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA9")

    ChrTalk(
        0xFE,
        (
            "You must be a citizen of the crossbell\x01",
            "Independence is a pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Moreover, that hero,\x01",
            "Arios McClein\x01",
            "It is responsible for national defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even the empire and the republic\x01",
            "It is quite reassuring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7F69")

    label("loc_7EA9")


    ChrTalk(
        0xFE,
        (
            "Until we understand the correspondence between the Empire and the Republic,\x01",
            "It seems that our company is on holiday for a while.\x01",
            "… Well, do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for why crossbell,\x01",
            "I have that \"sword of the wind\".\x01",
            "It will surely protect us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F69")

    Jump("loc_89E3")

    label("loc_7F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8022")

    ChrTalk(
        0xFE,
        (
            "Tangram gate by work\x01",
            "I used it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Air than usual\x01",
            "I did it as a pilgrim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even for persons coming and going, more than usual\x01",
            "It was like I was using mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_807E")

    label("loc_8022")


    ChrTalk(
        0xFE,
        (
            "The border gate is that way,\x01",
            "My job is not going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I'm eating too.\x01",
            "Munching …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_807E")

    Jump("loc_89E3")

    label("loc_8083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8149")

    ChrTalk(
        0xFE,
        (
            "What is Mainz occupied … …\x01",
            "I do not know where it is,\x01",
            "I will do something ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the Crossbell Guard\x01",
            "It seems quite elaborate.\x01",
            "If you leave it to me, is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_81A6")

    ChrTalk(
        0xFE,
        "Unfortunately it is raining today ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Driving is dangerous if it is raining,\x01",
            "Be careful not to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_81A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_82C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_826C")

    ChrTalk(
        0xFE,
        (
            "Apparently, the servant\x01",
            "She seems to have returned to her lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one is it?\x01",
            "Even after a meal after dinner\x01",
            "Or do you order …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Wow! Is it?\x01",
            "Delivery departure time\x01",
            "Is not it over?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_82BE")

    label("loc_826C")


    ChrTalk(
        0xFE,
        (
            "Oh yeah.\x01",
            "Delivery departure time\x01",
            "It has passed a long time ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, hurry and … …\x02",
    )

    CloseMessageWindow()

    label("loc_82BE")

    Jump("loc_89E3")

    label("loc_82C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8348")

    ChrTalk(
        0xFE,
        (
            "Oh …… Today's waiters\x01",
            "Is not she your usual girlfriend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what is it?\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_838C")

    label("loc_8348")


    ChrTalk(
        0xFE,
        (
            "Indeed, this store\x01",
            "Lady of that servant\x01",
            "It is only with a smile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_838C")

    Jump("loc_89E3")

    label("loc_8391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_84F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8471")

    ChrTalk(
        0xFE,
        (
            "With a conducting track,\x01",
            "What is the best performance right now\x01",
            "It is the latest version of Verne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, when becoming a new model\x01",
            "Our company is quite good\x01",
            "I do not think I can get out of hand …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in short, it's about\x01",
            "It is expensive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_84F3")

    label("loc_8471")


    ChrTalk(
        0xFE,
        (
            "To buy the latest type of power guide car\x01",
            "It is not quite possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exceptionally good economy\x01",
            "If it is not a company, it will be tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F3")

    Jump("loc_89E3")

    label("loc_84F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8577")

    ChrTalk(
        0xFE,
        (
            "Well, I also have a trade meeting\x01",
            "It's a bit of awful … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have work,\x01",
            "I feel alright now.\x01",
            "Munching …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8602")

    ChrTalk(
        0xFE,
        (
            "Waa, East Street\x01",
            "It was awfully crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively,\x01",
            "The traffic regulation seems to have been lifted … …\x01",
            "I also have to resume my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_8602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_871B")

    ChrTalk(
        0xFE,
        (
            "Anything from tomorrow from the tangram gate\x01",
            "Toward the East Crossbell Highway,\x01",
            "It seems that traffic regulations will be laid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President of the Republic\x01",
            "I'm coming to the trade meeting,\x01",
            "It seems to put a strict guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I regulate it all day\x01",
            "I do not think so ….\x01",
            "There seems to be some impact on work as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_87C1")

    label("loc_871B")


    ChrTalk(
        0xFE,
        (
            "From the Tangram gate tomorrow\x01",
            "Toward the East Crossbell Highway,\x01",
            "It seems that traffic regulations will be laid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It probably will not be all day … …\x01",
            "Delivery schedule\x01",
            "It seems necessary to review it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87C1")

    Jump("loc_89E3")

    label("loc_87C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_884B")

    ChrTalk(
        0xFE,
        (
            "Certainly, today is a wide area\x01",
            "It is said that it is raining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it gets terrible Hey inside\x01",
            "Who finishes the work\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_884B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_89E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892D")

    ChrTalk(
        0xFE,
        (
            "Today from the Republic\x01",
            "A fair amount of baggage\x01",
            "It's been a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm running across the border.\x01",
            "Crossing the Curie River, crossing the river,\x01",
            "I banged the Tangram Hills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew.\x01",
            "Transportation is not easy, is not it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_89E3")

    label("loc_892D")


    ChrTalk(
        0xFE,
        (
            "共和国とのI'm running across the border.\x01",
            "Crossing the Curie River, crossing the river,\x01",
            "I banged the Tangram Hills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have finished my belly ….\x01",
            "Soon running through the city\x01",
            "Will it come about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E3")

    TalkEnd(0xFE)
    Return()

    # Function_16_7C4E end

    def Function_17_89E7(): pass

    label("Function_17_89E7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I am also worried about the stalls … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Morse and Roy Kun from\x01",
            "Is it okay for me … ….?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_89E7 end

    def Function_18_8A45(): pass

    label("Function_18_8A45")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Lily、俺がついてるから\x01",
            "Calm down, are not you?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_8A45 end

    def Function_19_8A7F(): pass

    label("Function_19_8A7F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Dins、私怖い……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_8A7F end

    def Function_20_8AA0(): pass

    label("Function_20_8AA0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The host of Uchi who is at home also\x01",
            "I hope it is safe ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's like this\x01",
            "I quickly closed the store.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_8AA0 end

    def Function_21_8B19(): pass

    label("Function_21_8B19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2D")
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    label("loc_8B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B4E")
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    label("loc_8B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C69")

    ChrTalk(
        0x25,
        (
            "#03204FUntil things are settled, we\x01",
            "I am going to sit on a while.\x02\x03",
            "After that, both Luberce and the red constellation\x01",
            "The back society of the disappearing crossbell\x01",
            "Let's say you take it slowly.\x02\x03",
            "#03210FHuh, everyone with you\x01",
            "Although it may be conflicting,\x01",
            "Thank you in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8D14")

    label("loc_8C69")


    ChrTalk(
        0x25,
        (
            "#03204FUntil things are settled, we\x01",
            "I am going to sit on a while.\x02\x03",
            "#03210FHuh, everyone with you\x01",
            "Although it may be conflicting,\x01",
            "Thank you in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D14")

    TalkEnd(0xFE)
    Return()

    # Function_21_8B19 end

    def Function_22_8D18(): pass

    label("Function_22_8D18")


    ChrTalk(
        0x25,
        (
            "#03200FOh, Lloyd's … …\x01",
            "Is cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fツァ、Tsaoさん！？\x01",
            "What in a place like this …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FHuh, if we were here\x01",
            "Is something strange?\x02\x03",
            "#03200FBecause the city has calmed down\x01",
            "I am stretching the feathers to the meal\x01",
            "It is only it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThat's it.\x01",
            "It is too dignified ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FMoreover, in the hotel bar\x01",
            "In such a seat in the middle … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "I thought I was somewhat … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Guided by the waitress,\x01",
            "Tsao様も断らなかったもので。\x02",
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
        0x25,
        (
            "#03204FHuh, is not it nice?\x01",
            "As soon as I was having a meal\x01",
            "I want you to do.\x02\x03",
            "#03200FIn Crossbell City's release strategy,\x01",
            "In the fight against \"Red constellation\"\x01",
            "I have broken my bones for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… As for that,\x01",
            "Thank you for your cooperation.\x02\x03",
            "#00001FTsaoさんたちは、これから\x01",
            "What are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03205FFor a while, until the situation gathers\x01",
            "I'm going to decide the sidelines.\x02\x03",
            "#03209FAfter the incident converged in some form,\x01",
            "Establish a new office and work\x01",
            "It will be to resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FAre you after all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204F\"Red constellation\" and Rubathe\x01",
            "Now that the competitors have disappeared,\x01",
            "Because there is no obstacle any longer.\x02\x03",
            "#03202FHuh, there were twists and turns … …\x01",
            "It is said to suppress the back society of crossbell\x01",
            "The initial purpose seems to be achieved at last.\x02\x03",
            "Again, with Lloyds\x01",
            "\"Silver\" that I worked so far\x01",
            "It would not be an exaggeration to say thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013FDamn\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92B9")

    ChrTalk(
        0x106,
        "#10708F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_92B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9314")

    ChrTalk(
        0x10A,
        (
            "#00603F…… Anyway \"black moon\"\x01",
            "I will confront it again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93BD")

    label("loc_9314")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_936D")

    ChrTalk(
        0x109,
        (
            "#10103FWhich is \"black moon\"\x01",
            "It is likely to confront it again …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93BD")

    label("loc_936D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93BD")

    ChrTalk(
        0x105,
        (
            "#10403FWhich is \"black moon\"\x01",
            "It is going to confront again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93BD")


    ChrTalk(
        0x25,
        (
            "#03209FWell, even in such a meaning ……\x01",
            "Thank you in the future,\x01",
            "Everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… what kind of people are you\x01",
            "I tried to stand as a \"wall\" ……\x02\x03",
            "#00001FWe will never lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03209FHuh, that's it, Mr. Lloyd.\x02\x03",
            "#03204FWell, as we \"wall\"\x01",
            "It will not be a big deal.\x02\x03",
            "#03210FConfusion throughout the continent …\x01",
            "Compared to the threat of West in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F…. That's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FHuh, well for a while\x01",
            "In order to converge this situation\x01",
            "Please do your best.\x02\x03",
            "#03200FHere we are,\x01",
            "I will support you with a shadow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 1)
    Return()

    # Function_22_8D18 end

    def Function_23_95D4(): pass

    label("Function_23_95D4")


    ChrTalk(
        0x25,
        (
            "#03204FOh yeah … when the situation gathers up,\x01",
            "Lishaさんにも改めて契約を\x01",
            "I am thinking of asking you.\x02\x03",
            "#03202Fフフ、Lishaさんの\x01",
            "How is convenience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F…… I could borrow this time\x01",
            "I wish I could thank you in some way\x01",
            "I am thinking … ….\x02\x03",
            "#10701FNow, still, that question\x01",
            "I can not say \"yes\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FLisha……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FWell, also here\x01",
            "I do not have the right to force.\x02\x03",
            "Also for this time,\x01",
            "It was an equal cooperation to the last\x01",
            "There will be no borrowing and borrowing.\x02\x03",
            "#03200Fですが、それでLishaさんが\x01",
            "If you say you feel negative …\x02\x03",
            "#03209FAlcan Shell's S seat tickets as well\x01",
            "Is it reasonable if it is possible?\x02",
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
        0x25,
        (
            "#03204FHuh, it is a joke.\x02\x03",
            "#03200FJust … … As I said before,\x01",
            "In order for \"Black Moon\" to aim for height\x01",
            "I still want your power.\x02\x03",
            "I will support the stage,\x01",
            "I look forward to having a good relationship in the future\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 2)
    Return()

    # Function_23_95D4 end

    def Function_24_9964(): pass

    label("Function_24_9964")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9979")
    Call(0, 22)
    Jump("loc_9AC8")

    label("loc_9979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A45")

    ChrTalk(
        0xFE,
        (
            "…… Regarding this matter,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The hiding place of the battlefield, too,\x01",
            "It is the place I paid for it earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What we can cooperate with\x01",
            "I do not have any more … …\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9AC8")

    label("loc_9A45")


    ChrTalk(
        0xFE,
        (
            "The hiding place of the battlefield, too,\x01",
            "It is the place I paid for it earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What we can cooperate with\x01",
            "I do not have any more … …\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC8")

    TalkEnd(0xFE)
    Return()

    # Function_24_9964 end

    def Function_25_9ACC(): pass

    label("Function_25_9ACC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Today my whole family came to eat out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe he seems to be enjoying\x01",
            "Anything else.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_9ACC end

    def Function_26_9B2E(): pass

    label("Function_26_9B2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BF8")

    ChrTalk(
        0xFE,
        "Phaphhe, Chulubiru ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This Tanmen, too,\x01",
            "It is spicy and exciting taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meals sweat so much\x01",
            "It was not until I was born ……\x01",
            "However, it is very delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9C6C")

    label("loc_9BF8")


    ChrTalk(
        0xFE,
        (
            "This dish called Tanmen,\x01",
            "I liked it very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am perspiring because of spicyness,\x01",
            "It is very delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C6C")

    TalkEnd(0xFE)
    Return()

    # Function_26_9B2E end

    def Function_27_9C70(): pass

    label("Function_27_9C70")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today all the family members\x01",
            "I came to eat out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumumumu ……\x01",
            "This \"well-being\"\x01",
            "It is quiet.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_9C70 end

    def Function_28_9CE8(): pass

    label("Function_28_9CE8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Pork rough ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_9CE8 end

    def Function_29_9D09(): pass

    label("Function_29_9D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A12B")

    ChrTalk(
        0x20,
        (
            "It is bad for Mr. Timasu\x01",
            "Cooking here is awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Munching …\x01",
            "OK, will you change?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThat, a person of the Crossbell Guard\x01",
            "In such a place ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FDid you mean ……\x01",
            "Is not it Alexei?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x109, 0)
    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E98")
    Jump("loc_9EE2")

    label("loc_9E98")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EB8")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE2")

    label("loc_9EB8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ED8")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE2")

    label("loc_9ED8")

    OP_52(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9EE2")

    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    ChrTalk(
        0x20,
        (
            "Oh, noel's sergeant.\x01",
            "I guess this guy is odd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It's a break now.\x01",
            "Stretch the wing a little\x01",
            "I was eating here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOh, as usual.\x01",
            "To take the trouble to lunch,\x01",
            "From the tangram gate in the rain ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FTangram Gate……\x01",
            "Bey in the east road\x01",
            "Was it border gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, the guard is stuffing up\x01",
            "It's an important defensive point of the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Recently a new deputy commander arrived,\x01",
            "I'm getting busy with various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Sergeant Noel,\x01",
            "Either way it will be difficult, but do your best.\x01",
            "Everyone in the gate is supporting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 6)
    ClearChrFlags(0x20, 0x10)
    Jump("loc_A2BC")

    label("loc_A12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21E")

    ChrTalk(
        0x20,
        (
            "Recently, a new deputy commander has arrived\x01",
            "The guard was also busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "The new deputy commander\x01",
            "I am as good as Sonya Commander\x01",
            "It is a tough person …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Once in a while I extend the wings to the city,\x01",
            "Even eating strange mon\x01",
            "I have to refresh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_A2BC")

    label("loc_A21E")


    ChrTalk(
        0x20,
        (
            "A new deputy commander\x01",
            "I am as good as Sonya Commander\x01",
            "It is a tough person …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Once in a while I extend the wings to the city,\x01",
            "Even eating strange mon\x01",
            "I have to refresh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2BC")

    TalkEnd(0xFE)
    Return()

    # Function_29_9D09 end

    def Function_30_A2C0(): pass

    label("Function_30_A2C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A32F")

    ChrTalk(
        0xFE,
        (
            "Although it is a pleasant trip,\x01",
            "I hear that it is raining or the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a lot of rain\x01",
            "It is chilly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A372")

    label("loc_A32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A372")

    ChrTalk(
        0xFE,
        "Well, it is good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oriental cuisine is still the best.\x02",
    )

    CloseMessageWindow()

    label("loc_A372")

    TalkEnd(0xFE)
    Return()

    # Function_30_A2C0 end

    def Function_31_A376(): pass

    label("Function_31_A376")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A3D6")

    ChrTalk(
        0xFE,
        "Somewhat, Grandfather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eat here even if it is warm\x01",
            "Let's get warm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A40C")

    label("loc_A3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A40C")

    ChrTalk(
        0xFE,
        (
            "After all, my hometown cuisine\x01",
            "I agree with your mouth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A40C")

    TalkEnd(0xFE)
    Return()

    # Function_31_A376 end

    def Function_32_A410(): pass

    label("Function_32_A410")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A4A6")

    ChrTalk(
        0xFE,
        (
            "(fluent……)\x01",
            "Munching … … Hm …\x01",
            "According to this sightseeing guide ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A place with a nice view\x01",
            "It seems to be a lot, Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5C3")

    label("loc_A4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A533")

    ChrTalk(
        0xFE,
        (
            "(Kachakaka … …)\x01",
            "Suzu … It is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "by the way,\x01",
            "Reporters who were staying,\x01",
            "It seems that he got into the interview quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5C3")

    label("loc_A533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A5C3")

    ChrTalk(
        0xFE,
        (
            "Munching … … again\x01",
            "Crossbell is,\x01",
            "Again the economy looks good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In accordance with the trade meeting,\x01",
            "I feel the city is excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5C3")

    TalkEnd(0xFE)
    Return()

    # Function_32_A410 end

    def Function_33_A5C7(): pass

    label("Function_33_A5C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A634")

    ChrTalk(
        0xFE,
        "You, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is meal to read books\x01",
            "Do it after it ends,\x01",
            "Undignified.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F1")

    label("loc_A634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A695")

    ChrTalk(
        0xFE,
        "You, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To make a noise while eating\x01",
            "やめなさい、Undignified.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F1")

    label("loc_A695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A6F1")

    ChrTalk(
        0xFE,
        "You, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I talk while eating\x01",
            "やめなさい、Undignified.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6F1")

    TalkEnd(0xFE)
    Return()

    # Function_33_A5C7 end

    def Function_34_A6F5(): pass

    label("Function_34_A6F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A826")

    ChrTalk(
        0xFE,
        (
            "Today the airship is also\x01",
            "It's a story that it will stop running.\x01",
            "I have decided to go back to Libert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, a little more if it is true\x01",
            "It was a place I wanted to continue with the interview … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Anyway, in the crossbell\x01",
            "I need to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever it is,\x01",
            "We are expecting the success of the Defense Forces.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A89A")

    label("loc_A826")


    ChrTalk(
        0xFE,
        (
            "Anyway, on the crossbell\x01",
            "I want you to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever it is,\x01",
            "We are expecting the success of the Defense Forces.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A89A")

    Jump("loc_ACF7")

    label("loc_A89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A8C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8BA")
    Call(0, 45)
    Jump("loc_A8BD")

    label("loc_A8BA")

    Call(0, 46)

    label("loc_A8BD")

    Jump("loc_ACF7")

    label("loc_A8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AC5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABBE")

    ChrTalk(
        0xFE,
        (
            "Oh, the Special Affairs Division's\x01",
            "Not everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYou surely communicate with Libert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAlso on the crossbell\x01",
            "You had it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, in fact after the trade meeting\x01",
            "I have not returned home though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing, independent advocacy\x01",
            "Sensational suggestions\x01",
            "Because it was done ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurriedly ordered long-term interview,\x01",
            "To see the referendum referendum\x01",
            "It has become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FIndeed, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally,\x01",
            "Of alkane shell\x01",
            "I will also see a renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's also on the first day of the release date.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FFirst day of release date ……\x01",
            "You got a lot of tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYeah, with too much competition rate\x01",
            "It seems that there is a premier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, well to the reporter\x01",
            "There are various tricks and techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's why\x01",
            "In the city for a while\x01",
            "Hope to see you when you meet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 0)
    Jump("loc_AC58")

    label("loc_ABBE")


    ChrTalk(
        0xFE,
        (
            "Watch a renewal performance\x01",
            "After seeing a referendum,\x01",
            "My crossbrew interview is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's why\x01",
            "In the city for a while\x01",
            "Hope to see you when you meet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC58")

    Jump("loc_ACF7")

    label("loc_AC5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ACF7")

    ChrTalk(
        0xFE,
        (
            "Hehu, the shop here\x01",
            "It is delicious to the East Asian town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps Naiall yours\x01",
            "This time delicious Oriental cuisine\x01",
            "It may be a place to eat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACF7")

    TalkEnd(0xFE)
    Return()

    # Function_34_A6F5 end

    def Function_35_ACFB(): pass

    label("Function_35_ACFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD0D")
    Call(0, 37)
    Jump("loc_ADB2")

    label("loc_AD0D")

    TalkBegin(0xFE)

    ChrTalk(
        0x17,
        (
            "#02109FWell, after finishing the meal\x01",
            "Anyway I will cover the streets.\x02\x03",
            "#02104FLeaders' guards are hard,\x01",
            "If it is moving or something, chances are\x01",
            "There may be something ♪ ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_ADB2")

    Return()

    # Function_35_ACFB end

    def Function_36_ADB3(): pass

    label("Function_36_ADB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC5")
    Call(0, 37)
    Jump("loc_AE5C")

    label("loc_ADC5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "From the afternoon basically,\x01",
            "Citizenの街頭インタビューを\x01",
            "I'm planning to collect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fairly well, I will see the leaders somewhere\x01",
            "It is said that if you can shoot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_AE5C")

    Return()

    # Function_36_ADB3 end

    def Function_37_AE5D(): pass

    label("Function_37_AE5D")

    EventBegin(0x0)
    Fade(500)
    OP_68(9150, 1230, 4310, 0)
    MoveCamera(40, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 9500, 0, 5800, 180)
    SetChrPos(0x102, 11000, 0, 5410, 180)
    SetChrPos(0x104, 8000, 0, 5410, 180)
    SetChrPos(0x109, 10650, 0, 6220, 180)
    SetChrPos(0x105, 9250, 0, 6620, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_0D()
    SetChrSubChip(0x18, 0x1)
    Sleep(200)

    ChrTalk(
        0x18,
        "#6POh, everyone in the support department.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 0x2)
    Sleep(200)

    ChrTalk(
        0x17,
        (
            "#12P#02100FPerhaps,\x01",
            "Do you eat Lloyd guys as well?\x02\x03",
            "#02109FHuhu, anyway\x01",
            "The unveiling ceremony was amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, it certainly was terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FIn the aura of the leaders\x01",
            "I was really overwhelmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02106FIs not it?\x01",
            "Especially the presence of \"Chief Iron Blood Chamber\"\x01",
            "It is not a huangpa ~!\x02\x03",
            "#02100FI am close to that one too\x01",
            "It was my first time to see it,\x01",
            "I was made aware of the amazement again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "#12P#02105FOh yeah, that's right.\x01",
            "I was by the Prime Minister\x01",
            "I am a clerk-style man ….\x02\x03",
            "#02103FOh, I used to crossbell from before\x01",
            "来ていたRectorって子で\x01",
            "There is no doubt, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEr, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02104FHehe, well well\x01",
            "I understand that it is hard to answer.\x02\x03",
            "#02101F- Actually, I also have one,\x01",
            "There was something I remembered.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWhat does that mean ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103F…… Around the spring of last year,\x01",
            "Mr. Hartmann is secret backed\x01",
            "We informally talked … …\x02\x03",
            "#02100FOf course Lloyd,\x01",
            "You know that, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, that is okay ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn some information sources\x01",
            "It is no longer a famous fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103FYeah ….\x01",
            "But that was not the case at the time.\x02\x03",
            "Not to mention the crossbell 's mass communication,\x01",
            "The empire's mass communication ……\x02\x03",
            "#02101FOf course even for the crossbell police\x01",
            "All that information#4R噵 噵#I could not grasp it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P… and more\x01",
            "Escorting regardless of the important person\x01",
            "I heard that he did not attach it almost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PIt was as if I was taking a walk\x01",
            "As if I had dropped in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P… Well, that is why the opposite\x01",
            "Although it can be said that a secret has been kept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303FHmm … … What a terrible story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FOh, I can not be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02106FYes, it is impossible -\x01",
            "Or is it too regrettable!\x02\x03",
            "#02100FThat's why I later\x01",
            "I investigated variously with my hands.\x02\x03",
            "#02103FAs a result, to the setting of the talks\x01",
            "The name of the person who seems to be involved\x01",
            "Several people raised me ….\x02\x03",
            "#02101FI remembered being there.\x01",
            "Rectorという男性の名前がね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FTogether with the Prime Minister\x01",
            "Participation in the meeting itself\x01",
            "I was grasping it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FI also set it up\x01",
            "Rectorさんの仕業……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWhat is it …?\x01",
            "It is a terrible intolerance skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103F…… Yes, and such a thing\x01",
            "I can not be a one - sided clerk.\x02\x03",
            "#02102FThat's what it is\x01",
            "Unless it is a human of the Imperial Army Information Bureau, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see, I see … ….\x02\x03",
            "#00003F(I can not get there until I get there\x01",
            "  Graceさんも相当だな。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Oh, it's a terrible obsession.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02109FHuh, apparently a face star?\x02\x03",
            "#02106FHaa, but nothing\x01",
            "あの子がそのRectorとは\x01",
            "I did not think of dew.\x02\x03",
            "#02102FWell, Lloyd also has a position on you guys\x01",
            "There will be,\x01",
            "I will stop it any more … …\x02\x03",
            "#02100Fとにかく、あのRectorって子が\x01",
            "Surely it is not extraordinary.\x02\x03",
            "Lloyd,\x01",
            "If there is something to do with you in the future\x01",
            "It is best to tighten your mind at best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F情報Thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x0, 9420, 0, 5800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0x148, 0)
    EventEnd(0x5)
    Return()

    # Function_37_AE5D end

    def Function_38_BA8D(): pass

    label("Function_38_BA8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BBB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3F")

    ChrTalk(
        0xFE,
        (
            "Fight with Danna\x01",
            "I was running away from home ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At last I was crying yesterday\x01",
            "I was apologized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, yes.\x01",
            "When it is done there\x01",
            "A slightly guilty feeling … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BBB4")

    label("loc_BB3F")


    ChrTalk(
        0xFE,
        (
            "Well, sorry.\x01",
            "I also got tired of running away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow also incident\x01",
            "It seems to be happening ….\x01",
            "I will decide to return home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBB4")

    Jump("loc_BD8F")

    label("loc_BBB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC43")

    ChrTalk(
        0xFE,
        (
            "You found out in a quarreling danna.\x01",
            "I was told to go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, you should not apologize like that.\x01",
            "Sincerity does not come through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BC43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BCBA")

    ChrTalk(
        0xFE,
        (
            "A serving official to the usual person\x01",
            "It seems I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not count on it a little while ago.\x01",
            "Waiter is\x01",
            "I wonder what was it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BCBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BD1C")

    ChrTalk(
        0xFE,
        (
            "Somehow the serving officer\x01",
            "You do not count on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry and cook\x01",
            "I want you to bring it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8F")

    label("loc_BD1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BD8F")

    ChrTalk(
        0xFE,
        (
            "Because I fought with Danna,\x01",
            "You pettered away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm …\x01",
            "Because I will not forgive you until I apologize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD8F")

    TalkEnd(0xFE)
    Return()

    # Function_38_BA8D end

    def Function_39_BD93(): pass

    label("Function_39_BD93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BDF7")

    ChrTalk(
        0xFE,
        (
            "Oh, I also love you\x01",
            "My mother's family has got tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to see you daddy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BDF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BE32")

    ChrTalk(
        0xFE,
        (
            "Dad, still here\x01",
            "I wonder if they do not come …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BE32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BE67")

    ChrTalk(
        0xFE,
        (
            "Munching …\x01",
            "Well, it's delicious!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BE67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BEC4")

    ChrTalk(
        0xFE,
        (
            "Mommy, desk is what\x01",
            "I'm sticky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did people in the store forget to wipe?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF2A")

    label("loc_BEC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BF2A")

    ChrTalk(
        0xFE,
        "I came to play with Mom's parents house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Daddy will come later.\x01",
            "Your work is busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2A")

    TalkEnd(0xFE)
    Return()

    # Function_39_BD93 end

    def Function_40_BF2E(): pass

    label("Function_40_BF2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C182")

    ChrTalk(
        0x1D,
        (
            "#04405FAh … everyone,\x01",
            "It is strange in the place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FLet me eat ……\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04400FYeah, I got a break\x01",
            "I have just come to have lunch.\x02\x03",
            "#04403FThis fried rice,\x01",
            "There is a nice taste with depth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, Lease san's\x01",
            "It is as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FIt looks delicious, but … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Somehow on the counter\x01",
            "I have plenty of dishes … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Huh, and besides\x01",
            "Even Sister in Ryuujiro\x01",
            "It is quite a mismatch. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Ellie says\x01",
            "Looking at the place where it does not get crowded,\x01",
            "Is this normal? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 3)
    Jump("loc_C1F3")

    label("loc_C182")


    ChrTalk(
        0x1D,
        (
            "#04400FIf I do a little more\x01",
            "I am going back to the cathedral.\x02\x03",
            "If there is something\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1F3")

    TalkEnd(0xFE)
    Return()

    # Function_40_BF2E end

    def Function_41_C1F7(): pass

    label("Function_41_C1F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183E, 7)), scpexpr(EXPR_END)), "loc_C26D")

    ChrTalk(
        0xFE,
        (
            "For the restoration of the city,\x01",
            "I was volunteering a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The meal after having sweat\x01",
            "It is truly exceptional.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183E, 7)
    Jump("loc_C2D1")

    label("loc_C26D")


    ChrTalk(
        0xFE,
        (
            "The old city is still more\x01",
            "It seems to be working on restoration … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still have plenty\x01",
            "You may have some help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2D1")

    TalkEnd(0xFE)
    Return()

    # Function_41_C1F7 end

    def Function_42_C2D5(): pass

    label("Function_42_C2D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C39B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C307")
    Call(0, 54)
    Return()

    label("loc_C307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_C396")

    ChrTalk(
        0xFE,
        (
            "Oh, finally this\x01",
            "You may be able to see your father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'll leave it to you guys.\x01",
            "Please find your father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C396")

    Jump("loc_C3E8")

    label("loc_C39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C3E8")

    ChrTalk(
        0xFE,
        (
            "Airyにアルミン……\x01",
            "Yesterday is very wonderful\x01",
            "It was a day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3E8")

    TalkEnd(0xFE)
    Return()

    # Function_42_C2D5 end

    def Function_43_C3EC(): pass

    label("Function_43_C3EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C41E")
    Call(0, 54)
    Return()

    label("loc_C41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_C4BE")

    ChrTalk(
        0xFE,
        (
            "私たち、きっとAlmuのお父さまに\x01",
            "You can say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crystal of our love, Armin\x01",
            "By all means I have to do it!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "baby",
        "Boozoo.\x02",
    )

    CloseMessageWindow()

    label("loc_C4BE")

    Jump("loc_C523")

    label("loc_C4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C523")

    ChrTalk(
        0xFE,
        (
            "ええ、Almu……\x01",
            "Yesterday was very very\x01",
            "It was a wonderful day.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "baby",
        "Bubuu ♪\x02",
    )

    CloseMessageWindow()

    label("loc_C523")

    TalkEnd(0xFE)
    Return()

    # Function_43_C3EC end

    def Function_44_C527(): pass

    label("Function_44_C527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C53C")
    Call(0, 45)
    Jump("loc_C53F")

    label("loc_C53C")

    Call(0, 46)

    label("loc_C53F")

    TalkEnd(0xFE)
    Return()

    # Function_44_C527 end

    def Function_45_C543(): pass

    label("Function_45_C543")


    ChrTalk(
        0x27,
        (
            "Indeed, while you are here\x01",
            "You are taking an inn at Ryuujiro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Because meal is also excellent here\x01",
            "Are you comfortable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Thanks, yeah.\x01",
            "Do not eat too much\x01",
            "It is hard, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Although, I bother today\x01",
            "Sorry for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If true, click here\x01",
            "I should have gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Hehe, do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Walking and wandering are my\x01",
            "It's like a hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Hehuu, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Honorable stones\x01",
            "It is a free journalist.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Return()

    # Function_45_C543 end

    def Function_46_C6F7(): pass

    label("Function_46_C6F7")


    ChrTalk(
        0x16,
        (
            "ですが、Nielsenさんは\x01",
            "This time it is quite long\x01",
            "You have stayed right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "As I thought, my hometown\x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Well, what?\x01",
            "I want to feel it with the skin\x01",
            "There may be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Anyway, still for a while\x01",
            "I am planning to stay at the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_46_C6F7 end

    def Function_47_C7EE(): pass

    label("Function_47_C7EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C803")
    Call(0, 48)
    Jump("loc_C8C3")

    label("loc_C803")


    ChrTalk(
        0x1C,
        (
            "#01803FWhen I was in the Republic,\x01",
            "Moving for the convenience of my father's work\x01",
            "I was repeating … ….\x02\x03",
            "#01802Fふふ、Sunsanには\x01",
            "I really appreciate it.\x02\x03",
            "We also have ties with you and Iria\x01",
            "I want to cherish it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8C3")

    TalkEnd(0xFE)
    Return()

    # Function_47_C7EE end

    def Function_48_C8C7(): pass

    label("Function_48_C8C7")

    EventBegin(0x0)
    Fade(500)
    OP_68(13370, 1400, -1550, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16720, 0)
    SetChrPos(0x1C, 13800, 50, -320, 180)
    SetChrSubChip(0x1C, 0x0)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0xE1, 0x0)
    SetChrPos(0x101, 13620, 0, -1520, 0)
    SetChrPos(0x102, 13450, 0, -2830, 0)
    SetChrPos(0x103, 12500, 0, -2220, 45)
    SetChrPos(0x104, 11630, 0, -460, 90)
    SetChrPos(0x109, 12250, 0, -3430, 0)
    SetChrPos(0x105, 11670, 0, -1620, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x1C,
        (
            "#01802FAh……\x01",
            "こんにちは、Everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100Fふふ、こんにちはLishaさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FDid you come to dinner today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802FHuhu, yes.\x02\x03",
            "While receiving meal after dinner,\x01",
            "I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pyou,\x01",
            "Is it a human being of the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pも〜、せっかくLishaと\x01",
            "I was enjoying girls talk ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00302FHaha, that was bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, the artist\x01",
            "You can encounter private\x01",
            "After all it is a precious feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304Fsurely.\x01",
            "Celebrities like friendship\x01",
            "It's hard to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01809FHaha ……\x01",
            "Such a thing, I am still a newcomer.\x02\x03",
            "#01802FSunsanは休日、家にこもりがちな私を\x01",
            "It often takes me out for play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHuhu, because the same age, the talks also match.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11Pそれと、Lishaのプロポーションでも\x01",
            "It is fun to find clothes that can be worn cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01809FHaha, you are pretty cute\x01",
            "I can not find it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F（うーん、確かにLishaさんだと\x01",
            "It looks like there is not much size … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00203F(… … luxurious troubles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FHaha, but you really are on good terms.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802Fふふ、Sunsanには本当に\x01",
            "I am grateful.\x02\x03",
            "#01803FWhen I was in the Republic,\x01",
            "Moving for the convenience of my father's work\x01",
            "I was repeating … ….\x02\x03",
            "#01808FWho can call a friend\x01",
            "I can not do it easily,\x01",
            "Because I was always alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303FIs that so……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1C, 500)

    ChrTalk(
        0xA,
        "#11Pふふ、安心してLisha。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x1)

    ChrTalk(
        0xA,
        (
            "#11PAs I became friends with me,\x01",
            "Because there is no one alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf this is the case, go to the grave\x01",
            "一緒だからね！　Lisha。\x02",
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
    OP_63(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1C,
        (
            "#01802FHaha ……\x01",
            "ありがとう、Sunsan。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FGhost, apparently\x01",
            "We seem to be bugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYes, it is about time.\x01",
            "Let me have your time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x0)

    ChrTalk(
        0x1C,
        (
            "#01806FI'm sorry, everyone.\x01",
            "Let me take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004Fいや、Lishaと話せて\x01",
            "We also got a good breath.\x02\x03",
            "#00002FWell then, we are in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#01802FYes, then again.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17C, 2)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4C(0xA, 0xFF)
    SetChrPos(0x1C, 14000, 50, 0, 90)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13390, 0, -1690, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_C8C7 end

    def Function_49_D1BA(): pass

    label("Function_49_D1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x28)
    SetChrChipByIndex(0x28, 0x28)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 17010, 0, 15370, 315)
    SetChrFlags(0x9, 0x80)
    OP_4B(0x8, 0xFF)
    OP_68(-200, 1400, -640, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16270, 0)
    SetChrPos(0x101, -200, 0, 600, 90)
    SetChrPos(0x102, -600, 0, -600, 90)
    SetChrPos(0x109, -1400, 0, 600, 90)
    SetChrPos(0x105, -1800, 0, -600, 90)

    def lambda_D26F():
        OP_98(0x101, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D26F)
    Sleep(50)

    def lambda_D28C():
        OP_98(0x102, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D28C)
    Sleep(50)

    def lambda_D2A9():
        OP_98(0x109, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D2A9)
    Sleep(50)

    def lambda_D2C6():
        OP_98(0x105, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D2C6)
    OP_68(890, 1400, -390, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_0D()

    def lambda_D308():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D308)
    Sleep(50)

    def lambda_D318():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D318)
    Sleep(50)

    def lambda_D328():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D328)
    Sleep(50)

    def lambda_D338():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D338)
    Sleep(50)
    StopBGM(0xFA0)
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
        "#12P#00001FThere was …!\x02",
    )

    CloseMessageWindow()
    OP_68(15600, 1400, 15180, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(13750, 3000)
    OP_6F(0x1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    Sleep(100)

    ChrTalk(
        0x28,
        (
            "#03500FI see …\x01",
            "Do you use flower pickles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, with just the peppers\x01",
            "Both spice and flavor are uneven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PAlthough it is cultivated only in the east\x01",
            "Recently I can order by rail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03502F#11PNo, when you make Mabaugh yourself\x01",
            "It was not enough for me.\x02\x03",
            "#03504F\"hemp#2RMar#\"…\x01",
            "One thing I learned.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 5010, 0, 15540, 45)

    ChrTalk(
        0x101,
        (
            "#00000F#NRectorさん……\x01",
            "Were you here?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0xA, 0x80)
    OP_63(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(13510, 1400, 14500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15950, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 13000, 0, 14500, 90)
    SetChrPos(0x102, 12600, 0, 15500, 90)
    SetChrPos(0x109, 12000, 0, 14250, 90)
    SetChrPos(0x105, 11500, 0, 15250, 90)
    SetChrPos(0x28, 16010, 0, 14370, 270)
    OP_93(0x8, 0xE1, 0x0)

    def lambda_D644():
        OP_98(0x101, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D644)
    Sleep(50)

    def lambda_D661():
        OP_98(0x102, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D661)
    Sleep(50)

    def lambda_D67E():
        OP_98(0x109, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D67E)
    Sleep(50)

    def lambda_D69B():
        OP_98(0x105, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D69B)
    Sleep(50)
    OP_68(14290, 1400, 14500, 1500)
    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00105F(It was easy to find … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(No, something awful\x01",
            "Chalan Polan: That's right …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(If you can verify your identity\x01",
            "Although the mission is over … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03505FOh, it was late.\x02\x03",
            "#03509FI was waiting, my friend of mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHeck …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x28,
        (
            "#12P#03502FMaster.\x01",
            "They are those whom Guess and others said earlier.\x02\x03",
            "#03504FI have motivation and guts only\x01",
            "Please do it biscis.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x28, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        "Okay, I'll leave it.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#11PFour people are serious, but\x01",
            "It is nice to spread Oriental cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'll do my best and come along!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00012FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWhatever the story … ….\x02",
    )

    CloseMessageWindow()
    OP_68(11460, 1400, 11810, 1000)
    MoveCamera(41, 17, 0, 1000)
    OP_93(0x28, 0x10E, 0x0)
    OP_98(0x28, 0xFFFFF254, 0x0, 0xFFFFFB50, 0x1770, 0x0)
    OP_93(0x28, 0xB4, 0x0)
    Sleep(50)
    Sound(809, 0, 70, 0)
    OP_9D(0x28, 0x2B2A, 0x0, 0x2382, 0x2BC, 0x7D0)
    Sleep(100)
    OP_93(0x28, 0xE1, 0x0)
    OP_98(0x28, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1770, 0x0)
    OP_6F(0x1)
    WaitChrThread(0x101, 3)
    SetChrFlags(0x28, 0x80)
    OP_0D()

    def lambda_D9C0():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9C0)
    Sleep(50)

    def lambda_D9D0():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9D0)
    Sleep(50)

    def lambda_D9E0():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D9E0)
    Sleep(50)

    def lambda_D9F0():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D9F0)
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
        "#11P#00011FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FHe ran away … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10309FHaha, as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FIf you have to chase it!\x02",
    )

    CloseMessageWindow()

    def lambda_DAEE():
        OP_98(0x8, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DAEE)
    Sound(802, 0, 100, 0)
    OP_68(13640, 1400, 14410, 1000)
    MoveCamera(37, 24, 0, 1000)

    ChrTalk(
        0x8,
        "Kora, where will you go! Is it?\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "Training has already begun!\x01",
            "First of all it is preparing to prepare!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB81():
        OP_93(0x101, 0x5A, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB81)
    Sleep(50)

    def lambda_DB91():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB91)
    Sleep(50)

    def lambda_DBA1():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DBA1)
    Sleep(50)

    def lambda_DBB1():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBB1)

    ChrTalk(
        0x101,
        "#6P#00011FNo, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FWe, to the Crossbell Police\x01",
            "I belong to you ──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_68(15810, 1400, 13900, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15910, 0)
    SetChrPos(0x101, 15500, 0, 14370, 0)
    SetChrPos(0x102, 16500, 0, 14370, 0)
    SetChrPos(0x109, 15500, 0, 13370, 0)
    SetChrPos(0x105, 16500, 0, 13370, 0)
    SetChrPos(0x8, 16000, 0, 15870, 180)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Muu\x01",
            "It can not be helped if it is not Kang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, it is the edge of something.\x01",
            "You should take this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDEF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Recipe of Ryuugi fried rice\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Incidentally",
            scpstr(SCPSTR_CODE_ITEM, '料理手册'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00005FIs it good?\x01",
            "I got my notebook … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE70")

    label("loc_DDEF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '料理手册'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00005FIs it good?\x01",
            "I got it for free ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE70")

    AddItemNumber('料理手册', 1)

    ChrTalk(
        0x8,
        (
            "I do not mind it because it is the remainder of the store.\x01",
            "It is good to go on a ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FThank you very much.\x01",
            "Well then, I will excuse myself.\x02\x03",
            "#00001F── Everyone, I will chase you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101FYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FI understand.\x02",
    )

    CloseMessageWindow()

    def lambda_DF46():
        OP_93(0x101, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF46)

    def lambda_DF53():
        OP_93(0x102, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF53)

    def lambda_DF60():
        OP_93(0x109, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF60)

    def lambda_DF6D():
        OP_93(0x105, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DF6D)
    WaitChrThread(0x105, 1)

    def lambda_DF7E():
        OP_98(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF7E)
    Sleep(50)

    def lambda_DF9B():
        OP_98(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF9B)
    Sleep(50)

    def lambda_DFB8():
        OP_98(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DFB8)
    Sleep(50)

    def lambda_DFD5():
        OP_98(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFD5)
    Sleep(50)
    OP_93(0x8, 0x10E, 0x1F4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "* When examining a specific place such as a book placed in various places,\x01",
            "I may memorize the \"recipe\" of cooking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ \"Recipe\" will be recorded in \"Cookbook.\"\x01",
            "If you use \"food notebook\" anytime\x01",
            "You can make various effective dishes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Also, \"Great Success\" and \"Unexpected\" Dishes,\x01",
            "Cooking to be completed will change with a certain probability.\x01",
            "(It sometimes \"fails\" to cooking.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ \"food ingredients\" used for cooking\x01",
            "It is sold at stores such as general merchandise shops.\x01",
            "In addition, monsters may be dropped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x22, 4)
    NewScene("c1000", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_49_D1BA end

    def Function_50_E209(): pass

    label("Function_50_E209")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(250, 1400, -660, 0)
    MoveCamera(46, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19780, 0)
    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00302.itc", 0x2A)
    LoadChrToIndex("chr/ch02902.itc", 0x2B)
    LoadChrToIndex("chr/ch03002.itc", 0x2C)
    LoadChrToIndex("chr/ch45002.itc", 0x2D)
    LoadChrToIndex("apl/ch50092.itc", 0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E3C7")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x104, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E2FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E2FB)

    def lambda_E30C():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E30C)

    def lambda_E326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E326)

    def lambda_E337():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E337)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E36E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E36E)

    def lambda_E37F():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E37F)
    Sleep(200)

    def lambda_E39C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E39C)

    def lambda_E3AD():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E3AD)
    Jump("loc_E676")

    label("loc_E3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E521")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x109, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E455():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E455)

    def lambda_E466():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E466)

    def lambda_E480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E480)

    def lambda_E491():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E491)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E4C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E4C8)

    def lambda_E4D9():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4D9)
    Sleep(200)

    def lambda_E4F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E4F6)

    def lambda_E507():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E507)
    Jump("loc_E676")

    label("loc_E521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E676")
    SetChrPos(0x1A2, -2000, 0, 500, 90)
    SetChrPos(0x102, -2000, 0, -500, 90)
    SetChrPos(0x101, -2000, 0, 600, 90)
    SetChrPos(0x105, -2000, 0, -600, 90)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E5AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_E5AF)

    def lambda_E5C0():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_E5C0)

    def lambda_E5DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E5DA)

    def lambda_E5EB():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E5EB)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_E622():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E622)

    def lambda_E633():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E633)
    Sleep(200)

    def lambda_E650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E650)

    def lambda_E661():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E661)

    label("loc_E676")

    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "\"Ryuuji\" … ….\x01",
            "A shop that offers Eastern Cuisine on east side,?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FWould you like to take a break even a little?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hm, I see.\x01",
            "Just a hungry stomach is empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "What is this shop?\x01",
            "I will try out something to put out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(2730, 1400, 6720, 0)
    MoveCamera(41, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16270, 0)
    SetChrChipByIndex(0x29, 0x2E)
    SetChrSubChip(0x29, 0xB)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 4400, 600, 7100, 0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x2E)
    SetChrSubChip(0x2A, 0xB)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 3300, 600, 6100, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x2E)
    SetChrSubChip(0x2B, 0xB)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 2100, 600, 7100, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrSubChip(0x2C, 0xB)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 3300, 600, 8300, 0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_E8AD")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x104, 0x2A)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x104, 1600, 100, 7150, 90)
    Jump("loc_E9B4")

    label("loc_E8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_E933")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x109, 1600, 100, 7150, 90)
    Jump("loc_E9B4")

    label("loc_E933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_E9B4")
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x105, 0x2C)
    SetChrChipByIndex(0x1A2, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x1A2, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x1A2, 0x0)
    SetChrPos(0x1A2, 3250, 100, 9050, 180)
    SetChrPos(0x102, 4900, 100, 7100, 270)
    SetChrPos(0x101, 3250, 100, 5450, 0)
    SetChrPos(0x105, 1600, 100, 7150, 90)

    label("loc_E9B4")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#11P#00102FHow was the taste of the Ryuuen Restaurant?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EA3A")

    ChrTalk(
        0x104,
        (
            "#6P#00309FOh, I definitely know the real place\x01",
            "Human opinions are heard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EACF")

    label("loc_EA3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EA89")

    ChrTalk(
        0x109,
        (
            "#6P#10109FYeah, I definitely know the real place\x01",
            "I want to hear human opinions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EACF")

    label("loc_EA89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EACF")

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, I definitely know the real place\x01",
            "I want to hear the opinions of humans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EACF")

    BeginChrThread(0x1A2, 3, 0, 51)
    Sleep(1000)
    EndChrThread(0x1A2, 0x3)

    ChrTalk(
        0x1A2,
        (
            "#5PCrap\x01",
            "What the heck is that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PWhy this shop\x01",
            "Can you put out such dishes at such a price?\x01",
            "Are the shop owners sure? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FCome on, that loudly\x01",
            "Bad thing about the shop ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FNo, Shin said probably ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PFor example, this Mabo tofu ……\x01",
            "Taste also in the three star restaurant in the eastern people street\x01",
            "I have not quenched at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PIf this is three times you should be able to take the mirror -\x01",
            "Nevertheless it will not do! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EC99")

    ChrTalk(
        0x104,
        "#6P#00306FWell, that kind of story ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECFE")

    label("loc_EC99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_ECCF")

    ChrTalk(
        0x109,
        "#6P#10106FThat was such a story ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECFE")

    label("loc_ECCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ECFE")

    ChrTalk(
        0x105,
        "#6P#10304FHuh, that sort of thing.\x02",
    )

    CloseMessageWindow()

    label("loc_ECFE")


    ChrTalk(
        0x1A2,
        (
            "#5POh, okay ….\x01",
            "Why this shop in Crossbell ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FWell, anyway\x01",
            "It was nice to be satisfied.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 1)
    OP_29(0x73, 0x1, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_EDD4")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x1A2, 0x4)
    Jump("loc_EE53")

    label("loc_EDD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_EE16")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x1A2, 0x4)
    Jump("loc_EE53")

    label("loc_EE16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_EE53")
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x1A2, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x1A2, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x1A2, 0x4)

    label("loc_EE53")

    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_49()
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    OP_D7(0x2D)
    OP_D7(0x2E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1380, 20, -90, 270)
    EventEnd(0x5)
    Return()

    # Function_50_E209 end

    def Function_51_EE8E(): pass

    label("Function_51_EE8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEBE")

    def lambda_EE9E():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EE9E)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_51_EE8E")

    label("loc_EEBE")

    Return()

    # Function_51_EE8E end

    def Function_52_EEBF(): pass

    label("Function_52_EEBF")

    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00202.itc", 0x2A)
    LoadChrToIndex("chr/ch00302.itc", 0x2B)
    LoadChrToIndex("chr/ch02902.itc", 0x2C)
    LoadChrToIndex("chr/ch03002.itc", 0x2D)
    LoadChrToIndex("apl/ch50092.itc", 0x2E)
    EventBegin(0x0)
    Fade(500)
    OP_68(15350, 1400, 14950, 0)
    MoveCamera(61, 26, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 16000, -200, 14500, 0)
    SetChrPos(0x102, 14880, 0, 13460, 0)
    SetChrPos(0x103, 14200, 0, 14350, 0)
    SetChrPos(0x104, 13000, 0, 14910, 0)
    SetChrPos(0x109, 13590, 0, 13330, 0)
    SetChrPos(0x105, 12700, 0, 13930, 0)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EFE2")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_F025")

    label("loc_EFE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EFFA")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_F025")

    label("loc_EFFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F012")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Jump("loc_F025")

    label("loc_F012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F025")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_F025")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15A")

    ChrTalk(
        0x8,
        (
            "See, what are you doing!\x01",
            "I'm kidding again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hi, I'm sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUm, is it okay?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "I … is something for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As you can see, I am busy now.\x01",
            "If you order, I will ask the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, that's not it.\x01",
            "In fact\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1DD")

    label("loc_F15A")

    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Oh, is that something for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you order, I will ask the counter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1DD")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, it's about the example gourmet guide.\x01",
            "I certainly have heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I am busy but it can not be helped.\x01",
            "I'm waiting at a vacant table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm proud of \"Fried Rice Tenka\"\x01",
            "I will taste it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHuh, he's looking forward to it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000FThen let's suppose that you are on your seat.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x8, 5440, 0, 9730, 225)
    SetChrPos(0x101, 3230, 0, 8960, 180)
    SetChrPos(0x103, 1720, 0, 8710, 135)
    SetChrPos(0x102, 1600, 0, 7150, 90)
    SetChrPos(0x104, 3290, 0, 5440, 0)
    SetChrPos(0x105, 4520, 0, 5990, 315)
    SetChrPos(0x109, 4770, 0, 7180, 270)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x29, 0x2E)
    SetChrSubChip(0x29, 0x1)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x2E)
    SetChrSubChip(0x2A, 0x1)
    SetChrFlags(0x2A, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x2E)
    SetChrSubChip(0x2B, 0x1)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrSubChip(0x2C, 0x1)
    SetChrFlags(0x2C, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x2D, 0x2E)
    SetChrSubChip(0x2D, 0x1)
    SetChrFlags(0x2D, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2E, 0x2E)
    SetChrSubChip(0x2E, 0x1)
    SetChrFlags(0x2E, 0x8000)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrPos(0x29, 3990, 600, 7230, 0)
    SetChrPos(0x2A, 2760, 600, 6220, 0)
    SetChrPos(0x2B, 2330, 600, 6900, 0)
    SetChrPos(0x2C, 3300, 600, 8300, 0)
    SetChrPos(0x2D, 3900, 600, 6340, 0)
    SetChrPos(0x2E, 2360, 600, 7880, 0)
    OP_68(3250, 1400, 7170, 0)
    MoveCamera(58, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd 's ate fried rice under the tree.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00204F……Is delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, as expected\x01",
            "Master is fluffy.\x02\x03",
            "#00304FI made it so cute\x01",
            "Exquisite fried rice is only available at Longyuan Hotel\x01",
            "I can not eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huhun, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Originally fried rice was a favorite dish of me ……\x01",
            "I recently improved it further\x01",
            "There is no way it can not be delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHag Hug, Mog Mog …\x01",
            "Well, really … …!\x02\x03",
            "#10103FEven though it's a simple dish\x01",
            "I can not have a deep taste so far!\x02\x03",
            "#10109FI am a guard dormitory too\x01",
            "I have ever made it several times,\x01",
            "I am different from the prosperism … ….!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x105, 0x2)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x104,
        "#00306FI talk while eating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FNo, at a great momentum\x01",
            "It's crowded.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        (
            "Well, until that\x01",
            "If you like it\x01",
            "It was worth making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I'm pessimistic, I will take care of yourself again.\x01",
            "Shall we serve you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(100)

    ChrTalk(
        0x109,
        "#10109FCome on!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, Noel's sister ……\x01",
            "まるで育ち盛りのboyね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it seems you liked it quite a bit … …\x01",
            "Do you leave the article here to Noel?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 2300, 0, 500, 270)
    SetChrPos(0x103, 2300, 0, -500, 270)
    SetChrPos(0x104, 3400, 0, 500, 270)
    SetChrPos(0x105, 3400, 0, -500, 270)
    SetChrPos(0x109, 4500, 0, 500, 270)
    SetChrPos(0x102, 4500, 0, -500, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA6C")
    SetChrPos(0x8, 17080, 0, 15430, 0)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_FA7D")

    label("loc_FA6C")

    SetChrPos(0x8, 16000, 0, 15990, 0)

    label("loc_FA7D")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2E, 0x80)
    SetChrBattleFlags(0x2E, 0x8000)
    OP_68(2880, 1400, -40, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x172, 5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_FB2A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_FB47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_FB5A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_FB6D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_FB8A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_FB9D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_FBBA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_FBCD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_FBEA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_FBFD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_FC1A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FC1A")

    OP_29(0x80, 0x1, 0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD1D")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FD14")

    AnonymousTalk(
        0x101,
        (
            "#00003FすぐにでもGraceさんに\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FD14")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_FD1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDEE")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_FDEE")

    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FE0E")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_FE51")

    label("loc_FE0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FE26")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_FE51")

    label("loc_FE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FE3E")
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Jump("loc_FE51")

    label("loc_FE3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FE51")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_FE51")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2880, 0, -40, 278)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_EEBF end

    def Function_53_FE7D(): pass

    label("Function_53_FE7D")

    EventBegin(0x0)
    Fade(500)
    OP_68(11630, 1400, -4690, 0)
    MoveCamera(53, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 11200, 0, -5110, 90)
    SetChrPos(0x102, 10260, 0, -5180, 90)
    SetChrPos(0x104, 10900, 0, -4210, 90)
    SetChrPos(0x103, 9410, 30, -4580, 90)
    SetChrPos(0x105, 11260, 0, -3140, 135)
    SetChrPos(0x109, 10050, 0, -3500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        "Ha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(If she, Miscon's\x01",
            "In the \"waitress\" frame\x01",
            "I wonder if that is right. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Somehow I'm not cheerful\x01",
            "It looks like … ….\x01",
            "Why do not you ask me once? )\x02\x03",
            "#00000FUm, a little consultation\x01",
            "I have it, but … is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Are you …?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "Oh, that story …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Before this, when I was invited by Roy\x01",
            "I declined once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Lishaがいなくなったのに\x01",
            "I can not feel that way ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThen, it is not easy to invite\x01",
            "That's not good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHM……\x01",
            "Apparently, I'm still hesitating\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yup……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am not cheerful,\x01",
            "Also for customers of stores\x01",
            "It looked like it was transmitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Certainly I am in this state,\x01",
            "Customers are not fun too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, if there is hesitation\x01",
            "Why do not you try it?\x02\x03",
            "#10300FI regret not doing it\x01",
            "If there is a possibility,\x01",
            "I think that it is better to do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    Sound(809, 0, 40, 0)
    SetChrChipByIndex(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xA, 0x3070, 0x0, 0xFFFFEBB0, 0x2BC, 0x7D0)
    Sound(30, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xA,
        "… Yeah, I decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, I wish you good luck\x01",
            "I will make you excitement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whether it is miscon or hot water bath,\x01",
            "How come!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10106FWhat is hot water bath ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell then, then\x01",
            "Is it OK to participate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At the start of the program\x01",
            "Because I go to make it in time,\x01",
            "Please contact me later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10592")

    ChrTalk(
        0x101,
        (
            "#00003F─ ─ Now, at last\x01",
            "Participants' frame was filled.\x02\x03",
            "#00000FCitizen会館に行って\x01",
            "Let 's report to Roy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_10592")

    SetScenarioFlags(0x199, 4)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)
    ClearChrBattleFlags(0xA, 0x4)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10980, 0, -4730, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_53_FE7D end

    def Function_54_105E0(): pass

    label("Function_54_105E0")

    EventBegin(0x0)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1F, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-100570, 1430, -55230, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -100480, 30, -54280, 180)
    SetChrPos(0x102, -99460, 30, -53780, 180)
    SetChrPos(0x103, -101150, 30, -53570, 180)
    SetChrPos(0x104, -100010, 30, -52930, 180)
    SetChrPos(0x109, -101120, 30, -52250, 180)
    SetChrPos(0x105, -100010, 30, -51900, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D81")
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x1F,
        "baby",
        "Southeast\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Together …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "うふふ、見てAlmu。\x01",
            "Taking this asleep quickly\x01",
            "I'm asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "ああ、そうだねAiry。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "When I got into this sleeping face\x01",
            "It's almost like an angel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Huhu, you like goddess\x01",
            "Because I was born,\x01",
            "Naturally it is natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "まあ、Almuったら……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x1F, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F……Let me see.\x01",
            "Where you are capturing\x01",
            "I am sorry but …\x02\x03",
            "#00000FあなたがAlmuさんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_108B3():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_108B3)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        "Hmm……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Well, which one is it like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Police,\x01",
            "It is a person of the affairs support department.\x02\x03",
            "Look at the request\x01",
            "I asked him … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Oh, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I am glad that you came.\x01",
            "I'm really happy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "よかったわね、Almu！\x01",
            "With this finally ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        "ああ、Airy……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "babyが生まれたばかり\x01",
            "But even though it is really\x01",
            "You made a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "This servant is bad\x01",
            "All in all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Almuったら……\x01",
            "That's a promise not to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When I first held this child,\x01",
            "I swore by two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "No matter how hard it is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "…… me and you, and\x01",
            "This child to love ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "All my family gets over it.\x01",
            "… That was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "ああ、愛しているよAiry！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "私もよ、Almu！！\x02",
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
        (
            "#10106FうHa\x01",
            "It is love love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FTo the world of two people\x01",
            "It seems like I got in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FSounds like that … …\x02\x03",
            "#00000F…… Kohon.\x01",
            "I'm sorry, but for the request\x01",
            "Would you please let me know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Happy …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "That's right!\x02",
    )

    CloseMessageWindow()

    def lambda_10CFB():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_10CFB)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        (
            "Er …\x01",
            "You guys want a person search\x01",
            "I'd like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm sorry but\x01",
            "Can you take over immediately?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E1B")

    label("loc_10D81")

    OP_93(0x1E, 0x0, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1E,
        "Oh, I wonder if the hands are empty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "You guys want a person search\x01",
            "I'd like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm sorry but\x01",
            "Can you take over immediately?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E1B")

    Call(0, 55)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    SetChrPos(0x0, -100140, 30, -52870, 180)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_54_105E0 end

    def Function_55_10E6B(): pass

    label("Function_55_10E6B")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10ED5"),
        (1, "loc_10EDD"),
        (SWITCH_DEFAULT, "loc_110A8"),
    )


    label("loc_10ED5")

    Call(0, 56)
    Jump("loc_110A8")

    label("loc_10EDD")


    ChrTalk(
        0x101,
        (
            "#00006FEr … I'm sorry.\x01",
            "To say soon … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11043")

    ChrTalk(
        0x1E,
        (
            "Sounds like that … ….\x01",
            "Only you guys are asking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Please …\x01",
            "It is also for this child I love.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1F,
        "baby",
        "… …. E, the EEC …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Ogoshi Yoshi Almin,\x01",
            "It's all right …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, I managed to empty my hand\x01",
            "Because I will return ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Oh, I will ask.\x01",
            "I'll be waiting here forever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110A0")

    label("loc_11043")


    ChrTalk(
        0x1E,
        "Sounds like that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Well then, get your hands out quickly\x01",
            "Come over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Please, thanks……\x02",
    )

    CloseMessageWindow()

    label("loc_110A0")

    SetScenarioFlags(0x19A, 5)
    Jump("loc_110A8")

    label("loc_110A8")

    Return()

    # Function_55_10E6B end

    def Function_56_110A9(): pass

    label("Function_56_110A9")


    ChrTalk(
        0x101,
        (
            "#00000FYes, I understand.\x01",
            "Please choose for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Oh … really! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "No, I'm saved!\x01",
            "Where I was really in trouble\x01",
            "Was it …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "よかったわね、Almu！\x01",
            "I am very happy!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1F,
        "baby",
        "Happy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        (
            "ああ、Airy……\x01",
            "Armin is happy too\x01",
            "You seem to be giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "ええ、Almu……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F…… Please give details of the request.\x02",
    )

    CloseMessageWindow()

    def lambda_11211():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_11211)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        "Oh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "This, fault ……\x01",
            "I will talk to you soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(It was saved, Tiio ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(If this goes on\x01",
            "untill forever\x01",
            "Because it seems not to be included in the main subject. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Hoff …\x01",
            "I want to watch for a while\x01",
            "But I do. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "This time, to you guys\x01",
            "I want you to search ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I survived when I was young\x01",
            "It is my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FDo you live apart …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Oh, we are in the Liber Kingdom\x01",
            "I am living ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Actually, for me, when I was little\x01",
            "Living in the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Due to circumstances parents divorced,\x01",
            "There is a maternal parent's home\x01",
            "It was taken over by Libert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I guess I never meet again\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "The other day between us\x01",
            "This child I love was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "そしたらAlmu、\x01",
            "By all means to your father-in-law\x01",
            "Tell me you want to show off this girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "There were various things with my mother\x01",
            "It may be,\x01",
            "For me it's a real father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Having a happy family built\x01",
            "I absolutely wanted to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "So, persuade my mother\x01",
            "I decided to come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "However……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAfter a long time,\x01",
            "My father's place is\x01",
            "Does not it understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Oh, that's right ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "There was a mansion in a residential area\x01",
            "It should be,\x01",
            "Beautiful It is all lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I also asked my mother in communication,\x01",
            "Almost since I got divorced\x01",
            "It seems she did not get in touch … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "So, we are\x01",
            "I decided to look for my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Almuと一緒に\x01",
            "I listened to stories in various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Then, after sudden illness hospitalization\x01",
            "What moved to the old city is\x01",
            "分かったんHowever……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When we go to see you,\x01",
            "I do not usually come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FPerhaps,\x01",
            "Even on a trip for a mistake\x01",
            "Have you gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, I do not know ……\x02\x03",
            "#00000FFrom the residential area to the old city\x01",
            "It's a pretty special career.\x02\x03",
            "Ellie, who lived in a residential area\x01",
            "Does it make sense?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1E, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FNo, there is nothing that I do not have ….\x02\x03",
            "#00100Fあの、Almuさん。\x01",
            "Your father's name and occupation\x01",
            "Do you remember?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "Well, I guess so.\x01",
            "Because it is only the story that I asked to my mother\x01",
            "I do not know if I still work for that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I know the name.\x01",
            "One member of the Crossbell City Council,\x01",
            "People named \"Gabbal\".\x02",
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

    ChrTalk(
        0x101,
        "#00005FCongressman Gebal …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, that omen?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1E,
        "Oh … you know! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYeah, a while ago\x01",
            "I met you on request.\x02\x03",
            "#00100FAnyway, first of all, in the old city\x01",
            "You may as well visit the apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, yes.\x02\x03",
            "#00000FNow also he has no circumstances\x01",
            "You may understand something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Oh, I asked you guys,\x01",
            "It must be destiny!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I will leave it to you all,\x01",
            "Please find your father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fええ、Please choose for me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Searching for living fathers】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x90, 0x1, 0x0)
    SetScenarioFlags(0x19A, 6)
    Return()

    # Function_56_110A9 end

    SaveToFile()

Try(main)
