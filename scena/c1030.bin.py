from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Zhanghui",               # 1
        "Feng",                   # 2
        "Shanshan",               # 3
        "Puck",                   # 4
        "Ruth",                   # 5
        "Grid",                   # 6
        "Bond",                   # 7
        "Creil",                  # 8
        "Sunita",                 # 9
        "Mary",                   # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Reporter Noticia",       # 15
        "Grace",                  # 16
        "Reins",                  # 17
        "Madam",                  # 18
        "Boy",                    # 19
        "Citizen",                # 20
        "Rixia",                  # 21
        "Sister Ries",            # 22
        "Alm",                    # 23
        "Aerie",                  # 24
        "Alexei",                 # 25
        "Cronk",                  # 26
        "Danes",                  # 27
        "Lily",                   # 28
        "Marte",                  # 29
        "Cao",                    # 30
        "Lau",                    # 31
        "Nielsen",                # 32
        "Lechter",                # 33
        "食器",                   # 34
        "食器",                   # 35
        "食器",                   # 36
        "食器",                   # 37
        "食器",                   # 38
        "食器",                   # 39
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
        "Function_7_39BA",         # 07, 7
        "Function_8_4A3F",         # 08, 8
        "Function_9_4B45",         # 09, 9
        "Function_10_6229",        # 0A, 10
        "Function_11_62E3",        # 0B, 11
        "Function_12_6544",        # 0C, 12
        "Function_13_664A",        # 0D, 13
        "Function_14_73D4",        # 0E, 14
        "Function_15_74DA",        # 0F, 15
        "Function_16_85F5",        # 10, 16
        "Function_17_952F",        # 11, 17
        "Function_18_9598",        # 12, 18
        "Function_19_95C6",        # 13, 19
        "Function_20_95E7",        # 14, 20
        "Function_21_967B",        # 15, 21
        "Function_22_9877",        # 16, 22
        "Function_23_A244",        # 17, 23
        "Function_24_A5E7",        # 18, 24
        "Function_25_A767",        # 19, 25
        "Function_26_A7DF",        # 1A, 26
        "Function_27_A91C",        # 1B, 27
        "Function_28_A97E",        # 1C, 28
        "Function_29_A99F",        # 1D, 29
        "Function_30_AFF1",        # 1E, 30
        "Function_31_B0C4",        # 1F, 31
        "Function_32_B15C",        # 20, 32
        "Function_33_B33A",        # 21, 33
        "Function_34_B455",        # 22, 34
        "Function_35_BAE0",        # 23, 35
        "Function_36_BBAD",        # 24, 36
        "Function_37_BC64",        # 25, 37
        "Function_38_C9FD",        # 26, 38
        "Function_39_CD78",        # 27, 39
        "Function_40_CF0E",        # 28, 40
        "Function_41_D1C1",        # 29, 41
        "Function_42_D2C8",        # 2A, 42
        "Function_43_D3DC",        # 2B, 43
        "Function_44_D4E2",        # 2C, 44
        "Function_45_D4FE",        # 2D, 45
        "Function_46_D6B0",        # 2E, 46
        "Function_47_D7C0",        # 2F, 47
        "Function_48_D8AA",        # 30, 48
        "Function_49_E15D",        # 31, 49
        "Function_50_F31A",        # 32, 50
        "Function_51_100BB",       # 33, 51
        "Function_52_100EC",       # 34, 52
        "Function_53_111B8",       # 35, 53
        "Function_54_11931",       # 36, 54
        "Function_55_121BD",       # 37, 55
        "Function_56_123D5",       # 38, 56
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
            "If you're that pleased with it,\x01",
            "then it was worth making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you'd like to enjoy my cooking\x01",
            "again, please come anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B6")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2331")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B5")

    ChrTalk(
        0xFE,
        (
            "...Goodness, gracious me. Just when\x01",
            "I thought the weirdness outside ended,\x01",
            "it's just one weird thing after the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, it looks like you\x01",
            "guys are going somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in this situation, I want our\x01",
            "police officers to do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUmm, what's wrong?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A92")

    ChrTalk(
        0xFE,
        (
            "Hmm... It can't be helped. It looks like\x01",
            "you're doing your best on your chef training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today I shall teach you the\x01",
            "recipe that is told only to\x01",
            "the star of each generation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After all, you somehow managed to fill in that\x01",
            "recipe notebook I forced onto you.\x07\x00\x02",
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
            ""Medicinal Mapo Tofu"\x07\x00",
            " recipe obtained!\x02",
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
        "...There you go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(This is... It looks like the last\x01",
            "page of the notebook is filled in.)\x02\x03",
            "#00000FUmm, is this ok?\x01",
            "It's such a\x01",
            "precious recipe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. Thanks are not required. \x01",
            "I wanted to teach you it, \x01",
            "and so I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, the way\x01",
            "of the chef is very strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continue to focus on your\x01",
            "training from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1A92")


    ChrTalk(
        0xFE,
        (
            "Hmm... It can't be helped. It looks like\x01",
            "you're doing your best on your chef training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have put my soul into\x01",
            "this dish. Please take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x193, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph, I need no thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, the way\x01",
            "of the chef is very strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continue to focus on your\x01",
            "training from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1E")


    ChrTalk(
        0x101,
        "#00011F...Eh? R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come again if you get the chance.\x01",
            "I'll give you real chef training.\x02",
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
            "#00012FU-Umm... I've had a bad\x01",
            "feeling for awhile, but.\x02\x03",
            "Is it possible you\x01",
            "mistook us for people who\x01",
            "came for chef training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm? Are you talking about the\x01",
            "misunderstanding of many months ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no, this matter is different. Here, let\x01",
            "me have a look at your recipe notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell Chef League Member\x01",
            "Lloyd Bannings. It says it\x01",
            "right there in your notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a participating store,\x01",
            "it's my duty to train anyone\x01",
            "who has one. That's just it!\x02",
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
            "#00200FSo that recipe notebook\x01",
            "is the real deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FOh. I never\x01",
            "realized at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha. Then that means\x01",
            "all of us are fine chef\x01",
            "material, right?\x02\x03",
            "It might not be too\x01",
            "bad to try for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I don't know if I should\x01",
            "say it's reckless, but...\x02\x03",
            "#00000FUmm, but thank\x01",
            "you very much.\x02\x03",
            "I don't know how to say this, but\x01",
            "receiving something this nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. I don't need your thanks. For nice\x01",
            "young men and women like yourselves,\x01",
            "it was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, my cooking will give you energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want you to eat up, and get\x01",
            "back our daily lives right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Even so, I believe in you.\x01\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DE, 4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B0")

    label("loc_21B0")

    Jump("loc_232C")

    label("loc_21B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229B")

    ChrTalk(
        0xFE,
        (
            "Seriously, nothing but weird stuff ever happens. \x01",
            "Hmph, well I don't know what'd happen\x01",
            "if I panicked, so I'll keep running the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That shining pale azure tree is creepy.\x01",
            "I hope peace returns soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_232C")

    label("loc_229B")


    ChrTalk(
        0xFE,
        (
            "The Old Dragon is open for business.\x01",
            "If you're ordering, have a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Looks like you're\x01",
            "going somewhere.\x01",
            "Have a meal before you go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232C")

    Jump("loc_39B6")

    label("loc_2331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23FF")

    ChrTalk(
        0xFE,
        (
            "I don't know how long this martial\x01",
            "law will go on and it's getting on my\x01",
            "nerves. What's with this situation!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those monsters outside\x01",
            "damage my store, they\x01",
            "won't get away with it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B6")

    label("loc_23FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_249E")

    ChrTalk(
        0xFE,
        (
            "Seems like the citizens are excited\x01",
            "for Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really care, but\x01",
            "I wish they'd stop making\x01",
            "a fuss in my store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B6")

    label("loc_249E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256C")

    ChrTalk(
        0xFE,
        (
            "Rixia has disappeared, and it's\x01",
            "had quite the impact on Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's someone she could\x01",
            "really call a friend...\x01",
            "That's understandable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she cheers\x01",
            "up somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2852")

    label("loc_256C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C7")

    ChrTalk(
        0xFE,
        (
            "Shanshan looks\x01",
            "happy somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Has she cheered up or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2852")

    label("loc_25C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C4")

    ChrTalk(
        0xFE,
        (
            "Shanshan... To think she'd\x01",
            "participate in a pageant\x01",
            "without telling me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought she refused the invitation of the\x01",
            "Merchants Association President's grandson...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Who did this!? When I find\x01",
            "them, I'll cleave them limb from\x01",
            "limb with this kitchen knife!\x02",
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
        "#00306F(W-We can't say a word...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Hu hu. It'd be fun to see his\x01",
            "reaction when he finds out, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2852")

    label("loc_27C4")


    ChrTalk(
        0xFE,
        (
            "Well, it's great that Shanshan's\x01",
            "smile is back, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But even so, I'll tear\x01",
            "the one that made her\x01",
            "participate limb-from-limb.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2852")

    Jump("loc_39B6")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28EE")

    ChrTalk(
        0xFE,
        (
            "Hmm? What's wrong?\x01",
            "You look cornered, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't fight if you're hungry. \x01",
            "That's true the world over.\x01",
            "You should eat up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B6")

    label("loc_28EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2973")

    ChrTalk(
        0xFE,
        (
            "I always like it when there's\x01",
            "fewer customers on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can prepare tomorrow's\x01",
            "ingredients in one go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B6")

    label("loc_2973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AE4")

    ChrTalk(
        0xFE,
        (
            "Good grief. I tried having the part time \x01",
            "worker do some simple cooking, but...\x01",
            "He was completely useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to make him do\x01",
            "chores for awhile like I thought.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ADF")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get coverage for\x01",
            "the gourmet guide here, but...)\x02\x03",
            "#00003F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADF")

    Jump("loc_39B6")

    label("loc_2AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2C8F")
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C04")

    ChrTalk(
        0xFE,
        (
            "The secret to making fried rice\x01",
            "is to cook it using high heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do that, it'll have a nice\x01",
            "texture without sticking to the pan.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        "W-Wow, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey! Keep your\x01",
            "eyes on it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1200)
    OP_64(0xC)
    OP_93(0xC, 0x0, 0x1F4)

    ChrTalk(
        0xC,
        "S-Sorry!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    Jump("loc_2C86")

    label("loc_2C04")


    ChrTalk(
        0xFE,
        (
            "Ah, enough already...\x01",
            "It burned as soon as I said it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got to eat your\x01",
            "mistakes yourself. You hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wah...!\x02",
    )

    CloseMessageWindow()

    label("loc_2C86")

    OP_4C(0xC, 0xFF)
    Jump("loc_39B6")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9C")

    ChrTalk(
        0xFE,
        (
            "If Crossbell wants independence,\x01",
            "I think they should be, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The lack of safety\x01",
            "guarantees from the Empire\x01",
            "and Republic is the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want Shanshan to be in\x01",
            "even 1 rege of danger. That's\x01",
            "why I oppose independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E2E")

    label("loc_2D9C")


    ChrTalk(
        0xFE,
        (
            "If security can't be guaranteed,\x01",
            "then I oppose independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Shanshan is exposed to\x01",
            "even 1 rege of danger,\x01",
            "it's out of the question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2E")

    Jump("loc_39B6")

    label("loc_2E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFC")

    ChrTalk(
        0xFE,
        (
            "My new part-time worker\x01",
            "just doesn't learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I get the feeling he can't\x01",
            "stop leering at Shanshan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. I think I'll give him\x01",
            "a harsh scolding this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F94")

    label("loc_2EFC")


    ChrTalk(
        0xFE,
        (
            "Though there are a lot of people\x01",
            "who leer at Shanshan to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if any of them were to lay a hand\x01",
            "on her... Hmph, no need to say it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F94")

    Jump("loc_39B6")

    label("loc_2F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305F")

    ChrTalk(
        0xFE,
        (
            "There was a commotion\x01",
            "outside this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said the Republican\x01",
            "President has entered\x01",
            "Crossbell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't forgive anyone\x01",
            "who disturbs the peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_30B4")

    label("loc_305F")


    ChrTalk(
        0xFE,
        "I like my store quiet, see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't forgive anyone\x01",
            "who disturbs the peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B4")

    Jump("loc_39B6")

    label("loc_30B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_359A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3373")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Oh, you're that little customer\x01",
            "who was at the table earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How did you like my food?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        "C-Calling me little is too much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "But, the food was good as can be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's just, the quality is too high for the price.\x01",
            "As shopkeeper, you should raise―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, mister customer, you're\x01",
            "young but so very smart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You should remember this, though.\x01",
            "The Old Dragon is for the "common people".\x01",
            "I don't want to turn them away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's why I've no intention\x01",
            "of changing the prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I-I see... \x01",
            "I underestimated you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F(Ha ha. He's reserved all of a sudden.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1DC, 5)
    Jump("loc_340F")

    label("loc_3373")


    ChrTalk(
        0x8,
        (
            "Anyway, my little customer.\x01",
            "though you're still young, you're a\x01",
            "man who knows these differences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd really like Puck and\x01",
            "Ruth to learn from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340F")

    Jump("loc_3595")

    label("loc_3414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350F")

    ChrTalk(
        0xFE,
        (
            "For tomorrow's Trade Conference,\x01",
            "they say a lot of reporters will\x01",
            "be coming to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. There might be\x01",
            "reporters who take photos of\x01",
            "Shanshan without permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If any of them show up,\x01",
            "I won't go easy on them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3595")

    label("loc_350F")


    ChrTalk(
        0xFE,
        (
            "I think some reporters might take\x01",
            "photos of Shanshan without permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If any reporters\x01",
            "do that, I won't\x01",
            "go easy on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3595")

    Jump("loc_39B6")

    label("loc_359A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_363F")

    ChrTalk(
        0xFE,
        (
            "Oh yeah, those red-jacketed\x01",
            "brats from Downtown hardly\x01",
            "show their faces here anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't they\x01",
            "drink and skip\x01",
            "out on paying?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36C6")

    label("loc_363F")


    ChrTalk(
        0xFE,
        (
            "Not that I mind if guys who could lay\x01",
            "a hand on Shanshan aren't around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like them to pay their\x01",
            "tab, though. Seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C6")

    Jump("loc_39B6")

    label("loc_36CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_END)), "loc_384F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BB")

    ChrTalk(
        0xFE,
        (
            "And just when I\x01",
            "thought I'd gotten\x01",
            "some new apprentices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, if it's a mistake, it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But please, use that recipe\x01",
            "notebook as you like. You\x01",
            "should focus on your training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_384A")

    label("loc_37BB")


    ChrTalk(
        0xFE,
        (
            "But please, use that recipe\x01",
            "notebook as you like. You\x01",
            "should focus on your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trick to\x01",
            "growing is cooking.\x01",
            "...Understand?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384A")

    Jump("loc_39B6")

    label("loc_384F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3918")

    ChrTalk(
        0xFE,
        (
            "Customers mustn't recklessly\x01",
            "enter the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what you say,\x01",
            "to a chef, the kitchen\x01",
            "is sacred ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I wouldn't mind at all\x01",
            "if you were my apprentices.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39B6")

    label("loc_3918")


    ChrTalk(
        0xFE,
        (
            "If you want to learn the art of Eastern\x01",
            "cuisine, I stand ready to instruct you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If not, refrain from\x01",
            "entering the sacred ground\x01",
            "that is my kitchen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B6")

    TalkEnd(0xFE)
    Return()

    # Function_6_1556 end

    def Function_7_39BA(): pass

    label("Function_7_39BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B03")

    ChrTalk(
        0xFE,
        (
            "Hehe. That's Master for you.\x01",
            "He ignores that strange\x01",
            "scenery and keeps cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mother in the Republic is worried,\x01",
            "but the civil war that's occurring in the\x01",
            "Empire is the thing to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time for scattered thoughts.\x01",
            "I've got to study properly under Master.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BD9")

    label("loc_3B03")


    ChrTalk(
        0xFE,
        (
            "My mother in the Republic is worried,\x01",
            "but the civil war that's occurring in the\x01",
            "Empire is the thing to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time for scattered thoughts.\x01",
            "I've got to study properly under Master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD9")

    Jump("loc_4A3B")

    label("loc_3BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C5F")

    ChrTalk(
        0xFE,
        (
            "This has turned into an\x01",
            "unthinkable situation somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is probably\x01",
            "no time to be\x01",
            "running a store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3B")

    label("loc_3C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3A")

    ChrTalk(
        0xFE,
        (
            "Unless I run away today, it'll\x01",
            "probably be difficult to return\x01",
            "to the Republic for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder if my mother in the Republic is\x01",
            "worried. I wonder if it's better to go back...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D93")

    label("loc_3D3A")


    ChrTalk(
        0xFE,
        (
            "But, just where\x01",
            "did Rixia go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shanshan is worried. \x01",
            "It'd be nice if we knew.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D93")

    Jump("loc_4A3B")

    label("loc_3D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DA6")
    Jump("loc_4A3B")

    label("loc_3DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E1B")

    ChrTalk(
        0xFE,
        "Somehow, things have been dangerous lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not like we\x01",
            "can do anything about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3B")

    label("loc_3E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F13")

    ChrTalk(
        0xFE,
        (
            "Without part-time\x01",
            "workers, we'll have more\x01",
            "chores than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. Up until now,\x01",
            "we've been calling Puck\x01",
            "and Ruth "no-hopers."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, we've just started\x01",
            "calling them "somewhat\x01",
            "promising" Puck and Ruth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FA3")

    label("loc_3F13")


    ChrTalk(
        0xFE,
        (
            "It seems both Puck and Ruth were\x01",
            "finally able to throw away their\x01",
            "optimistic way of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've become a\x01",
            "little more promising.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA3")

    Jump("loc_4A3B")

    label("loc_3FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4058")

    ChrTalk(
        0xFE,
        (
            "Both Puck and Ruth\x01",
            "realized their own\x01",
            "inexperience and gave in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they don't regain their\x01",
            "footing here, they won't be able\x01",
            "to start a business at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3B")

    label("loc_4058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4156")

    ChrTalk(
        0xFE,
        (
            "Those Puck and Ruth. \x01",
            "They impertinently said they want\x01",
            "we make them do nicer jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I too said stuff like that a long\x01",
            "time ago, the Master got angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've got to understand that\x01",
            "chores are fine work too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41EA")

    label("loc_4156")


    ChrTalk(
        0xFE,
        (
            "You've got to take pride in the\x01",
            "work you've been given, no\x01",
            "matter what kind of work it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh, well, that's one of\x01",
            "the Master's sayings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EA")

    Jump("loc_4A3B")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_432A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C0")

    ChrTalk(
        0xFE,
        (
            "It's been awhile since I've\x01",
            "been back to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, working here is fun,\x01",
            "so I don't particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I need to contact my\x01",
            "mom every once in awhile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4325")

    label("loc_42C0")


    ChrTalk(
        0xFE,
        (
            "I guess I need to contact my mom\x01",
            "every once in awhile. It's been\x01",
            "awhile since I've been back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4325")

    Jump("loc_4A3B")

    label("loc_432A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4436")

    ChrTalk(
        0xFE,
        (
            "Even now, I'm on the Master's\x01",
            "list of "people who have tried\x01",
            "to lay a hand on Shanshan."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in charge of looking after her.\x01",
            "It's not like I'd have a reason\x01",
            "to lay a hand on her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Shanshan is like\x01",
            "a little sister to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44E8")

    label("loc_4436")


    ChrTalk(
        0xFE,
        (
            "I've been with the Master for\x01",
            "a long time, and Shanshan\x01",
            "is like a little sister to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I've been watching\x01",
            "over her, I've no reason at\x01",
            "all to lay a hand on her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E8")

    Jump("loc_4A3B")

    label("loc_44ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_45F3")

    ChrTalk(
        0xFE,
        (
            "According to a rumor, the Master was running a business\x01",
            "in the Eastern District. It's a particularly bad place\x01",
            "for a business because of a lack of public order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I met the Master\x01",
            "in Crossbell, he hardly\x01",
            "ever tells me old stories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3B")

    label("loc_45F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F1")

    ChrTalk(
        0xFE,
        (
            "It seems like Master is fond\x01",
            "of the Eastern District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he drove out the\x01",
            "ruffians himself when\x01",
            "he lived there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That must be where the glint in\x01",
            "his eye comes from when he glares\x01",
            "at men who look at Shanshan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_476B")

    label("loc_46F1")


    ChrTalk(
        0xFE,
        (
            "It seems like Master is fond\x01",
            "of the Eastern District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, seriously. If you make\x01",
            "him angry, you'll regret it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476B")

    Jump("loc_4A3B")

    label("loc_4770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4872")

    ChrTalk(
        0xFE,
        (
            "You see, the other day, I tried\x01",
            "motioning to Rixia, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She didn't notice at all.\x01",
            "She gave me a fresh\x01",
            "greeting and left to train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, I think she wants\x01",
            "to enjoy Arc-en-ciel more\x01",
            "than she wants love, huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48F2")

    label("loc_4872")


    ChrTalk(
        0xFE,
        (
            "For Rixia, wanting\x01",
            "to enjoy Arc-en-ciel\x01",
            "can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, somehow I've\x01",
            "become embarrassed\x01",
            "to be living aimlessly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F2")

    Jump("loc_4A3B")

    label("loc_48F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AE")

    ChrTalk(
        0xFE,
        (
            "We've left chores like collecting\x01",
            "payment, cleaning and dishwashing\x01",
            "to Puck and Ruth, our newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, I'll be able to\x01",
            "focus on the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A3B")

    label("loc_49AE")


    ChrTalk(
        0xFE,
        (
            "We've left all chores to\x01",
            "Puck and Ruth, our newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, they've progressed\x01",
            "since when they couldn't even\x01",
            "be behind the counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3B")

    TalkEnd(0xFE)
    Return()

    # Function_7_39BA end

    def Function_8_4A3F(): pass

    label("Function_8_4A3F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4B3E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B39")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Rest\x01",      # 2
            "Quit\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AB4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4AB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4AD3")
    OP_AF(0x34)
    Jump("loc_4AD5")

    label("loc_4AD3")

    OP_AF(0x33)

    label("loc_4AD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B34")

    label("loc_4AE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B04")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B34")

    label("loc_4B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B18")
    Jump("loc_4B34")

    label("loc_4B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B34")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_4B34")

    Jump("loc_4A55")

    label("loc_4B39")

    Jump("loc_4B41")

    label("loc_4B3E")

    Call(0, 9)

    label("loc_4B41")

    TalkEnd(0xA)
    Return()

    # Function_8_4A3F end

    def Function_9_4B45(): pass

    label("Function_9_4B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EE1")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B70")
    Call(0, 11)
    Jump("loc_4D2E")

    label("loc_4B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9C")

    ChrTalk(
        0xA,
        (
            "Rixia and everyone, it seems\x01",
            "like you're going somewhere\x01",
            "dangerous right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I really wish you wouldn't,\x01",
            "but... I know if you say you're\x01",
            "going, Rixia, I can't stop you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be here waiting for you...\x01",
            "Absolutely return safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10704FYeah... I absolutely will.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D2E")

    label("loc_4C9C")


    ChrTalk(
        0xA,
        (
            "Rixia and everyone, it seems\x01",
            "like you're going somewhere\x01",
            "dangerous right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be here waiting for you...\x01",
            "Absolutely return safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2E")

    Jump("loc_4EDC")

    label("loc_4D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D45")
    Call(0, 10)
    Jump("loc_4EDC")

    label("loc_4D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4A")

    ChrTalk(
        0xA,
        (
            "Rixia and everyone, it seems\x01",
            "like you're going somewhere\x01",
            "dangerous right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I really wish you wouldn't,\x01",
            "but... I know if you say you're\x01",
            "going, Rixia, I can't stop you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be here waiting for you...\x01",
            "Absolutely return safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EDC")

    label("loc_4E4A")


    ChrTalk(
        0xA,
        (
            "Rixia and everyone, it seems\x01",
            "like you're going somewhere\x01",
            "dangerous right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be here waiting for you...\x01",
            "Absolutely return safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EDC")

    Jump("loc_6228")

    label("loc_4EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_506A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F0C")
    Call(0, 11)
    Jump("loc_4FC7")

    label("loc_4F0C")


    ChrTalk(
        0xA,
        (
            "*cry*... I'm so\x01",
            "glad to see you\x01",
            "again, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without saying anything,\x01",
            "I'll never forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah... I promise.\x01",
            "Thank you, Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC7")

    Jump("loc_5065")

    label("loc_4FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FDE")
    Call(0, 10)
    Jump("loc_5065")

    label("loc_4FDE")


    ChrTalk(
        0xA,
        (
            "*cry*... I'm so\x01",
            "glad to see you\x01",
            "again, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without saying anything,\x01",
            "I'll never forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5065")

    Jump("loc_6228")

    label("loc_506A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512A")

    ChrTalk(
        0xA,
        (
            "To think something like this\x01",
            "happened to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If this turns into a war,\x01",
            "I feel like I won't be\x01",
            "able to see Rixia again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Rixia, where are you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5194")

    label("loc_512A")


    ChrTalk(
        0xA,
        (
            "If this turns into a war,\x01",
            "I feel like I won't be\x01",
            "able to see Rixia again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Rixia, where are you?\x02",
    )

    CloseMessageWindow()

    label("loc_5194")

    Jump("loc_6228")

    label("loc_5199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_544D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51CB")
    Call(0, 53)
    Return()

    label("loc_51CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5320")

    ChrTalk(
        0xA,
        (
            "...Just before she disappeared,\x01",
            "Rixia left a letter for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            ""I'll be away from Crossbell\x01",
            "due to some circumstances"\x01",
            "she wrote...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Leaving Arc-en-ciel out\x01",
            "to dry... That doesn't\x01",
            "sound like Rixia at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I wonder what kind of circumstances they are.\x01",
            "I wish she discussed them with me first...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_53BE")

    label("loc_5320")


    ChrTalk(
        0xA,
        (
            "To leave Arc-en-ciel out to\x01",
            "dry and disappear... That\x01",
            "doesn't seem like Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Something that she couldn't even\x01",
            "discuss with me, her best friend...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53BE")

    Jump("loc_5448")

    label("loc_53C3")


    ChrTalk(
        0xA,
        (
            "I'll do my best to make\x01",
            "the pageant a success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be there in time for\x01",
            "the program, so please\x01",
            "contact me when it's time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5448")

    Jump("loc_6228")

    label("loc_544D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5619")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557F")

    ChrTalk(
        0xA,
        (
            "I spotted Rixia\x01",
            "going to Arc-en-ciel\x01",
            "early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I greeted her, but...\x01",
            "Somehow, she\x01",
            "seemed very down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_END)), "loc_5522")

    ChrTalk(
        0x101,
        (
            "#00008F(...I guess all we can\x01",
            "do now is keep quiet...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5577")

    label("loc_5522")


    ChrTalk(
        0x101,
        (
            "#00003F(...Rixia... Did she go\x01",
            "to Arc-en-ciel to check\x01",
            "on the situation there?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5577")

    SetScenarioFlags(0x0, 2)
    Jump("loc_5614")

    label("loc_557F")


    ChrTalk(
        0xA,
        (
            "I saw Rixia this morning...\x01",
            "She seemed very down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I wonder if something happened. \x01",
            "If it's something I can help with, \x01",
            "I would like to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5614")

    Jump("loc_6228")

    label("loc_5619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_576E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56CD")

    ChrTalk(
        0xA,
        (
            "Rixia said she had something\x01",
            "to attend to and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*, I would have liked to talk to her a\x01",
            "little longer, but... I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5769")

    label("loc_56CD")


    ChrTalk(
        0xA,
        (
            "I would have liked to talk to\x01",
            "her a little longer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If she has something to attend to, it can't\x01",
            "be helped. ...I've got to get back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5769")

    Jump("loc_6228")

    label("loc_576E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_57FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5789")
    Call(0, 48)
    Jump("loc_57F7")

    label("loc_5789")


    ChrTalk(
        0xA,
        (
            "Ehehe... It must've been embarrassing\x01",
            "for Rixia to say that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Let's be lifelong friends, Rixia!\x02",
    )

    CloseMessageWindow()

    label("loc_57F7")

    Jump("loc_6228")

    label("loc_57FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5897")

    ChrTalk(
        0xA,
        (
            "In the end, Puck and Ruth\x01",
            "couldn't keep up and returned\x01",
            "to their original shifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Geez, papa is such a hard customer to deal with.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6228")

    label("loc_5897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5941")

    ChrTalk(
        0xA,
        (
            "...Gourmet guide coverage?\x01",
            "Yeah, I heard about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Papa's in the kitchen. Why\x01",
            "not try asking him about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_5941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59DA")

    ChrTalk(
        0xA,
        (
            "Papa and Mr. Feng\x01",
            "said just to do the\x01",
            "finances today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Puck and Ruth are always so busy.\x01",
            "I wonder if they'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A59")

    label("loc_59DA")


    ChrTalk(
        0xA,
        (
            "Puck is waiting on\x01",
            "all the tables today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...He looks really busy. I wonder if\x01",
            "it's really ok for me not to help him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A59")

    Jump("loc_6228")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B2B")

    ChrTalk(
        0xA,
        (
            "Welcome.\x01",
            "Are you ordering anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like all our customers today\x01",
            "are talking about the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The mayor said it, but does it\x01",
            "really make it that important?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6228")

    label("loc_5B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1B")

    ChrTalk(
        0xA,
        (
            "I'm the one who recommended my childhood\x01",
            "friends Puck and Ruth to work here part time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm glad those two are\x01",
            "working so hard for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm proud of them since it was \x01",
            "I who recommended them to papa.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5CA6")

    label("loc_5C1B")


    ChrTalk(
        0xA,
        (
            "It seems Puck and Ruth\x01",
            "are doing their best\x01",
            "with part-time work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm proud of them since it was \x01",
            "I who recommended them to papa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA6")

    Jump("loc_6228")

    label("loc_5CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D9B")

    ChrTalk(
        0xA,
        (
            "According to papa, the Republic\x01",
            "has even more Easterners than\x01",
            "Crossbell does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because I came here when\x01",
            "I was small, I don't\x01",
            "remember it at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems like a very busy\x01",
            "place. It seems fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5E2D")

    label("loc_5D9B")


    ChrTalk(
        0xA,
        (
            "It seems the Republic has even more\x01",
            "Easterners than Crossbell does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems lively and fun. \x01",
            "I'd like to go there if I get the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E2D")

    Jump("loc_6228")

    label("loc_5E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5ECA")
    TurnDirection(0xA, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        "Ah, you're that cute customer from earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Come again, ok? We'll be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F5F")

    label("loc_5ECA")


    ChrTalk(
        0xA,
        (
            "That lady sitting at the counter\x01",
            "says she's a reporter from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uh uh. Since she's here, I wonder\x01",
            "if she'll take a cute photo of meee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F5F")

    Jump("loc_6228")

    label("loc_5F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_60DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606C")

    ChrTalk(
        0xA,
        (
            "I can't believe Mr. Feng.\x01",
            "He tried to seduce Rixia.\x01",
            "What a troublesome man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Rixia should be able\x01",
            "to find someone waaay\x01",
            "better than him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though this could be rude towards Mr. Feng,\x01",
            "as her friend, I can't give Rixia to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_60D8")

    label("loc_606C")


    ChrTalk(
        0xA,
        (
            "Rixia should be able\x01",
            "to find someone waaay\x01",
            "better than him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ehehe. As her friend,\x01",
            "I guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60D8")

    Jump("loc_6228")

    label("loc_60DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6174")

    ChrTalk(
        0xA,
        (
            "Welcome. Please,\x01",
            "sit wherever you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Papa may be a little scary, but his\x01",
            "food is the best thing on this earth!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6228")

    label("loc_6174")


    ChrTalk(
        0xA,
        (
            "It's already been a year\x01",
            "since I started working here,\x01",
            "and I've gotten used to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "All our customers are good people. If it\x01",
            "stays like this, I could work here foreeever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6228")

    Return()

    # Function_9_4B45 end

    def Function_10_6229(): pass

    label("Function_10_6229")


    ChrTalk(
        0xA,
        (
            "Rixia... I wonder\x01",
            "what she's doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To think something like this has\x01",
            "happened to Crossbell... I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...It might be good to\x01",
            "bring her by later, huh...)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_10_6229 end

    def Function_11_62E3(): pass

    label("Function_11_62E3")

    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    ChrTalk(
        0xA,
        (
            "R-Rixia...\x01",
            "Is it really you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Where have you been!?\x01",
            "I was super worried about you...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703FSorry, Shanshan...\x01",
            "for worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ooh... Seriously! \x01",
            "You're such an idiot, Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...But... Thank goodness\x01",
            "I can see you again...\x01",
            "Waaaaaah...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x106)

    ChrTalk(
        0x106,
        "#10705FD-Don't cry, Shanshan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sob*... I mean, I was\x01",
            "really worried about you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you leave again without saying anything,\x01",
            "I'll never forgive you, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10704FYeah, I'm really sorry.\x01",
            "...Thanks for waiting for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F(Rixia... I'm glad for you.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 0)
    Return()

    # Function_11_62E3 end

    def Function_12_6544(): pass

    label("Function_12_6544")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_6643")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_655A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Rest\x01",      # 2
            "Quit\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65B9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_65B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_65D8")
    OP_AF(0x34)
    Jump("loc_65DA")

    label("loc_65D8")

    OP_AF(0x33)

    label("loc_65DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6639")

    label("loc_65E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6609")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6639")

    label("loc_6609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661D")
    Jump("loc_6639")

    label("loc_661D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6639")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_6639")

    Jump("loc_655A")

    label("loc_663E")

    Jump("loc_6646")

    label("loc_6643")

    Call(0, 13)

    label("loc_6646")

    TalkEnd(0xB)
    Return()

    # Function_12_6544 end

    def Function_13_664A(): pass

    label("Function_13_664A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6709")

    ChrTalk(
        0xB,
        (
            "Everyone's happy with a full belly.\x01",
            "That's the Master's motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I open a store with Ruth\x01",
            "in the future, I'll think of the\x01",
            "customers in just that way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_678F")

    label("loc_6709")


    ChrTalk(
        0xB,
        (
            "And so, today we have a large serving for free, \x01",
            "and as many second helpings as you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Chow down! It'll\x01",
            "give you energy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678F")

    Jump("loc_73D3")

    label("loc_6794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6823")

    ChrTalk(
        0xB,
        (
            "I wonder if this is the time to\x01",
            "clean. ...Although, there's\x01",
            "no where I could run to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh*... All I can do is sigh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_6823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_68B1")

    ChrTalk(
        0xB,
        (
            "What's going to happen now?\x01",
            "I can't even guess, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You have to get through times\x01",
            "like these with fighting spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_68B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695B")

    ChrTalk(
        0xB,
        (
            "Mr. Feng went\x01",
            "to help with the\x01",
            "charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm on kitchen duty instead\x01",
            "as Master's assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to do the\x01",
            "best I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69D7")

    label("loc_695B")


    ChrTalk(
        0xB,
        (
            "Although what I can do is on\x01",
            "the level of simple chores...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mr. Feng's not here, so I've\x01",
            "got to do the best I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D7")

    Jump("loc_73D3")

    label("loc_69DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A7B")

    ChrTalk(
        0xB,
        "100, 200, 300 mira...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, I'm better at the\x01",
            "register than I was before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The more you do something,\x01",
            "the better you get, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_6A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B82")

    ChrTalk(
        0xB,
        (
            "When it comes to work, I thought you can\x01",
            "do anything just with fighting spirit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected, that line of thinking \x01",
            "might've been naive somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, for now, I've got to do what\x01",
            "I can! I know that's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6BE3")

    label("loc_6B82")


    ChrTalk(
        0xB,
        (
            "Me and Ruth were depressed\x01",
            "yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well for now, all I\x01",
            "can do is what I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE3")

    Jump("loc_73D3")

    label("loc_6BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C85")

    ChrTalk(
        0xB,
        "*sigh*, I'm so tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I watched Shanshan working\x01",
            "I thought it was all fun and games, but\x01",
            "it didn't turn out like that, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_6C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6CF7")

    ChrTalk(
        0xB,
        (
            "Clearing tables, taking\x01",
            "orders, carrying food...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Waah, I'm so busy,\x01",
            "my head's spinning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_6CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E29")

    ChrTalk(
        0xB,
        (
            "To increase his part-time pay,\x01",
            "Ruth said he was going to ask\x01",
            "for a more important position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's certain that, for our future,\x01",
            "we have to earn all we can now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, if it is me and Ruth, we'll\x01",
            "get through it with fighting spirit\x01",
            "no matter what kind of work it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6E80")

    label("loc_6E29")


    ChrTalk(
        0xB,
        (
            "Hehe, I might have some ability\x01",
            "as a clerk... I think I'll\x01",
            "try asking the Master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E80")

    Jump("loc_73D3")

    label("loc_6E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_703A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA8")

    ChrTalk(
        0xB,
        (
            "Ruth, Shanshan and I were\x01",
            "classmates when we were\x01",
            "in Sunday School, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ever since then, the Master\x01",
            "makes scary faces at anyone\x01",
            "interested in Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Earlier too, he\x01",
            "glared at me just\x01",
            "for greeting her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh*, I wish he'd give me a break.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7035")

    label("loc_6FA8")


    ChrTalk(
        0xB,
        (
            "The Master glared at me just\x01",
            "for greeting Shanshan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's been like this ever\x01",
            "since Sunday School...\x01",
            "I wish he'd give me a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7035")

    Jump("loc_73D3")

    label("loc_703A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_70D4")

    ChrTalk(
        0xB,
        (
            "Ruth tries to standardize\x01",
            "anything and everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's why I wouldn't mind at all\x01",
            "even if we ran a restaurant\x01",
            "like we planned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_70D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7177")

    ChrTalk(
        0xB,
        (
            "That Ruth has a tendency\x01",
            "to overthink things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we just work hard like this,\x01",
            "we'll definitely be bigshots!\x01",
            "Nothing will come of worrying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D3")

    label("loc_7177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7293")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7206")

    ChrTalk(
        0xB,
        (
            "Ouchie... \x01",
            "I slipped and\x01",
            "fell just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uwaaah, this pain! I'll make it\x01",
            "fly away with my fighting spirit!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_728E")

    label("loc_7206")


    ChrTalk(
        0xB,
        (
            "...Ouchie.\x01",
            "Well, fighting spirit out or not,\x01",
            "what hurts, hurts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You guys be careful not to\x01",
            "slip and fall in today's rain too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_728E")

    Jump("loc_73D3")

    label("loc_7293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7377")

    ChrTalk(
        0xB,
        (
            "Awhile back, me and my partner\x01",
            "Ruth started working part time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, I'm not very good\x01",
            "with this register work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's fun, but I'm always\x01",
            "getting scolded for messing\x01",
            "up counting the mira.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_73D3")

    label("loc_7377")


    ChrTalk(
        0xB,
        (
            "But, I kinda like\x01",
            "working here as\x01",
            "an assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I think I'll make the most of it.\x02",
    )

    CloseMessageWindow()

    label("loc_73D3")

    Return()

    # Function_13_664A end

    def Function_14_73D4(): pass

    label("Function_14_73D4")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_74D3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74CE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Rest\x01",      # 2
            "Quit\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7449")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7468")
    OP_AF(0x34)
    Jump("loc_746A")

    label("loc_7468")

    OP_AF(0x33)

    label("loc_746A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74C9")

    label("loc_7479")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7499")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74C9")

    label("loc_7499")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74AD")
    Jump("loc_74C9")

    label("loc_74AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74C9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 15)

    label("loc_74C9")

    Jump("loc_73EA")

    label("loc_74CE")

    Jump("loc_74D6")

    label("loc_74D3")

    Call(0, 15)

    label("loc_74D6")

    TalkEnd(0xC)
    Return()

    # Function_14_73D4 end

    def Function_15_74DA(): pass

    label("Function_15_74DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_76C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7624")

    ChrTalk(
        0xC,
        (
            "I'm sure this experience of doing our best in times\x01",
            "of crisis will be of use to us in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I plan to open a huge store with my partner\x01",
            "Puck in the future, but... For now, we've got\x01",
            "to do our best with the work in front of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Alright, if that's how\x01",
            "it's going to be, cleaning!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_76BE")

    label("loc_7624")


    ChrTalk(
        0xC,
        (
            "This experience of working hard\x01",
            "in a crisis will be useful when\x01",
            "I open a shop with Puck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Alright, if that's how\x01",
            "it's going to be, cleaning!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76BE")

    Jump("loc_85F4")

    label("loc_76C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7726")

    ChrTalk(
        0xC,
        "Those things walking around outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What are they going to do to us...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_85F4")

    label("loc_7726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77AF")

    ChrTalk(
        0xC,
        (
            "Yahhoo, they say Crossbell's\x01",
            "gonna be independent, huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Man, what a good news.\x01",
            "I'll put zeal into cleaning too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F4")

    label("loc_77AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_782B")

    ChrTalk(
        0xC,
        (
            "Downtown is close by. If we're\x01",
            "not careful, the same thing'll\x01",
            "happen to East Street...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...*shiver*.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85F4")

    label("loc_782B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_78E8")

    ChrTalk(
        0xC,
        (
            "Hmm, if I sweep this problematic\x01",
            "square floor in a circle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would have been done faster \x01",
            "if I had done this from the start. \x01",
            "Cleaning is harder than I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F4")

    label("loc_78E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7B44")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79B0")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage? Ah,\x01",
            "come to think of it, the Master\x01",
            "said something about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Master's in the kitchen.\x01",
            "You should speak with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B3F")

    label("loc_79B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AB3")

    ChrTalk(
        0xC,
        (
            "I was crushed by my experience\x01",
            "in the kitchen yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After speaking with Puck,\x01",
            "we decided to do our best\x01",
            "at what we can do for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Difficult work can't be\x01",
            "entrusted to those who can't\x01",
            "even do simple work, right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7B3F")

    label("loc_7AB3")


    ChrTalk(
        0xC,
        (
            "In order to open a huge store with my\x01",
            "partner Puck in the future too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now, we have to become able\x01",
            "to complete chores perfectly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3F")

    Jump("loc_85F4")

    label("loc_7B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7BAF")

    ChrTalk(
        0xC,
        (
            "...I'm finally free\x01",
            "of Gehenna's kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're no good at this.\x01",
            "No good at all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F4")

    label("loc_7BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C22")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "H-Hot...!!\x01",
            "And the wok\x01",
            "is s-so heavy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "C'mon, get going!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "S-Sorry!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_7CAF")

    label("loc_7C22")


    ChrTalk(
        0xC,
        (
            "E-Eek... When I helped\x01",
            "before, I thought it'd\x01",
            "be a piece of cake, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To think it'd be this hard to\x01",
            "make even one fried rice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CAF")

    Jump("loc_85F4")

    label("loc_7CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7F03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7C")

    ChrTalk(
        0xC,
        (
            "Gourmet guide coverage? Ah,\x01",
            "come to think of it, the Master\x01",
            "said something about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Master's in the kitchen.\x01",
            "You should speak with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EFE")

    label("loc_7D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E63")

    ChrTalk(
        0xC,
        (
            "I knew we can't get by\x01",
            "with these part time jobs of\x01",
            "nothing but small chores...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For now, I'll try\x01",
            "asking the Master\x01",
            "how we can do more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What? For Ruth and I,\x01",
            "any kind of work is a\x01",
            "walk in the park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7EFE")

    label("loc_7E63")


    ChrTalk(
        0xC,
        (
            "We've got to step up and rid\x01",
            "ourselves of these chores soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I helped in the kitchen a bit\x01",
            "awhile back... Next time,\x01",
            "I'll try asking the Master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EFE")

    Jump("loc_85F4")

    label("loc_7F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE1")

    ChrTalk(
        0xC,
        (
            "All of a sudden, the places\x01",
            "we have to clean doubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could that Puck have\x01",
            "spoken to Shanshan\x01",
            "in front of the Master...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if that were true, how're\x01",
            "we both responsible? Ugh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8063")

    label("loc_7FE1")


    ChrTalk(
        0xC,
        (
            "Ah, later I've got to clean\x01",
            "the back of the store too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because Puck was careless,\x01",
            "there's another big cleaning to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8063")

    Jump("loc_85F4")

    label("loc_8068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_81B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_813F")

    ChrTalk(
        0xC,
        (
            "Puck said it'd be good to open\x01",
            "our own business, like a restaurant\x01",
            "or something in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm... But we don't even have\x01",
            "the minimum funds required.\x01",
            "I'm not sure about this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_81B0")

    label("loc_813F")


    ChrTalk(
        0xC,
        (
            "I plan to open a huge shop with\x01",
            "Puck in the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A restaurant, huh?\x01",
            "I'm not sure about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B0")

    Jump("loc_85F4")

    label("loc_81B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_82EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8274")

    ChrTalk(
        0xC,
        (
            "That Puck. It seems like\x01",
            "he's enjoying this part-time\x01",
            "job a little too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I bet he's forgotten our\x01",
            "goal of opening a store\x01",
            "together in the future...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_82E6")

    label("loc_8274")


    ChrTalk(
        0xC,
        (
            "We only took this\x01",
            "job as a way to\x01",
            "get mira for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That Puck sure looks like\x01",
            "he's enjoying himself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82E6")

    Jump("loc_85F4")

    label("loc_82EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_848B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83F0")

    ChrTalk(
        0xC,
        (
            "*sigh*... The sound\x01",
            "of the rain makes\x01",
            "me feel depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're saving little-by-little, but the\x01",
            "day we open our store is still far-off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder if we're really\x01",
            "getting closer to our dream,\x01",
            "working part-time like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8486")

    label("loc_83F0")


    ChrTalk(
        0xC,
        (
            "I wonder if we're really\x01",
            "getting closer to our dream,\x01",
            "working part-time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think I'll ask Puck what he\x01",
            "thinks about this later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8486")

    Jump("loc_85F4")

    label("loc_848B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_85F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8551")

    ChrTalk(
        0xC,
        (
            "My partner Puck and I have\x01",
            "started working part-time to\x01",
            "raise funds to open our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "These are our early days for when\x01",
            "one day we'll open our store, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_85F4")

    label("loc_8551")


    ChrTalk(
        0xC,
        (
            "Still, the Master is strict,\x01",
            "and the pay is low...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We got hired because we're childhood\x01",
            "friends with Shanshan, but... \x01",
            "I'm kind of regretting it lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F4")

    Return()

    # Function_15_74DA end

    def Function_16_85F5(): pass

    label("Function_16_85F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_87F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_873C")

    ChrTalk(
        0xFE,
        (
            "*munch, munch*... \x01",
            "We've resumed our shipping business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up until now, our routes have been mostly\x01",
            "to the Republic, but it seems we'll have to\x01",
            "stick within the autonomous state for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what we have to do isn't all that different.\x01",
            "We just have to do our best going forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_87F2")

    label("loc_873C")


    ChrTalk(
        0xFE,
        (
            "Well, just because we're limited\x01",
            "to in-state, what we have to do\x01",
            "isn't all that different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having a proper meal beforehand  I'll be\x01",
            "able to do my best, the same as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F2")

    Jump("loc_952B")

    label("loc_87F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8805")
    Jump("loc_952B")

    label("loc_8805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_89E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F1")

    ChrTalk(
        0xFE,
        (
            "As a Crossbell citizen,\x01",
            "independence is a happy thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, that hero,\x01",
            "Arios MacLaine, bears the\x01",
            "burden of state defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if the Empire or Republic\x01",
            "is our enemy, that's reassuring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_89E4")

    label("loc_88F1")


    ChrTalk(
        0xFE,
        (
            "Until I know how we're going to deal with the\x01",
            "Empire or Republic, my business is closed.\x01",
            "...Well, I suppose there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all is said and done,\x01",
            "the "Divine Blade of Wind" is in\x01",
            "Crossbell. I'm sure he'll protect us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E4")

    Jump("loc_952B")

    label("loc_89E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ACA")

    ChrTalk(
        0xFE,
        (
            "I used Tangram Gate for\x01",
            "my business, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The atmosphere is a lot\x01",
            "more tense than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like they're paying more attention to\x01",
            "the people coming and going than usual, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8B39")

    label("loc_8ACA")


    ChrTalk(
        0xFE,
        (
            "I can't run my business if\x01",
            "the border gate is like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll eat my food.\x01",
            "*munch, munch*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B39")

    Jump("loc_952B")

    label("loc_8B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8BF0")

    ChrTalk(
        0xFE,
        (
            "To think Mainz's occupied...\x01",
            "I don't know what's happened,\x01",
            "but that's absurd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the CGF are elites.\x01",
            "It'll be all right if we\x01",
            "leave it to them, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952B")

    label("loc_8BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8C68")

    ChrTalk(
        0xFE,
        "Rain again today, unfortunately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dangerous to drive in the rain.\x01",
            "I've got to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952B")

    label("loc_8C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1D")

    ChrTalk(
        0xFE,
        (
            "It seems the waitress\x01",
            "is back too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm finished,\x01",
            "I think I'll have a\x01",
            "drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Huh, what!? It's\x01",
            "past time to start\x01",
            "the deliveries!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8D7F")

    label("loc_8D1D")


    ChrTalk(
        0xFE,
        (
            "T-This isn't good. \x01",
            "I should have left for\x01",
            "deliveries hours ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I've got to hurry...\x02",
    )

    CloseMessageWindow()

    label("loc_8D7F")

    Jump("loc_952B")

    label("loc_8D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DFC")

    ChrTalk(
        0xFE,
        (
            "Oh... Isn't there the\x01",
            "usual waitress today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I've got to pull\x01",
            "myself together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8E42")

    label("loc_8DFC")


    ChrTalk(
        0xFE,
        (
            "I always knew this store\x01",
            "exists because of that\x01",
            "waitress' smile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E42")

    Jump("loc_952B")

    label("loc_8E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F14")

    ChrTalk(
        0xFE,
        (
            "The most capable\x01",
            "orbal truck is Verne\x01",
            "Corp.'s latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, the latest model\x01",
            "is out of reach of\x01",
            "companies like mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In short, they're\x01",
            "just that expensive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8F8B")

    label("loc_8F14")


    ChrTalk(
        0xFE,
        (
            "I can't quite buy the\x01",
            "latest orbal model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's especially tough for companies\x01",
            "that aren't in the best shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F8B")

    Jump("loc_952B")

    label("loc_8F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9029")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm a little interested in\x01",
            "the Trade Conference, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got work to do.\x01",
            "I've got to eat while I can.\x01",
            "*munch, munch*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952B")

    label("loc_9029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_90BA")

    ChrTalk(
        0xFE,
        (
            "Wow, East Street\x01",
            "is super busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, traffic restrictions\x01",
            "are suspended... I've got to\x01",
            "get back to work while I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952B")

    label("loc_90BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_92CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9210")

    ChrTalk(
        0xFE,
        (
            "I'm told that traffic restrictions\x01",
            "will be in force tomorrow from Tangram\x01",
            "Gate to East Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Republican President is coming\x01",
            "for the Trade Conference, and they're\x01",
            "going on high alert for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the restrictions are only\x01",
            "for a single day... I doubt\x01",
            "it'll impact my business much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_92C5")

    label("loc_9210")


    ChrTalk(
        0xFE,
        (
            "There will be traffic restrictions\x01",
            "tomorrow from Tangram Gate \x01",
            "to East Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it'll only be for\x01",
            "one day... I'll need to\x01",
            "revise the delivery schedule.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92C5")

    Jump("loc_952B")

    label("loc_92CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_936D")

    ChrTalk(
        0xFE,
        (
            "If I remember correctly, they said\x01",
            "there'll be rain over a wide area today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's best if I\x01",
            "finish work now before\x01",
            "it gets too bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952B")

    label("loc_936D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_952B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9471")

    ChrTalk(
        0xFE,
        (
            "Today, I'm handling a\x01",
            "large number of packages\x01",
            "from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I crossed the huge Cyre River\x01",
            "which flows through the border\x01",
            "and floored it through Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. The transport\x01",
            "industry isn't easy at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_952B")

    label("loc_9471")


    ChrTalk(
        0xFE,
        (
            "I crossed the huge Cyre River\x01",
            "which flows through the Republic border\x01",
            "and floored it through Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm through eating...\x01",
            "I'll take a spin through\x01",
            "the city before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_952B")

    TalkEnd(0xFE)
    Return()

    # Function_16_85F5 end

    def Function_17_952F(): pass

    label("Function_17_952F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm worried about my stand, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are President Mors, Roy\x01",
            "and the others all right...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_952F end

    def Function_18_9598(): pass

    label("Function_18_9598")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Lily, I'm here, so\x01",
            "calm down, ok?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_9598 end

    def Function_19_95C6(): pass

    label("Function_19_95C6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Danes, I'm scared...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_95C6 end

    def Function_20_95E7(): pass

    label("Function_20_95E7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I hope my husband who\x01",
            "is at home is safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. Now that the situation is like this, \x01",
            "I had to close up shop immediately.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_95E7 end

    def Function_21_967B(): pass

    label("Function_21_967B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_968F")
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    label("loc_968F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96B0")
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    label("loc_96B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D0")

    ChrTalk(
        0x25,
        (
            "#03204FWe plan to wait-and-see for now,\x01",
            "until the situation's resolved.\x02\x03",
            "After that, we'll slowly take over\x01",
            "the underworld, from which Revache\x01",
            "and the Red Constellation are gone.\x02\x03",
            "#03210FHu hu. It might not be too\x01",
            "long before we're enemies.\x01",
            "I look forward to then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9873")

    label("loc_97D0")


    ChrTalk(
        0x25,
        (
            "#03204FWe plan to wait-and-see for now,\x01",
            "until the situation's resolved.\x02\x03",
            "#03210FHu hu. It might not be too\x01",
            "long before we're enemies.\x01",
            "I look forward to then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9873")

    TalkEnd(0xFE)
    Return()

    # Function_21_967B end

    def Function_22_9877(): pass

    label("Function_22_9877")


    ChrTalk(
        0x25,
        (
            "#03200FOh, Mr. Lloyd and comrades...\x01",
            "Thank you all your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FM-Mr. Cao? What are\x01",
            "you doing in a place like...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FHu hu, is there something\x01",
            "strange about us being here?\x02\x03",
            "#03200FThe city has calmed down,\x01",
            "so we were just relaxing\x01",
            "having a meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBut even so, that's a\x01",
            "little too bold, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FA-And what's more, a seat right in\x01",
            "the middle of the restaurant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "I too had a problem with it, however...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "The waitress picked this seat for us,\x01",
            "and Master Cao didn't refuse it.\x02",
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
            "#03204FHu hu, isn't that just fine?\x01",
            "We're eating so we'd appreciate\x01",
            "if you'd take it easy.\x02\x03",
            "#03200FIt's been awhile since we fought against\x01",
            ""Red Constellation" so hard, as we did\x01",
            "in the Crossbell liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Regarding that. Thank you\x01",
            "very much for your cooperation.\x02\x03",
            "#00001FMr. Cao, what do you and\x01",
            "the others plan to do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03205FWe plan to keep watching the\x01",
            "situation until it's under control.\x02\x03",
            "#03209FAfter we have a handle on the\x01",
            "situation, we plan to build a\x01",
            "new HQ and resume business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F...As I thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FNow that our "Red Constellation" and\x01",
            "Revache competition is gone, there's\x01",
            "no further obstacles in our way.\x02\x03",
            "#03202FHu hu. There were many twists and turns, but...\x01",
            "It seems our original goal of gaining control of\x01",
            "Crossbell's underworld will finally be realized.\x02\x03",
            "It's no exaggeration to say it's\x01",
            "also due to the efforts of Master "Yin",\x01",
            "who you all have worked with before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013FKh......\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EDC")

    ChrTalk(
        0x106,
        "#10708F............\x02",
    )

    CloseMessageWindow()

    label("loc_9EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F42")

    ChrTalk(
        0x10A,
        (
            "#00603F...Sooner or later, we're going to\x01",
            "have to face "Heiyue" once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A012")

    label("loc_9F42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FAD")

    ChrTalk(
        0x109,
        (
            "#10103F...It seems we're going to have to\x01",
            "face "Heiyue" again sooner or later...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A012")

    label("loc_9FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A012")

    ChrTalk(
        0x105,
        (
            "#10403FLooks like we're going to have to face\x01",
            ""Heiyue" again sooner or later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A012")


    ChrTalk(
        0x25,
        (
            "#03209FWell that may be true, but...\x01",
            "I look forward to working\x01",
            "with you again, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...No matter what "barriers"\x01",
            "you put in our way...\x02\x03",
            "#00001FWe definitely won't lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03209FHu hu, that's why you're you.\x02\x03",
            "#03204FWell, people like us are\x01",
            "no significant "barrier".\x02\x03",
            "#03210FCompared to the chaos throughout the continent...\x01",
            "Especially the threat from the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F...T-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FHu hu, well for now, please\x01",
            "focus on doing something\x01",
            "about this situation.\x02\x03",
            "#03200FWe'll be rooting for you here,\x01",
            "from the shadows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 1)
    Return()

    # Function_22_9877 end

    def Function_23_A244(): pass

    label("Function_23_A244")


    ChrTalk(
        0x25,
        (
            "#03204FThat's right... Once this situation\x01",
            "is under control, I was thinking of\x01",
            "forming another contract with Miss Rixia.\x02\x03",
            "#03202FHu hu, how about\x01",
            "that, Miss Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F... I have a debt with you\x01",
            "and I don't know how I am\x01",
            "going to repay it, but...\x02\x03",
            "#10701FRight now, I cannot answer\x01",
            ""yes" to your question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#03204FWell, we have no\x01",
            "right to force you.\x02\x03",
            "And after this time, we'll\x01",
            "be even, so there'll be no\x01",
            "need for payment.\x02\x03",
            "#03200FHowever, if you feel\x01",
            "you are in our debt...\x02\x03",
            "#03209FArc-en-ciel S-seat tickets will be\x01",
            "appropriate compensation, I believe.\x02",
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
            "#03204FHu hu, that was a joke.\x02\x03",
            "#03200FIt's just... As I said before, to\x01",
            "reach the high place "Heiyue" is\x01",
            "aiming for, we want your strength.\x02\x03",
            "I will support your performances, \x01",
            "and I look forward to be on\x01",
            "good terms from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 2)
    Return()

    # Function_23_A244 end

    def Function_24_A5E7(): pass

    label("Function_24_A5E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5FC")
    Call(0, 22)
    Jump("loc_A763")

    label("loc_A5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6D8")

    ChrTalk(
        0xFE,
        (
            "...Regarding this incident I want\x01",
            "to thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We had vacated our hideout in the\x01",
            "Ancient Battlefield some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't help \x01",
            "you any more, but... \x01",
            "Please, do be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A763")

    label("loc_A6D8")


    ChrTalk(
        0xFE,
        (
            "We had vacated our hideout in the\x01",
            "Ancient Battlefield some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't help \x01",
            "you any more, but... \x01",
            "Please, do be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A763")

    TalkEnd(0xFE)
    Return()

    # Function_24_A5E7 end

    def Function_25_A767(): pass

    label("Function_25_A767")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I came to enjoy a restaurant meal with my family today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it seems they're\x01",
            "enjoying it. I'm glad.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_A767 end

    def Function_26_A7DF(): pass

    label("Function_26_A7DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8AB")

    ChrTalk(
        0xFE,
        "*breathe, breathe*, *slurp, slurp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These noodles have a spicy\x01",
            "and stimulating flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think a meal could make\x01",
            "one sweat this much... \x01",
            "But, it's really delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A918")

    label("loc_A8AB")


    ChrTalk(
        0xFE,
        (
            "I absolutely love\x01",
            "these noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though they're spicy and make\x01",
            "you sweat, they're quite delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A918")

    TalkEnd(0xFE)
    Return()

    # Function_26_A7DF end

    def Function_27_A91C(): pass

    label("Function_27_A91C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm eating out with\x01",
            "my family today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chew, chew*...\x01",
            "This "Mapo"\x01",
            "thing is great.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_A91C end

    def Function_28_A97E(): pass

    label("Function_28_A97E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*purr purr* nyaan...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_A97E end

    def Function_29_A99F(): pass

    label("Function_29_A99F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE32")

    ChrTalk(
        0x20,
        (
            "I'm sorry for Mr. Temas,\x01",
            "but this place's food is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "*munch, munch*... \x01",
            "Alright, I think I'll have seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh? Why is there a CGF member\x01",
            "in a place like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FCould it be...\x01",
            "Are you Mr. Alexei?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB42")
    Jump("loc_AB8C")

    label("loc_AB42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AB62")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8C")

    label("loc_AB62")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB82")
    OP_52(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8C")

    label("loc_AB82")

    OP_52(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB8C")

    OP_52(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    ChrTalk(
        0x20,
        (
            "Oh, Master Sergeant Noｱl. \x01",
            "Fancy meeting you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'm on break now.\x01",
            "I'm just relaxing here\x01",
            "a little, eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FY-You never change, do you. \x01",
            "Coming here all the way from\x01",
            "Tangram Gate just to have lunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FTangram Gate... \x01",
            "That border gate past\x01",
            "the East Highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, it's an important defense position\x01",
            "for Crossbell and managed by the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Recently, a new Vice Commander was assigned\x01",
            "and we've been busy doing stuff ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Sgt. Noｱl, you must have it tough too,\x01",
            "but please do your best. All of us at\x01",
            "the gate are cheering for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 6)
    ClearChrFlags(0x20, 0x10)
    Jump("loc_AFED")

    label("loc_AE32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF43")

    ChrTalk(
        0x20,
        (
            "Recently, a new vice commander was\x01",
            "assigned and we've been busy ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "And that new vice commander\x01",
            "is just as capable and\x01",
            "strict as Commander Sonya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Every once in awhile, I like to\x01",
            "relax in town, eat something\x01",
            "different and refresh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_AFED")

    label("loc_AF43")


    ChrTalk(
        0x20,
        (
            "That new vice commander is\x01",
            "just as capable and strict\x01",
            "as Commander Sonya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Every once in awhile, I like to\x01",
            "relax in town, eat something\x01",
            "different and refresh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFED")

    TalkEnd(0xFE)
    Return()

    # Function_29_A99F end

    def Function_30_AFF1(): pass

    label("Function_30_AFF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B06E")

    ChrTalk(
        0xFE,
        (
            "To think it'd rain when it's\x01",
            "our long-awaited vacation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's raining pretty\x01",
            "hard, and I'm cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0C0")

    label("loc_B06E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B0C0")

    ChrTalk(
        0xFE,
        "Hmm, this is really good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I knew Eastern cuisine was the best.\x02",
    )

    CloseMessageWindow()

    label("loc_B0C0")

    TalkEnd(0xFE)
    Return()

    # Function_30_AFF1 end

    def Function_31_B0C4(): pass

    label("Function_31_B0C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B125")

    ChrTalk(
        0xFE,
        "Now, now, my dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you eat something warm\x01",
            "here, it'll warm you up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B158")

    label("loc_B125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B158")

    ChrTalk(
        0xFE,
        (
            "I knew you'd like\x01",
            "some home cooking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B158")

    TalkEnd(0xFE)
    Return()

    # Function_31_B0C4 end

    def Function_32_B15C(): pass

    label("Function_32_B15C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B1F4")

    ChrTalk(
        0xFE,
        (
            "(*chatting*...) \x01",
            "*munch, munch*... Mmm, mmm...\x01",
            "This tourist guide is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell sure has a lot of\x01",
            "nice places, doesn't it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B336")

    label("loc_B1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B29B")

    ChrTalk(
        0xFE,
        (
            "(*clang, clang*...) \x01",
            "*sluuurp*... This is really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, those reporters that\x01",
            "were staying here seem they\x01",
            "quickly went to collect data.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B336")

    label("loc_B29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B336")

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*...\x01",
            "I always knew Crossbell was\x01",
            "a place with nice scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like the city is lively to\x01",
            "match the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B336")

    TalkEnd(0xFE)
    Return()

    # Function_32_B15C end

    def Function_33_B33A(): pass

    label("Function_33_B33A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B3AA")

    ChrTalk(
        0xFE,
        "Dear, my dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reading books is for\x01",
            "after you have finished\x01",
            "eating. How disgraceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B451")

    label("loc_B3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B402")

    ChrTalk(
        0xFE,
        "Dear, my dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stop making noise when\x01",
            "you eat. How disgraceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B451")

    label("loc_B402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B451")

    ChrTalk(
        0xFE,
        "Dear, my dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stop talking while you eat.\x01",
            "How disgraceful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B451")

    TalkEnd(0xFE)
    Return()

    # Function_33_B33A end

    def Function_34_B455(): pass

    label("Function_34_B455")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B600")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B59C")

    ChrTalk(
        0xFE,
        (
            "I'm telling you, airship service\x01",
            "will end today. It can't be helped.\x01",
            "Let's return home to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, I'd normally stay a\x01",
            "little longer to get coverage, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, security in\x01",
            "Crossbell can't be guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can only place our\x01",
            "hopes in the State Guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B5FB")

    label("loc_B59C")


    ChrTalk(
        0xFE,
        (
            "Anyway, I hope\x01",
            "Crossbell stays safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can only place our\x01",
            "hopes in the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5FB")

    Jump("loc_BADC")

    label("loc_B600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B623")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B61B")
    Call(0, 45)
    Jump("loc_B61E")

    label("loc_B61B")

    Call(0, 46)

    label("loc_B61E")

    Jump("loc_BADC")

    label("loc_B623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97D")

    ChrTalk(
        0xFE,
        (
            "My, if it isn't the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI think you're that Liberl reporter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou're still\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I didn't return home after\x01",
            "the Trade Conference, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, there was a\x01",
            "sensational proposal\x01",
            "like the independence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was hurriedly appointed for\x01",
            "long-term coverage, so I'll stay\x01",
            "until after the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FI see, so that's how it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, since I'm here,\x01",
            "I plan to see the Arc-en-ciel \x01",
            "renewal performance too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Incidentally, it's going to be on opening day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOpening day... \x01",
            "You did well to get a ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. They're hard to get, and there's\x01",
            "a significant premium price attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Well, we reporters\x01",
            "have our methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I expect we'll be\x01",
            "running into each other\x01",
            "around town for awhile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 0)
    Jump("loc_BA2F")

    label("loc_B97D")


    ChrTalk(
        0xFE,
        (
            "After I see the renewal performance\x01",
            "and the referendum, my Crossbell\x01",
            "coverage will be complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I expect we'll be\x01",
            "running into each other\x01",
            "around town for awhile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA2F")

    Jump("loc_BADC")

    label("loc_BA34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BADC")

    ChrTalk(
        0xFE,
        (
            "Uh uh, this store is on the same\x01",
            "level as those in Eastern District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible Nial and\x01",
            "Dorothy are eating Eastern\x01",
            "cuisine right around now too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BADC")

    TalkEnd(0xFE)
    Return()

    # Function_34_B455 end

    def Function_35_BAE0(): pass

    label("Function_35_BAE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAF2")
    Call(0, 37)
    Jump("loc_BBAC")

    label("loc_BAF2")

    TalkBegin(0xFE)

    ChrTalk(
        0x17,
        (
            "#02109FNow then, I'll finish eating,\x01",
            "then go around town for coverage.\x02\x03",
            "#02104FThe heads of state's security is\x01",
            "tight, but I might have a chance\x01",
            "while they're moving around♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_BBAC")

    Return()

    # Function_35_BAE0 end

    def Function_36_BBAD(): pass

    label("Function_36_BBAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBBF")
    Call(0, 37)
    Jump("loc_BC63")

    label("loc_BBBF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This afternoon, we plan to\x01",
            "go around conducting man-\x01",
            "on-the-street interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, if possible, I'd like to get\x01",
            "some photos of the heads of state.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_BC63")

    Return()

    # Function_36_BBAD end

    def Function_37_BC64(): pass

    label("Function_37_BC64")

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
        "#6POh, it's the Special Support Section.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 0x2)
    Sleep(200)

    ChrTalk(
        0x17,
        (
            "#12P#02100FCould you guys\x01",
            "be here to eat?\x02\x03",
            "#02109FUh uh, that aside, the inauguration\x01",
            "ceremony was amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, it really was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FThe aura of the heads of\x01",
            "state was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02106FRight? Right? Especially that\x01",
            ""Blood and Iron Chancellor".\x01",
            "He's the real deal!\x02\x03",
            "#02100FIt was my first time seeing him\x01",
            "this close, but it made me realize\x01",
            "his awesomeness all over again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "#12P#02105FRight, right, come to think of it,\x01",
            "there was that secretary-ish\x01",
            "man next to the Chancellor...\x02\x03",
            "#02103FHuh? If I'm not mistaken,\x01",
            "he's that Lechter kid who came\x01",
            "to Crossbell before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUmm, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02104FUh uh, well I understand\x01",
            "why that's hard to answer.\x02\x03",
            "#02101FTo tell you the truth, I just\x01",
            "remembered something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWhat do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103F...Last year, around springtime, the Blood\x01",
            "and Iron Chancellor and Chairman Hartmann\x01",
            "held a behind-the-scenes, informal meeting...\x02\x03",
            "#02100FYou guys of course know\x01",
            "about it, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, well, more or less...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn certain information channels\x01",
            "it's already a famous fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103FYes... \x01",
            "But, it wasn't at that time.\x02\x03",
            "Crossbell's mass media didn't mention it,\x01",
            "and neither did the Empire's...\x02\x03",
            "#02101FAnd of course not even the Crossbell\x01",
            "police got hold of that info at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P...What's more, even though he's\x01",
            "so important, it seems they\x01",
            "assigned hardly any guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PIt's as if he was casually\x01",
            "dropping by for a short walk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6P...Well, that's exactly why\x01",
            "secrecy is so important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303FHmm... What an amazing story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FYeah. To be honest, I can't even believe it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02106FYeah, you can't believe―\x01",
            "No, that's too harsh!\x02\x03",
            "#02100FBecause later, I'm going to\x01",
            "look into this every way I can.\x02\x03",
            "#02103FAs a result, some of the names of\x01",
            "people who seemed to be involved in the\x01",
            "setting of the talks were raised......\x02\x03",
            "#02101FI remember it was among them.\x01",
            "The name a young man, "Lechter".\x02",
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
            "#00005FJust the fact his name was mentioned\x01",
            "together with the Chancellor's is\x01",
            "good info itself, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FTo think the setting itself is\x01",
            "the work of Mr. Lechter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHow to say this... Those are\x01",
            "impressive counterintelligence skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02103F...Right, and that's just what a mere \x01",
            "secretary wouldn't be able to do.\x02\x03",
            "#02102FUnless...he's a member of the famed\x01",
            "Imperial Army Intelligence Division, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see...\x02\x03",
            "#00003F(That's Miss Grace for you.\x01",
            "She got all that by herself.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Yeah. She's so tenacious that's terrifyin'.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12P#02109FUh uh, it looks like I hit the bullseye, huh?\x02\x03",
            "#02106F*sigh*, but I can't believe\x01",
            "that kid was the Lechter \x01",
            "who appeared in public.\x02\x03",
            "#02102FWell, you guys have a job\x01",
            "to do so I won't detain\x01",
            "you any further, but...\x02\x03",
            "#02100FAnyway, it's sure that Lechter\x01",
            "kid isn't anybody normal.\x02\x03",
            "You guys should brace\x01",
            "yourselves if you're\x01",
            "getting involved with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, we'll keep it in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you for the information.\x02",
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

    # Function_37_BC64 end

    def Function_38_C9FD(): pass

    label("Function_38_C9FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CB66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CACB")

    ChrTalk(
        0xFE,
        (
            "I fought with my husband and\x01",
            "ran away from home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He finally apologized\x01",
            "yesterday while crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmm. \x01",
            "I felt slightly guilty for\x01",
            "pushing him that far...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CB61")

    label("loc_CACB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, well I got tired too\x01",
            "of running away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like some kind of\x01",
            "incident occurred too... \x01",
            "I should be getting home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB61")

    Jump("loc_CD74")

    label("loc_CB66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CC0E")

    ChrTalk(
        0xFE,
        (
            "I was found by my husband with whom\x01",
            "I fought. He told me to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, that's no way to apologize.\x01",
            "I didn't sense any sincerity at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD74")

    label("loc_CC0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CC94")

    ChrTalk(
        0xFE,
        (
            "Looks like they went back\x01",
            "to the usual waitress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what happened\x01",
            "to the unreliable\x01",
            "waiter from before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD74")

    label("loc_CC94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CCF8")

    ChrTalk(
        0xFE,
        (
            "The waiter looks\x01",
            "unreliable somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like him to bring\x01",
            "my food already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD74")

    label("loc_CCF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CD74")

    ChrTalk(
        0xFE,
        (
            "Because I fought with my\x01",
            "husband, I ran away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph... I won't forgive\x01",
            "him until he apologizes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD74")

    TalkEnd(0xFE)
    Return()

    # Function_38_C9FD end

    def Function_39_CD78(): pass

    label("Function_39_CD78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CDD6")

    ChrTalk(
        0xFE,
        (
            "Aww, man. I'm tired of\x01",
            "my grandparent's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to see papa.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF0A")

    label("loc_CDD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE03")

    ChrTalk(
        0xFE,
        (
            "Won't papa\x01",
            "come here yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF0A")

    label("loc_CE03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CE3D")

    ChrTalk(
        0xFE,
        (
            "*munch, munch*...\x01",
            "Ehehe, this is good!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF0A")

    label("loc_CE3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CE9E")

    ChrTalk(
        0xFE,
        (
            "Mama, the table is\x01",
            "kind of sticky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did the store people forget to clean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF0A")

    label("loc_CE9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF0A")

    ChrTalk(
        0xFE,
        "We're visiting mama's parent's home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Papa's coming later, she said.\x01",
            "He's busy with work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF0A")

    TalkEnd(0xFE)
    Return()

    # Function_39_CD78 end

    def Function_40_CF0E(): pass

    label("Function_40_CF0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14D")

    ChrTalk(
        0x1D,
        (
            "#04405FAh, everyone. \x01",
            "Fancy seeing you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, it looks like you're...\x01",
            "Eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04400FYes, I'm on break and came\x01",
            "here for something to eat.\x02\x03",
            "#04403FThis place's fried rice has\x01",
            "a deep and good flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, you're the\x01",
            "same as ever, Miss Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FT-That looks delicious, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(It looks like there's a lot of\x01",
            "plates on the counter...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hu hu. The Old Dragon\x01",
            "and a Sister don't match\x01",
            "very well at all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Miss Elie missed that\x01",
            "chance for a retort.\x01",
            "Is this normal...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 3)
    Jump("loc_D1BD")

    label("loc_D14D")


    ChrTalk(
        0x1D,
        (
            "#04400FI'll head back to the\x01",
            "cathedral in a little bit.\x02\x03",
            "Please come over there,\x01",
            "in case anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1BD")

    TalkEnd(0xFE)
    Return()

    # Function_40_CF0E end

    def Function_41_D1C1(): pass

    label("Function_41_D1C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183E, 7)), scpexpr(EXPR_END)), "loc_D24A")

    ChrTalk(
        0xFE,
        (
            "I volunteered for various things\x01",
            "to help with the reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Food is especially\x01",
            "good after hard work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183E, 7)
    Jump("loc_D2C4")

    label("loc_D24A")


    ChrTalk(
        0xFE,
        (
            "It looks like the Downtown\x01",
            "repairs are still in progress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still a lot of\x01",
            "things I can help them with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2C4")

    TalkEnd(0xFE)
    Return()

    # Function_41_D1C1 end

    def Function_42_D2C8(): pass

    label("Function_42_D2C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2FA")
    Call(0, 54)
    Return()

    label("loc_D2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_D388")

    ChrTalk(
        0xFE,
        (
            "Yeah, with this, I might\x01",
            "finally get to see my father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm leaving everything to\x01",
            "you guys. Please, find my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D388")

    Jump("loc_D3D8")

    label("loc_D38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D3D8")

    ChrTalk(
        0xFE,
        (
            "Aerie and Almin...\x01",
            "Yesterday was one\x01",
            "amazing day, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3D8")

    TalkEnd(0xFE)
    Return()

    # Function_42_D2C8 end

    def Function_43_D3DC(): pass

    label("Function_43_D3DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D48B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D40E")
    Call(0, 54)
    Return()

    label("loc_D40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_END)), "loc_D486")

    ChrTalk(
        0xFE,
        (
            "We'll definitely\x01",
            "see Alm's father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he'll hug Almin,\x01",
            "the fruit of our love!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Babuu.\x02",
    )

    CloseMessageWindow()

    label("loc_D486")

    Jump("loc_D4DE")

    label("loc_D48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D4DE")

    ChrTalk(
        0xFE,
        (
            "Yes, Alm... Yesterday\x01",
            "was one amazing,\x01",
            "amazing day.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Babu♪\x02",
    )

    CloseMessageWindow()

    label("loc_D4DE")

    TalkEnd(0xFE)
    Return()

    # Function_43_D3DC end

    def Function_44_D4E2(): pass

    label("Function_44_D4E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4F7")
    Call(0, 45)
    Jump("loc_D4FA")

    label("loc_D4F7")

    Call(0, 46)

    label("loc_D4FA")

    TalkEnd(0xFE)
    Return()

    # Function_44_D4E2 end

    def Function_45_D4FE(): pass

    label("Function_45_D4FE")


    ChrTalk(
        0x27,
        (
            "I see, so you're staying at The\x01",
            "Old Dragon Inn while you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Is this food here\x01",
            "to your liking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yes. It's so good,\x01",
            "I'm having trouble\x01",
            "not overeating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "But, sorry for calling\x01",
            "you out here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Normally, I should be\x01",
            "heading to your place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Hu hu, please don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Walking and wandering are\x01",
            "hobbies of mine, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Uh uh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "As expected of a\x01",
            "freelance journalist.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Return()

    # Function_45_D4FE end

    def Function_46_D6B0(): pass

    label("Function_46_D6B0")


    ChrTalk(
        0x16,
        (
            "But Mr. Nielsen, you're\x01",
            "staying for very long\x01",
            "this time, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You're concerned about developments\x01",
            "in your hometown, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "That's right. I suppose\x01",
            "you could say I know it\x01",
            "from experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Anyway, I plan to stay in\x01",
            "Crossbell awhile longer.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_46_D6B0 end

    def Function_47_D7C0(): pass

    label("Function_47_D7C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7D5")
    Call(0, 48)
    Jump("loc_D8A6")

    label("loc_D7D5")


    ChrTalk(
        0x1C,
        (
            "#01803FWhen I lived in the Republic,\x01",
            "I had to move repeatedly\x01",
            "due to my dad's work...\x02\x03",
            "#01802FUh uh, I'm really\x01",
            "thankful to Shanshan.\x02\x03",
            "My bonds with everyone, Miss Ilya\x01",
            "and the others are precious to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8A6")

    TalkEnd(0xFE)
    Return()

    # Function_47_D7C0 end

    def Function_48_D8AA(): pass

    label("Function_48_D8AA")

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
            "#01802FAh...\x01",
            "Hello, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100F*giggle*, hello Miss Rixia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAre you here for lunch today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802FUh uh, yes.\x02\x03",
            "After that, I was chatting\x01",
            "while having dessert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PYou guys are\x01",
            "policemen, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAww. And just when I was enjoying\x01",
            "some girl talk with Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00302FHa ha, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, meeting an artist\x01",
            "privately isn't a\x01",
            "chance you often get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FIndeed. It's hard to\x01",
            "figure out a famous\x01",
            "person's friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01809FAhaha... \x01",
            "No way, I'm still a newbie.\x02\x03",
            "#01802FShanshan often takes me places on her\x01",
            "days off when I'd just sit at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PUh uh. We're the same age, so we get along pretty well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAlso, even with Rixia's proportions is\x01",
            "fun to shop for cute clothes for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01809FAhaha, I almost can't\x01",
            "find cute things, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F(Hmm, it's true that it seems there're\x01",
            "only a few of Miss Rixia's size...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00203F(...A first world problem.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FHa ha, but you girls really are close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01802FUh uh, I'm really\x01",
            "grateful to Shanshan.\x02\x03",
            "#01803FWhen I lived in the Republic,\x01",
            "I had to move repeatedly due\x01",
            "to my dad's work...\x02\x03",
            "#01808FI've had trouble making\x01",
            "friends and have always\x01",
            "been by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303FI see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1C, 500)

    ChrTalk(
        0xA,
        "#11PUh uh, don't worry Rixia.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x1)

    ChrTalk(
        0xA,
        (
            "#11PNow that you're friends with me,\x01",
            "you'll never be alone again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe'll always be\x01",
            "together, Rixia!\x02",
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
            "#01802FAhaha... \x01",
            "Thank you, Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, looks like we're\x01",
            "the third wheel here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYeah, let's\x01",
            "leave them be.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0x0)

    ChrTalk(
        0x1C,
        (
            "#01806FSorry, everyone. It seems I\x01",
            "took up your valuable time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FNo, speaking with you made\x01",
            "a nice breather for us.\x02\x03",
            "#00002FSee you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#01802FYes, see you.\x02",
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

    # Function_48_D8AA end

    def Function_49_E15D(): pass

    label("Function_49_E15D")

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

    def lambda_E212():
        OP_98(0x101, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E212)
    Sleep(50)

    def lambda_E22F():
        OP_98(0x102, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E22F)
    Sleep(50)

    def lambda_E24C():
        OP_98(0x109, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E24C)
    Sleep(50)

    def lambda_E269():
        OP_98(0x105, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E269)
    OP_68(890, 1400, -390, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_0D()

    def lambda_E2AB():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E2AB)
    Sleep(50)

    def lambda_E2BB():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E2BB)
    Sleep(50)

    def lambda_E2CB():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E2CB)
    Sleep(50)

    def lambda_E2DB():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E2DB)
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
        "#12P#00001FThere he is...!\x02",
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
            "#03500FNow I understand...\x01",
            "You use Eastern pepper flowers, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PRight, there's quite the difference in\x01",
            "spiciness and flavor with just the pepper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIt's only cultivated in the East, but recently\x01",
            "I was able to order it via railroad transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03502F#11PMaaan, it was so unsatisfying\x01",
            "when making mapo myself...\x02\x03",
            "#03504FThe spice, eh...?\x01",
            "I've learned something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 5010, 0, 15540, 45)

    ChrTalk(
        0x101,
        (
            "#00000F#NMr. Lechter...\x01",
            "So you were here.\x02",
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

    def lambda_E63A():
        OP_98(0x101, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E63A)
    Sleep(50)

    def lambda_E657():
        OP_98(0x102, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E657)
    Sleep(50)

    def lambda_E674():
        OP_98(0x109, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E674)
    Sleep(50)

    def lambda_E691():
        OP_98(0x105, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E691)
    Sleep(50)
    OP_68(14290, 1400, 14500, 1500)
    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00105F(We found him easily...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(S-Somehow he looks like\x01",
            "so much irresponsible...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Then, if we could confirm his identity, \x01",
            "our mission would be complete...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#03505FHey, took you long enough.\x02\x03",
            "#03509FI was waiting for you, my best friends!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x28,
        (
            "#12P#03502FMaster.\x01",
            "These are the guys I talked you about before.\x02\x03",
            "#03504FThey haven't got willingness and guts for nothing,\x01",
            "so work them very hard!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x28, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        "Alright, thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#11PI think it'll be hard with four people,\x01",
            "but I'm glad Eastern cuisine spreads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDo your best and keep up with me!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00012FE-Ehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWhat're you talking...\x02",
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

    def lambda_EA0E():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA0E)
    Sleep(50)

    def lambda_EA1E():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EA1E)
    Sleep(50)

    def lambda_EA2E():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EA2E)
    Sleep(50)

    def lambda_EA3E():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EA3E)
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
        "#11P#00011FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FH-He ran away...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10309FHa ha, same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00107FW-We must chase after him!\x02",
    )

    CloseMessageWindow()

    def lambda_EB3F():
        OP_98(0x8, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EB3F)
    Sound(802, 0, 100, 0)
    OP_68(13640, 1400, 14410, 1000)
    MoveCamera(37, 24, 0, 1000)

    ChrTalk(
        0x8,
        "HEY, where're you going!?\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "Your training has already started!\x01",
            "First of all, pre-cooking practice!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EBEC():
        OP_93(0x101, 0x5A, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EBEC)
    Sleep(50)

    def lambda_EBFC():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EBFC)
    Sleep(50)

    def lambda_EC0C():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EC0C)
    Sleep(50)

    def lambda_EC1C():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EC1C)

    ChrTalk(
        0x101,
        "#6P#00011FN-No, we aren't here for...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FWe work for the\x01",
            "Crossbell Police──\x02",
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
            "Mrrr...\x01",
            "It can't be helped if it was a misunderstanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, somehow I guess it's fate.\x01",
            "Take this with you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE8B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Old Dragon Fried Rice recipe\x07\x00",
            " received.\x02",
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
            "Also, ",
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
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
            "#12P#00005FWait, is it alright?\x01",
            "We even got a notebook...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF0E")

    label("loc_EE8B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
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
            "#12P#00005FWait, is it alright?\x01",
            "Getting this for free...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF0E")

    AddItemNumber(0x2, 1)

    ChrTalk(
        0x8,
        (
            "They're just store remains, so don't worry about it.\x01",
            "Dedicate yourselves to it, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FThank you very much.\x01",
            "T-Then, we'll excuse us.\x02\x03",
            "#00001F──Everyone, after him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101FYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FRoger!\x02",
    )

    CloseMessageWindow()

    def lambda_F001():
        OP_93(0x101, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F001)

    def lambda_F00E():
        OP_93(0x102, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F00E)

    def lambda_F01B():
        OP_93(0x109, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F01B)

    def lambda_F028():
        OP_93(0x105, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F028)
    WaitChrThread(0x105, 1)

    def lambda_F039():
        OP_98(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F039)
    Sleep(50)

    def lambda_F056():
        OP_98(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F056)
    Sleep(50)

    def lambda_F073():
        OP_98(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F073)
    Sleep(50)

    def lambda_F090():
        OP_98(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F090)
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
            "※By investigating books laying around in many places\x01",
            "  or specific locations, you can learn dish "recipes".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※"Recipes" are recorded into the "Recipe Notebook".\x01",
            "  Using the "Recipe Notebook" you can always\x01",
            "  make dishes which have many effects.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Also, it is possible that the completed dish changes\x01",
            "  into a "Superb" dish or "Peculiar" dish.\x01",
            "  (The dish you cook can also end up in a "failure".)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※As for the ingredients used in cooking,\x01",
            "  they are sold at the general stores and in shops.\x01",
            "  Also, there is a chance that monsters drop them.\x07\x00\x02",
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

    # Function_49_E15D end

    def Function_50_F31A(): pass

    label("Function_50_F31A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F4D8")
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

    def lambda_F40C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F40C)

    def lambda_F41D():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F41D)

    def lambda_F437():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F437)

    def lambda_F448():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F448)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F47F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F47F)

    def lambda_F490():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F490)
    Sleep(200)

    def lambda_F4AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F4AD)

    def lambda_F4BE():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F4BE)
    Jump("loc_F787")

    label("loc_F4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F632")
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

    def lambda_F566():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F566)

    def lambda_F577():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F577)

    def lambda_F591():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F591)

    def lambda_F5A2():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F5A2)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F5D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F5D9)

    def lambda_F5EA():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5EA)
    Sleep(200)

    def lambda_F607():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F607)

    def lambda_F618():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F618)
    Jump("loc_F787")

    label("loc_F632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F787")
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

    def lambda_F6C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_F6C0)

    def lambda_F6D1():
        OP_95(0xFE, 1800, 30, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_F6D1)

    def lambda_F6EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F6EB)

    def lambda_F6FC():
        OP_95(0xFE, 1800, 30, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6FC)
    OP_68(1210, 1400, -360, 3000)
    SetCameraDistance(17850, 3000)
    Sleep(500)

    def lambda_F733():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F733)

    def lambda_F744():
        OP_95(0xFE, 600, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F744)
    Sleep(200)

    def lambda_F761():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F761)

    def lambda_F772():
        OP_95(0xFE, 200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F772)

    label("loc_F787")

    Sleep(500)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            ""The Old Dragon Inn"... A store on East Street\x01",
            "where Eastern cuisine is sold, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FShould we take a short break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmm, that's right. And just\x01",
            "when I was getting hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I want to see just what kind\x01",
            "of food they serve here.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F9EB")
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
    Jump("loc_FAF2")

    label("loc_F9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FA71")
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
    Jump("loc_FAF2")

    label("loc_FA71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FAF2")
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

    label("loc_FAF2")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#11P#00102FHow did The Old Dragon taste?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FB9F")

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah, I'd love to get the opinion of someone\x01",
            "who knows what the real thing tastes like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC85")

    label("loc_FB9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC14")

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, I'd love to hear the opinion of someone\x01",
            "who knows what the real thing tastes like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC85")

    label("loc_FC14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FC85")

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, I'd love to hear the opinion of someone\x01",
            "who knows what the real deal tastes like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC85")

    BeginChrThread(0x1A2, 3, 0, 51)
    Sleep(1000)
    EndChrThread(0x1A2, 0x3)

    ChrTalk(
        0x1A2,
        (
            "#5PKh― What's the\x01",
            "meaning of this!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PWhy does this store sell this kind\x01",
            "of thing at this kind of price?\x01",
            "Is the owner out of his mind!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FHey now, you shouldn't use such\x01",
            "a loud voice in a store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FNo, Shing is probably...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PFor example this Mapo Tofu... \x01",
            "The flavor isn't even beat by the three-star\x01",
            "restaurants in the Eastern District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PFor something this good, the price should\x01",
            "be three times what it is― Why is it not!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FE9D")

    ChrTalk(
        0x104,
        "#6P#00306FT-That, huh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF17")

    label("loc_FE9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FEE1")

    ChrTalk(
        0x109,
        "#6P#10106FSo that's what you're talking about...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF17")

    label("loc_FEE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FF17")

    ChrTalk(
        0x105,
        "#6P#10304FHu hu, so that's what it was.\x02",
    )

    CloseMessageWindow()

    label("loc_FF17")


    ChrTalk(
        0x1A2,
        (
            "#5PI-I don't believe this... Why is\x01",
            "a store like this in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha. Well anyway,\x01",
            "I'm glad you're satisfied.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 1)
    OP_29(0x73, 0x1, 0x9)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10001")
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
    Jump("loc_10080")

    label("loc_10001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10043")
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
    Jump("loc_10080")

    label("loc_10043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10080")
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

    label("loc_10080")

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

    # Function_50_F31A end

    def Function_51_100BB(): pass

    label("Function_51_100BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_100EB")

    def lambda_100CB():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100CB)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_51_100BB")

    label("loc_100EB")

    Return()

    # Function_51_100BB end

    def Function_52_100EC(): pass

    label("Function_52_100EC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1020F")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_10252")

    label("loc_1020F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10227")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_10252")

    label("loc_10227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1023F")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Jump("loc_10252")

    label("loc_1023F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10252")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_10252")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10380")

    ChrTalk(
        0x8,
        (
            "Hey, what're you doing!?\x01",
            "It'll burn again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "E-Eek, sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUmm, may I have a moment?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Hmm... What do you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As you can see, I'm busy now. \x01",
            "Go to the counter if you want to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, that's not it.\x01",
            "You see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1041D")

    label("loc_10380")

    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Oh, do you need something with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Go to the counter if you want to order.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1041D")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah, that gourmet guide, huh.\x01",
            "I indeed heard about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, we're busy but it can't be helped.\x01",
            "Wait at an empty table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll give you a taste of my "Peerless\x01",
            "Fried Rice", my pride and joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FOh, then I'm lookin' forward to this.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000FAlright then, we'll have a seat.\x02",
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
            "Lloyd and the others ate the Peerless Fried Rice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00204F...Delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FMan, you really\x01",
            "are good, Master.\x02\x03",
            "#00304FFried rice this good is a\x01",
            "masterpiece you can only\x01",
            "get at The Old Dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Heheh, naturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Originally, fried rice was my specialty... \x01",
            "I improved it furthermore a few days ago\x01",
            "and there's no way the result wasn't good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F*chomp, chomp*, *munch, munch*...\x01",
            "Wow, you're not kidding...!\x02\x03",
            "#10103FIt's such a simple dish. To think\x01",
            "it could have such deep flavor!\x02\x03",
            "#10109FI made it in the CGF dorm several\x01",
            "times, but when made by a pro,\x01",
            "it's on a whole other level...!\x02",
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
        "#00306FDon't talk with your mouth full.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FDear me, you're bolting it\x01",
            "down with such vigor, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        (
            "Hmm, well if you like\x01",
            "it that much, then it\x01",
            "was worth making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I made a lot, so\x01",
            "how about seconds?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(100)

    ChrTalk(
        0x109,
        "#10109FYes, please!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, Miss Noｱl...\x01",
            "You're like a growing boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it looks like you like it\x01",
            "quite a bit... I think I'll leave\x01",
            "this place's article to you, Noｱl.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D6F")
    SetChrPos(0x8, 17080, 0, 15430, 0)
    BeginChrThread(0x8, 0, 0, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_10D80")

    label("loc_10D6F")

    SetChrPos(0x8, 16000, 0, 15990, 0)

    label("loc_10D80")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_10E2D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_10E4A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_10E5D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_10E70")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_10E8D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_10EA0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_10EBD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_10ED0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_10EED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_10F00")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_10F1D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F1D")

    OP_29(0x80, 0x1, 0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11045")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1103C")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1103C")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_11045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11129")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "We have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_11129")

    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11149")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_1118C")

    label("loc_11149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11161")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jump("loc_1118C")

    label("loc_11161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11179")
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Jump("loc_1118C")

    label("loc_11179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1118C")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_1118C")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2880, 0, -40, 278)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_100EC end

    def Function_53_111B8(): pass

    label("Function_53_111B8")

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
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(I think she'd be\x01",
            "great as a "waitress"\x01",
            "for the pageant.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She looks down,\x01",
            "but... I'll try\x01",
            "asking her.)\x02\x03",
            "#00000FUmm, can I talk to\x01",
            "you for a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...Yes?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked her to participate in\x01",
            "the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "Oh, that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I turned down Roy when\x01",
            "he asked me earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With Rixia gone, I don't\x01",
            "really feel like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FIf that's the case, then it's\x01",
            "not good to force yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHmm... \x01",
            "It seems you're still \x01",
            "havin' trouble with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've been depressed and\x01",
            "it seems it's rubbing off\x01",
            "on the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The customers aren't\x01",
            "enjoying themselves either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell if you are having trouble,\x01",
            "then why not try participating?\x02\x03",
            "#10300FIf you think you might\x01",
            "regret it later, I think\x01",
            "it's better to do it.\x02",
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
        "...Alright, I've decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll do my best and\x01",
            "enliven the event!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whether it's a pageant or a hot bath,\x01",
            "I'll give it everything I've got!\x02",
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
        "#10106FA hot bath...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FUmm, will you take\x01",
            "part in it, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah, I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll be there in time for\x01",
            "the program, so please\x01",
            "contact me when it's time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright, we're counting on you.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118E3")

    ChrTalk(
        0x101,
        (
            "#00003F──Well then, with this we finally have\x01",
            "a sufficient number of participants.\x02\x03",
            "#00000FLet's go to the City Meeting Hall\x01",
            "and report to Roy and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_118E3")

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

    # Function_53_111B8 end

    def Function_54_11931(): pass

    label("Function_54_11931")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120CD")
    OP_93(0x1E, 0x5A, 0x0)
    OP_93(0x1F, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x1F,
        "Baby",
        "*zzz, zzz*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "There, there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Uhuhu, look, Alm.\x01",
            "He's fast asleep.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Yeah, looks that way, Aerie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Looking at him sleeping like this,\x01",
            "he's like an angel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Uh uh, well, a goddess like\x01",
            "you, Aerie gave birth to him,\x01",
            "so it's only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh, Alm...\x02",
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
            "#00003F...U-Umm, I'm\x01",
            "terribly sorry to\x01",
            "interrupt, but...\x02\x03",
            "#00000FAre you Mr. Alm?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11BE3():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_11BE3)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Uhh, who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe Crossbell Police\x01",
            "Special Support Section.\x02\x03",
            "We saw your request and\x01",
            "came to ask about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Ooh, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Thank goodness\x01",
            "you've come!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "That's great, Alm!\x01",
            "With this, we'll finally...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        "Yeah, Aerie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Even though our baby was\x01",
            "just born, I've been giving\x01",
            "so much trouble to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I've been so pathetic\x01",
            "this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Alm! You promised not to\x01",
            "say things like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "The first time we held him,\x01",
            "we both promised, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "No matter what happens...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "You, I, and this\x01",
            "child we both love...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "We'll get through it\x01",
            "together. I remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "I love you, Aerie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "So do I, Alm!\x02",
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
            "#10106FWow... They sure\x01",
            "are lovey-dovey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FLooks like they've been sucked\x01",
            "into their own little world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FL-Looks that way.\x02\x03",
            "#00000F...*ahem*. Excuse us,\x01",
            "but, can we ask\x01",
            "about your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Ah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh, that's right!\x02",
    )

    CloseMessageWindow()

    def lambda_12039():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_12039)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        (
            "Umm... \x01",
            "We'd like you to search\x01",
            "for a certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Sorry to spring this on you,\x01",
            "but can you accept right away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1216D")

    label("loc_120CD")

    OP_93(0x1E, 0x0, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1E,
        "Are you free?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "We'd like you to search\x01",
            "for a certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Sorry to spring this on you,\x01",
            "but can you accept right away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1216D")

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

    # Function_54_11931 end

    def Function_55_121BD(): pass

    label("Function_55_121BD")

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
            "[Accept]\x01",      # 0
            "[Quit]\x01",        # 1
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
        (0, "loc_1221D"),
        (1, "loc_12225"),
        (SWITCH_DEFAULT, "loc_123D4"),
    )


    label("loc_1221D")

    Call(0, 56)
    Jump("loc_123D4")

    label("loc_12225")


    ChrTalk(
        0x101,
        (
            "#00006FUmm... sorry. \x01",
            "We can't do it right away...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237A")

    ChrTalk(
        0x1E,
        (
            "N-No way... You're the\x01",
            "only ones we can count on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Please... For this\x01",
            "adorable child too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1F,
        "Baby",
        "...*ehh, ehh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "There, there, Almin,\x01",
            "it's all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FI-If we somehow get\x01",
            "free, we'll return...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yeah, please do. \x01",
            "We'll be waiting here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123CC")

    label("loc_1237A")


    ChrTalk(
        0x1E,
        "N-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Alright then. Get free\x01",
            "fast and return here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Please...\x02",
    )

    CloseMessageWindow()

    label("loc_123CC")

    SetScenarioFlags(0x19A, 5)
    Jump("loc_123D4")

    label("loc_123D4")

    Return()

    # Function_55_121BD end

    def Function_56_123D5(): pass

    label("Function_56_123D5")


    ChrTalk(
        0x101,
        (
            "#00000FYes, understood.\x01",
            "Please leave it to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Ohhh... Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Man, I'm saved!\x01",
            "I'm really in a\x01",
            "bind here, you see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "That's great, Alm!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1F,
        "Baby",
        "*goo, goo*.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        (
            "Uh, Aerie? \x01",
            "I think Almin's\x01",
            "happy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I think you're right, Alm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F...The request details, please.\x02",
    )

    CloseMessageWindow()

    def lambda_12521():
        OP_93(0x1E, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_12521)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x1F4)

    ChrTalk(
        0x1E,
        "A-Ah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "*ahem*, excuse us. \x01",
            "I'll explain them right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(T-Thanks, Tio...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(At that rate, it would have\x01",
            "never been over no matter\x01",
            "how long we waited.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Hu hu... I wanted\x01",
            "to watch awhile\x01",
            "longer, though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "*ahem*, who I want\x01",
            "you to search for is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "My father, with whom I was\x01",
            "separated when I was very young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSo it's a lifelong separation...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yeah. We live in\x01",
            "Liberl Kingdom, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I actually lived here in\x01",
            "Crossbell when I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "My parents divorced for some\x01",
            "reason, and I went to live with\x01",
            "my grandparents in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I thought I'd never see\x01",
            "my father again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "A few days ago, this child was born\x01",
            "out of our love for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When that happened, Alm said\x01",
            "he wanted to show his father\x01",
            "our child, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "He could have had his problems\x01",
            "with my mother, but to me,\x01",
            "he's my real father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'd really like to tell him about the\x01",
            "happy family we have built together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "And, I convinced my mother\x01",
            "and decided to come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIt's been too long, and you\x01",
            "don't know where your old\x01",
            "man has gone. That right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Yeah, exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "He should have a Residential\x01",
            "Street mansion, but he's\x01",
            "completely disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I heard from my mother,\x01",
            "but ever since the divorce\x01",
            "she hasn't heard from him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "So that's why we're\x01",
            "looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Alm and I have asked around\x01",
            "at a lot of different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Based on that, we know he\x01",
            "moved to Downtown after\x01",
            "being hospitalized, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Every time we go to see\x01",
            "him, he's never there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCould it be that he's\x01",
            "on vacation every\x01",
            "time you stop by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, I don't know, but...\x02\x03",
            "#00000FWe have a lot of experience with both\x01",
            "Residential Street and Downtown.\x02\x03",
            "Elie, do you have any ideas about someone\x01",
            "like that who lived in Residential Street?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1E, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FHmm. I don't think so, but...\x02\x03",
            "#00100FMr. Alm, do you remember\x01",
            "your father's name\x01",
            "and occupation?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "Hmm. I asked my mother about it,\x01",
            "but I don't know if he\x01",
            "still does the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I know his name. \x01",
            "He's "Geval", one of the\x01",
            "city's congressmen.\x02",
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
        "#00005FCongressman Geval...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, that gentleman, eh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1E,
        "Oh... So you know him!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes. We ran into him during\x01",
            "a request not too long ago.\x02\x03",
            "#00100FIn any case, I think we should pay\x01",
            "a visit to his Downtown apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, exactly.\x02\x03",
            "#00000FWe might learn something\x01",
            "about why he's never there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm sure it's fate that\x01",
            "you accepted our request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'll leave everything to you!\x01",
            "Please, find my father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "We're counting on you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
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
            "Quest [Search for Long Lost Father]\x07\x00",
            " started!\x02",
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

    # Function_56_123D5 end

    SaveToFile()

Try(main)
